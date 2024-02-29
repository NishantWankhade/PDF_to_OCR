import os
import matplotlib.pyplot as plt
from file_paths import retrieve_file_paths_text



def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def calculate_similarity(text1, text2):
    # Using Levenshtein distance as a simple similarity measure
    # You may need to install the python-Levenshtein package using: pip install python-Levenshtein
    from Levenshtein import distance

    # Normalize the distance by the length of the longer text
    max_length = max(len(text1), len(text2))
    normalized_distance = distance(text1, text2) / max_length

    # Similarity is 1 - normalized distance
    similarity = 1 - normalized_distance
    return similarity




if __name__ == "__main__":
    number_of_files = 4
    actual_dir = r"D:\pdf_to_ocr_B\3_paras"
    corrected_dir = r"D:\pdf_to_ocr_B\3_paras_cleaned"

    actual_files = retrieve_file_paths_text(number_of_files, actual_dir)
    corrected_files = retrieve_file_paths_text(number_of_files, corrected_dir)

    similarity_scores = []

    for i in range(min(len(corrected_files), len(actual_files))):
        corrected_file = corrected_files[i]
        actual_file = actual_files[i]

        text1 = read_text_file(corrected_file)
        text2 = read_text_file(actual_file)

        similarity = calculate_similarity(text1, text2)
        similarity_scores.append(similarity)

        print(f"Similarity between {corrected_file} and {actual_file}: {similarity}")

    # Generate histogram
    plt.hist(similarity_scores, bins=20, color='blue', alpha=0.7)
    plt.xlabel('Similarity Score')
    plt.ylabel('Frequency')
    plt.title('Histogram of Similarity Scores')
    plt.show()
