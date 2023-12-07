
import os

str_folder_destination = r'C:\Users\daner\Downloads'
str_folder_prefix = 'Files - '
str_folder_source = r'C:\Users\daner\Documents\test'

try:
    for str_entry in os.listdir(str_folder_source):
        str_entry_abs = str_folder_source + '\\' + str_entry
        if os.path.isfile(str_entry_abs):
            str_ext = os.path.splitext(str_entry)[1][1:]
            str_folder_destination_new = str_folder_destination + '\\' + str_folder_prefix + str_ext.upper()
            try:
                os.makedirs(str_folder_destination_new)
            except FileExistsError:
                print("Folder already exists: " + str_folder_destination_new)
            except OSError as e:
                print("Failed to create folder " + str_folder_destination_new + ": " + e)
        elif os.path.isdir(str_entry_abs):
            # Pending
            pass
        pass
except FileNotFoundError:
    print("Directory not found for " + str_folder_source)
except PermissionError:
    print("Permission denied for " + str_folder_source)