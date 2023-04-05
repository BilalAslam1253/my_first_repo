"""def gensquares (n):
    for i in  range(n):
      yield i**2


for square in gensquares(10):
    print(square)
    

import random


def rand_num(low,high,n):

    for x in range(n):
        yield random.randint(low,high)

for i in rand_num(1,10,20):
    print(i)


s = 'hello'

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))



from collections import Counter
s = "what the hell is a counter module and all of its stupid parameters? how many times do each word show up in this sentence? sentence is a sentence! Not a word! word is a word too, not a sentence"
words = s.split()
#print(words)
c = Counter(words)
#print(c)
#print(c.most_common(5))
#print(c.values())
print(c.items())
#print(list(c))
#print(Counter(dict(c.items())))
c+=Counter()
print(c.most_common()[:-100-1:-1])
#print(c)

import time

t1 = time.time()

print(t1)
for i in range(100):
    print('A')
    a = 4*5
    b = 5*35
    pdb.set_trace()
t2 = time.time()
print(t2)
import timeit

print(timeit.timeit('"-".join(map(str,range(100)))',number = 10000))
print("-".join([str(n) for n in range(100)]))

import re

pattern = 'hello'

text = "Hello, my name is hello ? And i would like @tos say hello to all them peep is in all."


gp_pattern = re.compile(r'(\w{4}) (\w{3})')
print(gp_pattern)


for match in re.finditer(gp_pattern, text):
    #for i in range(1,3):
    print(match)

a = re.finditer(gp_pattern,text)
print(a)

for i in a:
    print(i.group())

#b = re.split('@',text)


#print(text.split('@'))


#rint(a.group())

import random
import math
list_check = [1,2,3,4,5,6,7,8,9,9,10,1,2,4,6,7,11,44,23,67,46,86,99]
print(random.sample(population=list_check, k=13))
print(random.choices(population=list_check, k=13))

print(math.pi)
print(math.log(100,2))
print(math.degrees(math.pi/2))

random.seed(101)

print(random.randint(0,100))
print(random.randint(0,100))
"""
from ast import keyword
import os
import shutil
#f = open("test_file.txt",'w+')
#f.write("This is a test text file!")
#f.close()
#print(os.getcwd())
#print(os.listdir('C:\\Users\\New\\Documents'))
#shutil.move('test_file.txt','C:\\Users\\New\\Documents\\Final Capstone Projects Python Specialization\\Zero to hundred course projects')
#os.unlink('C:\\Users\\New\\Documents\\Final Capstone Projects Python Specialization\\Zero to hundred course projects\\test_file.txt')
"""
for folders, sub_folders, files in os.walk('C:\\Users\\New\\Documents\\Final Capstone Projects Python Specialization'):
    
    print(f'Currently, Going through the folder "{folders}"\n')
    print("The subfolders are :")
    for subfolder in sub_folders:
       
        print(f'\t SubFolder : {subfolder}')
        print("The files are :")
    for f in files:
        print(f'\t File : {f}')
for i in os.walk('C:\\Users\\New\\Documents\\Final Capstone Projects Python Specialization'):
    print(i)
    """
# a=[]
# round(2.356789, 2)
# #print(int(False))
# #print(len(a))

# party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
# #print(party_attendees.index('Mona'))

# def has_lucky_number(nums):
#     """Return whether the given list of numbers is lucky. A lucky list contains
#     at least one number divisible by 7.
#     """
#     for num in nums:
#         if num % 7 == 0:
#             return True

#     return False

# has_lucky_number ([1,2,3,5,6,8])

def word_search(doc_list, keyword):
    indexes = []
    for i, doc in enumerate(doc_list):
        spilt_item = doc.split()
        final = [item.lower().strip(".,?") for item in spilt_item]
        # print(final)
        if keyword.lower() in final:
            indexes.append(i)
    return indexes
# print(word_search(doc_list,keywords))



# def word_search(doc_list, keyword):
#     # list to hold the indices of matching documents
#     indices = [] 
#     # Iterate through the indices (i) and elements (doc) of documents
#     for i, doc in enumerate(doc_list):
#         # Split the string doc into a list of words (according to whitespace)
#         tokens = doc.split()
#         print(tokens)
#         # Make a transformed list where we 'normalize' each word to facilitate matching.
#         # Periods and commas are removed from the end of each word, and it's set to all lowercase.
#         normalized = [token.rstrip('.,').lower() for token in tokens]
#         print(normalized)
#         # Is there a match? If so, update the list of matching indices.
#         if keyword.lower() in normalized:
#             indices.append(i)
#     return indices

# doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
# print(word_search(doc_list,"casino"))
# print("casino" in ["casinoville"])

def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    value = []
    findings = {}
    for i, key in enumerate(keywords):
        findings[key] = word_search(doc_list,key)
        
    return findings

doc_list = ['The Learn Python Challenge Casino', 'They bought a car', 'Casinoville?']
keywords = ['casino', 'ear']
print(multi_word_search(doc_list, keywords))
