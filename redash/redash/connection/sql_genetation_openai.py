import psycopg2
import openai
# Set your OpenAI API key
openai.api_key = "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"
#openai.api_key = openai.api_key = "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"
# Connect to the PostgreSQL database
conn = psycopg2.connect(
    
      'host':'localhost',
      'user': 'postgres',
      'port': '15432',
      'database': 'youtube_datas'
)
# Create a cursor object to interact with the database
cursor = conn.cursor()
try:
    # Fetch the table schema
    cursor.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'city_chart'")
    schema_rows = cursor.fetchall()
    schema = {row[0]: row[1] for row in schema_rows}
    while True:
        # Prompt for a question or enter 'exit' to end the conversation
        question = input("Enter a question or type 'exit' to end the conversation: ")
        if question.lower() == "exit":
            break
        # Generate SQL query using OpenAI
        prompt = f"Retrieve data from the 'city_chart' table based on the question: {question}."
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.5,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        sql_query = response.choices[0].text.strip()
        # Execute the SQL query
        cursor.execute(sql_query)
        result = cursor.fetchall()
        # Print the question, SQL query, SQL result, and answer
        print("Question:", question)
        print("SQL Query:", sql_query)
        print("SQL Result:", result)
        print("Answer:", response.choices[0].text.strip())
finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()