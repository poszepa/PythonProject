
def fileSave():
    with open("test.txt", "w") as file:
        file.write("new line")


def readLine():
    with open("test.txt", "r", encoding="UTF-8") as file:
        for line in file:
            print(line)
        #With as working like open and close the file. We not need to rembember to close the file.



def controlLine():
    with open("test.txt", "r", encoding="UTF-8") as file:
        print(file.readline())
        print(file.tell())
        print(file.readline())
        print(file.tell())
        file.seek(0) # here we go to first place in file
        print(file.readline())
        print(file.tell())

    #file.tell - return number of char
    #With file.seek we can jump to conctret place in file


def fileAppend():
    with open("test.txt", "a", encoding="UTF-8") as file:
        file.write(
            "\n" +
            "Test"
        )

        #Arg 'a' wrtie 'append' add text to end of file in last line.

#Test r+
#r+ do not create new file in file in arg doesn't exsist. So if
#we try to open file which we dont have on the driver we will got
#error

def file_r_plus():
    with open("test.txt", "r+", encoding="UTF-8") as file:
        for line in file:
            print(line)
        file.write("\nThat is the last message99")
        file.seek(0)
        for line in file:
            print(line)