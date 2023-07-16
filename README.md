# fhir
Backend Engineer - Technical Assessment By kumarrameg

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Usage](#usage)
- [Docker](#docker)

## Project Description

Project Name is a healthcare API that provides comprehensive patient care record functionality. It allows healthcare providers to manage and access patient data efficiently, enabling seamless delivery of healthcare services. The API supports CRUD operations for patients, encounters, and observations, allowing users to create, retrieve, update, and delete patient records easily.

## Features

- **Patient Management:** Create and manage patient records, including personal information, demographics, and contact details.
- **Encounter Tracking:** Track patient encounters, including visit dates, locations, and relevant details.
- **Observation Tracking:** Record and manage patient observations such as vitals, lab results, and clinical findings.
- **API Endpoints:** Provides RESTful API endpoints for seamless integration with various healthcare applications and systems.
- **Data Validation:** Ensures data integrity by validating incoming data against predefined rules and constraints.
- **Authentication and Authorization:** Secure API endpoints with authentication mechanisms to control access and protect patient data.
- **Documentation:** Includes comprehensive API documentation to guide developers in integrating the API into their applications.

## Technologies Used

- **Django:** Python web framework for building the API endpoints and handling data models.
- **PostgreSQL:** Database system for storing patient records and related data.
- **Django REST Framework:** Facilitates building RESTful APIs with robust serialization, authentication, and request handling.
- **Docker:** Provides containerization for easy deployment and management of the application.

## Usage

Refer to the API documentation [https://chat.openai.com/docs/api.md] for detailed information on using the API endpoints and data structures.

With this prototype, you have basic CRUD operations for patients, encounters, and observations:

### User create & Authentication:

- `POST /api/user/create/` - Create a new user
- `GET /api/user/me/` - Get the current user's details
- `PUT /api/user/me/` - Update the current user's details
- `PATCH /api/user/me/` - Partially update the current user's details
- `POST /api/user/token/` - Generate an authentication token for the user

#### Login:
Once the token is generated, you can authenticate using Swagger:
1. Click the "Authorize" button
2. Choose the last option "tokenAuth" (apiKey)
3. Paste your token in the format `Token **************`

### Patients:

- `GET /patients/` - Get a list of all patients
- `POST /patients/` - Create a new patient
- `GET /patients/{id}/` - Get details of a specific patient
- `PUT /patients/{id}/` - Update details of a specific patient
- `DELETE /patients/{id}/` - Delete a specific patient

### Encounters:

- `GET /encounters/` - Get a list of all encounters
- `POST /encounters/` - Create a new encounter
- `GET /encounters/{id}/` - Get details of a specific encounter
- `PUT /encounters/{id}/` - Update details of a specific encounter
- `DELETE /encounters/{id}/` - Delete a specific encounter

### Observations:

- `GET /observations/` - Get a list of all observations
- `POST /observations/` - Create a new observation
- `GET /observations/{id}/` - Get details of a specific observation
- `PUT /observations/{id}/` - Update details of a specific observation
- `DELETE /observations/{id}/` - Delete a specific observation

## Docker

The project utilizes Docker for containerization. Follow these steps to run the project using Docker:

1. Install Docker: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
2. Clone the repository: `git clone https://github.com/kumarrameg/fhir-ramkumar.git`
3. Navigate to the project directory: `cd project`
4. Build the Docker image: `docker build .`
5. Run the Docker container: `docker-compose up -d`
6. Run the migrations: `docker-compose run --rm app sh -c "python manage.py makemigrations"`
7. Run the migrations: `docker-compose run --rm app sh -c "python manage.py migrate"`
8. Access the project in your browser at [http://localhost:8000](http://localhost:8000)
