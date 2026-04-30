from bronze_config import INGESTION_CONFIG
for item in INGESTION_CONFIG:
  source_name = item['source']
  file_path = item['path']
  table_name = item['table']
print(f'processing {source_name} from {file_path} to bronze.{table_name}')

#Read csv with header and schema inference
df = spark.read.option('header', 'true').option('inferschema', 'true').csv(file_path)

#write into bronze layer
df.write.format('delta').mode('overwrite').saveAsTable(f'bronze.{table_name}')

print('All bronze ingestion completed succesfully')
