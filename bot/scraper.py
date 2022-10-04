
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import requests

from bot.constants import BASE_URL_, houses_links


class Bot(webdriver.Chrome):
    
    count = 0

    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Bot, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def load_all_houses(self, url):
        self.get(url)
        self.scroll_page()

    def load_one_house(self, url):
        self.get(url)

    def search_Results_Grid(self):
        link = self.find_elements(By.CLASS_NAME, 'property-card__link')
        for item in link:
            link_data = item.get_attribute('href')
            houses_links.append(link_data)
            print(houses_links)
    
    def collect_house_info(self):
        
        for link in houses_links:
            self.load_one_house(link)
            images = self.find_elements(By.CSS_SELECTOR, 'source[media="(max-width: 1024px)"]')
            address = self.find_element(By.CLASS_NAME, 'listing-details__address')
            for iteration, img in enumerate(images):
                if iteration < 5:
                    image = img.get_attribute('srcset')
                    url = image
                    text = url.split('/')[-1]
                    filename = text.split('?')[0]
                    r = requests.get(url, allow_redirects=True)
                    open(filename, 'wb').write(r.content)
                    print(image)
                else:
                    break
            try:
                price = self.find_element(By.CLASS_NAME, 'listing-details__price')
                print(price.text)
            except:
                    print('No price attached')
            print(address.text)
            
        
           



    def scroll_page(self):
        time.sleep(3)
        previous_height = self.execute_script('return document.body.scrollHeight')

        while True:
            self.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
            new_height = self.execute_script('return document.body.scrollHeight')
            if new_height == previous_height:
                break
            else:
                self.search_Results_Grid()
            previous_height = new_height

    def click_about(self):
        about = self.find_element(By.XPATH, '//*[@id="tabsContent"]/tp-yt-paper-tab[6]')
        about.click()

    def got_to_sign_in(self):
        signin_link = self.find_element(By.XPATH, '//*[@id="details-container"]/table/tbody/tr[1]/td[2]/yt-formatted-string/a')
        signin_link.click()

    def enter_email_address(self):
        input = self.find_element(By.XPATH, '//*[@id="identifierId"]')
        input.clear()
        input.send_keys('reaganssebbaale@gmail.com')

    def proceed_To_Password(self):
        button = self.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
        button.click()

    def click_transcript_btn(self):
        showTranscript = self.find_element(By.CLASS_NAME, 'ytd-menu-popup-renderer')
        showTranscript.click()

    def get_transcript(self):
        transcript = self.find_elements(By.CSS_SELECTOR, 'yt-formatted-string[class="segment-text style-scope ytd-transcript-segment-renderer"]')
        for line in transcript:
            print(line.text)