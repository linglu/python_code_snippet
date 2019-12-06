
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

# 过滤文件
def filter_files_with():
    for path, dirnames, filenames in os.walk("."):
        for f in filenames:
            if type in f:
                fs = path "/" + f
                yield fs
