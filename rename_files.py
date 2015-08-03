import os

def rename_files():
    # get the names from folder
    file_list = os.listdir(r"/home/castor/Documents/Nanodegree/FullStack/Example/secretmessage")
    print(file_list)

    saved_path = os.getcwd()
    print ("the directory is " + saved_path)
    os.chdir(r"/home/castor/Documents/Nanodegree/FullStack/Example/secretmessage")

    # for each file, rename file
    for file_name in file_list:
        print ("Old name is " + file_name)
        os.rename(file_name,file_name.translate(None,"0123456789"))
        print ("New name is " + file_name)

    os.chdir(saved_path)

rename_files()
