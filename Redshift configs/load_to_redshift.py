import boto3
import json

def load_data_to_redshift():
    client = boto3.client('redshift')
    
    with open("transformed_sales_data.json", "r") as f:
        data = json.load(f)
    
    # Assume data is loaded into Redshift using COPY command or another method
    
if __name__ == "__main__":
    load_data_to_redshift()
