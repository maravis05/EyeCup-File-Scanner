

from create_database import all_good_files
import csv
import util
import os

dest = (os.getenv("userprofile")+"\\Box\\Alderya EyeCup Images\\019 test")



with open("c:\\temp\\move.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader:
        for ea_file in all_good_files:
            path = ea_file[9]+"\\"+ea_file[10]
            ea_file.remove(ea_file[7:])
            if row == ea_file:
                util.copy_this_file(path,dest)
            
