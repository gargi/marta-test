import os
import json
import requests

api_key = os.environ["MartaApiKey"]

def main():
    station_name = input('Enter your station: ')

def get_train(station = "MIDTOWN STATION"):
    url = "http://developer.itsmarta.com/RealtimeTrain/RestServiceNextTrain/GetRealtimeArrivals?apikey={}"
    response = requests.get(url.format(api_key)).json()
    if station is not None:
      for arrival in response:
          if station.upper() in arrival['STATION']:
           output = "Direction : " + arrival['DIRECTION'] + " Destination : " + arrival['DESTINATION'] + " Waiting Time : " + arrival['WAITING_TIME']
           print output

if __name__ == '__main__':
	main()
