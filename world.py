import requests
from bs4 import BeautifulSoup


def cleaning(data):
    x_axis = ""
    name1 = ""
    data1 = ""
    name2 = ""
    data2 = ""

    temp_x = data[data.find("categories: ") + len("categories: ") :]
    x_axis = '"x_axis":' + temp_x[: temp_x.find('"]') + 2]

    temp_y = data[data.find("series: ") + len("series: ") :]
    removed_script_tag = temp_y[: temp_y.find("responsive: {") - 11]

    name1 = removed_script_tag[
        removed_script_tag.find("name")
        + len("name") : removed_script_tag.find("',")
        + 1
    ]
    name1 = '"name1"' + name1.replace("'", '"')

    data1 = removed_script_tag[
        removed_script_tag.find("data: ")
        + len("data") : removed_script_tag.find("]")
        + 1
    ]
    data1 = '"data1"' + data1

    removed_script_tag_second = removed_script_tag[removed_script_tag.find("]") :]
    removed_script_tag_second = removed_script_tag_second[
        removed_script_tag_second.find("name") :
    ]

    name2 = removed_script_tag_second[
        removed_script_tag_second.find("name")
        + len("name") : removed_script_tag_second.find(",")
    ]

    if len(name2) > 0:

        name2 = '"name2"' + name2.replace("'", '"')
        data2 = removed_script_tag_second[
            removed_script_tag_second.find("data: ")
            + len("data") : removed_script_tag_second.find("]")
            + 1
        ]
        data2 = '"data2"' + data2
        return (
            "{" + x_axis + "," + name1 + "," + data1 + "," + name2 + "," + data2 + "}"
        )

    # return "{" +  x_axis + "," + name1 + "," + data1 +  "}"
    return "{" + x_axis + "," + name1 + "," + data1 + "}"


URL = "https://www.worldometers.info/coronavirus/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
result = soup.find_all("script")

wanted_number = [19, 20, 21, 22]
data_string = ""

for n in wanted_number:
    cleaned_data = '"item' + str(n) + '":' + cleaning(str(result[n]))
    data_string = data_string + "," + cleaned_data

# x_axis_string = "{" + x_axis_string[:-2] + "]}"

with open("world.json", "w") as f:
    f.write(str("{" + data_string[1:] + "}"))
