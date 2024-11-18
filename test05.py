import requests
from bs4 import BeautifulSoup

# 设置目标URL
url = "https://www.bing.com/dict/search?q=welcome&FORM=BDVSP6&cc=cn"

# 设置请求头，模拟浏览器行为
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

# 发起GET请求
response = requests.get(url, headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    # 解析HTML内容
    soup = BeautifulSoup(response.content, "html.parser")

    # 查找例句部分
    examples_section = soup.find_all("div", class_="se_li")

    print("例句:")
    for example in examples_section:
        # 查找例句中的文字
        english = example.find("div", class_="sen_en").get_text(strip=True)
        chinese = example.find("div", class_="sen_cn").get_text(strip=True)
        print(f"英文: {english}\n中文: {chinese}\n")
else:
    print(f"请求失败，状态码: {response.status_code}")
