from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import cv2
import urllib.request
import numpy as np
import os

filename = 'keywords.csv'
imgcount = 10
imgcount = imgcount+3

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\User\AppData\Local\Google\Chrome\User Data")
driver = webdriver.Chrome(executable_path="chromedriver.exe",options=options)

def GetPhoto(url,path):
    try:
        try:
            os.mkdir('output') 
        except:
            print("Output Directory /output")
            
        driver.get(url)
        for i in range (2, imgcount):
            try:
                try:
                    os.mkdir('output/'+path)
                except:
                    print(path)
                item = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".islrc > .isv-r:nth-child("+str(i)+") .rg_i"))).click()
                imgurl=WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".KAlRDb"))).get_attribute("src")
                url_response = urllib.request.urlopen(imgurl)
                img = cv2.imdecode(np.array(bytearray(url_response.read()), dtype=np.uint8), -1)
                
                width = 800
                height = 800
                dim = (width, height)

                # resize image
                resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

                saveloc = 'output/'+path+'/'+str(i-1)+'img.png'
                cv2.imwrite(saveloc,resized)
            except:
                print("Can't get image")

        return

    except:
        print("Link Missing!")
        return
        

with open(filename, 'r') as keywordfile:
    datareader = csv.reader(keywordfile)
    try:
        for row in datareader:
            url="https://www.google.com/search?tbm=isch&q="+row[0]+" spare"
            path=row[0]
            foto = GetPhoto(url,path)
    except:
        print("Browser error")




driver.quit



