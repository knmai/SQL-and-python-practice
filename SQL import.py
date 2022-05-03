from google.cloud import bigquery

#create cclient pbject
client = bigquery.Client()

#construct a reference to "hacker_news" dataset
dataset_ref = client.dataset("hacker_news", project = "bigquery-public-data")

#api request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

#list all the tables in the "hacker_news" dataset
tables = list(client.list_tables(dataset))

#print names of all tables in the dataset (there are four!)
for tables in tables:
    print(table.table_id)


















