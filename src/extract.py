import xml.etree.ElementTree as ET
import glob
import os

def extract_text_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    text = " ".join(elem.text for elem in root.iter() if elem.text)
    return text

def combine_articles(folder_path, file_extension="xml"):
    file_list = glob.glob(os.path.join(folder_path, f"*.{file_extension}"))
    articles = [extract_text_from_xml(file) for file in file_list]
    return articles