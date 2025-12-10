!\[Python](https://img.shields.io/badge/Python-3.10+-blue)

!\[FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)

!\[Status](https://img.shields.io/badge/Status-Prototype-success)

!\[License](https://img.shields.io/badge/License-MIT-lightgrey)



\# Central Intelligence Hub (Prototype)



A modern, lightweight prototype of a Central Intelligence Hub that consolidates NPS, sales volume, POC feedback, and monthly trends into a single dashboard. Built for shortlisting and demonstration for AB InBev's Software Development coding role.



---



\## Features

\- NPS score display

\- Total sales volume visualization

\- POC feedback summary

\- Monthly sales bar chart

\- FastAPI backend exposing `/insights`

\- Modern, human-designed frontend (HTML/CSS/JS)



---



\## Project Structure

central\_intelligence\_hub\_modern/

├── backend/

│ ├── main.py

│ └── requirements.txt

├── frontend/

│ └── index.html

├── data/

│ └── insights.json

└── README.md





---



\## Tech Stack

\- Backend: FastAPI, Python

\- Frontend: HTML, CSS, JavaScript

\- Data: JSON

\- Server: Uvicorn



---



\## Run (local)

1\. Open terminal and start backend:

cd "%USERPROFILE%\\Desktop\\central\_intelligence\_hub\_modern\\backend"

pip install -r requirements.txt

uvicorn main:app --reload



2\. Open frontend:

\- Open `frontend/index.html` in your browser and click \*\*Load Insights\*\*.



---



\## API

`GET /insights` — returns JSON (nps, sales\_volume, monthly\_sales, poc\_feedback)



---



\## Milestones Completed

\- Requirements gathering

\- Backend API development

\- Mock data integration (JSON)

\- Frontend dashboard (UI + chart)

\- Local UAT (tested)



---



\## Future Enhancements

\- Add PostgreSQL for persistent storage

\- Add authentication (JWT)

\- Add country-level filters and export options

\- Deploy to cloud (Render / AWS / Azure)



\## Contribution Guidelines

\- Fork the repository

\- Create a feature branch

\- Submit a pull request with clear changes







