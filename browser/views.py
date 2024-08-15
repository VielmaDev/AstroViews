
from django.shortcuts import render, HttpResponse
import requests
from datetime import date


# Create your views here.

#---Imagen del día (fecha actual)---

def today(request):

    URL_API="https://api.nasa.gov/planetary/apod?"
    now=date.today()

    try:
        params= {
            "api_key":"c2OYvrWfzSWPDRAburcCkTmIc0iKnAZk88xLwaVq",
            "date": now,
            #"date":"2024-08-09",
        }
        # Intenta realizar la solicitud GET a la API
        response = requests.get(URL_API, params=params)

        if response.status_code == 200:
            # se utiliza el método json() para extraer los datos en formato JSON de la respuesta y se almacenan en la variable productos
            today=response.json()

            #url= today["url"]
            #if today['media_type']=="image": 
                    #with open ("image.jpg", "wb") as f:
                        #f.write(requests.get(url).content)
        else:
            # En caso de un código de respuesta no exitoso, manejar de acuerdo a tus necesidades
            #print(f"Error en la solicitud: {response.status_code}")
            today= []
    
    except requests.RequestException as e:
        # Manejar errores de solicitud, por ejemplo, problemas de red
        #print(f"Error en la solicitud: {e}")
        today= []

    return render(request,'browser/index.html', {'today': today})

#---Buscador de imagen---
def browser_set(request):

    URL_API="https://api.nasa.gov/planetary/apod?"
    date= request.GET["Fecha"]
    
    params= {
        "api_key":"c2OYvrWfzSWPDRAburcCkTmIc0iKnAZk88xLwaVq",
        "date": date,
    }

    # Intenta realizar la solicitud GET a la API
    response = requests.get(URL_API, params=params)

    if response.status_code==200:
        # se utiliza el método json() para extraer los datos en formato JSON de la respuesta y se almacenan en la variable productos
        query=response.json()
        return render(request, 'browser/index.html', {'query': query})
    else:

        today=date.today()

        params={
            "api_key":"c2OYvrWfzSWPDRAburcCkTmIc0iKnAZk88xLwaVq",
            "date": today,
        }

        # Intenta realizar la solicitud GET a la API
        response = requests.get(URL_API, params=params)
        now=response.json()
        return render(request, 'browser/index.html', {'now': now})






            
           





   





   


       