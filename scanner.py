#!/usr/bin/python3

#################################################################################
#                                                                               #
# Verison 1.0                                                                   #
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
import shodan
import time
import sys

######### Banner ##########

print("#" * 75)
print("\n")
print(" " * 30 + "Shodan Scanner")
print("\n")
print("#" * 75)
print("\n")

time.sleep(0.5)

def scanner():
	if os.path.exists("./api.txt"):
		with open("api.txt", "r") as file:
			api_key = file.readline()

	else:
		file = open("api.txt", "w+")
		api_key = input("Please enter a valid Shodan API Key:")
		file.write(api_key)
		print("\n" + "File written: ./api.txt")
		file.close()

	api = shodan.Shodan(api_key)
	time.sleep(0.4)

	limit = 10
	counter = 1

	print("\n")
	print("#" *75)
	print("\n")

	try:
		print("Checking Shodan API Key...")
		api.search("my_search")
		print ("API Key Authentication: SUCCESS..")
		my_search = input("What would you like to search? ")
		print("\n")
		counter = counter + 1
		for banner in api.search_cursor(my_search):
			print("#" * 25 + "\n")
			print("IP: " + (banner["ip_str"]))
			print("Port: " + str(banner["port"]))
			print("Organization: " + str(banner["org"]))
			print("Location: " + str(banner["location"]))
			print("Layer: " + (banner["transport"]))
			print("Domains: " + str(banner["domains"]))
			print("Hostnames: " + str(banner["hostnames"]))
			print("Banner Info: " + "\n" + "\n" + str(banner["data"]))
			print("Result: %s.  Search query: %s" % (str(counter), str(my_search)))
			print("\n")
			time.sleep(0.4)
			
			counter += 1
			if counter >= limit:
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
