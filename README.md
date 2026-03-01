# A software for automating job search

### Output 
```
candidatures/
└── Entreprise_Poste_Ville/
    ├── cv_adapté.pdf          ← CV de base reconfiguré pour l'offre
    ├── lettre_motivation.pdf  ← lettre personnalisée entreprise + poste
    └── accroche.txt           ← 1-2 phrases pour l'objet mail / InMail
```
#### Monitoring dashboard 
```
┌─────────────────┬──────────┬───────┬─────────┬──────────────┐
│ Entreprise      │ Poste    │ Score │ Statut  │ Dernière MAJ │
├─────────────────┼──────────┼───────┼─────────┼──────────────┤
│ Google          │ Dev Py   │ 9/10  │ Envoyée │ 01/07        │
│ Mistral AI      │ AI Eng   │ 8/10  │ Entretien│ 03/07       │
│ BNP             │ Data Sci │ 6/10  │ Refus   │ 02/07        │
│ Doctolib        │ Backend  │ 8/10  │ À relancer│ ...        │
└─────────────────┴──────────┴───────┴─────────┴──────────────┘
```

#### number goals (for example)
```
200 offres agrégées
→  ~60 offres score > 7 (vous validez)
→  60 dossiers générés (CV + lettre + accroche)
→  60 candidatures envoyées
→  objectif : 5-10 entretiens
```

### First step, project structure
```
job_agent/
├── .env
├── .gitignore
├── requirements.txt
├── data/
│   ├── profil.json          # votre profil de base
│   └── offres.json          # offres agrégées
├── candidatures/            # output final
├── src/
│   ├── scraper.py           # récupération des offres
│   ├── scorer.py            # scoring offre vs profil
│   ├── generator.py         # génération CV + lettre + accroche
│   └── tracker.py           # dashboard suivi
└── main.py                  # point d'entrée
```

### Second step, creating the structure
```bash
mkdir job_agent && cd job_agent
mkdir -p data candidatures src
touch .env .gitignore requirements.txt main.py
touch src/scraper.py src/scorer.py src/generator.py src/tracker.py
```

### Third step, base profile
```
data/profil creation with real infos :
```
```json
{
    "nom": "ABC DEF",
    "niveau": "Bac+3",
    "domaine": "Mathématiques / Informatique",
    "competences": [
        "Python",
        "LLM / API calls",
        "Machine Learning",
        "SQL",
        "Git"
    ],
    "langues": ["Français", "Anglais"],
    "preferences": {
        "postes": ["AI Engineer", "Backend Engineer", "Data Engineer"],
        "localisation": ["Paris", "France", "Europe"],
        "type": ["Stage", "Alternance"],
        "secteurs": ["IA", "Tech", "Fintech", "Santé"]
    },
    "cv_base": "data/cv_base.txt"
}
```

### Fourth step, dependencies
```bash
pip install groq python-dotenv requests
```

### Step 5, the scraper
```
Commençons par **Adzuna** — l'API la plus simple et gratuite.

1. Créez un compte sur **developer.adzuna.com**
2. Récupérez votre `app_id` et `app_key`
3. Ajoutez dans votre `.env` :
```
GROQ_API_KEY=votre_clé_groq
ADZUNA_APP_ID=votre_app_id
ADZUNA_APP_KEY=votre_app_key


scraper.py    →   scorer.py   →   generator.py   →   tracker.py
(récupérer)       (filtrer)       (générer docs)      (suivre)
   ↑
je  suis ici

28/02/2026, 02h53
TO DO : écrire le script scraper.py 
scraper.py : assistant qui parcourt n sites d'offres d'emploi à ma place, récupères les offres d'emplois
intéressantes et les ajoutes dans un fichier de mon dossier, le but étant de centraliser toutes ces 
offres pour les traiter et garder celles qui correspondent au profil en question !
```