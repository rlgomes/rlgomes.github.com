
from sst.actions import *
from freshen import *

import os

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
@When('I click back')
def click_back():
    go_back()

@When('I click on (.*)')
def click_on(element):
    element = find_element(element)
    click_element(element)
