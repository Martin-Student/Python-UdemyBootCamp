#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting Dictionary in Dictionary

nested_dictionaries = {
    "France": {"cities_visited": ["Paris", "Lille"], "total_visits": 12}
}

# Nesting Dictiopnary in a List

travel_log = {
    {
        "country": "France",
        "city visited": ["Paris", "Dijon"],
        "total_visits": 12},
    {
        "country": "Germany",
        "city visited": ["Berlin", "Frankfurt"],
        "total_visits": 12}
}