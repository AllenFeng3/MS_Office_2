import requests
from bs4 import BeautifulSoup


def fetch_bing_dict_full(word):
    # 构造URL
    url = f"https://www.bing.com/dict/search?q={word}&FORM=BDVSP6&cc=cn"

    # 发送HTTP请求
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # 解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 获取单词
        word_title = soup.find("div", {"class": "qdef"}).find("h1").text.strip()
        print(f"单词: {word_title}")

        # 获取音标
        phonetics_us = soup.find_all("div", {"class": "hd_prUS"})
        phonetics_us_text = [p.text.strip() for p in phonetics_us]
        phonetics_en = soup.find_all("div", {"class": "hd_pr"})
        phonetics_en_text = [p.text.strip() for p in phonetics_en]
        print("音标:", ", ".join(phonetics_us_text), ", ".join(phonetics_en_text))

        # 获取释义
        definitions = [item.text for item in soup.find_all("span", {"class": "def"})]
        print("释义:")
        for i, definition in enumerate(definitions, 1):
            print(f"{i}. {definition}")

        # 获取例句
        examples = soup.find_all("div", {"class": "sen_en"})
        print("例句:")
        for example in examples:
            print(f" - {example.text.strip()}")

        # 获取短语和搭配
        phrases = soup.find("div", {"class": "df_div2"})
        if phrases:
            print("短语和搭配:")
            phrase_items = phrases.find_all("a")
            for phrase in phrase_items:
                print(f" - {phrase.text.strip()}")

        # 获取同义词和反义词
        synonyms = soup.find("div", {"class": "syn_fl"})
        if synonyms:
            print("同义词和反义词:")
            synonym_items = synonyms.find_all("a")
            for synonym in synonym_items:
                print(f" - {synonym.text.strip()}")

    else:
        print(f"请求失败，状态码: {response.status_code}")


# 示例调用
fetch_bing_dict_full("welcome")
