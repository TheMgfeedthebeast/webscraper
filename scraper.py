

############################################################################################################################################################################################################
#WebCrawler the Dreadnought
############################################################################################################################################################################################################

#################################
#inporting all the nessecery packages
import time
from time import sleep
import os
import requests
#################################

#################################
#asks if the user want's to use this app if they want to it will automaticly istall all the pip packages
r = int(input("do you want to run webscraper? 1 for yes 2 to exit: "))#asks if they want to run
if r == 1: #fi  the user choose yes then run:
	os.system("pip install beautifulsoup4")#installing beautifulsoup4
	os.system("pip install google")#installing the google package for seacrh
	os.system("pip install tqdm")#installing tqdm
elif r == 2: #if the user choose to quit:
	print("you selected quit ):")#says its quitting
	sleep(5)#waits for 5 secs so the user can see the message
	exit()#quits using the exit command

from tqdm import tqdm#if the user did not quit after it has installed tqdm it will enable it

#################################

#################################
#creating the var "e" which has the value of none which applies to all the var's before use
e = None #creates e var with the value of none
numb1 = e#creates & sets var to none
n = e#creates & sets var to none
t = e#creates & sets var to none
s = e#creates & sets var to none
s1 = e#creates & sets var to none
leni = [e,e,e,e,e,e,e,e,e,e,]#creates & sets list to none
#################################

#################################
#
while t == e :#uses a while loop to make sure the user types a valid input
	t = int(input("please type either 1 or 2, 1 for query search, and 2 for config, in config you can change settings like how many websites to scan(not implimented only option 1 works)"))#asks for input
	print ("the type you chose: ",t)#shows the user its input
	if t == 1: #checks if the user goes strait to search 
		n = input("input qeury for search: " )#asks for the qeury to seacrh
		print ("the query you chose: ", n)#shows the query
	elif t == 2:#checks if it should rater config everything
		n = input("input name for search: " )#does the same as the privius if command since the config is not integrated
		print ("the query you chose: ", n)#does the same as the privius if command since the config is not integrated
#################################

#################################
#checks if the google package is working and installed
try:#tryes if not it will spit out an error by doing an except
    from googlesearch import search#atempts a search
except ImportError:#makes an except and error
    print("error the google packadge did not install correctly! ---- ABORT! ABORT! ABORT!")#prints an error to the user
    sleep(2)#sleeps for 2 sec
    print("quitting")#prints quitting
    sleep(1)#sleeps for 1 sec
    print(".")#prints a . just for graphics
    sleep(1)#sleeps for 1 sec
    print(".")#prints a . just for graphics
    sleep(1)#sleeps for 1 sec
    print(".")#prints a . just for graphics
    sleep(1)#sleeps for 1 sec
    exit()#quits using the exit command
#################################

#################################
#searcesand saving to a var while printing to the user
query = n #makes a qeury var for seacrh
for j in search(query, tld="co.in", num=30, stop=30, pause=2):#sets the search limit and searches
    print(j)#gives the user the list in terminal
    leni.append(j)#gives the list all the vars content for each run
#################################

#################################
#asks the user if they want to print the url list to a .txt doc
s = int(input("do you want to print out a txt with your responces? 1 for yes 2 for no: "))#ask the user if they want to make a doc with the url links
if s == 1:#if the user wants to print out a doc then:
	f = open("responces.txt","w+")#makes a doc and opens it
	f.write(j)#pastes content into file
#################################

#################################
#debug 
print(leni, "       this is the content if you want to downoald the code in the next func this message is just to verify and is for my self as a dev to debug :D")#output for debug
#################################

#################################
#asks if the user wants to scrape and if so downloads the websites
s1 = int(input("do you want to coppy all the code of the resolts in a txt file? 1 for yes 2 to quit: "))#
if s1 == 1:#checks if the user wants to download the urls if so then:
	for index, url in enumerate(leni, start=1):#taskes the urls form leni and indexes it for each one in a for loop
	    try:#tries to download it it does not work it will print an error
	        response = requests.get(url, stream=True)#checks the status of the websites
	        response.raise_for_status()#checks the status of the websites
	        total_length = int(response.headers.get('content-length', 0))#checks the lenght so they can give a progress bar
	        filename = f"content_{index}.html"# cannot comment the next lines srry but it basicly sets ut the progress bar
	        with open(filename, "wb") as file, tqdm(
	            desc=f"Downloading {url}",
	            total=total_length,
	            unit='B', unit_scale=True, unit_divisor=1024
	        ) as bar:
	            for data in response.iter_content(chunk_size=1024):
	                file.write(data)#checks ammot written & givges to var
	                bar.update(len(data))  # Update the progress bar

	        print(f"Content from {url} saved to {filename}")#saves the htmls
	    except requests.exceptions.RequestException as e:#if something goes wrong then make an except and then:
	        print(f"Error downloading content from {url}: {e}")#prints an error to the user since something is not quite right same on next line
	        print("error expected from your typing please try training your keyboard skils dumb*ssssss!!!!!!!!!! This is your fault I will not loop thru the code you mor*n, even more code to make for a incompitant user, thoght you were a poweruser for downloading random scripts from github and randomly haveing the correct version of python installed, I geuss you are using linux like me but you can't type lol! Lets stopp this rant now before I turn into steve from gn ")
#################################

#################################
#gets reddy to search for keywords then askes for a keword to search 
script_directory = os.path.dirname(os.path.abspath(__file__))#makes a list of files to search and makes a list of htmls to search and gives its dir/path
search_keyword = input("if you want to search what do you want to search for if you dont want to seacrh just quit: ")#asks the user for a keyword
def copy_lines_with_keyword(file_path, keyword, output_file_path):#makes a func that takes the "lines of keywords" with your search result in files and coppies it and makes the args dor the def
    lines_with_keyword = []#makes the var for later use
    with open(file_path, "r", encoding="utf-8") as file: #sets encoding
        for line in file:#makes a for loop  to check each line
            if keyword in line:#if the keyword is in a line then:
                lines_with_keyword.append(line)#makes a list with all the lines for later use, def is done!
    
    if lines_with_keyword:#if teh lines has the keyword then:
        with open(output_file_path, "a", encoding="utf-8") as output_file:#opens the file with the encoding ect
            output_file.write(f"--- Keyword found in {file_path} ---\n")#writes the file they found the keydord in
            output_file.writelines(lines_with_keyword)#pastes the line
            output_file.write("\n")#makes that file
            print(f"Lines with keyword from {file_path} copied to {output_file_path}")#tells the user in the terminal that it has found a keyword in the file and the path

output_file_path = os.path.join(script_directory, "lines_with_keyword.txt")#makes the file and joins the scr dir/path
for filename in os.listdir(script_directory):#for each filename then:
    if filename.endswith(".html"):#checks if it is html
        file_path = os.path.join(script_directory, filename)#makes the file and joins the scr dir/path
        copy_lines_with_keyword(file_path, search_keyword, output_file_path)#pastes the keywords dir/path in the doc
#################################


exit()#scripts done! quitting




#line 150 yay