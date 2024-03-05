from bs4 import BeautifulSoup
    
def get_all_tag_values(path,list_of_tags):
    tag_value_pair = {}
    with open(path, 'r') as f:
        data = f.read()

    Bs_data = BeautifulSoup(data, "xml")
    
    for tag in list_of_tags:
        values = Bs_data.find_all(tag)
        pair = ""
        for value in values:
            pair = pair + value.text
            pair = pair + "\n"
        
        if(len(values) == 0): 
            pair = "NaN"
        tag_value_pair[tag] = pair
    
    return tag_value_pair        

# parse_xml("/home1/multilingual/ArchiveOrg/data/hindi/0-bachho-inse-seekho-hardam-sachchidanand-sinha/0-bachho-inse-seekho-hardam-sachchidanand-sinha_meta.xml")

# path = "/home1/multilingual/ArchiveOrg/data/hindi/0-bachho-inse-seekho-hardam-sachchidanand-sinha/0-bachho-inse-seekho-hardam-sachchidanand-sinha_meta.xml"

# with open("/home1/multilingual/ArchiveOrg/analysis/metaData/meta_data_list.txt" , 'r') as file:
#         text = file.read()
        
# list_of_tags = text.split('\n')

# print(get_all_tag_values(path,list_of_tags))


