# print("Hello world!")
# print("What's your name?")
# my_name = input()
# print(f"It's good to meent you, {my_name}")
# print("The length of your name is:")
# print(len(my_name))
# print("What is your age?")
# my_age = input()
# print(f"You will be {str(int(my_age) + 1)} in a year.")
# print(str(29))
# print(int(1.25))
# print(False and False)
# print(True and True)
# print(False and True)
# print((4 < 5) and (5 < 6))
# spam = 0
# while spam < 5:
#     print("Hello world!")
#     spam = spam + 1
# name = ''
# while name != 'your name':
#     print("Please type your name.")
#     name = input()
# print("Thank you!")
# while True:
#     print("Please type your name.")
#     name = input()
#     if name == 'your name':
#         break
# print("Thank you.")
# while True:
#     print("Who are you?")
#     name = input()
#     if name != 'Joe':
#         continue
#     print("Hello, Joe. What's the password? (It's a fish.)")
#     password = input()
#     if password == 'swordfish':
#         break
# print("Access granted.")
# print("My name is:")
# for i in range(5):
#     print(f"Jimmy Five Times {i}")
# total = 0
# for num in range(101):
#     total += num
# print(total)
# for i in range(5, -1, -1):
#     print(i)
# import random
# for i in range(5):
#     print(random.randint(1, 10))
# import sys
# while True:
#     print("Type exit to exit.")
#     response = input()
#     if response == 'exit':
#         sys.exit()
#     print(f"You typed {response}.")
# import random
# secretNumber = random.randint(1, 20)
# print("I'm thinking of a number between 1 and 20.")
#
# for guessesTaken in range(1, 7):
#     print("Take a guess.")
#     guess = int(input())
#
#     if guess < secretNumber:
#         print("Your guess is too low.")
#     elif guess > secretNumber:
#         print("Your number is too high.")
#     else:
#         break
#
# if guess == secretNumber:
#     print(f"Good job! YOU guessed my number in {str(guessesTaken)} guesses!")
# else:
#     print(f"Nope. The number i thinking of was {str(secretNumber)}")
# import random
# secretNumber = random.randint(1, 20)
# print("I am thinking of a number between 1 and 20.")
# for guessssTaken in range(1, 7):
#     print("Take a guess.")
#     guess = int(input())
#     if guess < secretNumber:
#         print("Your guess is too low.")
#     elif guess > secretNumber:
#         print("Your guess is too high.")
#     else:
#         break
# import random
# import sys
#
# print("ROCK, PAPER, SCISSORS")
# wins = 0
# losses = 0
# ties = 0
#
# while True:
#     print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
#     while True:
#         print("Enter your move: (r)ock (p)aper (s)cissors or (q)iut")
#         playerMove = input()
#         if playerMove == 'q':
#             sys.exit()
#         if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
#             break
#         print("Type one of r, p, s, or q.")
#
#     if playerMove == 'r':
#         print("ROCK versus...")
#     elif playerMove == 'p':
#         print("PAPER versus...")
#     elif playerMove == 's':
#         print("SCISSORS versus...")
#
#     randomNmuber = random.randint(1, 3)
#     if randomNmuber == 1:
#         computerMove = 'r'
#         print("ROCK")
#     elif randomNmuber == 2:
#         computerMove = 'p'
#         print("PAPER")
#     elif randomNmuber == 3:
#         computerMove = 's'
#         print("SCISSORS")
#
#     if playerMove == computerMove:
#         print("It's a tie!")
#         ties = ties + 1
#     elif playerMove == 'r' and computerMove == 's':
#         print("You win!")
#         wins = wins + 1
#     elif playerMove == 'p' and computerMove == 'r':
#         print("You win!")
#         wins = wins + 1
#     elif playerMove == 's' and computerMove == 'p':
#         print("You win!")
#         wins = wins + 1
#     elif playerMove == 'r' and computerMove == 'p':
#         print("You lose!")
#         losses = losses + 1
#     elif playerMove == 'p' and computerMove == 's':
#         print("You lose!")
#         losses = losses + 1
#     elif playerMove == 's' and computerMove == 'r':
#         print("You lose!")
#         losses = losses + 1
# def hello(name):
#     print(f"Hello, {name}")
# hello("Alice")

# print(round(5.215,2))

# spam = print("Hello!")
# print(None==spam)
#
# print("Hello,", end="")
# print("World")
# print("cats","dogs","mice", sep=",")

# def a():
#     print("a() starts")
#     b()
#     d()
#     print("a() returns")
#
# def b():
#     print("b() starts")
#     c()
#     print("b() returns")
#
# def c():
#     print("c() starts")
#     print("c() returns")
#
# def d():
#     print("d() starts")
#     print("d() returns")
#
# a()

# def spam():
#     eggs = 31337
# spam()
# print(eggs)
# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)
#
# def bacon():
#     ham = 101
#     eggs = 0
#
# spam()

# def spam():
#     eggs = 'spam local'
#     print(eggs)
#
# def bacon():
#     eggs = 'bacon local'
#     print(eggs)
#     spam()
#     print(eggs)
#
# eggs = 'global'
# bacon()
# print(eggs)

# def spam():
#     global eggs
#     eggs = 'spam'
#
# eggs = 'global'
# spam()
# print(eggs)

# def spam():
#     print(eggs)
#     eggs = 'spam local'
# eggs = 'local'
# spam()

# def spam(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print("Error: Invalid argument")
#
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

# import time, sys
# indent = 0   # How many spaces to indent.
# indentIncreasing = True  # Whether the indentation is increasing or not.
#
# try:
#     while True:
#         print("  " * indent, end='')
#         print("********")
#         time.sleep(0.1)  # Pause for 1/10 of a second.
#
#         if indentIncreasing:
#              # Increase the number of space:
#              indent = indent + 1
#              if indent == 20:
#                  # Change direction:
#                  indentIncreasing = False
#         else:
#             # Decrease the number of space:
#             indent = indent - 1
#             if indent == 0:
#                 # Change direction:
#                 indentIncreasing = True
# except KeyboardInterrupt:
#     sys.exit()

# def collatz(number):
#     if number == 1:
#         print(number)
#     else:
#         while number != 1:
#             if number % 2 == 0:
#                 number = number // 2
#                 print(number)
#             elif number % 2 == 1:
#                 number = number * 3 + 1
#                 print(number)
#
# try:
#     message = ''
#     print(f"Enter a number: {message}")
#     message = input()
#     collatz(int(message))
# except ValueError:
#     print("请输入一个整数。")

# spam = [['cat','bat','rat','elephant'], ['A']]
# print(spam[1][0])
# print(len(spam[1][0]))
# catNames = []
# while True:
#     print(f"Enter the name of cat {str(len(catNames) + 1)}, or enter nothing to stop:")
#     name = input()
#     if name == '':
#         break
#     catNames = catNames + [name]
# print("The cat names are:")
# for name in catNames:
#     print(f" {name}")

# for i in range(4):
#     print(i)
# supplies = ['pens','staplers','flame-throwers','binders']
# for i in range(len(supplies)):
#     print(f"Index {str(i)} in supplies is {supplies[i]}")

# cat = ['fat','black','loud']
# size, color, dispoisition = cat
# print(size)
# supplies = ['pens','staplers','flamethrowers','binders']
# for index, item in enumerate(supplies):
#     print(f"Index {str(index)} in supplies is {item}")
# print(supplies.index('pens'))
# spam = ['a','Z','A','z']
# spam.reverse()
# print(spam)

# import random
#
# message = ['It is certain',
#     'It is decidedly so',
#     'Yes definitely',
#     'Reply hazy try again',
#     'Ask again later',
#     'Concentrate and ask again',
#     'My reply so',
#     'Outlook not so good',
#     'Very doubtful']
#
# print(message[random.randint(0, len(message) - 1)])

# eggs = ('hello', 42, 0.5)
# print(eggs[0])
# print(type(('hello',)))
# print(type('hello'))
# print(tuple(('cat','dog','5')))
# print(tuple('hello'))
# beacon = 'Hello'
# print(id(beacon))
# beacon += 'World!'
# print(id(beacon))
# def eggs(someParameter):
#     someParameter.append('Hello')
#
# spam = [1,2,3]
# eggs(spam)
# print(spam)

# import copy
# spam = ['A','B','C','D']
# print(id(spam))
# cheese = copy.copy(spam)
# print(id(cheese))

# Conway's Game of Life
# import random, time, copy
# WIDTH = 60
# HEIGHT = 20
#
# # Create a list of list for the cells:
# nextCells = []
# for x in range(WIDTH):
#     column = []  #Create a new column.
#     for y in range(HEIGHT):
#         if random.randint(0, 1) == 0:
#             column.append('#')  #Add a living cell.
#         else:
#             column.append('')   #Add a dead cell.
#     nextCells.append(column)  # nextcell is a list of column lists.
#
# while True:  #Main program loop.
#     print("\n\n\n\n\n")  # Separate each step with newlines.
#     currentCells = copy.deepcopy(nextCells)
#     #  Print currentCells on the screen:
#     for y in range(HEIGHT):
#         for x in range(WIDTH):
#             print(currentCells[x][y], end='')  # Print the # or space.
#         print()  # Print a newline at the end of the row.
#
# # Calculate the next step's cells based on current step's cells:
#     for x in range(WIDTH):
#         for y in range(HEIGHT):
#             #  Get neighbouring coordinates:
#             #  ' %  WIDTH'  ensures leftCorrd is always between 0 and WIDTH - 1
#             leftCoord = (x - 1) % WIDTH
#             rightCoord = (x + 1) % WIDTH
#             aboveCoord = (y - 1) % HEIGHT
#             belowCoord = (y + 1) % HEIGHT
#
#             #  Count number of living neighbours:
#             numNeighbors = 0
#             if currentCells[leftCoord][aboveCoord] == '#':
#                 numNeighbors += 1  # Top-left neighbor is alive.
#             if currentCells[x][aboveCoord] == '#':
#                 numNeighbors += 1  #Top neighbor is alive.
#             if currentCells[rightCoord][aboveCoord] == '#':
#                 numNeighbors += 1  #Top-right neighbor is alive.
#             if currentCells[leftCoord][y] == '#':
#                 numNeighbors += 1  #Left neighbor is alive.
#             if currentCells[rightCoord][y] == '#':
#                 numNeighbors += 1  #Right neighbor is alive.
#             if currentCells[leftCoord][belowCoord] == '#':
#                 numNeighbors += 1  #Bottom-left neighbor is alive.
#             if currentCells[x][belowCoord] == '#':
#                 numNeighbors += 1  #Bottom neighbor is alive.
#             if currentCells[rightCoord][belowCoord] == '#':
#                 numNeighbors += 1  #Bottom-right neighbor is alive.
#
#             # Set cell based on Conway's Game of Life rules:
#             if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
#                 # Living cells with 2 or 3 neighbors stay alive:
#                 nextCells[x][y] = '#'
#             elif currentCells[x][y] == '' and numNeighbors == 3:
#                 # Dead cells with 3 neighbors become alive:
#                 nextCells[x][y] = '#'
#             else:
#                 # Everything else dies or stays dead:
#                 nextCells[x][y] = ''
#     time.sleep(1)  # Add a 1-second pause to reduce flickering.
# import random
# numberOfStreaks = 0
# head = []
# tail = []
# for experimentNumber in range(1000000):
#     # Code that creates a list of 100 'heads' or 'tails' values.
#     if random.randint(0, 1) == 0:
#         numberOfStreaks += 1
#         head.append('T')
#     else:
#         numberOfStreaks += 1
#         tail.append('F')
# print(f"正面出现的概率: {len(head) / 1000000}")
# print(f"反面出现的概率: {len(tail) / 1000000}")
#
#     # Code that checks if there is a streak of 6 heads or tails in a row.
# x = 0  #正面
# y = 0  #反面
# a = 0  #正面概率
# b = 0  #反面概率
# head_tail = head + tail
# for i in range(len(head_tail)):
#     if head_tail[i] == 'T' and head_tail[i-1] == head_tail[i]:
#         x += 1
#     elif head_tail[i] == 'F' and head_tail[i-1] == head_tail[i]:
#         y += 1
#     if x == 5:
#         a += 1
#         x = 0
#     elif y == 5:
#         b += 1
#         y = 0
# print(a/len(head_tail))
# print(b/len(head_tail))
#
# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', '0', '0', '.', '.', '.'],
#         ['0', '0', '0', '0', '.', '.'],
#         ['0', '0', '0', '0', '0', '.'],
#         ['.', '0', '0', '0', '0', '0'],
#         ['0', '0', '0', '0', '0', '.'],
#         ['0', '0', '0', '0', '.', '.'],
#         ['.', '0', '0', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]
#
# for i in range(len(grid[0])):  # 外循环
#     for j in range(len(grid)):  # 内循环，先内再外
#         print(grid[j][i], end='  ')
#     print('\t')  # 用制表符隔开

# myCat = {'size':'fat','color':'gray','disposition':'loud'}
# print(myCat['size'])
# birthdays = {'Alice': 'Apr 1', 'Bob':'Dec 12','Carol':'Mar 4'}
# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break
#
#     if name in birthdays:
#         print(f"{birthdays[name]} is the birthday of {name}.")
#     else:
#         print(f"I don't have birthday information for {name}")
#         print("What's their birthday?")
#         bday = input()
#         birthdays[name] = bday
#         print("Birthday database updated.")


# spam = {'color':'red','age':42}
# for i in spam.values():
#     print(i)
# spam = {'name':'Pooka','age':5}
# spam.setdefault('color','black')
# print(spam)
# spam.setdefault('color','white')
# print(spam)
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
# print(count)
# import pprint
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1
# pprint.pprint(count)
# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print("-+-+-")
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print("-+-+-")
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print(f"Turn for {turn}. Move on which space?")
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = '0'
#     else:
#         turn = 'X'
# printBoard(theBoard)

# allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
#              'Bob': {'ham sandwiches': 3, 'apples': 2},
#              'Carol': {'cups': 3, 'apple pies': 1}}
# def totalBrought(guests, item):
#     numBrought = 0
#     for k, v in guests.items():
#         numBrought = numBrought + v.get(item, 0)
#     return numBrought
#
# print("Number of things being brought:")
# print(f" - Apples          {totalBrought(allGuests, 'apples')}")
# print(f" - Cups            {totalBrought(allGuests, 'cups')}")
# print(f" - Cakes           {totalBrought(allGuests, 'cakes')}")
# print(f" - Ham Sandwiches  {totalBrought(allGuests, 'ham sandwiches')}")
# print(f" - Apple Pies      {totalBrought(allGuests, 'apple pies')}")

# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# def displayInventory(inventory):
#     print("Inventory:")
#     item_total = 0
#     for k, v in inventory.items():
#         print(f"{v}  {k}")
#         item_total += v
#     print(f"Total number of items: {item_total}")
# displayInventory(stuff)

# print('That is Carol\'s cat')
# print("""Dear Alice,
# Eve's cat has benn arrested for catnapping, cat burglary, and extortion.
# Sincerely,
# Bob""")
# name = 'AI'
# age = 4000
# msg = 'My name is %s. I am %s years old' % (name, age)
# print(msg)
# spam = 'Hello, World!'
# print(spam.endswith('d!'))
# spam = ['cats', 'rats', 'bats']
# print('ABC'.join(spam))
# msg = 'My name is Simon.'
# print(msg.split())
# spam = 'Hello, world!'
# before, sep, after = spam.partition(' ')
# print(before)
# print(spam.center(100, '*'))

# def printPicnic(itemsDict, leftWidth, rightWidth):
#     print("PICNIC ITEMS".center(leftWidth + rightWidth, '-'))
#     for k, v in itemsDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
#
# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies':8000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)
# spam = '    Hello,World    '
# print(spam.strip())
# print(ord('A'))
# print(chr(65))
# import pyperclip
# pyperclip.copy('Hello')
# print(pyperclip.paste())


# TEXT = {'agree':"""Yes. I agree. That sounds fine to me.""",
#         'busy': """Sorry, can we do this later this week or next week?""",
#         'upsell': """Would you consider making this a monthly donation?"""}
# import sys
# import pyperclip
#
# if len(sys.argv) < 2:
#     print("Usage: python mclip.py [keyphrase] - copy phrase text")
#     sys.exit()
#
# keyphrase = sys.argv[1]    # first command line arg is the key
#
# if keyphrase in TEXT:
#     pyperclip.copy(TEXT[keyphrase])
#     print(f"Text for {keyphrase} copied to clipboard.")
# else:
#     print(f"There is no text for {keyphrase}")

# import pyperclip
#
# text = pyperclip.paste()
#
# lines = text.split('\n')
# for i in range(len(lines)):
#     lines[i] = '*' + lines[i]
# text = '\n'.join(lines)
# pyperclip.copy(text)


# print("Enter the English message to translate into Pig Latin:")
# message = input()
#
# VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
#
# pigLatin = []  # A list of the words in Pig Latin.
# for word in message.split():
#     # Separate the non-letters at the start of this world:
#     prefixNonLetters = ''
#     while len(word) > 0 and not word[0].isalpha():
#         prefixNonLetters += word[0]
#         word = word[1:]
#     if len(word) == 0:
#         pigLatin.append(prefixNonLetters)
#         continue
#
#     # Separate the non-letters at the end if this word:
#     suffixNonLetters = ''
#     while not word[-1].isalpha():
#         suffixNonLetters += word[-1]
#         word = word[:-1]
#
#     # Remember if the word was in uppercase or title case
#     wasUpper = word.isupper()
#     waeTitle = word.istitle()
#
#     word = word.lower() # Make the word lowercase for translation.
#
#     # Separate the consonants at the start of this word:
#     prefixNonLetters = ''
#     while len(word) > 0 and not word[0] in VOWELS:
#         prefixNonLetters += word[0]
#         word = word[1:]
#
#     # Add the pig Latin ending to the word:
#     if prefixNonLetters != '':
#         word += prefixNonLetters + 'ay'
#     else:
#         word += 'yay'
#
#     # Set the word back to uppercase or title case:
#     if wasUpper:
#         word = word.upper()
#     if waeTitle:
#         word = word.title()
#
#     # Add the non-letters back to the start or end of the word.
#     pigLatin.append(prefixNonLetters + word + suffixNonLetters)
#
# # Join all the words back together into a single string:
# print(' '.join(pigLatin))

# import re
# phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is (415) 555-4242.')
# print(mo.group(1))
# heroRegex = re.compile(r'Batman|Tina Fey')
# mo1 = heroRegex.search('Batman and Tina Fey.')
# print(mo1.group())
# mo2 = heroRegex.search('Tina Fey and Batman')
# print(mo2.group())
# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')
# print(mo.group(1))
# batRegex = re.compile(r'Bat(wo)*man')
# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group())
# mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group())
# mo3 = batRegex.search('The Adventures of Batwowowowowowowoman ')
# print(mo3.group())
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# print(mo)
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
# mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# print(mo)
# vowelRegex = re.compile(r'[^aeiouAEIOU]')
# mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
# print(mo)
# beginsWithHello = re.compile(r'^Hello')
# mo1 = beginsWithHello.search('Hello world!')
# print(mo1)
# mo2 = beginsWithHello.search('He said hello.')
# print(mo2)
# endsWithNumber = re.compile(r'\d$')
# mo = endsWithNumber.search('Your number is 42')
# print(mo)
# wholeStringIsNum = re.compile(r'^\d+$')
# mo = wholeStringIsNum.search('0123456789')
# print(mo)
# atRegex = re.compile(r'.at')
# mo = atRegex.findall('The cat in the hat sat on the flat mat.')
# print(mo)
# nameRagex = re.compile(r'First name: (.*) Last Name: (.*)')
# mo = nameRagex.search('First name: Al Last Name: Sweigart')
# print(mo.group(1))
# print(mo.group(2))
# print(mo.groups())
# nongreedyRegex = re.compile(f'<.*?>')
# mo = nongreedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())
# greedyRegex = re.compile(r'<.*>')
# mo = greedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())
# noNewlineRegex = re.compile('.*', re.DOTALL)
# mo = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.'
#                            '\nUphold the law')
# print(mo.group())
# robocop = re.compile(r'robocop', re.IGNORECASE)
# mo1 = robocop.search('RoboCop is part man, part machine, all cop.')
# print(mo1.group())
# mo2 = robocop.search('ROBOCOP protects the innocent.')
# print(mo2.group())
# namesRegex = re.compile(r'Agent \w+')
# mo = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
# print(mo)
# agentNamesRegex = re.compile(r'Agent (\w)\w*')
# mo = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
# print(mo)
# Finds phone numbers and email address on the clipboard

# import pyperclip
# import re
#
# phoneRegex = re.compile(r'''(
# (\d{3}|\(\d{3}\))?                  # area code
# (\s|-|\.)?                          # separator
# (\d{3})                             # first 3 digits
# (\s|-|\.)                           # separator
# (\d{4})                             # last 4 digits
# (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
# )''', re.VERBOSE)
#
# # TODO: Create email regex.
# emailRegex = re.compile(r'''(
# [a-zA-Z0-9._%+-]+       # username
# @                       # @ symbol
# [a-zA-Z0-9.-]+          # domain name
# (\.[a-zA-Z]{2,4})       # dot-something
# )''', re.VERBOSE)
#
# # TODO: Find matches in clipboard text.
# text = str(pyperclip.paste())
#
# matches = []
# for groups in phoneRegex.findall(text):
#     phoneNum = '-'.join([groups[1], groups[3], groups[5]])
#     if groups[8] != '':
#         phoneNum += ' x' + groups[8]
#     matches.append(phoneNum)
# for groups in emailRegex.findall(text):
#     matches.append(groups[0])
#
# # TODO: Copy results to the clipboard.
# if len(matches) > 0:
#     pyperclip.copy('\n'.join(matches))
#     print('Copied to clipboard:')
#     print('\n'.join(matches))
# else:
#     print('No phone numbers or email address found.')

# while True:
#     print("Enter your age:")
#     age = input()
#     try:
#         age = int(age)
#     except:
#         print("Please use numeric digits.")
#         continue
#     if age < 1:
#         print("Please enter a positive number.")
#         continue
#     break
#
# print(f"Your name is {age}.")

# import pyinputplus as pyip
# response = pyip.inputInt(prompt='Enter a number:')
# print(response)
# response = pyip.inputNum(prompt='Enter number:', min=4)
# print(response)
# response = pyip.inputNum(prompt='Enter number:', blank=True, limit=1, default='你好')
# print(response)
# response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
# print(response)
# response = pyip.inputNum(blockRegexes=[r'[02468]$'])
# print(response)
# response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])
# print(response)
# def addsUpToTen(numbers):
#     numbnerList = list(numbers)
#     for i, digit in enumerate(numbnerList):
#         numbnerList[i] = int(digit)
#     if sum(numbnerList) != 10:
#         raise Exception('The digits must add up to 10, not %s.'%(sum(numbnerList)))
#     return int(numbers)
#
# response = pyip.inputCustom(addsUpToTen)
# print(response)
# while True:
#     promote = "Want to know how to keep a person busy for hours?\n"
#     response = pyip.inputYesNo(promote)
#     if response == 'no':
#         break
#     print(response)
# import pyinputplus as pyip
# import random, time
# numberOfQuestions = 10
# correctAnswers = 0
# for questionNumber in range(numberOfQuestions):
#     # Pick two random numbers:
#     num1 = random.randint(0, 9)
#     num2 = random.randint(0, 9)
#
#     prompt = f'{questionNumber}: {num1} x {num2} = '
#     try:
#         # Right answers are handled by allowRegexes.
#         # Wrong answers are handled by blockRegexes, with a custom message.
#         pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
#                               blockRegexes=[('.*', 'Incorrect!')],
#                               timeout=3, limit=3)
#     except pyip.TimeoutException:
#         print("Out of time!")
#     except pyip.RetryLimitException:
#         print("Out of tries!")
#     else:
#         # This block runs if no exceptions were raised in the try block.
#         print("Correct!")
#         correctAnswers += correctAnswers
#     time.sleep(1)    # Brief pause to let user see the results.
# print(f"Score: {correctAnswers} / {numberOfQuestions}")



# from pathlib import Path
# print(str(Path('spam','bacon','eggs')))
# answer = Path('spam')/ 'bacon'/ 'eggs'
# print(answer)
# homeFolder = r'C:\Users\AI'
# subFolder = 'spam'
# response = homeFolder + '\\' + subFolder
# print(response)
# print('\\'.join([homeFolder, subFolder]))
# import os
# print(Path.cwd())
# print(Path.home())
# print(os.makedirs('C:\\delicious\\walnut\\waffles'))
# print(Path.cwd().is_absolute())
# p = Path('F:/pathon/LZY')
# print(p.glob('*.txt'))
# winDir = Path('C:/windows')
# notExistsDir = Path('C:/This/Folder/Does/Not/Exist.')
# calcFile = Path('C:/Windows/System32/calc.exe')
# print(winDir.exists())
# print(notExistsDir.exists())
# print(calcFile.is_file())
# print(calcFile.is_dir())
# dDrive = Path('D:/')
# print(dDrive.exists())
# p = Path('spam.txt')
# print(p.write_text('Hello, world!'))
# print(p.read_text())

# baconFile = open('bacon.txt', 'w')
# print(baconFile.write('Hello, world!\n'))
# import shelve
# shelveFile = shelve.open('mydata')
# cats = ['Zophie', 'Pooka', 'Simon']
# shelveFile['cats'] = cats
# shelveFile.close()
# shelfFile = shelve.open('mydata')
# print(type(shelfFile))
# print(shelfFile['cats'])

# import pprint
# cats = [{'name': 'zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
# print(pprint.pformat(cats))
# fileObj = open('myCats.py', 'w')
# fileObj.write(f'cats = {pprint.pformat(cats)} \n ')

# import random
#
# # The quiz data. Keys are states and values are their capitals.
# capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock',
#             'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
#             'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
#             'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
#             'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
#             'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
#             'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
#             'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
#             'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
#             'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
#             'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
#             'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
#             'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
#
# # Generate 35 quiz files.
# for quizNum in range(35):
#     # TODO: Create the quiz and answer key files.
#     quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
#     answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')
#
#     # TODO: Write out the header for quiz .
#     quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
#     quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
#     quizFile.write('\n\n')
#
#     # TODO: Shuffle the order of the states.
#     states = list(capitals.keys())
#     random.shuffle(states)
#
#     # TODO: Loop through all 50 states, making a question for each.
#     for questionNum in range(50):
#         # Get right and wrong answers.
#         correctAnswer = capitals[states[questionNum]]
#         wrongAnswers = list(capitals.values())
#         del wrongAnswers[wrongAnswers.index(correctAnswer)]
#         wrongAnswers = random.sample(wrongAnswers, 3)
#         answerOptions = wrongAnswers + [correctAnswer]
#         random.shuffle(answerOptions)
#
#         # TODO: Write the question and answer optionals to the quiz file.
#         quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
#         for i in range(4):
#             quizFile.write(f"    {'ABCD'[i]}.{  answerOptions[i]}\n")
#             quizFile.write('\n')
#
#         # TODO: Write the answer key to a file.
#         answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}")
#     quizFile.close()
#     answerKeyFile.close()

# import send2trash
# baconFile = open('bacon.txt', 'a')
# baconFile.write('Bacon is not a vegetable.')
# baconFile.close()
# send2trash.send2trash('bacon.txt')

# import os
# for folderName, subfolders, filenames in os.walk('F:\python\LZY'):
#     print(f'The current folder is {folderName}.')
#     for subfolder in subfolders:
#         print(f'SUBFOLDER OF {folderName} : {subfolder}')
#     for filename in filenames:
#         print(f'FILE INSIDE {folderName} : {filename}')
#     print('')
# import zipfile

# exampleZip = zipfile.ZipFile('F:\python\LZY\study_time\example.zip')
# print(exampleZip.namelist())
# spamInfo = exampleZip.getinfo('spam.txt')
# print(spamInfo.file_size)
# print(spamInfo.compress_size)
# print(f"Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller.")
# exampleZip.close()
# exampleZip = zipfile.ZipFile('F:\python\LZY\study_time\example.zip')
# exampleZip.extract('spam.txt')
# exampleZip.close()
# newZip = zipfile.ZipFile('new.zip', 'w')
# newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
# newZip.close()


# import shutil, os, re
# # Create a regex that maches files with the American data formate.
# datePattern = re.compile(r"""^(.*)? # all text before the date
# ((0|1)?\d)-# one or two digits for the month
# ((0|1|2|3)?\d)-# one or two digists for the day
# ((19|20)\d\d)# four digists for the year
# (.*?)$# all text after the date
# """, re.IGNORECASE)
#
# # TODO: Loop over the files in the working directory.
# for amerFilename in os.listdir('.'):
#     mo = datePattern.search(amerFilename)
#
# # TODO: Skip files without a date.
#     if mo == None:
#         continue
#
# # TODO: Get the difference parts of the filename.
#     beforePart = mo.group(1)
#     monthPart = mo.group(2)
#     dayPart = mo.group(4)
#     yearPart = mo.group(6)
#     afterPart = mo.group(8)
#
# # TODO: Form the European-style filename.
#     euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
#
# # TODO: Get the full, absolute file paths.
#     absWorkingDir = os.path.abspath('.')
#     amerFilename = os.path.join(absWorkingDir, amerFilename)
#     euroFilename = os.path.join(absWorkingDir, euroFilename)
#
# # TODO: Rename the files.
#     print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
#     shutil.move(amerFilename, euroFilename)    # uncomment after testing

# import zipfile, os
#
# def backupToZip(folder):
#     # Back up the entire contents of "folder" into a ZIP file.
#
#     folder = os.path.abspath(folder)    # make sure folder is absolute
#
#     # Figure out the filename this code should use based on
#     # what files already exist
#     number = 1
#     while True:
#         zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
#         if not os.path.exists(zipFilename):
#             break
#         number += 1
#
#     # TODO: Create the ZIP file.
#     print(f'Creating {zipFilename}...')
#     backupZip = zipfile.ZipFile(zipFilename, 'w')
#
#     # TODO: Walk the entire tree and compress the files in each folder.
#     for foldername, subfolers, filenames in os.walk(folder):
#         print(f'Adding files in {foldername}...')
#         # Add the current folder to the ZIP file.
#         backupZip.write(foldername)
#         # Add all the files in this folder to the ZIP file.
#         for filename in filenames:
#             newBase = os.path.basename(folder) + '_'
#             if filename.startswith(newBase) and filename.endswith('.zip'):
#                 continue    # don't back up ZIP files
#             backupZip.write(os.path.join(foldername, filename))
#     backupZip.close()
#     print('Done.')
#
# backupToZip('F:\\delicious')

# def boxPrint(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception('Symbol must be a single character string.')
#     if width <= 2:
#         raise Exception('Width must be greater than 2.')
#     if height <= 2:
#         raise Exception('Height must be greater than 2.')
#
#     print(symbol * width)
#     for i in range(height - 2):
#         print(symbol + (' ' * (width - 2)) + symbol)
#     print(symbol * width)
#
# for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('zz', 3, 3)):
#     try:
#         boxPrint(sym, w, h)
#     except Exception as err:
#         print(f'An exception happened: {err}')

# def spam():
#     bacon()
# def bacon():
#     raise Exception("This is the error message.")
#
# spam()

# import traceback
# try:
#     raise Exception('This is the error message.')
# except:
#     errorFile = open('errorInfo.txt', 'w')
#     errorFile.write(traceback.format_exc())
#     errorFile.close()
#     print('The traceback info was written to errorInfo.txt')

# ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
# ages.reverse()
# print(ages)
# assert(ages[0] <= ages[-1])

# market_2nd = {'ns': 'green', 'ew': 'red'}
# mission_16th = {'ns': 'red', 'ew': 'green'}
#
# def switchLights(stoplight):
#     for key in stoplight.keys():
#         if stoplight[key] == 'green':
#             stoplight[key] = 'yellow'
#         elif stoplight[key] == 'yellow':
#             stoplight[key] = 'red'
#         elif stoplight[key] == 'red':
#             stoplight[key] = 'green'
#     assert 'red' in stoplight.values, 'Neither light is red!' + str(stoplight)
#
# switchLights(market_2nd)

# import logging
# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug('Start of program')
#
# def factorial(n):
#     logging.debug('Start of factorial(%s%%)' % (n))
#     total = 1
#     for i in range(1, n + 1):
#         total *= i
#         logging.debug(f'i is {i}, total is {total}')
#     logging.debug('End of factorial(%s%%)' % (n))
#     return total
#
# print(factorial(5))
# logging.debug('End of program')

# import logging
# logging.basicConfig(filename='myprogram.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug('Some debugging details.')
# logging.info('The logging module is working.')
# logging.warning('An error message is about to be logged.')
# logging.error('An error has occurred.')
# logging.critical('The program is unable to cover!')
# print('Enter the first number to add:')
# first = input()
# print('Enter the second number to add:')
# second = input()
# print('Enter the third number to add:')
# third = input()
# print(f'The sum is {first + second + third}')
# import random
# heads = 0
# for i in range(1, 1001):
#     if random.randint(0, 1) == 1:
#         heads += 1
#     if i == 500:
#         print('Halfway done!')
# print(f'Headers came up {heads} times.')
# import random
# guess = ''
# while guess not in ('headers', 'tails'):
#     print('Guess the coin toss! Enter headers or tails:')
#     guess = input()
# toss = random.randint(0, 1)    # 0 is tails, 1 is headers.
# if toss == 0:
#     toss = 'tails'
# else:
#     toss = 'headers'
# if guess == toss:
#     print('You got it!')
# else:
#     print('Nope! Guess again!')
#     guess = input()
#     if toss == guess:
#         print('You got it!')
#     else:
#         print('Nope. You are really bad at this game.')

# import webbrowser
# webbrowser.open('https://www.csdn.net/')
# import sys, webbrowser
# import pyperclip
# if len(sys.argv) > 1:
#     # Get address from command line.
#     address = ' '.join(sys.argv[1:])
# else:
#     # TODO: Get address from clipboard.
#     address = pyperclip.paste()
#
# webbrowser.open(f'https://www.google.com/maps/place/{address}')
# import requests
# res = requests.get('https://www.baidu.com/')
# print(res)
# import bs4
# soup = bs4.BeautifulSoup(open('F:\python\LZY\study_time\example.html'), 'html.parser')
# elems = exampleSoup.select('#author')
# print(type(elems))
# print(len(elems))
# print(type(elems[0]))
# print(str(elems[0]))
# print(elems[0].getText())
# print(elems[0].attrs)
# pElems = exampleSoup.select('p')
# print(str(pElems[0].getText()))
# print(str(pElems[1].getText()))
# print(str(pElems[2].getText()))
# spanElem = soup.select('span')[0]
# print(str(spanElem))
# print(spanElem.get('id'))
# print(spanElem.get('some_nonexistent_addr') == None)
# print(spanElem.attrs)
# import requests, sys, webbrowser, bs4
#
# print('Searching...') # display text while downloading the search result page
# res = requests.get('http://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
# res.raise_for_status()
#
# soup = bs4.BeautifulSoup(res.text, features='html.parser')
# linkElems = soup.select('.package-snippet')
# numOpen = min(5, len(linkElems))
# for i in range(numOpen):
#     urlToOpen = 'http://pypi.org' + linkElems[i].get('href')
#     print('Opening', urlToOpen)
#     webbrowser.open(urlToOpen)

# import requests, os, bs4
#
# url = 'https://xkcd.com/'    # starting the url
# os.makedirs('xkcd', exist_ok=True)    # store comics in ./xkcd
# while not url.endswith('#'):
#     # TODO: Download the page.
#     print('Download page %s...' % url)
#     res = requests.get(url)
#     res.raise_for_status()
#
#     soup = bs4.BeautifulSoup(res.text, 'html.parser')
#
#     # TODO: Find the URL of the comic image.
#     comicElem = soup.select('#comic img')
#     if comicElem == []:
#         print('Could not find comic image.')
#     else:
#         comicUrl = 'https:' + comicElem[0].get('src')
#
#         # TODO: Download the image.
#         print('Downloading image...%s' % (comicUrl))
#         res = requests.get(comicUrl)
#         res.raise_for_status()
#
#         # TODO: Save the image to ./xkcd.
#         imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
#         for chunk in res.iter_content(100000):
#             imageFile.write(chunk)
#         imageFile.close()
#
#         # TODO: Get the Prev button's url.
#         prevLink = soup.select('a[rel="prev"]')[0]
#         url = 'https://xkcd.com/' + prevLink.get('href')
#
# print('Done.')

# from selenium import webdriver
# broswer = webdriver.Edge()
# broswer.get('https://inventwithpython.com/')
# try:
#     elem = broswer.find_element('class name', ' cover-thumb')
#     print('Found <%s> element with that class name!' % (elem.tag_name))
# except:
#     print('Was not able to find an element with that name.')

# from selenium import webdriver
# broswer = webdriver.Edge()
# broswer.get('https://inventwithpython.com/')
# linkElem = broswer.find_element('link text','Read Online for Free')
# type(linkElem)
# linkElem.click()    # follows the "Read Online for Free" link

# from selenium import webdriver
# broswer = webdriver.Edge()
# broswer.get('https://www.waves.com/login')
# userElem = broswer.find_element('by id', 'username')
# userElem.send_keys('123')
#
# passwordElem = broswer.find_element('by id', 'password')
# passwordElem.send_keys('123')
# passwordElem.submit()

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# broswer = webdriver.Edge()
# broswer.get('')
# htmlElem = broswer.find_element('tag mane', 'html')
# htmlElem.send_keys(Keys.END)
# htmlElem.send_keys(Keys.HOME)

# import time
# from selenium import webdriver
# browser = webdriver.Edge()
# browser.get('https://www.baidu.com')
# time.sleep(4)
# searchElem = browser.find_element('id', 'kw')
# searchElem.send_keys('qq音乐')
# linkElem = browser.find_element('id', 'su')
# linkElem.click()
# time.sleep(10)
# qqmusicElem = browser.find_element('xpath', '//*[@id="1"]/div/div[1]/h3/a[1]')
# qqmusicElem.click()
# time.sleep(10)

# import openpyxl
# wb = openpyxl.load_workbook('F:\python\LZY\study_time\example.xlsx')
# sheet = wb['Sheet1']
# print(sheet.max_row)
# print(type(sheet.max_row))

# import openpyxl
# from openpyxl.utils import get_column_letter, column_index_from_string
# print(get_column_letter(1))
# print(column_index_from_string('A'))
# wb = openpyxl.load_workbook('F:\python\LZY\study_time\example.xlsx')
# sheet = wb['Sheet1']
# print(get_column_letter(sheet.max_column))

# import openpyxl
# wb = openpyxl.load_workbook('F:\python\LZY\study_time\example.xlsx')
# sheet = wb['Sheet1']
# print(tuple(sheet['A1':'C3']))
# for rowOfCellObjects in sheet['A1':'C3']:
#     for cellObj in rowOfCellObjects:
#         print(cellObj.coordinate, cellObj.value)
#     print('--- END OF ROW ---')

# import openpyxl
# wb = openpyxl.load_workbook('F:\python\LZY\study_time\example.xlsx')
# sheet = wb.active
# list_column = list(sheet.columns)[1]
# print(list_column)
# for cellobj in list_column:
#     print(cellobj.value)


# import openpyxl, pprint
# print('Opening workbook...')
# wb = openpyxl.load_workbook('F:\python\LZY\study_time\censuspopdata.xlsx')
# sheet = wb.active
# countryData = {}
#
# # TODO: Fill in countyData with each country's population and tracts.
# print('Loading rows...')
# for row in range(2, sheet.max_row + 1):
#     # Each row in the spreadsheet has data for one census tract.
#     state = sheet['B' + str(row)].value
#     country = sheet['C' + str(row)].value
#     pop = sheet['D' + str(row)].value
#     # Make sure the key for this state exists.
#     countryData.setdefault(state, {})
#     # Make sure the key for this country state exists.
#     countryData[state].setdefault(country, {'tracts': 0, 'pop': 0})
#     # Each row represents one census tract, so increment by one.
#     countryData[state][country]['tracts'] += 1
#     # Increase the country pop by the pop in this census tract.
#     countryData[state][country]['pop'] += int(pop)
#
# # TODO: Open a new text file and write the contents of countryData to it.
# print('Writing results...')
# resultFile = open('census2010.py', 'w')
# resultFile.write(f'allData = {pprint.pformat(countryData)}')
# resultFile.close()
# print('Done.')

# import openpyxl
# wb = openpyxl.Workbook() # Create a blank workbook.
# print(wb.sheetnames) # It starts with one sheet.
# sheet = wb.active
# print(sheet.title)
# sheet.title = 'Spam Bacon Eggs Sheet' # Change title
# print(wb.sheetnames)
# import openpyxl
# wb = openpyxl.load_workbook('F:\python\LZY\study_time\example.xlsx')
# sheet = wb.active
# sheet.title = 'Spam Spam Spam'
# wb.save('example_copy.xlsx') # Save the workbook
# import openpyxl
# wb = openpyxl.Workbook()
# print(wb.sheetnames)
# print(wb.create_sheet()) # Add a new sheet
# print(wb.sheetnames)
# # Creat a new sheet at index 0.
# wb.create_sheet(index=0, title='First sheet')
# print(wb.sheetnames)
# wb.create_sheet(index=2, title='Middle sheet')
# print(wb.sheetnames)
# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb['Sheet']
# sheet['A1'] = 'Hello, World!' # Edit the cell's value
# print(sheet['A1'].value)

# import openpyxl
# wb = openpyxl.load_workbook('F:\python\LZY\study_time\censuspopdata.xlsx')
# sheet = wb['Population by Census Tract']
#
# # The peoduces types and their updated prices.
# PRICE_UPDATES = {
#     'Garlic': 3.07,
#     'Celery': 1.19,
#     'Lemon': 1.27,
# }
#
# # TODO: Loop through the rows and update the prices.
# for rowNum in range(2, sheet.max_row): # skip the first row
#     produceName = sheet.cell(row=rowNum, column=1).value
#     if produceName in PRICE_UPDATES:
#         sheet.cell(row=rowNum, column=2).value = PRICE_UPDATES[produceName]
#
# wb.save('updateProduceSales.xlsx')

# from openpyxl.styles import Font
# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb['Sheet']
# italic24Font = Font(size=24, italic=True) # Create a font
# sheet['A1'].font = italic24Font # Apply the font to A1.
# sheet['A1'] = 'Hello, world!'
# wb.save('styles.xlsx')
# from openpyxl.styles import Font
# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active
#
# fontObj1 = Font(name='Times New Roman', bold=True)
# sheet['A1'].font = fontObj1
# sheet['A1'] = 'Blod Times New Roman'
#
# fontObj2 = Font(size=24, italic=True)
# sheet['B3'].font = fontObj2
# sheet['B3'] = '24 pt Italic'
#
# wb.save('styles.xlsx')
# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet['A1'] = 200
# sheet['A2'] = 300
# sheet['A3'] = '=sum(A1:A2)' # Set the formula.
# wb.save('writeFormula.xlsx')
# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet['A1'] = 'Tall row'
# sheet['B2'] = 'Wide column'
# # Set the height and width:
# sheet.row_dimensions[1].height = 70
# sheet.column_dimensions['B'].width = 20
# wb.save('dimensions.xlsx')
# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet.merge_cells('A1:D3') # Merge all these cells.
# sheet['A1'] = 'Twelve cells merged together.'
# sheet.merge_cells('C5:D5') # Merge these two cells.
# sheet['C5'] = 'Two merged cells'
# sheet.unmerge_cells('A1:D3')
# wb.save('merged.xlsx')
# import openpyxl
# wb = openpyxl.load_workbook('F:\python\LZY\study_time\produceSales.xlsx')
# sheet = wb.active
# sheet.freeze_panes = 'A3' # Freeze the rows above A2.
# sheet.freeze_panes = 'B1'
# wb.save('freezeExample.xlsx')

# import openpyxl
# wb = openpyxl.Workbook()
# sheet = wb.active
# for i in range(1, 11): # create some data in column A.
#     sheet['A' + str(i)] = i
#
# refObj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
# seriesObj = openpyxl.chart.Series(refObj, title='First series')
#
# chartObj = openpyxl.chart.BarChart()
# chartObj.title = 'My chart'
# chartObj.append(seriesObj)
#
# sheet.add_chart(chartObj, 'C5')
# wb.save('sampleChart.xlsx')

# import openpyxl
# from openpyxl.styles import Font
# wb = openpyxl.Workbook()
# sheet = wb.active
# print("Please write an number:")
# number = input()
# for i in range(1, int(number) + 1):
#     sheet.cell(row=1, column=i+1).value = i
#     sheet['A' + str(i + 1)] = i
#     fontObj = Font(bold=True)
#     sheet['A' + str(i + 1)].font = fontObj
#     sheet.cell(row=1, column=i + 1).font = fontObj
#
# for j in range(1, int(number) + 1):
#     for k in range(1, int(number) + 1):
#         sheet.cell(column=j+1, row=k+1).value = (j*k)
#
# sheet.freeze_panes = 'A2'
# wb.save('multiplicationTable.xlsx')

# import PyPDF2
# pdfFileObj = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# pageObj = pdfReader.getPage(0)
# print(pageObj.extractText())
# pdfFileObj.close()

# import PyPDF2
# pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
# pdfReader.decrypt('rosebud')
# print(pdfReader.getPage(0).extractText())

# import PyPDF2
# pdf1File = open('meetingminutes.pdf', 'rb')
# pdf2File = open('meetingminutes2.pdf', 'rb')
# pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
# pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
# pdfWriter = PyPDF2.PdfFileWriter()
#
# for pageNum in range(pdf1Reader.numPages):
#     pageObj = pdf1Reader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)
#
# for pageNum in range(pdf2Reader.numPages):
#     pageObj = pdf2Reader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)
#
# pdfOutputFile = open('combineminutes.pdf', 'wb')
# pdfWriter.write(pdfOutputFile)
# pdfOutputFile.close()
# pdf1File.close()
# pdf2File.close()

# import openpyxl
# minutesFile = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(minutesFile)
# page = pdfReader.getPage(0)
# page.rotateCounterClockwise(90)
# pdfWriter = PyPDF2.PdfFileWriter()
# pdfWriter.addPage(page)
# resultPdfFile = open('rotatedCounterPage.pdf', 'wb')
# pdfWriter.write(resultPdfFile)
# resultPdfFile.close()
# minutesFile.close()

# import PyPDF2
# minutesFile = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(minutesFile)
# minutesFirstPage = pdfReader.getPage(0)
# pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
# minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
# pafWriter = PyPDF2.PdfFileWriter()
# pafWriter.addPage(minutesFirstPage)
#
# for pageNum in range(1, pdfReader.numPages):
#     pageObj = pdfReader.getPage(pageNum)
#     pafWriter.addPage(pageObj)
#
# resultPdfFile = open('watermarkedCover.pdf', 'wb')
# pafWriter.write(resultPdfFile)
# minutesFile.close()
# resultPdfFile.close()

# import PyPDF2
# pdfFile = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFile)
# pdfWiter = PyPDF2.PdfFileWriter()
# for pageNum in range(pdfReader.numPages):
#     pdfWiter.addPage(pdfReader.getPage(pageNum))
#
# pdfWiter.encrypt('swordfish')
# resultPdf = open('encryptedminutes.pdf', 'wb')
# pdfWiter.write(resultPdf)
# resultPdf.close()

# import PyPDF2, os
# # Get all the PDF filenames
# pdfFiles = []
# for filename in os.listdir('.'):
#     if filename.endswith('.pdf'):
#         pdfFiles.append(filename)
# pdfFiles.sort(key=str.lower)
#
# pdfWriter = PyPDF2.PdfFileWriter()
#
# # TODO: Loop through all the PDF files.
# for filename in pdfFiles:
#     pdfFileObj = open(filename, 'rb')
#     pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#
#     # TODO: Loop through all the pages (except the first) and add them.
#     for pageNum in range(1, pdfReader.numPages):
#         pageObj = pdfReader.getPage(pageNum)
#         pdfWriter.addPage(pageObj)
#
# # TODO: Save the resulting PDF to a file.
# pdfOutput = open('allminutes.pdf', 'wb')
# pdfWriter.write(pdfOutput)
# pdfOutput.close()

# import docx
# doc = docx.Document('demo.docx')
# print(len(doc.paragraphs))
# print(doc.paragraphs[0].runs[0].text)
# import docx
#
# def getText(filename):
#     doc = docx.Document(filename)
#     fullText = []
#     for para in doc.paragraphs:
#         fullText.append(' ' + para.text)
#     return '\n'.join(fullText)
#
# print(getText('demo.docx'))

# import PyPDF2
#
# file = open('dictionary.txt', 'r')
#
# pdfReader = PyPDF2.PdfFileReader(open('F:\python\LZY\study_time\encryptedminutes.pdf', 'rb'))
# dictionary = []
# for line in file.readlines():
#     dictionary.append(line.rstrip())
#     dictionary.append(line.rstrip().lower())
#
# for word in dictionary:
#     number = pdfReader.decrypt(word)
#     if number == 1:
#         print(f"The password: {word}")
#         break
# file.close()

# import csv
# exampleFile = open('F:\python\LZY\study_time\example.csv')
# exampleReader = csv.reader(exampleFile)
# for row in exampleReader:
#     print(f"Row #{str(exampleReader.line_num)} {str(row)}")

# import csv
# outputFile = open('output.csv', 'w', newline='')
# outputWriter = csv.writer(outputFile)
# outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
# outputWriter.writerow(['hello, world!', 'eggs', 'bacon', 'ham'])
# outputWriter.writerow([1, 2, 3.1415926, 4])
# outputFile.close()

# import csv
# csvFile = open('example.tsv', 'w', newline='')
# csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
# csvWriter.writerow(['apples', 'oranges', 'grapes'])
# csvWriter.writerow(['eggs', 'oranges', 'grapes'])
# csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
# csvFile.close()

# import csv
# exampleFile = open('F:\python\LZY\study_time\exampleWithHeader.csv')
# exampleDictReader = csv.DictReader(exampleFile)
# for row in exampleDictReader:
#     print(row['Timestamp'], row['Fruit'], row['Quantity'])

# import csv, os
#
# os.makedirs('headerRemoved', exist_ok=True)
#
# # Loop through every file in the current working directory.
# for csvFilename in os.listdir('.'):
#     if not csvFilename.endswith('.csv'):
#         continue    # skip non-csv files
#
#     print(f'Removing header from {csvFilename} ...')
#
#     # TODO: Read the csv file in (skipping first row).
#     csvRows = []
#     csvFileObj = open(csvFilename)
#     readerObj = csv.reader(csvFileObj)
#     for row in readerObj:
#         if readerObj.line_num == 1:
#             continue    # skip first row
#         csvRows.append(row)
#     csvFileObj.close()
#
#     # TODO: Write out the csv file.
#     csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
#     csvWriter = csv.writer(csvFileObj)
#     for row in csvRows:
#         csvWriter.writerow(row)
#     csvFileObj.close()

# import json
# stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught":0, "felineIQ": null}'
# print(json.loads(stringOfJsonData))
# pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
# stringOfJsonData = json.dumps(pythonValue)
# print(stringOfJsonData)

# import time
# print(time.time())
# import time
# import sys
# def calcProud():
#     # Calculate the product of the first 100000 numbers.
#     product = 1
#     for i in range(1, 100000):
#         product = product * i
#     return product
#
# startTime = time.time()
# prod = calcProud()
# endTime = time.time()
# sys.set_int_max_str_digits(10000000)
# print(f"The result is {len(str(prod))} digits long.")
# print(f"Took {endTime - startTime} seconds to calculate")
# import time
# print(time.ctime())

# import time
#
# # Display the program's instructions.
# print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
# input()
# print('Started.')
# startTime = time.time()
# lastTime = startTime
# lapNum = 1
#
# # TODO: Start tracking the lap times.
# try:
#     while True:
#         input()
#         lapTime = time.time() - lastTime
#         totalTime = time.time() - startTime
#         print(f'Lap #{lapNum}: {totalTime} ({lapTime})', end='')
#         lapNum += 1
#         lastTime = time.time()    # Reset the last lap time.
# except KeyboardInterrupt:
#     print('\nDone.')

# import datetime
# delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
# print(str(delta))
# dt = datetime.datetime.now()
# print(dt)
# thousands = datetime.timedelta(days=1000)
# print(dt + thousands)

# import threading, time
# print('Start of program.')
#
# def takeANap():
#     time.sleep(5)
#     print('Wake up!')
#
# threadObj = threading.Thread(target=takeANap)
# threadObj.start()
#
# print('End of program.')
# import threading
# threadObj = threading.Thread(target=print, args=['Cats', 'Dogs','Frogs'], kwargs={'sep':' & '})
# threadObj.start()

# import subprocess
# paintProc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')
# print(paintProc.poll() == None)
# paintProc.wait()
# paintProc.poll()
# import subprocess
# fileObj = open('hello.txt', 'w')
# fileObj.write('hello, world')
# fileObj.close()
# subprocess.Popen(['start', 'hello.txt'], shell=True)

# import time, threading
#
# timeLeft = 60
# while timeLeft > 0:
#     print(timeLeft, end='')
#     time.sleep(1)
#     timeLeft -= timeLeft
#
# # TODO: At the end of the countdown, play a sound file.
#     subprocess.Popen(['start', 'alarm.wav'], shell=True)

# from PIL import ImageColor
# print(ImageColor.getcolor('red', 'RGBA'))
# from PIL import Image
# catIm = Image.open('F:\python\LZY\study_time\zophie.png')
# print(catIm.format_description)
# catIm.save('zophie.jpg')
# from PIL import Image
# im = Image.new('RGBA', (100, 200), 'purple')
# im.save('purpleImage.png')
# im2 = Image.new('RGBA', (20, 20))
# im2.save('transparentImage.png')
# from PIL import Image
# catIm = Image.open('F:\python\LZY\study_time\zophie.png')
# croppedIm = catIm.crop((335, 345, 565, 560))
# croppedIm.save('cropped.png')
# from PIL import Image
# catIm = Image.open('F:\python\LZY\study_time\zophie.png')
# width, height = catIm.size
# quartersize = catIm.resize((int(width / 2), int(height / 2)))
# quartersize.save('quartersized.png')
# svelteIm = catIm.resize((width, height + 300))
# svelteIm.save('svelteIm.png')
#
#
# import pyautogui
# wh = pyautogui.size()
# print(wh)

# import pyautogui
# for i in range(10):    # Move mouse in a square.
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)
# import pyautogui
# for i in range(10):
#     pyautogui.move(100, 0, duration=0.25)
#     pyautogui.move(0, 100, duration=0.25)
#     pyautogui.move(-100, 0, duration=0.25)
#     pyautogui.move(0, -100, duration=0.25)
# import pyautogui
# pyautogui.click(10, 5)
# import pyautogui, time
# time.sleep(5)
# pyautogui.click()    # Click to make the window active.
# distance = 600
# change = 20
# while distance > 0:
#     pyautogui.drag(distance, 0, duration=0.2)    # Move right.
#     distance = distance - change
#     pyautogui.drag(0, distance, duration=0.2)    # Move down.
#     pyautogui.drag(-distance, 0, duration=0.2)    # Move left.
#     distance = distance - change
#     pyautogui.drag(0, -distance, duration=0.2)    # Move up.
# import pyautogui
# pyautogui.mouseInfo()
# import pyautogui
# print(pyautogui.pixel(50, 200))
# print(pyautogui.pixelMatchesColor(50, 200, (75, 79, 82)))
# b = pyautogui.locateOnScreen('F:\python\LZY\study_time\屏幕截图_20230203_142109.png')
# pyautogui.click(1600, 639, 522, 404)
# print(pyautogui.getAllTitles())
# import pyautogui
# fw = pyautogui.getActiveWindow()
# fw.minimize()
# import pyautogui, time
# pyautogui.click(1100, 500)
# time.sleep(2)
# pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y'], 0.25)
# import pyautogui
# print(pyautogui.KEYBOARD_KEYS)
# import pyautogui
# pyautogui.sleep(3)
# pyautogui.countdown(10)
# print('Starting in ', end='');pyautogui.countdown(3)
# import pyautogui
# pyautogui.alert('This is a message.', 'Important')
# pyautogui.confirm('Do you want to continue?')
# print(pyautogui.prompt("What's your cat's name?"))
# print(pyautogui.password('What is the password'))
