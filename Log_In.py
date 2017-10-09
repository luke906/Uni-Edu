import WebDriver_Class
import time
from bs4 import BeautifulSoup

str_Chrome_Path = "C:/Users/이성원/Selenium_Driver/chromedriver_win32/chromedriver"

# str_AirBitClub_Login_URL = "https://www.bitbackoffice.com/auth/login"
str_Edu_URL = "https://www2.u-uniedu.com/"
Wallet_Path = "https://www.bitbackoffice.com/wallets"


Browser1 = WebDriver_Class.WebDriver(str_Chrome_Path)
Browser1.move_to_url(str_Edu_URL)
Browser1.send_key_by_name("inLoginID", "newlife094")
Browser1.send_key_by_name("inLoginPWD", "9685")
Browser1.send_click_event('/html/body/div[2]/div/div[5]/div[3]/div[1]/form/div[2]/a/img')
for index in range(17, 25):
    Browser1.execute_javascript("window.open('http://www2.u-uniedu.com/myClass/d_class.html?Chapter=" + str(
        index) + "&Page=1&CSIDX=97457', 'new_window')")
    time.sleep(610)
driver = Browser1.return_browser()
driver.close()


Browser2 = WebDriver_Class.WebDriver(str_Chrome_Path)
Browser2.move_to_url(str_Edu_URL)
Browser2.send_key_by_name("inLoginID", "newlife103")
Browser2.send_key_by_name("inLoginPWD", "0024")
Browser2.send_click_event('/html/body/div[2]/div/div[5]/div[3]/div[1]/form/div[2]/a/img')
for index in range(17, 25):
    Browser2.execute_javascript("window.open('http://www2.u-uniedu.com/myClass/d_class.html?Chapter=" + str(
        index) + "&Page=1&CSIDX=97461', 'new_window')")
    time.sleep(610)
driver = Browser2.return_browser()
driver.close()

""""""
Browser3 = WebDriver_Class.WebDriver(str_Chrome_Path)
Browser3.move_to_url(str_Edu_URL)
Browser3.send_key_by_name("inLoginID", "newlife109")
Browser3.send_key_by_name("inLoginPWD", "7966")
Browser3.send_click_event('/html/body/div[2]/div/div[5]/div[3]/div[1]/form/div[2]/a/img')
for index in range(17, 25):
    Browser3.execute_javascript("window.open('http://www2.u-uniedu.com/myClass/d_class.html?Chapter=" + str(
        index) + "&Page=1&CSIDX=97464', 'new_window')")
    time.sleep(610)
driver = Browser3.return_browser()
driver.close()

""""""
Browser4 = WebDriver_Class.WebDriver(str_Chrome_Path)
Browser4.move_to_url(str_Edu_URL)
Browser4.send_key_by_name("inLoginID", "newlife158")
Browser4.send_key_by_name("inLoginPWD", "1788")
Browser4.send_click_event('/html/body/div[2]/div/div[5]/div[3]/div[1]/form/div[2]/a/img')
for index in range(17, 25):
    Browser4.execute_javascript("window.open('http://www2.u-uniedu.com/myClass/d_class.html?Chapter=" + str(
        index) + "&Page=1&CSIDX=97637', 'new_window')")
    time.sleep(610)
driver = Browser4.return_browser()
driver.close()

""""""
Browser5 = WebDriver_Class.WebDriver(str_Chrome_Path)
Browser5.move_to_url(str_Edu_URL)
Browser5.send_key_by_name("inLoginID", "newlife036")
Browser5.send_key_by_name("inLoginPWD", "3927")
Browser5.send_click_event('/html/body/div[2]/div/div[5]/div[3]/div[1]/form/div[2]/a/img')
for index in range(17, 25):
    Browser5.execute_javascript("window.open('http://www2.u-uniedu.com/myClass/d_class.html?Chapter=" + str(
        index) + "&Page=1&CSIDX=97425', 'new_window')")
    time.sleep(610)
driver = Browser5.return_browser()
driver.close()

""""""
Browser6 = WebDriver_Class.WebDriver(str_Chrome_Path)
Browser6.move_to_url(str_Edu_URL)
Browser6.send_key_by_name("inLoginID", "newlife159")
Browser6.send_key_by_name("inLoginPWD", "1220")
Browser6.send_click_event('/html/body/div[2]/div/div[5]/div[3]/div[1]/form/div[2]/a/img')
for index in range(13, 17):
    Browser6.execute_javascript("window.open('http://www2.u-uniedu.com/myClass/d_class.html?Chapter=" + str(
        index) + "&Page=1&CSIDX=97638', 'new_window')")
    time.sleep(610)
driver = Browser6.return_browser()
driver.close()



""""""
Browser7 = WebDriver_Class.WebDriver(str_Chrome_Path)
Browser7.move_to_url(str_Edu_URL)
Browser7.send_key_by_name("inLoginID", "newlife104")
Browser7.send_key_by_name("inLoginPWD", "3104")
Browser7.send_click_event('/html/body/div[2]/div/div[5]/div[3]/div[1]/form/div[2]/a/img')
for index in range(10, 17):
    Browser7.execute_javascript("window.open('http://www2.u-uniedu.com/myClass/d_class.html?Chapter=" + str(
        index) + "&Page=1&CSIDX=97462', 'new_window')")
    time.sleep(610)
driver = Browser7.return_browser()
driver.close()


""""""
Browser8 = WebDriver_Class.WebDriver(str_Chrome_Path)
Browser8.move_to_url(str_Edu_URL)
Browser8.send_key_by_name("inLoginID", "newlife037")
Browser8.send_key_by_name("inLoginPWD", "4763")
Browser8.send_click_event('/html/body/div[2]/div/div[5]/div[3]/div[1]/form/div[2]/a/img')
for index in range(10, 17):
    Browser8.execute_javascript("window.open('http://www2.u-uniedu.com/myClass/d_class.html?Chapter=" + str(
        index) + "&Page=1&CSIDX=97426', 'new_window')")
    time.sleep(610)
driver = Browser8.return_browser()
driver.close()


""""""
Browser9 = WebDriver_Class.WebDriver(str_Chrome_Path)
Browser9.move_to_url(str_Edu_URL)
Browser9.send_key_by_name("inLoginID", "newlife133")
Browser9.send_key_by_name("inLoginPWD", "1551")
Browser9.send_click_event('/html/body/div[2]/div/div[5]/div[3]/div[1]/form/div[2]/a/img')
for index in range(10, 17):
    Browser9.execute_javascript("window.open('http://www2.u-uniedu.com/myClass/d_class.html?Chapter=" + str(
        index) + "&Page=1&CSIDX=97471', 'new_window')")
    time.sleep(610)
driver = Browser9.return_browser()
driver.close()

""""""
Browser10 = WebDriver_Class.WebDriver(str_Chrome_Path)
Browser10.move_to_url(str_Edu_URL)
Browser10.send_key_by_name("inLoginID", "newlife156")
Browser10.send_key_by_name("inLoginPWD", "3731")
Browser10.send_click_event('/html/body/div[2]/div/div[5]/div[3]/div[1]/form/div[2]/a/img')
for index in range(10, 17):
    Browser10.execute_javascript("window.open('http://www2.u-uniedu.com/myClass/d_class.html?Chapter=" + str(
        index) + "&Page=1&CSIDX=97491', 'new_window')")
    time.sleep(610)
driver = Browser10.return_browser()
driver.close()


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
