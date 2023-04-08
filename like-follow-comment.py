# Instagram limitations:

# follow/unfollow
# Follow/unfollow per day limit: 200
# 10 follows/unfollows per hour keep account safe

# likes
# likes limit per day: 1000
# keep account safe with 700 likes per day
# 30-35 per hour

# comments
# 180 to 200 comments per day
# 8-10 per hour


# from imgs import *  # gets all functions and their names
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# import pyautogui
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
from datetime import date
from random import choice
from selenium.webdriver.firefox.options import Options
import json


def read_password_file(filepath):
    """
    Read and return the user/password file.
    """
    try:
        with open(filepath, 'r') as fd:
            lines = fd.readlines()
            fd.close()
            return lines
    except IOError:
        raise ValueError("Can't open password file for reading.")

def check_for_popups():
    try:
        login_button = driver.find_element(By.XPATH, '//button[text()="Log in"]')
        login_button.click()
        sleep(1)
        return print('found login button')
    except: print("No 'do not dw app click on login found'")
    try:
        # add instagram to your home screen, cancel
        button = driver.find_element(By.XPATH, '//button[text()="Cancel"]')
        button.click()
        sleep(1)
        return print('found cancel button')
    except: print("No 'add instagram to your home screen, cancel' button found'")
    try:
        # do not save login info, click on not now
        button = driver.find_element(By.XPATH, '//button[text()="Not Now"]')
        button.click()
        sleep(1)
        return print('found not now button')
    except: print("No 'do not save login info, click on not now' button found'")
    try:
        button = driver.find_element(By.XPATH, '//button[text()="Allow essential and optional cookies"]')
        button.click()
        sleep(1)
        return print('found allow essential and optional cookies button')
    except: print("No essential cookies popup button found.")
    print("Popup check finished, no recognizable popup currently on the screen.")

def login():
    check_for_popups()

    my_email=driver.find_element(By.XPATH, '//input[@name="username"]')
    my_email.send_keys("motivation_blu")

    my_password=driver.find_element(By.XPATH, '//input[@name="password"]')
    my_password.send_keys(read_password_file('./.pass'))
    sleep(2)

    login=driver.find_element(By.XPATH, '//div[text()="Log in"]')
    login.click()

    sleep(3)

    check_for_popups()

# fetch comment from txt file and add heart at the end
def fetch_random_comment():
    lines = open('quotes_original_full.txt').read().splitlines()
    return choice(lines) + " 💙"


def fetch_posts(loop_length):  # loop length is how many pages it should scroll down
    def fetching_loop(loop_length):
        while loop_length > 0:
            driver.execute_script(
                'window.scrollTo(0, document.documentElement.scrollHeight)')
            sleep(2)
            loop_length -= 1
    fetching_loop(loop_length)
    
    # get list of posts
    posts_list = driver.find_elements(By.CSS_SELECTOR, 'a')
    # print(posts_list)

    posts_list_filtered = []
    for element in posts_list:
    #     print(element.get_attribute("href"))
        elem = element.get_attribute("href")

        if "/p/" in elem:
            posts_list_filtered.append(elem)
    print("fetched: ", len(posts_list_filtered), "videos")
    return posts_list_filtered

def leave_comment(message):
    try: textbox = driver.find_element(By.XPATH, '//textarea[@placeholder="Add a comment…"]')
    except: 
        print("Error: Comment section not found.")
        return False
        
    # check if comment is duplicate
    all_comments = driver.find_element(By.XPATH, '//div[@role="presentation"]').get_attribute('innerHTML')
    if all_comments.count("motivation_blu") > 0:
        print("Error: Duplicate comment found.")
        return False
    
    textbox.send_keys(message)
    sleep(1)
    post_button = driver.find_element(By.XPATH, '//div[text()="Post"]')
    post_button.click()
    sleep(5)
    return True  # this returns if the function was successful
    
def like_post():
    try: post_div = driver.find_element(By.XPATH, '//div[@role="button"]')
    except: 
        print("FATAL ERROR: like button not found! Check if this is a normal page.")
        return False
    actionChains = ActionChains(driver)
    actionChains.double_click(post_div).perform()    
    sleep(3)
    return True
    
def follow_user():
    try: 
        follow_button = driver.find_element(By.XPATH, '//div[text()="Follow"]')
        follow_button.click()
    except: 
        print("Error: Follow button not found or already following...")
        return False
    # add user to status.json 
    sleep(3)
    
    return True  # this returns if the function was successful
    
def unfollow_user():  # you have to be on user's post page, it also unfollwos from main profile page
    follow_button = driver.find_element(By.XPATH, '//div[text()="Following"]')
    follow_button.click()
    sleep(3)
    try: 
        unfollow_button = driver.find_element(By.XPATH, '//button[text()="Unfollow"]')  # for post
        unfollow_button.click()  
        return
    except: 
        print('no unfollow button found, trying with unfollow div...')
    try:
        unfollow_button = driver.find_element(By.XPATH, '//div[text()="Unfollow"]')  # for main profile page
        unfollow_button.click()   
        return
    except Exception as e:
        print('no unfollow div found, this is bad!', e)
        

        



presets = [
    {
        "key": "480x800",
        "name": "Google Nexus one",
        "width": 480,
        "height": 800
    },

    # TO FILL

    {
        "key": "1680x1050",
        "name": "Desktop - stat 2.96%",
        "width": 1680,
        "height": 1050
    }
]




# driver = webdriver.Firefox(profile)


# driver.get('http://google.com/')


# binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox')
# driver = webdriver.Firefox()





from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
import random, psutil, shutil, os, time


# can be a new folder
profile_path = r"C:\Users\blu\AppData\Roaming\Mozilla\Firefox\Profiles\stschfau.default-release"

# if not os.path.isdir(profile_path):
# 	os.mkdir(profile_path)


firefox_profile = webdriver.FirefoxProfile(profile_path)
options = Options()

options.profile = firefox_profile
firefox_profile.set_preference('devtools.responsiveUI.presets', json.dumps(presets))


options.profile.set_preference('signon.autologin.proxy', True)
options.profile.set_preference('signon.autologin.username', 'motivation_blu')
options.profile.set_preference('signon.autologin.password', 'Www.mafia.com8')
options.profile.set_preference('browser.sessionstore.interval', 10)
options.profile.set_preference('browser.sessionstore.resume_from_crash', True)
options.profile.set_preference('browser.sessionstore.max_tabs_undo', 5)
options.profile.set_preference('browser.sessionstore.max_windows_undo', 5)
options.profile.set_preference('browser.sessionstore.privacy_level', 2)

# # Launch Firefox with the profile that has your login credentials
# driver = webdriver.Firefox(firefox_profile=profile)

options.binary_location = r'C:\\Program Files\\Mozilla Firefox\\firefox.exe'

# add a random thing so we can distinguish the firefox process
# distinguishkey = "-persistentprofileworkaround"+str(random.randint(111111,999999))

# options.add_argument(distinguishkey)


# print("gistinguish_key is: ", distinguishkey)

driver = webdriver.Firefox(firefox_profile, options=options, executable_path="geckodriver")





# do web stuff here


# driver.minimize_window()
# driver.maximize_window()
driver.get("https://www.instagram.com/")
sleep(3)

check_for_popups()


try:
    login()
except Exception as e:
    print('We had the following problem: ', e)


    
check_for_popups()

sleep(5)

check_for_popups()

sleep(5)

check_for_popups()

#1 goto https://www.instagram.com/explore/tags/motivational/ you can also make this a list that gets a random tag



# leave a comment function




hashtag_list = [
    'https://www.instagram.com/explore/tags/motivationalquotes/',
    'https://www.instagram.com/explore/tags/motivation/',
    'https://www.instagram.com/explore/tags/motivational/',
    'https://www.instagram.com/explore/tags/quotes/',
    'https://www.instagram.com/explore/tags/quote/',
    'https://www.instagram.com/explore/tags/follow/',
    'https://www.instagram.com/explore/tags/like/',
    'https://www.instagram.com/explore/tags/inspirationalquotes/',
    'https://www.instagram.com/explore/tags/love/',
    'https://www.instagram.com/explore/tags/live/',
    'https://www.instagram.com/explore/tags/life/',
    'https://www.instagram.com/explore/tags/lifestyle/',
    'https://www.instagram.com/explore/tags/instagood/',
    'https://www.instagram.com/explore/tags/success/',
    'https://www.instagram.com/explore/tags/workout/',
    'https://www.instagram.com/explore/tags/gym/',
    'https://www.instagram.com/explore/tags/goals/',
    'https://www.instagram.com/explore/tags/mindset/',
    'https://www.instagram.com/explore/tags/positivevibes/',
    'https://www.instagram.com/explore/tags/follow/',
    'https://www.instagram.com/explore/tags/fitness/',
    'https://www.instagram.com/explore/tags/happiness/',
    'https://www.instagram.com/explore/tags/entrepreneur/',
    'https://www.instagram.com/explore/tags/believe/',
    'https://www.instagram.com/explore/tags/fitness/',
    'https://www.instagram.com/explore/tags/loveyourself/',
    'https://www.instagram.com/explore/tags/business/',
    'https://www.instagram.com/explore/tags/lifequotes/',
    'https://www.instagram.com/explore/tags/sale/',
    'https://www.instagram.com/explore/tags/fashion/',
    'https://www.instagram.com/explore/tags/forsale/',
    'https://www.instagram.com/explore/tags/acution/',
    'https://www.instagram.com/explore/tags/giveaway/',
    'https://www.instagram.com/explore/tags/hip-hop/',
    'https://www.instagram.com/explore/tags/producer/',
    'https://www.instagram.com/explore/tags/followme/',
    'https://www.instagram.com/explore/tags/nature/',
    'https://www.instagram.com/explore/tags/happy/',
    'https://www.instagram.com/explore/tags/like4like/',
    'https://www.instagram.com/explore/tags/cute/',
    'https://www.instagram.com/explore/tags/picoftheday/',
    'https://www.instagram.com/explore/tags/travel/',
    'https://www.instagram.com/explore/tags/photooftheday/',
    'https://www.instagram.com/explore/tags/instagram/',
    'https://www.instagram.com/explore/tags/style/',
    'https://www.instagram.com/explore/tags/summer/',
    'https://www.instagram.com/explore/tags/vibe/',
    'https://www.instagram.com/explore/tags/music/',
    'https://www.instagram.com/explore/tags/freebies/',
    'https://www.instagram.com/explore/tags/vibes/',
    'https://www.instagram.com/explore/tags/instamood/',
    'https://www.instagram.com/explore/tags/success/',
    'https://www.instagram.com/explore/tags/onlineshop/',
    'https://www.instagram.com/explore/tags/marketing/',
    'https://www.instagram.com/explore/tags/retail/',
    'https://www.instagram.com/explore/tags/ecommerce/',
    'https://www.instagram.com/explore/tags/startups/',
    'https://www.instagram.com/explore/tags/management/',
    'https://www.instagram.com/explore/tags/selfcare/',
    'https://www.instagram.com/explore/tags/smile/',
    'https://www.instagram.com/explore/tags/beautiful/']

random_hashtag = randint(0, len(hashtag_list))

driver.get(hashtag_list[random_hashtag])
hashtag_list.pop(0)

posts = fetch_posts(5)


#best settings
# to_follow = randint(8,11)
# to_comment = randint(8, 11)
# to_like = randint(30, 36)

to_follow = randint(1,5)
to_comment = randint(1, 5)
to_like = randint(1, 10)



# to_follow, to_comment, to_like = 0, 0, 0

follow_counter, like_counter, comment_counter, posts_counter = 0, 0, 0, 0

while True:
    if posts_counter == len(posts):  # check if post counter reaches maximum length of available post for that hashtag
        # go to next hashtag
        driver.get(hashtag_list[0])
        hashtag_list.pop(0)
        posts = fetch_posts(5)
        driver.get(posts[0])
        posts_counter = 0
        sleep(5)  # wait for new page to load
    if follow_counter == to_follow and like_counter == to_like and comment_counter == to_comment:
        print("We reached limit for all: comment, like and follow.")
        break
        
    driver.get(posts[posts_counter])
    sleep(5)
    
    if follow_counter < to_follow:
        if follow_user():
            follow_counter += 1
            print("Followed this user.")
        else:
            print("Followed counter did not increase")
    else: 
        print("We reached follow limit for now.")
    
    if like_counter < to_like:
        if like_post():
            like_counter += 1
            print("Liked this post.")
        else:
            print("Like counter did not increase.")
    else:
        print("We reached like limit for now.")
    if comment_counter < to_comment:
        if leave_comment(fetch_random_comment()):
            comment_counter += 1
        else: print("Comment counter did not increase.")
    else:
        print("We reached comment limit for now.")
        
    posts_counter += 1

    
    print(f"Counters: {like_counter}/{to_like} likes given, {comment_counter}/{to_comment} comments posted, {follow_counter}/{to_follow} followed")
    print(f"We have {posts_counter}/{len(posts)}")
        


print("Closing web driver...")
driver.close()








#driver.get("http://localhost/cookie.php")
#time.sleep(1)
#driver.get("http://localhost/cookie.php")
#time.sleep(1)
#driver.get("http://localhost/cookie.php")



# for pid in psutil.pids():
#     try:
#         cmdline = open("/proc/"+str(pid)+"/cmdline", "r").read()
#         print("_____________________")
#         print(cmdline)
#         if distinguishkey in cmdline:
#             profile = cmdline.split('-profile')[1].split(' ')[0].replace('\x00', '')
#             break
#     except:
#         pass

# psutil.Process(pid).kill() # kill firefox (nicely) and unlock profile lock
# if os.path.isdir(profile_path):
# 	shutil.rmtree(profile_path)
# shutil.copytree(profile, profile_path, symlinks=True) # copy the new profile to profile_path, don't resolve "lock" symlink

try:
  driver.quit() # will throw an error because we killed firefox
except:
  pass

# # cleanup
# if os.path.isdir(profile):
# 	shutil.rmtree(profile)
# if os.path.isdir(driver.profile.tempfolder):
# 	shutil.rmtree(driver.profile.tempfolder)