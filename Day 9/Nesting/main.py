capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

# Nested List in Dictionary

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Stuttgart"],
}

#print Lille
print(travel_log["France"][1])

travel_log = {
    "France" : {
        "times_visited" : 8,
        "cities_visited" : ["Paris", "Lille", "Dijon"],
    },
    "Germany" : {
        "times_visited" : 4,
        "cities_visited" : ["Berlin", "Stuttgart"],
    },
}

print(travel_log["Germany"]["cities_visited"][1])