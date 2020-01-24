# chol_analysis.py

def cholesterol_analysis():
	print("Cholesteerol Analysis")
	HDLinput = input("Enter test result: ")
	test_info = HDLinput.split("=")
	if test_info[0] == "HDL":
		HDL_analysis()
		result = check_HDL(int(chol_data[1]))
		print("The cholesterol level is {}.".format(result))
	elif test_info[0] == "LDL":
		LDL_analysis()
		result = check_HDL(int(chol_data[1]))
		print("The cholesterol level is {}.".format(result))


def interface():
	while True:
		print("Cholestreol Calculator")
		print("Options: ")
		print("  1 - Cholesterol Analysis")
		print("  9 - Quit")
		choice = input("Enter your option: ")
		if choice == '9':
			return
		elif choice == '1':
			cholesterol_analysis()

if __name__ == "__main__":
	interface()