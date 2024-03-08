from pymongo import MongoClient
import os
import json


# client = MongoClient("mongodb://209.94.57.120:27017/")
client = MongoClient("mongodb://209.151.154.45:27017/") # for hw3
collection = client['hw2']["65b1b43bab30997971ab6f56"]
print(collection.count_documents({}))

def load_json():
    collection.delete_many({})
    parent_directory = os.getcwd()
    hw2_folder_path = os.path.join(parent_directory, 'hw2_datas')

    for dir in os.listdir(hw2_folder_path):
        dir_path = hw2_folder_path + '\\' + dir
        for (_, _, filename) in os.walk(dir_path):
            for file in filename:
                file_path = dir_path + '\\' + file
                f = open(file_path,encoding='utf-8')
                data = json.load(f)
                collection.insert_one(data)
                f.close()

    
load_json()

print(collection.count_documents({}))