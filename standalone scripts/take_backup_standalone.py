
import os
import shutil

scanned_files = 0
copied_files = 0
td = (os.getenv("userprofile")+"\\Box\\Alderya EyeCup Images")
dd = "D:\\Aldeyra EyeCup Photos"

for directory, _, files_list in os.walk(td):
    for ea_filename in files_list:
        
        scanned_files += 1
        if ( scanned_files % 1000 ) == 0 : print("Scanned ",scanned_files," files.")

        file_path = (directory+"\\"+ea_filename)
        file_attributes = ea_filename.split("_")
        try:
            if file_attributes[10]: file_attributes.remove(file_attributes[10])
        except: pass
        if len(file_attributes) != 10:
            continue
        elif file_attributes[1] == "000-000":
            continue
        else:
            dest_dir = dd+"\\"+file_attributes[0]+"\\"+file_attributes[1]+"\\"+file_attributes[2]
            if os.path.isfile(dest_dir+"\\"+ea_filename) != True:
                os.makedirs(dest_dir,exist_ok=True)
                shutil.copy2(file_path,dest_dir)
                
            else: continue
            continue

