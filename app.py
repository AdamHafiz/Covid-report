import json
import yagmail
import os
import matplotlib.pyplot as plt
import seaborn as sns


def generate_malaysia_report():
  with open('malaysia.json', "r") as file:
    json_data = file.read()

  data = json.loads(json_data)
  data_total_cases = data["item21"]
  data_daily_cases = data["item22"]
  data_active_cases = data["item23"]
  data_total_deaths = data["item24"]
  data_daily_deaths = data["item25"]


  print(data_total_cases["name1"], data_total_cases["x_axis"][-1], data_total_cases["data1"][-1])
  for n in range(7):
    print(data_daily_cases["name1"], data_daily_cases["x_axis"][-(n+1)], data_daily_cases["data1"][-(n+1)])
  print(data_active_cases["name1"], data_active_cases["x_axis"][-1], data_active_cases["data1"][-1])
  print(data_total_deaths["name1"], data_total_deaths["x_axis"][-1], data_total_deaths["data1"][-1])
  for n in range(7):
    print(data_daily_deaths["name1"], data_daily_deaths["x_axis"][-(n+1)], data_daily_deaths["data1"][-(n+1)])


def generate_world_report():
  with open('world.json', "r") as file:
    json_data = file.read()

  data = json.loads(json_data)
  data_active_cases = data["item19"]
  data_deathrate = data["item20"]
  data_total_cases = data["item21"]
  data_total_deaths = data["item22"]
  
  print(data_total_cases["name1"], data_total_cases["x_axis"][-1], data_total_cases["data1"][-1])

  for n in range(7):
    print(data_active_cases["name1"], data_active_cases["x_axis"][-1], data_active_cases["data1"][-1])

  print(data_total_deaths["name1"], data_total_deaths["x_axis"][-1], data_total_deaths["data1"][-1])

  for n in range(7):
    print(data_deathrate["name1"], data_deathrate["x_axis"][-(n+1)], data_deathrate["data1"][-(n+1)])
  

  generate_graph(data_deathrate["x_axis"],data_deathrate["data2"],"recoveryrate" )
  generate_graph(data_deathrate["x_axis"],data_deathrate["data1"],"deathrate" )


def generate_graph(x,y,name):
  sns.set_theme(style="darkgrid")
  swarm_plot = sns.lineplot(x, y)
  fig = swarm_plot.get_figure()
  fig.savefig(name + ".png") 
  plt.plot(x,y)
  plt.clf()


# generate_malaysia_report()
generate_world_report()
# generate_graph()

def generate_result():
  generate_world_report

with open("result.json", "w") as f:
    f.write(str())

#yag = yagmail.SMTP('adamhafizswitch@gmail.com', 'iixnapwiuecrmyfy')
#contents = ['This is the body, and here is just text http://somedomain/image.png',
#             'You can find an audio file attached.', '/local/path/song.mp3']
#yag.send('adamhafizswitch@gmail.com', 'subject', contents)