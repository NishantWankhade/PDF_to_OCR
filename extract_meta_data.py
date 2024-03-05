import csv
import os
from bs4 import BeautifulSoup
from xmlparse import get_all_tag_values

def retrive_xml_file_paths(root_directory):
    folders = os.listdir(root_directory)
    file_paths_list = []
     
    for file in folders:
        file_path = os.path.join(root_directory, file)
        if os.path.isdir(file_path):
            txt_files = os.listdir(file_path)
            for txt in txt_files:
                if txt.endswith('.xml'):
                    file_paths_list.append(os.path.join(file_path, txt))
    return file_paths_list


def extract_meta(lst, output_csv):
    list_of_tags = []
    
    xml_not_rendered = []
    metaData = []
    xml_lst = []
    
    with open("/home1/multilingual/ArchiveOrg/analysis/metaData/meta_data_list.txt" , 'r') as file:
        text = file.read()
        
    list_of_tags = text.split('\n')
    
    for xml in lst :
        try:
            tags_values = get_all_tag_values(xml, list_of_tags)
            metaData.append(tags_values)
            xml_lst.append(xml)
        except:
            xml_not_rendered.append(xml)
            continue

    print(len(list_of_tags))
    print(len(xml_lst))
    print(len(metaData))
    extract_metadata_details(xml_lst, list_of_tags, metaData, output_csv)
    

def extract_metadata_details(xml_lst, list_of_tags, metaData, output_csv):
    
    print(list_of_tags)
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["S.No." , "Xml Path"] + list_of_tags)
        count = 0
        for xml in xml_lst:
            csv_writer.writerow([count + 1, xml] + metaData[count])
            count = count + 1
            

if __name__ == "__main__":
    base_dir = "/home1/multilingual/ArchiveOrg/data"
    # data_folders = ["bengali", "tamil", "telugu", "hindi", "malayalam", "marathi" ,"kannada", "gujarati"]
    data_folders = ["hindi"]
    root_directories = [os.path.join(base_dir, i) for i in data_folders]
    output_csv_file = [f"/home1/multilingual/ArchiveOrg/analysis/metaData/meta_{i}.csv" for i in data_folders]

    for i in range(len(root_directories)):
        lst = retrive_xml_file_paths(root_directories[i])
        extract_meta(lst, output_csv_file[i])

        