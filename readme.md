# Aucrade - Online Auction Platform

## Overview
Aucrade is a full-stack web application designed to facilitate online auctions. Users can register, log in, and participate in auctions by bidding on listed items. The platform provides real-time updates and ensures secure transactions through backend authentication.

## Features
- User authentication (signup, login, session handling)
- Item listing for auctions
- Bidding system
- Secure backend API
- Responsive frontend built with TypeScript and Vite
- Database-backed auction management

## Technologies Used
### Frontend:
- TypeScript
- React (Vite-based setup)
- Tailwind CSS (if applicable)

### Backend:
- Django (Python-based framework)
- SQLite (default database, can be changed to PostgreSQL/MySQL)
- Django Rest Framework (API handling)

## Project Structure
```
aucrade-main/
│── backend/                    # Backend (Django-based)
│   ├── auctry/                 # Main Django application
│   ├── db.sqlite3              # SQLite database (for development)
│   ├── manage.py               # Django management script
│   ├── requirements.txt        # Python dependencies
│── frontend/                   # Frontend (React + TypeScript)
│   ├── auctry/aucrade/         # Main frontend application
│   ├── package.json            # Frontend dependencies
│   ├── vite.config.ts          # Vite configuration
│── readme.md                   # Project documentation
```

## Installation & Setup
### Backend Setup:
1. Install Python and Django (if not installed):
   ```sh
   pip install -r backend/requirements.txt
   ```
2. Navigate to the backend directory:
   ```sh
   cd backend/auctry
   ```
3. Run database migrations:
   ```sh
   python manage.py migrate
   ```
4. Start the backend server:
   ```sh
   python manage.py runserver
   ```
5. The backend will be running at `http://127.0.0.1:8000/`

### Frontend Setup:
1. Navigate to the frontend directory:
   ```sh
   cd frontend/auctry/aucrade
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the frontend server:
   ```sh
   npm run dev
   ```
4. Open the browser and visit `http://localhost:5173/`

## API Endpoints
The backend exposes the following API endpoints:
- **User Authentication**: `/accounts/signup/`, `/accounts/login2/`
- **Auction Items**: `/items/all/`
- **Bidding System**: Endpoints for placing and tracking bids

For detailed API interaction, check `src/API/api.ts` in the frontend.

