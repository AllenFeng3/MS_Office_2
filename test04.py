from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


def fetch_bing_dict_with_selenium(word):
    url = f"https://www.bing.com/dict/search?q={word}&FORM=BDVSP6&cc=cn"

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # 无头模式
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)

        # 显式等待释义部分加载
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "qdef"))
        )

        # 获取页面内容
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # 提取单词标题
        word_title = soup.find("div", {"class": "qdef"}).find("h1").text.strip()
        print(f"单词: {word_title}")

        # 提取释义部分
        definitions_section = soup.find("ul", {"class": "qdef"}).find_all("li")
        print("释义和单词类型:")
        for i, item in enumerate(definitions_section, 1):
            pos = item.find("span", {"class": "pos"}).text.strip() if item.find("span", {"class": "pos"}) else "N/A"
            definition = item.find("span", {"class": "def"}).text.strip()
            print(f"{i}. [{pos}] {definition}")

    except Exception as e:
        print(f"提取数据时出错: {e}")
    finally:
        driver.quit()


# 示例调用
fetch_bing_dict_with_selenium("welcome")
