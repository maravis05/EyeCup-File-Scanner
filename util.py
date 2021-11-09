
import os
import shutil
#import config

moved_files = 0
deleted_files = 0

def safe_input(prompt,options):
    
    first_letters = []
    print(prompt)
    for option in options:
        first_letter = option[0]
        first_letters.append(first_letter.casefold())
        print("("+option[0].upper()+")"+option[1:(len(option)+1)])
    a = str(input("?"))
    a = a.casefold()
    if a not in first_letters:
        print(a, "is not an option.")
        a = safe_input(prompt,options)
        return a
    else: return a

def get_directory():
        
    desired_dir = input("Please enter desired directory:\n")
    if os.path.isdir(desired_dir) == False: 
        input("That directory does not exist.\n[PRESS ENTER]")
        get_directory()
    else: return desired_dir


def copy_this_file(source_file,dest_dir):
    os.makedirs(dest_dir,exist_ok=True)
    shutil.copy2(source_file,dest_dir)

def move_this_file(source_file,dest_dir,filename):
    global moved_files
    global deleted_files
    os.makedirs(dest_dir,exist_ok=True)

    try:
        if os.path.isfile(dest_dir+"\\"+filename):
            shutil.copy2(source_file,dest_dir)
            os.remove(source_file)
            deleted_files =+ 1
            print((dest_dir+"\\"+filename),"already exists. Deleting",source_file)
            return
        else:
            shutil.move(source_file,dest_dir)
            print("moved",source_file)
            moved_files =+ 1
    except: pass

def enter():
    return input("[PRESS ENTER TO CONTINUE]")

