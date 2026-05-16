import streamlit as st
from pathlib import Path
import os

st.set_page_config(page_title="CRUD File Manager", page_icon="📁")

st.title("📁 CRUD File & Folder Manager")

# -----------------------------
# SHOW FILES & FOLDERS
# -----------------------------
def readfileandfolder():
    p = Path('.')
    items = list(p.rglob('*'))

    if items:
        st.subheader("📂 Files & Folders")
        for index, file in enumerate(items):
            st.write(f"{index+1}. {file}")
    else:
        st.info("No files or folders found.")


readfileandfolder()

st.divider()

# -----------------------------
# SIDEBAR MENU
# -----------------------------
option = st.sidebar.selectbox(
    "Choose Operation",
    (
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
        "Rename File",
        "Create Folder",
        "Delete Folder"
    )
)

# -----------------------------
# CREATE FILE
# -----------------------------
if option == "Create File":

    st.header("📄 Create File")

    file_name = st.text_input("Enter file name")
    content = st.text_area("Enter file content")

    if st.button("Create File"):

        p = Path(file_name)

        if p.exists():
            st.error("FILE ALREADY EXISTS")
        else:
            with open(file_name, 'w') as file:
                file.write(content)

            st.success("FILE CREATED SUCCESSFULLY")


# -----------------------------
# READ FILE
# -----------------------------
elif option == "Read File":

    st.header("📖 Read File")

    file_name = st.text_input("Enter file name")

    if st.button("Read File"):

        p = Path(file_name)

        if p.exists():
            with open(file_name, 'r') as file:
                st.text_area("File Content", file.read(), height=300)
        else:
            st.error("FILE NOT FOUND")


# -----------------------------
# UPDATE FILE
# -----------------------------
elif option == "Update File":

    st.header("✏️ Update File")

    file_name = st.text_input("Enter file name")

    update_option = st.radio(
        "Choose update type",
        ("Overwrite", "Append")
    )

    content = st.text_area("Enter content")

    if st.button("Update File"):

        p = Path(file_name)

        if p.exists():

            if update_option == "Overwrite":
                with open(file_name, 'w') as file:
                    file.write(content)

            elif update_option == "Append":
                with open(file_name, 'a') as file:
                    file.write(content)

            st.success("FILE UPDATED SUCCESSFULLY")

        else:
            st.error("FILE DOES NOT EXIST")


# -----------------------------
# DELETE FILE
# -----------------------------
elif option == "Delete File":

    st.header("❌ Delete File")

    file_name = st.text_input("Enter file name")

    if st.button("Delete File"):

        p = Path(file_name)

        if p.exists():
            os.remove(p)
            st.success("FILE DELETED SUCCESSFULLY")
        else:
            st.error("FILE DOES NOT EXIST")


# -----------------------------
# RENAME FILE
# -----------------------------
elif option == "Rename File":

    st.header("🔁 Rename File")

    file_name = st.text_input("Enter current file name")
    new_file_name = st.text_input("Enter new file name")

    if st.button("Rename File"):

        p = Path(file_name)

        if p.exists():
            p.rename(new_file_name)
            st.success("FILE RENAMED SUCCESSFULLY")
        else:
            st.error("FILE NOT FOUND")


# -----------------------------
# CREATE FOLDER
# -----------------------------
elif option == "Create Folder":

    st.header("📁 Create Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Create Folder"):

        p = Path(folder_name)

        if p.exists():
            st.error("FOLDER ALREADY EXISTS")
        else:
            p.mkdir()
            st.success("FOLDER CREATED SUCCESSFULLY")


# -----------------------------
# DELETE FOLDER
# -----------------------------
elif option == "Delete Folder":

    st.header("🗑️ Delete Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Delete Folder"):

        p = Path(folder_name)

        if p.exists():

            try:
                p.rmdir()
                st.success("FOLDER DELETED SUCCESSFULLY")

            except:
                st.error("FOLDER IS NOT EMPTY")

        else:
            st.error("FOLDER DOES NOT EXIST")


            