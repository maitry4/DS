# write given text in a file
with open("something.txt", 'w') as f:
    f.write("write this")
    print("written successfully")

# read whole data
with open("something.txt", 'r') as f:
    text = f.read()
    print(text)  

# read first 10 characters
with open("something.txt", 'r') as f:
    text = f.read(10)
    print(text)  

# read a line
with open("something.txt", 'r') as f:
    text = f.readline()
    print(text)  

# print current position of cursor
with open("something.txt", 'r') as f:
    print(f.tell())
    text = f.read(3)
    print(text)  
    print(f.tell())