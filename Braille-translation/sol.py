def solution(s):
    if not isinstance(s, str) or len(s) > 50 or not all(char.isalpha() or char.isspace() for char in s):
        raise ValueError("Invalid input")

    caps_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet = 'abcdefghijklmnopqrstuvwxyz '

    braille_key = [
        '100000', '110000', '100100', '100110', '100010', '110100', '110110', '110010', '010100', '010110',
        '101000', '111000', '101100', '101110', '101010', '111100', '111110', '111010', '011100', '011110',
        '101001', '111001', '010111', '101101', '101111', '101011', '000000'
    ]
    caps = '000001'

    braille_mapping = {}
    
    for i, char in enumerate(alphabet):
        braille_mapping[char] = braille_key[i]

    for letter in caps_alphabet:
        braille_mapping[letter] = f"{caps}{braille_mapping[letter.lower()]}"
    
    input_string = s.split()
    result = []

    for input_text in input_string:
        if result:
            result.append(' ')
        result.append(input_text)

    output_list = []
    
    for word in result:
        if word == ' ':
            output_list.append(braille_mapping[' '])
        else:
            for letter in word:
                if letter in braille_mapping:
                    value = braille_mapping[letter]
                    output_list.append(value)
    
    Output = ''.join(output_list)
    
    return Output