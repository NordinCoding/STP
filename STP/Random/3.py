me = {"age": "20",
      "height": "176cm",
      "favorite game": "Super Mario Galaxy"}

question = input("What Would you like to know? Age, Height or Favorite game: ")
question = question.lower()

if question in me:
    print(me[question])
