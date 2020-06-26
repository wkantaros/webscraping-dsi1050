# Web Scraping Homework

## About

The purpose of this assignment is to work with python web scraping tools in an applicable way. To do so, we will be using modern and established web scraping tools, such as [Scrapy](https://scrapy.org/), [Requests](https://requests.readthedocs.io/en/master/), and [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to build a Google Chrome extension that compares the prices of Amazon books with other online retailers, such as Barnes and Nobles and Booksamillion.

## Outline

Basically going to parse through every book on http://books.toscrape.com/ and add pertinent information to a database

Going to essentially do the project twice (once with scrapy, and once with requests + soup)

Looking for:
    name of book
    author
    price
    availability
    stars

*note: the first part of this project can also be done with Scrapy, but in efforts to be techincally literate with as many packages as possible we're electing to do with with Requests and Soup*

## Things to figure out/to be discussed with TA's
- what database should be used for caching - atlas could be cool since the entire class could then access it

- what's the best way to turn this into a chrome extension, is it even worthwhile to do so 