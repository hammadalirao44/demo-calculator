from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Headless Chrome for GitHub Actions
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

# Open the HTML file (adjust path if needed)
driver.get("file:///C:/Users/user/Desktop/Github/demo-calculator/index.html")

# Enter values
driver.find_element(By.ID, "num1").send_keys("10")
driver.find_element(By.ID, "num2").send_keys("5")

# Select operation
driver.find_element(By.ID, "operation").send_keys("add")

# Click calculate
driver.find_element(By.ID, "calculate").click()

# Check result
result = driver.find_element(By.ID, "result").text
assert result == "15", f"Expected 15 but got {result}"

print("Test passed!")
driver.quit()


print("this is hammad")