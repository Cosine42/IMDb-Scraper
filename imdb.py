import requests
from bs4 import BeautifulSoup as bs

# getting the movie name as input
st=input()
st=st.replace(" ","+")

# searching the movie
res = requests.get("https://www.imdb.com/find?s=tt&q="+st)
res.raise_for_status()
soup = bs(res.text,'html.parser')

# fetching the best matched movie name
elems = soup.select(".findResult.odd>.result_text>a")
title = elems[0]['href']

# opening the title's main page
res = requests.get("https://www.imdb.com"+title)
soup = bs(res.text,'html.parser')
res.raise_for_status()

# fetching the summary
summary = soup.select('.summary_text')[0].text.strip()

# the IMDb rating
rating = soup.select('.ratingValue')[0].text.strip()

# name of director
director = soup.select('.credit_summary_item')[0].text.strip()

# printing the details
print("IMDb Rating: "+rating)
print("\nSummary:\n"+summary)
print('\n'+director)
5
# printing the meta score
elem = soup.select('.metacriticScore')
if len(elem)>0:
    meta = elem[0].text.strip()
    print("\nMetascore: "+meta)



