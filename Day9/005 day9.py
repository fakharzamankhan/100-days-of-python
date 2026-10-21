travel_log= [
    {"Country": "France",
     "cities_visited": ["Paris","Lille","Dijon"],
     "total_visits": 12
    },
    {"Country": "Germany",
     "cities_visited": ["Berlin"," Hamburg","stuttgart"],
     "Total_visits": 5
    },
]

def add_new_country(country_visited,times_visited,cities_visited):
    new_country= {"Country": country_visited, "Visits": times_visited, "Cites": cities_visited}
    travel_log.append(new_country)


add_new_country("Russia",2,["Moscow", "Saint Petersburg"])
print(travel_log)
