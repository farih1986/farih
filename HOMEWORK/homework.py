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