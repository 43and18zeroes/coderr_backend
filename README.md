# Coderr

## Overview

This project a web application that replicates a freelancing platform. It serves to learn the concepts and technologies required to build an interactive web application with a backend in Django REST Framework and a frontend in JavaScript. By building a platform for freelance services, we gain practical experience in developing features such as user authentication, service offering creation, search functionality, and booking processes.

## Technologies Used

*   **Backend:** Django REST Framework (DRF), Python 3.13.1
*   **Frontend:** JavaScript
*   **Database:** (SQLite)

## Installation

### Prerequisites

*   Python 3.13.1
*   Node.js and npm (or Yarn) (Specify versions)
*   Virtualenv (optional, but highly recommended)

### Steps

1.  **Clone the backend repository:**
    ```bash
    git clone https://github.com/43and18zeroes/coderr_backend.git
    ```
    ```bash
    cd coderr_backend
    ```

2.  **Set up the backend:**
    *   Create a virtual environment (optional):
        ```bash
        py -m venv env
        env/Scripts/activate
        ```
    *   Install Django:
        ```bash
        py -m pip install Django
        pip install djangorestframework
        ```
    *   Install dependencies:
        ```bash
        pip install -r requirements.txt
        ```
    *   Migrate the database:
        ```bash
        py manage.py migrate
        ```
    *   Start the backend server:
        ```bash
        py manage.py runserver
        ```

3.  **Clone the frontend repository:**
    ```bash
    git clone https://github.com/43and18zeroes/coderr_frontend.git
    cd coderr_frontend
    ```

4.  **Set up the frontend:**
    *   Install dependencies:
        ```bash
        npm install  # Or yarn install
        ```
    *   Start the frontend app (using a local live server):
        ```bash
        npm start  # Or yarn start
        ```

## Contact

*   **Author:** Christoph Wagner
*   **Email:** christoph@cw-coding.de