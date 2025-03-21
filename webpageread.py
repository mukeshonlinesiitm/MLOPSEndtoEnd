from selenium import webdriver
from tempfile import mkdtemp


options = webdriver.ChromeOptions()

# Ensure JavaScript is enabled (default in Chrome, but set explicitly)
prefs = {
    "profile.default_content_setting_values.javascript": 1,  # 1 = Allow JavaScript
    "profile.default_content_setting_values.cookies": 1      # 1 = Allow Cookies
}
options.add_experimental_option("prefs", prefs)

# Other recommended options
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--headless=new")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--log-level=3")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-notifications")
options.add_argument("--disable-extensions")
options.add_argument("--disable-background-networking")
options.add_argument("--ignore-certificate-errors")
options.add_argument(f"--user-data-dir={mkdtemp()}")
options.add_argument(f"--data-path={mkdtemp()}")
options.add_argument(f"--disk-cache-dir={mkdtemp()}")
options.add_argument("--remote-debugging-port=9226")

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

# Open a website to test
driver.get("https://maximelabonne.substack.com/p/uncensor-any-llm-with-abliteration-d30148b7d43e")


# Check if JavaScript is working
js_test = driver.execute_script("return 2 + 2;")
print("JavaScript Test Result:", js_test)  # Should print 4

# Check if cookies are enabled
driver.get("https://maximelabonne.substack.com/p/uncensor-any-llm-with-abliteration-d30148b7d43e")
cookies = driver.get_cookies()
print("Cookies:", cookies)  # Should print a list of cookies
