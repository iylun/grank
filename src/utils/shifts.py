from datetime import datetime
from json import dumps
from time import sleep

from utils.shared import data


def shifts(Client) -> None:
	"""A function which controls shifts.

	Args:
		username (str): The username of the account.
		config (dict): The dictionary version of the configuration file.
		cwd (str): The current working directory.
	"""
 
	while True:
		if (datetime.strptime(datetime.now().strftime("%x-%X"), "%x-%X") - datetime.strptime(Client.database["shifts"]["last active"], "%x-%X")).total_seconds() > Client.config["shifts"]["active"]:
			data[Client.username] = False
			Client.log("DEBUG", "Beginning sleep phase.")
			sleep(Client.config["shifts"]["passive"])
			data[Client.username] = True
			Client.log("DEBUG", "Beginning active phase.")
			Client.database["shifts"]["last active"] = datetime.now().strftime("%x-%X")
		
		Client.database_file.write(dumps(Client.database))

		cooldown = (datetime.strptime(datetime.now().strftime("%x-%X"), "%x-%X") - datetime.strptime(Client.database["shifts"]["last active"], "%x-%X")).total_seconds() - Client.config["shifts"]["active"]

		if cooldown > 0:
			sleep(cooldown)