
# 遍历所有文件
def print_every_file_path(dirs):
    for path, dirnames, filenames in os.walk(dirs):
        for f in filenames:
            print(path + "/" + f)


# 遍历所有目录
def print_every_dir_path(dirs):
    for path, dirnames, filenames in os.walk(dirs):
        for d in dirnames:
            print(path + "/" + d)
