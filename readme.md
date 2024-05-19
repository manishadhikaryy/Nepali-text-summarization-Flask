Sure, here's the fixed version of your README.md file with corrected formatting:

```markdown
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
   git clone https://github.com/manishadhikaryy/Nepali-text-summarization-Flask.git
   cd flask-text-summarizer
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Flask app:**

   ```sh
   python app.py
   ```

2. **Open your web browser and go to:**

   ```
   http://127.0.0.1:5000/
   ```

### Usage

1. Enter the text you want to summarize in the text area.
2. Click the "Summarize" button.
3. View the summarized text on the result page.

## Project Structure

```
flask-text-summarizer/
├── app.py
├── templates/
│   ├── index.html
│   └── result.html
├── requirements.txt
└── README.md
```

- `app.py`: The main Flask application file.
- `templates/`: Folder containing HTML templates.
- `static/`: Folder for static files (e.g., CSS).
- `requirements.txt`: File listing the Python dependencies.
```
```
