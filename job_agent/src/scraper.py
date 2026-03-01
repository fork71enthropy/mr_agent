import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

ADZUNA_APP_ID = os.environ["ADZUNA_APP_ID"]
ADZUNA_APP_KEY = os.environ["ADZUNA_APP_KEY"]

def fetch_adzuna(poste, localisation="france", nb_offres=50):
    url = f"https://api.adzuna.com/v1/api/jobs/fr/search/1"
    
    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "results_per_page": nb_offres,
        "what": poste,
        "where": localisation,
        "content-type": "application/json"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    offres = []
    for job in data.get("results", []):
        offres.append({
            "titre": job.get("title"),
            "entreprise": job.get("company", {}).get("display_name"),
            "localisation": job.get("location", {}).get("display_name"),
            "description": job.get("description"),
            "url": job.get("redirect_url"),
            "salaire_min": job.get("salary_min"),
            "salaire_max": job.get("salary_max"),
            "date": job.get("created"),
            "source": "adzuna"
        })
    
    return offres

def sauvegarder_offres(offres, chemin="data/offres.json"):
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(offres, f, ensure_ascii=False, indent=2)
    print(f"✅ {len(offres)} offres sauvegardées dans {chemin}")

if __name__ == "__main__":
    print("🔍 Récupération des offres...")
    
    offres = []
    postes = ["AI Engineer", "Data Scientist", "Machine Learning"]
    
    for poste in postes:
        print(f"  → {poste}...")
        offres += fetch_adzuna(poste, nb_offres=20)
    
    sauvegarder_offres(offres)
    print(f"\n📊 Total : {len(offres)} offres récupérées")
    print("\nExemple d'offre :")
    print(json.dumps(offres[0], indent=2, ensure_ascii=False))