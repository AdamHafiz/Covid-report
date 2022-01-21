import requests
from bs4 import BeautifulSoup

def cleaning_xaxis(data):
    temp = (data[data.find("categories: ") + len("categories: "):])
    print(temp[:temp.find('"]')+2])

def cleaning_yaxis(data):
    temp = data[data.find("series: ") + len("series: "):]
    removed_script_tag = temp[:temp.find('responsive: {')-11]


    print(removed_script_tag[removed_script_tag.find('name'):removed_script_tag.find("',")])
    print(removed_script_tag[removed_script_tag.find('data: '):removed_script_tag.find("]")+1])


    removed_script_tag_second = removed_script_tag[removed_script_tag.find("]"):]
    removed_script_tag_second = removed_script_tag_second[removed_script_tag_second.find("name"):]


    print(removed_script_tag_second[removed_script_tag_second.find('name'):removed_script_tag_second.find("',")])
    print(removed_script_tag_second[removed_script_tag_second.find('data: '):removed_script_tag_second.find(']')+1])

URL = "https://www.worldometers.info/coronavirus/country/malaysia/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
result = soup.find_all('script')

wanted_number=[21,22,23,24,25]

for n in wanted_number:
    cleaning_xaxis(str(result[n]))
    cleaning_yaxis(str(result[n]))
