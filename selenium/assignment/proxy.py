from bs4 import BeautifulSoup as soup
import requests

# pulled heavily from this article
# https://medium.com/datadriveninvestor/how-to-not-get-caught-while-web-scraping-88097b383ab8

# this also looks promising (although less work for student)
# https://medium.com/ml-book/multiple-proxy-servers-in-selenium-web-driver-python-4e856136199d


def get_proxies():
    proxy_url = 'https://free-proxy-list.net/'
    response = requests.get(proxy_url)
    proxy_html = response.text
    proxy_soup = soup(proxy_html, 'html.parser')

    table_body = proxy_soup.find_all('tbody')[0]
    proxies = set()
    counter = 0
    # we only want first 80 out of 300 (can adjust later potentially)
    for row in table_body.find_all('tr')[0:300]:
        ip = row.find_all('td')[0].text
        port = row.find_all('td')[1].text
        anonymity = row.find_all('td')[4].text
        https = row.find_all('td')[6].text

        if anonymity == 'elite proxy' and https == 'yes':
            proxy = ip + ':' + port
            proxies.add(proxy)
            counter+=1
        print(ip + ':' + port + ' ' + anonymity + ' ' + https)
    print(counter)
    return(proxies)


def check_proxies():
    working_proxies = set()
    proxies = get_proxies()
    test_url = 'https://httpbin.org/ip'
    for i in proxies:
        print("\nTrying to connect with proxy: {}".format(i))
        try:
            response = requests.get(
                test_url, proxies={"http": i, "https": i}, timeout=1)
            print(response.json())
            print("Adding proxy to the list")
            working_proxies.add(i)

        except:
            print("Skipping. Connnection error / too slow")

    return working_proxies


working_proxies = check_proxies()
print(working_proxies)
# get_proxies()
