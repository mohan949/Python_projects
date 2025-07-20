import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
keyword = "laptop"
for page_no in range (1, 3):
    driver.get(f"https://www.amazon.in/s?k={keyword}&page={page_no}&crid=2BTJRAN65AN4A&sprefix=hi%2Caps%2C268&ref=nb_sb_noss_2")
    #https://www.amazon.in/s?k=laptop&page=2&crid=J0O00RBYNMJF&qid=1732812863&sprefix=lapto%2Caps%2C244&ref=sr_pg_2
    product_card_xpath = "//div[@class='puis-card-container s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis puis-v4s73penu6ddq273xf3q9lbp2k s-latency-cf-section puis-card-border']"
    # assert "Python" in driver.title
    elem = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    # print(elem.text)
    # print(elem.get_attribute("outerHTML"))

    print(f'{len(elem)} --> elements found')

    for ele in elem:
        print(ele.text)

    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
    time.sleep(3)
    driver.close()