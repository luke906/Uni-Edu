import WebDriver_Class
import time
import os
import telegram
# from apscheduler.schedulers.background import BlockingScheduler
from bs4 import BeautifulSoup
bot = telegram.Bot(token='453642591:AAFwBdO7CaZ4XpfYi1ud3b6nURjYisHgs-s')

str_Chrome_Path = "./chromedriver"
str_Edu_URL = "https://www1.u-uniedu.com/"

id_list = []
password_list = []
browser_list = []

def get_person_info():

    global id_list
    global password_list
    global browser_list

    try:
        f = open("./ID_List.txt", 'r')
        read_line = f.readlines()

        for line in read_line:
            if len(line) > 0 and line != '\n':
                id_list.append(line.split('/')[0])
                password_list.append(line.split('/')[1])
                browser_list.append(line.split('/')[2].rstrip('\n'))

        f.close()

    except FileNotFoundError as e:
        print(str(e))


def get_account_count():
    return len(id_list)


def class_exam():

    global id_list, password_list, browser_list

    for start_index in range(0, get_account_count()):
        id = id_list[start_index]
        pw = password_list[start_index]
        Browser = WebDriver_Class.WebDriver(str_Chrome_Path)
        Browser.move_to_url(str_Edu_URL)
        Browser.send_key_by_name("inLoginID", id)
        Browser.send_key_by_name("inLoginPWD", pw)
        Browser.send_click_event('/html/body/div[2]/div/div[3]/div[3]/div[1]/form/div[2]/a/img')
        # Browser.execute_javascript("fnLogin();")

        for class_index in range(1, 7):
            start_time = time.time()
            Browser.execute_javascript("window.open('http://www1.u-uniedu.com/myClass/d_class.html?Chapter=" + str(class_index) + "&Page=1&CSIDX=" + browser_list[start_index] + "');")

            while True:
                if ( time.time()- start_time ) > 610:
                    break

        Browser.quit_browser()


if __name__   == "__main__":

    get_person_info()
    class_exam()




