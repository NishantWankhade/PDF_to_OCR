import os
def retrive_file_paths(number_of_files, root_dir):
    file_paths_list = []
    count = 0
    for subdir, dirs, files in os.walk(root_dir):
        if not dirs:
            identifier = subdir.split("/")[-1]
            for file in files:
                if file.endswith(".pdf") and count < number_of_files:
                    file_path = os.path.join(subdir, file)
                    file_paths_list.append(file_path)
    print(file_paths_list)
    return file_paths_list

# retrive_file_paths(10,"hindi_pdf/pdfs")
# this code gives the foll output

# ['hindi_pdf/pdfs/0-0_20230331/#काँग्रेस_के_कुकर्म  का पीढ़ी दर पीढ़ी एक वफादार के0एम0जोसेफ.pdf', 
# 'hindi_pdf/pdfs/0.1_20211124/0.1.pdf', 
# 'hindi_pdf/pdfs/00intro_202305/00intro.pdf', 
# 'hindi_pdf/pdfs/1-acharya-ramdev-ji/भारतवर्ष का इतिहास 1 (Acharya Ramdev ji).pdf', 
# 'hindi_pdf/pdfs/00-intro_20230103/00_intro.pdf', 
# 'hindi_pdf/pdfs/1_20191004/दानसागर.pdf', 
# 'hindi_pdf/pdfs/1_20191004/वेद विज्ञान आलोक.pdf', 
# 'hindi_pdf/pdfs/1_20191004/विवाह संस्कार प्रकाश.pdf']
