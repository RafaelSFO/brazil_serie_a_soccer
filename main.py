# %%
from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np
# %%
# Defining the seasons
seasons = ['2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']
global all_seasons
all_seasons = pd.DataFrame()

data_list_full = []
def get_season_table(year):
    # Getting content of the page
    url_page = f'https://fbref.com/en/comps/24/{year}/{year}-Serie-A-Stats'
    html_page = requests.get(url_page)
    if html_page.status_code == 200:
        print('Conection ok!')
    else:
        print('No conection')
    # Parsing HTML page with BeautifulSoup to get the table
    page_with_bs = BeautifulSoup(html_page.content, 'html5lib')
    table_id = f'results{year}241_overall'
    table = page_with_bs.find('table', {'id': table_id})
    #Getting the wanted columns
    columns = []
    for column in table.find_all('th')[0:19]:
        columns.append(column.text.strip().replace('/', '').replace(' ', '_'))
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
        if len(rows) == 18:
            xg = rows[10].text.strip()
            xga = rows[11].text.strip()
            xgd = rows[12].text.strip()
            xgd_90 = rows[13].text.strip()
            attendance = rows[14].text.strip()
            top_team_scorer = rows[15].text.strip()
            goalkeeper = rows[16].text.strip()
            notes = rows[17].text.strip()
        else:
            xg = np.nan
            xga = np.nan
            xgd = np.nan
            xgd_90 = np.nan
            attendance = rows[10].text.strip()
            top_team_scorer = rows[11].text.strip()
            goalkeeper = rows[12].text.strip()
            notes = rows[13].text.strip()
        data_list = [rnk, squad, mp, w, d, l, gf, ga, gd, pts, pts_mp, xg, xga, xgd, xgd_90, attendance, top_team_scorer, goalkeeper, notes, year]
        data_list_full.append(data_list)
    data_list_full.insert(0, columns)
    return data_list_full
# %%
for year in seasons:
    data_from_list = get_season_table(year)
del data_from_list[0]
# %%
pd.DataFrame(columns=['Rk',
 'Squad',
 'MP',
 'W',
 'D',
 'L',
 'GF',
 'GA',
 'GD',
 'Pts',
 'PtsMP',
 'xG',
 'xGA',
 'xGD',
 'xGD90',
 'Attendance',
 'Top_Team_Scorer',
 'Goalkeeper',
 'Notes', 'Year'], data=data_from_list).to_excel(r'C:\Users\rafae\Documents\RAFAEL - ESTUDOS\Data Engineering\teste.xlsx', index=False)
# %%

# %%
