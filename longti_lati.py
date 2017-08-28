import urlib.requests

res = requests.get('https://parks.ny.gov/parks/130/maps.aspx')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text,"lxml")
longti = noStarchSoup.select("#desc-col > div")[3].getText().strip('Longitude ')
lati = noStarchSoup.select("#desc-col > div")[2].getText().strip('Latitude ')
