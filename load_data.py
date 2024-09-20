import pandas as pd
from pymilvus import connections, Collection, FieldSchema, DataType, CollectionSchema
from sklearn.feature_extraction.text import TfidfVectorizer

#Establishes a connection to the Milvus Database
conn = connections.connect(
    host="127.0.0.1",
    port="19530",
    db_name="default"
)

#Controls dimension of vectors
dim = 10

#Loads CSV file
df = pd.read_csv('log_data(in).csv')

#Converts Content column (originally chars) to vector format using the sci-kit learn library
vectorizer = TfidfVectorizer(max_features=dim)
vectors = vectorizer.fit_transform(df['Content']).toarray()

#Prepares data by lining up each vector with its corresponding LineId column
data = [
    {"LineId": value1, "Vector": vector.tolist()}
    for value1, vector in zip(df['LineId'], vectors)
]

#Creates field to be added to the collection. Ensure that the name of each field matches the name of each column in the csv file
fields = [
    FieldSchema(name="LineId", dtype=DataType.INT64, is_primary=True, auto_id=False),
    FieldSchema(name="Vector", dtype=DataType.FLOAT_VECTOR, dim=dim)
]

#Creates schema
schema = CollectionSchema(fields, "log_data", enable_dynamic_field=True)
collection = Collection("collection5", schema)

#Creates an index for the data which is needed to organize the data
index_params = {
    "index_type": "IVF_FLAT",
    "params": {"nlist": dim}, 
    "metric_type": "L2"
}

collection.create_index(field_name="Vector", index_param=index_params, index_name="auto_id")

#Inserts data into collection
mr = collection.insert(data)


print("data loaded!")
