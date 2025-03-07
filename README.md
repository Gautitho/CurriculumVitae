# CurriculumVitae

Ce répertoire a pour objectif de stocker un CV au format Markdown et de le générer au format PDF.

### Mettre en place l'environnement
```
sudo apt-get install wkhtmltopdf
python -m venv .env               # Create a virtual environnement / /!\ Don't commit the .env directory
source .env/bin/activate          # Apply virtual env / Do this each time, you reopen a terminal
pip install -r requirements.txt   # Install all required librairies in the virtual env
```

### Générer le CV au format PDF
```
python generate_pdf.py
```