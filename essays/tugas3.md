### Tugas 3

1. Agar lebih modular dan dinamis, lebih baik menggunakan ModelForm. {% csrf_token %} ditulis sebagai verifikasi untuk menghindari serangan Cross-Site Request Forgery.
2. Format JSON lebih mirip dengan format bahasa pemrograman modern, maka XML lebih terlihat jadul dibanding JSON. Selain itu, untuk beberapa orang (dan menurut saya sendiri), XML terlihat lebih rumit dan unfamiliar dibanding JSON.
3. Request HTTP > URL Dispatcher > View > Query Model (ORM) > Model/QuerySet Python > Serializer (JSON Conversion) > JsonResponse > Response HTTP. Ibarat kata, serialization adalah proses mengubah bahasanya django menjadi JSON/XML, dan ini perlu dilakukan.

DEKLARASI AI:
Gemini Flash 3.8 digunakan pada tugas kali ini untuk debug masalah error yang sangat confusing pada models, yang ternyata perlu ditambahkan (default=timezone.now). Selain itu, saya menggunakan tool Gemini Flash 3.6 (via web gemini) untuk menanyakan hal-hal mengenai django seperti cara untuk membuat delete dan edit. Beberapa debug-debug minor (seperti penempatan tombol yang kurang tepat) juga saya lakukan dengan AI, namun hanya sebagai last-resort. Namun, beberapa prompt yang saya berikan pada AI berada pada temporary chat, yang tidak lagi bisa saya akses.