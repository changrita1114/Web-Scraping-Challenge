## Web-Scraping-Challenge
In this project, a web application that scrapes various websites for data related to the Mission to Mars was built and displays the information in a single HTML page. There were two main steps for building up this HTML page.
<br>
### Step 1 - Scraping
Scraping the necessary from four different websites using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter. "mission_to_mars.ipynb" was created for completing all scraping and analysis tasks. Below are the fours websites were scraped.
#### NASA Mars News: [NASA Mars News Site](https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest)
The latest news title and paragraph texts were scraped and collected. Assigned the text to variables which could be referenced later.
#### JPL Mars Space Images - Featured Image
Splinter was used to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called "featured_image_url."
#### Mars Facts

#### Mars Hemispheres
### Step 2 - MongoDB and Flask Application
#### Mission to Mars Application Image
![alt app_image](https://github.com/changrita1114/Web-Scraping-Challenge/blob/main/Missions_to_Mars/app_screenshot.png?raw=true)

#### Disclaimer
The resources of this master branch are only for educational purposes. All reserved rights belong to UCSD Data Science and Visualization Boot Camp.
