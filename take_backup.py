
import os
import util
import config

scanned_files = 0
copied_files = 0

for directory, _, files_list in os.walk(config.td):
    #directory looks like "c:\user\box\...\phonexx\images"

    for ea_filename in files_list:
        #ea_filename looks like "ADX-....jpg"

        file_path = (directory+"\\"+ea_filename)
        #file_path looks like "c:\td\...\[filename].jpg"
                
        file_attributes = ea_filename.split("_")

        scanned_files += 1
        if ( scanned_files % 1000 ) == 0 : print("Scanned ",scanned_files," files.")
        
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
            dest_dir = config.dd+"\\"+file_attributes[0]+"\\"+file_attributes[1]+"\\"+file_attributes[2]
            
            if os.path.isfile(dest_dir+"\\"+ea_filename) != True:
                util.copy_this_file(file_path,dest_dir)
                print("Copied",ea_filename)
                copied_files += 1
                if (copied_files % 1000) == 0 : print("Copied",copied_files,"files.")
            else: continue
            continue


