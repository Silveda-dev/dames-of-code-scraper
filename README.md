# dames-of-code-scraper

Dames of Code is a web-app designed to share the stories of early women in technology. Using BeautifulSoup, it scrapes and formats content from their Wikipedia profiles and then, using Flask, renders this information in a HTML template. All of the women featured in DoC were sourced from the book _Broad Band_ by Claire L. Evans.

**INSTRUCTIONS TO RUN YOUR OWN DEMO (FOR LINUX USERS)**
1) Download this repo
2) If you don't already have virtualenv installed, you can install it with the command ```pip install virtualenv```
3) Create (```virtualenv venv```) and then activate (```source ./venv/bin/activate```) a virtual environment
4) If you don't already have Flask installed, you can install it with ```pip install Flask```
5) Run the file dame-scraper.py
6) With your browser, open the address indicated in the terminal (this will usually be http://127.0.0.1:5000/)
