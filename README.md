# Aplicație Flask Minimală

Aceasta este o aplicație simplă Flask pentru a demonstra un proiect minimal.

## Instalare

### 1. Clonează repo-ul:
   ```bash
   git clone https://github.com/username/proiectul-tau.git
   cd proiectul-tau
   ```

### 2. Instalează dependențele:
   ```bash
   pip install -r requirements.txt

## Cum să rulezi aplicația

### 1. Lansează aplicația Flask:
   ```bash
   python app/backend.py

### 2. Accesează aplicația la http://127.0.0.1:5000

### 4. **Verifică securitatea și confidențialitatea**
- Asigură-te că nu urci informații sensibile, cum ar fi chei API sau parole în fișierele de configurare.
- Dacă ai fișiere de configurare cu informații sensibile (ex. `config.py`), pune-le în `.gitignore` și folosește variabile de mediu pentru a le păstra în siguranță.

### 5. **Commit și Push pe GitHub**
Acum poți face următoarele comenzi pentru a pune totul pe GitHub:

#### 1. Inițializează Git (dacă nu ai făcut-o deja):
   ```bash
   git init

#### 2. Adaugă fișierele pentru commit:
   ```bash
   git add .

#### 3. Fă commit:
   ```bash
   git commit -m "First commit - Flask app working"

#### 4. Creează un repo pe GitHub și adaugă remote-ul:
   ```bash
   git remote add origin https://github.com/username/proiectul-tau.git

#### 5. Push la GitHub:
   ```bash
   git push -u origin master
