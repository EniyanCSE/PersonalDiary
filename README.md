# Personal Diary Application

This Streamlit web application allows you to manage your personal diary entries. You can create, view, update, and delete diary entries using this app.

## Setup

1. Install the required packages:
   ```bash
   pip install streamlit pandas
   ```
   
2. To run
   ```bash
   streamlit run app.py
   ```
## Usage
  Upon running the Streamlit app, you will see a sidebar with options to select existing diary entries or create a new entry.
  If no entries exist or if it's the first time running the app, a default entry titled "Diary" will be created with the current date.
  You can select an existing entry from the sidebar to view and edit its details such as title, date, and description.
  To create a new entry, click the "Create New Entry" button and provide a title for the entry.
  The app automatically saves your changes to an Excel file named personal_diary.xlsx.
