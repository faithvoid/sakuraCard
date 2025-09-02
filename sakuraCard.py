import subprocess
import shutil
import os

MEMCARD_TOOL = "/usr/local/bin/ps3mca-tool"
MEMCARD_PATH = "/home/pi/RetroPie/roms/psx/pcsx-card2.mcr"
MEMCARD_BACKUP = "/home/pi/RetroPie/roms/psx/backup"

def dump_card():
    subprocess.run([MEMCARD_TOOL, "dump", "pcsx-card2.mcr"], check=True)
    shutil.copy("pcsx-card2.mcr", MEMCARD_PATH)
    print(f"Playstation memory card dumped and copied to: {MEMCARD_PATH}")

def backup_retro_saves():
    backup_file = os.path.join(MEMCARD_BACKUP, "pcsx-card2-backup.mcr")
    shutil.copy(MEMCARD_PATH, backup_file)
    print(f"Playstation save backed up to: {backup_file}")

def write_back_to_card():
    subprocess.run([MEMCARD_TOOL, "write", MEMCARD_PATH], check=True)
    print("Playstation save written back to memory card.")

# Need to modify this later to dump the memory card on PSX core startup, compare hash values (or check dates if possible?), and if the hash values are different or the memory card save data is newer, treat the memory card (if available) as the primary source of save data, back up the existing memcard file (if detected - need to edit backups to save by date), and dump the physical card into a virtual card.  
dump_card()
backup_retro_saves()
write_back_to_card()
