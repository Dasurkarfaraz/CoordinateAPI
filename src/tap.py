from appium.webdriver.common.touch_action import TouchAction

def tap_on_coordinates(driver, x, y):
    action = TouchAction(driver)
    action.tap(x=x, y=y).perform()
