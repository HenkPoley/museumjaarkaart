#!/usr/bin/env python3

import random
import json

# Lees de museumkaart data uit een JSON-bestand
def load_museum_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Toon de provincies met nummering
def show_provinces(data):
    print("Kies een provincie (bijvoorbeeld 1,2):")
    for i, province in enumerate(data["Museumkaart"], 1):
        print(f"{i}. {province['province']}")

# Vraag de gebruiker om invoer
def get_user_input():
    show_provinces(museum_data)
    selected_provinces = input("Voer de nummers van de provincies in (bijvoorbeeld '1,2') of druk op Enter voor alle provincies: ")
    
    if selected_provinces.strip() == "":  # Als er geen invoer is, kies alle provincies
        province_indices = list(range(len(museum_data["Museumkaart"])))
    else:
        province_indices = [int(i.strip()) - 1 for i in selected_provinces.split(",")]
    
    return province_indices

# Toon de gekozen provincies
def show_selected_provinces(data, province_indices):
    print("Je hebt gekozen voor:")
    for index in province_indices:
        print(f"- {data['Museumkaart'][index]['province']}")

# Vraag hoeveel musea moeten worden weergegeven
def get_museum_count():
    try:
        count = input("Hoeveel musea wil je zien? (druk op Enter voor 10): ")
        if count == "":
            return 10
        else:
            return int(count)
    except ValueError:
        print("Ongeldige invoer, het standaard aantal (10) wordt gebruikt.")
        return 10

# Haal musea uit de geselecteerde provincies
def get_museums_from_provinces(data, province_indices):
    selected_museums = []
    for index in province_indices:
        province_data = data["Museumkaart"][index]
        selected_museums.extend(province_data["museums"])
    return selected_museums

# Toon willekeurig gekozen musea
def show_random_museums(museums, count):
    random_museums = random.sample(museums, min(count, len(museums)))
    for museum in random_museums:
        print(f"{museum['name']} - {museum['location']}")

# Main function
def main():
    global museum_data
    museum_data = load_museum_data('./museumjaarkaart-oktober-2024.json')  # Laad JSON-bestand
    province_indices = get_user_input()
    show_selected_provinces(museum_data, province_indices)
    museum_count = get_museum_count()
    museums = get_museums_from_provinces(museum_data, province_indices)
    show_random_museums(museums, museum_count)

if __name__ == "__main__":
    main()
