# 67 Opening Files - Simple Line Search

# 65 66 advanced exceptions and reading files line by line
import re


# print out lines in a file / read that file!!!!
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


# search line by delegated term / novice least complexity
def readLinesAndSearch():
    print("#####-----NOW USING HARD SEARCH-----THIS IS THE EASIEST-----#####")
    try:
        with open('simple_people.txt') as file_object:
            contents = file_object.readlines()
            for line in contents:
                if line.rstrip() == 'Lucy':
                    print('--> We Found Lucy!\n')
                else:
                    print(line)
    except OSError as booboo:
        print("we had a booboo!!")
        print(booboo)
    print('#####-----END-----#####\n')


# uses the -find- method to search lines / intermediate slight complexity
def readLinesWithFind():
    print('#####-----NOW USING FIND PROPERTY (premade method/framework)-----THIS IS MEDIUM-----#####')
    try:
        with open('people.txt') as file_object:
            contents = file_object.readlines()
            for line in contents:
                hit = line.find("Lucy")

                if hit != -1:
                    print("--> We found Lucy in the line of text!!!\n")
                else:
                    print(line)
    except OSError as booboo:
        print("We had an even worse booboo!!!!!")
        print(booboo)
    print('#####-----END-----#####\n')


def regExMagic(pattern, string):
    objectMatch = re.search(pattern, string)
    return objectMatch


# RegEx is short for regular expressions / advanced most complexity
def readLinesWithRegEx():
    print('#####-----NOW USING RegEX FUNCTION/METHOD THIS IS THE MOST ADVANCED AND COMPLEX LEARN THIS-----#####')
    try:
        with open('people.txt') as file_object:
            contents = file_object.readlines()
            print("\n")
            for line in contents:
                pattern = 'Lucy$'  # beginning and end symbols ^ and $ refer to the beginning and end of searched line alpha and omega
                if str(regExMagic(pattern, line)) == "None":
                    print(line)
                else:
                    print("--> We found the text: " + pattern + ", in this line " + line + "\n")
    except OSError as booboo:
        print("We had an even worse booboo!!!!!")
        print(booboo)
    print('#####-----END-----#####\n')


readLinesAndSearch()

readLinesWithFind()

readLinesWithRegEx()
