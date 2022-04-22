# Developer: Jack Bowman
# Program: upper_lower
# Date: 02/21/2022

def main():
    sentence = input('Please enter a sentence in camel case to reformat it: ')

    # creates a new variable to change the sentence above to normal text
    newSentence = sentence[0].upper()  # capitalizes and inserts first letter

    # inserts spaces before capital letters
    for i in range(1, len(sentence)):
        if sentence[i].isupper():
            newSentence += ' ' + sentence[i].lower()
        else:
            newSentence += sentence[i]

    print(newSentence)

if __name__ == '__main__':
    main()