# Shodan Scanner
**Verison Control:**

- Verison 1.2

    -Added Summary search to search for Top companies that run a service
    
    -Added different banner using pyfiglet library 
    
    -Added progress bar with tqdm library
    
    -Enhanced UI with better different color text 
    
    -Various bug fixes 

- Verison 1.1

    -Added Choice between Search, Hosts, and Scans

    -Cleaned code / bug fixes 

    -Added ImportError to Shodan Library Import

    -Removed limit variable / Need to add y or n input for this               
              
- Verison 1.0 

    -Initial Release
_____________________________________________________________________________________________


Shodan Scanner is a basic scanner of Shodan's API using an exisiting API key that is provided by...  https://account.shodan.io/

_____________________________________________________________________________________________

**To install:**

```
git clone https://github.com/trevorisenberg94/shodan_scanner.git
cd shodan_scanner
pip3 install -r requirements.txt
```
_____________________________________________________________________________________________

**How to Use:**

`./scanner.py` within the shodan_scanner dir

```



######################################################################
          ____  _               _             
         / ___|| |__   ___   __| | __ _ _ __  
         \___ \| '_ \ / _ \ / _` |/ _` | '_ \ 
          ___) | | | | (_) | (_| | (_| | | | |
         |____/|_| |_|\___/ \__,_|\__,_|_| |_|
                                              

                    ____                                  
                   / ___|  ___ __ _ _ __  _ __   ___ _ __ 
                   \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
                    ___) | (_| (_| | | | | | | |  __/ |   
                   |____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                          

######################################################################


Locating "./api.txt" file
100%|████████████████████████████| 1700861/1700861 [00:00<00:00, 4725867.19it/s]


File Located: SUCCESS


######################################################################


Checking Shodan API Key...
100%|████████████████████████████| 9610049/9610049 [00:01<00:00, 5848906.89it/s]


API Key Authentication: SUCCESS


######################################################################


Thank you for using Shodan Scanner!
To use this tool, please select one of the following...


1 = General Shodan Search
2 = Search a Specific Host's IP Address
3 = Scan an IP that may or may not be in Shodan DB
     WARNING:  This requires paid Shodan API Key
4 = Provide Summary for a specific service


Please choose? 
```

_____________________________________________________________________________________________

**Resources:**

https://developer.shodan.io/api

https://shodan.readthedocs.io/en/latest/

https://readthedocs.org/projects/shodan/downloads/pdf/latest/
