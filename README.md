## Web-Scraping-Challenge
In this project, a web application that scrapes various websites for data related to the Mission to Mars was built and displays the information in a single HTML page. There were two main steps for building up this HTML page.
### Step 1 - Scraping
Scraping the necessary information from four different websites using Jupyter notebook, BeautifulSoup, Pandas, and Requests/Splinter. "mission_to_mars.ipynb" was created for completing all scraping and analysis tasks. Below are the fours websites that were scraped.
#### NASA Mars News: [NASA Mars News Site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest)
The latest news title and paragraph texts were scraped and collected. Assigned the text to variables which could be referenced later.
#### JPL Mars Space Images - Featured Image [NASA Jet Propulsion Laboratory](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)
Splinter was used to navigate the site and find the image url for the current featured Mars image and assigned the url string to a variable called "featured_image_url."
#### Mars Facts [SPACE FACTS](https://space-facts.com/mars/)
Pandas was used to scrape the table containing facts about the planet including diameter, mass, etc, and the table was converted to a HTML table string.
#### Mars Hemispheres [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
The four Mars hemispheres high resolution images were scraped from this site. A click function was used to find each full resolution image url. The urls and the names of the hemispheres were stored in a Pyhton dictionary.
### Step 2 - MongoDB and Flask Application
MongoDB with Flask templating was used to create a new HTML page that displays all of the information that was scraped from the URLs above.
* The scraping methods which were established in Jupyter notebook were converted into a Python script called "scrape_mars.py" with a function called scrape that will execute all of the scraping codes from above and return one Python dictionary containing all of the scraped data.
* A route called /scrape was created that will import "scrape_mars.py" script and call all the scrape functions. The returned values were stored in Mongo as a Python dictionary.
* A root route / was created that will query your Mongo database and pass the mars data into an HTML template to display the data.
* A template HTML file called index.html was created that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 
#### Mission to Mars Application Image
![alt app_image](https://github.com/changrita1114/Web-Scraping-Challenge/blob/main/Missions_to_Mars/app_screenshot.png?raw=true)

### Disclaimer
The resources of this master branch are only for educational purposes. All reserved rights belong to UCSD Data Science and Visualization Boot Camp.
