from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(options=chrome_options)

def login(usr, pw):
    driver.get("https://www.instagram.com/")
    sleep(1)
    driver.find_element_by_xpath("/html/body/div[3]/div/div/button[1]").click()
    sleep(2)
    driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(usr)
    driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
    driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div").click()
    sleep(4)
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    sleep(1)
    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    sleep(2)

def startLiking(x):
    #go to discover
    driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]/a").click()
    sleep(3)
    for j in range(1, x):
        for i in range(1, 4):
            # click on the first picture
            driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div[1]/div/div[{0}]/div[{1}]".format(j , i)).click()
            sleep(2)
            # like
            driver.find_element_by_xpath("//*[contains(@class,'wpO6b')]").click()
            # close
            driver.find_element_by_xpath("/html/body/div[4]/div[3]/button").click()
            sleep(1)
            print(i)

def scrivi(param):
    f = open("lista.txt", "r")
    lista = f.read()
    f.close()

    f = open("lista.txt", "w")
    lista = lista + (param + "\n")
    f.write(lista)
    f.close()

def addFollow(x):
    # go to discover
    driver.get("https://www.instagram.com/explore/")
    while(x > 0):

        sleep(3)
        #inizia il ciclo dei primi 24 (3*8)
        for j in range(1, 9):
            for i in range(1, 4):
                # click on the first picture
                driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div[1]/div/div[{0}]/div[{1}]".format(j , i)).click()
                sleep(2)
                #get the name
                name = driver.find_element_by_xpath("//div[contains(@class, 'e1e1d')]//a[contains(@class, 'sqdOP yWX7d     _8A5w5   ZIAjV ')]").text
                print(name)
                #write the name on the file
                scrivi(name)
                #follow
                driver.find_element_by_xpath("//div[contains(@class, 'bY2yH')]//button[contains(text(), 'Follow')]").click()
                # like
                driver.find_element_by_xpath("//*[contains(@class,'wpO6b')]").click()
                # close
                driver.find_element_by_xpath("/html/body/div[4]/div[3]/button").click()
                sleep(1)
        print(x)
        driver.refresh()
        x = x - 24


def leggi():
    f = open("lista.txt", "r")
    lista = f.read()
    return lista.splitlines()

def clear():
    f = open("lista.txt", "w")
    f.write("")
    f.close()

def remFollow():
    lista = leggi()
    for i in (lista):
        if (i != ""):
            driver.get("https://www.instagram.com/{}/".format(i))
            sleep(1)
            try:
                driver.find_element_by_xpath("//button[contains(text(), 'Following')]").click()
                #sleep(1)
                driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()
                sleep(1)
                #driver.close()
            except NoSuchElementException:
                pass
    clear()

def likeforlike(keyword, x):
    initial = x
    # look by keyword
    driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(keyword)
    sleep(2)
    # click the first element of the list
    driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]").click()
    while (x > 0):
        sleep(5)
        # start the cycle of the first 24 (3*8)
        for j in range(1, 9):
            for i in range(1, 4):
                # click on the first picture
                driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div/div[{0}]/div[{1}]".format(j, i)).click()
                sleep(1)
                # like
                driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button").click()
                # close
                driver.find_element_by_xpath("/html/body/div[5]/div[3]/button").click()
                sleep(1)
                x -= 1
                print(initial - x)
        driver.refresh()


login("username", "password")
#startLiking(3)

likeforlike("instadaily", 200)
#likeforlike("photography", 200)

#remFollow()
#addFollow(500)

