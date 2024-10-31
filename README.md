 
**Sentiment Analysis Tool for Research Papers**

A multi-format sentiment analysis tool that processes **text, PDF, and DOCX files** to provide sentiment scores and content summaries. Built with **Streamlit** for an interactive and user-friendly experience.

 Features
- Accepts text, PDF, and DOCX file uploads
- Provides a sentiment score with options to show positive, neutral, negative, and compound ratings
- Displays content summary and extracted text upon request

 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies:**
   Make sure you have Python installed, then install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Usage

1. Launch the Streamlit app by running the command above.
2. Upload a text, PDF, or DOCX file.
3. View the sentiment score. Optionally, click to expand and view the content summary.

## Project Structure

- `app.py`: Main application file
- `requirements.txt`: Contains all necessary packages for the project

## Technologies Used
- Python
- Streamlit
- PyMuPDF (`fitz`) for PDF handling
- `python-docx` for DOCX file handling