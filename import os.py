import os
import shutil
from datetime import datetime

source_folder = "D:/test1" # < hier ändert ihr den Ordnerpfad der Kopiert bzw n Backup von gemacht werden soll
backup_base_folder = "D:/test2" # < hier ändert ihr den Zielpfad wo des Backup hin soll

os.makedirs(backup_base_folder, exist_ok=True)

timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
target_folder = os.path.join(backup_base_folder, f"backup_{timestamp}")

try:
    shutil.copytree(source_folder, target_folder)
    print(f"Geht: {target_folder}")
except FileExistsError:
    print(f"Ordner schon da: {target_folder}")
except Exception as e:
    print(f"Geht net: {e}")