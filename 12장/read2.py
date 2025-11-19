infile = open(r"C:\2025_python\12장\phones.txt", "r", encoding="utf-8")
line=infile.readline()
while line!="":
    print(line)
    line=infile.readline()
infile.close()