from selenium import webdriver
from selenium.webdriver.common.by import By

# create a new browser instance
driver = webdriver.Chrome()

# navigate to the NY Times website
driver.get("https://www.nytimes.com/")

button = driver.find_element(By.CSS_SELECTOR, "css-10488qs")
button.click()

# find the search box element
search_box = driver.find_element(By.NAME, "query")

# enter a search query
search_box.send_keys("Coronavirus")

# submit the search form
search_box.submit()

# find the first article on the search results page
first_article = driver.find_element(By.CSS_SELECTOR, ".css-2fgx4k")

# click on the first article to open it
first_article.click()

# print the headline of the article
headline = driver.find_element(By.CSS_SELECTOR,".css-1h8wlje edye5kn2")
print(headline.text)

# close the browser
driver.quit()

#Please also note that the .css selectors were gathered by hand as the NYTimes uses an algorithm to generate css selectors so while some may be the same they will not all be (This is to help prevent webscraping)