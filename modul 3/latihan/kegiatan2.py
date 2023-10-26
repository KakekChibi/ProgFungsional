data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

# Fungsi ini akan memisahkan teks menjadi karakter, dan kemudian memeriksa apakah karakter tersebut adalah angka.
def extract_integers(text):
    return ''.join(filter(str.isdigit, text))

# Memisahkan setiap string dalam data menjadi karakter dan kemudian mengambil nilai integer
result = [list(extract_integers(item)) for item in data]

# Menampilkan hasil dalam format yang diminta
for item in result:
    print(item)
