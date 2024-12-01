import os
import pandas as pd
import pymysql


# 数据库连接配置
db_config = {
    "host": "localhost",  # 数据库主机地址
    "user": "root",  # 数据库用户名
    "password": "123456",  # 数据库密码
    "database": "hyd_tax_law"  # 替换为目标数据库名称
}

# 创建数据库连接
conn = pymysql.connect(**db_config)
cursor = conn.cursor()

# 创建 MySQL 表（如果不存在）
create_table_query = """
CREATE TABLE IF NOT EXISTS court_cases (
    序号 INT,
    案号 VARCHAR(255),
    案名 TEXT,
    承办庭室 VARCHAR(255),
    开庭地点 VARCHAR(255),
    开始时间 DATETIME,
    结束时间 DATETIME,
    法庭用途 VARCHAR(255)
);
"""
cursor.execute(create_table_query)

# 定义 Excel 文件夹路径
folder_path = "page1"  # 替换为包含多个 Excel 文件的文件夹路径

# 遍历文件夹中的所有 Excel 文件
for file_name in os.listdir(folder_path):
    if file_name.endswith(".xlsx") or file_name.endswith(".xls"):  # 仅处理 Excel 文件
        file_path = os.path.join(folder_path, file_name)

        # 读取 Excel 文件
        data = pd.read_excel(file_path)

        # 插入数据到 MySQL 表
        insert_query = """
        INSERT INTO court_cases (序号, 案号, 案名, 承办庭室, 开庭地点, 开始时间, 结束时间, 法庭用途)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        for _, row in data.iterrows():
            # 拆分开始时间和结束时间
            start_time, end_time = row["开始时间/结束时间"].split("/")
            cursor.execute(insert_query, (
                row["序号"], row["案号"], row["案名"], row["承办庭室"],
                row["开庭地点"], start_time, end_time, row["法庭用途"]
            ))

        print(f"已处理文件: {file_name}")
        conn.commit()

# 提交事务并关闭连接

cursor.close()
conn.close()

print("所有文件的数据已成功插入到 MySQL 数据库！")
