import requests
# pip install requests
from bs4 import BeautifulSoup
# pip install beautifulsoup4


def get_citations_needed_count(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    needs = soup.find_all(title="Wikipedia:Citation needed")
    print(len(needs))


def get_citations_needed_report(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    needs = soup.find_all(title="Wikipedia:Citation needed")
    for need in needs:
        print(need.find_parent("p").text)


if __name__ == '__main__':
    get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico")
    get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico")


# if __name__ == '__main__':
#     url = "https://testing-www.codefellows.org/course-calendar/?filters=400:%20Advanced,code-python-401"
#     response = requests.get(url)
#     results = parse(response.text)
#     print(results)
