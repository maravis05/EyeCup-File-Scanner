
import config
import os
import util



yesno = ['Yes','No']

while True:
    os.system('cls')
    print("..........EYECUP FILE SCANNER..........\n")
    choices = ['1 Create File Database','2 Take Backup from Box','3 Move Pixel Files']
    a = util.safe_input('What would you like to do?',choices)

    if a == '1':
        b = util.safe_input("Would you like to scan\n"+config.td,yesno)
        if b == 'n': config.td = util.get_directory()
        import create_database
        create_database
    elif a == '2':
        b = util.safe_input("Would you like to backup\n"+config.td,yesno)
        if b == 'n': config.td = util.get_directory()
        b = util.safe_input("Backup to\n"+config.dd,yesno)
        if b == 'n': config.dd = util.get_directory()
        import take_backup
        take_backup
    elif a == '3':
        b = util.safe_input("Would you like to move Pixel files out of:\n"+config.td,yesno)
        if b == 'n': config.td = util.get_directory()
        config.dd = "D:\\All Pixel Photos"
        b = util.safe_input("Move files to\n"+config.dd,yesno)
        if b == 'n': config.dd = util.get_directory()
        import move_pxl
        move_pxl
