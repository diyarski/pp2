car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

car["year"] = 2020

car["color"] = "red"

car.pop("model")

car.clear()
