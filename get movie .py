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
        print("成功 建立/更新 json檔")
        # print(f"JSON檔案已建立\n位置:{file_path}\n資訊:{data}")

def select_by_bs4(element) -> dict:
    data = {}
    from bs4 import BeautifulSoup
    element_html = element.get_attribute("outerHTML")
    soup = BeautifulSoup(element_html)
    li_tags = soup.find_all('li')
    num = 0
    check = []
    for i in li_tags:
        # print(type(i)) -> 顯示 <class 'bs4.element.Tag'> 需要變成str才可以利用bs4抓取
        soup2 = BeautifulSoup(str(i), "html.parser")

        # 抓取照片
        img_link = soup2.find("img").get("src")
        img_link = str(img_link).replace("..","https://www.vscinemas.com.tw/vsweb")
        
        # 抓取片名
        flim_name = soup2.find(class_ = "infoArea").find("a")
        flim_name = flim_name.text

        # 載入新網頁
        href = soup2.find("a").get("href")
        detail_link = target_link.replace("index.aspx",href)
        driver.get(detail_link)
        content = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".movieInfo")))
        try:
            # 上映時間
            release_date = content.find_element(By.CSS_SELECTOR, "time")
            release_date = "威秀" + release_date.text

            # 抓取內文
            info = content.find_element(By.CSS_SELECTOR, "table").text
            info = info.replace("：\n","：")
        except Exception as e:
            if "No symbol" in str(e):
                error_message = f"電影名稱: {flim_name} \n 錯誤類別: 定位元素時出現錯誤"
                print(error_message)
                print()
                continue
            print("未知的錯誤")
            error_message = f"電影名稱: {flim_name} \n 錯誤類別: 未知"
            print(error_message)
            print()
            continue

        # check duplicate information
        if flim_name in check:
            continue
        # if "：" in flim_name:
        #     # print(flim_name)
        #     # print("修改過後->")
        #     index = flim_name.index("：")
        #     new_name = flim_name[:index+1] + "\n" + flim_name[index+3:]
        #     # print(new_name)
        #     new_name = new_name.strip()
        #     flim_name = new_name

        # store information
        data[num] = {"name":flim_name,"img":img_link,"time":release_date,"info":info,"link":detail_link}
        check.append(flim_name)
        num += 1
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