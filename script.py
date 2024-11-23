import os
import csv

nama_file = "datasets.csv"
output_file = "destinations.sql"

with open(nama_file, mode="r") as file:
    csv_reader = csv.DictReader(file)
    headers = csv_reader.fieldnames  # Menampilkan header di file CSV

    with open(output_file, mode="w") as sql_file:
        for row in csv_reader:
            image_url = row.get(headers[1])
            title = row.get(headers[2])
            state = row.get(headers[5])
            city = row.get(headers[6])
            cityTag = row.get(headers[7])
            phone = row.get(headers[8])
            categoryName = row.get(headers[9])
            description = row.get(headers[10])
            placeId = row.get(headers[11])

            bucket_link = "https://storage.googleapis.com/travelease-bucket/"
            new_image_url = (
                bucket_link + cityTag + "/" + title.replace(" ", "_").lower() + ".jpg"
            )

            sql_query = f'INSERT INTO destinations (id, title, state, city, cityTag, phone, categoryName, description, imageUrl) VALUES ("{placeId}", "{title}", "{state}", "{city}", "{cityTag}", "{phone}", "{categoryName}", "{description}", "{new_image_url}");\n'
            sql_file.write(sql_query)
