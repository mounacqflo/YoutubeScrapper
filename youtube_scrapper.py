from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import re
import json
import argparse


class Scrapper:
    def __init__(self):
        service = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(service=service, chrome_options=options)
        
    # titre
    def getTitre(self):
        return self.soup.title.text

    # vidéaste
    def getVideaste(self):
        return self.soup.find("link", {"itemprop": "name"})['content']

    # pouces bleu
    def getPoucesBleu(self):
        res = ''
        pouces_bleu = self.soup.find("button", {"class": "yt-spec-button-shape-next yt-spec-button-shape-next--tonal yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-leading yt-spec-button-shape-next--segmented-start"})
        # re.findall takes in parameter a string containing int and return a table of these int -> ['17', '314']
        tab = re.findall(r'\d+', pouces_bleu['aria-label'])
        # concatenate tab elements
        for i in range(len(tab)):
            res += tab[i]
        return res

    # description
    def getDescription(self):
        # accept cookies at the launch of google chrome
        try: 
            self.driver.find_element(By.XPATH, "//*[@id=\"content\"]/div[2]/div[6]/div[1]/ytd-button-renderer[1]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]").click()
        except(NoSuchElementException):
            pass
        # click on "more" to display the entire description
        self.driver.find_element(By.XPATH, "//*[@id=\"expand\"]").click()
        # update soup data with the entire description
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        return soup.find("yt-formatted-string", {"class": "style-scope ytd-text-inline-expander"}).text

    # lien
    def getLiens(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        description = soup.find("yt-formatted-string", {"class": "style-scope ytd-text-inline-expander"})
        #print(description)
        links = []
        for a in description.find_all("a"):
            if a['href'][0] == '/':
                links.append("https://www.youtube.com"+a['href'])
            else:
                links.append(a['href'])
        return links

    # id
    def getId(self):
        return self.soup.find("meta", {"itemprop": "videoId"})['content']

    # commentaires
    def getComments(self, N):
        # execute a script to scroll to the comments
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.XPATH, "//*[@id=\"comments\"]"))

        comments = []
        while comments == []:
            time.sleep(1)
            # update soup data with the comments
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            comments = soup.find_all("ytd-comment-thread-renderer", {"class": "style-scope ytd-item-section-renderer"}, limit = N)

        commentsList = []
        for comment in comments:
            commentsList.append(comment.find("yt-formatted-string", {"id": "content-text"}).text)

        return commentsList

    def getDriverAndSoup(self, id):
        self.driver.get("https://www.youtube.com/watch?v="+id)
        time.sleep(1)
        self.soup = BeautifulSoup(self.driver.page_source, 'html.parser')

def main():
    parser = argparse.ArgumentParser(description='Input & Output json')
    parser.add_argument('--input', action='store')
    parser.add_argument('--output', action='store')

    args = parser.parse_args()
    with open(args.input) as input:
        inputs = json.load(input)
    
    videos = {"videos": []}
    for video_id in inputs['videos_id']:
        print(video_id)
        scrapper = Scrapper()
        scrapper.getDriverAndSoup(video_id)

        #driver.get("https://www.youtube.com/watch?v="+video_id)
        #time.sleep(1)

        #soup = BeautifulSoup(driver.page_source, 'html.parser')


        video = {}
        video["titre"] = scrapper.getTitre()
        video["videaste"] = scrapper.getVideaste()
        video["pouces_bleu"] = scrapper.getPoucesBleu()
        video["description"] = scrapper.getDescription()
        video["liens"] = scrapper.getLiens()
        video["id"] = scrapper.getId()
        video["commentaires"] = scrapper.getComments(10)

        videos['videos'].append(video)

        with open(args.output, 'w') as output:
            json.dump(videos, output, indent = 4)

    scrapper.driver.quit()
    
if __name__ =='__main__':
    main()