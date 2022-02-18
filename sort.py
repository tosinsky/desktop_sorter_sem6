import glob
import os
import shutil

desktop_path = "C:/Users/pc0/Desktop"

def sort(path):
    os.chdir(path)
    ASU_list = glob.glob('asu_*')
    ABD_list = glob.glob('abd_*')
    ETOS_list = glob.glob('etos_*')
    INCZ_list = glob.glob('incz_*')
    SSID_list = glob.glob('ssid_*')
    TP_list = glob.glob('tp_*')

    for file in ASU_list:
        seperated_name = file.split("_")
        shutil.move("C:/Users/pc0/Desktop/"+file, "C:/Users/pc0/Desktop/SEM6/ASU/"+seperated_name[1])
    for file in ABD_list:
        seperated_name = file.split("_")
        shutil.move("C:/Users/pc0/Desktop/"+file, "C:/Users/pc0/Desktop/SEM6/ABD/"+seperated_name[1])
    for file in ETOS_list:
        seperated_name = file.split("_")
        shutil.move("C:/Users/pc0/Desktop/"+file, "C:/Users/pc0/Desktop/SEM6/ETOS/"+seperated_name[1])
    for file in INCZ_list:
        seperated_name = file.split("_")
        shutil.move("C:/Users/pc0/Desktop/"+file, "C:/Users/pc0/Desktop/SEM6/INCZ/"+seperated_name[1])
    for file in SSID_list:
        seperated_name = file.split("_")
        shutil.move("C:/Users/pc0/Desktop/"+file, "C:/Users/pc0/Desktop/SEM6/SSID/"+seperated_name[1])
    for file in TP_list:
        seperated_name = file.split("_")
        shutil.move("C:/Users/pc0/Desktop/"+file, "C:/Users/pc0/Desktop/SEM6/TP/"+seperated_name[1])

if __name__ == '__main__':
    path = input()
    if path == "":
        sort(desktop_path)
    else:
        sort(path)

