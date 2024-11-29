import time

import requests
import csv


def read_csv_to_dict(file_path):
    data_dict = {}

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        # 跳过表头
        next(csv_reader)
        for row in csv_reader:
            data_dict[row[0]] = {}

    return data_dict


def fetch_word_html(word):
    """
    根据关键词爬取 Bing 字典的页面并保存为 HTML 文件。
    如果爬取失败，将关键词保存到 cannotfind.csv 文件中。

    参数：
        word (str): 要搜索的关键词。
    """
    # 构造 URL
    url = f"https://www.bing.com/dict/search?q={word}&FORM=BDVSP6&cc=cn"

    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    try:
        # 发送 HTTP 请求
        response = requests.get(url, headers=headers)

        # 检查响应状态码
        if response.status_code == 200:
            # 保存 HTML 内容到文件
            filename = f"docs/htmlDocs/{word}.html"
            with open(filename, "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"页面已成功保存为 {filename}")
            time.sleep(1)
        else:
            # 将关键词保存到 cannotfind.csv 文件
            print(f"无法爬取关键词：{word}，状态码：{response.status_code}")
            save_to_csv(word)
    except Exception as e:
        # 处理请求错误并记录关键词
        print(f"爬取关键词 {word} 时发生错误：{e}")
        save_to_csv(word)


def save_to_csv(word):
    """
    将无法爬取的关键词保存到 cannotfind.csv 文件。

    参数：
        word (str): 无法爬取的关键词。
    """
    try:
        with open("cannotfind.csv", mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([word])
        print(f"关键词 {word} 已保存到 cannotfind.csv")
    except Exception as e:
        print(f"无法保存关键词 {word} 到 cannotfind.csv：{e}")


def main():
    filepath = "docs/csvDocs/cet46officialwords.csv"
    dict_words = read_csv_to_dict(filepath)
    for word in dict_words:
        fetch_word_html(word)


if __name__ == "__main__":
    main()
