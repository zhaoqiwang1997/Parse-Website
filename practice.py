# use undetected chrome driver against CloudFlare/ Distil
import time
from selenium.webdriver import ChromeOptions
import undetected_chromedriver as uc
import csv


## test if the chrome checking exsits:  window.navigator.webdriver
option = ChromeOptions()
# option.add_argument("--disable-blink-features=AutomationControlled")
# #
# # # get rid of "Chrome is being controlled bt automated testing software"
# # option.add_experimental_option("useAutomationExtension", False)
# # option.add_experimental_option("excludeSwitches",["enable-automation"])
# #
# # # get rid of the info bar popping up
# # option.add_argument('--disable-infobars')
#
# # incognito mode
# # option.add_argument("--incognito")

# open the website with Chrome
driver = uc.Chrome(options= option)
# driver = webdriver.Chrome("/Users/wangzhaoqi/Downloads/chromedriver",options= option)

driver.get("https://socialblade.com")



# find element and click, it will return a list
btn = driver.find_elements_by_link_text("Login")
btn[0].click()

# Locate the writing box. Fill the username and password.
btn_username = driver.find_element_by_name("dashboard_email")
btn_username.send_keys("hanjiang219@gmail.com")
time.sleep(5)

btn_password = driver.find_element_by_name("dashboard_password")
btn_password.send_keys("bigfloppaislife")
time.sleep(5)

# click login button
btn_login = driver.find_element_by_class_name("core-button")
btn_login.click()
time.sleep(5)

# select channel through selector locating. It returns the web.
btn_channel = driver.find_element_by_class_name("dd-selected-text")
btn_channel.click()
time.sleep(5)

btn_instgram = driver.find_element_by_css_selector("#search-special > ul > li:nth-child(4) > a > label")
btn_instgram.click()
time.sleep(5)

# Locate and fill the search input
btn_search = driver.find_element_by_id("SearchInput")
btn_search.send_keys("nft.mentor")
time.sleep(5)

# Locate and click search button
btn_search_button = driver.find_element_by_css_selector("#topSearchForm > div:nth-child(1) > button > i")
btn_search_button.click()
time.sleep(15)

# get followers
def followers_collector(followers, path, loop):
    for i in range(1, loop+1):
        new_path = path
        new_path_complete = new_path[:62] + str(i) + new_path[63:]
        followers.append(driver.find_element_by_css_selector(new_path_complete).text)

followers = []

followers_collector(followers, "#socialblade-user-content > div:nth-child(11) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span", 14)

followers.append(driver.find_element_by_css_selector("#socialblade-user-content > div:nth-child(12) > div:nth-child(2) > span").text)
followers.append(driver.find_element_by_css_selector("#socialblade-user-content > div:nth-child(13) > div:nth-child(2) > span").text)

print(followers)

time.sleep(15)

# get date
def date_collector(dates, path, loop):
    for i in range(1, loop+1):
        new_path = path
        new_path_complete = new_path[:62] + str(i) + new_path[63:]
        dates.append(driver.find_element_by_css_selector(new_path_complete).text)

dates = []

date_collector(dates, "#socialblade-user-content > div:nth-child(11) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)", 14)

dates.append(driver.find_element_by_css_selector("#socialblade-user-content > div:nth-child(12) > div:nth-child(1)").text)
dates.append(driver.find_element_by_css_selector("#socialblade-user-content > div:nth-child(13) > div:nth-child(1)").text)

print(dates)

time.sleep(15)

# get day of week
def day_collector(dates, path, loop):
    for i in range(1, loop+1):
        new_path = path
        new_path_complete = new_path[:62] + str(i) + new_path[63:]
        days.append(driver.find_element_by_css_selector(new_path_complete).text)

days = []

day_collector(days, "#socialblade-user-content > div:nth-child(11) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2)", 14)
days.append("")
days.append("")
print(days)

time.sleep(15)

# write csv
header = ["Date", "Day of week", "followers"]
data = []
for i in range(0, len(followers)):
    row_data = []
    row_data.append(dates[i])
    row_data.append(days[i])
    row_data.append(followers[i])
    data.append(row_data)

#use it when the csv not exists
file_path = "/Users/wangzhaoqi/Desktop/Practice/nft.csv"
with open(file_path, "w", encoding="UTF8", newline="") as f:
    writer = csv.writer(f)

    # header
    writer.writerow(header)

    # multiple rows
    writer.writerows(data)

    f.close()

# use it when the csv exists already
# with open("file_path, "a", encoding="UTF8", newline="") as f:
#     writer = csv.writer(f)
#
#     # header
#     # writer.writerow(header)
#
#     # multiple rows
#     writer.writerows(data)
#
#     f.close()