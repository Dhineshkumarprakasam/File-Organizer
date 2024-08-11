# Dhinesh file organizer
import pyfiglet
import os
import time

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def stop():
    clear_screen()
    print("Organizing files completed...\n")
    t5=pyfiglet.figlet_format("Thank You")
    print(t5)
    time.sleep(3)
    n=input()

def fileExist():
    clear_screen()
    print("Exiting with error..")
    print("File exist")
    time.sleep(3)



class unique():
    def __init__(self):
        uniqueFileTypes=set()
        files=os.listdir()

        #finding unique file types
        for i in files:
            f = i.split('.')
            if len(f)>=2:
                uniqueFileTypes.add(f[-1])

        #creating folders for each file type
        while(True):
            try:
                for j in uniqueFileTypes:
                    os.mkdir(j)
                break
            except FileExistsError:
                fileExist()
                break

        
        #moving files to the folder
        while True:
            try:
                for i in files:
                    for j in uniqueFileTypes:
                        if i.endswith(j):
                            os.rename(i,j+"\\"+i)
            except FileExistsError:
                fileExist()
                break


class categorize:
    def __init__(self):

        #file types
        image = ['jpeg', 'jpg', 'png', 'gif', 'bmp', 'tiff', 'tif', 'webp', 'ico', 'svg', 'heic', 'heif', 'cr2', 'cr3', 'nef', 'arw', 'rw2', 'orf', 'raf', 'dng']
        video = ['mp4', 'mkv', 'avi', 'mov', 'wmv', 'flv', 'webm', 'mpeg', 'mpg', 'm4v', '3gp', '3g2', 'f4v', 'f4p', 'f4a', 'f4b', 'vob', 'ogv']
        document = ['pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt', 'rtf', 'odt', 'ods', 'odp', 'odg', 'odf', 'csv', 'tsv', 'epub', 'mobi']
        music = ['mp3', 'wav', 'flac', 'aac', 'ogg', 'wma', 'm4a', 'alac','aiff', 'pcm', 'amr', 'opus', 'au']

        #creating folder
        folders={"images","videos","documents","music","others"}
        while True:
            try:
                for i in folders:
                    os.mkdir(i)
                break
            except FileExistsError:
                fileExist()
                break
        
        #moving files
        files=os.listdir()
        for i in files:
            f=i.split('.')

            if(len(f)>=2):
                fileType=f[-1]

                if fileType in image:
                    os.rename(i,"images\\"+i)
                
                elif fileType in video:
                    os.rename(i,"videos\\"+i)

                elif fileType in document:
                    os.rename(i,"documents\\"+i)
                
                elif fileType in music:
                    os.rename(i,"music\\"+i)

                else:
                    os.rename(i,"others\\"+i)
                

                
# main program 
clear_screen()
t1 = pyfiglet.figlet_format("Welcome")
t2 = pyfiglet.figlet_format("           TO")
t3 = pyfiglet.figlet_format("File Organizer")

print(t1)
print(t2)
print(t3)
print("Loading...")

time.sleep(5)
clear_screen()

while(True):
    try:
        print("0.Exit \n1.Unique folder for each file type \n2.Categorize as image, video, documents and others")
        choice = int(input("Enter Your choice : "))

        if choice == 0:
            stop()
            break

        elif choice == 1:
            clear_screen()
            t4 = pyfiglet.figlet_format("Organizing..")
            print(t4)
            time.sleep(3)
            obj = unique()
            stop()
            break
        
        elif choice == 2:
            clear_screen()
            t4 = pyfiglet.figlet_format("Organizing..")
            print(t4)
            time.sleep(3)
            obj = categorize()
            stop()
            break

        else:
            clear_screen()
            print("**Oops, Try again**")
            time.sleep(2)
            clear_screen()
            continue

    except ValueError or TypeError:
        clear_screen()
        print("**Oops, Try again**")
        time.sleep(2)
        clear_screen()
        continue
