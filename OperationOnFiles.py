
try:
    file = open("test.txt", "w")
    file.write("I'm testing")

    print(0/0)

    file.write("I'm testing here")
finally:
    file.close()