# len(x) => finds length of something
from calendar import different_locale
from ctypes import Union


len("hello world")
len([1,2,3,4,5,6])

# LISTS => mutable ordered sequence => big O notation (takes more work to add search and delete is all it means)
alpha = ['a', 'b', 'c'] #literal syntax
#can also do this:
list('hello')
list(range(10,20,2))
#in operator => check for membership also works with strings
vegan_nos = ['eggs', 'meat', 'dairy', 'figs']
pie_ingredients = ['flour', 'apples', 'sugar', 'eggs']
for food in pie_ingredients:
    if food in vegan_nos:
        print(f"{food} is not vegan")
    else: 
        print(f'i love {food}')
special_chars = '!@#$%&*'
'.' in special_chars #False

vegan_nos[3] #gives element at index 3
vegan_nos[7] #gives error
vegan_nos[-1] #can go backwards => first index from the end
vegan_nos[2] = 'dairy' #update element at a given index
#cannot set a NEW index in this way
#remember again => lists are reference types; copies will point to the same ref types
#slicing
nums = list(range(0,100,1))
nums[50:60:1] # prints 50 - 59 by 1
#start is inclusive, end is non-inclusive
nums[90:] #everything from 90 onwards to end of list
nums[90::2] #from 90 onwards by 2's => leaves a default stop value when not specified BUT we need that colon
nums[::5]
nums[::-9] #reverses entire list with a step of 9
#NONE OF THIS MUTATES THE ORIGINAL
nums[20:10:-1]

# SPLICING => same syntax as slice, but this allows us to update or remove elements
colors = ['red', 'orange', 'yellow']
colors[0:1] = ['dark red', 'pink'] # takes whatever was found between index of 0 and 1 and updates it to the list we have set
#ENTIRE LIST UPDATES
colors [3:] = ['yellow', 'green', 'blue', 'purple']
colors[5:] = [] #removes last two

# built in list methods
# l.append(x) => can only append one item at a time
# l.copy() => copy = list.copy()
# l.count(x) => how many times a given element appears in a list
# l.extend(l2) => adds l2 to list one, iterates whatver we pass in 
bratz = ['yasmine', 'sasha', 'cloe', 'jade']
more_bratz = ['dylan', 'kobe', 'ethan']
bratz.extend(more_bratz) #both lists now joined, OG list is updated
# l.index(x)
'dylan' in bratz
bratz.index('dylan') #tells WHERE 'dylan' is found in the list; will only return first matching index, if not in list raises an error
# l.insert(i,x)
bratz.insert(0, 'roxxi')
bratz.insert(7, ['cameron', 'phoebe', 'braden']) #will LITERALLY insert the list
# l.pop(i) => all purpose remove if no index specified
bratz.pop(7)
# l.reverse() => reverses list in place
# l.sort() => sorts alphabetically or numerically by default => can also do:
bratz.sort(reverse=True) #backwards alphabetical order
#no heterogenous sort
#doesn't return automatically after we tweak

# STRINGS
price = 3.50
qty = 7
print(f"your total is {price * qty}$")
str(5.6)
nums = [3,4,5]
str(nums)
price = '56.99$'
'$' in price
#can use slices NOT splices (b/c strings are immutable)
'!' * 10

#string methods
# s.count(t) => case sensitive
# s.endswith(t) => returns True or False
# s.find() => find a character in string and returns index of first instance
# s.isdigit() => is string made up entirely of digits?
# s.join(seq) => makes new string for us but they separated by |
#   => we usually join lists into a string
"|".join(bratz)
".".join('LMFAO')
# s.lower()
# s.upper()
# s.capitalize() => will cap first letter
# s.replace(t, count) => replace some string or substring with wtf ever we pass in
things = 'apples-tomatoes-pickles'
things.replace('-','=',1)
text = 'i hate you so much'
text.replace(' ', '...')
# s.split(sep) => takes string and split into list based on some separating charcater
animals = "goats,chickens,ducks,pigs,alpacas"
animals.split(',')
# s.splitlines() => turns each line into its own element in a list
"""
hello
i
love
you
""".splitlines()
# s.startwith(t) => returns True or False
person = 'Mr. Jones'
person.startswith("Mr. ")
# s.strip() => removes leading or trailing spaces

# DICTIONARIES => KEY-VALUE PAIRS MAPPED TOGETHER
person = {'first': 'Henry', 'last': 'Hocket'}
# keys and values can be ANY immutable type
dog = {'name': 'Bowser', 'age': '4', 'breed': 'Staffordshire Terrier'}
stuff = {True: 34, 100: 'AWESOME'}
#membership
'breed' in dog
'Bowser' in dog #ONLY works for keys so this will throw an error
#retrieval
dog['breed'] #staffordshire terrier
# can update as well => dog['age'] = 3
dog.get('weight', '70lbs') # => use .get() to FIND keys and if none is found we return an error OR you can assign a value if it is known that it's not in dictionary
#can pass in a default value:
dog('sex', 'unknown') # default
dog['sex'] = 'M' # updated to display "male" sex and default goes unused

dict() #makes new dictionary => dict([[True,0],[False,1]]) => {True: 0, False: 1}

#iterating over dictionaries
person = {
    'name': 'Rane',
    'sex': 'F',
    'age': 22,
    'birth_chart': {
        'sun': 'gemini',
        'moon': 'cancer',
        'rising': 'saggitarius'
    },
    'is_single': True
}
#over keys:
keys = person.keys() #ITS NOT A LIST ALL WE CAN DO IS ITERATE
for key in person.keys():
    print(key)
for value in person.values():
    print(value)
person.items() # gives us a dict-items collection in pairs
for pair in person.items():
    print(pair)
#unpack pairs from items
for (k,v) in person.items():
    print(k, '=>' ,v)
#dictionaries ordered by insertion
#dictionary methods
# d.copy() 
# d.pop()
# d.popitem() => removes and returns SOME random ass pair... weird, why?
# d.fromkeys() => makes ya brand new dict, doesn't impact or operate on the dictionary that it was called on
{}.fromkeys('MTWTF', True)
#d.clear() => removes all items from dict

# SETS => unordered unique collection of items IMMUTABLE TYPES ONLY DOESNT HAVE TO BE ALL ONE DATA TYPE EITHER
coding_languages = {'ruby', 'python', 'javascript'}
type(coding_languages) # set => notice there's no k-v pairs
languages = ['spanish', 'mandarin', 'english', 'arabic', 'english', 'english']
set(languages) #gets rid of extras n creates a set; can also do this with strings
# SET METHODS
'mandarin' in languages
# addition to sets
languages.add('french')
# .pop() => takes arbitrary element from a set
# .remove(s) => explicitly remove a value
len(languages)
languages.remove('french')
# .copy()
# .clear()
# SET OPERATIONS => have to deal with taking two or more sets and calculating:
moods = {'happy', 'sad', 'grumpy', 'shy', 'sleepy', 'silly'}
dwarfs = {'happy', 'grumpy', 'doc', 'sneezy', 'sleepy', 'dopey', 'bashful'}
# union => just joins em together w/ ofc dupes removed
moods | dwarfs
moods | dwarfs | {'sneaky', 'relaxed'}
# intersection => what do they have in common
moods & dwarfs
# difference (order matters) => what they DONT have in common returns set 1 - the objects that were in common from set 2
moods - dwarfs
dwarfs - moods
# symmetric difference => returns all elements that are in EXACTLY ONE of the sets (is missing everything that was in the intersection basically)
moods ^ dwarfs
# there is a difference between the shortcuts (only works between two sets) and the named methods (takes an iterable and changes it into a set and THEN compares set to created set)
# SETS ARE ITERABLES!!!!! and they are fast
for mood in moods:
    print(moods)
for written in moods | dwarfs:
    print(written)

# TUPLES => ordered collections of values and they are immutable => cant put whatever ya want in there
t1 = (1,2,3)
colors = ('red', 'yellow', 'green')
colors[1] # can access values
len(colors) # check length
# in order to make a one item tuple we need a trailing comma
t2 = (3,)
# don't have to be unique values
#can be used as dict keys or put into sets bc of immutability: (e.g)
board = {
    (0,0): 'X',
    (0,1): None,
    (0,2): 'O',
    (1,0): 'O',
    (1,1): 'X',
    (1,2): 'X',
    (2,0): None,
    (2,1): None,
    (2,2): 'O'
}
#methods: .count(t) => how many times value occurs and .index(t) => first instance of where item occurs in tuple

# LIST COMPREHENSIONS => create a list based off of some other iterable
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
evens = [num for num in nums if num % 2 == 0]
#create new list and filled with content based on og
# num => variable name
# for num in nums => loop
# carry out some condition
dubs = [num * 2 for num in nums]
# we want to multiply every num in nums by 2
excited = ['heyo!' for inputs in nums] #loops over every element and essentially replaces it with string
[n ** 2 for n in [2,4,6,8]] #squares each element in line
[char.upper() + '.' for char in 'LMFAO']
[num/2 for num in range(10,20)] #takes nums from range and adds into a list
#nested comprehensions
[[0 for y in range(3)] for x in range(3)] #gives us a 3x3 nested "gameboard" filled with 0's
def gen_board(size, initial_val = None):
    return [[initial_val for x in range(size)] for y in range(size)]
gym_people = [
    {'name': 'araya', 'sex': 'F'},
    {'name': 'jack', 'sex': 'M'},
    {'name': 'jake', 'sex': 'M'},
    {'name': 'jewel', 'sex': 'F'},
    {'name': 'tavias', 'sex': 'M'},
    {'name': 'kim', 'sex': 'F'},
]
gym_bros = [gym_people['name'] for bro in gym_people if gym_people['sex'] == 'M'] #for every name in gympeople list names ONLY IF they are the bros
scores = [55,89,99,87,60,70,74,76,90,82]
grades = ['Pass' if score >= 70 else 'Fail' for score in scores]
#syntax breakdown => [do_this IF something ELSE do_this for THING in THINGS]
#LAST EXAMPLE OMFG
def get_number(ltr):
    lookup = {
        'A':1,
        'B':2,
        'C':3,
        'D':4,
        'E':5,
        'F':6,
        'G':7,
        'H':8,
        'I':9,
        'J':10,
        'K':11,
        'L':12,
        'M':13,
        'N':14,
        'O':15,
        'P':16,
        'Q':17,
        'R':18,
        'S':19,
        'T':20,
        'U':21,
        'V':22,
        'W':23,
        'X':24,
        'Y':25,
        'Z':26
    }
    return lookup.get(ltr.upper(), '') #param 1 => what want to retrieve, 2: what we pass back if it cannot be retrieved
msg = [get_number(char) for char in 'ILY']
def get_code(phrase):
    return " ".join([get_number(char) for char in phrase])

# DICTIONARY AND SET COMPREHENSIONS
{day:0 for day in 'mtwrfsu'} #character used as key for dictionary with a preset value of 0
{num: num * num for num in range(1,10) if num % 2 == 0} #evens and their squares
#given 1-10, use those nums as key with a value of their square IF that number is even
{char for char in 'abracadabra' if char not in 'aeiou'} #contains every value from string that isn't a vowel => we made a set woo