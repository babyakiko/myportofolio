Nama : Baby Akiko Gracia
NPM : 2506625224
Kelas : PBP C

### Assignment 1

1. Saya menggunakan elemen HTML5 seperti <header>, <main>, <section>, <nav>, <footer> serta elemen deskripsi terstruktur seperti <dl>, <dt>, dan <dd>.

2. Tantangan yang saya hadapi adalah saat mengatur ukuran image education, image yang saya gunakan latar belakangnya transparan dan ternyata karena itu saat saya membuka web portofolio di mobile, imagenya malah kegedean. Untuk mengatasi hal tersebut saya mencoba untuk mengecilkan ukuran image dan akhirnya menambahkan style pada bagian HTML agar masalah tersebut teratasi.

3. Saya merasa masih banyak kekurangan dari web ini, mungkin dari segi visual, contact person, dll. Untuk selanjutnya saya berniat untuk menambahkan fitur contact person.

### AI Disclosure

Dalam pengerjaan portofolio ini, saya menggunakan bantuan AI sebagai sarana pembelajaran dan alat bantu *debugging*.

Alat yang digunakan: Gemini
Bagian yang dibantu: 
    1. Mempelajari dasar elemen semantik pada HTML, dan mengatur *layout* pada CSS
    2. Membantu menyelesaikan kendala saat terjadi *error* terutama pada bagian image education 
    3. Membantu dalam melakukan perintah Git 
Refleksi Pengembangan: AI saya gunakan sebagai sarana belajar. Setiap kode HTML dan CSS saya coba pahami dan pelajari agar saya benar-benar bisa menguasainya dan kedepannya bisa membuat kode secara mandiri.

### Assignment 2

1.  a. urls.py proyek: Mengarahkan url global masuk ke aplikasi yang sesuai
    b. urls.py aplikasi: Memetakan sub-jalur khusus aplikasi ke view yang benar
    c. view: Sebagai penghubung, berfungsi untuk mengambil data dan menyiapkannya untuk ditampilkan
    d. model: Mendefinisikan struktur basis data serta mengelola pengambilan dan penyimpanan data
    e. template: Menentukan tampilan visual dan struktur HTML yang disajikan kepada user

2. Model vs. Menulis data langsung (*Hardcode*) di template:
    Pengaruh terhadap pemeliharaan (*Maintenance*):
    a. Pembaruan Dinamis: Dengan menggunakan model, kita dapat mengubah, menambah, atau menghapus proyek portofolio melalui dasbor admin tanpa harus menyentuh kode sumber lagi.
    b. Kode yang lebih bersih: Penulisan langsung (*Hardcode*) mencaampur adukkan data, jika mengubah satu judul saja kita harus membongkar file HTML yang berisiko menimbulkan kesalahan sintaksis.

    Pengaruh terhadap pengembangan masa depan:
    a. Skalabilitas: Jika portofolio berkembang dari 5 proyek menjadi 100 proyek, sebuah model dapat menangani penomoran halaman dan penyaringan dengan mudah.
    b. Perluasan fitur: Model memudahkan implementasi fitur di kemudian hari.

3. Perbedaan antara makemigrations dan migrate:
    a. makemigrations: Bertindak sebagai *blueprint* (pembuat cetak biru). Perintah ini memeriksa file models.py untuk melihat apakah ada perubahan, lalu mengemas perubahan tersebut ke dalam file baru di dalam folder migrations/.
    b. migrate: Bertindak sebagai eksekutor. Perintah ini mengambil file yang dihasilkan makemigrations dan menerapkannya ke basis data fisik, dengan menjalankan perintah SQL untuk membuat atau mengubah tabel basis data yang sebenarnya. 

### AI Disclosure

Dalam pengerjaan portofolio ini, saya menggunakan bantuan AI sebagai sarana pembelajaran, teman diskusi, dan alat bantu *debugging*.

Alat yang digunakan: Gemini
Bagian yang dibantu: 
    1. Membantu mengubah desain CSS serta menambahkan elemen hiasan seperti kaomoji.
    2. Membantu membuat fitur pop-up pada section proyek. 
    3. Membantu dalam melakukan perintah Git 
    4. Membantu menjelaskan dan menyusun jawaban untuk reflective questions.
Refleksi Pengembangan: AI saya gunakan sepenuhnya sebagai sarana belajar dan pendukung. Setiap baris kode (HTML, CSS, maupun JavaScript) serta konsep yang diberikan selalu saya coba pahami terlebih dahulu. Tujuannya agar saya benar-benar menguasai materi tersebut dan kedepannya mampu membangun serta mengembangkan proyek secara mandiri tanpa ketergantungan penuh pada AI.