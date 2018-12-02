import os
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def scrape():

    mars_filepath = os.path.join("News_NASA_Mars_Exploration_Program.html")
    nasa_mars_html = open(mars_filepath, "r").read()


    soup = bs(nasa_mars_html, 'html.parser')

    news_headlines = soup.find('li',class_="slide").find('div',class_="content_title").text
    news_paragraph = soup.find('li',class_="slide").find('div',class_="article_teaser_body").text



    featured_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    response = requests.get(featured_image_url)
    soup = bs(response.text, 'html.parser')
    image = soup.find(class_="button fancybox")["data-fancybox-href"]
    featured_image_url = "https://www.jpl.nasa.gov/" + image
    featured_image_url

    mars_weather_twitter_url = 'https://twitter.com/marswxreport?lang=en'
    response = requests.get(mars_weather_twitter_url)
    soup = bs(response.text, 'html.parser')
    mars_weather_tweets = soup.find_all('p', class_='TweetTextSize')


    mars_facts_url = 'https://space-facts.com/mars/'
    mars_facts = pd.read_html(mars_facts_url)[0]
    mars_facts.columns = ['Fact', 'Characteristic']
    mars_facts_html = mars_facts.to_html()



mars_dictionary = {"news headline": news_headlines,
                   "news paragraph": news_paragraph,
                   "featured image url": featured_image_url,
                   "mars weather twitter": mars_weather_tweets,
                   "mars facts": mars_facts_html


}

return mars_dictionary
