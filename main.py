
import config
import os
import util


#need to separate scanning function and database building
#want the database to be built after duplicates have been removed



z = ''
yesno = ['Yes','No']

def check_dir(dir):
    if os.path.isdir(dir) == False: 
        print("That directory does not exist.")
        return util.get_directory()
    return dir
    



while z != 'q':
    config.deleted_files = 0
    config.moved_files = 0
    os.system('cls')
    print("..........EYECUP FILE SCANNER..........\n")
    choices = ['1 Create File Database','2 Take Backup from Box','3 Move Pixel Files','4 Move Duplicate Files, Create DB','5 Move Duplicate Files, Move Duplicate Timestamps, Create DB']
    a = util.safe_input('What would you like to do?',choices)

    if a == '1':
        config.td = (os.getenv("userprofile")+"\\Box\\Alderya EyeCup Images")

        b = util.safe_input("Would you like to scan\n"+config.td,yesno)
        if b == 'n': config.td = util.get_directory()
        else: config.td = check_dir(config.td)
        import create_database
        create_database

    elif a == '2':
        config.td = (os.getenv("userprofile")+"\\Box\\Alderya EyeCup Images")
        config.dd = dd = "D:\\Aldeyra EyeCup Photos"
        
        b = util.safe_input("Would you like to backup\n"+config.td,yesno)
        if b == 'n': config.td = util.get_directory()
        else: config.td = check_dir(config.td)
        b = util.safe_input("Backup to\n"+config.dd,yesno)
        if b == 'n': config.dd = util.get_directory()
        else: config.dd = check_dir(config.dd)
        import take_backup
        take_backup

    elif a == '3':
        config.td = (os.getenv("userprofile")+"\\Box\\Alderya EyeCup Images")
        config.dd = "D:\\All Pixel Photos"

        b = util.safe_input("Would you like to move Pixel files out of:\n"+config.td,yesno)
        if b == 'n': config.td = util.get_directory()
        else: config.td = check_dir(config.td)
        b = util.safe_input("Move files to\n"+config.dd,yesno)
        if b == 'n': config.dd = util.get_directory()
        else: config.dd = check_dir(config.dd)
        import move_pxl
        move_pxl

    elif a == '4':
        config.td = (os.getenv("userprofile")+"\\Box\\Alderya EyeCup Images")
        config.dd = dd = "D:\\Aldeyra EyeCup Photos"

        b = util.safe_input("Would you like to scan\n"+config.td,yesno)
        if b == 'n': config.td = util.get_directory()
        else: config.td = check_dir(config.td)
        b = util.safe_input("Move duplicates to\n"+config.dd,yesno)
        if b == 'n': config.dd = util.get_directory()
        else: config.dd = check_dir(config.dd)
        config.move_dupe_file = 'yes'
        import create_database
        create_database

    elif a == '5':
        config.td = (os.getenv("userprofile")+"\\Box\\Alderya EyeCup Images")
        config.dd = "D:\\Duplicate Timestamps"

        b = util.safe_input("Would you like to scan\n"+config.td,yesno)
        if b == 'n': config.td = util.get_directory()
        else: config.td = check_dir(config.td)
        b = util.safe_input("Move duplicates to\n"+config.dd,yesno)
        if b == 'n': config.dd = util.get_directory()
        else: config.dd = check_dir(config.dd)
        config.find_dupe_time = 'yes'
        import create_database
        create_database
        import move_dupe_time
        move_dupe_time
    
        

    print("Request completed.\n")
    choices = ['Quit','Restart Application']
    z = util.safe_input("What would you like to do?",choices)
    
    
