import csv
import json
import time

import requests
from bs4 import BeautifulSoup


# 读取csv文件并返回列表
def read_csv_to_dict(file_path):
    data_dict = {}

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        # 跳过表头
        next(csv_reader)
        for row in csv_reader:
            data_dict[row[0]] = {}

    return data_dict


def fetch_bing_dict_full(word):
    word_dict = {"phonemes": {}, "translations": {}, "tense_plural": {}, "collocation_thesaurus_antonym": {},
                 "interpretation": {}, "sample_sentences": {}}

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
        # word_title = soup.find("div", {"class": "qdef"}).find("h1").text.strip()
        # print(f"单词: {word_title}")

        # 获取音标并存储进word_dict, key为phonemes
        phonetics_us = soup.find_all("div", {"class": "hd_prUS"})
        phonetics_us_text = [p.text.strip() for p in phonetics_us]
        phonetics_en = soup.find_all("div", {"class": "hd_pr"})
        phonetics_en_text = [p.text.strip() for p in phonetics_en]

        if phonetics_us_text:
            word_dict["phonemes"]["美"] = phonetics_us_text[0][2:]
        if phonetics_en_text:
            word_dict["phonemes"]["英"] = phonetics_en_text[0][2:]
        # print("音标:", ", ".join(phonetics_us_text), ", ".join(phonetics_en_text))

        # 获取复数,现在健忘,过去式
        phonetics_us = soup.find_all("div", {"class": "hd_if"})
        phonetics_us_text = [p.text.strip() for p in phonetics_us]
        if phonetics_us_text:
            key_val = phonetics_us_text[0].split("\xa0\xa0")
            for e in key_val:
                key, value = e.split("：")
                word_dict["tense_plural"][key] = value

        # 查找词性和对应释义并存储进word_dict, key为translations
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
                    if pos_key not in word_dict["translations"]:
                        word_dict["translations"][pos_key] = []

                    word_dict["translations"][pos_key] = definition

        # 获取例句并存储进word_dict, key为sample_sentences:
        examples_section = soup.find_all("div", class_="se_li")
        set_len = len(examples_section)
        set_cnt = 0
        sn_li = ""

        # print("例句:")
        for example in examples_section:
            # 获取英文例句的内容，保留格式
            english_parts = example.find("div", class_="sen_en").find_all(string=True)
            english = "".join(english_parts).strip()

            # 获取中文翻译
            chinese = example.find("div", class_="sen_cn").get_text(strip=True)
            set_cnt += 1
            if set_cnt != set_len:
                sn_li = sn_li + str(set_cnt) + ". " + english + '\n' + chinese + '\n'
            else:
                sn_li = sn_li + str(set_cnt) + ". " + english + '\n' + chinese

        word_dict["sample_sentences"] = sn_li
        # print(word_dict)

        # 获取搭配,同义词和反义词
        # tb_divs = soup.find_all("div", {"class": "tb_div"})
        # # todo
        # for tb_div in tb_divs:
        #     pass
        #
        # phrases = soup.find("div", {"class": "df_div2"})
        # if phrases:
        #     print("短语和搭配:")
        #     phrase_items = phrases.find_all("a")
        #     for phrase in phrase_items:
        #         print(f" - {phrase.text.strip()}")

        # 获取同义词和反义词
        # synonyms = soup.find("div", {"class": "syn_fl"})
        # if synonyms:
        #     print("同义词和反义词:")
        #     synonym_items = synonyms.find_all("a")
        #     for synonym in synonym_items:
        #         print(f" - {synonym.text.strip()}")

    else:
        print(f"请求失败，状态码: {response.status_code}")

    return {word: word_dict}


# 将单条字典数据追加到 JSON Lines 文件
def store_single_dict(data, file_path):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(json.dumps(data, ensure_ascii=False) + '\n')
    print(f"已存储数据: {data}")


# 从 JSON Lines 文件读取所有记录
def read_all_data(file_path):
    data_list = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                data_list.append(json.loads(line.strip()))
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在！")
    return data_list


# 示例
if __name__ == "__main__":

    # 示例调用
    # fetch_bing_dict_full("win")

    file_name = "data_bak.json"
    file_path = r'docs/z_toeflcet46.csv'  # 替换为你的 CSV 文件路径
    # data = read_csv_to_dict(file_path)
    # for data_key in data.keys():
    #     print(data_key)
    #     dict = fetch_bing_dict_full(data_key)
    #     # 存储数据
    #     store_single_dict(dict, file_name)
    #     time.sleep(1)

    lst = read_all_data("data_bak.json")
    print(len(lst))