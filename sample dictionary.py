# receives input from the user
word = input("Enter the word you are searching for").lower()
# stores dictionary of words with their meaning
Word = {
    "lazy": "unwilling to work or use energy",
    "obey": "to comply with instructions or rules",
    "grow": "to progress to maturity",
    "tolerate": "being able to accept or endure with forbearance",
    "magnify": "to make an appear larger than it actually is",
}
# prints out the meaning of the word if the word the user mentions is found in the dictionary
if word in Word:
    result = Word.get(word)
    print(word + "means: " + result)
# prints the subsequent message if user's input is not found in the dictionary
else:
    print("Sorry,This word doesn't exist in my dictionary")
