'''
Created on Dec 13, 2013

@author: Navinder
'''
import collections

def vowelCounter():
    str= raw_input("Enter the string:")
    vow_dict=collections.defaultdict(lambda : 0)
    #str= "sdsaaamauocao uda"
    vowels="aeiou"
    for c in str:
        if c in vowels and c in vow_dict.keys():
            vow_dict[c]= vow_dict[c]+1
        elif c in vowels and c not in vow_dict.keys():
                vow_dict[c]=1
    
    for vow,count in vow_dict.items():
        print vow,":",count
                
if __name__ == '__main__':
    vowelCounter()
