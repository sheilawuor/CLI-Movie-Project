# MOVIE WATCHLIST CLI
A simple Command Line Interface (CLI) application to manage a personal TV watchlist.
Built with Python and SQLAlchemy ORM, this project demonstrates concepts such as Python fundamentals, OOP, data structures, databases, ORM, and building CLIs.

## Features
- Full CRUD for users, movies, genres, and reviews
- Find-by-attribute flows (e.g., movie by title, genre by name, review by ID)
- Related-object views (movies per genre, reviews per movie/user)
- SQLite database using SQLAlchemy ORM (one-to-many relationships)
- Clean tabular CLI output with [tabulate]
- Input validation and helpful error messages

## Requirements
- Python 3.12+
- Virtual environment (pipenv recommended)
- Dependencies (see Pipfile):
  - SQLAlchemy
  - Alembic
  - Tabulate
- Set DATABASE_URL in your environment to override the default SQLite file (watchlist.db).

## Installation & Setup
1) Clone the repository:

```bash
git clone <your-repo-url>
cd Movie-CLI-Project-1
```

2) Install dependencies:

```bash
pipenv install
```

3) Run the CLI (auto-creates the SQLite DB):

```bash
pipenv run python cli.py
```

4) Seed dummy data (optional):

```bash
pipenv run python seeds.py
```

## Usage (menus)
### Main menu:

- 1: Movies (submenu)
- 2: Genres (submenu)
- 3: Users (submenu)
- 4: Reviews (submenu)
- 0: Exit

### Movies submenu:

- Add movie, list movies, delete movie, find by title
- View reviews for a movie
- List movies by genre

### Genres submenu:

- Add/list/delete genres
- Find genre by name
- View movies in a genre

### Users submenu:

- Add/list/delete users
- Find user by username
- View reviews from a user

### Reviews submenu:

- Add/list/delete reviews
- Find review by ID

## Database Design
The application uses SQLAlchemy ORM with 4 related tables:

- User → can add reviews
- Movie → belongs to a genre, can have reviews
- Review → links users to movies
- Genre → categorizes movies

### Key constraints:

- Unique usernames/emails; genres unique by name
- Movies unique per title+genre
- Reviews unique per user+movie; rating constrained to 1–5

## Project Hygiene
- .gitignore excludes DB files, venvs, caches, and .env.
- Configure secrets/connection strings via DATABASE_URL env var (no secrets in code).

## Learning Goals Demonstrated
- **Python fundamentals** → CLI logic, user input/output
- **Data structures** → lists, dicts, tuples in CLI functions
- **OOP & Inheritance** → SQLAlchemy models
- **SQL & ORM** → CRUD operations, relationships
- **Application structure** → modular code

## Author
Sheila Awuor

## License
MIT License