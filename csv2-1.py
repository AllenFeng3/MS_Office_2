import pandas as pd

# 读取第一个CSV文件
file1 = "docs/csvDocs/01englishwords.csv"  # 第一个CSV文件的路径
file2 = "docs/csvDocs/z_toeflcet46.csv"  # 第二个CSV文件的路径
output_file = "filtered_file9.csv"  # 输出的CSV文件路径

# 假设CSV文件中每行是一个单词并且只有一列
# 读取第一个文件的单词列表
words1 = pd.read_csv(file1, header=None, names=["Word"])["Word"].tolist()

# 读取第二个文件
df2 = pd.read_csv(file2, header=None, names=["Word"])

# 从第二个文件中过滤掉在第一个文件中的单词
filtered_df = df2[~df2["Word"].isin(words1)]

# 保存过滤后的结果到新文件
filtered_df.to_csv(output_file, index=False, header=False)

print(f"过滤后的单词已保存到 {output_file}")
