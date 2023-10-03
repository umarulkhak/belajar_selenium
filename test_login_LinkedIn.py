from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Inisialisasi WebDriver (gunakan driver yang sesuai dengan browser yang Anda gunakan)
driver = webdriver.Chrome()

# Buka halaman LinkedIn
driver.get("https://www.linkedin.com")

# Isi formulir login
username = "your_username"
password = "your_password"

username_field = driver.find_element(By.ID, "session_key")
password_field = driver.find_element(By.ID, "session_password")

username_field.send_keys(username)
password_field.send_keys(password)

# Submit formulir login
password_field.send_keys(Keys.RETURN)

# Menunggu beberapa detik untuk memastikan halaman sepenuhnya dimuat
driver.implicitly_wait(10)

# Verifikasi login berhasil (contoh: memeriksa apakah elemen profil pengguna muncul)
try:
    profile_element = driver.find_element(By.CLASS_NAME, "profile-rail-card__actor-link")
    print("Login berhasil!")
except Exception as e:
    print("Login gagal: ", e)

# Menutup browser setelah pengujian selesai
driver.quit()
