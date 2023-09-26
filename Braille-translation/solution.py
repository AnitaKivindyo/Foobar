'''
A function that takes a string parameter, and returns a sting of '1's and '0's representing the bumps and no bumps in the input string. 
The function should be able to:
 1. encode the 26 lower case letters.
 2. encode capital letters - by adding the capitization mark before the charcter.
 3. USe a blank character (000000) for spaces.

 Note: All signs are less than fifty characters long AND use only letters and spaces
'''

def solution(plaintext):
    #space = '000000'

    if not isinstance(plaintext,str) or len(plaintext)>50 or not all(char.isalpha() or char.isspace() for char in plaintext):
        raise ValueError
    

    else:

        caps_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

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
            '101011',  # z
            '000000'  # space
        ]
        caps = '000001'


        # mapping lower case characters 
        braille_mapping = {}

        for i in range(len(alphabet)):
            braille_mapping[alphabet[i]] = braille_key[i]

        #print (braille_mapping)

        # encode capital letters

        for letter in caps_alphabet:
            braille_mapping[letter] = f"{caps}{braille_mapping[letter.lower()]}"


        #split input text 
        input_string = plaintext.split(" ")
        result = []

        # convert the input into a list, including spaces
        for input in input_string:
            if result:
                result.append(" ")
            result.append(input)

        #print(result)

        output = []

        # iterate through each letter in the list and concatinate them in a list
        word_string_list = [] 

        for word in result:
            word_string= list(word)
            word_string_list.extend(word_string)


        #print(word_string_list) 

        #iterate through each letter in the word_string_list
        for letter in word_string_list:
            if letter in braille_mapping:
                value= braille_mapping[letter]
                output.append(value)

        #print(output)

        #join the output list to form a string
        encoded_text = ''.join(output)

        return encoded_text

#text =input('Enter an input')
#test1 = braille_translator(text)
#print(test1)


if __name__ == '__main__':
    # Test cases
    input_text = "A b"
    print(solution(input_text))

    #input_text = "code"
    print(solution(input_text))

    #input_text = "Braille"
    print(solution(input_text))






                



