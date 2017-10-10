import WebDriver_Class
import time
import os
import telegram

bot = telegram.Bot(token='453642591:AAFwBdO7CaZ4XpfYi1ud3b6nURjYisHgs-s')
from bs4 import BeautifulSoup

str_Chrome_Path = "C:/Users/이성원/Selenium_Driver/chromedriver_win32/chromedriver"

# str_AirBitClub_Login_URL = "https://www.bitbackoffice.com/auth/login"
str_Edu_URL = "https://www2.u-uniedu.com/"
Wallet_Path = "https://www.bitbackoffice.com/wallets"

str_complete_message = ""



Browser1 = WebDriver_Class.WebDriver(str_Chrome_Path)
Browser1.move_to_url(str_Edu_URL)
Browser1.send_key_by_name("inLoginID", "newlife094")
Browser1.send_key_by_name("inLoginPWD", "9685")
#Browser1.send_click_event('/html/body/div[2]/div/div[5]/div[3]/div[1]/form/div[2]/a/img')
Browser1.execute_javascript("fnLogin();")
for index in range(25, 33):
    Browser1.execute_javascript("window.open('http://www2.u-uniedu.com/myClass/d_class.html?Chapter=" + str(
        index) + "&Page=1&CSIDX=97457');")
    time.sleep(610)
    str_complete_message = "newlife094 Chapter" + str(index) + "Completed. (17~25)"
    #bot.sendMessage(chat_id='468017156', text=str_complete_message)
bot.sendMessage(chat_id='468017156', text="newlife094 Finished!")
Browser1.quit_browser()


Browser2 = WebDriver_Class.WebDriver(str_Chrome_Path)
Browser2.move_to_url(str_Edu_URL)
Browser2.send_key_by_name("inLoginID", "newlife103")
Browser2.send_key_by_name("inLoginPWD", "0024")
Browser2.execute_javascript("fnLogin();")
# Browser2.send_click_event('/html/body/div[2]/div/div[5]/div[3]/div[1]/form/div[2]/a/img')
for index in range(25, 33):
    Browser2.execute_javascript("window.open('http://www2.u-uniedu.com/myClass/d_class.html?Chapter=" + str(
        index) + "&Page=1&CSIDX=97461');")
    time.sleep(610)
    str_complete_message = "newlife103 Chapter" + str(index) + "Completed. (17~25)"
    bot.sendMessage(chat_id='468017156', text=str_complete_message)
bot.sendMessage(chat_id='468017156', text="newlife103 Finished!")
Browser2.quit_browser()

""""""
Browser3 = WebDriver_Class.WebDriver(str_Chrome_Path)
Browser3.move_to_url(str_Edu_URL)
Browser3.send_key_by_name("inLoginID", "newlife109")
Browser3.send_key_by_name("inLoginPWD", "7966")
Browser3.execute_javascript("fnLogin();")
# Browser3.send_click_event('/html/body/div[2]/div/div[5]/div[3]/div[1]/form/div[2]/a/img')
for index in range(25, 33):
    Browser3.execute_javascript("window.open('http://www2.u-uniedu.com/myClass/d_class.html?Chapter=" + str(
        index) + "&Page=1&CSIDX=97464');")
    time.sleep(610)
    str_complete_message = "newlife109 Chapter" + str(index) + "Completed. (17~25)"
    bot.sendMessage(chat_id='468017156', text=str_complete_message)
bot.sendMessage(chat_id='468017156', text="newlife109 Finished!")
Browser3.quit_browser()

""""""
Browser4 = WebDriver_Class.WebDriver(str_Chrome_Path)
Browser4.move_to_url(str_Edu_URL)
Browser4.send_key_by_name("inLoginID", "newlife158")
Browser4.send_key_by_name("inLoginPWD", "1788")
Browser4.execute_javascript("fnLogin();")
# Browser4.send_click_event('/html/body/div[2]/div/div[5]/div[3]/div[1]/form/div[2]/a/img')
for index in range(25, 33):
    Browser4.execute_javascript("window.open('http://www2.u-uniedu.com/myClass/d_class.html?Chapter=" + str(
        index) + "&Page=1&CSIDX=97637');")
    time.sleep(610)
    str_complete_message = "newlife158 Chapter" + str(index) + "Completed. (17~25)"
    bot.sendMessage(chat_id='468017156', text=str_complete_message)
bot.sendMessage(chat_id='468017156', text="newlife158 Finished!")
Browser4.quit_browser()



""""""
Browser5 = WebDriver_Class.WebDriver(str_Chrome_Path)
Browser5.move_to_url(str_Edu_URL)
Browser5.send_key_by_name("inLoginID", "newlife036")
Browser5.send_key_by_name("inLoginPWD", "3927")
Browser5.execute_javascript("fnLogin();")
#Browser5.send_click_event('/html/body/div[2]/div/div[4]/div[3]/div[1]/form/div[2]/a/img')
for index in range(25, 33):
    Browser5.execute_javascript("window.open('http://www2.u-uniedu.com/myClass/d_class.html?Chapter=" + str(
        index) + "&Page=1&CSIDX=97425');")
    time.sleep(610)
    str_complete_message = "newlife036 Chapter" + str(index) + "Completed. (17~25)"
    # bot.sendMessage(chat_id='468017156', text=str_complete_message)
bot.sendMessage(chat_id='468017156', text="newlife036 Finished!")
Browser5.quit_browser()

""""""
Browser6 = WebDriver_Class.WebDriver(str_Chrome_Path)
Browser6.move_to_url(str_Edu_URL)
Browser6.send_key_by_name("inLoginID", "newlife159")
Browser6.send_key_by_name("inLoginPWD", "1220")
Browser6.execute_javascript("fnLogin();")
#Browser6.send_click_event('/html/body/div[2]/div/div[5]/div[3]/div[1]/form/div[2]/a/img')
for index in range(17, 25):
    Browser6.execute_javascript("window.open('http://www2.u-uniedu.com/myClass/d_class.html?Chapter=" + str(
        index) + "&Page=1&CSIDX=97638');")
    time.sleep(610)
    str_complete_message = "newlife159 Chapter" + str(index) + "Completed. (13~17)"
    # bot.sendMessage(chat_id='468017156', text=str_complete_message)
bot.sendMessage(chat_id='468017156', text="newlife159 Finished!")
Browser6.quit_browser()


""""""
Browser7 = WebDriver_Class.WebDriver(str_Chrome_Path)
Browser7.move_to_url(str_Edu_URL)
Browser7.send_key_by_name("inLoginID", "newlife104")
Browser7.send_key_by_name("inLoginPWD", "3104")
Browser7.execute_javascript("fnLogin();")
#Browser7.send_click_event('/html/body/div[2]/div/div[5]/div[3]/div[1]/form/div[2]/a/img')
for index in range(17, 25):
    Browser7.execute_javascript("window.open('http://www2.u-uniedu.com/myClass/d_class.html?Chapter=" + str(
        index) + "&Page=1&CSIDX=97462');")
    time.sleep(610)
    str_complete_message = "newlife104 Chapter" + str(index) + "Completed. (10~17)"
    # bot.sendMessage(chat_id='468017156', text=str_complete_message)
bot.sendMessage(chat_id='468017156', text="newlife104 Finished!")
Browser7.quit_browser()


""""""
Browser8 = WebDriver_Class.WebDriver(str_Chrome_Path)
Browser8.move_to_url(str_Edu_URL)
Browser8.send_key_by_name("inLoginID", "newlife037")
Browser8.send_key_by_name("inLoginPWD", "4763")
Browser8.execute_javascript("fnLogin();")
#Browser8.send_click_event('/html/body/div[2]/div/div[5]/div[3]/div[1]/form/div[2]/a/img')
for index in range(17, 25):
    Browser8.execute_javascript("window.open('http://www2.u-uniedu.com/myClass/d_class.html?Chapter=" + str(
        index) + "&Page=1&CSIDX=97426');")
    time.sleep(610)
    str_complete_message = "newlife037 Chapter" + str(index) + "Completed. (10~17)"
    # bot.sendMessage(chat_id='468017156', text=str_complete_message)
bot.sendMessage(chat_id='468017156', text="newlife037 Finished!")
Browser8.quit_browser()

""""""
Browser9 = WebDriver_Class.WebDriver(str_Chrome_Path)
Browser9.move_to_url(str_Edu_URL)
Browser9.send_key_by_name("inLoginID", "newlife133")
Browser9.send_key_by_name("inLoginPWD", "1551")
Browser9.execute_javascript("fnLogin();")
#Browser9.send_click_event('/html/body/div[2]/div/div[5]/div[3]/div[1]/form/div[2]/a/img')
for index in range(17, 25):
    Browser9.execute_javascript("window.open('http://www2.u-uniedu.com/myClass/d_class.html?Chapter=" + str(
        index) + "&Page=1&CSIDX=97471');")
    time.sleep(610)
    str_complete_message = "newlife133 Chapter" + str(index) + "Completed. (10~17)"
    # bot.sendMessage(chat_id='468017156', text=str_complete_message)
bot.sendMessage(chat_id='468017156', text="newlife133 Finished!")
Browser9.quit_browser()

""""""
Browser10 = WebDriver_Class.WebDriver(str_Chrome_Path)
Browser10.move_to_url(str_Edu_URL)
Browser10.send_key_by_name("inLoginID", "newlife156")
Browser10.send_key_by_name("inLoginPWD", "3731")
Browser10.execute_javascript("fnLogin();")
#Browser10.send_click_event('/html/body/div[2]/div/div[5]/div[3]/div[1]/form/div[2]/a/img')
for index in range(17, 25):
    Browser10.execute_javascript("window.open('http://www2.u-uniedu.com/myClass/d_class.html?Chapter=" + str(
        index) + "&Page=1&CSIDX=97491');")
    time.sleep(610)
    str_complete_message = "newlife156 Chapter" + str(index) + "Completed. (10~17)"
    # bot.sendMessage(chat_id='468017156', text=str_complete_message)
bot.sendMessage(chat_id='468017156', text="newlife156 Finished!")
Browser10.quit_browser()


    # driver = Browser1.return_browser()
    # driver.switch_to.window(driver.window_handles[1])
    # driver.close()

# Browser1.send_key_by_name("user[username]", "lsw120300")
# Browser1.send_key_by_name("user[password]", "lsw8954!")
# Browser1.send_click_event('//*[@id="new_user"]/button')
# Browser1.move_to_url(Wallet_Path)





"""
wallet_html_source = Browser1.get_html_source()
soup = BeautifulSoup(wallet_html_source, 'html.parser')
print(soup.find_all('p', {'class':'result btc-container'}))
"""
