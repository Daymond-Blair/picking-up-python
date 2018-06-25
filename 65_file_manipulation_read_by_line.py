# 65 66 advanced exceptions and reading files line by line
def readLines():
    count = 0

    try:
        with open('people.txt') as file_object:
            contents = file_object.readlines()
            for line in contents:
                count += 5
                print('line ' + str(count) + ': ' + line)
    except OSError as booboo:  # Parent error to FileNotFound and child to Exception

        print("We had a booboo!!")
        print(booboo)


readLines()
