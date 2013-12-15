'''
Created on Dec 13, 2013

@author: sean
'''

def check_pallindrome():
    str="racecarq"
    print str[::-1]
    for i in range(len(str)):
        if str[i] != str[len(str)-i-1]:
            print (str, 'is not a pallindrome')
            return
    print str, "is a pallindrome"

if __name__ == '__main__':
    check_pallindrome()
    
    