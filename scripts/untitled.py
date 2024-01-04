import psycopg2
import csv
from psycopg2 import sql

class DatabaseConnector:
    # ... (unchanged code)

    def load_csv_to_table(self, table_name, csv_file_path):
        try:
            with self.connection.cursor() as cursor:
                with open(csv_file_path, 'r') as f:
                    # Assuming the CSV file has a header
                    reader = csv.DictReader(f)
                    columns = reader.fieldnames

                    # Create a temporary table for bulk loading
                    temp_table_name = f"temp_{table_name}"
                    create_temp_table_query = sql.SQL("CREATE TEMP TABLE {} ({});").format(
                        sql.Identifier(temp_table_name),
                        sql.SQL(', ').join(sql.Identifier(column) for column in columns)
                    )
                    cursor.execute(create_temp_table_query)

                    # Copy data from CSV to the temporary table
                    copy_data_query = sql.SQL("COPY {} FROM %s WITH CSV HEADER;").format(
                        sql.Identifier(temp_table_name)
                    )
                    cursor.copy_expert(copy_data_query, f)

                    # Insert data from the temporary table to the target table
                    insert_data_query = sql.SQL("INSERT INTO {} SELECT * FROM {};").format(
                        sql.Identifier(table_name),
                        sql.Identifier(temp_table_name)
                    )
                    cursor.execute(insert_data_query)

                    # Drop the temporary table
                    drop_temp_table_query = sql.SQL("DROP TABLE {};").format(
                        sql.Identifier(temp_table_name)
                    )
                    cursor.execute(drop_temp_table_query)

            print(f"Data from CSV file '{csv_file_path}' loaded into table '{table_name}'.")
        except Exception as e:
            print(f"Error loading data from CSV: {e}")

# Example Usage:
db_connector = DatabaseConnector(
    host='your_host',
    database='your_database',
    user='your_user',
    password='your_password',
    port='your_port'
)

db_connector.connect()

# Example: Load CSV data into 'your_table'
csv_file_path = '/path/to/your/file.csv'
db_connector.load_csv_to_table(table_name='your_table', csv_file_path=csv_file_path)

# Example Query
query = sql.SQL("SELECT * FROM your_table;")
result = db_connector.execute_query(query)

if result:
    for row in result:
        print(row)

db_connector.close_connection()
