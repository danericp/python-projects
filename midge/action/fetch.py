
import argparse
import os
import shutil

str_folder_destination = r'C:\Users\daner\Downloads'
str_folder_prefix = 'Files - '
str_folder_source = r'C:\Users\daner\Downloads'
str_protocol_ifexist = 'rename'

def do_move(target, destination, protocol):
    try:
        os.makedirs(destination)
    except FileExistsError:
        print("Folder already exists: " + destination)
    except OSError as e:
        print("Failed to create folder " + destination + ": " + e)
        exit()
    finally:
        if protocol == 'overwrite':
            shutil.move(target, destination)
        elif protocol == 'rename':
            int_counter = 1
            destination_new = destination + '\\' + os.path.basename(target)
            while os.path.exists(destination_new):
                int_counter = int_counter + 1
                destination_new = os.path.splitext(destination_new)[0] + " Copy " + str(int_counter) + os.path.splitext(destination_new)[1]
            shutil.move(target, destination_new)
        else:
            print('Protocol ' + protocol + ' not known.')
            exit()

def do_move_check(target, destination, protocol):
    boolean_proceed = True
    if os.path.isfile(target):
        str_folder_destination_new = destination + '\\' + str_folder_prefix + os.path.splitext(target)[1][1:].upper()
    elif os.path.isdir(target):
        str_folder_destination_new = destination + r'\Folders'
        if os.path.basename(target) == 'Folders' or os.path.basename(target)[0:len(str_folder_prefix)] == str_folder_prefix:
            print("Cannot proceed moving the folder '" + target)
            boolean_proceed = False
    if boolean_proceed:
        do_move(target, str_folder_destination_new, protocol)

def main(str_folder_source, str_folder_destination, str_protocol_ifexist):
    try:
        for str_entry in os.listdir(str_folder_source):
            print(str_entry)
            str_entry_abs = str_folder_source + '\\' + str_entry
            do_move_check(str_entry_abs, str_folder_destination, str_protocol_ifexist)
    except FileNotFoundError:
        print("Directory not found for " + str_folder_source)
    except PermissionError:
        print("Permission denied for " + str_folder_source)
    
if __name__ == "__main__":
    obj_parser = argparse.ArgumentParser(description='Move a file or a folder')
    obj_parser.add_argument('source', type=str, help='Source file or folder.')
    obj_parser.add_argument('destination', type=str, help='Destination folder.')
    obj_parser.add_argument('protocol', type=str, help='What will the program do if same file or folder was found? (rename/overwrite)')
    obj_args = obj_parser.parse_args()
    str_folder_destination = obj_args.destination
    str_folder_source = obj_args.source
    str_protocol_ifexist= obj_args.protocol
    main(str_folder_source, str_folder_destination, str_protocol_ifexist)