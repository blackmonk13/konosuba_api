import requests
from bs4 import BeautifulSoup, SoupStrainer

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'
}

api_url = "https://konosuba.fandom.com/wiki/Category:Characters"

def has_char_class(tag):
    print(tag['class'])
    return tag.has_attr('class')# and tag['class'] == 'category-page__members-for-char'

def get_characters():
    try:
        req = requests.get(api_url, headers=headers, timeout=10)

        if req.status_code == requests.codes.ok:
            fchars_content = req.text
            fchars_soup = BeautifulSoup(fchars_content, features="html5lib")
            charmembers = fchars_soup.find_all("li", "category-page__member")
            # print(list(filter(lambda x: not x['character'].startswith("Category"),[dict(character=cm.find('a', 'category-page__member-link').text, link=cm.find('a', 'category-page__member-link')['href']) for cm in charmembers])))
            return list(filter(lambda x: not x['character'].startswith("Category"),[dict(character=cm.find('a', 'category-page__member-link').text, link=cm.find('a', 'category-page__member-link')['href']) for cm in charmembers]))
    except Exception as e:
        print("Oops! Something went wrong. Please try again.")
        return []

# get_characters()