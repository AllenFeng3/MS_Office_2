import csv


# 读取 CSV 文件并转换为列表
def csv_to_list(file_path):
    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


# 去除列表中重复的行
def remove_duplicates(data):
    unique_data = []
    seen = set()
    for row in data:
        row_tuple = tuple(row)  # 将行转换为元组以支持哈希
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_data.append(row)
    return unique_data


# 保存去重后的数据回 CSV 文件
def save_to_csv(file_path, data):
    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)  # 确保传递的是列表的列表


# 使用示例
file_path = 'docs/csvDocs/gaozhong.csv'  # 替换为你的 CSV 文件路径
output_file_path = 'docs/csvDocs/gaozhongoutput.csv'  # 输出文件路径

# 转换和去重
data_list = csv_to_list(file_path)
unique_data_list = remove_duplicates(data_list)
print(len(unique_data_list))

# 保存结果
save_to_csv(output_file_path, unique_data_list)

print(f"去重后的数据已保存到 {output_file_path}")
