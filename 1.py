try :
    with open("sample.txt", "rt") as f:
        l = f.readlines()
        print("Reading file content :")
        for line in range(len(l)):
            print(f"Line {line+1}: {l[line].rstrip('\n')}")
except FileNotFoundError:
        print(f"Error: The file 'sample.txt' was not found.")