#defining a function that finds the wor(s) equivalent for user's input
def convert(number):
    # creates an empty list where the words will be appended
    answer = []

    numbers = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    }
    # iterates through the number the user inputted
    for i in number:
        # retrives the value (word equivalent) of the number from the dictionary
        result = numbers.get(i)
        # appends the word equivalent to the "answer" list and outputs the answer
        answer.append(result)
    return answer

# user inputs a number
number = input("Enter a number")
# calls the function to find the word-equivalent for the inputted number
print(convert(number))






