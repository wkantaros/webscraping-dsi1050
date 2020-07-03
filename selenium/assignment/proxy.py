from bs4 import BeautifulSoup as soup
import requests

# pulled heavily from this article
# https://medium.com/datadriveninvestor/how-to-not-get-caught-while-web-scraping-88097b383ab8

# this also looks promising (although less work for student)
# https://medium.com/ml-book/multiple-proxy-servers-in-selenium-web-driver-python-4e856136199d


def get_proxies():
    proxy_url = 'https://free-proxy-list.net/'
    response = requests.get(proxy_url)
    proxy_page_html = response.text
    proxy_page_soup = soup(proxy_page_html, 'html.parser')
