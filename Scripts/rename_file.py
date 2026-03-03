#mporting os module

import os

# Function to rename multiple files

def rename_file(file_path):
  
 os.chdir(file_path)
 count = 1
 for f in os.listdir():

    f_name, f_ext = os.path.splitext(f)

    #f_title, f_course, f_num = f_name.split('-')

    f_name = f_name.strip()

    new_name = '{}-{}{}'.format(count, f_name, f_ext)

    print(new_name)

    os.rename(f, new_name)
    count=count+1

if __name__ == '__main__':

    # Calling main() function
    rename_file('test')

