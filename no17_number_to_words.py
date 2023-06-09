"""
https://www.quora.com/How-do-I-convert-numbers-to-words-in-Python.
"""

global suffixes
suffixes = ["", "Thousand", "Million", "Billion"]

global ones
ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

global after_ten
after_ten = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

global tens
tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety", "Hundred"]

#handles the nomenclature of a triplet
#number: the number in the string form, index: position of the triplet


def gimmeThemWords(number, index):
    length = len(number)

    if(length > 3):
        return False
    #pads the number's string representation with 0s on the left
    number = number.zfill(3)
    string = ""

    hundreds_digit = ord(number[0]) - 48
    tens_digit = ord(number[1]) - 48
    ones_digit = ord(number[2]) - 48

    string += "" if number[0] == '0' else ones[hundreds_digit]
    string += " Hundred " if not string == "" else ""

    if(tens_digit > 1):
        string += tens[tens_digit - 2]
        string += " "
        string += ones[ones_digit]

    elif(tens_digit == 1):
        string += after_ten[(int(tens_digit + ones_digit) % 10) - 1]

    elif(tens_digit == 0):
        string += ones[ones_digit]

    #counter check to determine the positional system
    if(string.endswith("Zero")):
        string = string[:-len("Zero")]

    else:
        string += " "

    if(not len(string) == 0):    
        string += suffixes[index]

    return string

#initiates the process of converting the number into its cardinal form


def initiateProcess(number):
    length = len(str(number))

    #counter contains the number of size- 3 groupings of digits that can be formed from the number
    counter = int(length / 3) if length % 3 == 0 else int(length / 3) + 1
    counter_copy = counter
    word_representation = []

    for i in range(length - 1, -1, -3):
        word_representation.append(gimmeThemWords(str(number)[0 if i - 2 < 0 else i - 2 : i + 1], counter_copy - counter))
        counter -= 1

    # print(number,": ", end = "", flush = True)
    for s in reversed(word_representation):
        if(not len(s.strip()) == 0):
            print(s, "", end = "", flush = True)

    #newline
    print()

t = int(input())
for _ in range(t):
    n = int(input())
    initiateProcess(n)