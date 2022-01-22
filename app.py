import json
import os
import matplotlib.pyplot as plt
from numpy import append
import seaborn as sns


def generate_malaysia_report():
    with open("malaysia.json", "r") as file:
        json_data = file.read()

    data = json.loads(json_data)
    data_total_cases = data["item21"]
    data_daily_cases = data["item22"]
    data_active_cases = data["item23"]
    data_total_deaths = data["item24"]
    data_daily_deaths = data["item25"]

      
    temp_date = []
    temp_data = []
    temp_daily_cases_date = []
    temp_daily_cases = []
    temp_daily_deaths_date = []
    temp_daily_deaths = []
    for n in range(7):
        temp_date.append(str(data_active_cases["x_axis"][-1-n]))
        temp_data.append(str(data_active_cases["data1"][-1-n]))
        temp_daily_cases_date.append(str(data_daily_cases["x_axis"][-1-n]))
        temp_daily_cases.append(str(data_daily_cases["data1"][-1-n]))
        temp_daily_deaths_date.append(str(data_daily_deaths["x_axis"][-1-n]))
        temp_daily_deaths.append(str(data_daily_deaths["data1"][-1-n]))


    return(
        '{"malaysia":{"total_cases": {"date":"'
        + data_total_cases["x_axis"][-1]
        + '","cases":'
        + str(data_total_cases["data1"][-1])
        + '},"total_deaths": {"date":"'
        + data_total_deaths["x_axis"][-1]
        + '","cases":'
        + str(data_total_deaths["data1"][-1])
        + '},"active_cases":{"date":'
        + str(temp_date)
        + ',"cases":'
        + str(temp_data)
        + '},"daily_cases":{"date":'
        + str(temp_daily_cases_date)
        + ',"cases":'
        + str(temp_daily_cases)
        + '},"daily_deaths":{"date":'
        + str(temp_daily_deaths_date)
        + ',"cases":'
        + str(temp_daily_deaths)
        + " }}}"
    )
  


def generate_world_report():
    with open("world.json", "r") as file:
        json_data = file.read()

    data = json.loads(json_data)
    data_active_cases = data["item19"]
    data_deathrate = data["item20"]
    data_total_cases = data["item21"]
    data_total_deaths = data["item22"]

    generate_graph(data_deathrate["x_axis"],data_deathrate["data2"],"recoveryrate" )
    generate_graph(data_deathrate["x_axis"],data_deathrate["data1"],"deathrate" )

    temp_date = []
    temp_data = []
    for n in range(7):
        temp_date.append(str(data_active_cases["x_axis"][-1-n]))
        temp_data.append(str(data_active_cases["data1"][-1-n]))

    return(
        '{"world":{"total_cases": {"date":"'
        + data_total_cases["x_axis"][-1]
        + '","cases":'
        + str(data_total_cases["data1"][-1])
        + '},"total_deaths": {"date":"'
        + data_total_deaths["x_axis"][-1]
        + '","cases":'
        + str(data_total_deaths["data1"][-1])
        + '},"active_cases":{"date":'
        + str(temp_date)
        + ',"cases":'
        + str(temp_data)
        + " }}}"
    )


def generate_graph(x, y, name):
    sns.set_theme(style="darkgrid")
    swarm_plot = sns.lineplot(x, y)
    fig = swarm_plot.get_figure()
    fig.savefig(name + ".png")
    plt.plot(x, y)
    plt.clf()


# generate_malaysia_report()
# generate_world_report()

with open("result.json", "w") as f:
    f.write(str())

def main():
    world = generate_world_report()
    malaysia = generate_malaysia_report()
    with open("result.json", "w") as f:
      f.write(str(world[:-1] + "," + malaysia[1:] ).replace("'", '"'))  



main()
