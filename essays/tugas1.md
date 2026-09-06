### Tugas 1

1. Saat merancang dan menentukan tampilan dari website portofolio saya, saya perlu menggunakan elemen semantik dari HTML5 berupa <section> dan <article>. <section> memudahkan saya untuk membagi website kedalam beberapa bagian penting, serta agar bisa diakses dengan mudah melalui navigation button pada header. Elemen <article> mempermudah saya pada bagian section Education untuk membagi informasi pendidikan saya dalam beberapa 'card' agar lebih mudah disusun.
2. Saat mengatur tampilan website portofolio sesuai dengan selera saya sendiri, saya menemukan tantangan bahwa, setelah saya mengganti ukuran dan posisi photo-block, foto avatar yang ada di atasnya terlihat 'berpisah' saat berada di tampilan mobile. Saya memperbaiki masalah avatar tersebut dengan mengganti parameter position pada CSS. Selain itu, saya mengalami masalah unik pada header, karena setelah saya menambahkan line border pada container, header terlihat memiliki garis border serupa yang terlihat kurang bagus. Masalah tersebut bisa saya selesaikan dengan menambahkan "border: none;" pada ".site-header .container".
3. Walaupun untuk sekarang, saya tidak mengalami batasan pada static web murni, namun saya ingin agar bisa memperbarui konten pada website secara dinamis tanpa harus meng-update kode pada website. Misalkan saya akan membuat section baru yang berupa project-project saya, yang bisa langsung saya perbarui ketika ada project baru.

DEKLARASI AI:
Tools AI berupa Gemini Flash 3.6 digunakan untuk beberapa elemen dalam website ini, seperti pada bagian border-radius, warna, efek blur, serta efek "glow" pada tombol social. Metode prompting saya berupa pertanyaan, bukan suruhan. Dan hasil dari AI saya gunakan sebagai suggestion dan informasi, bukan saya copy-paste secara mentah-mentah. Pada bagian education, saya menggunakan AI untuk membantu saya menyusun konten di dalam website. Namun, setelah saya mengikuti suggestion dari AI, saya menemukan kesalahan pada penempatan tulisan "Education" yang seharusnya berada di bagian paling atas pada section, setelah itu, saya menginspeksi kode yang diberikan AI dan saya membuat ulang struktur yang diberikan sehingga masalah tersebut hilang.

Beberapa prompt yang saya gunakan:
"how do i make my website look similar to apple's design language"
"how do i add a glow effect to a text in css"
"how do i put a row of contents in a section with article in css"
".kicker-comp{
    color: #ff0000;
}

.kicker-science{
    color: #002aff;
}

how do i make these red and blue csui colors more subtle in dark mode"
