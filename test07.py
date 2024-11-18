import requests
from bs4 import BeautifulSoup
import re


def scrape_bing_dict(url, key):
    try:
        # 发送 HTTP 请求获取网页内容
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # 使用 BeautifulSoup 解析网页内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 使用正则表达式匹配英文单词和汉字
        english_pattern = re.compile(r'[a-zA-Z]+')
        chinese_pattern = re.compile(r'[\u4e00-\u9fa5]+')

        english_words = set()  # 使用集合避免重复
        chinese_words = set()

        # 遍历所有标签提取文本
        for text in soup.stripped_strings:
            english_words.update(english_pattern.findall(text))
            chinese_words.update(chinese_pattern.findall(text))

        # 将结果存储到字典中
        result = {
            key: {
                'english': list(english_words),
                'chinese': list(chinese_words)
            }
        }

        return result

    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None


# 示例用法
url = "https://www.bing.com/dict/search?q=welcome&FORM=BDVSP6&cc=cn"
key = "welcome"
result = scrape_bing_dict(url, key)
if result:
    print(result)
