import requests

# Wir holen uns 10 User-Datensätze
response = requests.get("https://jsonplaceholder.typicode.com/users")
user_liste = response.json()

# Level 1 (Deep Dive): city des dritten Users anzeigen
city_dritter_user = user_liste[2]["address"]["city"]
print("Level 1 - Stadt des 3. Users:", city_dritter_user)

# Level 2 (Der Filter-Loop): Name ausgeben, wenn Website auf .net endet
print("\nLevel 2 - User mit .net-Website:")
for user in user_liste:
    if user["website"].endswith(".net"):
        print(user["name"])

# Level 3 (Interaktion): User-ID abfragen und E-Mail ausgeben
user_id = int(input("\nLevel 3 - Gib eine User-ID (1-10) ein: "))
email = user_liste[user_id - 1]["email"]
print("E-Mail:", email)
