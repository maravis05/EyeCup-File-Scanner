

#from create_database import all_good_files
import csv
import os
import shutil
moved = 0
total = 0
not_moved = []

dest = (os.getenv("userprofile")+"\\Box\\Alderya EyeCup Images\\019 J-Chin missing")

with open("c:\\temp\\J-Chin Missing.csv") as csv_file:
    find_these = csv.reader(csv_file, delimiter=',')
    for row in find_these:
        good = 'no'

        with open("c:\\temp\\database.csv") as database:
            database = csv.reader(database, delimiter=',')
            total += 1

            for ea_file in database:
                new_file = ea_file[:7]
                path = ea_file[10]+"\\"+ea_file[11]
                if row == new_file:
                    shutil.copy2(path,dest)
                    moved += 1
                    good = 'yes'
                    break
        if good == 'no': print(row,"not found")

            
            

