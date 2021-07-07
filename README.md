# Fund-Performance-Web-Scraper
This is a Python web-scraper for generating performance graphs of equity funds.
<img alt="GUI" src="https://i.imgur.com/5P9EeSY.png"></img>

## Setup 
1. In addition to [Python]( https://www.python.org/downloads/) you will need the following libraries:
	- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) _for web scraping_
	- [Matplotlib](https://pypi.org/project/matplotlib/) _for generating performance graphs_
	- [Pillow](https://pypi.org/project/Pillow/)
2. Visit http://www.fundsdata.co.za/navs/default.htm 
3. Click on one of the Funds links, for example _South African - Equity - General Funds_
4. Save the webpage as ```Funds.html``` in the application’s directory 

## Using the application  
### You are provided with two options:
- **Extract all data**:  This scrapes all the data from the webpage and saves it into a ```.csv``` file
- **Search for fund name**: Produces a performance graph in the code’s directory for the queried fund. This is the primary function of the application, here is an example:
<img alt="PerformanceExample" src=" https://i.imgur.com/MfLGjpV.jpg "></img>
