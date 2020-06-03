import os
from selenium import webdriver
from time import sleep

target_url = "http://www.naver.com" 
# chromedriver 실행 경로
driver = "C:\ProgramData\Anaconda3\Lib\site-packages\selenium\chromedriver\chromedriver"
screenshot_name = "K:\My files\Download\screen\my_screen_shot_0601.png"
#screenshot_name = "my_screen_shot_0601.png"

#User options 선언 
#webdriver chorme 기본옵션 -> 유저 옵션 option으로 지정
options = webdriver.ChromeOptions()
options.add_argument("disable-gpu")
options.add_argument("lang=ko_KR") # 한국어!
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

# 유저 options 추가 webdriver사용시 default directory      
options.add_experimental_option("prefs", {
  "download.default_directory": r"K:\My files\Download\screen",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
   })     
#웹드라이버 실행 
#driver = webdriver.Chrome(driver)

#웹드라이버 실행 with user options
driver = webdriver.Chrome(driver, chrome_options = options)
#driver.get(target_url) 
# adding the loading time.
sleep(0.1)

#driver.set_window_size(1920, 1080)
driver.get(target_url)

# chapture!
#driver.get_screenshot_as_file(screenshot_name)
driver.implicitly_wait(3)
#webdriver 사용중 capture 저장시,webdriver default directory보다는, 화일이름지정시 경로명시 
driver.save_screenshot(screenshot_name)
#driver.quit()
print("화면 캡처 완료...")
# 브라우저를 닫는다.
driver.close()
