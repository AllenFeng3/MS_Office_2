import time

import requests

# 目标 URL
# url = "https://www.bing.com/dict/search?q=welcome&FORM=BDVSP6&cc=cn"
url = "https://www.bing.com/dict/search?q=aftermath&FORM=BDVSP6&cc=cn"

# 设置请求头模拟浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

try:
    # 发送 HTTP GET 请求
    response = requests.get(url, headers=headers)

    # 检查 HTTP 请求是否成功
    if response.status_code == 200:
        # 保存 HTML 内容到文件
        with open("aftermath.html", "w", encoding="utf-8") as file:
            file.write(response.text)
        print("页面已成功保存为 welcome.html")
        time.sleep(0.5)
    else:
        print(f"请求失败，状态码：{response.status_code}")
except Exception as e:
    print(f"发生错误：{e}")
