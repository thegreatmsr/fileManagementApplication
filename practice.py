with open("practice.txt", "w") as f:
    f.write("Hi Everyone\nWe are learning I/O File Operation\n")
    f.write("Using Java\n I Like Programming ")
    
# Now we have to write a program in which java will be replace with Python
with open("practice.txt", "r") as f:
    data = f.read()
newData=data.replace("Java", "Python")
print(newData)