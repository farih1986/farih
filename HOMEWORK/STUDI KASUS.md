#DATA MAHASISWA YANG TIDAK MEMBAWA STNK

Seperti yang kita tahu,ketika mahasiswa politeknik harapan bersama akan keluar menggunakan motor,maka ketika di pintu keluar akan dicek STNK nya.Namun,tak jarang mahasiswa yang STNK nya tertinggal/lupa dibawa.Bagi mahasiswa yang tidak membawa STNK maka akan disuruh untuk menulis data mahasiswa tersebut pada sebuah buku yang ada pada pintu keluar.pada saat mahasiswa sedang menulis datanya,terkadang membuat antrian yang menghalangi jalan keluar.

![Untitled Diagram drawio](https://github.com/user-attachments/assets/4e49dc2b-2557-4cb8-a868-f90be9afc7b2)
# MAHASISWA YANG TIDAK MEMBAWA STNK
name = str(input(' Masukan Nama : '))
NIM = int(input('Masukan NIM : '))
alamat = str(input('Alamat : '))
prodi = str(input('Prodi : '))
jenis_motor  = str(input('Jenis Motor :'))
warna_motor = str(input('Warna Motor : '))
nomor_hp = int(input('No. HP : (+62) '))
plat_motor = str(input('Plat Motor : '))

print('Nama         :', (name))
print('Nim          :', (NIM))
print('Alamat       :',(alamat))
print('Prodi        :', (prodi))
print('Jenis Motor  :', (jenis_motor))
print('Warna Motor  :', (warna_motor))
print('No.Hp        : (+62)',(nomor_hp))
print('No.Plat Motor:', (plat_motor))
print('-Tunjukkan Ke Penjaga Pintu Keluar-')


jawaban=['sesuai', 'benar', 'oke']
petugas=input('Petugas      : ')
hasil = 'ANDA TELAH MENGISI DATA DENGAN BENAR' if (petugas in jawaban) else 'ISI ULANG DATA ANDA DENGAN BENAR'
print(hasil)
