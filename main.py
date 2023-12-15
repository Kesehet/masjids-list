from src.gmaps import Gmaps

# write a loop to index from 300 to 400 and then 400 to 500
for i in range(400, 3000, 100):
   queries = Gmaps.Cities.India("masjid")[i:i+100]
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


