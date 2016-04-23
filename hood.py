# mytree

import os
import sys


def neighborhood(depth, flag):
    """A simple re-implimentation of the tree command"""
    spacer = "  "*depth
    list_hood = os.listdir()
    if depth == 0:
        print(".")
    for des in list_hood:
        if flag == "a":
            pass
        else:
            if des[0] == ".":
                continue
        print("{0}|__ {1}".format(spacer, des))
        if os.path.isdir(des):
            os.chdir(des)
            neighborhood(depth + 2, flag)
            os.chdir("../")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        flag = sys.argv[1].split("-")[-1]
    else:
        flag = False
    neighborhood(0, flag)
    print()
