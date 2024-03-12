# %%
import requests
html_page = requests.get('https://fbref.com/en/comps/24/2022/2022-Serie-A-Stats')
# %%
# Checking if our conection with the website is working or not
if html_page.status_code == 200:
    print('Ok!')
else:
    print('No conection')
# %%