import WebDriver_Class
import time
import os
import telegram
from apscheduler.schedulers.background import BlockingScheduler

bot = telegram.Bot(token='453642591:AAFwBdO7CaZ4XpfYi1ud3b6nURjYisHgs-s')
from bs4 import BeautifulSoup

str_Chrome_Path = "./chromedriver"

# str_AirBitClub_Login_URL = "https://www.bitbackoffice.com/auth/login"
str_Edu_URL = "https://www1.u-uniedu.com/"

# http://www1.u-uniedu.com/myClass/d_class.html?Chapter=1&Page=1&CSIDX=101035

id_list = []
password_list = []
browser_list = []

start_index = 0
end_index = 3
login_flag = False
login_index = -1



scheduler = None

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

    global Browser
    global start_index
    global scheduler
    global login_flag, login_index
    global id_list, password_list

    start_index += 1

    if login_index == get_account_count():
        print("종료")
        scheduler.remove_job('browser1')
        return

    if login_flag == False:
        login_index += 1
        Browser = WebDriver_Class.WebDriver(str_Chrome_Path)
        Browser.move_to_url(str_Edu_URL)
        Browser.send_key_by_name("inLoginID", id_list[start_index])
        Browser.send_key_by_name("inLoginPWD", password_list[start_index])
        Browser.execute_javascript("fnLogin();")
        login_flag = True

    if start_index == end_index:
        login_flag = False
        Browser.quit_browser()
        return

    Browser.execute_javascript("window.open('http://www1.u-uniedu.com/myClass/d_class.html?Chapter=" + str(start_index) + "&Page=1&CSIDX=" + browser_list[login_index] + "');")

def kill_schedule(schedule, schedule_id):
    schedule.remove_job(schedule_id)

if __name__   == "__main__":

    get_person_info()

    scheduler = BlockingScheduler()
    scheduler.add_job(class_exam, 'interval', seconds=10, id='browser1')
    scheduler.start()


