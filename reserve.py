import chrome_driver
from config import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from time import sleep

def main():

    # ドライバの準備
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.switch_to.frame('MainFrame')
    driver.implicitly_wait(10.0)

    for num in range(USER.shape[0]):
        user = USER.loc[num]
        print(log_in(driver, user.user_id, user.password))
        print(reserve(driver))
        print(log_out(driver))

def reserve(driver):

    wait_func()
    driver.find_element_by_partial_link_text(PURPOSE).click()
    wait_func()
    driver.find_element_by_partial_link_text('施設、時間帯を').click()
    wait_func()
    Select(driver.find_element_by_name('lst_kaikan')).select_by_visible_text(FACILITY)
    wait_func()

    for num in range(DATETIME.shape[0]):
        datetime = DATETIME.loc[num]

        disp_date = driver.find_element_by_class_name('clsCalTitleYM').text
        year_text = str(datetime.year) + '年'
        month_text = str(datetime.month) + '月'
        if year_text not in disp_date:
            wait_func()
            driver.find_element_by_link_text(year_text).click()
        if month_text not in disp_date:
            wait_func()
            driver.find_element_by_link_text(month_text).click()

        wait_func()
        driver.find_element_by_link_text(str(datetime.day)).click()
        wait_func()

        try:
            if driver.find_element_by_xpath("//img[@alt=\"抽選予約\"]").is_displayed():
                pass
        except:
            target = driver.find_element_by_name('ahref00000' + str(datetime.time_code) + '000')
            target_text = target.find_element_by_tag_name('img').get_attribute('alt')
            if target_text != '抽選予約画面へ移動':
                continue
            wait_func()
            driver.find_element_by_name('ahref00000' + str(datetime.time_code) + '000').click()
            wait_func()
            Alert(driver).accept()

        wait_func()
        target = driver.find_element_by_name('ahref00000' + str(datetime.time_code) + '000')
        target_text = target.find_element_by_tag_name('img').get_attribute('alt')
        if target_text != '抽選予約可能':
            continue
        wait_func()
        driver.find_element_by_name('ahref00000' + str(datetime.time_code) + '000').click()
        wait_func()

        win = driver.window_handles
        driver.switch_to.window(win[1])
        wait_func()
        Select(driver.find_element_by_name('men_1_1')).select_by_visible_text('1')
        wait_func()
        driver.find_elements_by_name('btn_modoru')[0].click()
        wait_func()
        driver.switch_to.window(win[0])
        driver.switch_to.frame(driver.find_elements_by_xpath("//frame")[0])
        wait_func()
        driver.find_element_by_name('btn_ok').click()
        wait_func()
        try:
            driver.find_element_by_name('btn_next').click()
        except:
            return 'アカウントが無効です。'
        wait_func()
        driver.find_element_by_name('btn_next').click()
        wait_func()
        driver.find_element_by_name('btn_cmd').click()
        wait_func()
        Alert(driver).accept()
        wait_func()
        driver.find_element_by_partial_link_text('施設、時間帯を').click()
        wait_func()
        Select(driver.find_element_by_name('lst_kaikan')).select_by_visible_text(FACILITY)

    return '予約完了'

def log_in(driver, user_id, password):
    driver.find_element_by_xpath("//input[@value='マイメニュー']").click()
    driver.find_element_by_name('txt_usr_cd').send_keys(user_id)
    driver.find_element_by_name('txt_pass').send_keys(password)
    wait_func()
    driver.find_element_by_name('btn_ok').click()
    wait_func()
    driver.find_element_by_name('btn_MoveMenu').click()
    return 'ID: {} でログイン完了'.format(user_id)

def log_out(driver):
    wait_func()
    driver.find_element_by_name('btn_LogOut').click()
    return 'ログアウト完了'

def wait_func(time=WAIT_TIME):
    sleep(time)
    return

if __name__ == '__main__':
    main()
