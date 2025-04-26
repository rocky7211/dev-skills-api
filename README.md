# Developer Skills API

## Overview
The Developer Skills API is a web API built with Python, that allows users to track and manage their skills. The API uses Python with Flask for the backend, and PostgreSQL for the database, which is connected via an internal private network on Render. Both the API and Database are hosted on Render, to allow for this private connection.

Currently this implementation only has a backend and there is no frontend implementation as of yet. There are plans to add API frontend. [My Portfolio website](https://jaredmcdowall.me/) has a basic frontend implementation in React. [Api website here](https://api.jaredmcdowall.me) although a frontend solution is yet to come, this is the domain that hosts the api that talk directly to render.

## API Features
- **POST**: Add new skill
- **GET**: Get all skills
- **DELETE**: Remove a skill
- **PUT**: Decrement the count of a skill 
- **GET**: Get details of a specific skill

## Setup and Installation

### Prerequisites
- Python 3.11
- PostgreSQL
- pip (Python package installer)

There is no local version of this API. The live program uses an internal private connection to the database. You must connect to your own database via the `.env` file to import the database secret into the environment variable defined in `main.py`.

```python
# Entry point of the application
if __name__ == "__main__":
    # Connect to the PostgreSQL database set your own environment variable in a .env file
    db_url = os.environ.get("DATABASE_URL")
    if db_url is None:
        raise ValueError("DATABASE_URL environment variable not set")
    skills_service = service.SkillsService(PostgreSQLRepository(db_url))
```
This API is bound to `0.0.0.0` for Render, change if needed in `main.py`.

```python
 # Start the Flask app
    app.run(debug=False, host='0.0.0.0') # required for render
```

### Installation Steps
1. **Clone the repository:**
    ```sh
    git clone https://github.com/rocky7211/dev-skills-api.git
    cd dev-skills-api
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the PostgreSQL database:**
    - Create a new PostgreSQL database.
    - Update the `DATABASE_URL` environment variable in `main.py` with your PostgreSQL database secret in a `.env` file.
    ```sh
    #.env file
    DATABASE_URL = "enter database secret"
    ```

5. **Run the application:**
    ```sh
    python main.py
    ```

## API Endpoints

### Get All Skills
- **URL:** `/skills/get_all_skills`
- **Method:** `GET`
- **Response:**
    ```json
    [
        {
            "skill_name": "Python",
            "count": 5
        },
        ...
    ]
    ```

### Add a Skill
- **URL:** `/skills/add_skill`
- **Method:** `POST`
- **Response:**
    - Success: `201 Created`
    - Error: `400 Bad Request` or `403 Forbidden`

### Remove a Skill
- **URL:** `/skills/remove_skill`
- **Method:** `PUT`
- **Response:**
    - Success: `204 No Content`
    - Error: `404 Not Found`

### Decrement a Skill
- **URL:** `/skills/decrement_skill`
- **Method:** `PUT`
- **Response:**
    - Success: `204 No Content`
    - Error: `404 Not Found`

### Get a Specific Skill
- **URL:** `/skills/get_skill?skill_name={skill_name}`
- **Method:** `GET`
- **Example Response:**
```json
        {
            "skill_name": "Python",
            "count": 5
        }
```
