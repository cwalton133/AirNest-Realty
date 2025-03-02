# AirNest-Realty

## Overview

**AirNest-Realty** is a modern real estate platform that enables realtors to list, manage, and analyze
Airbnb-style rental properties.
Built with **Django (DRF) for the backend** and **React TypeScript with Vite for the frontend**,
it ensures high performance, scalability, and a smooth user experience.

## Tech Stack

- **Backend:** Django REST Framework (DRF), PostgreSQL
- **Frontend:** React.js + TypeScript + Vite, Tailwind CSS
- **Authentication:** JWT (Django Simple JWT)
- **Deployment:** Docker, AWS (EC2, S3), Vercel (Frontend)
- **CI/CD:** GitHub Actions

---

## Features

- 🏡 **Property Listings** – Add, edit, and manage rental properties.
- 🔐 **Authentication** – User sign-up, login, and role-based access.
- 📊 **Analytics Dashboard** – Track performance of listed properties.
- 📍 **Google Maps Integration** – View locations of properties.
- 📅 **Booking System** – API to integrate booking features.

---

## Project Setup

### **Backend (Django API)**

#### 1️⃣ Clone the repository

```bash
git clone https://github.com/cwalton133/AirNest-Realty.git
cd AirNest-Realty


python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows


pip install -r backend/requirements.txt

4️⃣ Run database migrations
bash
python manage.py migrate

5️⃣ Create a superuser
bash
python manage.py createsuperuser

Run the Django server
python manage.py runserver

Frontend (React + Vite)
1️⃣ Navigate to the frontend folder
bash
cd frontend

Install dependencies
npm install

tart the development server
npm run dev

Environment Variables
Create a .env file in both backend/ and frontend/ with the following:

Backend (backend/.env)
ini

SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=*
DATABASE_URL=your_postgres_db_url

Frontend (frontend/.env)
ini
VITE_API_BASE_URL=http://127.0.0.1:8000/api

Project Structure

AirNest-Realty/
│── backend/               # Django backend (DRF)
│   ├── airnest_realty/              # Main Django app
│   ├── listing/               # API endpoints
│   ├── static/            # Static files
│   ├── media/             # Media uploads
│   ├── manage.py          # Django entry point
│   └── requirements.txt   # Backend dependencies
│
│── frontend/              # React + TypeScript + Vite frontend
│   ├── src/               # Source files
│   ├── public/            # Public assets
│   ├── index.html         # Root HTML file
│   ├── vite.config.ts     # Vite config file
│   └── tsconfig.json      # TypeScript config
│
│── .gitignore             # Git ignore rules
│── README.md              # Project documentation
│── .env.example           # Environment variable example
│── docker-compose.yml     # Docker setup
│── LICENSE                # Open-source license
└── CONTRIBUTING.md        # Contribution guidelines


Contributing
1. We welcome contributions! To contribute:
2. Fork the repository.
3. Create a feature branch (git checkout -b feature-name).
4. Commit your changes (git commit -m "Add feature").
5. Push to GitHub (git push origin feature-name).
6. Create a Pull Request (PR) for review.

License
This project is licensed under the MIT License.
MIT License
Copyright (c) 2025









License
This project is licensed under the MIT License.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Fork the repository.
Create a feature branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.

Contact Us
For any questions or feedback, please contact:

Charles Walton - cwalton1335@gmail.com
GitHub: cwalton133
OluwaSegun Bankole -bankoleoluwasegun17@yahoo.com
GithHub:

Thank you for checking out the AirNest-Realtor Application!
```
