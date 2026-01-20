x = input("Enter text to write to the file: ")
with open("output.txt","wt") as o:
    o.write(x)
    print("Data successfully written to output.txt.\n")
y = input("Enter additional text to append: ")
with open("output.txt","at") as a:
    a.write("\n")
    a.write(y)
    print("Data successfully appended.\n")
print("Final content of output.txt:")
with open("output.txt","rt") as r:
    l = r.readlines()
    for line in l:
        print(line.rstrip('\n'))