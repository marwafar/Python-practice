destinations =['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'Sao Paulo, Brazil', 'Cairo, Egypt']

test_traveler=['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

attractions = [[] for index in range(len(destinations))]


def get_destination_index(destination):
  destination_index=destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination=traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

def add_attraction(destination,attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append (attraction) 
    return
  except ValueError:
    print ("Destinantion does not exist")
    return
  
def find_attractions (destination,interests):
  destination_index = get_destination_index(destination)
  attractions_in_city=attractions [destination_index]
  attractions_with_interest=[]
  for attraction in attractions_in_city:
    possible_attraction=attraction[0]
    attraction_tags = attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append (possible_attraction)
  return attractions_with_interest

def get_attractions_for_traveler(traveler):
  traveler_destination=traveler[1]
  traveler_interests=traveler[2]
  traveler_attractions=find_attractions (traveler_destination,traveler_interests)
  interests_string = "Hi "+ traveler[0] + ", we think you'll like these places around " + traveler_destination
  for attraction in traveler_attractions:
    interests_string += attraction
  return interests_string
  

test_destination_index= get_traveler_location(test_traveler)
#print (test_destination_index)
add_attraction("Los Angeles, USA", ['Venice Beach',['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

#print (attractions)

la_arts = find_attractions("Los Angeles, USA",["art"])

#print(la_arts)
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print (smills_france)

