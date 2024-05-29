'''
2024/5/29

作用: 利用網路爬蟲生成電影json檔案的資訊

使用技術: 網路爬蟲 -> [selenium 、 bs4]
資料來源網址: https://www.vscinemas.com.tw/vsweb/film/index.aspx

< 環境配置需求 >
chrome-test : (合適的版本)
web_driver : (合適的版本)
-- 參考 : https://googlechromelabs.github.io/chrome-for-testing/

'''


target_link = 'https://www.vscinemas.com.tw/vsweb/film/index.aspx'
chrome_driver_path = r'C:\Users\USER\Desktop\chrome-test\chromedriver-win64\chromedriver.exe'

def w_json(data:dict):
    import json
    # 指定儲存位置並將資料寫入JSON檔案
    file_path = r'.\data.json'
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)
        print(f"JSON檔案已建立\n位置:{file_path}\n資訊:{data}")

def select_by_bs4(element) -> dict:
    data = {}
    from bs4 import BeautifulSoup
    element_html = element.get_attribute("outerHTML")
    soup = BeautifulSoup(element_html)
    li_tags = soup.find_all('li')
    index = 0
    check = []
    for i in li_tags:
        # print(type(i)) -> 顯示 <class 'bs4.element.Tag'> 需要變成str才可以利用bs4抓取
        soup2 = BeautifulSoup(str(i), "html.parser")
        img_link = soup2.find("img").get("src")
        img_link = str(img_link).replace("..","https://www.vscinemas.com.tw/vsweb")
        
        flim_name = soup2.find(class_ = "infoArea").find("a")
        flim_name = flim_name.text

        # check duplicate information
        if flim_name in check:
            continue

        # store information
        data[index] = {"name":flim_name,"img":img_link}
        check.append(flim_name)
        index += 1
    return data

# 預設環境
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")

# 載入網頁
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)    # 指向 chromedriver 的位置
driver.get(target_link)
wait = WebDriverWait(driver, 10)

element = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".movieList"))
)

data = select_by_bs4(element)
w_json(data)