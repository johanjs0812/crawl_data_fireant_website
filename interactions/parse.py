from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from config.setting import TIME_OUT

def parse_page(driver):
    try:
        # Chờ để đảm bảo trang đã tải hoàn toàn sau khi click
        WebDriverWait(driver, TIME_OUT).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, 'button'))
        )
        WebDriverWait(driver, TIME_OUT).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, 'th'))
        )
        WebDriverWait(driver, TIME_OUT).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, 'td'))
        )

        # Phân tích cú pháp HTML với BeautifulSoup từ mã nguồn trang web
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Tìm và lấy text từ tất cả các phần tử th, td, button
        button = soup.find('button', class_="inline-flex items-center justify-center text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:opacity-50 disabled:pointer-events-none ring-offset-background bg-primary text-primary-foreground hover:bg-primary/90 h-9 px-3 rounded-md")
        button_text = button.text.strip() if button else None

        th_elements = soup.find_all('th')
        th_texts = [th.text for th in th_elements]

        td_elements = soup.find_all('td')
        td_texts = [td.text for td in td_elements]

        return th_texts, td_texts, button_text

    except TimeoutException:
        print("Timeout waiting for elements to be present.")
        return False  # Trả về danh sách rỗng và None nếu có ngoại lệ TimeoutException
