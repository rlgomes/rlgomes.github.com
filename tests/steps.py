
from sst.actions import *
from freshen import *

import enchant
import re
import os

browser_type = 'firefox'
if 'BROWSER' in os.environ:
    browser_type = os.environ['BROWSER']

import sst.config as config
config.browser_type = browser_type

# part of the spell checking done during content validation
dict = enchant.Dict('en_US')
custom_words = [
                "prolog", "java", "python", "sst", "freshen", "rodney", "lopes",
                "gomes", 'disqus', 'memoize', 'corun', 'kif', 'github', 'nic',
                'GitHub', 'rlgomes.github.com', 'pyperf', 'clifu', 'pangu',
                "jsdb"
               ]

for word in custom_words:
    dict.add(word)

@After
def teardown(scenario_ctx):
    close_window()
    stop()

test_env = 'test'
if 'ENV' in os.environ.keys():
    test_env = os.environ['ENV']

if test_env == 'test':
    url_alias = {
                 'main blog site' : 'http://localhost:4000',
                }
elif test_env == 'prod':
    url_alias = {
                 'main blog site' : 'http://rlgomes.github.com',
                }
else:
    raise Exception("Unknown environment %s" % test_env)


def find_element(search_string):
    """
    Attempt to find an element by using the specified search string to find the
    element in the following order of searching:

        1. by id
        2. by css_class
        3. by text
        4. by text_regex

    """
    if exists_element(id=search_string):
        return get_element(id=search_string)

    if exists_element(css_class=search_string):
        return get_element(css_class=search_string)

    if exists_element(text=search_string):
        return get_element(text=search_string)

    if exists_element(text_regex=search_string):
        return get_element(text_regex=search_string)

    raise Exception("Can't find the element %s" % search_string)

@Given('I am at (.*)')
def i_am_at(url):
    if url in url_alias:
        url = url_alias[url]

    go_to(url)

@Then('I should see the title (.*)')
def should_see_the_title(title):
    assert_title(title)

@NamedTransform('{list}', '([\w\, ]+)', '([\w\, ]+)')
def transform_user_list(list):
    return [ name.strip() for name in list.split(',') ]

@Then('I should see the links? {list}')
def should_see_the_link(links):
    for link in links:
        element = find_element(link)
        assert_link(element)

@Then('I should see the headers? {list}')
def should_see_the_headers(headers):
    for header in headers:
        aux = 'text()="%s"' % header
        get_element_by_xpath('//h1[%s] | //h2[%s] | //h3[%s] | //h4[%s]' % \
                             (aux, aux, aux, aux))


@Then('I should see everything spelled correctly')
def verify_page_spelling():
    text = get_element(tag="body").text
    text = text.replace('\n',' ')
    text = text.replace(':',' ')
    text = text.replace('-',' ')
    words = text.split()
    word_regex = re.compile("[a-zA-Z]+")

    mispelled_words = []
    for word in words:
        if not(word_regex.match(word)):
            continue

        if not(dict.check(word)):
            mispelled_words.append(word)

    if mispelled_words:
        print("misspelled words %s" % mispelled_words)
        fails()

@When('I click back')
def click_back():
    go_back()

@When('I click on (.*)')
def click_on(element):
    element = find_element(element)
    click_element(element)
