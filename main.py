import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

def CoronaStats():

    # Webdriver path, please ensure:
    path = 'D:/Documents/chromedriver/chromedriver'
    url = 'https://www.worldometers.info/coronavirus/?'

    # In order to show the process:
    browser = webdriver.Chrome(path)
    browser.get(url)

    htmlText = requests.get(url).text
    soup = BeautifulSoup(htmlText, "lxml")

    print(soup)



    totalCasesWorld = soup.find(attrs={'class': 'total_row_body body_world'
                                       }).find(attrs={'class': 'total_row'
                                                      }).find_all('td')[2].getText()

    totalDeathsWorld = soup.find(attrs={'class': 'total_row_body body_world'
                                       }).find(attrs={'class': 'total_row'
                                                      }).find_all('td')[4].getText()

    totalRecoverWorld = soup.find(attrs={'class': 'total_row_body body_world'
                                       }).find(attrs={'class': 'total_row'
                                                      }).find_all('td')[6].getText()


    totalActiveWorld = soup.find(attrs={'class': 'total_row_body body_world'
                                       }).find(attrs={'class': 'total_row'
                                                      }).find_all('td')[8].getText()

    totalSeriousWorld = soup.find(attrs={'class': 'total_row_body body_world'
                                       }).find(attrs={'class': 'total_row'
                                                      }).find_all('td')[9].getText()

    print("Total CASES around the world: ", totalCasesWorld)
    print("Total DEATHS around the world: ", totalDeathsWorld)
    print("Total RECOVERS around the world: ", totalRecoverWorld)
    print("Total ACTIVE CASES around the world: ", totalActiveWorld)
    print("From them " + totalSeriousWorld + " in SERIOUS CONDITION")










    #print(soup)
    #print(soup)
    #print(soup)









CoronaStats()