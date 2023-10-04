from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Inisialisasi WebDriver (gunakan driver yang sesuai dengan browser yang Anda gunakan)
driver = webdriver.Chrome()

# Buka halaman Tokopedia
driver.get("https://www.tokopedia.com")

# Cari barang dengan kata kunci "samsung"
search_box = driver.find_element(By.CLASS_NAME, "css-3017qm")
search_box.send_keys("samsung")
search_box.send_keys(Keys.ENTER)

# Menunggu beberapa detik untuk memastikan hasil pencarian dimuat sepenuhnya
driver.implicitly_wait(10)

# Menutup browser setelah pengujian selesai
driver.quit()
