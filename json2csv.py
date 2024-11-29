import json
import csv

# 定义 JSON 文件路径
json_file_path = "docs/jsonDocs/englishDicts/WaiYanSheChuZhong_6.json"
csv_file_path = "WaiYanSheChuZhong_6.csv"

# 存储解析的 headWord 值
headwords = []

# 逐行读取 JSON 文件中的独立 JSON 对象
with open(json_file_path, "r", encoding="utf-8") as json_file:
    for line in json_file:
        line = line.strip()  # 去掉多余的空白和换行符
        if line:  # 跳过空行
            try:
                obj = json.loads(line)  # 解析单行 JSON
                if "headWord" in obj:
                    headwords.append(obj["headWord"])
            except json.JSONDecodeError as e:
                print(f"解析错误: {e}，行内容: {line}")

# 将结果写入 CSV 文件
with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["headWord"])  # 写入表头
    writer.writerows([[word] for word in headwords])  # 写入数据

print(f"已提取 {len(headwords)} 个 headWord 值，并保存到 '{csv_file_path}' 文件中。")
