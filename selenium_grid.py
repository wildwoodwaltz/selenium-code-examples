from selenium import webdriver

# set the url for the gridhub
grid_hub_url = "http://[grid_hub_ip]:4444/wd/hub"

# configure the desired capabilities the browsers using a dictionary object
firefox_cap = {
                'browserName': 'firefox',
                'platform': 'linux',
                'version': 'latest'
            }
chrome_cap = {
                'browserName': 'chrome',
                'platform': 'linux',
                'version': 'latest'
            }

# create a new browser instance for Firefox and chrome on the grid hub
firefox_browser = webdriver.Remote(command_executor=grid_hub_url,
                                   desired_capabilities=firefox_cap)
chrome_browser = webdriver.Remote(command_executor=grid_hub_url,
                                   desired_capabilities=chrome_cap)

# navigate to a website on Firefox and Chrome
firefox_browser.get("https://www.google.com")
chrome_browser.get("https://www.google.com")
 
# print the page title on Firefox and chrome
print(f'Page title on Firefox: {firefox_browser.title}')
print(f'Page title on Chrome: {chrome_browser.title}')

# close the browsers
firefox_browser.quit()
chrome_browser.quit()
