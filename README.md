# LLM Tweet Analysis

Note:
This project is currently under development and adopts two distinct approaches:
  1. Main Branch Approach:
      
     The primary approach, implemented in the main branch, leverages SQLAlchemy for database management, Pydantic for data validation, and a Large Language Model      (LLM) for sentiment analysis. The objective is to gain insights into public sentiment during critical events. The overall code architecture relies on the LLM (instructor client) to analyze tweets and classify them into three categories: Political, Offensive, and Neutral.

  2. Secondary Approach:
     
     The second approach will be maintained in a separate branch (name to be determined). This method depends on keywords extracted from tweets stored in the database. It employs a rule-based LLMClassifier to process tweets, without direct reliance on an LLM client.


## Project Overview
This project is designed to analyze tweets stored in a PostgreSQL database and classify them into three categories: `Political`, `Offensive`, or `Neutral`. It uses:
- **SQLAlchemy** for ORM and database management.
- **Pydantic** for data validation and response modeling.
- **Pandas** for keyword extraction from an Excel file.
- A mock LLM client for future integration of language models.

The project implements a hybrid classification system using keywords stored in an Excel file for efficient and customizable detection.

---

## Directory Structure
First Approach (Main Branch)
``` 
tweet_analysis_project/
│
├── app/
│ ├── init.py
│ ├── config.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ ├── services.py
│ └── main.py
│
├── migrations/
│ └── versions/
│ └── <timestamp>_create_tweets_table.py
│
├── requirements.txt
├── README.md
└── .env

Second Approach (Second Branch)

llm_tweet_analysis/
|-- main.py                    # Entry point of the application
|-- models/
|   |-- __init__.py            # Initialize models module
|   |-- database.py            # SQLAlchemy ORM models
|-- schemas/
|   |-- __init__.py            # Initialize schemas module
|   |-- tweet_model.py         # Pydantic models for response validation
|-- services/
|   |-- __init__.py            # Initialize services module
|   |-- llm_classifier.py      # Classification logic
|   |-- business_logic.py      # Business logic to fetch and classify tweets
|-- config/
|   |-- settings.py            # Configuration for database and paths
|-- keywords.xlsx              # Excel file with keywords for classification
|-- README.md                  # Documentation of the project
|-- requirements.txt           # Project dependencies
```

---

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/llm_tweet_analysis.git
cd llm_tweet_analysis
```

### 2. Install Dependencies
Ensure you have Python 3.8+ installed. Then run:
```bash
pip install -r requirements.txt
```

### 3. Database Setup
Update the `DATABASE_URL` in `config/settings.py` to match your PostgreSQL credentials. Create the database schema:
```bash
python -m models.database
```

### 4. Prepare the Keywords
Ensure `keywords.xlsx` is present in the root directory with the following structure:
| Keyword        | Category    |
|----------------|-------------|
| biden          | Political   |
| trump          | Political   |
| f***           | Offensive   |

### 5. Run the Application
```bash
python3 -m app.main
```

---

## Features
- **Dynamic Keyword Loading**: Reads keywords from `keywords.xlsx` for flexibility.
- **Hybrid Classification**: Combines rule-based logic with LLM support.
- **Pydantic Validation**: Ensures data integrity and prevents hallucinations in results.
- **SQLAlchemy ORM**: Efficient database querying and management.

---

## Key Files and Responsibilities

### 1. `models/database.py`
Defines the SQLAlchemy `Tweet` model to interact with the database.

### 2. `schemas/tweet_model.py`
Implements the Pydantic `TweetModel` for response validation and compatibility with SQLAlchemy.

### 3. `services/llm_classifier.py`
Loads keywords and classifies tweets using predefined rules.

### 4. `services/business_logic.py`
Fetches tweets from the database and integrates classification logic for client-ready responses.

### 5. `config/settings.py`
Centralizes configuration such as database URL and file paths.

---

## Future Enhancements
- **Integrate OpenAI API**: Replace the mock LLM client with a live API integration for advanced classification.
- **Web Interface**: Add a FastAPI-based web service for real-time tweet classification.
- **Improved Keyword Management**: Develop a GUI tool for managing the Excel/CSV DB file.

---

## Contributing
Feel free to fork this repository and submit pull requests. Contributions are welcome!




