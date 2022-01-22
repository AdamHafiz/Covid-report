import yagmail
import json
from datetime import date


with open("result.json", "r") as file:
    json_data = file.read()
data = json.loads(json_data)

world = data["world"]
malaysia = data["malaysia"]


yag = yagmail.SMTP('adamhafizswitch@gmail.com', 'iixnapwiuecrmyfy')
contents = [f"""<body style="line-height: 0.5;">
  <h2>Covid Report for {date.today()}</h2>
  <h3>Malaysia</h3>
  <table>
  <p>Total cases: {malaysia["total_cases"]["cases"]}</p>

  <p>Total loss: {malaysia["total_deaths"]["cases"]}</p>
  <th> Active cases:</th>
    <tr>
      <td>{malaysia["active_cases"]["date"][0]}</td>
      <td>{malaysia["active_cases"]["cases"][0]}</td>
    </tr>
    <tr>
      <td>{malaysia["active_cases"]["date"][1]}</td>
      <td>{malaysia["active_cases"]["cases"][1]}</td>
    </tr>
    <tr>
      <td>{malaysia["active_cases"]["date"][2]}</td>
      <td>{malaysia["active_cases"]["cases"][2]}</td>
    </tr>
    <tr>
      <td>{malaysia["active_cases"]["date"][3]}</td>
      <td>{malaysia["active_cases"]["cases"][3]}</td>
    </tr>
    <tr>
      <td>{malaysia["active_cases"]["date"][4]}</td>
      <td>{malaysia["active_cases"]["cases"][4]}</td>
    </tr>
    <tr>
      <td>{malaysia["active_cases"]["date"][5]}</td>
      <td>{malaysia["active_cases"]["cases"][5]}</td>
    </tr>
    <tr>
      <td>{malaysia["active_cases"]["date"][6]}</td>
      <td>{malaysia["active_cases"]["cases"][6]}</td>
    </tr>
  </table>

  <h3>World</h3>
  <p>Total cases: <span>{world["total_cases"]["cases"]}</span></p>
  <p>Total loss: <span>{world["total_deaths"]["cases"]}</span></p>

</body>"""]


yag.send('alifzulkifeli@gmail.com', 'subject', contents)
yag.send('adamhafizswitch@gmail.com', 'subject', contents)