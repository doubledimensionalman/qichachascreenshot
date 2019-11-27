
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd
st= xlrd.open_workbook(r"D:\User Data\Desktop\截图.xlsx")
table = st.sheets()[0]
col_values=table.col_values(0, start_rowx=0, end_rowx=None)
i=1
for col_value in col_values:
    if i==1:
        driver= webdriver.Chrome()
        driver.get("https://www.qichacha.com/")
        ele=driver.find_element_by_id("searchkey")
        ele.send_keys(col_value)
        ele.send_keys(Keys.RETURN)
    else:
        ele1=driver.find_element_by_xpath('//*[@id="headerKey"]')
        ele1.clear()
        ele1.send_keys(col_value)
        ele1.send_keys(Keys.RETURN)
         
    abc=driver.find_element_by_xpath('//*[@id="search-result"]/tr[1]/td[3]/a')
    abc.click()
    handles = driver.window_handles
    driver.switch_to.window(handles[i])
    X=r'D:\User Data\Desktop\截图\\'[:-1]
    Y='.png'
    time.sleep(0.75)
    driver.save_screenshot(X+col_value+Y)
    i=i+1 
driver.close()
driver.quit()
