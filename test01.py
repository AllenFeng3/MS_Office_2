from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options


def save_html(url, keyword):
    # 设置 Edge 选项
    edge_options = Options()
    edge_options.use_chromium = True  # 使用 Chromium 内核
    edge_options.add_argument("--headless")  # 无头模式，不打开浏览器窗口
    edge_options.add_argument("--disable-gpu")  # 禁用GPU加速
    edge_options.add_argument("--disable-dev-shm-usage")  # 禁用/dev/shm使用
    edge_options.add_argument("--no-sandbox")  # 以最高权限运行
    edge_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36")  # 设置用户代理

    # 初始化 Edge 浏览器
    edge_service = Service("msedgedriver.exe")  # 请将驱动程序路径替换为实际路径
    edge_driver = webdriver.Edge(service=edge_service, options=edge_options)

    # 打开网页
    edge_driver.get(url)

    # 获取页面源码
    html_content = edge_driver.page_source

    # 关闭浏览器
    edge_driver.quit()

    # 保存源码到文件
    filename = f"{keyword}.html"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(html_content)
    print(f"源码已保存至 {filename}")


def main():
    keyword = "abandon"
    url = f"https://www.bing.com/dict/search?q={keyword}"
    save_html(url, keyword)


if __name__ == "__main__":
    main()
