"""import requests
li=["https://www.google.com/","https://www.ubereats.com/en-US/","https://twitter.com","https://www.facebook.com/"]
for i in li:
    
    
    a = requests.get(i)

    print(a.encoding)
    print(a.status_code)
    print(a.elapsed)
    print(a.url)
    #print(a.text)
"""
'''import requests
n=int(input("enter no. of webs:"))
for i in range(0,n):
    a=requests.get(input("enter the url:"))
    print(a.encoding)
    print(a.status_code)
    print(a.url)'''
#slicing
'''import requests
a = requests.get("https://www.google.com/")
print (a.text[0:501])'''


"""import requests
from requests_html import HTMLSession
session=HTMLSession()
"""
'''r = session.get("https://www.imdb.com/chart/top/")
listerList=r.html.find(".lister-list",first=True)
print(listerList)
Title=listerList.find('.titleColumn')
rating = listerList.find('.ratingColumn strong')

for i in range(0,len(Title)):
    print(Title[i].text)
    print(rating[i].text)

img = listerList.find(".posterColumn a img")
for i in img:
    print(i.attrs['src'])

r = session.get("https://www.imdb.com/movies-coming-soon/")
overview=r.html.find(".list", first=True)
print(overview)
Title=overview.find(".overview-top  a")
Cast=overview.find(".txt-block a")
print(Title[0])
for i in range(0,len(Title)):
    print(Title[i].text)
    # print(Cast[i].text)

r = session.get("https://www.imdb.com/title/tt1187043/")
listerList=r.html.find(".title_block " , first=True)
print(listerList.text)
img=listerList.find(".slate_wrapper poster a img")
print(img.attrs["src"])'''


import requests
from requests_html import HTMLSession
session=HTMLSession()
r = session.get("https://www.imdb.com/movies-in-theaters/")
listerList = r.html.find(".overview-top")
#print(listerList.text)
Title=[]
for i in listerList:
    Title.append(i.find("h4 a")[0].text)

for j in Title:
    print(j)
