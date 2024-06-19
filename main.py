from bs4 import BeautifulSoup
import pandas as pd
import requests
#-----------------URL----------------------
base_url = "https://www.billboard.com/charts/hot-100"
user_in = input("Enter date (YYYY-MM-DD): ")
final_url = base_url + '/' + user_in
response = requests.get(url=final_url)
html_doc=response.text

#---------------Soup----------------------
song_final=[]
soup=BeautifulSoup(html_doc, 'html.parser')
div_tags=soup.find_all("div",class_="o-chart-results-list-row-container")
for i in div_tags:
    temp=i.find("h3").string.strip()
    song_final.append(temp)

print(song_final)

#=========Spotify Auth=========
