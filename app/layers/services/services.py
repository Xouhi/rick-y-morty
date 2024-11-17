# capa de servicio/lógica de negocio
import requests
from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user

def getAllImages(input=None):
    api_url = "https://rickandmortyapi.com/api/character/"
    response = requests.get(api_url)

    # Si la respuesta fue exitosa, procesamos los datos
    json_collection = []
    if response.status_code == 200:
        json_collection = response.json().get('results', [])
    else:
        print("Error al obtener datos de la API")
        return []

    # Convertimos los datos "crudos" en una lista de diccionarios (Cards)
    images = []
    for item in json_collection:
        card = {
            'name': item['name'],  # Nombre del personaje
            'status': item['status'],  # Estado del personaje
            'url': item['image'],  # URL de la imagen
            'last_location': item['location']['name'],  # Última ubicación
            'first_seen': item['origin']['name'],  # Fecha de creación del personaje
        }
        images.append(card)

    return images

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = '' # transformamos un request del template en una Card.
    fav.user = '' # le asignamos el usuario correspondiente.

    return repositories.saveFavourite(fav) # lo guardamos en la base.

# usados desde el template 'favourites.html'
def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = [] # buscamos desde el repositories.py TODOS los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
            card = '' # transformamos cada favorito en una Card, y lo almacenamos en card.
            mapped_favourites.append(card)

        return mapped_favourites

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.