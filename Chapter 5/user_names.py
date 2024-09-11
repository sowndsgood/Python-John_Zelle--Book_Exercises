def main():
    infile=open("names.txt","r")
    outfile=open("usernames.txt","w")

    for line in infile:
        first,last=line.split()
        username=(first[0]+last[0:7]).lower()
        print(username,file=outfile)

    infile.close()
    outfile.close()

main()
