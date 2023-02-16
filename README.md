# weatherapiapp

this is a simple flask application that gets the weather of cities. the user types in a city, and gets various details about the weather of that city. 

at first, when there's no city, it alerts the user of a lack of city.
![image](https://user-images.githubusercontent.com/89423596/219464205-732b0bcb-52d7-4200-908f-3db015ccc67d.png)

when the user enters a city, the weather information is shown below:

![image](https://user-images.githubusercontent.com/89423596/219464804-5af3dfcd-3ec8-4d29-869d-33faec8ee233.png)



to get it working:
  1. Get an api key from https://home.openweathermap.org
  2. navigate to the terminal where the project is stored, and activate the virtual encvironment "venv"
    --> venv\Scripts\activate or --> venv\Scripts\activate.bat
 
  3. install the required packages using the python package installer(pip or pip3[for mac]) from requirements.txt
    --> pip install -r requirements.txt
    
  4. on the terminal type ---> flask run 
