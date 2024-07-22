restaurants = [

    {"name": "Restaurante A", "nota": 4.5},
    {"name": "Restaurante B", "nota": 3.0},
    {"name": "Restaurante C", "nota": 4.2},
    {"name": "Restaurante D", "nota": 2.3},

]

filtered_restaurantes = []
min_rating_restaurants = []

min_rating = 4.0

for restaurant in restaurants:
    if restaurant["nota"] > min_rating:
        filtered_restaurantes.append(restaurant)

for restaurant in restaurants:
    if restaurant["nota"] < min_rating:
        min_rating_restaurants.append(restaurant)

print("aqui", min_rating_restaurants)

print(filtered_restaurantes)
