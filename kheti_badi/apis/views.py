from rest_framework.decorators import api_view
from rest_framework.response import Response
import model
import requests
import json

# import Request 

# @api_view(['POST'])
def data_from_esp(request):
    global Data 
    Data=request
    soil_type = request.get('soil_type')
    crop_type = request.get('crop_type')
    temp = request.get('temp')
    humidity = request.get('humidity')
    moisture = request.get('moisture')
    potassium = request.get('potassium')
    nitrogen = request.get('nitrogen')
    phosphorous = request.get('phosphorous')
    lister=[temp,humidity,moisture,soil_type,crop_type,nitrogen,potassium,phosphorous]
    print(lister)
    pred=model.predict(lister)
    print("The Recommended URL is ",pred)
    return pred


@api_view(['GET'])
def send_data_to_front(request):
    list={"potassium":80, "nitrogen":90,"phosphorous":90}
    return Response(list)


@api_view(['POST'])
def getFertilizer(request):
    farm_id=request.POST.get('farm_id')
    print(farm_id)
    dict={'soil_type':'sandy','temp':10,'crop_type':'maize','nitrogen':10,'potassium':10,'phosphorous':10,'humidity':10,'moisture':10}
    fert=data_from_esp(dict)
    return Response({'fert':fert})
@api_view(['GET'])

def rainfallStatus(request):
    api_key = "feb9b2de86f6d578ba83164f3854fdd6"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    city_name = "Patiala"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    
    response = requests.get(complete_url)
    

    x = response.json()
    x=x['weather']
    return Response(x['main'])
    


