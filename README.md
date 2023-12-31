<br />
<p align="center">
  <a href="https://github.com/gonzasestopal/lambda-integrations/serverless-fast">
    <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="Logo">
  </a>

  <h3 align="center">Restaurant Service</h3>

  <p align="center">
    API using serverless and fastapi.
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This API allows diners to do reservations on restaurants based on requirements.


### Built With

* [serverless](https://www.serverless.com/)
* [fastapi](https://fastapi.tiangolo.com/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* npm
  ```sh
  nvm install node
  ```

* psql
  ```sh
  docker-compose up
  ```

### Installation

1. Clone the repo
   ```sh
   git clone git@github.com:Gonzasestopal/reservations-service.git
   ```
2. Install NPM packages
   ```sh
   npm i
   ```

3. Install python packages
   ```sh
   pip install -r requirements.txt
   ```

4. Install python dev packages
   ```sh
   pip install -r requirements-dev.txt
   ```

5. Add settings
   ```sh
   cp env.example .env
   ```

6. Run migrations
   ```sh
   alembic upgrade head
   ```

7. Run seeds
   ```sh
   python seeds.py
   ```

8. Run app
    ```sh
    uvicorn app.main:app --reload --env-file .env
    ```


### Docs

FastAPI auto generated docs will be available at http://localhost:8000/docs

### Testing

To verify tests are working follow these simple steps.

1. Install python dev packages
   ```sh
   pip install -r requirements-dev.txt
   ```

2. Run tests
    ```sh
    mamba tests
    ```
