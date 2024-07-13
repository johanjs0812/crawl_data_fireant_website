from selenium import webdriver

def init_driver():
    # Khởi tạo trình duyệt (chọn driver phù hợp trình duyệt)
    driver = webdriver.Chrome()
    return driver

def open_url(driver, url):
    # Mở URL
    driver.get(url)
    print('URL hiện tại:', driver.current_url)

def close_url(driver):
    # Đóng trình duyệt
    driver.quit()
    print('Đã đóng trình duyệt')
