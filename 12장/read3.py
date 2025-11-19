infile = open(r"C:\2025_python\12장\phones.txt", "r", encoding="utf-8")
for line in  infile:
    line=line.rstrip()
    print(line)
infile.close()