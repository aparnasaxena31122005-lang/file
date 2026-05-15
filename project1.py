#project -CRUD Operation

from pathlib import Path
import os #operating system
def readfileandfolder():
        try:
           p = Path('')
           items = list(p.rglob('*'))
           for index , file in enumerate (items):
            print(f'{index+1}-(file)')
        except Exception as e:
            print(e)


def creat_file():
    try:
       readfileandfolder()
   # C:\Users\BiG BOSS\Desktop\python\himawari.txt
       file_name = input ('enter name of file:')
       p = Path(file_name)
       if p.exists():
         print('FILE ALREADY EXISTS')
       else:
        with open(file_name,'w') as file:
            content = input ('enter your file content:')
            file.write(content)
            print('FILE ADDED')
    except Exception as e:
        print(e)


def read_file():
    try:
       readfileandfolder()
       file_name = input('enter name of your file')
       p = Path(file_name)
       if p.exists():
         with open(file_name,'r') as file:
            print(file.read())
       else:
        print('FILE NOT FOUND!')  
    except Exception as e:
        print(e)


def update_file():
     try:
          readfileandfolder()  
          file_name = input ("enter name of your file")
          p = Path(file_name)
          if p.exists():
             print("press 1 to overwrite the content") 
             print("press 2 to append new content")

             option = int(input("Enter your choice for updating a file"))
             if option ==1:
                 with open(file_name,'w')as file:
                     content = input("Enter your content:")
                     file.write(content)
                     print("CONTENT CHANGED...")
             elif option ==2:
                 with option(file_name,'a') as file:
                     content = input("Enter your content")
                     file.write(content)
                     print("CONTENT CHANGED...")
             else:
                 print("INVALID INPUT...")
          else:
            print("FILE DOES NOT EXISTS...")

        
     except Exception as e:
         print(e)

def delete_file():
    try:
        readfileandfolder()
        file_name = input("enter name of your file")         
        p = Path(file_name)
                
        if p.exists():
            os.remove(p)#os is removing path of that completely from the system
            print("FILE DELETED...")
        else:
            print('FILE DOES NOT EXISTS...')
    except Exception as e:
        print(e)


def rename_file():
    try:
        readfileandfolder()
        file_name = input("Enter your file name:")
        p = Path(file_name)
        if p.exists():
            new_file = input("Enter new name of file")
            p.rename(new_file)
            print("FILE NOT FOUND")
    except Exception as e:
        print(e)      

def create_folder():
    try:
        readfileandfolder()
        folder_name = input("write the name of your folder:")
        p = Path(folder_name)
        if p.exists():
            print("FOLDER ALREADY EXISTS...")
        else:
            p.mkdir()
            print("FOLDER CREATED...")
    except Exception as e:
        print(e)

def delete_folder():
    try:
        readfileandfolder()
        folder_name = input("write the name of your folder which to delete:")
        p = Path(folder_name)
        if p.exists():
            p.rmdir()
            print("FOLDER DELETED...")
        else:
            print("FOLDER DOES NOT EXISTS...")
    except Exception as e:
        print(e)                        
    





while True:

     print ("press 1 for creating a file")
     print ("press 2 for reading a file")
     print ("press 3 for update a file")
     print ("press 4 for deleting a file")
     print ("press 5 for renaming a flie")
     print ("press 6 for creating a folder")
     print ("press 7 for deleting a folder")
     print ("press 0 for exiting")    


     option = int(input("enter your choice:"))

    
     if option == 1:
            
            creat_file()
            
     if option ==2:
            read_file()

     if option ==3:
            update_file()
     if option ==4:
             delete_file()

     if option ==5:
            rename_file()

     if option ==6:
            create_folder()
            
     if option ==7:
            delete_folder()
     if option==0:
         break