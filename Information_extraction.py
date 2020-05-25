import urllib.request
import bs4
import string
import re

import nltk

modified_punctuation=string.punctuation
modified_punctuation=modified_punctuation.replace('\'','')


myurl=urllib.request.urlopen("http://tuxworld.wordpress.com")
html_string=myurl.read()
text=bs4.BeautifulSoup(html_string,'html.parser').get_text()
text=text.encode("ascii","ignore")
text=text.decode()
text1=text

for i in modified_punctuation:
    text=text.replace(i," ")
text=text.split()


print("Text: ",text)
#TO to remove all special characters and left only ascii text
text_list=[]
for i in  text:
    if i not in string.punctuation:
        text_list.append(i)

#TO lowercase all letters
for i in range(len(text_list)):
    text_list[i]=text_list[i].lower()

for i in text_list:
    temp=""
    for j in i:
        if j in string.ascii_lowercase:
            temp=temp+j
    i=temp

#TO remove stop words
#stopwords actually depend what u want, language keep changing.
#there is short list of stopwords and long list of stopwords
#different library different size of stopwords
#download stopwords via nltk, go google
from nltk.corpus import stopwords
#nltk.download('stopwords') add this line to download
all_stopwords=stopwords.words('english')
all_stopwords.append('has')
print("Stopword:", all_stopwords)

#you can jump to line 220 if you wish to use first stopwords from NLTK - shortcut ( CTRL +G )
#this is default stopwords from the link provided
# all_stopwords2=['a','about','above','after','again','against','all','am','an','and','any','are','aren\'t','as','at','be','because','been','before'
# ,'being'
# ,'below'
# ,'between'
# ,'both'
# ,'but'
# ,'by'
# ,'can\'t'
# ,'cannot'
# ,'could'
# ,'couldn\'t'
# ,'did'
# ,'didn\'t'
# ,'do'
# ,'does'
# ,'doesn\'t'
# ,'doing'
# ,'don\'t'
# ,'down'
# ,'during'
# ,'each'
# ,'few'
# ,'for'
# ,'from'
# ,'further'
# ,'had'
# ,'hadn\'t'
# ,'has'
# ,'hasn\'t'
# ,'have'
# ,'haven\'t'
# ,'having'
# ,'he'
# ,'he\'d'
# ,'he\'ll'
# ,'he\'s'
# ,'her'
# ,'here'
# ,'here\'s'
# ,'hers'
# ,'herself'
# ,'him'
# ,'himself'
# ,'his'
# ,'how'
# ,'how\'s'
# ,'i'
# ,'i\'d'
# ,'i\'ll'
# ,'i\'m'
# ,'i\'ve'
# ,'if'
# ,'in'
# ,'into'
# ,'is'
# ,'isn\'t'
# ,'it'
# ,'it\'s'
# ,'its'
# ,'itself'
# ,'let\'s'
# ,'me'
# ,'more'
# ,'most'
# ,'mustn\'t'
# ,'my'
# ,'myself'
# ,'no'
# ,'nor'
# ,'not'
# ,'of'
# ,'off'
# ,'on'
# ,'once'
# ,'only'
# ,'or'
# ,'other'
# ,'ought'
# ,'our'
# ,'ours'
# ,'ourselves'
# ,'out'
# ,'over'
# ,'own'
# ,'same'
# ,'shan\'t'
# ,'she'
# ,'she\'d'
# ,'she\'ll'
# ,'she\'s'
# ,'should'
# ,'shouldn\'t'
# ,'so'
# ,'some'
# ,'such'
# ,'than'
# ,'that'
# ,'that\'s'
# ,'the'
# ,'their'
# ,'theirs'
# ,'them'
# ,'themselves'
# ,'then'
# ,'there'
# ,'there\'s'
# ,'these'
# ,'they'
# ,'they\'d'
# ,'they\'ll'
# ,'they\'re'
# ,'they\'ve'
# ,'this'
# ,'those'
# ,'through'
# ,'to'
# ,'too'
# ,'under'
# ,'until'
# ,'up'
# ,'very'
# ,'was'
# ,'wasn\'t'
# ,'we'
# ,'we\'d'
# ,'we\'ll'
# ,'we\'re'
# ,'we\'ve'
# ,'were'
# ,'weren\'t'
# ,'what'
# ,'what\'s'
# ,'when'
# ,'when\'s'
# ,'where'
# ,'where\'s'
# ,'which'
# ,'while'
# ,'who'
# ,'who\'s'
# ,'whom'
# ,'why'
# ,'why\'s'
# ,'with'
# ,'won\'t'
# ,'would'
# ,'wouldn\'t'
# ,'you'
# ,'you\'d'
# ,'you\'ll'
# ,'you\'re'
# ,'you\'ve'
# ,'your'
# ,'yours'
# ,'yourself'
# ,'yourselves'
# ]


#can actually done using shorter codes..... can actually do with python in or NLTK
# for i in all_stopwords:
#     if i in text_list:
#         text_list.remove(i)

#to complete assignment, we use string matching algorithm, in fact binary search would be much faster T(n)= logn

newtext=" "
for i in text_list:
    newtext=newtext+i+" "
print("Text_List: ",text_list)
print("NEWTEST: ",newtext)

num_allchars=256
def badCharSet(stringg,size):
    badChar=[-1]*num_allchars
    for i in range(size):
        badChar[ord(stringg[i])]=i

    return badChar

def boyer_moore(txt,pat):
    m=len(pat)
    n=len(txt)
    txt2=txt


    badChar=badCharSet(pat,m)
    # s is shift of the pattern with respect to text
    s=0
    while(s<=n-m):
        j=m-1
        # print(j)
        front_space = False
        back_space = False

        # front_space and back_space used to check whether its a full word
        if s+j+1<len(txt):
            if txt[s+j+1]==" ":
                back_space=True
        # comparing the last character consequently to front
        while j>=0 and pat[j]==txt[s+j]:
            j-=1

        if txt[s+j]==" ":
            front_space=True
        # print(front_space)
        # print(back_space)
        if j < 0 and front_space==True and back_space==True:
            # print("Pattern occur at shift = {}".format(s))
            txt2=re.sub(" "+pat+" "," ",txt2)

            # s will shift to the next position where the pattern is matched
            s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
        else:
            # print(ord(txt[s + j]))
            # s will shift to the next position by choosing 1 or the maximum shifting
            s += max(1, j - badChar[ord(txt[s + j])])


    return txt2


# to compare each stopword to the text
for i in all_stopwords:
    newtext=boyer_moore(newtext,i)

print("Corrected text: ",newtext)

newtext_list=newtext.split()
dictt={}
for i in newtext_list:
    if i in dictt:
        dictt[i]=dictt[i]+1
    else:
        dictt[i]=1

print(dictt)
print("\nBest Time Complexity of Boyer Moore: O(n/m)")
print("Worst Time Complexity of Boyer Moore: O(mn)")
print(("In this case, the time complexity would times m"))
