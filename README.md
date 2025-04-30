# JFG Costura

**JFG Costura** is a simple website entirely built with Django and HTMX for a sewing machine company.

## Features

- **Home Page**: Overview of JFG Costura with dynamic content loading via HTMX.
- **About Page**: Information about JFG Costura, loaded interactively with HTMX.
- **Machines Page**: Details of machines in stock and for sale with HTMX-powered filtering and sorting.
- **Contact Form**: HTMX-driven form to send messages to the shop with instant validation and feedback.
- **Responsive Design**: Basic responsive layout using custom CSS without any framework.

## Technologies Used

- **Python 3.x**  
- **Django**  
- **HTMX** (for interactive, AJAX-like functionality)  
- **SQLite** (development database)  
- **HTML/CSS**  
- **Vanilla JavaScript** (minimal)

## Project Structure

```
jfg-costura/
├── jfg/                    # Django project settings & configuration  
│   ├── settings.py         # Main settings  
│   ├── urls.py             # URL routing  
│   └── wsgi.py             # WSGI entry point  
├── website/                # Main application  
│   ├── migrations/         # Database migrations  
│   ├── templates/          # HTML templates  
│   │   ├── base.html       # Base layout with HTMX integration  
│   │   ├── home.html       # Home page  
│   │   ├── about.html      # About page  
│   │   ├── machines.html   # Machines page  
│   │   └── contact.html    # Contact form page  
│   ├── static/             # CSS, JS, images  
│   │   └── css/style.css   # Custom styling  
│   ├── views.py            # View functions using HTMX responses  
│   ├── urls.py             # App-level routes  
│   └── forms.py            # Contact form definition  
├── manage.py               # Django management script  
└── requirements.txt        # Python dependencies  
```

## Installation

### Prerequisites

- Python 3.8 or higher  
- pip  
- Virtual environment (recommended)

### Setup Steps

1. **Clone the repository**  
   ```bash
   git clone https://github.com/GOMES31/jfg-costura.git
   cd jfg-costura
   ```

2. **Create & activate a virtual environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**  
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**  
   ```bash
   python manage.py runserver
   ```

6. **Open in your browser**  
   Navigate to `http://127.0.0.1:8000/` to view the site.

## Usage

- **Browse Pages**: Home, About, Machines, and Contact, all powered by HTMX for seamless interactions.  
- **Send a Message**: Use the HTMX-enabled contact form for instant feedback without page reloads.  
