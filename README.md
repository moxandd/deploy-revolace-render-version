<p align="center"><img src="https://i.postimg.cc/wvqj5Tnh/6aed7e76bed4492fbb1c73122ca736a0-free.png" /></p>

### Revolace: Web-blog, Portfolio Project

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Revolace is a full-stack web application built by Danil Kazakov (moxandd) to showcase my combined skills in modern web development. It uses a range of web development technologies such as HTML, CSS, TailwindCSS, Django, Postresql Database on NeonDB and etc.

## Key Features

- **Dynamic models for posts, users:** Utilizing Database to provide data for rendering all the information on frontend site, no hardcoded values.
- **Simple Post Search by Titles:** Quickly find posts with the filetering by a title.
- **Dynamic view count on posts:** Everytime a user (you) visits a post, it's view count increases.
- **Responsive Design:** Seamlessly adapts to different screen sizes using Tailwind CSS, providing an optimal experience on desktop, tablet, and mobile devices.

## Technologies Used

- **Backend:**
  - Django (Python) - Robust web framework for efficient development and database management.
- **Frontend:**
  - HTML, CSS, Tailwind CSS - Structural foundation, styling, and responsive design utility framework.
  - JavaScript - Dynamic elements, interactions, and data handling but mostly intergation with TailwindCSS due to the npm.

## Project Highlights

- **Clean and Simple User Interfaces:** Prioritizes usability and visual appeal, with thoughtful CSS/Tailwind CSS usage.

## How to Run (For Demonstration)

**Prerequisites**

Create .env file and put information there accordingly to the .env_example file.

- **Python 3.10 - Python 3.12:**

After you create the .env file and put all neccessary information there, you can launch it yourself.But note that there is not gonna be any data in your database, you can create your own instances of the models using Django Admin Panel.

Using Docker:

1. `docker build -f Dockerfile -t revolace .`

2. `docker run --env-file .env -p 8001:8000 --rm --name revolace-dev -it revolace`

!IMPORTANT: THE SERVER IS GONNA RUN ON "localhost:8001" = "http://127.0.0.1:8001/"

Or manually type and run the follwoing commands in the terminal:

1. `python -m venv .venv`

2. `.venv/scripts/activate`

3. `pip install -r requirements.txt`

4. `npm install`

5. `npm run dev`

6. `python manage.py runserver`

## Feedback and Contact

We welcome feedback and suggestions on how to further improve this project.
**My Contact:** danya-kazakov-96@mail.ru
