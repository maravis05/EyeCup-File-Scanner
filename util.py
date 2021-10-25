
import os

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

