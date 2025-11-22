from bs4 import BeautifulSoup
import requests

link = "https://www.wsj.com/"

request = requests.get(link)
contents = request.content
soup = BeautifulSoup(contents, "html.parser")

#print(soup.prettify())
headlines = soup.find_all('h2', class_ = 'WSJTheme--headline--unZqjb45 reset WSJTheme--heading-3--2z_phq5h typography--serif-display--ZXeuhS5E')

for i in range(len(headlines)):
    print(headlines[i].text)
