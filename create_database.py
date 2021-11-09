
import config
import os
import csv
import datetime
import time
import util

scanned_files = 0
all_good_files = []
stamp_to_file = {}


def find_first(timestamp):
    #get first instance of duplicate timestamp
    global all_good_files
    for ea_file in all_good_files:
        if ea_file[9] == timestamp: return ea_file

def dupe_dict(timestamp,file):
    global all_good_files
    global stamp_to_file
    #creating a dictionary of duplicate timestamps
    for ea_file in all_good_files:
        if timestamp in ea_file:
            if timestamp not in stamp_to_file:
                stamp_to_file[timestamp] = [find_first(timestamp)]
            stamp_to_file[timestamp].append(file)

def move_dupe_file(file,file_path,filename):
    global all_good_files
    for ea_file in all_good_files:
        if filename in ea_file:
            dest_dir = config.dd+"\\"+file[0]+"\\"+file[1]+"\\"+file[2]
            util.move_this_file(file_path,dest_dir,filename)
            



print('..........SCANNING FILES..........')
time.sleep(2)

# goes through every path in target directory and gets list of files
for directory, _, files_list in os.walk(config.td):
    #directory looks like "c:\user\box\...\phonexx\images"

    # iterates over every file's name in the current path
    for ea_filename in files_list:
        #ea_filename looks like "ADX-....jpg"

        file_path = (directory+"\\"+ea_filename)
        # "c:\td\...\[filename].jpg"
        
        scanned_files += 1
        if ( scanned_files % 1000 ) == 0 : print("Scanned ",scanned_files," files.")
                
        file_attributes = ea_filename.split("_")

        try:
            if len(file_attributes) > 10:
                file_attributes.remove(file_attributes[10])
        except: pass

        if len(file_attributes) != 10:
            print("Skipping",file_path)
            continue
        elif file_attributes[1] == "000-000":
            util.move_this_file(file_path,config.dd+"\\000-000\\"+directory.replace(config.td, ""),ea_filename)
            continue
        else:
            file_attributes = file_attributes+[directory]+[ea_filename]
            
            if config.find_dupe_time == 'yes': dupe_dict(file_attributes[9],file_attributes)
            if config.move_dupe_file == 'yes': move_dupe_file(file_attributes,file_path,ea_filename)

            all_good_files.append(file_attributes)
            all_good_files.sort()


        

        # protocol = fileAttributes[0]
        # patient = fileAttributes[1]
        # visit = fileAttributes[2]
        # study = fileAttributes[3]
        # timeEntry = fileAttributes[4]
        # eye = fileAttributes[5]
        # view = fileAttributes[6]
        # phone = fileAttributes[7]
        # technician = fileAttributes[8]
        # timestamp = fileAttributes[9]

        # print("This file looks like:\n")
        # print(fileAttributes+[fullPath]+[eachName])
        # input("Pausing...")



print("\n....................\n")
print("Scanning complete.\n")
print("Scanned", scanned_files, "Files\n")
print("Found", len(all_good_files), "Properly Named Files\n")
print("Moved",util.moved_files, "Files\n")
print("Removed",util.deleted_files,"Duplicate Files\n")

current = datetime.datetime.now()
report_time = (str(current.year)+"-"+str(current.month)+"-"+str(current.day)+" "+str(current.hour)+"."+str(current.minute)+"."+str(current.second))
header = [
    "PROTOCOL",
    "PATIENT",
    "VISIT",
    "STUDY",
    "TIME ENTRY",
    "EYE",
    "VIEW",
    "PHONE",
    "TECHNICIAN",
    "TIMESTAMP",
    "FILE PATH",
    "FILENAME",
]

try:
    os.mkdir(os.getenv("userprofile") + "\\desktop\\scan reports")
except: pass

try:
    with open((os.getenv("userprofile") + "\\desktop\\scan reports\\database "+str(report_time)+".csv"), "w", newline="") as report:
        f = csv.writer(report)
        f.writerow(header)
        f.writerows(all_good_files)
    print("Database successfully saved to",(os.getenv("userprofile") + "\\desktop\\scan reports\n"))
except: input("couldn't write database file.")



