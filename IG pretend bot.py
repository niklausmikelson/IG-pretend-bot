from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException

      
def check_exists_by_xpath(xpath):
    try:
        driver.find_element(by=By.XPATH, value=xpath)
    except NoSuchElementException:
        return False
    return True
def click_until_interactable(xpath):
    interactable=False
    while(not interactable):
        try:
            driver.find_element(by=By.XPATH, value=xpath).click()
            interactable=True
            
        except(ElementClickInterceptedException,ElementNotInteractableException,NoSuchElementException) as e:
            continue
def click_until_interactable_for_search(xpath):
    interactable=False
    z=0
    while(not interactable):
        try:
            driver.find_element(by=By.XPATH, value=xpath).click()
            interactable=True
            print("success")
        except(ElementClickInterceptedException,ElementNotInteractableException,NoSuchElementException) as e:
            driver.execute_script("window.scrollTo(0,"+str(z+500)+")")
            continue
def click_until_interactable_for_reload(xpath):
    interactable=False
    r=0
    while(not interactable):
        try:
            driver.find_element(by=By.XPATH, value=xpath).click()
            interactable=True
            
        except(ElementClickInterceptedException,ElementNotInteractableException,NoSuchElementException) as e:
            r=r+1
            print(r)
            if(r>20):
                driver.execute_script('location.reload()')
            continue
    
    
nlikes=108
username="your username"
pswd="your password"
PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com")
sleep(5)
driver.find_element(by=By.XPATH, value='//input[@type="text"]').send_keys(username)
driver.find_element(by=By.XPATH, value='//input[@name="password"]').send_keys(pswd)
sleep(1)
driver.find_element(by=By.XPATH, value='//button[@class="sqdOP  L3NKy   y3zKF     "]').click()

sleep(7)

searchTerm = ["#memes","#funny","#hilarious","#celebritygossip","#nft","#ecommerce","#animememes"]
searchTerm = searchTerm[random.randint(0,len(searchTerm)-1)]
#searching
driver.find_element(by=By.XPATH, value='//input[@class="XTCLo  d_djL  DljaH "]').send_keys(searchTerm)
sleep(4)
driver.find_element(by=By.XPATH, value='//div[@class="             qF0y9          Igw0E     IwRSH        YBx95     acqo5  vwCYk                                                                                                               "]').click()
sleep(8)

sleep(random.uniform(0.5,1))            
h=1
x=8+random.random()*5
x=int(x)


for k in range(3):
    for j in range(1,x):
        for i in range(1,4):
            sleep(random.uniform(1,1.5))
            if(check_exists_by_xpath('//div/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/article/div[2]/div/div['+str(j)+']/div['+str(i)+']/a/div[1]/div[2]')):
                click_until_interactable_for_search('//div/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/article/div[2]/div/div['+str(j)+']/div['+str(i)+']/a/div[1]/div[2]')
        
            sleep(random.uniform(1,3.5))
            #PRESSING THE LIKE BUTTON 
            if(random.random()>= 0.40):
                click_until_interactable_for_reload('//div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
            sleep(random.uniform(0.5,3))
            driver.find_element(by=By.XPATH, value='//div/div/div/div/div[2]/div/div/div[1]/div/div[2]/div').click()
        
    driver.find_element(by=By.XPATH, value='//div/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(Keys.CONTROL + "a")
    driver.find_element(by=By.XPATH, value='//div/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(Keys.DELETE)
    searchTerm = ["#memes","#funny","#hilarious","#celebritygossip","#nft","#ecommerce","#animememes"]
    searchTerm = searchTerm[random.randint(0,len(searchTerm)-1)]
    driver.find_element(by=By.XPATH, value='//div/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(searchTerm)
    sleep(5)
    driver.find_element(by=By.XPATH, value='//div/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click()
    sleep(7)