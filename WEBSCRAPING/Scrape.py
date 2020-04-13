"""from bs4 import BeautifulSoup
import requests

url="https://www.imdb.com/chart/top/"
response=requests.get(url)
data=response.text
soup=BeautifulSoup(data , 'lxml')
#print(soup.prettify())
title=soup.find_all(class_="titleColumn")
for i in title:
    print(i.get_text())
#print(title)
"""
"""import requests
from requests_html import HTMLSession
session = HTMLSession()
r=session.get("https://www.imdb.com/chart/top/")
listerList = r.html.find(".lister-list" , first=True)
Title=listerList.find('.titleColumn')
rating = listerList.find('.ratingColumn strong')

for i in range(0,len(Title)):
    print(Title[i].text)
    print(rating[i].text)

img = listerList.find(".posterColumn a img")
for i in img:
    print(i.attrs['src'])
"""

#from bs4 import BeautifulSoup
#import requests

"""for i in range(50,71):
    i=str(i)
    url=("http://books.toscrape.com/catalogue/page-"+i+".html")
    response=requests.get(url)
    data=response.text
    soup=BeautifulSoup(data , 'lxml')
    print(soup.prettify())
    """
"""url="https://www.shutterstock.com/search/wallpaper?search_source=base_search_form&page=1&sort=popular&image_type=vector&safe=true&sharedid=&irgwc=1&utm_medium=Affiliate&utm_campaign=Freepik+Company%2C+S.L.&utm_source=39422&utm_term="
response = requests.get(url)
data=response.text
soup=BeautifulSoup(data,"lxml")
img = soup.find_all(class_="z_g_c")
x=int(input(":"))
y=int(input(":"))
for i in range(x,y+1):
    print(soup.prettify())



from bs4 import BeautifulSoup
from requests_html import HTMLSession
import csv

session = HTMLSession()
urls=[]
for i in range(1,51):
    urls.append(f"http://books.toscrape.com/catalogue/page-{i}.html")

csv_file=open('book.csv','w')
csv_writer=csv.writer(csv_file,lineterminator='\n')

csv_writer.writerow(["Title","Price","ImageURL"])
count=1
for url in urls:
    source=session.get(url).html.html
    soup=BeautifulSoup(source,'lxml')

    box=soup.find('ol')
    elements = box.find_all('li')
    title=[]
    pics=[]
    cost=[]
    for element in elements:
        name = element.select('h3 a')[0]['title']
        title.append(name)
        image=element.select('img')[0]['src']
        image_url=r'http://books.toscrape.com/'+image
        pics.append(image_url)
        price=element.find('p',class_='price_color').text
        cost.append(price)
        csv_writer.writerow([name,pics,cost])
        print(count,end='')
        count+=1

csv_file.close()"""


from bs4 import BeautifulSoup
from requests_html import HTMLSession
import csv

session=HTMLSession()
url="https://www.zomato.com/mumbai/kharghar-restaurants"
csv_file=open('sweets.csv','w')
csv_writer=csv.writer(csv_file,lineterminator='\n')
csv_writer.writerow(['name','location','imgURL','ratings'])
count=1
source=session.get(url).html.html
soup=BeautifulSoup(source,'lxml')

box=soup.find('orig-search-list')
elements = box.find_all('div', class_='col-s-12')
name=[]
location=[]
img=[]
ratings=[]
for element in elements:
    nm =element.select(('a')[0]['title'])
    name.append(nm)
    ln =element.select("div.col-m-16 search-result-addess grey-text nowrap ln22")
    location.append(ln)
    rat=element.find('div',class_="rating-popup rating-for-19269148 res-rating-nf right level-7 bold").text
    ratings.append(rat)
    csv_writer.writerow(['name','location','ratings'])
    print(count)
    count=+1

csv_file.close()
