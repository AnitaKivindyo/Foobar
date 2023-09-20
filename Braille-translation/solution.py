'''
A function that takes a string parameter, and returns a sting of '1's and '0's representing the bumps and no bumps in the input string. 
The function should be able to:
 1. encode the 26 lower case letters.
 2. encode capital letters - by adding the capitization mark before the charcter.
 3. USe a blank character (000000) for spaces.

 Note: All signs are less than fifty characters long AND use only letters and spaces
'''

space = 000000

caps_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

braille_key = [
    '100000',  # a
    '110000',  # b
    '100100',  # c
    '100110',  # d
    '100010',  # e
    '110100',  # f
    '110110',  # g
    '110010',  # h
    '010100',  # i
    '010110',  # j
    '101000',  # k
    '111000',  # l
    '101100',  # m
    '101110',  # n
    '101010',  # o
    '111100',  # p
    '111110',  # q
    '111010',  # r
    '011100',  # s
    '011110',  # t
    '101001',  # u
    '111001',  # v
    '010111',  # w
    '101101',  # x
    '101111',  # y
    '101011'   # z
]


# mapping lower case characters 
braille_mapping = {}

for i in range(len(alphabet)):
    braille_mapping[alphabet[i]] = braille_key[i]

print (braille_mapping)




# encode capital letters

#if text.isupper():
#    braille_mapping['a'] = f".{braille_mapping['a']}"

#print(braille_mapping['a'])

# function
def braille_translate(text):
    # split the text into words
    input_string = text.split(" ")
    result = []
    for input in input_string:
        if result:
            result.append(" ")
        result.append(input)

    return result

  
text =input('Enter an input')
test = braille_translate(text)
print (test)