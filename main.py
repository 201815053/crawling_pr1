from bs4 import BeautifulSoup as BS
import requests as req

# 네이버 주식 종가
# url = "https://finance.naver.com/sise/lastsearch2.naver"
# res = req.get(url)
# soup = BS(res.text, "html.parser")

# # for title in soup.select("a.tltle"):
# #     print(title.get_text(strip=True))

# # print(len(soup.select("a.tltle")))

# for tr in soup.select("table.type_5 tr"):
#     if len(tr.select("a.tltle")) == 0:
#         continue
#     title = tr.select("a.tltle")[0].get_text(strip=True)  
#     price = tr.select("td.number:nth-child(4)")[0].get_text(strip=True)
#     change = tr.select("td.number:nth-child(6)")[0].get_text(strip=True)
#     print(title, price, change) #종목명, 현재가, 등락률

# 야후 주식 종가
url = "https://finance.yahoo.com/most-active"
res = req.get(url)
soup = BS(res.text, "html.parser")

for tr in soup.select("table tbody tr"):
    title = tr.select("td:nth-child(1) a")[0].get_text(strip=True)
    price = tr.select("td:nth-child(3) fin-streamer")[0].get_text(strip=True)
    change = tr.select("td:nth-child(5) span")[0].get_text(strip=True)
    print(title, price, change) #symbol, price, % change

