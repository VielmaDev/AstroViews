
from django.shortcuts import render
import requests
from datetime import date


# Create your views here.
#---Imagen del día (fecha actual)---

def today(request):

    now=date.today()
    URL_API="https://api.nasa.gov/planetary/apod?"
    
    try:
        params= {
            "api_key":"c2OYvrWfzSWPDRAburcCkTmIc0iKnAZk88xLwaVq",
            "date": now,
        }
        # Intenta realizar la solicitud GET a la API
        response = requests.get(URL_API, params=params)

        if response.status_code == 200:
            # se utiliza el método json() para extraer los datos en formato JSON de la respuesta 
            query=response.json()

        else:
            # En caso de un código de respuesta no exitoso
            query=['No se han publicado imagenes el día de hoy']
    
    except requests.RequestException as e:
        # Manejar errores de solicitud
        query= ['Error en solicitud :{e}']

    return render(request,'browser/index.html', {'query': query})


#---Buscador de imagen---
def browser_set(request):

    URL_API="https://api.nasa.gov/planetary/apod?"

    try:
        params= {
            "api_key":"c2OYvrWfzSWPDRAburcCkTmIc0iKnAZk88xLwaVq",
            "date":request.GET["date"],
        }

        # Intenta realizar la solicitud GET a la API
        response = requests.get(URL_API, params=params)

        if response.status_code==200:
            # se utiliza el método json() para extraer los datos en formato JSON de la respuesta 
            query=response.json()
        else:
            query=['No se encontraron resultados asociados a la consulta']
    
    except requests.RequestException as e:
        query= ['Error en solicitud :{e}']

    return render(request,'browser/index.html', {'query': query})



    






            
           





   





   


       