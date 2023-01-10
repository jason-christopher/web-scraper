import requests    # pip install requests
from bs4 import BeautifulSoup    # pip install beautifulsoup4
import re


def helper(r):
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.find_all(title="Wikipedia:Citation needed")


def polish(text):
    polished = re.sub(r"\[(.*?)\]", "", text)
    return polished


def get_citations_needed_count(url):
    needs = helper(requests.get(url))
    print("Number of citations needed: ", len(needs))


def get_citations_needed_report(url):
    needs = helper(requests.get(url))
    for need in needs:
        text = polish(need.find_parent("p").text)
        print(text)


def get_citations_needed_by_section(url):
    needs = helper(requests.get(url))
    current_header = needs[0].find_previous("h3").text
    print(polish(current_header) + "\n")
    for need in needs:
        if need.find_previous("h3").text != current_header:
            current_header = need.find_previous("h3").text
            print(polish(current_header) + "\n")
        text = polish(need.find_parent("p").text)
        print(text)


if __name__ == '__main__':
    get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico")
    # get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico")
    get_citations_needed_by_section("https://en.wikipedia.org/wiki/History_of_Mexico")
