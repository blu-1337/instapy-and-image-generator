from imgs import *  # gets all functions and their names
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui



message = \
    "Alwaysaa try to end the day with a positiveday with a positiveday with a positive thought. No matter how hard as df  asdfas dfas asdf a things are, tomorrow is a fresh opportunity to make everything better."

message2 = "When you say you suffer from a physical illness, you get sympathy. When you say you suffer from depression, you sometimes get blamed. We know it sucks, but at the very least, please take solace in the fact that you are not alone – as evidenced by the fact that 350 million people in the world struggle with depression."

message3 = 'asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf qwe qwer qwer qwer qwer qwer asdf asdf asdf qwer qwef qwef qwef asdf asdf qwef qwefq wef qwef asdf asdf qwef asdf awef awefa wef awef awef asdf asdf asd fasd fasdf asdf asdf '
message4 = 'Alwaysaa try to end the day with a positiveday with a positiveday with a positive thought. No matter how hard as df'
message5 = 'giochero per vincere niggas be niggas all the time no cap we strong brosefinos leggo my birtth light'
message25 = "Lorem ipsum dolor sit ame"
message50 = "Lorem ipsum dolor sit amet, consectetuer adipiscin"
message120 = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis nat"  # average quote size
message220 = 'Lorem ipsum dolor sit amet, consectetueradipiscing welit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies.'
message260 = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.'
message325 = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel'
message500 = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu'


# up to 260 incl. fontsize: 72, width 20
# up to 120 incl. fontsize: 72, width 16

# run program:

get_image_from_unsplash()
create_image_with_message(message50, 'post')
# create_image_with_message(message500, 'story')



# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.instagram.com/")
# time.sleep(5)
# my_email=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
# my_email.send_keys("------")
#
# my_password=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
# my_password.send_keys("-------")
# time.sleep(10)
#
# login=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
# login.click()
#
# time.sleep(5)
# upload=driver.find_element_by_xpath('//div[@class="QBdPU "]')
# upload.click()
# time.sleep(2)
# img_upload=driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]').click()
# time.sleep(2)
# path = "D:\Pictures\ph.png" # your imagepath
# pyautogui.write(path)
# time.sleep(2)
# pyautogui.press('enter')
