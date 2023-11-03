
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


#Test w+
#That arg is not usually use because when file is exsist those file will be
#remove and will be create new file.

###################################################

#Test a+
#that propably work similary like r+.
#On r+ we have cursor on the start file, on the a+ we have on the end.

def text_from_file(file_name):
    text = []
    with open(file_name, "r", encoding="UTF-8") as file:
        for line in file:
            text.append(line.split("\n")[0])
    return text

def split_firstName_surname(text):
    list_name_and_surname = []
    for name in text:
        person = name.split(" ")
        try:
            list_name_and_surname.append((person[0], person[1]))
        except IndexError:
            list_name_and_surname.append(("none", person[0]))
    return list_name_and_surname

def save_firstName_Surname_to_file(list_name, file_firstName = "imiona.text", file_surname = "nazwiska.txt"):
    with open(file_firstName, "w", encoding="UTF-8") as file:
        for firstName in list_name:
            file.write("\n" + firstName[0])
    with open(file_surname, "w", encoding="UTF-8") as file:
        for lastName in list_name:
            file.write("\n" + lastName[1])



def read_file(file_name):
    try:
        return text_from_file(file_name)
    except FileNotFoundError:
        print("file doesn't exsist")


def run_program_first():
    file_name = input("Input file name: ")
    print(read_file(file_name))

