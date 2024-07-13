from interactions.html_interactions import click_element
from models.get_fin_statement import get_data
from helpers.format_data import clean_first_value

def getInforBCTC(driver, time_out, limit_years, cacbangcanlay, stock):

    # Click điều hướng đến khu vực báo cáo tài chính
    click_element(driver, "//button[contains(text(), 'Để sau')]", time_out)
    click_element(driver, "//li[contains(text(), 'Tài chính')]", time_out)
    click_element(driver, "//button[contains(text(), 'Báo cáo tài chính')]", time_out)

    company = {
        "symbol": f"{stock}",
        "bao_cao_tai_chinh": {}
    }

    for table in cacbangcanlay:
        name_table = clean_first_value(table)
        data = get_data(driver, time_out, limit_years, table)
    
        if name_table not in company["bao_cao_tai_chinh"]:
            company["bao_cao_tai_chinh"][name_table] = data
        else:
            company["bao_cao_tai_chinh"][name_table] = data

    return company






