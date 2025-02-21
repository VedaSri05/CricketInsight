from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import os

# Set up Selenium WebDriver
chrome_driver_path = r"C:/Program Files/chromedriver-win64/chromedriver.exe"
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
driver = webdriver.Chrome(service=service, options=options)

# Open the website
url = "https://www.bcci.tv/international/men/stats/odi"
driver.get(url)

# Wait for the page to load
wait = WebDriverWait(driver, 10)

# List to store player data
data = []

# **Extract Top Player (Highlighted Player Outside Table)**
try:
    top_player_section = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".team-ranking-wrapper.player")))

    # Extract Player Name
    first_name = top_player_section.find_element(By.CSS_SELECTOR, ".player-name-trw p").text
    last_name = top_player_section.find_element(By.CSS_SELECTOR, ".player-name-trw span").text
    player_name = f"{first_name} {last_name}"

    # Extract Stats
    stats = [stat.text for stat in top_player_section.find_elements(By.CSS_SELECTOR, ".ranking-top-table td p")]

    if len(stats) >= 10:
        total_matches = stats[0]
        innings = stats[1]
        average_score = stats[2]
        strike_rate = stats[3]
        highest_score = stats[4]
        fours = stats[5]
        sixes = stats[6]
        fifties = stats[7]
        hundreds = stats[8]
        total_runs = stats[9]

        # Append to data list
        data.append([player_name, total_matches, innings, average_score, strike_rate, highest_score, fours, sixes, fifties, hundreds, total_runs])

except Exception as e:
    print("Error extracting top player:", e)

# **Extract Players from the Main Table**
try:
    rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".stats-data-table-player tbody tr")))

    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")

        if len(columns) < 12:
            continue  # Skip incomplete rows

        player_name = columns[1].text.strip()
        total_matches = columns[2].find_element(By.TAG_NAME, "h6").text.strip()
        innings = columns[3].find_element(By.TAG_NAME, "h6").text.strip()
        average_score = columns[4].find_element(By.TAG_NAME, "h6").text.strip()
        strike_rate = columns[5].find_element(By.TAG_NAME, "h6").text.strip()
        highest_score = columns[6].find_element(By.TAG_NAME, "h6").text.strip()
        fours = columns[7].find_element(By.TAG_NAME, "h6").text.strip()
        sixes = columns[8].find_element(By.TAG_NAME, "h6").text.strip()
        fifties = columns[9].find_element(By.TAG_NAME, "h6").text.strip()
        hundreds = columns[10].find_element(By.TAG_NAME, "h6").text.strip()
        total_runs = columns[11].find_element(By.TAG_NAME, "h6").text.strip()

        # Append player data
        data.append([player_name, total_matches, innings, average_score, strike_rate, highest_score, fours, sixes, fifties, hundreds, total_runs])

except Exception as e:
    print("Error extracting table data:", e)

# **Ensure 'data/' directory exists**
os.makedirs("data", exist_ok=True)

# **Save Data to CSV**
columns = ["Name", "Total Matches", "Innings", "Average Score", "Strike Rate", "Highest Score", "Fours", "Sixes", "Fifties", "Hundreds", "Total Runs"]
df = pd.DataFrame(data, columns=columns)

df.to_csv("data/bcci_odi_stats.csv", index=False)

print("Scraping completed! Data saved to 'data/bcci_odi_stats.csv'.")

# Close the browser
driver.quit()

# Display first few rows
df.head()
