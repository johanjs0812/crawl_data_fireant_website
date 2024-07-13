from interactions.html_interactions import click_element, select_option
from helpers.format_data import clean_first_value
from data_processing.cv_to_table import convert_to_table_data
from interactions.parse import parse_page

def get_data(driver, time_out, limit_years, name_table):

    #Đặt tên đối tượng của bảng
    n_tb = clean_first_value(name_table)
    baocaotaichinh = {
        f"{n_tb}": {}
    }

    # Click chọn loại báo cáo tài chính
    tb_name = name_table
    xpath = "//button[contains(text(), '{}')]".format(tb_name)
    click_element(driver, xpath, time_out)

    check = parse_page(driver)

    if check:
        # Chọn giá trị từ select
        select_option(driver, "//select[@class='py-1 bg-transparent border-gray-300 rounded-lg dark:border-gray-700']", '1', time_out)
        
        # Gọi hàm lấy thông tin và chuyển sang dạng bảng
        return convert_to_table_data(driver, time_out, limit_years, baocaotaichinh)
    else:
        print("Không tìm thấy các thẻ th và td sau khi chờ đợi.")
        return {}

