
import os
import csv

all_good_files = []
scanned_files = 0

for directory, _, files_list in os.walk(os.getenv("userprofile")+"\\Box\\Alderya EyeCup Images"):
    for ea_filename in files_list:

        scanned_files += 1
        if ( scanned_files % 1000 ) == 0 : print("Scanned ",scanned_files," files.")

        file_attributes = ea_filename.split("_")
        try:
            if len(file_attributes) > 10:
                file_attributes.remove(file_attributes[10])
        except: pass

        if len(file_attributes) != 10:
            continue
        elif file_attributes[1] == "000-000":
            continue
        else:
            file_attributes = file_attributes+[directory]+[ea_filename]
            all_good_files.append(file_attributes)
            all_good_files.sort()
            

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
    with open(os.getenv("userprofile")+"\\Box\\New EyeCup Project\\!photodatabase.csv", "w", newline="") as report:
        f = csv.writer(report)
        f.writerow(header)
        f.writerows(all_good_files)
except: input("couldn't write database file.")



