from urllib import response
import requests
from bs4 import BeautifulSoup
# https://www.startupjobs.cz/
# pip install bs4
#url = "https://api.github.com/user"
url = "https://www.expats.cz/jobs/offers/it-itc"
#url = "https://twitter.com/search?q=python"
response = requests.get(url)
"""
response.raise_for_status()

with open ("soubor.html", "wb") as input:
    input.write(response.content)
"""

soup = BeautifulSoup(response.content,"html.parser") # "html.parser"

main_content = soup.find(id="jobs-index")

header = main_content.find("div",class_="list-header")

#print(type(header))
#print(header.prettify())

anchor_text = header.find("a").text
#print(anchor_text)

list_of_jobs = soup.find(class_="job-list")

all_jobs = list_of_jobs.find_all("article")

for job in all_jobs:
    anchor = job.find("h3").find("a")
    print(anchor.text)
    print(anchor["href"])