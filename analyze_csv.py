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
def write_cluster_files(cluster_dict, name, optimized = ""):
    os.makedirs("analysis",exist_ok=True)
    with open(f"analysis/{optimized}_{name}.csv", 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([f"{name}", "1"])
        for i in cluster_dict :
            csv_writer.writerow([i, cluster_dict[i]])

#Removing Punctuations and Converting to lowercase
def optimize_csv(csv_path):
    with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
        csv_file = csv.reader(csvfile)
        cluster_dict = {}
        first = 0
        for row in csv_file:
            name = row[0].lower().replace(" ","")
            for x in [',', '"' , '\'','.', ';', ':' ,'-']:
                name = name.replace(x, "")
            cluster_dict[name] = cluster_dict.get(name, 0) + int(row[1])
        
        print(len(cluster_dict))
        write_cluster_files(cluster_dict, "subject" , "optimized")


if __name__ == "__main__":
    csv_path = "analysis/_subject.csv"
    csv.field_size_limit(100000000)
    optimize_csv(csv_path)

    # print("Creating CSV cluster")
    # for i in range(2, 108):
    # create_csv_cluster(csv_path,95)



