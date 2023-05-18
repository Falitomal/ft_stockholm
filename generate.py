import os
import random
from pathlib import Path
#Variables waranacry
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

def main():
    """crear 200 archivos en la carpeta home/test/infection"""
    path = DEFAULT_DIR

    if not os.path.exists(path):
        os.makedirs(path)
        print("Carpeta creada")
    for i in range(0, 200):
        name = str(i) + random.choice(exts_wanacry)
        file_path = os.path.join(path, name)
        with open(file_path, "w") as file:
            file.write("Hola mundo")
        print("Archivo " + name + " creado en " + path)
    else:
        print("Carpeta ya existe")
    
    path = path + "/subfolder/"
    if not os.path.exists(path):
            os.makedirs(path)
            print("Carpeta creada")
    for i in range(0, 200):
        name = str(i) + random.choice(exts_wanacry)
        file_path = os.path.join(path, name)
        with open(file_path, "w") as file:
            file.write("Hola mundo")
        print("Archivo " + name + " creado en " + path)
    else:
        print("SubCarpeta ya existe")
    
    
if __name__ == '__main__':
    main()