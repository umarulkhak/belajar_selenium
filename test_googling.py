from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Inisialisasi WebDriver (gunakan Chrome WebDriver, Anda harus mengunduhnya terlebih dahulu)
driver = webdriver.Chrome()

# Buka halaman Google
driver.get("https://www.google.com")

# Temukan elemen input pencarian menggunakan nama elemennya (q untuk Google Search)
search_box = driver.find_element("name", "q")

# Masukkan teks pencarian (nama Umar Ulkhak)
search_box.send_keys("Umar Ulkhak")

# Tekan tombol Enter untuk memulai pencarian
search_box.send_keys(Keys.RETURN)

# Tunggu beberapa detik untuk memberi cukup waktu halaman web merespons
driver.implicitly_wait(10)

# Verifikasi hasil pencarian (Anda dapat menambahkan logika pengujian lainnya di sini)
if "Umar Ulkhak" in driver.page_source:
    print("Pencarian berhasil! Test Passed.")
else:
    print("Pencarian gagal! Test Failed.")

# Tutup browser setelah pengujian selesai
driver.quit()
