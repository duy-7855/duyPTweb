
using System;
using System.Diagnostics;
using System.IO;
using System.Security.Cryptography;
using System.Text;

class Program
{
    private static RSA? rsa;
    private static bool hasPrivateKey = false;

    private static readonly string KeyFolder = "keys";

    static void Main()
    {
        Console.OutputEncoding = Encoding.UTF8;
        Console.InputEncoding = Encoding.UTF8;

        Directory.CreateDirectory(KeyFolder);

        Console.WriteLine("===== CHUONG TRINH RSA-2048 =====");

        while (true)
        {
            Console.WriteLine("\n========== MENU ==========");
            Console.WriteLine("1. Tao cap khoa RSA-2048");
            Console.WriteLine("2. Xuat khoa ra file PEM");
            Console.WriteLine("3. Nhap khoa tu file PEM");
            Console.WriteLine("4. Ma hoa van ban");
            Console.WriteLine("5. Giai ma van ban Base64");
            Console.WriteLine("6. Bam SHA-256");
            Console.WriteLine("7. Ky so RSA-PSS");
            Console.WriteLine("8. Xac minh chu ky");
            Console.WriteLine("9. Do toc do ma hoa/giai ma");
            Console.WriteLine("10. Xem va phan tich file PEM");
            Console.WriteLine("11. Thu ky RSA-PSS hai lan");
            Console.WriteLine("0. Thoat");
            Console.Write("Lua chon: ");

            string? choice = Console.ReadLine();

            try
            {
                switch (choice)
                {
                    case "1":
                        GenerateKeys();
                        break;
                    case "2":
                        ExportKeys();
                        break;
                    case "3":
                        ImportKey();
                        break;
                    case "4":
                        EncryptText();
                        break;
                    case "5":
                        DecryptText();
                        break;
                    case "6":
                        HashText();
                        break;
                    case "7":
                        SignText();
                        break;
                    case "8":
                        VerifySignature();
                        break;
                    case "9":
                        Benchmark();
                        break;
                    case "10":
                        ViewPem();
                        break;
                    case "11":
                        ComparePssSignatures();
                        break;
                    case "0":
                        rsa?.Dispose();
                        Console.WriteLine("Da thoat chuong trinh.");
                        return;
                    default:
                        Console.WriteLine("Lua chon khong hop le.");
                        break;
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Loi: " + ex.Message);
            }
        }
    }

    // 1. Tao cap khoa RSA-2048
    static void GenerateKeys()
    {
        rsa?.Dispose();

        rsa = RSA.Create(2048);
        hasPrivateKey = true;

        Console.WriteLine("\nDa tao cap khoa RSA-2048 thanh cong.");
        Console.WriteLine("Public key: dung de ma hoa va xac minh chu ky.");
        Console.WriteLine("Private key: dung de giai ma va ky so.");
        Console.WriteLine("Hay chon 2 de luu cap khoa ra file PEM.");
    }

    // 2. Xuat khoa ra file PEM
    static void ExportKeys()
    {
        if (!RequirePrivateKey())
            return;

        Directory.CreateDirectory(KeyFolder);

        string publicPath =
            Path.Combine(KeyFolder, "public_key.pem");

        string privatePath =
            Path.Combine(KeyFolder, "private_key.pem");

        File.WriteAllText(
            publicPath,
            rsa!.ExportSubjectPublicKeyInfoPem());

        File.WriteAllText(
            privatePath,
            rsa.ExportPkcs8PrivateKeyPem());

        Console.WriteLine("\nDa xuat khoa thanh cong.");
        Console.WriteLine("Public key: " + publicPath);
        Console.WriteLine("Private key: " + privatePath);
        Console.WriteLine("Khong chia se file private_key.pem.");
    }

    // 3. Nhap khoa tu file PEM
    static void ImportKey()
    {
        Console.Write("Nhap duong dan file PEM: ");

        string path = (Console.ReadLine() ?? "")
            .Trim()
            .Trim('"');

        if (!File.Exists(path))
        {
            Console.WriteLine("Khong tim thay file PEM.");
            return;
        }

        string pem = File.ReadAllText(path);

        RSA newRsa = RSA.Create();

        try
        {
            newRsa.ImportFromPem(pem);
        }
        catch (Exception ex) when (
            ex is CryptographicException ||
            ex is ArgumentException)
        {
            newRsa.Dispose();
            Console.WriteLine("Khong the doc khoa PEM: " + ex.Message);
            return;
        }

        bool importedPrivateKey;

        try
        {
            RSAParameters parameters = newRsa.ExportParameters(true);
            importedPrivateKey = parameters.D != null;
        }
        catch (CryptographicException)
        {
            importedPrivateKey = false;
        }

        rsa?.Dispose();
        rsa = newRsa;
        hasPrivateKey = importedPrivateKey;

        Console.WriteLine("\nNhap khoa thanh cong.");
        Console.WriteLine($"Kich thuoc khoa: {rsa.KeySize} bit");

        if (hasPrivateKey)
        {
            Console.WriteLine("Loai khoa: PRIVATE KEY.");
            Console.WriteLine("Co the ma hoa, giai ma va ky so.");
        }
        else
        {
            Console.WriteLine("Loai khoa: PUBLIC KEY.");
            Console.WriteLine("Co the ma hoa va xac minh chu ky.");
            Console.WriteLine("Khong the giai ma hoac ky so.");
        }
    }

    // Kiem tra da co khoa hay chua
    static bool RequireKey()
    {
        if (rsa == null)
        {
            Console.WriteLine(
                "Hay tao cap khoa (chon 1) hoac nhap khoa PEM (chon 3).");

            return false;
        }

        return true;
    }

    // Kiem tra co khoa rieng hay khong
    static bool RequirePrivateKey()
    {
        if (!RequireKey())
            return false;

        if (!hasPrivateKey)
        {
            Console.WriteLine(
                "Thao tac nay can private key. Hay tao khoa hoac nhap private_key.pem.");

            return false;
        }

        return true;
    }

    // Nhap van ban va kiem tra gioi han RSA-OAEP-SHA256
    static byte[] ReadInputBytes()
    {
        Console.Write("Nhap noi dung: ");

        string input = Console.ReadLine() ?? "";
        byte[] data = Encoding.UTF8.GetBytes(input);

        if (data.Length == 0)
        {
            throw new InvalidOperationException(
                "Noi dung khong duoc de trong.");
        }

        // RSA-2048 + OAEP-SHA256: toi da 190 byte
        if (data.Length > 190)
        {
            throw new InvalidOperationException(
                $"Van ban co {data.Length} byte, vuot gioi han 190 byte.");
        }

        return data;
    }

    // 4. Ma hoa van ban
    static void EncryptText()
    {
        if (!RequireKey())
            return;

        byte[] data = ReadInputBytes();

        byte[] encrypted = rsa!.Encrypt(
            data,
            RSAEncryptionPadding.OaepSHA256);

        string base64 = Convert.ToBase64String(encrypted);

        File.WriteAllText("ciphertext.txt", base64);

        Console.WriteLine("\nBan ma Base64:");
        Console.WriteLine(base64);
        Console.WriteLine("Da luu ban ma vao ciphertext.txt.");
    }

    // 5. Giai ma van ban
    static void DecryptText()
    {
        if (!RequirePrivateKey())
            return;

        Console.Write(
            "Nhap ban ma Base64 (Enter de doc ciphertext.txt): ");

        string base64 = (Console.ReadLine() ?? "").Trim();

        if (string.IsNullOrWhiteSpace(base64))
        {
            if (!File.Exists("ciphertext.txt"))
            {
                Console.WriteLine("Khong tim thay ciphertext.txt.");
                return;
            }

            base64 = File.ReadAllText("ciphertext.txt").Trim();
        }

        byte[] encrypted = Convert.FromBase64String(base64);

        byte[] decrypted = rsa!.Decrypt(
            encrypted,
            RSAEncryptionPadding.OaepSHA256);

        Console.WriteLine("\nNoi dung giai ma:");
        Console.WriteLine(Encoding.UTF8.GetString(decrypted));
    }

    // 6. Bam SHA-256
    static void HashText()
    {
        Console.Write("Nhap van ban can bam SHA-256: ");

        string input = Console.ReadLine() ?? "";

        byte[] hash = SHA256.HashData(
            Encoding.UTF8.GetBytes(input));

        Console.WriteLine("\nSHA-256:");
        Console.WriteLine(
            Convert.ToHexString(hash).ToLowerInvariant());

        Console.WriteLine("Do dai ma bam: 32 byte (256 bit).");
    }

    // 7. Ky so RSA-PSS
    static void SignText()
    {
        if (!RequirePrivateKey())
            return;

        byte[] data = ReadInputBytes();

        byte[] signature = rsa!.SignData(
            data,
            HashAlgorithmName.SHA256,
            RSASignaturePadding.Pss);

        string base64 = Convert.ToBase64String(signature);

        File.WriteAllText("signature.txt", base64);

        Console.WriteLine("\nChu ky RSA-PSS (Base64):");
        Console.WriteLine(base64);
        Console.WriteLine("Da luu chu ky vao signature.txt.");
    }

    // 8. Xac minh chu ky
    static void VerifySignature()
    {
        if (!RequireKey())
            return;

        Console.Write("Nhap van ban goc: ");
        string text = Console.ReadLine() ?? "";

        Console.Write(
            "Nhap chu ky Base64 (Enter de doc signature.txt): ");

        string base64 = (Console.ReadLine() ?? "").Trim();

        if (string.IsNullOrWhiteSpace(base64))
        {
            if (!File.Exists("signature.txt"))
            {
                Console.WriteLine("Khong tim thay signature.txt.");
                return;
            }

            base64 = File.ReadAllText("signature.txt").Trim();
        }

        byte[] data = Encoding.UTF8.GetBytes(text);
        byte[] signature = Convert.FromBase64String(base64);

        bool valid = rsa!.VerifyData(
            data,
            signature,
            HashAlgorithmName.SHA256,
            RSASignaturePadding.Pss);

        Console.WriteLine(valid
            ? "Chu ky HOP LE."
            : "Chu ky KHONG HOP LE.");
    }

    // 9. Do toc do ma hoa va giai ma
    static void Benchmark()
    {
        if (!RequirePrivateKey())
            return;

        byte[] data = ReadInputBytes();

        Stopwatch sw = Stopwatch.StartNew();

        byte[] encrypted = rsa!.Encrypt(
            data,
            RSAEncryptionPadding.OaepSHA256);

        sw.Stop();
        double encryptMs = sw.Elapsed.TotalMilliseconds;

        sw.Restart();

        byte[] decrypted = rsa.Decrypt(
            encrypted,
            RSAEncryptionPadding.OaepSHA256);

        sw.Stop();
        double decryptMs = sw.Elapsed.TotalMilliseconds;

        bool correct = CryptographicOperations.FixedTimeEquals(
            data, decrypted);

        Console.WriteLine("\n===== KET QUA DO TOC DO =====");
        Console.WriteLine($"Du lieu goc: {data.Length} byte");
        Console.WriteLine($"Ban ma: {encrypted.Length} byte");
        Console.WriteLine($"Thoi gian ma hoa: {encryptMs:F4} ms");
        Console.WriteLine($"Thoi gian giai ma: {decryptMs:F4} ms");
        Console.WriteLine($"Du lieu giai ma dung: {correct}");
    }

    // 10. Phan tich file PEM
    static void ViewPem()
    {
        Console.Write("Nhap duong dan file PEM: ");

        string path = (Console.ReadLine() ?? "")
            .Trim()
            .Trim('"');

        if (!File.Exists(path))
        {
            Console.WriteLine("Khong tim thay file PEM.");
            return;
        }

        string pem = File.ReadAllText(path);

        using RSA tempRsa = RSA.Create();

        try
        {
            tempRsa.ImportFromPem(pem);
        }
        catch (Exception ex) when (
            ex is CryptographicException ||
            ex is ArgumentException)
        {
            Console.WriteLine("File PEM khong hop le: " + ex.Message);
            return;
        }

        RSAParameters publicParams;

        try
        {
            publicParams = tempRsa.ExportParameters(false);
        }
        catch (CryptographicException ex)
        {
            Console.WriteLine("Khong doc duoc tham so khoa: " + ex.Message);
            return;
        }

        bool containsPrivateKey;

        try
        {
            RSAParameters privateParams = tempRsa.ExportParameters(true);
            containsPrivateKey = privateParams.D != null;
        }
        catch (CryptographicException)
        {
            containsPrivateKey = false;
        }

        Console.WriteLine("\n===== PHAN TICH FILE PEM =====");
        Console.WriteLine($"Kich thuoc khoa: {tempRsa.KeySize} bit");

        Console.WriteLine("Loai khoa: " +
            (containsPrivateKey ? "PRIVATE KEY" : "PUBLIC KEY"));

        Console.WriteLine("\nn (Modulus) - HEX:");
        Console.WriteLine(Convert.ToHexString(publicParams.Modulus!));
        Console.WriteLine("Y nghia: n = p * q, modulus cua khoa RSA.");

        Console.WriteLine("\ne (Public exponent) - HEX:");
        Console.WriteLine(Convert.ToHexString(publicParams.Exponent!));
        Console.WriteLine("Y nghia: so mu cong khai.");

        Console.WriteLine("\nd (Private exponent):");

        if (containsPrivateKey)
        {
            Console.WriteLine(
                "Co tham so d trong khoa rieng. Gia tri duoc an de bao mat.");
        }
        else
        {
            Console.WriteLine(
                "Khong co d. File nay chi chua khoa cong khai.");
        }

        Console.WriteLine("\nPhan tich PEM hoan tat.");
        Console.WriteLine(
            "Luu y: Khong chia se private_key.pem hoac gia tri khoa rieng.");
    }

    // 11. Ky hai lan bang RSA-PSS
    static void ComparePssSignatures()
    {
        if (!RequirePrivateKey())
            return;

        Console.Write("Nhap noi dung can ky hai lan: ");

        string text = Console.ReadLine() ?? "";
        byte[] data = Encoding.UTF8.GetBytes(text);

        if (data.Length == 0)
        {
            Console.WriteLine("Noi dung khong duoc de trong.");
            return;
        }

        if (data.Length > 190)
        {
            Console.WriteLine(
                "Noi dung vuot qua 190 byte. Hay nhap van ban ngan hon.");
            return;
        }

        byte[] signature1 = rsa!.SignData(
            data,
            HashAlgorithmName.SHA256,
            RSASignaturePadding.Pss);

        byte[] signature2 = rsa.SignData(
            data,
            HashAlgorithmName.SHA256,
            RSASignaturePadding.Pss);

        bool different =
            !CryptographicOperations.FixedTimeEquals(
                signature1, signature2);

        bool valid1 = rsa.VerifyData(
            data,
            signature1,
            HashAlgorithmName.SHA256,
            RSASignaturePadding.Pss);

        bool valid2 = rsa.VerifyData(
            data,
            signature2,
            HashAlgorithmName.SHA256,
            RSASignaturePadding.Pss);

        Console.WriteLine("\n===== KET QUA THU RSA-PSS =====");

        Console.WriteLine("\nChu ky lan 1 (Base64):");
        Console.WriteLine(Convert.ToBase64String(signature1));

        Console.WriteLine("\nChu ky lan 2 (Base64):");
        Console.WriteLine(Convert.ToBase64String(signature2));

        Console.WriteLine("\nHai chu ky khac nhau: " + different);
        Console.WriteLine("Chu ky 1 hop le: " + valid1);
        Console.WriteLine("Chu ky 2 hop le: " + valid2);

        File.WriteAllText(
            "signature.txt",
            Convert.ToBase64String(signature1));

        Console.WriteLine("Da luu chu ky lan 1 vao signature.txt.");
    }
}
