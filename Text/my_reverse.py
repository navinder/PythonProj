'''
Created on Dec 13, 2013

@author: navinder
'''

def reverse_string(string):
    chars=[char for char in string]
    print chars
    for index in range(len(chars)/2):
        chars[index],chars[len(chars)-index-1]=chars[len(chars)-index-1],chars[index]
    return ''.join(chars)
    

def driver():
    #input_string= raw_input("Enter the string : ")
    input_string="navinder jeet"
    print reverse_string(input_string)


if __name__ == '__main__':
    driver()