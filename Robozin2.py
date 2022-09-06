import time
import requests
import pandas as pd
import lxml
import html5lib

from bs4 import BeautifulSoup
# selenium things
# from selenium import
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Site a ser atuado
url = "https://www.nba.com/stats/players/traditional/?sort=TEAM_ABBREVIATION&dir=1&Season=2019-20&SeasonType=Regular" \
      "%20Season&PerMode=Totals "

# Checa se o WebDriver esta atualizado
servico = Service(ChromeDriverManager().install()) # erro aq

# navegador = webdriver.Chrome(service=servico)

# option headless roda tudo em backgraund
# option = Options()
# option.headless = True
driver = webdriver.Chrome()  # options=option esta dando error

driver.get(url)
time.sleep(8)
# ação a ser executada
driver.find_element(By.XPATH,
                    "//div[@class='nba-stat-table__overflow']//table//thead//tr//th[@data-field='PTS']").click()

element = driver.find_element(By.XPATH, "//div[@class='nba-stat-table__overflow']//table")
html_content = element.get_attribute('outerHTML')

# Extração
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

# convertendo o html em dados
df_full = pd.read_html(str(table))[0].head(10)
df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', 'PTS']]
df.columns = ['pos', 'player', 'team', 'total']

print(df)
# Fechar a pagina
driver.quit()
