import sqlite3
import csv

db = sqlite3.connect("database.sqlite")
cursor = db.cursor()

cursor.execute('''select a.name as author_name, 
                         p.year as publish_year,
                         p.title as paper_title, 
                         p.pdf_name as pdf_name, 
                         p.abstract as paper_abstract, 
                         p.paper_text as paper_text
                   from paper_authors
                       inner join authors a on a.id = paper_authors.author_id
                       inner join papers p on p.id = paper_authors.paper_id;''')

with open("data.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=";")
    csv_writer.writerow([i[0] for i in cursor.description])
    csv_writer.writerows(cursor)

cursor.close()
