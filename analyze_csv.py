import csv
import os

#Reading CSV 
def create_csv_cluster(csv_path, row_num):
    with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
        csv_file = csv.reader(csvfile)
        cluster_dict = {}
        first = 0
        for row in csv_file:
            if first == 0:
                name = row[row_num]
                first = first + 1
            cluster_dict[row[row_num]] = cluster_dict.get(row[row_num], 0) + 1
        
        write_cluster_files(cluster_dict, name)

#Cluster on the basis of Creator
def write_cluster_files(cluster_dict, name):
    os.makedirs("analysis",exist_ok=True)
    with open(f"analysis/{name}.csv", 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([f"{name}", "1"])
        for i in cluster_dict :
            csv_writer.writerow([i, cluster_dict[i]])

if __name__ == "__main__":
    csv_path = "meta_hindi.csv"
    csv.field_size_limit(100000000)

    print("Creating CSV cluster")
    for i in range(2, 108):
        create_csv_cluster(csv_path,i)

