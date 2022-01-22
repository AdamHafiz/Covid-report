import yagmail

date = 0

yag = yagmail.SMTP('adamhafizswitch@gmail.com', 'iixnapwiuecrmyfy')
contents = [f"""<body>
		<h1>Covid Report for {date}</h1>
		<h2>asdas</h2>
	</body>"""]
yag.send('alifzulkifeli@gmail.com', 'subject', contents)
# yag.send('alifzulkifeli@gmail.com', 'subject', contents)