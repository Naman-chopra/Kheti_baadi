from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def data_from_esp(request):
    soil_type = request.POST.get('soil_type')
    crop_type = request.POST.get('crop_type')
    temp = request.POST.get('temp')
    humidity = request.POST.get('humidity')
    moisture = request.POST.get('moisture')
    potassium = request.POST.get('potassium')
    nitrogen = request.POST.get('nitrogen')
    phosphorous = request.POST.get('phosphorous')

