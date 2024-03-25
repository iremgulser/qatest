from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Chrome WebDriver'ı başlat
driver = webdriver.Chrome()

try:
    # QA iş ilanları sayfasına git
    driver.get("https://useinsider.com/careers/quality-assurance/")

    # Pencereyi tam ekran yap
    driver.maximize_window()

    # Düğmeyi bulmak için bekleyici oluştur
    accept_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "wt-cli-accept-all-btn"))
    )
    # Düğmeye tıkla
    accept_button.click()

    # "See all QA jobs" butonuna tıklamak için JavaScript kullan
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-outline-secondary rounded text-medium mt-2 py-3 px-lg-5 w-100 w-md-50']"))))

    # Sayfanın yüklenmesini bekleyin
    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading-spinner")))


    # Departman seçim kutusunu bul
    department_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "select2-selection__rendered")))

    # Departman seçim kutusunu tıkla
    department_dropdown.click()

    # Quality Assurance'ı seç
    qa_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "//li[contains(@class, 'select2-results__option') and text()='Quality Assurance']")))
    qa_option.click()

    # WebDriverWait kullanarak "Quality Assurance" seçeneğini bekleyecek kod
    wait = WebDriverWait(driver, 30)
    element = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.select2-results__option[id*="Quality Assurance"]')))
    element.click()

    # "All" seçeneğine tıklamak için XPath'i kullanabilirsiniz
    all_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@title='All']")))

    # "All" seçeneğine tıklama işlemini gerçekleştirin
    all_option.click()

    # "Istanbul, Turkey" seçeneğine tıklamak için XPath'i kullanabilirsiniz
    istanbul_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//li[@id='select2-filter-by-location-result-498v-Istanbul, Turkey']")))
    istanbul_option.click()

    # İş ilanlarının listesini kontrol et
    job_listings = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, "//span[@class='position-department text-large font-weight-600 text-primary']")))
    all_qa = all("Quality Assurance" in listing.text for listing in job_listings)

    # Find the "View Role" button by its XPath or other suitable selector
    view_role_button = driver.find_element_by_xpath("//a[@class='btn btn-navy rounded pt-2 pr-5 pb-2 pl-5' and text()='View Role']")

    # Click the "View Role" button
    view_role_button.click()

    # Verify that the current URL is the Lever Application form page URL
    if "https://jobs.lever.co/useinsider/" in driver.current_url:
        print("Clicked 'View Role' button successfully redirected to the Lever Application form page.")
    else:
        print("Failed to redirect to the Lever Application form page after clicking 'View Role' button.")

finally:
    # Tarayıcıyı kapat
    driver.quit()
