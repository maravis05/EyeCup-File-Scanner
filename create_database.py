
from main import td
import os
import csv
import datetime
import time


scannedFiles = 0
all_good_files = []

print('..........SCANNING FILES..........')
time.sleep(2)

# goes through every path in target directory and gets list of files
for directory, _, files_list in os.walk(td):
    #directory looks like "c:\user\box\...\phonexx\images"

    # iterates over every file's name in the current path
    for ea_filename in files_list:
        #ea_filename looks like "ADX-....jpg"

        file_path = (directory+"\\"+ea_filename)
        # "c:\td\...\[filename].jpg"
        
        scannedFiles += 1
        if ( scannedFiles % 1000 ) == 0 : print("Scanned ",scannedFiles," files.")
                
        fileAttributes = ea_filename.split("_")

        try:
            if fileAttributes[10]:
                fileAttributes.remove(fileAttributes[10])
        except: pass

        if len(fileAttributes) != 10 or len(fileAttributes[4]) != 2 or len(fileAttributes[5]) != 2:
            print("Skipping",file_path)
            continue
        elif fileAttributes[1] == "000-000":
            print("Skipping",file_path)
            continue
        else: 
            all_good_files.append(fileAttributes+[directory]+[ea_filename])

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

all_good_files.sort()

print("\n....................\n")
print("Scanning complete.\n\n")
print("Scanned", scannedFiles, "Files\n\n")
print("Found", len(all_good_files), "Properly Named Files\n")

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
    print("Database successfully saved to",(os.getenv("userprofile") + "\\desktop\\scan reports"))
except: input("couldn't write database file.")

input("Done. Press enter to quit.")

