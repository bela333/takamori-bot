from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import time
from PIL import Image
import io

def render(text):
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options = chrome_options)
    path = os.path.abspath("takamori_comic/index.html")
    driver.get("file:///" + path)

    driver.execute_script("updateText(arguments[0])", text)
    time.sleep(2)

    render_space = driver.find_element_by_id("renderSpace")

    driver.set_window_size(render_space.size["width"], render_space.size["height"])

    image_data = driver.get_screenshot_as_png()
    image = Image.open(io.BytesIO(image_data))
    return image