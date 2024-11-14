import csv
import requests
import os


def download_image(url, save_path):
    try:
        # Kirim permintaan GET ke URL gambar
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Memeriksa apakah permintaan berhasil

        # Menyimpan gambar ke lokasi yang ditentukan
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

        print(f"Gambar berhasil didownload dan disimpan di {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan: {e}")


nama_file = "medan.csv"

direktori_tujuan = "medan"
os.makedirs(direktori_tujuan, exist_ok=True)

with open(nama_file, mode="r") as file:
    csv_reader = csv.DictReader(file)
    headers = csv_reader.fieldnames  # Menampilkan header di file CSV
    print(headers[0])

    for row in csv_reader:
        image_url = row.get(headers[0])
        title = row.get(headers[1])
        new_format = title.replace(" ", "_").lower()
        new_title = direktori_tujuan + "/" + new_format + ".jpg"

        download_image(image_url, new_title)
