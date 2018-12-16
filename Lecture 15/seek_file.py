with open('myfile.txt', 'r+') as f:
    f.write('0123456789abcdef')
    f.seek(5)
    print(f.read(1))
    f.seek(-3,2)
    print(f.read(1))
