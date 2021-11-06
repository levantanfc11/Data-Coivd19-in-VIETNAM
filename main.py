from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import os, time

if __name__ == '__main__':
    save_data = []
    driver_path = os.path.join('etc', 'chromedriver.exe')
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get("https://covid19.gov.vn/")
    driver.switch_to.frame(1)
    target = driver.find_elements_by_xpath('/html/body/div[2]/div[1]/div')
    for data in target:
        thanhpho = data.find_elements_by_class_name("city")
        tongsoca = data.find_elements_by_class_name("total")
        homnay = data.find_elements_by_class_name("daynow")
        socatuvong = data.find_elements_by_class_name("die")
    list_thanhpho = [city.text for city in thanhpho]
    list_tongsoca = [total.text for total in tongsoca]
    list_homnay = [today.text for today in homnay]
    list_socatuvong = [die.text for die in socatuvong]
    for i in range(len(list_thanhpho)):
        row = "{},{},{},{}\n".format(list_thanhpho[i], list_tongsoca[i], list_homnay[i], list_socatuvong[i])
        save_data.append(row)
    today = (datetime.datetime.now()).strftime("%d-%m-%Y")
    filename = f"{today}.csv"
    with open(os.path.join("data", filename), "w+", encoding="utf-8") as f:
        f.writelines(save_data)

    driver.close()