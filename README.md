# Creating a Real Time Weather App in Flask Using Python requests and geocoder
This is the complete source code of my article on Medium: <br>
https://medium.com/li-ting-liao-tiffany/creating-a-real-time-weather-app-in-flask-using-python-requests-and-geocoder-f6a2be3f8b31

## What I’m going to make and Why I’m doing it
This is my hands-on project in which I’ll use Flask to create a weather app and will be using Open weather Data API of the Taiwan Government Central Weather Bureau 中央氣象局 with Python requests to get the data.

## Environment used in this project
I'm using Python3 in VS code.

## Skills used in this project
* Create a simple web application with flask.
* Use python decorator to create route() which will tell Flask what URL should trigger our function.
* Request data from external API with request module.
* Get current location’s latitude and longitude with geocoder module.
* Find the nearest weather station by calculating the distance of each weather station and my current location.
* Use render_template function to pass data to a designed html structure.
* Display the result on browser.

## Notes for files
* weather_final_main.py: for flask web app
* weather.html: to display on browser
