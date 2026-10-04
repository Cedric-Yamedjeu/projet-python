# Analyse des paroles de chansons

from collections import Counter
import json
from pprint import pprint
import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def obtention_urls():
   
    lien = []
    page = 1
    
    while True:    
        print(f"fenching page {page}...")
        url = f"https://genius.com/api/artists/29743/songs?page={page}&sort=popularity"
        r =  requests.get(url, headers=headers)
        #print(r.status_code)
        if r.status_code == 200:
            response = r.json().get("response",{})
            # pour récupérer tous les urls des songs
            songs = response.get("songs")
            all_song = [music.get("url") for music in songs]
            lien.extend(all_song)
            
            #pprint(response)
            # pour parcourir toutes les pages
            next_page = response.get("next_page")
            #print(next_page)
            if not next_page:
                break

            page = next_page
        else:
            print("Mauvais status_code")
            break
    #pprint(lien)
    #print(len(lien))
    return lien
    
    




def extract_lyrics(url):
    print(f"fetching lyrics {url}...")
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print("Mauvais url")
        return None
    # utiliser le modules Beautifulsoup pour contenir les paroles
    soup = BeautifulSoup(r.content,'html.parser')
    #pprint(r.content)
    # récupérer les paroles
    lyrics = soup.find_all("div" ,attrs={"data-lyrics-container": "true"})
    #lyrics = soup.find("div" ,class_ = "Lyrics__Container-sc-d019c5fa-1 iHiXlq")
    if not lyrics:
        return []

    #print(lyrics)

    tous_paroles = []

    for parole in lyrics:
        for sentences in parole.stripped_strings:
            paroles = [mot.lower().strip(",.") for mot in sentences.split() if ("[" not in mot and "]" not in mot)]
            #print(paroles)
            tous_paroles.extend(paroles)
    return tous_paroles
    
#trier_paroles = sorted(set(tous_paroles))
#print(trier_paroles)


#extract_lyrics(url='https://genius.com/Patrick-bruel-du-bout-des-levres-lyrics')         


def extract_tous_lyrics():
    urls = obtention_urls()
    paroles_complet = []
    for url in urls:
        tous_lyrics = extract_lyrics(url=url) 
        if tous_lyrics:
           paroles_complet.extend(tous_lyrics)

    #pprint(paroles_complet)
    with open("music.json", "w", encoding="utf-8") as f:
        json.dump(paroles_complet, f, indent=4, ensure_ascii=False)


    #with open("music.json", "r") as f:
     #   paroles_complet = json.load(f)

# Compter les mots communs dans les songs
    compter = Counter([mot for mot in paroles_complet if len(mot)>5])
    compter_mots_communs = compter.most_common(5)
    print(compter_mots_communs)



extract_tous_lyrics()




