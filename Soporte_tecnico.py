from typing import Sized
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, TimeoutException
from datetime import date
from datetime import datetime
import time
import keyword
import keyboard
import os
import shutil
from tkinter import messagebox
import pandas as pd
import telegram

options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_experimental_option("prefs",{
#   "download.default_directory" : "C:/Users/asalvador/Desktop/Automatización/Descargas",
    "download.default_directory" : "C:\Bim\Llamadas",})

driver = webdriver.Chrome("C:/Users/asalvador/Desktop/Automatización/chromedriver.exe",chrome_options=options)

folder = r"C:\Bim\Llamadas"
folder2 = r"C:\Bim\Productividad"
folder3 = r"C:\Bim\Tickets"

#Limpiar Carpeta llamadas
for the_file in os.listdir(folder):
    file_path = os.path.join(folder,the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #Elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)

#Limpiar Carpeta Productividad
for the_file in os.listdir(folder2):
    file_path = os.path.join(folder2,the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #Elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)

#Limpiar Carpeta Tickets
for the_file in os.listdir(folder3):
    file_path = os.path.join(folder3,the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #Elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)
