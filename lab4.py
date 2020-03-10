from selenium import webdriver
import time

driver = webdriver.Chrome()

with open('sites.txt') as sites:
    sites_list = [line.strip() for line in sites]
    sites_list.sort(key=lambda s: len(s))
    print('### OPENING SITES ###')
    for index, line in enumerate(sites_list):
        print(f'{index} : {line}')
        driver.get(line)
        if index < 9:
            driver.execute_script("window.open('','_blank')")
            driver.switch_to.window(driver.window_handles[index + 1])

    tabs_list = sites_list.copy()
    sites_list.sort()

    print('### CLOSING SITES ###')
    for site in sites_list:
        print(site)
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[tabs_list.index(site)])
        driver.close()
        tabs_list.remove(site)
