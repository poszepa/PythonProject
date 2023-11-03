
def fileSave():
    with open("test.txt", "w") as file:
        file.write("new line")


def readLine():
    with open("test.txt", "r", encoding="UTF-8") as file:
        for line in file:
            print(line)

        #With as working like open and close the file. We not need to rembember to close the file.