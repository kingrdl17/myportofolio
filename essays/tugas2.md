### Tugas 2

1. user membuka /education > urls.py memanggil show_education pada view -> view memanggil model Education -> Models muncul pada template -> muncul pada    HTML -> tampil kepada user di browser
    
    urls.py (project) = Mendeklarasikan URL untuk django admin, serta mendeklarasi adanya URL lain (pada main app)
    urls.py (app) = Mendeklarasikan URL lain, serta memanggil views
    Views = sebagai 'jembatan' antara model dan template
    Model = Mendeklarasikan apa saja fields yang bisa digunakan pada suatu halaman
    Template = Menampilkan models pada website nya sendiri, dengan penempatan yang sudah ditentukan pada HTML
2. Data pada bagian portofolio sebaiknya disimpan pada model dan tidak ditulis di dalam template, karena jika hard-coded, maka sulit untuk melakukan pembaruan informasi.
3. makemigrations akan membuat berkas-berkas migration, dan migrate akan menjalankan proses migrasi tersebut dan merubah struktur database.

DEKLARASI AI:
Tools AI berupa Gemini Flash 3.6 digunakan untuk beberapa bagian dari tugas ini. AI digunakan secara bijak untuk membantu memahami dan bukan untuk sekedar memberikan jawaban tanpa berusaha untuk memahami. Pada bagian models, AI digunakan untuk menjelaskan code existing dari bagian experiences. AI juga saya gunakan untuk menjelaskan apa itu views. Selain itu, dalam proses setup admin panel Django, AI saya gunakan untuk melakukan troubleshooting pada masalah CSRF.