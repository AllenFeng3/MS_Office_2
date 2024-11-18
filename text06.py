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

    # 初始化大字典
    word_info = {"welcome": {}}

    # 查找词性和对应释义
    pos_section = soup.find_all("div", class_="qdef")
    if pos_section:
        for pos in pos_section:
            meanings = pos.find_all("li")
            for meaning in meanings:
                # 提取词性 (如 n., adj.)
                pos_key = meaning.find("span", class_="pos").get_text(strip=True).rstrip(".")
                # 提取释义
                definition = meaning.find("span", class_="def").get_text(strip=True)

                # 将释义存储到字典中
                if pos_key not in word_info["welcome"]:
                    word_info["welcome"][pos_key] = []
                word_info["welcome"][pos_key].append(definition)

    # 查找其他信息（如过去式、复数等）
    inflections_section = soup.find("div", class_="hd_if")
    print(inflections_section)
    if inflections_section:
        inflections = inflections_section.find_all("li")
        for inflection in inflections:
            # 提取形式和内容
            form = inflection.find("span", class_="p").get_text(strip=True)
            print(form)
            content = inflection.find("span", class_="p1-11").get_text(strip=True)

            # 将信息存储到字典中
            word_info["welcome"][form] = content

    # 输出大字典
    print("提取结果：")
    for key, value in word_info["welcome"].items():
        print(f"{key}: {value}")

    print(word_info)
else:
    print(f"请求失败，状态码: {response.status_code}")
