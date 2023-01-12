import requests    # pip install requests
from bs4 import BeautifulSoup    # pip install beautifulsoup4
import re


input_url = input("> Paste the URL of the Wikipedia page you'd like to scrape (or push Return for the default): ")


# returns list of all <a> tags that have a title of "Wikipedia:Citation needed"
def helper(r):
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.find_all(title="Wikipedia:Citation needed")


# Uses the helper function to return a list of <a> tags and returns the number of citations needed
def get_citations_needed_count(url):
    needs = helper(requests.get(url))
    print("Number of citations needed: ", len(needs))


# Uses the helper function to return a list of <a> tags, then finds the parent <p> tag for each and returns the text
def get_citations_needed_report(url):
    try:
        needs = helper(requests.get(url))
        for need in needs:
            print(need)
    except:
        print("No citations needed")


# Uses the helper function to return a list of <a> tags, then finds its parent <h3> tag, then...
# determines if it's already been printed, then finds the parent <p> tag for each and returns the text
def get_citations_needed_by_section(url):
    try:
        needs = helper(requests.get(url))
        current_header = needs[0].find_previous("h3").text
        print(re.sub(r"\[(.*?)\]", "", current_header) + "\n")
        for need in needs:
            if need.find_previous("h3").text != current_header:
                current_header = need.find_previous("h3").text
                print(re.sub(r"\[(.*?)\]", "", current_header) + "\n")
            print(need.find_parent("p").text)
    except:
        print("No citations needed")


if __name__ == '__main__':
    if not input_url:
        get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico")
        # get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico")
        get_citations_needed_by_section("https://en.wikipedia.org/wiki/History_of_Mexico")
    else:
        get_citations_needed_count(input_url)
        # get_citations_needed_report(input_url)
        get_citations_needed_by_section(input_url)
