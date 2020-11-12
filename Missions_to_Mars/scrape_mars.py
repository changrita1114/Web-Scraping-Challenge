from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit NASA Mars News
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Retrieve the latest news
    results = soup.find_all('ul', class_='item_list')
    # loop over results to get article data
    for result in results:
        news_title = result.find('div', class_='content_title').text
        news_p = result.find('div', class_='article_teaser_body').text

    # Visit JPL Mars Space Images - Featured Image
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars#submit"
    url_2 = "https://www.jpl.nasa.gov/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Find the src for the featured image
    relative_image_path = soup.find_all('img', class_='thumb')[15]['src']
    featured_image_url = url_2 + relative_image_path

    # Visit Mars Facts page
    url = "https://space-facts.com/mars/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page using pandas
    tables = pd.read_html(url)
    mars_df = tables[2]
    mars_df.columns = ['Description', 'Mars']
    html_table = mars_df.to_html(index=False)
    html_table = html_table.replace('\n', '')

    # Visit Mars Hemispheres page
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    time.sleep(1)

    # Find the src for 4 images
    browser.find_by_text('Cerberus Hemisphere Enhanced').click()
    html = browser.html
    soup = bs(html, 'html.parser')
    fig_1 = soup.find_all('li')[0].a["href"]
    title_1 = soup.find('h2', class_="title").text

    # Visit page again
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    time.sleep(1)

    # Find the src for 4 images
    browser.find_by_text('Schiaparelli Hemisphere Enhanced').click()
    html = browser.html
    soup = bs(html, 'html.parser')
    fig_2 = soup.find_all('li')[0].a["href"]
    title_2 = soup.find('h2', class_="title").text

    # Visit page again
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    time.sleep(1)

    # Find the src for 4 images
    browser.find_by_text('Syrtis Major Hemisphere Enhanced').click()
    html = browser.html
    soup = bs(html, 'html.parser')
    fig_3 = soup.find_all('li')[0].a["href"]
    title_3 = soup.find('h2', class_="title").text

    # Visit page again
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    time.sleep(1)

    # Find the src for 4 images
    browser.find_by_text('Valles Marineris Hemisphere Enhanced').click()
    html = browser.html
    soup = bs(html, 'html.parser')
    fig_4 = soup.find_all('li')[0].a["href"]
    title_4 = soup.find('h2', class_="title").text

    # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "html_table": html_table,
        "fig_1": fig_1,
        "title_1": title_1,
        "fig_2": fig_2,
        "title_2": title_2,
        "fig_3": fig_3,
        "title_3": title_3,
        "fig_4": fig_4,
        "title_4": title_4
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
