from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome WebDriver'ı başlat
driver = webdriver.Chrome()

try:
    # Insider'ın ana sayfasına gi
    driver.get("https://www.useinsider.com")

    # Company dropdown menüsünü aç
    company_dropdown = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='nav-link dropdown-toggle' and contains(text(),'Company')]")))
    company_dropdown.click()

    # "Careers" linkini bul ve tıkla
    careers_link = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='dropdown-sub' and contains(text(),'Careers')]")))
    careers_link.click()

    # Kariyer sayfasının tamamen yüklenmesini bekle
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//div[@class='content']")))
    # Sayfanın yüklenme işlemi tamamlandıktan sonra devam edebilirsiniz
    print("Sayfa tamamen yüklendi.")

except Exception as e:
    print("Hata:", e)

    # "See all teams" butonunu kontrol et
    teams_button = driver.find_element(By.XPATH, "//a[@class='btn btn-outline-secondary rounded text-medium mt-5 mx-auto py-3 loadmore']")
    assert teams_button.is_displayed(), "See all teams button is not accessible"

    # Our Locations metnini kontrol et
    locations_text = driver.find_element(By.XPATH, "//h3[@class='category-title-media ml-0']")
    assert locations_text.is_displayed(), "Our Locations text is not accessible"

    # Life at Insider metnini kontrol et
    life_text = driver.find_element(By.XPATH, "//h2[@class='elementor-heading-title elementor-size-default']")
    assert life_text.is_displayed(), "Life at Insider text is not accessible"

    print("Başarılı")


finally:
    # Tarayıcıyı kapat
    driver.quit()
