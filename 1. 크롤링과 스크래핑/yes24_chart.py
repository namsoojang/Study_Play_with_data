import requests
from bs4 import BeautifulSoup

url = "http://www.yes24.com/24/category/bestseller"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

bestList = soup.select("ol > li")
print(len(bestList))

#bestList > ol > li.num1 > p:nth-child(3) > a
for book in bestList[:5]:
    #bestList > ol > li.num1 > p:nth-child(3) > a
    title = book.select('p > a')[2].text
    #bestList > ol > li.num1 > p.aupu > a:nth-child(1)
    author = book.select('p.aupu > a')[0].text
    #bestList > ol > li.num1 > p.aupu > a:nth-child(2)
    company = book.select('p.aupu > a')[1].text
    #bestList > ol > li.num1 > p.price
    price_text = book.select('p.price')[0].text
    price = book.select('p.price > strong')[0].text
    #bestList > ol > li.num1 > p:nth-child(7)
    stars = book.select('p')[6].select('img')
    # 평점 확인 : print(len(stars))
    try:
        # 내용 평점 가져오기
        star_content = 0
        for star in stars[:5]:
            if (star['src'][-6:-4] == 'On') : 
                star_content += 1
        # 편집/구성 평점 가져오기
        star_edit = 0
        for star in stars[5:]:
            if (star['src'][-6:-4] == 'On') :
                star_edit += 1
    except:
        star_content = 0
        star_edit = 0

    print(title, author, company, price_text, price, star_content, star_edit, sep=' / ')

# 참고 : 크롬에서 가져오는 값 
    # HTML : <img src="http://image.yes24.com/sysimage/interface/smallStarOn.gif" align="absmiddle">
    # SELECTOR : #bestList > ol > li.num1 > p:nth-child(7) > img:nth-child(1) 
    # XPATH //*[@id="bestList"]/ol/li[1]/p[7]/img[1]
