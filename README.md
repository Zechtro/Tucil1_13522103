# Tucil1 - 13522103
> Tugas Besar 2 IF2123 Aljabar Linier dan Geometri 
>
> Aplikasi Aljabar Vektor dalam Sistem Temu Balik Gambar Semester I Tahun 2023/2024

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)


## General Information
- This project aims to solve the _Cyberpunk 2077 Breach Protocol_ minigame by _Brute Force_ Algorithm. The minigame simulates hacking on local network from _ICE (Intrusion Countermeasures Electronics)_ on _Cyberpunk 2077_.


## Technologies Used
- Python - version 3.11.0


## Features
- Generate matrix and sequence(s) from _CLI_ input
- Load matrix and sequence(s) information from .txt file
- Save solution into .txt file


## Screenshots
![Example screenshot](./img/1.png)

![Example screenshot](./img/2.png)


## Setup
Untuk memulai program, perlu dilakukan beberapa instalasi dan set up:
1. Activate Virtual Environment

    >In **src** directory
    >
    >Windows:
    >
    >`algeo02\Scripts\activate.bat`
    >
    >Unix/MacOS:
    >
    >`source algeo02/Scripts/activate`
    
2. Intall Django

    `pip install Django`

3. Install Numpy

    `pip install numpy`

4. Install Pillow

    `pip install Pillow`

5. Install Widget Tweaks

    `pip install django-widget-tweaks`

6. Install Whitenoise

    `pip install whitenoise`

7. RUN SERVER

    >In **src/CBIR/** directory
    >
    >`python manage.py runserver`
    >
    >After that, go to the website address where the server is running


## Usage
1. Pada Homepage, tekan tombol **START**
2. Kemudian masukkan gambar masukan yang ingin dilakukan pencarian, setelah itu tekan tombol tanda panah yang berada pada bagian kanan
3. Setelah itu masukkan kumpulan gambar yang akan dijadikan dataset, setelah itu tekan tombol tanda panah yang berada pada bagian kanan
4. Pilih parameter yang ingin digunakan (warna/tekstur), kemudian tekan tombol **SEARCH!** untuk memulai pencarian
5. Tunggu hingga hasil keluar
6. Tekan tombol **Change Image** untuk mengganti gambar masukan dan tombol **Change Dataset** untuk mengganti dataset


## Project Status
Project is: _complete_.


## Room for Improvement
- Dapat ditambahkan loading screen ketika sedang dilakukan pemrosesan gambar dataset.
