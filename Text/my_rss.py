'''
Created on Dec 15, 2013

@author: sean
'''
import urllib2
import re


def get_rss(url):
    ''' function to return the rss feed from the passed url'''
    response= urllib2.urlopen(url).read()
    
    #extract the titles and their links data in html format
    link_format=re.compile('<link>(.*?)</link>')
    title_format= re.compile('<title>(.*?)</title>')
    
    #extract the english titles and their links
    titles_list= re.findall(title_format, response)[1:]
    link_list= re.findall(link_format, response)[1:]
    for (title,link) in zip(titles_list, link_list):
        print title,"\n", link,"\n"
        
        
if __name__ == '__main__':
    url='http://feeds.abcnews.com/abcnews/topstories'
    #url='http://feeds.feedburner.com/WebDesignLedger'
    get_rss(url)