from src.gmaps import Gmaps

star_it = '''Help us reach 850 stars, and we'll break the GMaps 120 limit, giving you 150+ to 250+ potential customers per search.
             Star us to make it happen ⭐! https://github.com/omkarcloud/google-maps-scraper/'''

queries = Gmaps.Cities.India("masjid")[0:100]
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