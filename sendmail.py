import yagmail
import json
from datetime import date

def send():
  with open("result.json", "r") as file:
      json_data = file.read()
  data = json.loads(json_data)

  world = data["world"]
  malaysia = data["malaysia"]


  yag = yagmail.SMTP("adamhafizswitch@gmail.com", "iixnapwiuecrmyfy")
  contents = [
      f"""
      Covid Report for {date.today()}
          
      Malaysia: 
      Total cases: {malaysia["total_cases"]["cases"]}
      Total loss: {malaysia["total_deaths"]["cases"]}
    
      Active cases(current, new, loss):
      {malaysia["active_cases"]["date"][0]}: {malaysia["active_cases"]["cases"][0]}, +{malaysia["daily_cases"]["cases"][0]}, -{malaysia["daily_deaths"]["cases"][0]}, 
      {malaysia["active_cases"]["date"][1]}: {malaysia["active_cases"]["cases"][1]}, +{malaysia["daily_cases"]["cases"][1]}, -{malaysia["daily_deaths"]["cases"][1]}, 
      {malaysia["active_cases"]["date"][2]}: {malaysia["active_cases"]["cases"][2]}, +{malaysia["daily_cases"]["cases"][2]}, -{malaysia["daily_deaths"]["cases"][2]}, 
      {malaysia["active_cases"]["date"][3]}: {malaysia["active_cases"]["cases"][3]}, +{malaysia["daily_cases"]["cases"][3]}, -{malaysia["daily_deaths"]["cases"][3]}, 
      {malaysia["active_cases"]["date"][4]}: {malaysia["active_cases"]["cases"][4]}, +{malaysia["daily_cases"]["cases"][4]}, -{malaysia["daily_deaths"]["cases"][4]}, 
      {malaysia["active_cases"]["date"][5]}: {malaysia["active_cases"]["cases"][5]}, +{malaysia["daily_cases"]["cases"][5]}, -{malaysia["daily_deaths"]["cases"][5]}, 
      {malaysia["active_cases"]["date"][6]}: {malaysia["active_cases"]["cases"][6]}, +{malaysia["daily_cases"]["cases"][6]}, -{malaysia["daily_deaths"]["cases"][6]}

      

      World:
      Total cases: {world["total_cases"]["cases"]}
      Total loss: {world["total_deaths"]["cases"]}

      Active cases:
      {world["active_cases"]["date"][0]}: {world["active_cases"]["cases"][0]}
      {world["active_cases"]["date"][1]}: {world["active_cases"]["cases"][1]}
      {world["active_cases"]["date"][2]}: {world["active_cases"]["cases"][2]}
      {world["active_cases"]["date"][3]}: {world["active_cases"]["cases"][3]}
      {world["active_cases"]["date"][4]}: {world["active_cases"]["cases"][4]}
      {world["active_cases"]["date"][5]}: {world["active_cases"]["cases"][5]}
      {world["active_cases"]["date"][6]}: {world["active_cases"]["cases"][6]}

  """
  ]


  yag.send("alifzulkifeli@gmail.com", "Covid-19 Daily Report", contents, attachments=['recoveryrate.png', 'deathrate.png'])
  yag.send("adamhafizswitch@gmail.com", "Covid-19 Daily Report", contents,attachments=['recoveryrate.png', 'deathrate.png'])
  # yag.send('izzat.ibtisyam@gmail.com', 'subject', contents)
