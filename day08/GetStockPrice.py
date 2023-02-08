# 網路資料: https://tw.stock.yahoo.com/quote/{}
# <span class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)">540</span>  <-標籤(tag)名稱
# <span class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)">540</span>
# 安裝beautifulsoup
import requests
from bs4 import BeautifulSoup


def get_stock_price(stock_no):
    url = 'https://tw.stock.yahoo.com/quote/{}'.format(stock_no)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    # print(soup)
    tag_name = 'span'  # 選取 tage
    class_value = 'Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)'  # 選取 屬性內容
    tag = soup.find(name=tag_name, attrs={"class": class_value})  # 執行找出整個tag 從原始代碼  #  找第一次
    # print(tag)
    if tag is None:
        class_value = 'Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)'
        tag = soup.find(name=tag_name, attrs={"class": class_value})
    return tag.text





if __name__ == '__main__':
    price = get_stock_price('2330')
    print(price)























