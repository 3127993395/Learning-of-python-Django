# message = "hello world"
# print(message)
# message = "Liu zhuyi"
# print(message)
# name = "ada lovelace"
# print(name.title())
# name = "ada lovelace"
# print(name.upper())
# print(name.lower())
# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# print(full_name)
# first_name = "ada"
# second_name = "lovelace"
# full_name = f"{first_name} {second_name}"
# print(f"hello{full_name.title()}!")
# first_name = "ada"
# second_name = "lovelace"
# full_name = f"{first_name} {second_name}"
# message = f"hello,{first_name} {second_name}" f:连接
# print(message)
# print("python")
# print("\tpython")           打印空格\t     换行\n
# print("language:\nEnglish\nChinese\ncanadian")
# favorite_language = '   python   '
# favorite_language.rstrip()    .rstrip()删除右边空白right
# ' python'
# favorite_language.lstrip()    .lstrip()删除左边空白left
# 'python '
# favorite_language.strip()      .strip()删除两边空白
# 'python'
# favorite_language = '   python   '
# favorite_language = favorite_language.strip()
# print(favorite_language)
# message = "One of Pathon's strengths is its diverse community."
# print(message)
# first_name = "Hello Eric,"
# last_name = "would you like to learn some Python today?"
# print(f"{first_name} {last_name}")
# first_name = "Liu"
# last_name = "Zhuyi"
# message = (f"{first_name} {last_name}")
# print(message.title())
# print(message.upper())
# print(message.lower())
# first_name = "Albert Einstein"
# second_name = "\tonce said,"
# last_name = '"A person who never made a mistake nevear tried anything new."'
# message = (f"{first_name}{second_name}{last_name}")
# print(message)
# first_name = "  Liu\n  "
# first_name = first_name.strip()
# last_name = "  Zhuyi  "
# last_name = last_name.strip()
# message = (f"{first_name}{last_name}")
# print(message)
# a=1+2+3
# print(a)
# b=sum([1,2,3])
# print(b)
# a=0.1+0.2
# print(a)
# print(2+3)
# bicycles = ['trek','cannondale','redline','specialized']
# print(bicycles[0].title())
# print(bicycles[1].title())
# print(bicycles[2].title())
# print(bicycles[3].title())
# print(bicycles[-1].title())
# bicycles = ['trek','cannondale','redline','specialized']
# message = f"My first bicycle was a {bicycles[0].title()}."
# print(message)
# names = ['刘朱熠','小王','张三李四']
# message = f"My name is {names[2].title()}."
# print(message)
# names = ['刘朱熠','小王','张三李四']
# message = f"{names[0]}你好"
# print(message)
# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)
# motorcycles[1] = 'ducati'
# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)
# motorcycles.append('ducati')                                                                                           .append()在列表最后添加
# print(motorcycles)
# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)
# motorcycles = ['honda','yamaha','suzuki']
# motorcycles.insert(0,'ducati')                                                                                         .insert在指定列表前添加新元素
# print(motorcycles)
# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles)
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# del motorcycles[0]
# print(motorcycles)
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# message = motorcycles.pop()
# print(motorcycles)
# print(message)
# motorcycles = ['honda', 'yamaha', 'suzuki']
# last_owned = motorcycles.pop(0)
# print(f"The last motorcycles I owned was a {last_owned.title()}")
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# motorcycles.remove('suzuki')
# print(motorcycles)
# motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
# print(motorcycles)
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"\nA {too_expensive.title()} is too expensive for me.")
# 练习3-4 3-5 3-6 3-7（自己写的）
# names = ['dad','mom','grandfather']
# message0 = f"{names[0].title()},welcome to the party!"
# message1 = f"{names[1].title()},welcome to the party!"
# message2 = f"{names[2].title()},welcome to the party!"
# print(message0)
# print(message1)
# print(message2)
# message4 = f"However {names[0].title()} can't come to the party."
# print(message4)
# names.remove('dad')
# names.insert(0,'grandmother')
# message5 = f"{names[0].title()} will instead my dad."
# print(message5)
# message6 = "I find a bigger table."
# print(message6)
# names.insert(0,'unlce')
# names.insert(1,'sister')
# names.append('brother')
# message7 = f"{names[0].title()},welcome to the party!"
# message8 = f"{names[1].title()},welcome to the party!"
# message9 = f"{names[2].title()},welcome to the party!"
# message10 = f"{names[3].title()},welcome to the party!"
# message11 = f"{names[4].title()},welcome to the party!"
# print(message7)
# print(message8)
# print(message9)
# print(message10)
# print(message11)
# message12 = "The new table can't send on time.\nI can only invite two people."
# print(message12)
# 网上答案3-7
# print('龙虎山罗天大醮答谢晚宴名单：')
# invites = ['张楚岚', '冯宝宝', '夏禾', '王也']
# for invite in invites:
#     print(f'\t-{invite}')
# print('乖乖，酒店还有更大的桌子，继续摇人摇人！！')
# invites.insert(0, '徐四')
# invites.insert(3, '风沙燕')
# invites.append('陆静')
# print('修改后的嘉宾名单：')
# for invite in invites:
#     print(f'\t-{invite}')
# print('酒店只剩一张小桌子了，只能邀请两人。')
# name = invites.pop()
# print(f'{name}，抱歉不能一起吃饭了，下次有机会聚。')
# name = invites.pop()
# print(f'{name}，抱歉不能一起吃饭了，下次有机会聚。')
# name = invites.pop()
# print(f'{name}，抱歉不能一起吃饭了，下次有机会聚。')
# name = invites.pop()
# print(f'{name}，抱歉不能一起吃饭了，下次有机会聚。')
# name = invites.pop()
# print(f'{name}，抱歉不能一起吃饭了，下次有机会聚。')
# print(invites)
# for invite in invites:
#     print(f'{invite}，很高兴可以共进晚餐。')
# del(invites[0])
# del(invites[0])
# print(invites)
# 自己写3-7
# print('Sorry,I can only invite two people.')
# names = ['dad','mom','sister','brother']
# print(f"{names.pop(0).title()},sorry.")
# print(f"{names.pop(0).title()},sorry.")
# print(f"{names[0].title()},you are still invited.")
# print(f"{names[1].title()},you are still invited.")
# del names[0]
# del names[1]
# print(names)
# cars = ['bmw','audi','toyota','subaru']
# cars.sort()                                                                                                           .sort按字母顺序排序（永久）
# print(cars)
# cars.sort(reverse=True)
# print(cars)
# cars = ['bmw','audi','toyota','subaru']
# print("Here is the original list:")
# print(cars)
# print("\nHere is the sorted list:")
# print(sorted(cars))                                                                                                      .sorted按临时字母顺序排序
# print("\nHere is the original list again:")
# print(cars)
# cars = ['bmw','audi','toyota','subaru']
# print(cars)
# cars.reverse()                                                                                                         .reserve不按字母，反转顺序
# print(cars)
# cars = ['bmw','audi','toyota','subaru']
# print(len(cars))
# 练习3-8 3-9 3-10
# tourist_attractions = ['beijing','tianjing','chongqing','changsha','nantong']
# print("Here is the original list:")
# print(tourist_attractions)
# print("Here is the sorted list:")
# print(sorted(tourist_attractions))
# print("Here is the original list:")
# print(tourist_attractions)
# print("Here is the reserve list:")
# tourist_attractions.reverse()
# print(tourist_attractions)
# print("Here is the aort list:")
# print(sorted(tourist_attractions))
# print("Here is the sort(reverse=true) list:")
# tourist_attractions.sort(reverse=True)
# print(tourist_attractions)
# print(len(tourist_attractions))
# magicians = ['alice','david','carolina']
# for magicians in  magicians:
#     print(magicians)
# magicians = ['alice','david','carolina']
# for magicians in magicians:
#     print(f"{magicians.title()},that was a great trick!")
#     print(f"I can't wait to see you next trick,{magicians.title()}\n")
# print("Thankyou,everyone.That's was a good magic show!")
# pizzas = ['one','two','three']
# for pizzas in pizzas:
#     print(f"I like {pizzas}!")
# print("I really like pizzas!")
# animals = ['dog','cat','pig']
# for animals in  animals:
#     print(f"A {animals} would make a great pet!")
# print("Any of these animals would make a great animal!")
# for value in range(-1,6):                                                                                              -1<=x<6
#     print(value)
# numbers = list(range(1,6))
# print(numbers)
# even_numbers = list(range(2,11,3))
# print(even_numbers)
# squares = []
# for value in range(1,11):
#     squares.append(value**2)
# print(squares)
# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# squares = [value**2 for value in range(1,11)]
# print(squares)
# numbers = [value**3 for value in range(1,100)]
# print(numbers)
# numbers = [value for value in range(1,1000000)]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# numbers = [value for value in range(1,21,2)]
# print(numbers)
# numbers = [value for  value in range(3,20,3)]
# print(numbers)
# numbers = [value**3 for value in range(1,11)]
# print(numbers)
# playes = ['caerles','martina','michael','florence','eli']
# print(playes[0:3])                                                                                                       0<=x<3
# print(playes[-3:])
# print(playes[0:4:2])
# playes = ['caerles','martina','michael','florence','eli']
# print("Here are the first three players on my team:")
# for player in playes[:3]:
#     print(player.title())
# my_foods = ['pizza','falafel','carrot cake']
# friends_foods = my_foods[:]
# my_foods.append('cannoli')
# friends_foods.append('ice cream')
# print(f"My favorite foods are:\n{my_foods}")
# print(f"\nMy friend's favorite foods are:\n{friends_foods}")
# my_foods = ['pizza','falafel','carrot cake','cannoli','ice cream']
# print(f"The first three items in the list are:")
# for my_food in my_foods[-3:]:
#     print(my_food)
# my_foods = ['pizza','falafel','carrot cake','cannoli','ice cream']
# friends_foods = my_foods[:]
# my_foods.append('drink')
# friends_foods.append('water')
# for my_foods in my_foods:
#     print(f"My favorite pizzas are:{my_foods}")
# for friends_foods in  friends_foods:
#     print(f"My friend's favorite pizzas are:{friends_foods}")
# dimensions = (200,50)
# for dimensions in dimensions:
#     print(dimensions)
# dimensions = (200,50)
# print("Qriginal dimensions:")
# for dimensions in dimensions:
#     print(dimensions)
# dimensions = (400,100)
# print("\nModified dimensions:")
# for dimensions in dimensions:
#     print(dimensions)
# foods = ("pizza","cake","bread")
# print("\nQriginal foods")
# for foods in foods:
#     print(foods)
# foods = ("fruit","cake","bread")
# print("\nModified foods:")
# for foods in foods:
#     print(foods)
# cars = ['audi','bmw','subaru','toyato']
# for car in  cars:
#    if car == 'bmw':
#          print(car.upper())
#    else:
#         print(car.title())
# car = 'audi'
# print(car == 'bmw')
# car = 'Audi'
# print(car.lower() == 'audi')
# requested_topping = 'mushrooms'
# if requested_topping !='anchovies':
#     print("Hold the anchovies")
# age = 18
# print(age == 18)
# age_0 = 22
# age_1 = 18
# print(age_0 >=21 and age_1>=21)
# age_1 = 22
# print(age_0 >=21 and age_1>=21)
# requested_toppings =['mushrooms','onions','pineapple']
# print('mushrooms' in requested_toppings)
# print('pepperoin' in requested_toppings)
# banned_used = ['andrew','carolina','david']
# user = 'marie'
# if user not in banned_used:
#     print(f"{user.title()},you can post a response if you wish.")
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# age = 17
# if age >=18:
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")
# else:
#     print("Sorry,you are too young to vote.")
#     print("please register to vote as soon as you turn 18!")
# age = 19
# if age < 4:
#     print("You admission cost is $0.")
# elif age <18:
#     print("Your admission cost is $25.")
# else:
#     print("Your admission cost is $40.")
# age = 19
# if age < 4:
#     price = 0
# elif age <18:
#     price = 25
# else:
#     price = 40
# print(f"Your admission cost is ${price}.")
# age = 19
# if age < 4:
#     price = 0
# elif age <18:
#     price = 25
# elif age <65:
#     price = 40
# else:
#     price = 20
# print(f"Your admission cost is ${price}.")
# age = 66
# if age < 4:
#     price = 0
# elif age <18:
#     price = 25
# elif age <65:
#     price = 40
# elif age >=65:
#     price = 20
# print(f"Your admission cost is ${price}.")
# requested_toppings = ['mushroom','extra cheese']
# if 'mushroom' in requested_toppings:
#     print("Adding,mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")
# print("\nFinished making you pizza!")
# alien_color = ['green','yellow','red']
# if 'green' in alien_color:
#     print("You get 5 points!")
# if 'yellow' in alien_color:
#         print("You get 10 points!")
# if 'red' in alien_color:
#     print("You get 15 points!")
# age = 6
# if age < 2:
#     print("You are a baby.")
# elif age < 4:
#     print("You are a infant.")
# elif age < 13:
#     print("You are a child.")
# elif age < 20:
#     print("You are a teenager.")
# elif age <65:
#     print("You are a adult.")
# else:
#     print("You are an old man.")
# favorite_fruits = ['banana','apple','orange']
# if 'banana' in favorite_fruits:
#     print("You really like bananas!")
# if 'watermelon' in favorite_fruits:
#     print("You really like watermelon!")
# if 'apple' in favorite_fruits:
#     print("You really like apple!")
# if 'orange' in favorite_fruits:
#     print("You really like orange!")
# if 'pear' in favorite_fruits:
#     print("You really like pear!")
# requested_toppings =['mushrooms','green peppers','extra cheese']
# for requested_toppings in requested_toppings:
#     if requested_toppings == 'green peppers':
#         print("Sorry,we are out of green peppers right now.")
#     else:
#         print(f"Adding {requested_toppings}.")
# print("\nFinished making your pizza!")
# requested_toppings = ['green peppers']
# if requested_toppings:
#     for requested_toppings in requested_toppings:
#         print(f"Adding {requested_toppings}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")
# available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
# requested_toppings = ['mushrooms','french fries','extra cheese']
# for requested_toppings in requested_toppings:
#     if requested_toppings in available_toppings:
#         print(f"Adding {requested_toppings}.")
#     else:
#         print(f"Sorry,we don't have {requested_toppings}.")
# print("\nFinished making your pizza!")
# users = ['admin','alien','one','two','three']
# for users in users:
#     if users == 'admin':
#         print("Hello admin,would you like to see a status report?")
#     else:
#         print(f"Hello {users},thank for you logging in again.")
# users = []
# if not users:
#     print("We need to find some users！")
# current_users = ['one','two','three','four','five']
# new_users = ['four','five','six','seven','eight']
# for new_users in new_users:
#     if new_users in current_users:
#         print(f"{new_users.title()} has been used.")
#     else:
#         print(f"{new_users.title()} has't been used.")
# numbers = ['1','2','3','4','5','6','7','8','9','10']
# for numbers in numbers:
#     if '1' in numbers:
#         print('1st')
#     if '2' in numbers:
#         print('2nd')
#     if '3' in numbers:
#         print('3rd')
#     if '4' in numbers:
#         print('4th')
#     if '5' in numbers:
#         print('5th')
#     if '6' in numbers:
#         print('6th')
#     if '7' in numbers:
#         print('7th')
#     if '8' in numbers:
#         print('8th')
#     if '9' in numbers:
#         print('9th')
# alien_0 = {'color': 'green','points':5}
# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")
# alien_0 = {'color': 'green','points':5}
# print(alien_0)
# alien_0 ['x_position'] = 0
# alien_0 ['y_position'] = 25
# print(alien_0)
# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)
# alien_0 = {'color':'green'}
# print(f"The alien is {alien_0['color']}.")
# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}.")
# alien_0 = {'x_position':0,'y_position':25,'speed':'fast'}
# print(f"Original x_position:{alien_0['x_position']}")
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New x_position: {alien_0['x_position']}")
# alien_0 = {'color':'green','points':5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)
# favorite_language = {
#     'Jen':'python',
#     'sarah':'c',
#     'eward':'ruby',
#     'phil':'python',
#     }
# language = favorite_language['sarah'].title()
# print(f"Sarah's favourite language is {language}.")
# print(favorite_language['sarah'])
# alien_0 = {'color':'green','speed':'slow','points':5}
# point_value = alien_0.get('points','No point value assigned.')
# print(point_value)
# alien_0 = {'color':'green','speed':'slow'}
# point_value = alien_0.get('points','No point value assigned.')
# print(point_value)
# person = {'first_name':'张博恒',
#           'laxt_name':'张林枫',
#           'age':19,
#           'cith':'南通'
#           }
# print(person)
# favourite_numbers = {'a':1,
#                      'b':2,
#                      'c':3,
#                      'd':4,
#                      'e':5
#                      }
# print(f"A favourite number is {favourite_numbers['a']}")
# print(f"B favourite number is {favourite_numbers['b']}")
# print(f"C favourite number is {favourite_numbers['c']}")
# print(f"D favourite number is {favourite_numbers['d']}")
# print(f"E favourite number is {favourite_numbers['e']}")
# user_0 = {
#     'username':'efermi',
#     'first':'enrico',
#     'last':'fermi,'
#     }
# for k, v in user_0.items():
#     print(f"\nKey: {k}")
#     print(f"Value: {v}")
# favorite_language = {
#     'Jen':'python',
#     'sarah':'c',
#     'eward':'ruby',
#     'phil':'python',
#     }
# for name, language in favorite_language.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")
# for name in favorite_language.keys():
#     print(name.title())
# favorite_language = {
#     'Jen':'python',
#     'sarah':'c',
#     'eward':'ruby',
#     'phil':'python',
#     }
# friends = ['phil','sarah']
# for name in favorite_language.keys():
#     print(f"Hi {name.title()}")
#     if name in friends:
#         language = favorite_language[name].title()
#         print(f"\t{name.title()},I see you love {language}.")
# favorite_language = {
#     'Jen':'python',
#     'sarah':'c',
#     'eward':'ruby',
#     'phil':'python',
#     }
# if 'erin' not in favorite_language.keys():
#     print("Erin,please take out poll!")
# favorite_language = {
#     'Jen':'python',
#     'sarah':'c',
#     'eward':'ruby',
#     'phil':'python',
#     }
# for name in sorted(favorite_language.keys()):
#     print(f"{name.title()},thank you for taking the poll.")
# favorite_language = {
#     'Jen':'python',
#     'sarah':'c',
#     'eward':'ruby',
#     'phil':'python',
#     }
# print("THe following language have been mentioned.")
# for language in set(favorite_language.values()):
#     print(language.title())
# river_country = {
#     'nile':'egypt',
#     'yangzi':'chine',
#     'changjiang':'china',
#     }
# for river,country in river_country.items():
#     print(f"The {river.title()} runs through {country.title()}.")
# for river in river_country.keys():
#     print(river.title())
# for country in river_country.values():
#     print(country.title())
# favorite_language = {
#     'Jen':'python',
#     'sarah':'c',
#     'eward':'ruby',
#     'phil':'python',
#     }
# under_investigation = ['Jen','eward','a','b','c']
# for name,language in favorite_language.items():
#     if name in under_investigation:
#         print(f"{name.title()},thankyou for taking the roll!")
#     if name not in under_investigation:
#         print(f"{name.title()},please take the roll!")
# aliens = []
# for alien_number in range(30):
#     new_alien = {'color':'green',
#                  'points':'5',
#                  'speed':'slow'
#                  }
#     aliens.append(new_alien)
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15
# for alien in aliens[:10]:
#     print(alien)
# print("...")
# pizza = {
#     'crust':'thick',
#     'toppings':['mushroom','extra cheese'],
# }
# print(f"You ordered a {pizza['crust']}-crust pizza "
#       "with the following toppings:")
# for topping in pizza['toppings']:
#     print("\t" + topping)
# favorite_language = {
#     'Jen':['python','ruby'],
#     'sarah':['c'],
#     'eward':['ruby','go'],
#     'phil':['python','haskell'],
# }
# for name,language in favorite_language.items():
#     print(f"\n{name.title()}'s favourite languages are:")
#     for language in language:
#         print(f"\t{language.title()}")
# users = {
#     'aeinstein':{
#         'first':'albert',
#         'last':'einstein',
#         'location':'princetion',
#     },
#     'mcurie':{
#         'first':'marie',
#         'last':'curie',
#         'location':'paris',
#     }
# }
# for usersname,user_into in users.items():
#     print(f"\nUsername:{usersname}")
#     full_name = f"{user_into['first']} {user_into['last']}"
#     location = user_into['location']
#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")
# message = input("Tell me something, and I will repeat it back to you:")
# print(message)
# name = input("Please enter your name: ")
# print(f"\nHello, {name}")
# prompt = "If you tell us who you are, we can personalize the message you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}")
# height = input("How tall are you, in centimetre? ")
# height = int(height)
# if height >=150:
#     print("\nYou are tall enough yo ride!")
# else:
#     print("\nYou'll be able to ride when you're a little order.")
# number = input("Enter a number,and I'll tell you if it's even or odd:")
# number = int(number)
# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")
# print("What kind of car do you want to rent?")
# name = input()
# print(f"Let me see if I can find you a {name}.")
# print("How many customers are eating?")
# numbers = input()
# numbers = int(numbers)
# if numbers >=8:
#     print("Sorry,we have no place.")
# else:
#     print("We have some tables left.")
# numbers = input("Enter a number,and I'll tell you if it's multiple of 10.")
# numbers = int(numbers)
# if numbers %10 == 0:
#     print(f"The number {numbers} is multiple of 10.")
# else:
#     print(f"The number {numbers} is not multiple of 10.")
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
# prompt = "\nTell me something, and I will repeat it back to you:" \
#          "\nEnter 'quit' too end the program."
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
# prompt = "\nTell me something, and I will repeat it back to you:" \
#          "\nEnter 'quit' too end the program."
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#         print("Game over！")
#     else:
#         print(message)
# prompt = "\nPlease enter the name of a city you have visisted:" \
#          "\n(Enter 'quit' when you are finished.) "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go {city.title()}")
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)
# x = 1
# while x <= 4999:
#     x += 1
#     print(x)
# prompt = "请输入pizza配料:"
# while True:
#     answer = input(prompt)
#     if answer == 'quit':
#         break
#     else:
#         print(f"我会在pizza中加入{answer}")
# print("告诉我你的年龄：")
# while True:
#     age = ""
#     age = input(age)
#     age = int(age)
#     if age <= 3:
#         print("You are free!")
#     elif age <= 12:
#         print("You need give me 10 dollars!")
#     elif age <=200:
#         print("You need to give me 15 dollars!")
#     else:
#         break
# unconfirmed_unsers = ['alice','brain','candace']
# confirmed_unsers = []
# while unconfirmed_unsers:
#     current_user = unconfirmed_unsers.pop()
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_unsers.append(current_user)
# print("\nThe following users have been confirmed:")
# for confirmed_unsers in confirmed_unsers:
#     print(confirmed_unsers.title())
# pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)
# responses = {}
# polling_active = True
# while polling_active:
#     name = input("\nWhat's your name?")
#     response = input("Which mountain would you like to climb someday?")
#     responses[name] = response
#     repeat = input("Would you like to let another person responed? (yes or no) ")
#     if repeat == 'no':
#         polling_active = False
# print("\n--- Poll Results ---")
# for name,response in responses.items():
#     print(f"{name.title()} would like to climb {response}.")
# sandwich_orders = ['pizza1','pizza2','pizza3','pastraim','pastraim','pastraim']
# finished_sandwiches = []
# print("There have no pastraim.")
# while 'pastraim' in sandwich_orders:
#     sandwich_orders.remove('pastraim')
# while sandwich_orders:
#     current_orders = sandwich_orders.pop()
#     print(f'I made your {current_orders.title()}')
#     finished_sandwiches.append(current_orders)
# finished_sandwiches.reverse()
# print(f'\n---All Sandwiches are finished--- ')
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich.title())
# def greet_user(username):
#     """显示简单的问候语。"""
#     print(f"Hello,{username.title()}")
# greet_user('jesse')
# greet_user('mike')
# greet_user('sarah')
# def display_message(messagename):
#     print(f"学习了如何{messagename}。")
# display_message('定义函数')
# def favourite_book(title):
#     print(f"One of our favourite books is {title} in Wonderland.")
# favourite_book('Alice')
# def describe_pet(animal_type,pet_name):
#     """显示宠物信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}")
# describe_pet('hamster','harry')
# describe_pet('dog','willie')
# def make_shirt(size,writing):
#     print(f"\nThe size of the T-shirt is {size} and the example of the T-shirt is {writing}.")
# make_shirt('1','a')
# make_shirt('2','b')
# def describle_city(c,country):
#     print(f"{c.title()} is in {country.title()}.")
# describle_city('beijing','china')
# describle_city('paris','france')
# describle_city('new work','england')
# def get_formatted_name(first_name,last_name,middle_name=''):
#     """返回整洁的姓名。"""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('jhon','hendrix','lee')
# print(musician)
# musician = get_formatted_name('liu','zhu','yi')
# print(musician)
# musician = get_formatted_name('sun','yan')
# print(musician)
# def build_person(first_name,last_name,age=None):
#     """返回一个字典，其中包含有关一个人的信息。"""
#     person = {'first': first_name,'last':last_name}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('jimi','hendrix',age=27)
# print(musician)
# def get_formatted_name(first_name,last_name):
#     """返回整洁的姓名。"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name:")
#     if f_name == '':
#         break
#     l_name = input("Last name:")
#     if l_name == '':
#         break
#     formatted_name = get_formatted_name(f_name.title(),l_name.title())
#     print(f"\nHello,{formatted_name}!"
# def city_counrty(city,country):
#     full_name = f"{city},{country}"
#     return full_name.title()
# while True:
#     print("\nPlease tell me the city")
#     ci = input("city:")
#     if ci == '':
#         break
#     co = input("country:")
#     if co == '':
#         break
#     whole_city_country = city_counrty(ci,co)
#     print(f"{ci.title()},{co.title()}")
# def make_album(singer,name):
#     full_name = f"{singer},{name}"
#     return full_name.title()
# while True:
#     print("\nPlease tell me the singer and their album")
#     s = input("singer:")
#     if s == '':
#         break
#     a = input("album:")
#     if a == '':
#         break
#     print(f"{a.title()} is {s.title()}'s album.")
# def greet_users(names):
#     """向列表中的每位用户发出简单的问候。"""
#     for name in names:
#         msg = f"Hello,{name.title()}!"
#         print(msg)
#
#
# usersname = ['hannah','ty','margot']
# greet_users(usersname)
# def print_modles(unprinted_designs,completed_modles):
#     """
#     模拟打印每个设计，直到没有未打印的设计为止。
#     打印每个设计后，都将其移到列表completed_modles中。
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model:{current_design}")
#         completed_modles.append(current_design)
# def show_completed_modles(completede_modles):
#     """显示打印好的模型。"""
#     print("\nThe following modles have been printed:")
#     for completede_modle in completede_modles:
#         print(completede_modle)
# unprinted_designs = ['phone case','robot pendant','dodecahedron']
# completed_modles = []
# print_modles(unprinted_designs[:],completed_modles)
# show_completed_modles(completed_modles)
# def show_messages(messages):
#     """打印列表中的所有消息。"""
#     print('显示所有消息：')
#     for message in messages:
#         print(message)
#
#
# def send_messages(messages, sent_messages):
#     """打印每条消息，再将其移到列表sent_messages中。"""
#     print('\n发送所有消息：')
#     while messages:
#         current_message = messages.pop()
#         print(current_message)
#         sent_messages.append(current_message)
#
#
# Anywhere = ['张楚岚', '冯宝宝', '王也']
# show_messages(Anywhere)
#
# sent_message = []
# send_messages(Anywhere, sent_message)
#
# print('\n最终消息列表：')
# print(Anywhere)
# print(sent_message)
# def make_pizza(*toppings):
#     """打印顾客点的所有配料。"""
#     print(toppings)
# make_pizza('pepperoin')
# make_pizza('mushrooms','green peppers','extra cheese')
# def make_pizza(*toppings):
#     """概述要制作的披萨。"""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
# make_pizza('pepperoin')
# make_pizza('mushrooms','green peppers','extra cheese')
# def make_pizza(size,*toppings):
#     """概述要制作的披萨。"""
#     print(f"\nMaking a {size}-inch pizza with the following toppongs:")
#     for topping in toppings:
#         print(f"- {topping}")
# make_pizza(16,'pepperoin')
# make_pizza(12,'mushrooms','green peppers','extra cheese')
# def build_profile(first,last,**user_into):
#     """创建一个字典，其中包含我们知道的有关用户的一切。"""
#     user_into['firse_name'] = first
#     user_into['last_name'] = last
#     return user_into
# user_profile = build_profile('albert','einstein',
#                              location='princetion',
#                              field='physics')
# print(user_profile)
# class Dog:
#     """一次模拟小狗的简单尝试。"""
#
#     def __init__(self, name, age):
#         """初始化属性name，age。"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """模拟小狗受到命令时蹲下。"""
#         print(f"{self.name} is now sitting.")
#
#     def roll_over(self):
#         """模拟小狗收到命令时打滚。"""
#         print(f"{self.name} rolled over!")
#
# my_dog = Dog('Willie',6)
# your_dog = Dog('Lucy',3)
#
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()
#
# print(f"\nYour dog's name is {your_dog.name}")
# print(f"My dog is {my_dog.age} years old.")
# your_dog.sit()

# class Restaurant:
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(f"{self.restaurant_name} is on business.")
#
#     def open_restaurant(self):
#         print(f"{self.cuisine_type} you can choose.")
#
# my_restaurant = Restaurant('Noddles','noddle')
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()
# class Car:
#     """一次模拟汽车的简单尝试。"""
#
#     def __init__(self,make,modle,year):
#         """初始化描述汽车的信息。"""
#         self.make = make
#         self.modle = modle
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descrptive_name(self):
#         """返回整洁的描述性信息。"""
#         long_name = f"{self.year} {self.make} {self.modle}"
#         return long_name.title()
#
#     def read_odometer(self):
#         """打印一条指出汽车里程的消息。"""
#         print(f"This car has {self.odometer_reading} miles on it.")
#
#     def update_odometer(self,mileage):
#         """将里程表读数设置为指定的值。
#         禁止将里程碑读数往回调。"""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self,miles):
#         """将里程表读数增加指定的量。"""
#         self.odometer_reading += miles
#
# my_used_car = Car('subaru','outback','2015')
# print(my_used_car.get_descrptive_name())
#
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
# class Car:
#     """一次模拟汽车简单的尝试。"""
#
#     def __init__(self,make,modle,year):
#         self.make = make
#         self.modle = modle
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descrptive_name(self):
#         """返回整洁的描述性信息。"""
#         long_name = f"{self.year} {self.make} {self.modle}"
#         return long_name.title()
#
#     def read_odometer(self):
#         """打印一条指出汽车里程的消息。"""
#         print(f"This car has {self.odometer_reading} miles on it.")
#
#     def update_odometer(self,mileage):
#         """将里程表读数设置为指定的值。
#         禁止将里程碑读数往回调。"""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self,miles):
#         """将里程表读数增加指定的量。"""
#         self.odometer_reading += miles
#
# class ElectricCar(Car):
#     """电动车的独特之处。"""
#
#     def __init__(self,make,modle,year):
#         """初始化父类的属性。
#         再初始化电动汽车特有的属性。
#         """
#         super().__init__(make,modle,year)
#         self.battery_size = 75
#
#     def describe_battery(self):
#         """打印一条描述电瓶容量的消息。"""
#         print(f"This car has a {self.battery_size}-KWh battery.")
#
#     def fill_gas_tank(self):
#         """电动汽车没有油箱。"""
#         print("This car doesn't need a gas tank!")
#
# my_tesla = ElectricCar('tesla','modle s',2019)
# print(my_tesla.get_descrptive_name())
# my_tesla.describe_battery()
# my_tesla.fill_gas_tank()


# class Car:
#     """一次模拟汽车简单的尝试。"""
#
#     def __init__(self,make,modle,year):
#         self.make = make
#         self.modle = modle
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descrptive_name(self):
#         """返回整洁的描述性信息。"""
#         long_name = f"{self.year} {self.make} {self.modle}"
#         return long_name.title()
#
#     def read_odometer(self):
#         """打印一条指出汽车里程的消息。"""
#         print(f"This car has {self.odometer_reading} miles on it.")
#
#     def update_odometer(self,mileage):
#         """将里程表读数设置为指定的值。
#         禁止将里程碑读数往回调。"""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self,miles):
#         """将里程表读数增加指定的量。"""
#         self.odometer_reading += miles
#
# class Battery:
#     """一次模拟电动汽车电瓶的简单尝试。"""
#     def __init__(self,battery_size=100):
#         """初始化电瓶属性。"""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """打印一条描述电瓶容量的消息。"""
#         print(f"This car has a {self.battery_size}-KWh battery.")
#
#     def get_range(self):
#         """打印一条消息，指出电瓶的续航里程。"""
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315
#
#         print(f"This car can go about {range} miles on a full charge.")
#
# class ElectricCar(Car):
#     """电动车的独特之处。"""
#
#     def __init__(self,make,modle,year):
#         """初始化父类的属性。
#         再初始化电动汽车特有的属性。
#         """
#         super().__init__(make,modle,year)
#         self.battery= Battery()
#
# my_tesla = ElectricCar('tesla','modle s','2019')
# print(my_tesla.get_descrptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

# from random import randint
# print(randint(1,49))
# from  random import choice
# players = ['charles','martian','michael','florence','eli']
# first_up = choice(players)
# print(first_up)

# message = "I really like dogs."
# print(message.replace('dog','cat'))

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero.")

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit")
#
# while True:
#     first_number = input("\nFirst number:")
#     if first_number == 'q':
#         break
#     second_number = input("Second number:")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)

# title = "Alice in Wonderland"
# print(title.split())

# import json
# numbers = [2,3,5,7,11,13]
# filename = 'number.json.txt'
# with open(filename,'w')as f:
#     json.dump(numbers,f)

# import json
# filename = 'number.json.txt'
# with open(filename)as f:
#     numbers = json.load(f)
# print(numbers)

# import json
# username = input("What is your name?")
# filename = 'number.json.txt'
# with open(filename,'w')as f:
#     json.dump(username,f)
#     print(f"We'll remember you when you come back, {username}!")
#
# import json
# filename = 'number.json.txt'
# with open(filename) as f:
#     username = json.load(f)
#     print(f"Welcome back, {username}!")

# def get_formatted_name(first,last):
#     """生成整洁的姓名。"""
#     full_name = f"{first} {last}"
#     return full_name
#
# print("Enter 'q' at any time to quit.")
# while True:
#     first = input("\nPlease give me a first name: ")
#     if first == 'q':
#         break
#     last = input("\nPlease give me a last name: ")
#     if last == 'q':
#         break
#
#     formatted_name = get_formatted_name(first,last)
#     print(f"\tNeaatly formatted name {formatted_name}.")

# class AnonymousSurvey:
#     """收集匿名调查问卷答案。"""
#
#     def __init__(self,question):
#         """存储一个问题，并为存储答案最准备。"""
#         self.question = question
#         self.responses = []
#
#     def show_question(self):
#         """显示调查问卷。"""
#         print(self.question)
#
#     def store_response(self,new_response):
#         """存储单份调查答案。"""
#         self.responses.append(new_response)
#
#     def show_results(self):
#         """显示收集到的所有答案。"""
#         print("Survey results: ")
#         for response in self.responses:
#             print(f"- {response}")
#
#
# #from survey import AnonymousSurvey
# #定义一个问题，并创建一个调查。
# question = "What language did you first learn to speak?"
# my_survey = AnonymousSurvey(question)
#
# #显示问题并储存答案。
# my_survey.show_question()
# print("Enter 'q' at any time to quit.\n")
# while True:
#     response = input("Language: ")
#     if response == 'q':
#         break
#     my_survey.store_response(response)
#
# #显示调查结果。
# print("\nThank you to everyone who participated in the survey!")
# my_survey.show_questions
