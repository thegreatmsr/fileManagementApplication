f = open("I and O\python.txt", "r")
data = f.read(5)
print(data)
print(type(data))
f.close()


f = open("I and O\python.txt", "r+")
line1 =f.readline()
print(line1)
f.close()


# data = f.read() Reads entire line
# data= f.readline() Reads one line at a time
# We can write to file in two ways write mode or the append mode any of the mode can we used to write into a file but append means to write in file at the end of it 
f = open("I and O\python.txt", "w")
f.write("I want to eat ice cream original made at home\n")
f.close #write mode writen the data (it made my old text basically it overwrite my file)


f = open("I and O\python.txt", "a")
f.write("\nI want to eat ice cream original made at home with love")
f.close()

#Now Let's suppose we don't have a particular file but we want to write a data in any such desired file so Python we automatically make a such file for us 
f = open("sample.txt","a")
#f.write("How are you Doing Man?")
f.close()

# r+ thing overwrite the data from the beginnng this is a pen will become abcd is a pen 
# w+ in this truncate is done
# a+ in this no truncate is done
# r+ in this no truncate is done
with open("sample2.txt", "r") as f:
    data = f.read()
    print(data)
    
# How to delete a file in python
# we can use the module to delete a file in the python
import os
os.remove("sample.txt") # it delete the file named sample.txt
    