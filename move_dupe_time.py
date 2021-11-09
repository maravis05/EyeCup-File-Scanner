

from create_database import stamp_to_file
import util

#stamp_to_file entry looks like timestamp: [[file1,attributes],[file2,attributes]]



for ea_timestamp, files in stamp_to_file.items():
    print(files)
    util.enter
    files.sort()
    print(files)
    util.enter

    # i = len(files)-1
    # for i in range(len(files)-1):
        

