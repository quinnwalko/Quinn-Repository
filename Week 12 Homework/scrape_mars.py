from bs4 import BeautifulSoup
from splinter import browser
import pandas as pd 
import requests

def initialize_browser():
    executable_path = {"executable_path":  "/app/.chromedriver/bin/chromedriver"}
    return Browser("chrome", headless = True, **executable_path)

mars_information = {}

def scrape_mars_news():
    try:
        browser = initialize_browser()

        url = "https://mars.nasa.gov/news/"
        browser.visit(url)

        html = browser.html
        soup = bs(html, "html.parser")

        news_headline = soup.find("div", class_="content_title").find("a").text
        news_story = soup.find("div", class_="article_teaser_body").text

        mars_information["news_headline"] = news_headline
        mars_information["news_story"] = news_story

        return mars_information

    finally:
        browser.quit() 

def scrape_mars_image():
    try:
        browser = initialize_browser()

        url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(url_image)

        html_image = browser.html
        soup = bs(html_image, "html.parser")

        featured_image_url = soup.find("article")["style"].replace("background-image: url(","").replace(");", "")[1:-1]
        main_url = "https://www.jpl.nasa.gov"
        featured_image_url = main_url + featured_image_url
        featured_image_url
        mars_information["featured_image_url"] = featured_image_url

        return mars_information

    finally:
        browser.quit()

def scrape_mars_weather():
    try:
        browser = initialize_browser()
        
        weather_url = "https://twitter.com/marswxreport?lang=en"
        browser.visit(weather_url)

        html_weather = browser.html
        soup = bs(html_weather, "html.parser")

        recent_tweets = soup.find_all("div", class_="js-tweet-text-container")

        for tweet in recent_tweets:
            weather_tweet = tweet.find("p").text
            if "Sol" and "pressure" in weather_tweet:
                print(weather_tweet)
                break
            else:
                pass

        mars_information["weather_tweet"] = weather_tweet

        return mars_information

    finally:
        browser.quit()

def scrape_mars_facts():
    try:
        browser = initialize_browser

        facts_url = "https://space-facts.com/mars/"
        table = pd.read_html(facts_url)
        mars_facts_df = table[0]
        mars_facts_df.columns = ["Measurement", "Value"]
        mars_facts_df.set_index("Measurement", inplace = True)
        data = mars_facts_df.to_html()
        mars_information["table"] = data

        return mars_information

    finally:
        browser.quit()

