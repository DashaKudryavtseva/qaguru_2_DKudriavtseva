import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture()
def opening():
    browser.config.window_width = 1280
    browser.config.window_height = 720



@pytest.fixture()
def opening_negative():
    browser.config.window_width = 1920
    browser.config.window_height = 1080



def test_search(opening):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_negative(opening_negative):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('dsfкариылпрnlskdnglskg%%%12787snblksjnbldxn').press_enter()
    browser.element('[id="result-stats"]').should(
        have.text('Результатов: примерно 0'))
