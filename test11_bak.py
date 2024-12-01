import os
import time

import requests
from bs4 import BeautifulSoup

# 基本配置信息
base_url = "http://csyhfy.hunancourt.gov.cn"

save_dir = "雨花区法院page1"  # 保存xlsx文件的目录

# 模拟浏览器的请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

# 确保保存目录存在
os.makedirs(save_dir, exist_ok=True)


def download_xlsx(file_url, save_path):
    """下载xlsx文件并保存"""
    try:
        response = requests.get(file_url, headers=headers)
        response.raise_for_status()
        with open(save_path, "wb") as file:
            file.write(response.content)
        print(f"下载成功: {save_path}")
    except Exception as e:
        print(f"下载失败: {file_url}, 错误: {e}")


def scrape_site(start_page):
    """爬取主页面和子页面，下载xlsx文件"""
    try:
        # 获取主页面内容
        response = requests.get(start_page, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # 提取所有标题链接
        links = soup.find_all("a", href=True)
        for link in links:
            href = link["href"]
            if "article/detail" in href:  # 确保是子页面链接
                child_page_url = base_url + href
                # child_page_url = href
                print(f"解析子页面: {child_page_url}")

                # 请求子页面
                child_response = requests.get(child_page_url, headers=headers)
                child_response.raise_for_status()
                child_soup = BeautifulSoup(child_response.text, "html.parser")

                # 查找xlsx文件链接
                xlsx_links = child_soup.find_all("a", href=True)
                for xlsx_link in xlsx_links:
                    xlsx_href = xlsx_link["href"]
                    print(xlsx_href)

                    
                    if xlsx_href.endswith(".xlsx") or xlsx_href.endswith(".xls"):  # 确保是xlsx文件
                        # file_url = base_url + xlsx_href
                        print(xlsx_link.text)
                        file_url = xlsx_href
                        print(file_url)
                        file_name = xlsx_link.text + ".xlsx"
                        save_path = os.path.join(save_dir, file_name)
                        download_xlsx(file_url, save_path)

                        time.sleep(1)

    except Exception as e:
        print(f"爬取失败: {e}")


# 开始爬取
# start_page = "http://csyhfy.hunancourt.gov.cn/article/index/id/M0guNjDINDAwNCACAAA/page/11.shtml"
# scrape_site(start_page)



# 定义基础 URL
start_page = "http://csyhfy.hunancourt.gov.cn/article/index/id/M0guNjDINDAwNCACAAA/page/"

# 使用列表推导式生成从 1 到 100 页的 URL
urls = [f"{start_page}{page}.shtml" for page in range(2, 3)]

# 打印生成的 URL 列表
for url in urls:
    # print(url)
    scrape_site(url)

