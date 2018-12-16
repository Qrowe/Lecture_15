from glob import glob
import os

#delete path
def deletePath(filepath):
    return os.path.basename(filepath)
#search file and path from two direcotry.
def searchTwoDirectory(input1 , input2):
    files1 = glob(input1+"/*.*")
    files2 = glob(input2 + "/*.*")
    find = []
    for filepath1 in files1:
        for filepath2 in files2:
            if deletePath(filepath1) == deletePath(filepath2):
                find.append(filepath1)
                find.append(filepath2)
    return find

def searchSomeDirectory(bathpath):
    dirname = os.path.dirname(bathpath)
    dirpath = glob(dirname+"/*")
    result = []
    if len(dirpath) > 1:
        for filepath1 in dirpath:
            for filepath2 in dirpath:
                if filepath1 != filepath2:
                    result.append(searchTwoDirectory(filepath1 , filepath2))
    else:
        print("Error:cannot find path more than two")
    return result

def combination(n , k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))
#階乗
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
def test():
    input1 = "./パス1"
    input2 = "./パス2"
    findpath= searchTwoDirectory(input1 , input2)
    for filepath in findpath:
        print(filepath)
    return

findpath = searchSomeDirectory("ここにパスをいれる")
for filepath1 in findpath:
    for filepath2 in filepath1:
        print(filepath2)