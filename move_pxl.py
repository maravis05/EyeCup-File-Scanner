
import os
import util
import config

scanned_files = 0
moved_files = 0

for directory, _, files_list in os.walk(config.td):
    #directory looks like "c:\user\box\...\phonexx\images"

    for ea_filename in files_list:
        #ea_filename looks like "ADX-....jpg"

        file_path = (directory+"\\"+ea_filename)
        #file_path looks like "c:\td\...\[filename].jpg"

        relative_dir = directory.replace(config.td, "")
        # looks like "\phonexx\images"                
        
        file_attributes = ea_filename.split("_")

        scanned_files += 1
        if ( scanned_files % 1000 ) == 0 : print("Scanned ",scanned_files," files.")
        
        if file_attributes[0] == 'PXL':
            dest_dir = config.dd+"\\"+relative_dir
            util.move_this_file(file_path,dest_dir,ea_filename)
            moved_files += 1
            if (moved_files % 1000) == 0 : print("Moved",moved_files,"files.")
        else: continue

