import json


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
    file_name = "data.jsonl"

    # 存储数据
    # store_single_dict(data, file_name)


