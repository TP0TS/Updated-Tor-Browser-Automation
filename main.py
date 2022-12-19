from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
from selenium import webdriver
import json,time,socket,subprocess
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('127.0.0.1',9050))
if result != 0:
    process = subprocess.Popen(["runfirst.exe"])
    print("opening tor circuit")
    time.sleep(5)

with open("settings.json") as settingsfile:
    settings = json.load(settingsfile)

waittime = settings["waitaftervisit"]
torpath = r'{}'.format(settings["firefoxexe"])
profilepath = r'{}'.format(settings["profilepath"])
driverpath=r'{}'.format(settings["geckodriverpath"])



while True:
    try:
        options=Options()
        options.set_preference('profile', profilepath)
        options.set_preference('network.proxy.type', 1)
        options.set_preference('network.proxy.socks', '127.0.0.1')
        options.set_preference('network.proxy.socks_port', 9050)
        options.set_preference("network.proxy.socks_remote_dns", False)
        options.set_preference( "javascript.enabled", True )
        options.set_preference( "permissions.default.image", 1 )

        options.binary_location = torpath

        service = Service(driverpath)
        driver = Firefox(options=options, service=service)

        driver.get("https://www.bing.com")

        wait = WebDriverWait(driver, 10)
        idlewait = WebDriverWait(driver, 50)

        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="sb_form_q"]')))
        yahoo = driver.find_element(By.XPATH,'//*[@id="sb_form_q"]')

        yahoo.send_keys("https://mawuv.com/")
        yahoo.send_keys(Keys.ENTER)

        wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Inspiration Station")))
        link = driver.find_element(By.LINK_TEXT,"Inspiration Station")
        link.click()

        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        idlewait.until(EC.presence_of_element_located((By.LINK_TEXT,"Best Car Insurance Companies In USA")))
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(30)
        driver.quit()

    except:
        try:
            driver.quit()
            pass
        except:
            pass