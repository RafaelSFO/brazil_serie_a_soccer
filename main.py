# %%
from bs4 import BeautifulSoup
import pandas as pd
import requests

# Getting content of the page
html_page = requests.get('https://fbref.com/en/comps/24/2022/2022-Serie-A-Stats')
# %%
# Checking if the conection with the website is working or not
if html_page.status_code == 200:
    print('Ok!')
else:
    print('No conection')
# %%
# Parsing HTML page with BeautifulSoup to get the table
page_with_bs = BeautifulSoup(html_page.content, 'html5lib')
table = page_with_bs.find('table', {'id': 'results2022241_overall'})
# %%
# Getting the wanted columns
columns = []
for column in table.find_all('th')[0:19]:
    columns.append(column.text.strip().replace('/', '').replace(' ', '_'))
# %%
regular_season = pd.DataFrame()
index_num = 0
# Inside each 'tr' is where whe can find the content of a row 'td'
for each_row in table.tbody.find_all('tr'):
    rows = each_row.find_all('td')
    rnk_rows = each_row.find_all('th')
    rnk = rnk_rows[0].text.strip()
    squad = rows[0].text.strip()
    mp = rows[1].text.strip()
    w = rows[2].text.strip()
    d = rows[3].text.strip()
    l = rows[4].text.strip()
    gf = rows[5].text.strip()
    ga = rows[6].text.strip()
    gd = rows[7].text.strip()
    pts = rows[8].text.strip()
    pts_mp = rows[9].text.strip()
    xg = rows[10].text.strip()
    xga = rows[11].text.strip()
    xgd = rows[12].text.strip()
    xgd_90 = rows[13].text.strip()
    attendance = rows[14].text.strip()
    top_team_scorer = rows[15].text.strip()
    goalkeeper = rows[16].text.strip()
    notes = rows[17].text.strip()
    regular_season = pd.concat([regular_season, pd.DataFrame.from_records({'Rk': rnk, 'Squad':squad, 'MP': mp,
    'W': w, 'D': d, 'L': l, 'GF': gf, 'GA': ga, 'GD': gd, 'Pts': pts, 'PtsMP': pts_mp,
    'xG': xg, 'xGA':xga, 'xGD':xgd, 'xGD90': xgd_90, 'Attendance': attendance, 'Top_Team_Scorer': top_team_scorer, 'Goalkeeper': goalkeeper, 'Notes':notes}, columns=columns, index=[index_num])], axis=0)
    index_num = index_num + 1
