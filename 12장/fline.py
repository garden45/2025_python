infile=open(r"C:\2025_python\12장\proverbs.txt")

outfile=open("output.txt", "w")

i=1

for line in infile:
    outfile.write(str(i)+": "+line)

    i=i+1

infile.close()
outfile.close()