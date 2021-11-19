

from create_database import all_good_files
import csv
import util
import os

dest = (os.getenv("userprofile")+"\\Box\\Alderya EyeCup Images\\019 test")


with open("c:\\temp\\database") as database:
    database = csv.reader(database, delimiter=',')

with open("c:\\temp\\move.csv") as csv_file:
    find_these = csv.reader(csv_file, delimiter=',')
    
    for row in find_these:
        for ea_file in database:
            path = ea_file[10]+"\\"+ea_file[11]
            new_file = ea_file[:7]
            if row == new_file:
                util.copy_this_file(path,dest)
            
