travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_visited, visits_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = visits_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

def add_another_country(country_visited, visits_visited, cities_visited):
    new_country = {
        "country":country_visited,
        "visits":visits_visited,
        "cities":cities_visited
    }
    travel_log.append(new_country)

add_another_country("USA", 3, ["Los Angeles", "New York", "Miami"])

print(travel_log)