# Flask Text Summarizer

This is a simple Flask web application that summarizes text using TF-IDF. The application takes a block of text as input and returns a summarized version of the text.

## Features

- Input text in Nepali or English.
- Summarizes text using TF-IDF.
- Simple and clean user interface.

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/flask-text-summarizer.git
   cd flask-text-summarizer
Create and activate a virtual environment:

```sh
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required packages:

```sh
Copy code
pip install -r requirements.txt
Running the Application
Start the Flask app:

```sh
Copy code
python app.py
Open your web browser and go to:

arduino
Copy code
http://127.0.0.1:5000/
Usage
Enter the text you want to summarize in the text area.
Click the "Summarize" button.
View the summarized text on the result page.
Project Structure
arduino
Copy code
flask-text-summarizer/
├── app.py
├── templates/
│   ├── index.html
│   └── result.html
├── requirements.txt
└── README.md

app.py: The main Flask application file.
templates/: Folder containing HTML templates.
static/: Folder for static files (e.g., CSS).
requirements.txt: File listing the Python dependencies.