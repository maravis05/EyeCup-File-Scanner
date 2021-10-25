
import os
import shutil
import config

copied_files = 0

for directory, _, files_list in os.walk(config.td):
    #directory looks like "c:\user\box\...\phonexx\images"

    for ea_filename in files_list:
        #ea_filename looks like "ADX-....jpg"

        file_path = (directory+"\\"+ea_filename)
        #file_path looks like "c:\td\...\[filename].jpg"
                
        file_attributes = ea_filename.split("_")
        
        try:
            if file_attributes[10]: file_attributes.remove(file_attributes[10])
        except: pass

        if len(file_attributes) != 10:
            #print("Skipping",file_path)
            continue
        elif file_attributes[1] == "000-000":
            #print("Skipping",file_path)
            continue
        else:
            d_path = config.dd+"\\"+file_attributes[0]+"\\"+file_attributes[1]+"\\"+file_attributes[2]
            os.makedirs(d_path,exist_ok=True)
            if os.path.isfile(d_path+"\\"+ea_filename) != True:
                shutil.copy2(file_path,d_path)
                print("Copied",file_path)
                copied_files += 1
                if (copied_files % 1000) == 0 : print("Copied",copied_files,"files.")
            else: continue


