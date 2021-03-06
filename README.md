# Rescale_Backend_Assignment

I have developed the WebCrawler in Python. Below are the steps needed before executing or to execute the program.

**Running the program on Linux terminal:**

**Once you open the linux terminal, become the root user using the following commands:**

sudo su

cd

**After becoming the root user, install python, pip, bs4, requests using the below commands:**

yum install python python-pip -y

pip install bs4

pip install requests

**Check the versions of python and pip:**

python --version

**Output:** Python 2.7.18

pip --version

**Output:** pip 9.0.3 from /usr/lib/python2.7/site-packages (python 2.7)

**Cloning the application from Git:**

yum install git -y

git --version

**Output:** git version 2.23.3

git clone https://github.com/DivyaMounikaKalluru/Rescale_Backend_Assignment.git

ls -la -> to check the list of all the files

cd Rescale_Backend_Assignment

ls -la (you can see crawler.py file in our Repo, It is the one which contains the code of our WebCrawler)

**Executing this crawler.py file that is in Rescale_Backend_Assignment Repository using the command:**

python crawler.py

**Providing the input:**

Once the program is executed, it will ask for the URL saying **Enter the URL:**

If no URL provided and the user just hits enter, It will prompt - **You are done with Execution :)**

![image](https://user-images.githubusercontent.com/71857062/110062770-e430aa80-7d37-11eb-9a18-a91fc6f22141.png)

If the input provided by you is just '', "", ' ', " ", '  ', "  ", i.e., including nothing or spaces in between the quotes without any URL will prompt - **Please enter a valid URL**

![image](https://user-images.githubusercontent.com/71857062/110063021-5f925c00-7d38-11eb-98eb-761fb4b7b4ca.png)

If the URL enclosed in single quotes or double quotes is provided, It will show all the URLs along with the URL that is visited.

All the visited URLs are printed without any indentation, all the URLs found on that page will be printed with one indentation.

![image](https://user-images.githubusercontent.com/71857062/110063190-a97b4200-7d38-11eb-8afb-59eef241d7c5.png)

![image](https://user-images.githubusercontent.com/71857062/110219480-79918300-7e8d-11eb-9f12-8910c02e3d91.png)

**URL can be:**

'https://linkedin.com' or "https://linkedin.com"

'https://facebook.com' or "https://facebook.com"

or any other absolute URL (https or http)

To stop the loop, I have implemented a stopping condition, i.e., when the program prompts you for the input and when you press enter, the iteration will terminate.

You can provide any URL (http and https) as input enclosed in either single or double quotes.

The results will be similar to the screenshots I have included.

**Note** - I am using python package here not python3.

So, install python package using the commands I included and execute the program.
