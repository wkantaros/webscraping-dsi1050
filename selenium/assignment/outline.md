# Web Scraping Homework

## About

The purpose of this assignment is to work with python web scraping tools in an applicable way. To do so, we will be using [Selenium](https://www.selenium.dev/documentation/en/) to build a virtual crawler that 1) logs into and scrapes the product names from a given website and 2) searches for that product on ebay & amazon and returns it to the user.


### A brief reintroduction to the internet

- discuss internet
- discuss dom
- workout an outline (explain what a browser is, document object model, static vs dynamic styling)
- explain html, css, and js -- dom
- find example of site with and w/o js
- Discuss js rendered vs html rendered content

### Selenium

Selenium was created as a tool to help developers automate testing on the internet. 
- Discuss what selenium does and why its important
- more powerful than other tools (some only render html content)

## Outline

- very high level what will be happening in project

- playing around with inspector
- going through authentication in driver
- going to be searching for price on ebay
- going to be searching for price on amazon
<!-- - if not yet in database, add to database
- if in database, pull out price of good
- if already in database, report back to user and let know if price 
- increased or decreased since the last search -->
- discuss importance of proxy farms, why we'll be using those

>"Websites are cabaple of tracking your IP information, pages you visit with the same IP, your user agent information, your request frequencies and many other metrics. You can think IP as of your internet identity and any systematic requests sent from the same IP to a website can be easily detected by anti-webscraper tools and you will get IP-banned.
>Our robot should be imitating regular human internet surfing behaviour so that it will not get noticed or cause any suspicion to any website. To make it more clear: Imagine yourself visiting pages of a website while using a free VPN service each time you change the page. Wait for a random amount of time in between two pages and also copy/paste the data from the website."

Explain difference between elite and anonymous proxies
"Elite or High Anonymity Proxies are considered to be the best because they provide the absolute highest level of anonymity. When using this type of proxy, the server you are connecting to has no idea that the connection was made through a proxy nor does it know your real IP address."

"Anonymous Proxies or sometimes known as distorting proxies can provide a sufficient level of anonymity and are thus considered to be useful for most purposes. This type of proxy does not reveal your IP address to a server, however the server will know that the connection was made through a proxy because of the additional information that is sent with each request. Anonymous Proxies usually identify themselves by attaching additional headers to each request such as:
HTTP_CLIENT_IP = ...
HTTP_X_FORWARDED_FOR = ...
HTTP_X_FORWARDED = ...
HTTP_X_CLUSTER_CLIENT_IP = ...
HTTP_FORWARDED_FOR = ...
HTTP_FORWARDED = ...
"

transparent proxies arent great 



- Get a persistent mongdodb database somewhere
- finish that
- find outline for those
- finish outline for outline.md
start brainstorming a 