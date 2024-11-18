# C:\Users\18896\Desktop\chromedriver-win64\chromedriver.exe

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import os

# 设置Chrome选项
chrome_options = Options()
chrome_options.add_argument("--headless")  # 如果你不想看到浏览器窗口，可以设置为无头模式
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# ChromeDriver路径
chrome_driver_path = r'C:\Users\18896\Desktop\chromedriver-win64\chromedriver.exe'  # 替换为你ChromeDriver的路径

# 创建Chrome浏览器对象
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 要爬取的网页URL
url = 'https://hanime1.me/comic/115898'
driver.get(url)

# 使用显式等待等待页面加载并确保图片元素出现
try:
    # 等待所有图片元素加载完毕
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, 'img'))
    )
except Exception as e:
    print("Error during waiting for images: ", e)
    driver.quit()
    exit()

# 获取页面源代码
page_source = driver.page_source

# 关闭浏览器
driver.quit()

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(page_source, 'html.parser')

# 找到所有图片标签
img_tags = soup.find_all('img')

# 创建一个文件夹来保存下载的图片
os.makedirs('images', exist_ok=True)

# 伪造请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 遍历所有图片标签并下载图片
for img in img_tags:
    img_url = img.get('src')
    if img_url:
        # 确保图片URL是完整的
        if not img_url.startswith('http'):
            img_url = 'https:' + img_url
        # 获取图片文件名
        img_name = os.path.basename(img_url)
        # 发送HTTP请求下载图片
        img_response = requests.get(img_url, headers=headers)
        if img_response.status_code == 200:
            # 将图片保存到文件夹
            with open(os.path.join('images', img_name), 'wb') as f:
                f.write(img_response.content)
            print(f"Downloaded {img_name}")
        else:
            print(f"Failed to download {img_name}")

print("All images have been downloaded.")


# 关闭浏览器
driver.quit()

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(page_source, 'html.parser')

# 找到所有图片标签
img_tags = soup.find_all('img')

# 创建一个文件夹来保存下载的图片
os.makedirs('images', exist_ok=True)

# 伪造请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 遍历所有图片标签并下载图片
for img in img_tags:
    img_url = img.get('src')
    if img_url:
        # 确保图片URL是完整的
        if not img_url.startswith('http'):
            img_url = 'https:' + img_url
        # 获取图片文件名
        img_name = os.path.basename(img_url)
        # 发送HTTP请求下载图片
        img_response = requests.get(img_url, headers=headers)
        if img_response.status_code == 200:
            # 将图片保存到文件夹
            with open(os.path.join('images', img_name), 'wb') as f:
                f.write(img_response.content)
            print(f"Downloaded {img_name}")
        else:
            print(f"Failed to download {img_name}")

print("All images have been downloaded.")
