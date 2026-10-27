# A2.2 - Favourite Items

favourites = []

for i in range(5):
    item = input("Enter a favourite item: ")
    favourites.append(item)

print("My favourite items are:")
for item in favourites:
    print(item)