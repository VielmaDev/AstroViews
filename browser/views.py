
from django.shortcuts import render, HttpResponse
import requests
import datetime

# Create your views here.

#---Imagen del día---

def get_imagen(request):

    URL_API="https://api.nasa.gov/planetary/apod?"

    try:
        params= {
            "api_key":"c2OYvrWfzSWPDRAburcCkTmIc0iKnAZk88xLwaVq",
            "date":"2024-05-20"
        }
        # Intenta realizar la solicitud GET a la API
        response = requests.get(URL_API, params=params)

        if response.status_code == 200:
            # se utiliza el método json() para extraer los datos en formato JSON de la respuesta y se almacenan en la variable productos
            today=response.json()

            url= today["url"]

            if today['media_type']=="image": 
                    with open ("imagen.jpg", "wb") as f:
                        f.write(requests.get(url).content)
        else:
            # En caso de un código de respuesta no exitoso, manejar de acuerdo a tus necesidades
            print(f"Error en la solicitud: {response.status_code}")
            today= []
    
    except requests.RequestException as e:
        # Manejar errores de solicitud, por ejemplo, problemas de red
        print(f"Error en la solicitud: {e}")
        today= []

    return render(request,'browser/index.html', {'today': today})



#---Buscador de imagen---
def imagen_query(request):
    
    params= {
        "api_key":"DEMO_KEY"
    }
    
    dates=request.GET['dates']
    params['date']=dates

    url=request.get("https//api.nasa.gov/planetary/apod", params=params)
    result=request.get(url)

    if result.status_code == 200:
        query= url.json()
        return render(request, 'browser/imagen.html', {"query": query})
    


            
           





   





   


       