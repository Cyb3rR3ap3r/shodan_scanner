#!/usr/bin/python3

#################################################################################
#                                                                               #
# Verison 1.2                                                                   #
#                                                                               #
# Changes from 1.1                                                              #
#    Added Summary search to search for Top companies that run a service        #
#    Added different banner using pyfiglet library                              #
#    Added progress bar with tqdm library                                       #
#    Enhanced UI with better different color text                               #
#    Various bug fixes                                                          #
#                                                                               #
# Furture Changes...                                                            #
#    Output to file                                                             #
#    Better Error Handling                                                      #
#    Help menu with common Shodan search filters                                #
#                                                                               #
# Developer: Trevor Isenberg                                                    #
# Date: 02/26/2020                                                              #
#                                                                               #
#################################################################################

import os
import time
import sys
from termcolor import colored

# Wrapped into try / except clause to provide error handling feedback
# pip3 install shodan
try:
	import shodan
except ImportError:
	print("Shodan library not found.  Please install prior to running script")
	sys.exit()

# pip3 install pyfiglet
try:
	import pyfiglet
except ImportError:
	print("pyliglet library not found.  Please install prior to running script")
	sys.exit()

# pip3 install tqdm
try:
	from tqdm import tqdm
except ImportError:
	print("tqdm library not found.  Please install prior to running script")
	sys.exit()


######### Banner ##########

ascii_banner1 = colored(pyfiglet.figlet_format("         Shodan"), "green")
ascii_banner2 = colored(pyfiglet.figlet_format("                   Scanner"),"green")
line = colored("#" * 70, "green")
banner_line = colored("#" * 70, "grey")

print("\n")
print("\n")
print(banner_line)
print(ascii_banner1)
print(ascii_banner2)
print(banner_line)
print("\n")

time.sleep(0.5)

def scanner():  # Main function for the scanner
	if os.path.exists("./api.txt"):  # If / Else stat for api key
		with open("api.txt", "r") as file:  # Open as read only if file exsists
			api_key = file.readline()
			print('Locating "./api.txt" file')
			time.sleep(0.3)
			for i in tqdm(range(int(170086))):
				pass
			time.sleep(0.3)
			print("\n")
			print("File Located: " + colored("SUCCESS", "green"))

	else:
		file = open("api.txt", "w+") # Create as Write+Read if file doesn't exist
		api_key = input("Please enter a valid Shodan API Key:")
		file.write(api_key)
		print("\n" + "File Created Successfully: ./api.txt")
		file.close()

	api = shodan.Shodan(api_key) # Initiates searches with api key above
	time.sleep(0.4)

	#limit = 10
	counter = 1

	FACETS = [                      # This List is for the summary option
		'org',                  # It will loop through the shodan results and grab
		'domain',               # each item value from this list
		'port',
		'asn',
		('country', 3),
	]
	FACETS_TITLES = {
		'org': 'Top 5 Organizations',         # This dictionary takes give the list
		'domain': 'Top 5 Domains',            # above a key and value, we we can print
		'port': 'Top 5 Ports',                # the value "Top 5 ...." and then loop
		'asn': 'Top 5 Autonomouse Systems',   # using the list to print out from result
		'country': 'Top 3 Countries',
	}

	print("\n")
	print(banner_line)
	print("\n")

	try:
		print("Checking Shodan API Key...")
		for i in tqdm(range(int(981004))):
				pass
		print("\n")
		test_connection = api.host("8.8.8.8")
		print ("API Key Authentication: " + colored("SUCCESS", "green"))
		print("\n")
		print(banner_line)
		print("\n")
		print(colored("Thank you for using Shodan Scanner!", "green"))
		print(colored("To use this tool, please select one of the following...", "green"))
		print("\n")
		print(colored("1 = General Shodan Search", "green"))
		print(colored("2 = Search a Specific Host's IP Address", "green"))
		#print(colored("3 = Scan an IP that may or may not be in Shodan DB", "green"))
		#print(colored("     WARNING:  This requires paid Shodan API Key", "red"))
		print(colored("3 = Provide Summary for a specific service", "green"))
		print("\n")
		my_choice = input("Please choose? ")

		if my_choice == "1":
			my_search = input("What would you like to search? ")
			results = api.search(my_search)
			# This calls Shodan.search which returns a dictionary of info
			# If you print(results), you  will see all info returned from shodan
			time.sleep(0.5)
			print("\n")

			counter = counter + 1
			for result in results['matches']: # Here we are looping through the
							  # dictionary we called from shodan
							  # to display only the info we want
				print(line + "\n")
				print("IP: " + (colored(result["ip_str"], "green")))
				print("Port: " + str(colored(result["port"], "green")))
				print("Organization: " + str(colored(result["org"], "green")))
				print("Location: " + str(colored(result["location"], "green")))
				print("Layer: " + (colored(result["transport"], "green")))
				print("Domains: " + str(colored(result["domains"], "green")))
				print("Hostnames: " + str(colored(result["hostnames"], "green")))
				print("Data: " + "\n" + str(colored(result["data"], "blue")))
				#print("Result: %s.  Search query: %s" % (str(colored(counter, "green")), str(colored(my_search), "green")))
				#print("Result: %s.  Search Query: %s." % (str(colored(counter), "green"), str(my_search)))
				print("Result: " + (colored(counter, "green")) + "  Search Query: " + (colored(my_search, "green")))
				print("\n")
				time.sleep(0.4)

				counter += 1
				#if counter >= limit:
					#exit()
		elif my_choice == "2":
			my_host = input("What is the host IP? ")
			results = api.host(my_host)
			time.sleep(0.5)
			print("\n")

			for item in results['data']:
				print(line + "\n")
				print("IP: " + (colored(item["ip_str"], "green")))
				print("Port: " + str(colored(item["port"], "green")))
				print("Organization: " + str(colored(item["org"], "green")))
				print("Location: " + str(colored(item["location"], "green")))
				print("Layer: " + (colored(item["transport"], "green")))
				print("Domains: " + str(colored(item["domains"], "green")))
				print("Hostnames: " + str(colored(item["hostnames"], "green")))
				print("Data: " + "\n" + str(colored(item["data"], "blue")))
				print("\n")
				time.sleep(0.4)


		elif my_choice == "3":
			my_summary = input("What service would you like a summary for? ")
			result = api.count(my_summary, FACETS) # Need to add argv for FACETS list
							       # so it will output the values
							       # within list
			time.sleep(0.5)
			print("\n")
			print("Summary Infomation:")
			print("Query: " + my_summary)
			print("Total Results: " + str(result['total']))
			for facet in result['facets']:
				print("\n")
				print(FACETS_TITLES[facet])

				for item in result['facets'][facet]:
					print(colored("%s: %s ", "green") % (item["value"], item["count"]))

		else:
			print("Invalid entry.  Exiting..")
			exit()


	except KeyboardInterrupt:
		print("\n")
		print("User Interruption Detected..")
		time.sleep(0.5)
		sys.exit(1)

	except shodan.APIError as error:
		print((colored(" Error: ", "red")))
		error1 = str(error)   # Need to convert "error" into string for the if/else
				      #	statment to work
		print(error1)
		print("\n")
		if (error1 == "Invalid API key"):
			file = open("api.txt", "w+")
			api_key = input("Please enter a valid Shodan API Key:")
			file.write(api_key)
			print("\n" + "File written: ./api.txt")
			file.close()
			time.sleep(1)
			scanner()
		else:
			print("Exiting...")
			sys.exit()

######### Main ##########

if __name__ == "__main__":
	scanner()
