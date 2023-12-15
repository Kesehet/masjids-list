from src.gmaps import Gmaps


queries = Gmaps.Cities.India("masjid")[200:300]
fields = [
   Gmaps.Fields.NAME, 
   Gmaps.Fields.MAIN_CATEGORY,
   Gmaps.Fields.ADDRESS,
   Gmaps.Fields.DETAILED_ADDRESS,
   Gmaps.Fields.IMAGES,
   Gmaps.Fields.LINK,
   Gmaps.Fields.COORDINATES
]


Gmaps.places(queries,fields=fields)