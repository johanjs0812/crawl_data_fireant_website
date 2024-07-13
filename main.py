from config.connection import init_driver, open_url, close_url
from controllers.get_fin_statement import getInforBCTC
from data_processing.cv_to_json_file import convert_to_json2
from config.setting import TIME_OUT, FIREANT_URL, CACBANGCANLAY, VN30STOCK, LIMIT_YEARS

if __name__ == "__main__":

    for stock in VN30STOCK:

        url = f"{FIREANT_URL}{stock}"

        driver = init_driver()
        open_url(driver, url)

        final_df = getInforBCTC(driver, TIME_OUT, LIMIT_YEARS, CACBANGCANLAY, stock)
        convert_to_json2(final_df, stock)

        close_url(driver)

    print("VN30 DONE!!! JOHAN FPT")

