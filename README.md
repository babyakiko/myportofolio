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
    4. Membantu menjelaskan dan menyusun jawaban untuk *reflective questions*.
Refleksi Pengembangan: AI saya gunakan sepenuhnya sebagai sarana belajar dan pendukung. Setiap baris kode (HTML, CSS, maupun JavaScript) serta konsep yang diberikan selalu saya coba pahami terlebih dahulu. Tujuannya agar saya benar-benar menguasai materi tersebut dan kedepannya mampu membangun serta mengembangkan proyek secara mandiri tanpa ketergantungan penuh pada AI.

### Assignment 3

1. ModelForm vs Manual HTML & Fungsi {% csrf_token %}
    a. Alasan menggunakan Django ModelForm daripada membuat form HTML secara manual:
        1. Otomatisasi & Efisiensi: ModelForm secara otomatis membuat struktur *field* form berdasarkan model Django yang telah didefenisikan, sehingga mengurangi kode berulang.
        2. Validasi Bawaan: Django menangani validasi data secara otomatis sebelum disimpan ke database.
        3. Kemudahan Penyimpanan: Dengan perintah form.save(), data dari pengguna dapat langsung divalidasi dan disimpan ke database tanpa harus memetakannya satu per satu secara manual.
    b. Alasan menambahkan {% csrf_token %}: Token ini digunakan untuk melindungi aplikasi dari serangan *Cross-Site Request Forgery* (CSRF). Token yang dibuat oleh server ini memastikan bahwa *request* POST yang dikirim berasal dari halaman web yang sah dan tepercaya.

2. Keunggulan JSON dibandingkan XML dalam Pengembangan Web Modern:
    a. Lebih Ringan dan Cepat: JSON memiliki sintaks yang lebih bersih dan ukuran *file* yang lebih kecil dibandingkan XML, sehingga mempercepat proses transmisi data melalui jaringan.
    b. Kompatibilitas Asli dengan JavaScript: Karena berbasis pada objek JavaScript, JSON sangat mudah dan cepat untuk diurai langsung oleh peramban web.
    c. Keterbacaan: Struktur data JSON menggunakan format *key-value pairs* dan array yang lebih intuitif serta mudah dibaca oleh manusia dibandingkan struktur tag berlapis pada XML.

3. Alur Pengembalian Data Portofolio dalam Format JSON & Pentingnya Serialization
    a. Alur Penggunaan View Function untuk JSON:
        1. Klien (seperti peramban atau Postman) mengirimkan *request* ke *endpoint* API (misalnya /api/projects/).
        2. *View function* (seperti get_projects_json) menerima permintaan tersebut dan mengambil data dari database menggunakan *QuerySet* model Django.
        3. Data objek model diubah ke dalam bentuk teks JSON menggunakan fungsi serializers.serialize().
        4. Server mengembalikan data tersebut ke klien menggunakan HttpResponse dengan tipe konten (content_type) berupa application/json.
    b. Alasan perlu melakukan proses serialization:
        1. Objek model Django adalah objek Python kompleks yang terhubung langsung ke database dan tidak dapat dikirim secara langsung melalui protokol HTTP.
        2. Proses *serialization* berfungsi menerjemahkan objek kompleks tersebut menjadi format teks standar (JSON) yang universal, sehingga dapat dibaca dan dipahami oleh berbagai jenis klien di sisi *frontend*.

### AI Disclosure

Dalam pengerjaan portofolio ini, saya menggunakan bantuan AI sebagai sarana pembelajaran, teman diskusi, dan alat bantu *debugging*.

Alat yang digunakan: Gemini
Bagian yang dibantu: 
    1. Membantu *debugging* error Django (seperti `NoReverseMatch`) dan mengimplementasikan fitur CRUD (*form*, *view*, *URL routing*, dan *template*) untuk section *Experience*.
    2. Membantu menjelaskan dan menyusun jawaban untuk *reflective questions*.
Refleksi Pengembangan: Melalui pengerjaan tugas ini, saya mulai memahami alur dasar pengelolaan data dan pembuatan *form* di Django. Meskipun saat ini masih memerlukan bantuan untuk mengatasi kendala dan menyusun kodenya, saya berharap ke depannya saya dapat terus belajar, semakin memahami alur kerja pengembangan web secara utuh, dan mampu mengerjakannya secara mandiri tanpa ketergantungan pada AI.

### AI Disclosure Assignment 4

Dalam pengerjaan portofolio ini, saya menggunakan bantuan AI sebagai sarana pembelajaran dan alat bantu *debugging*.

Alat yang digunakan: Gemini
Bagian yang dibantu: Melakukan *debugging* dan penyesuaian tampilan CSS/layout saat posisi *button* tidak sejajar, serta memahami cara perbaikannya.
Refleksi Pengembangan: Proses *debugging* ini membantu saya memahami cara kerja perataan elemen (*alignment*) pada tampilan web. Ke depannya, saya berharap dapat menyelesaikan masalah tata letak antarmuka secara mandiri tanpa bergantung pada AI.