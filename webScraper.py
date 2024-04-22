from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import pandas as pd


class webScraper():
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.domain = urlparse(url).netloc.split(".")[-2]
        self.data = {'InnerLinks': [], 'OuterLinks': [],'Emails': [], 'Titles': [], 'Image Directory': []}

    def runAllFunctions(self):
        print("Scraper started.....")
        bot = self.driver
        bot.get(self.url)
        self.getLinks(bot)
        self.getImages(bot)
        self.getTitles(bot)
        self.getEmails(bot)
        bot.quit()
        print("Scraper stopped.....")

    def getLinks(self, bot):
        print("Getting links.....")

        links = bot.find_elements(By.TAG_NAME, "a")
        for link in links:
            href = link.get_attribute("href")
            
            if not href or "void" in href or "javascript" in href:
                continue
            if self.domain in href:
                self.data['InnerLinks'].append(href)
            else:
                self.data['OuterLinks'].append(href)
        
    def getImages(self, bot):
        print("Getting images.....")
        images = bot.find_elements(By.TAG_NAME,"img")
        os.makedirs(self.domain, exist_ok=True)
        image_directory = []
        for index, image in enumerate(images):
            src = image.get_attribute("src")
            if not src:
                continue
            
            response = requests.get(src)
            image_path = f"{self.domain}/image_{index}.jpg"
            with open(image_path, "wb") as file:
                file.write(response.content)
            image_directory.append(image_path)
            
        self.data['Image Directory'] = image_directory

    def getTitles(self, bot):
        print("Getting titles.....")
        titles = bot.find_elements(By.TAG_NAME,"h1")
        title_texts = [title.text for title in titles]
        
        self.data['Titles'] = title_texts
        
    def getEmails(self, bot):
        print("Getting emails.....")
        page_source = bot.page_source

        soup = BeautifulSoup(page_source, 'html.parser')

        email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        emails = email_pattern.findall(str(soup))
        
        self.data['Emails'] = emails

    def makeExcelSheet(self):
        print("Making excel sheet.....")
        data = self.data
        innerLinks = pd.Series(data["InnerLinks"], name="Inner Links")
        outerLinks = pd.Series(data["OuterLinks"], name="Outer Links")
        emails = pd.Series(data["Emails"], name="Emails")
        titles = pd.Series(data["Titles"], name="Titles")
        images = pd.Series(data["Image Directory"], name="Image Directory Path")
        df = pd.concat([titles, emails, innerLinks, outerLinks , images], axis=1)
        df.to_excel(f"{bot.domain}.xlsx", index=False)
        

url = "https://www.monolithai.com/blog/4-ways-ai-is-changing-the-packaging-industry"

bot = webScraper(url)
bot.runAllFunctions()
bot.makeExcelSheet()

