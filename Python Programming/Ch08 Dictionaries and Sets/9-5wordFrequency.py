# Developer: Jack Bowman
# Program: Word Frequency
# Date: 03/16/2022

def main():
    file = open(input('Please enter the name of a text file: '), 'r')  # gets file from user
    words = getwords(file)  # puts words of file into list
    dictionary = {i: words.count(i) for i in words}  # counts instances of word in dictionary
    file.close()

    print(dictionary)


# loops through words in file and returns words in a list
def getwords(file):
    words = []
    for line in file:
        for word in line.split():
            words.append(word.lower())
    return words


if __name__ == '__main__':
    try:
        main()
    except FileNotFoundError:
        print('File not found')
    except Exception as exception:
        print(f'The following error occurred: {exception}')
