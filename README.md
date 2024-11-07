# Movie Recommendation System

This project is a **Movie Recommendation System** built using Flask, pandas, and collaborative filtering techniques. The system allows users to select a movie and receive movie recommendations based on user preferences.

## Project Overview

- **Technologies used**:

  - Python
  - Flask (Web Framework)
  - Pandas (Data manipulation)
  - Scikit-learn (for Cosine Similarity calculation)

- **Functionalities**:
  - A web-based interface built with Flask allows users to choose a movie from a list.
  - The recommendation system suggests similar movies based on collaborative filtering (using Cosine Similarity).

## Installation

Follow these steps to set up and run the project locally.

### Prerequisites

1. Install **Python 3** and **pip** if you don't have them installed.
2. Clone the repository or download the project folder.

### Setting up the environment

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:

   Windows:
   bash
   .\venv\Scripts\activate

3. Install dependencies from requirements.txt:
   bash
   pip install -r requirements.txt
