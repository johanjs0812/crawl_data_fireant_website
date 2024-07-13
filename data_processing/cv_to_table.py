from interactions.parse import parse_page
from interactions.html_interactions import click_element, click_pagination
from helpers.format_data import convert_to_safe_name, clean_first_value

import pandas as pd

def convert_to_table_data(driver, time_out, limit_years, baocaotaichinh):

    Baocaotaichinh = baocaotaichinh

    found_desired_column = False
    all_dataframes = []

    while not found_desired_column:
        # Parse trang và lấy thông tin
        th_texts, td_texts, button_text = parse_page(driver)

        # Chia dữ liệu thành các hàng
        num_columns = len(th_texts)
        rows = [td_texts[i:i+num_columns] for i in range(0, len(td_texts), num_columns)]

        # Tạo DataFrame từ dữ liệu
        df = pd.DataFrame(rows, columns=th_texts)

        # Thêm DataFrame vào danh sách
        all_dataframes.append(df)

        # Kiểm tra nếu đã tìm thấy cột quý 1 của năm yêu cầu
        if limit_years in th_texts:
            found_desired_column = True
            break
        
        # Nếu không tìm thấy, tiếp tục click vào button pagination để chuyển sang trang tiếp theo
        clicked = click_pagination(driver, "//button[@class='inline-flex items-center justify-center text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:opacity-50 disabled:pointer-events-none ring-offset-background bg-primary text-primary-foreground hover:bg-primary/90 h-7 px-2 rounded-md mr-2']", time_out)
        
        # Nếu không click được (button bị disabled hoặc không tìm thấy), dừng vòng lặp
        if not clicked:
            print("Không thể click vào button pagination, dừng vòng lặp.")
            break

    final_df = pd.concat(all_dataframes, axis=1)
    final_df = final_df.loc[:, ~final_df.columns.duplicated()]

    # Loại bỏ cột có tên là ""
    if "" in final_df.columns:
        final_df.drop("", axis=1, inplace=True)

    # Thay đổi tên cột đầu tiên thành "name"
    if len(final_df.columns) > 0:
        final_df.columns.values[0] = 'name'

    # Thay đổi tên các cột còn lại
    final_df.columns = [convert_to_safe_name(col) for col in final_df.columns]

    # Chuyển đổi dữ liệu đầu tiên trong mỗi cột
    for col in final_df.columns:
        final_df[col] = final_df[col].apply(lambda x: clean_first_value(x) if isinstance(x, str) else x)

    # Tạo đối tượng dữ liệu
    for index, row in final_df.iterrows():
        data_object = {
            "name": row['name']
        }
        for col in final_df.columns[1:]: 
            data_object[col] = str(row[col])  # Chuyển đổi thành chuỗi
        Baocaotaichinh[row['name']] = data_object
    
    return Baocaotaichinh

