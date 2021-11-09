
import config
import os
import util


z = ''
yesno = ['Yes','No']

def check_dir(dir):
    if os.path.isdir(dir) == False: 
        input("That directory does not exist.\n[PRESS ENTER]")
        dir = util.get_directory()
    return



while z != 'q':
    os.system('cls')
    print("..........EYECUP FILE SCANNER..........\n")
    choices = ['1 Create File Database','2 Take Backup from Box','3 Move Pixel Files','4 Move Duplicate Timestamps (Creates DB)','5 Move Duplicate Files (Creates DB)']
    a = util.safe_input('What would you like to do?',choices)

    if a == '1':
        b = util.safe_input("Would you like to scan\n"+config.td,yesno)
        if b == 'n': config.td = util.get_directory()
        else: check_dir(config.td)
        import create_database
        create_database
    elif a == '2':
        b = util.safe_input("Would you like to backup\n"+config.td,yesno)
        if b == 'n': config.td = util.get_directory()
        else: check_dir(config.td)
        b = util.safe_input("Backup to\n"+config.dd,yesno)
        if b == 'n': config.dd = util.get_directory()
        else: check_dir(config.dd)
        import take_backup
        take_backup
    elif a == '3':
        config.dd = "D:\\All Pixel Photos"
        b = util.safe_input("Would you like to move Pixel files out of:\n"+config.td,yesno)
        if b == 'n': config.td = util.get_directory()
        else: check_dir(config.td)
        b = util.safe_input("Move files to\n"+config.dd,yesno)
        if b == 'n': config.dd = util.get_directory()
        else: check_dir(config.dd)
        import move_pxl
        move_pxl
    elif a == '4':
        config.dd = "D:\\Duplicate Timestamps"
        b = util.safe_input("Would you like to scan\n"+config.td,yesno)
        if b == 'n': config.td = util.get_directory()
        else: check_dir(config.td)
        b = util.safe_input("Move duplicates to\n"+config.dd,yesno)
        if b == 'n': config.dd = util.get_directory()
        else: check_dir(config.dd)
        config.find_dupe_time = 'yes'
        import create_database
        create_database
        import move_dupe_time
        move_dupe_time
    elif a == '5':
        b = util.safe_input("Would you like to scan\n"+config.td,yesno)
        if b == 'n': config.td = util.get_directory()
        else: check_dir(config.td)
        b = util.safe_input("Move duplicates to\n"+config.dd,yesno)
        if b == 'n': config.dd = util.get_directory()
        else: check_dir(config.dd)
        config.move_dupe_file = 'yes'
        import create_database
        create_database
        

    print("Request completed.\n")
    choices = ['Quit','Restart Application']
    z = util.safe_input("What would you like to do?",choices)
    
    
