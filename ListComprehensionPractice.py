# List comprehension to be used for practice problems:

nums = [i for i in range(1,1001)]

string = 'Practice Problems to Drill List Comprehension in Your Head.'

#1 - Find all of the numbers from 1-1000 that are divisible by 8:

[num for num in nums if num % 8 == 0]

#2 - Find all the numbers from 1-1000 that have a 6 in them:

[num for num in nums if '6' in str(num)]

#3 - Count the number of spaces in a string:

print(len([char for char in string if char == ' ']))

#4 - Remove all of the vowels in a string:

vowels = ['a', 'e', 'i', 'o', 'u']

''.join([char for char in string if char not in vowels])

#5 - Find all of the words in a string that are less than 5 letters:

words = string.split(' ')
[word for word in words if len(word) < 5]

#6 - Use a dictionary comprehension to count the length of each word in a sentence:

dictOfLengths = {word:len(word) for word in words}
