# Flipkart Clone - Django E-commerce Website

A modern e-commerce website built with Django, featuring a clean UI and product categories.

## Features

- 🏠 Home page with featured products
- 📱 Mobile phones category
- 👔 Fashion category
- 🎨 Modern gradient design
- 📦 Product cards with images
- 🛒 Responsive layout

## Technologies Used

- Python 3.x
- Django 6.0.2
- SQLite Database
- HTML/CSS
- Pillow (for image handling)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd <repo-name>
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate virtual environment:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

4. Install dependencies:
```bash
pip install django pillow
```

5. Run migrations:
```bash
cd flipkart
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

7. Open your browser and visit: `http://127.0.0.1:8000/`

## Project Structure

```
flipkart/
├── flipkart/          # Main project settings
├── products/          # Products app
│   ├── templates/     # HTML templates
│   ├── models.py      # Product models
│   └── views.py       # View functions
├── cart/              # Cart app
└── users/             # Users app
```

## Screenshots

Visit the following pages:
- Home: http://127.0.0.1:8000/
- Mobiles: http://127.0.0.1:8000/mobiles/
- Fashion: http://127.0.0.1:8000/fashion/

## License

This project is for educational purposes.
