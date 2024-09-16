
from django.shortcuts import render
import requests
from datetime import date


# Create your views here.
#---Imagen del día (fecha actual)---

def today(request):

    #fecha actual tomada del servidor
    now=date.today()

     #API APOD que permite consultar la imagen del día publicada por la NASA
    URL_API="https://api.nasa.gov/planetary/apod?"
    
    try:
        #parámetros de busqueda
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
             #si no se encuentra resultados
            query=[]

    #excepción de error al cargar el sitio web
    except requests.RequestException as e:
        query= []

    #retorno de respuesta a el sitio web
    return render(request,'browser/index.html', {'query': query})


#---Buscador de imagen---
def browser_set(request):

    #API APOD que permite consultar la imagen del día publicada por la NASA
    URL_API="https://api.nasa.gov/planetary/apod?"

    try:
        #parámetros de busqueda
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
            #si no se encuentra resultados
            query=[]

    #excepción de error al cargar el sitio web
    except requests.RequestException as e:
        query= ['{e}']

    #retorno de respuesta a el sitio web
    return render(request,'browser/index.html', {'query': query})



    






            
           





   





   


       