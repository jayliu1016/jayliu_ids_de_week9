[![Python CI](https://github.com/jayliu1016/jayliu_ids_de_week9/actions/workflows/ci.yml/badge.svg)](https://github.com/jayliu1016/jayliu_ids_de_week9/actions/workflows/ci.yml)
# Week 9 Mini Project

## Project Overview
This project involves setting up a cloud-hosted Jupyter Notebook for data manipulation tasks using the `US_birth.csv` dataset.

## Google colab link:
https://colab.research.google.com/drive/1_4-E6Qzfre5eQdrGY8RI7-TlfcrpFIh7#scrollTo=U_eedmoKivIb

## Data Description
- **Dataset**: U.S. birth data from 2000 to 2014.
- **Columns**: Year, Month, Day of Month, Day of Week, Number of Births.

## Setup Instructions
1. Clone the repository: `git clone <repository-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the setup script: `bash setup.sh`

## Usage
- **Jupyter Notebook**: Open `main.ipynb` in Google Colab or a local Jupyter environment.
- **Scripts**: Run `main.py` for data manipulations in a command-line interface.

## CI/CD Pipeline
GitHub Actions has been used for:
- Linting (`flake8`)
- Running unit tests (`pytest`)

## Dependencies
- Python 3.9+
- Libraries: pandas, matplotlib, seaborn, flake8, pytest

