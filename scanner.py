#!/usr/bin/python3

#################################################################################
#                                                                               #
# Verison 1.1                                                                   #
#                                                                               #
# Changes from 1.0                                                              #
#    Added Choice between Search, Hosts, and Scans                              #
#    Cleaned code / bug fixes                                                   #
#    Added ImportError to Shodan Library Import                                 #
#    Removed limit variable / Need to add y or n input for this                 # 
#                                                                               #
# Furture Changes...                                                            #
#    Output to file                                                             #
#    More Search Results                                                        #
#    Show more than 1 port                                                      #
#    Better Error Handling                                                      #
#    Better Banner                                                              #
#    Help menu with common Shodan search filters                                #
#    Use different color text / Better UI                                       #
#                                                                               #
# Developer: Trevor Isenberg                                                    #
# Date: 02/26/2020                                                              #
#                                                                               #
#################################################################################                

import os
import time
import sys

# Wrapped into try / except clause to provide error handling feedback
try:
	import shodan
except ImportError:
	print("Shodan library not found.  Please install prior to running script")

######### Banner ##########

print("#" * 75)
print("\n")
print(" " * 30 + "Shodan Scanner")
print("\n")
print("#" * 75)
print("\n")

time.sleep(0.5)

def scanner():  # Main Defintion for the scanner
	if os.path.exists("./api.txt"):  # If / Else stat for api key
		with open("api.txt", "r") as file:
			api_key = file.readline()

	else:
		file = open("api.txt", "w+")
		api_key = input("Please enter a valid Shodan API Key:")
		file.write(api_key)
		print("\n" + "File written: ./api.txt")
		file.close()

	api = shodan.Shodan(api_key) # Initiates searches with api key above
	time.sleep(0.4)

	#limit = 10
	counter = 1

	print("\n")
	print("#" *75)
	print("\n")

	try:
		print("Checking Shodan API Key...")
		print ("API Key Authentication: SUCCESS..")
		print("1 = Search, 2 = Host, 3 = Scan")
		my_choice = input("Please choose? ")

		if my_choice == "1":
			my_search = input("What would you like to search? ")
			results = api.search(my_search)
			time.sleep(0.5)
			print("\n")

			counter = counter + 1
			for result in results['matches']:
				print("#" * 75 + "\n")
				print("IP: " + (result["ip_str"]))
				print("Port: " + str(result["port"]))
				print("Organization: " + str(result["org"]))
				print("Location: " + str(result["location"]))
				print("Layer: " + (result["transport"]))
				print("Domains: " + str(result["domains"]))
				print("Hostnames: " + str(result["hostnames"]))
				print("Data: " + "\n" + str(result["data"]))
				print("Result: %s.  Search query: %s" % (str(counter), str(my_search)))
				print("\n")
				time.sleep(0.4)
			
				counter += 1
				#if counter >= limit:
					#exit()
		elif my_choice == "2":
			my_host = input("What is host IP? ")
			results = api.host(my_host)
			time.sleep(0.5)
			print("\n")

			for item in results['data']:			
				print("#" * 75 + "\n")
				print("IP: " + (item["ip_str"]))
				print("Port: " + str(item["port"]))
				print("Organization: " + str(item["org"]))
				print("Location: " + str(item["location"]))
				print("Layer: " + (item["transport"]))
				print("Domains: " + str(item["domains"]))
				print("Hostnames: " + str(item["hostnames"]))
				print("Data: " + "\n" + str(item["data"]))
				print("\n")
				time.sleep(0.4)

		elif my_choice == "3":
			my_scan = input("Who would you like to scan? ")
			result = api.scan(my_scan)
			time.sleep(0.5)
			print(result)

		else:
			exit()
		

	except KeyboardInterrupt:
		print("\n")
		print("User Interruption Detected..")
		time.sleep(0.5)
		sys.exit(1)

	except shodan.APIError as error:
		print("Error: %s " % (error))
		print("\n")
		error1 = str(error)   # Need to convert "error" into string for the if/else stat to work
		print(error1)
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
