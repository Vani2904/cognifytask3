import re

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def check(email):


	if(re.fullmatch(pattern , email)):
		print("Valid Email")

	else:
		print("Invalid Email")


if __name__ == '__main__':


	email = "vani@gmail.com"
	check(email)

	email = "sasi@gmail"
	check(email)

	email = "NaNi326.com@gmail.com"
	check(email)

