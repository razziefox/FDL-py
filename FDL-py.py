# FDL parser library for Python3
# florencio (c) 2023

def open_fdl(file_path):
    file = open(file_path, "r")
    return file

def close_fdl(file):
    file.close()

def fetch_fdl(file, group, sub_group):
    fetch = False
    for x in file:
        if ("[" + group) in x:
            fetch = True
        if "[/" in x:
            fetch = False

        if fetch == True and sub_group+"=" in x:
            length = len(sub_group)
            return x[length+1:]
    else:
        return (f"Error: Failed to find info for '{group}' in FDL file")
