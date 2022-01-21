import requests
from bs4 import BeautifulSoup

def cleaning(data):
    x_axis = ""
    name1 = ""
    data1 = ""
    name2 = ""
    data2 = ""

    temp_x = data[data.find("categories: ") + len("categories: ") :]
    x_axis = temp_x[: temp_x.find('"]') + 2]

    temp_y = data[data.find("series: ") + len("series: ") :]
    removed_script_tag = temp_y[: temp_y.find("responsive: {") - 11]

    name1 = removed_script_tag[
        removed_script_tag.find("name") : removed_script_tag.find(",")
    ]
    data1 = removed_script_tag[
        removed_script_tag.find("data: ") : removed_script_tag.find("]") + 1
    ]

    removed_script_tag_second = removed_script_tag[removed_script_tag.find("]") :]
    removed_script_tag_second = removed_script_tag_second[
        removed_script_tag_second.find("name") :
    ]

    name2 = removed_script_tag_second[
        removed_script_tag_second.find("name") : removed_script_tag_second.find("',")
    ]
    if len(name2) > 0:
        data2 = removed_script_tag_second[
            removed_script_tag_second.find("data: ") : removed_script_tag_second.find(
                "]"
            )
            + 1
        ]
    print( x_axis, name1, data1, name2, data2)


URL = "https://www.worldometers.info/coronavirus/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
result = soup.find_all("script")

wanted_number = [19, 20, 21, 22]
x_axis_string = ""

# for n in wanted_number:
# x_axis_string = x_axis_string +'"arr'+ str(n) +'" :' + cleaning_xaxis(str(result[n])) + ","
cleaning(str(result[20]))

# x_axis_string = "{" + x_axis_string[:-2] + "]}"

with open("res.json", "w") as f:
    f.write(str(x_axis_string))
