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

