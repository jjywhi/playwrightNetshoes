# features/steps/steps.py
from behave import given, when, then
from playwright.sync_api import sync_playwright
import os

def take_screenshot(context, step_name):
    screenshot_path = os.path.join('reports', f'{step_name}.png')
    context.page.screenshot(path=screenshot_path)

@given('I open the Netshoes homepage')
def step_open_homepage(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    context.page.goto('https://www.netshoes.com.br')
    take_screenshot(context, 'screenshot_home')
    context.page.wait_for_timeout(2000)

@when('I search for "{product}"')
def step_search_product(context, product):
    search_1 = context.page.wait_for_selector('//input[@id="search"]')
    search_1.click()
    search_1.type(product)
    take_screenshot(context, 'screenshot_Nike')
    search_1.press('Enter')
    take_screenshot(context, 'screenshot_search')

@when('I click on the product with text "{text}"')
def step_click_product(context, text):
    text_preco = context.page.wait_for_selector(f'//*[@id="content"]/div/div[2]/section/div/div[4]/a/div[2]/h2[contains(text(), "{text}")]')
    text_preco.click()
    context.page.wait_for_timeout(2500)
    take_screenshot(context, 'screenshot_preco')

@when('I select the size')
def step_select_size(context):
    size = context.page.wait_for_selector('//*[@id="content"]/div[2]/div[3]/div[1]/section/div[2]/ul/li[4]/a')
    size.click()
    take_screenshot(context, 'screenshot_size')
    context.page.wait_for_timeout(1000)

@when('I click the buy button')
def step_click_buy_button(context):
    comprar = context.page.wait_for_selector('//*[@id="content"]/div[2]/div[3]/div[2]/div/div/div/button')
    comprar.click()
    take_screenshot(context, 'screenshot_buy')
    context.page.wait_for_timeout(1000)
    take_screenshot(context, 'screenshot_1+')
@then('I click on the home icon')
def step_click_home(context):
    botao_home = context.page.wait_for_selector('div.logo__image')
    botao_home.click()
    take_screenshot(context, 'screenshot_home_icon')
    context.page.wait_for_timeout(1000)

@then('I hover over the cart icon')
def step_hover_cart_icon(context):
    context.page.hover('span.mini-cart__number')
    take_screenshot(context, 'screenshot_hover_icon')
    context.page.wait_for_timeout(3000)
    context.browser.close()
