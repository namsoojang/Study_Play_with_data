from selenium import webdriver
 
# 드라이버 추출하기 
driver = webdriver.Chrome()

# 검색 페이지 로딩 
print("## 페이지 로딩 ## ")
keyword = "강남역"
path = "https://www.diningcode.com/isearch.php?query=" + keyword
driver.get(path)
driver.implicitly_wait(3)

# 추천 카테고리로 가져오기 
tags = driver.find_elements_by_xpath("//*[@id='main_area']/div/div/div/div/div/a")
print("## '", keyword, "' 추천 카테고리")
for tag in tags :
    print("\t - ", tag.text)

print("## 추천 레스토랑 ")
resturant_names = driver.find_elements_by_xpath("//*[@id='main_area']/div/div/div/div/div/div/a")
for name in resturant_names :
    print("\t - ", name.text)