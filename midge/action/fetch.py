
import os
import shutil

str_folder_destination = r'C:\Users\daner\Downloads'
str_folder_prefix = 'Files - '
str_folder_source = r'C:\Users\daner\Downloads'
str_protocol_ifexist = 'rename'

def do_move(target, destination):
    try:
        os.makedirs(destination)
    except FileExistsError:
        print("Folder already exists: " + destination)
    except OSError as e:
        print("Failed to create folder " + destination + ": " + e)
        exit()
    finally:
        if str_protocol_ifexist == 'overwrite':
            shutil.move(target, destination)
        elif str_protocol_ifexist == 'rename':
            int_counter = 1
            destination_new = destination + '\\' + os.path.basename(target)
            while os.path.exists(destination_new):
                int_counter = int_counter + 1
                destination_new = os.path.splitext(destination_new)[0] + " Copy " + str(int_counter) + os.path.splitext(destination_new)[1]
            shutil.move(target, destination_new)

def do_move_check(target, destination):
    boolean_proceed = True
    if os.path.isfile(target):
        str_folder_destination_new = destination + '\\' + str_folder_prefix + os.path.splitext(str_entry)[1][1:].upper()
    elif os.path.isdir(target):
        str_folder_destination_new = destination + r'\Folder'
        if os.path.basename(target) == 'Folder' or os.path.basename(target)[0:len(str_folder_prefix)] == str_folder_prefix:
            print("Cannot proceed moving the folder '" + target)
            boolean_proceed = False
    if boolean_proceed:
        do_move(target, str_folder_destination_new)

try:
    for str_entry in os.listdir(str_folder_source):
        str_entry_abs = str_folder_source + '\\' + str_entry
        do_move_check(str_entry_abs, str_folder_destination)
except FileNotFoundError:
    print("Directory not found for " + str_folder_source)
except PermissionError:
    print("Permission denied for " + str_folder_source)