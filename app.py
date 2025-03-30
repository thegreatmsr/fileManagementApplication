import os
def createFile(filename):
    try:
        with open (filename, 'x') as f:
            print(f"File Name {filename}: Created Successfully!")
    except FileExistsError:
        print(f"File name {filename} already exists!")
    except Exception as E: 
        print("An Error Occurred")
def viewAllFile():
    files = os.listdir()
    if not files:
        print("No File Found in the directory:")
    else:
        print("File in Directory")
        for file in files:
            print(file)
def deleteFile(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted completely:")
    except FileNotFoundError:
        print("File Not Found")
    except Exception as E:
        print("An Error Occured")
        
def readFile(filename):
    try:
        with open('I and O\sample.txt' , 'r') as f:
            data =f.read()
            print(f"Content of '{filename}':\n{data}")
        
    except FileNotFoundError:
        print(f"{filename} doesn't exists!")
        
    except Exception as E:
        print("An Error Occured")
        
def editFileName(filename):
    try:
        with open('I and O\sample.txt', 'a') as f:
            data =input("Enter the new data here")
            f.write(data+"\n")
            print("Successfully addedd")
    except FileNotFoundError:
        print(f"{filename} doesn't exists!")
        
    except Exception as E:
        print("An Error Occured")
        
def main():
    while True:
        print("FILE MANAGEMENT APP")
        print("1. Create")
        print("2. View")
        print("3. Delete")
        print("4. Read")
        print("5. Edit")
        print("6.Exit")
        
        choice = input("Enter your chocie")
        if choice=="1":
            filename = input("Enter the name of the file:")
            createFile(filename)
        elif choice=="2":
            viewAllFile()
        elif choice=="3":
            filename= input("Enter the name of the file you want to delete ")
            deleteFile(filename)
        elif choice=="4":
            filename= input("Enter the name of the file you want to delete ")
            readFile(filename)
        elif choice=="5":
            filename= input("Enter the name of the file you want to delete ")
            editFileName()
        else:
            print("COME YOU YESH")
if __name__=="__main__":
    main()

            
            

            
            


        
        
    
            
    

