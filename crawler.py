import requests
from bs4 import BeautifulSoup

#Function to crawl through the URLs inside a URL
def webcrawler(url):
    if not(url and url.strip()):          #condition to check if entered input is a valid URL.
        print("Please enter a valid URL")
    else:
        print(url)
        reqs = requests.get(url)          #Using Requests package to get the HTML content of a URL entered.
        soup = BeautifulSoup(reqs.text, 'html.parser') #Using BS4 to parse throught the HTML content.

        for link in soup.find_all('a'):    #iterating through the parsed HTML content to look for hyperlinks.
            if link.get('href') is None:   #Condition to check if the HREF content is None.
                pass
            else:
                if "https" in link.get('href'):    #Condition to check if the HREF contains https.
                    print ("    "+link.get('href'))
                elif "http" in  link.get('href'):   #Condition to check if the HREF contains http.
                    print ("    "+link.get('href'))

while True:                                        #Creating a loop to enter the input until a stopping condition is met.
        try:
            x=input("Enter the URL:")
            webcrawler(x)                         #Invoking the webcrawler function and passing the input to it.
        except Exception:                            #Stopping condition if user hits ENTER as input.
            print "You are done with Execution :) "
            break
