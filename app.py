import streamlit as st
import pandas as pd
import os

# Function to check if the Excel file exists, and create it if not
def create_excel_file(file_path):
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=["Title", "Date", "Description"])
        df.loc[0] = ["Diary", pd.to_datetime("2024-01-01"), ""]
        df.to_excel(file_path, index=False)
        return True
    return False

# Function to load data from Excel file into DataFrame
def load_data(file_path):
    df = pd.read_excel(file_path)
    return df

# Function to save DataFrame to Excel file
def save_data(df, file_path):
    df.to_excel(file_path, index=False)

# Function to add new entry to Excel file
def add_new_entry(title, date, description, file_path):
    df = load_data(file_path)
    new_row_index = df.shape[0]
    df.loc[new_row_index, "Title"] = title
    df.loc[new_row_index, "Date"] = date
    df.loc[new_row_index, "Description"] = description
    save_data(df, file_path)


# Main function
def main():
    st.title("Personal Diary")

    # Check if Excel file exists and create it if not
    file_path = "personal_diary.xlsx"
    excel_created = create_excel_file(file_path)

    # Load data from Excel file
    df = load_data(file_path)

    # Initialize selected_entry_title
    selected_entry_title = None

    # Sidebar
    st.sidebar.header("Options")
    if df.empty or excel_created:
        st.sidebar.write("No entries created.")
    else:
        selected_entry_title = st.sidebar.selectbox("Select Entry:", df["Title"].unique())

    # Display entry details if selected_entry_title is not None
    if selected_entry_title is not None:
        st.subheader(f"Entry Details: {selected_entry_title}")
        selected_entry_data = df[df["Title"] == selected_entry_title].iloc[0]
        title = st.text_input("Title:", selected_entry_data["Title"])
        date = st.date_input("Date:", pd.to_datetime(selected_entry_data["Date"]))  # Convert to datetime
        description = st.text_area("Description:", selected_entry_data["Description"])

        # Update DataFrame with user input
        df.loc[df["Title"] == selected_entry_title, "Title"] = title
        df.loc[df["Title"] == title, "Date"] = date
        df.loc[df["Title"] == title, "Description"] = description

        # Save DataFrame to Excel file
        save_data(df, file_path)


    # Create new entry button
    if st.sidebar.button("Create New Entry"):
        new_entry_title = st.sidebar.text_input("Enter Entry Title:")
        if new_entry_title.strip():
            add_new_entry(new_entry_title, pd.to_datetime("today"), "", file_path)
            st.sidebar.success("New entry created successfully!")

            # Reload the app to reflect the changes
            st.experimental_rerun()

if __name__ == "__main__":
    main()
