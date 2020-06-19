# Djano-ocr

Django based Optical character recognition (OCR)

Extract text from PDF and images (JPG, BMP, TIFF, GIF) and convert into editable Word, and Text output formats

It was created using [Flask](https://flask.palletsprojects.com/en/1.1.x/).

### Prerequisites

- [Python3](https://www.python.org/) - Python 3.6 or later
- Poppler-util
- [Tesseract OCR](https://tesseract-ocr.github.io//)
- [Tessdata languages](https://tesseract-ocr.github.io//)
  - Language used (Africans (afr) - English (eng) - Francais (fra) - Russian (rus) - Italian (ita) - Chinese (chin_sim & chin_tra) - Portguese (port)

## Getting Started

2. **Clone** the fork with HTTPS, using your local terminal to a preferred location, and **cd** into the project.

```bash
git clone https://github.com/hyaovi/django-ocr.git

Cloning into 'django-ocr'...
remote: Enumerating objects...

cd django-ocr/
```

3. Create your virtual environment, and activate it.

```bash
python -m venv env

source env/bin/activate  # Linux/Mac
env/Scripts/activate  # Windows
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Run local server, and **DONE**!

```bash
python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 19, 2020 - 11:50:14
Django version 3.0.7, using settings 'core.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

## Built With

- [Django](https://www.djangoproject.com/) Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- [Tesseract OCR](https://tesseract-ocr.github.io//)
  PyMongo is a Python distribution containing tools for working with MongoDB
