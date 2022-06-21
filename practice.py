#product
def product(a,b):
    """return product of a and b"""
    return a * b

#weekday name
def weekday_name(DOTW):
    """user enters #1-7 and system returns corresponding DOTW (day of the week"""
    if DOTW == 1:
        return 'Monday'
    elif DOTW == 2:
        return 'Tuesday'
    elif DOTW == 3:
        return 'Wednesday'
    elif DOTW == 1:
        return 'Thursday'
    elif DOTW == 1:
        return 'Friday'
    elif DOTW == 1:
        return 'Saturday'
    elif DOTW == 1:
        return 'Sunday'
    else:
        return None

#last element
def last_element(lst):
    """return last item in list or None if list is empty"""
    if lst:
        return lst[-1]
    else:
        return None

#number compare
def number_compare(a,b):
    if a < b:
        return f"{a} is less than {b}"
    elif a > b:
        return f"{a} is greater than {b}"
    else:
        return "Numbers are equal"

#reverse string
def reverse_string(str):
    return str[::-1]

#single letter count
def single_letter_count(str, ltr):
    return str.lower().count(ltr.lower())

#multi letter count
def mult_letter_count(str):
    count = {}
    for ltr in str:
        count[ltr] = count.get(ltr, 0) + 1
    return count

#list manipulation
def list_manip(lst, command, location, value = None):
    if command == "add":
        if location == "beginning":
            lst.insert(0, value)
            return lst
        elif location == "end":
            lst.append(value)
            return lst
    elif command == "remove":
        if location == "beginning":
            return lst.pop(0)
        elif location == "end":
            return lst.pop()

def is_palindrome(str):
    forward = str.lower().replace(' ', '')
    if forward == forward[::-1]:
        return True
    else:
        return False

def frequency(lst, lookup):
    return lst.count(lookup)

def flip_case(str, swap):
    swap = swap.lower()
    output = ""
    for ltr in str:
        if ltr.lower() == swap:
            ltr = ltr.swapcase()
        output += ltr
    return output

def multiply_evens(nums):
    product = 1
    for num in nums:
        if num % 2 == 0:
            product = product * num
    return product

def capitalize(str):
    str.capitalize()

def compact(lst):
    return [inp for inp in lst if inp]

def intersection(one, two):
    return list(set(one) & set(two))

def partition(lst, func):
    true = []
    false = []
    for val in lst:
        if func(val):
            true.append(val)
        else: 
            false.append(val)
    return [true, false]

def mode(nums):
    from statistics import mode
    return mode(nums)

def calc(operation, a, b, make_int = False, message = "Results: "):
    if operation == 'add':
        results = a + b
    elif operation == 'subtract':
        results = a - b
    elif operation == 'multiply':
        results = a * b
    elif operation == 'divide':
        results = a / b
    else:
        return None
    if make_int:
        results = int(results)
    return f"{message}{results}"

def friend_date(a,b):
    """Given two friends, do they have sny hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    return bool(set(a[2] & set(b[2])))

def triple_and_filter(nums):
    return [num * 3 for num in nums if num % 4 == 0]

def extract_full(people):
    return [f"{person['first']} {person['last']}" for person in people]

def sum_floats(nums):
    return sum([num for num in nums if isinstance(num, float)])

def list_check(lst):
    for item in lst:
        if not isinstance(item, list):
            return False
    return True

def rm_every_other(lst):
    return lst[::2]

def sum_pairs(nums, goal):
    listed = set()
    for i in nums:
        diff = goal - i
        if diff in listed:
            return (diff, i)
        listed.add(i)
    return ()

def vowel_count(str):
    str = str.lower()
    count = {}

    for ltr in str:
        if ltr in 'aeiou':
            count[ltr] = count.get(ltr, 0) + 1
    return count

def titleize(str):
    return str.title()

def find_factors(num):
    factors = [n for n in range (1,num // 2 + 1) if num % n == 0]
    factors.append(num)
    return factors

def includes(collection, sought, start=None):
    if isinstance(collection, dict):
        return sought in collection.values()
    if start is None or isinstance(collection, set):
        return sought in collection
    return sought in collection[start:]

def repeat(str, num):
    if not isinstance(num, int) or num < 0:
        return None
    return str * num

def truncate(str, n):
    if n < 3:
        return "Truncation must be at least 3 characters"
    if n > len(str) + 2:
        return str
    return str[:n - 3] + '...'

def two_list_dict(k,v):
    from itertools import zip_longest
    return dict(zip_longest(k,v))

def sum_range(nums, start=0, end=None):
    if end is None:
        end = len(nums)
    return sum(nums[start:end + 1])

def freq_counter(coll):
    counts = {}
    for x in coll:
        counts[x] = counts.get(x,0) + 1
    return counts

def same_freq(num1, num2):
    return freq_counter(str(num1)) == freq_counter(str(num2))

def two_oldest(ages):
    some_ages = set(ages)
    oldest = sorted(some_ages)[-2:]
    return tuple(oldest)

def find_dupe(nums):
    yup = set()
    for num in nums:
        if num in yup:
            return num
        yup.add(num)

def sum_diags(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
        total += matrix[i][-1 - i]
    return total

def min_max_key(d):
    keys = d.keys()
    return (min(keys), max(keys))

def find_greater_nums(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                count += 1
    return count