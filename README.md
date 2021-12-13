# hotel-guest-forecast

## Deskripsi singkat

Repository ini berisi semua file yang dibutuhkan untuk melakukan deployment model Machine Learning ARIMA. Adapun model yang digunakan merupakan model untuk memprediksi jumlah tamu pada hotel berbintang mulai dari bulan oktober 2021.

#

## Folder, file, dan kegunaannya

- notebook/
    - Data/
        - JakartaHotel.csv --> Data tamu hotel bintang pada provinsi DKI Jakarta yang telah melalui proses Data preparation
        - TamuHotelBintang.xlsx --> Data tamu hotel bintang seluruh provinsi yang belum melalui proses apapun (Data asli)
    - Data Preparation.ipynb --> Notebook yang berisi proses Data Preparation yang kami lakukan pada Data
    - Modelling.ipynb --> Notebook yang berisi proses modelling ARIMA.
- templates/
    - index.html --> Berisi template website
- ProcFile --> File untuk menjalankan python web app pada heroku
- app.py --> Berisi konfigurasi route untuk API
- model.pkl --> Model ARIMA yang sudah di-training
- requirements.txt --> Berisi daftar dependency/package Python yang diperlukan untuk menjalankan API dan model ARIMA

#

## Cara menjalankan API pada komputer Anda

### Menjalankan API

Pastikan Anda sudah menginstall Anaconda
Buka terminal/command prompt/power shell
Buat virtual environment dengan
`conda create -n <nama-environment> python=3.9`
Aktifkan virtual environment dengan
`conda activate <nama-environment>`
Install semua dependency/package Python dengan
`pip install -r requirements.txt`
Jalankan API menggunakan perintah
`python app.py`

### Akses melalui Website
1. Anda akan diberikan URL untuk membuka website berupa `localhost:5000/` atau `127.0.0.1:5000/`
1. Atau anda bisa mencoba mengakses halaman web yang telah kami bangun `https://guest-forecast.herokuapp.com/`
1. Buka URL dengan browser, coba masukkan periode waktu yang ingin di prediksi
1. Anda akan diberikan estimasi jumlah tamu pada periode yang anda masukan pada chart yang berada di sisi kanan halaman website
