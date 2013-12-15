'''
Created on Dec 14, 2013

@author: sean
'''
from collections import defaultdict
import operator
def count_words(str):
    word_dict=defaultdict(int)
    words=str.split()
    for word in words:
        if word in word_dict:  word_dict[word]+=1 
        else: word_dict[word]=1
    word_dict=sorted(word_dict.iteritems(), key=operator.itemgetter(1),reverse=True)
    for word,count in word_dict[:5]:
        print word,count
    

if __name__ == '__main__':
    str="csec vrsv wrev wef v srv se vwes v se kal jal kal jal v se se kal"
    count_words(str)