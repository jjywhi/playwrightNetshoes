import os
from behave.model_core import Status

def after_step(context, step):
    if step.status == Status.failed:
        screenshot_path = os.path.join('reports', f'{step.name}.png')
        context.page.screenshot(path=screenshot_path)
        context.attach_file(screenshot_path, 'image/png')

def after_scenario(context, scenario):
    context.browser.close()
    context.playwright.stop()