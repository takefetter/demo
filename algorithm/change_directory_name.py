import os
import re


def filename(path):
    for file in os.listdir(path):
        dir = os.path.join(path)
        print(dir)
        oldname = os.path.basename(file)
        oldlist = oldname.split('_')
        print(oldlist)
        try:
            a = int(oldlist[1])
        except ValueError:
            continue
        if (a == 18):
            if len(oldlist) == 2:
                newname = oldlist[1] + '_' + oldlist[0]
            elif len(oldlist) == 3:
                newname = oldlist[2] + '_' + oldlist[0] + '_' + oldlist[1]
            os.rename(os.path.join(dir, oldname), os.path.join(dir, newname))


if __name__ == '__main__':
    filename('D:\githubblog\\takef-demo\\algorithm\CodingInterview2ndChineseSolution_Python')
