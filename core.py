import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')
#driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=options)
#time.sleep(5) # Let the user actually see something!
#driver.get('https://supermercado.laanonimaonline.com/bebidas/n1_1/pag/2/')

#Get all the links grouped by subcategory
np.subsubcat=[]
subcat_items = soup.find_all("a", {'class': "link_05 bold"})
src_subcat=[link["href"]for link in subcat_items if "href" in link.attrs]
for urls in src_subcat:
    page = requests.get(urls)
    soup = BeautifulSoup(page.text, "html.parser")
    print(np.subsubcat.append(src_subcat))


    #Created all the lists I will need.
    np.title_product=[]
    np.price_before=[]
    np.price_promo=[]
    np.condition_text=[]

    #Got the info I needed and cleaned it.
    div_items = soup.find_all("div", {"class": "titulo02 aux1 titulo_puntos clearfix"})
    for div in div_items:
        title= (BeautifulSoup(str(div.find("a")),"lxml")).get_text()
        np.title_product.append(title)

    div_items = soup.find_all("div", {"class": "precio_complemento aux1"})
    for div in div_items:
        p_before= (BeautifulSoup(str(div.find(class_="precio anterior codigo")),"lxml")).get_text()
        p_promo= (BeautifulSoup(str(div.find(class_="precio semibold aux1")).replace(".",""),"lxml")).get_text()
        condition= (BeautifulSoup(str(div.find(class_="especial1")),"lxml")).get_text()
    #Stored the data 
        np.price_before.append(p_before)
        np.price_promo.append(p_promo)
        np.condition_text.append(condition)
    #All into one array
    array= np.vstack((np.title_product,np.price_before,np.price_promo,np.condition_text))
    #Created the df
    df = pd.DataFrame(
        data = array, 
        index = ["producto","precio_anterior","precio_promocional","condición"],
        columns= range(0,150),
        )

    print(df.transpose())
