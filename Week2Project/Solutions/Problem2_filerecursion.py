import os

def find_files(suffix, path):
    files_ = os.listdir(path)
    count = 0
    for file_ in files_:
        print(path +"/" +  file_)
        if os.path.isfile(path + "/" + file_):
            if file_.endswith(suffix):
                count += 1
        if os.path.isdir(path + "/" +  file_):
            count += find_files(suffix, path + "/" +file_)
    return count



if __name__ ==  '__main__':
    print(find_files(".c","./testdir"))
