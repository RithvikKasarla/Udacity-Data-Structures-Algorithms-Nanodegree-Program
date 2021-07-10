import os

def find_files(suffix, path):
    try:
        files_ = os.listdir(path)
    except:
        return "Path Not Found"
    count = 0
    for file_ in files_:
        if os.path.isfile(path + "/" + file_):
            if file_.endswith(suffix):
                count += 1 
        if os.path.isdir(path + "/" +  file_):
            count += find_files(suffix, path + "/" +file_)
    return count



if __name__ ==  '__main__':
    print(find_files(".c","./testdir")) # Answer 4
    print(find_files(".h","./testdir")) # Answer 4
    print(find_files(".k","./testdir")) # Answer 0
    print(find_files(".c","./WRONGDIR")) # Answer "Path Not Found"