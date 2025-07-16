import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import have
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install())
browser.config.driver = webdriver.Chrome(service=service)
browser.config.window_width = 1920
browser.config.window_height = 1080
browser.config.timeout = 10


def test_issue_name_clean_selen():
    browser.open('https://github.com')

    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('ZhannaOvcharenko/qa_guru_python_10_hw').press_enter()
    browser.element(by.link_text('ZhannaOvcharenko/qa_guru_python_10_hw')).click()
    browser.element('#issues-tab').click()

    browser.element('a.Link--primary[data-hovercard-type="issue"]').should(have.text('Test issue'))


def test_issue_name_dynamic_steps():
    allure.dynamic.tag("github")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Issues в репозитории")
    allure.dynamic.story("Проверка соответствия названия issue")
    allure.dynamic.link("https://github.com", name="Testing")

    with allure.step("Открыть главную страницу"):
        browser.open('https://github.com')

    with allure.step("Найти репозиторий"):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type('ZhannaOvcharenko/qa_guru_python_10_hw').press_enter()

    with allure.step("Перейти по ссылке в репозиторий"):
        browser.element(by.link_text('ZhannaOvcharenko/qa_guru_python_10_hw')).click()

    with allure.step("Открыть вкладку 'issues'"):
        browser.element('#issues-tab').click()

    with allure.step("Проверить наличие issue с названием 'Test issue'"):
        browser.element('a.Link--primary[data-hovercard-type="issue"]').should(have.text('Test issue'))


@allure.tag("github")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "ZhannaOvcharenko")
@allure.feature("Issues в репозитории")
@allure.story("Проверка соответствия названия issue")
@allure.link("https://github.com", name="Testing")
def test_issue_name_with_decorator_steps():
    open_github_main_page()
    search_for_repository('ZhannaOvcharenko/qa_guru_python_10_hw')
    go_to_repository('ZhannaOvcharenko/qa_guru_python_10_hw')
    open_issues_tab()
    should_see_issue_with_name('Test issue')


@allure.step("Открыть главную страницу")
def open_github_main_page():
    browser.open('https://github.com')


@allure.step("Найти репозиторий {repo}")
def search_for_repository(repo):
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type(repo).press_enter()


@allure.step("Перейти по ссылке в репозиторий {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открыть вкладку 'issues'")
def open_issues_tab():
    browser.element('#issues-tab').click()


@allure.step("Проверить наличие issue с названием {name}")
def should_see_issue_with_name(name):
    browser.element('a.Link--primary[data-hovercard-type="issue"]').should(have.text(name))
