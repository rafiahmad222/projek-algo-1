import csv
import os
from pathlib import Path
import pandas as pd
from datetime import datetime, timedelta, date
import time
from prettytable import PrettyTable
#tampilan loading
def loading(text):
    for i in range(7):
        print("\r{0}  {1}".format(text,"."*i),end="")
        time.sleep(0.5)
        
 # fitur registrasi       
def register():
    os.system('cls')
    print(" ========================================")
    print(" Silahkan Registrasi")
    print(" ========================================")
    username= (input("Masukkan username = "))
    kondisi = False
    data = []
    
    with open('data_user.csv', 'r') as file:
        csv_user = csv.reader(file, delimiter=',')
        for row in csv_user:
            data.append({'username': row[0]})
    
    for row in data:
        if row['username'] == username:
            kondisi = True
            break
        
    if kondisi:
        os.system('cls')
        print("========================================")
        print("Username sudah terdaftar")
        print("Silahkan registrasi dengan username lain")
        print("========================================")
        loading("Kembali ke menu registrasi")
        register()
    
    else:
        password= (input("Masukkan password = "))
        with open('data_user.csv', 'a', newline='') as file:
            csv_user = csv.writer(file, delimiter=',')
            csv_user.writerow([username,password])
            file.close()
            
    print("========================================")
    loading("Registrasi Berhasil")
    os.system('cls')
    loading("Masuk ke menu login")
    login()
#fitur login
def login():
    os.system('cls')
    print("========================================")
    print("Silahkan Login")
    print("========================================")
    username= (input(" Masukkan username = "))
    password= (input(" Masukkan password = "))
    kondisi = False
    data = []
    
    with open('data_user.csv', 'r') as file:
        data_user = csv.reader(file, delimiter=',')
        for row in data_user:
            data.append({'username': row[0], 'password': row[1]})
        print(data_user)
    
    for row in data:
        if row['username'] == username and row['password'] == password:
            kondisi = True
            break
        
    if not kondisi:
        os.system('cls')
        print("========================================")
        print("Username atau password salah")
        print("========================================")
        loading("Kembali ke menu login")
        login()
    else:
        os.system('cls')
        print("========================================")
        print("Login Berhasil")
        os.system('cls')
        loading("Masuk ke menu utama")
        os.system('cls')
        menu_utama()
        
#fitur menampilkan data
def tampilkan_data():
    dataproduk = pd.read_csv('dataproduk.csv')      
    dataproduk.index = range(1, len(dataproduk)+1)
    tabel = PrettyTable()
    tabel.field_names = dataproduk.columns.tolist()
    for i in dataproduk.values:
        tabel.add_row(i)
    
    print(tabel)
                    
 # fitur pencatatan produk   
def tambahdata():
    os.system('cls')
    with open('dataproduk.csv', 'a', newline='') as file:
        tambah = csv.writer(file, delimiter=',')
        nama = input("Masukkan Nama Produk: ")
        namapemilik = input("Masukkan Nama Pemilik Produk:")
        jenisProduk = input("Masukkan Jenis Produk: ")
        harga = input("Masukkan Harga Produk: ")
        stok = input("Masukkan Stok Produk: ")
        inputan = int(input("Masukan Berapa Hari Expired: "))
        hari = datetime.now().date()
        expireddate = hari + timedelta(days=inputan)
        tambah.writerow([
            nama,namapemilik,jenisProduk,harga,stok,expireddate,
            ])
        file.close()
        loading("Menambahkan Data")
        os.system('cls')
        print("Data berhasil ditambahkan!")
        input("Tekan Enter untuk kembali ke menu")
        menu_pencatatan()
        
def lihatdata():
    os.system('cls')
    loading("Menampilkan Data")
    os.system('cls')
    tampilkan_data()
    inputan = int(input('Ada yang ingin dicari ketik 1(tekan 0 untuk kembali)'))
    if inputan == 1:
        nama = input("Masukkan Nama Produk yang ingin dicari: ")
        cari = pd.read_csv('dataproduk.csv')
        cari_nama = nama
        hasil = cari[cari['nama'].str.contains(cari_nama, na=False)]
        hasil.index = range(1, len(hasil)+1)
        print(hasil)
    elif inputan == 0:
        menu_pencatatan()
    else :
        print('Inputan Tidak Memenuhi')
        lihatdata()
    input("Tekan enter untuk kembali")
    menu_pencatatan()
    
def hapusdata():   
    os.system('cls')
    tampilkan_data()
    inputan = int(input('Ada yang ingin dicari ketik 1(tekan 0 untuk kembali)'))
    if inputan == 1:
        nama = input("Masukkan Nama Produk yang ingin dicari: ")
        cari = pd.read_csv('dataproduk.csv')
        cari_nama = nama
        hasil = cari[cari['nama'].str.contains(cari_nama, na=False)]
        hasil.index = range(1, len(hasil)+1)
        print(hasil)
        hapus = int(input("pilih nomor yang ingin dihapus : "))
        dataproduk = cari.drop(hapus)
        cari.reset_index(drop=True, inplace=True)
        dataproduk.to_csv('dataproduk.csv', index=False)
        loading("Menghapus Data")
        os.system('cls')
        print("Data berhasil dihapus")
        input("\n enter untuk lanjutkan")
        menu_pencatatan()
    elif inputan == 0:
        menu_pencatatan()
    else :
        print('Inputan Tidak Memenuhi')
        hapusdata()
    
def editdata(): 
    os.system('cls')
    loading("Menampilkan Data")
    os.system('cls')
    tampilkan_data()
    df = pd.read_csv('dataproduk.csv')
    pilihan = input('Ada yang ingin dicari ketik 1(tekan 0 untuk kembali)')
    if pilihan == "1":
        nama = input("Masukkan Nama Produk yang ingin dicari: ")
        cari = pd.read_csv('dataproduk.csv')
        cari_nama = nama
        hasil = cari[cari['nama'].str.contains(cari_nama, na=False)]
        hasil.index = range(1, len(hasil)+1)
        print(hasil)
        edit = int(input("pilih nomor yang ingin diedit : "))
        print("1. Nama Produk")
        print("2. Nama Pemilik Produk")
        print("3. Jenis Produk")
        print("4. Harga Produk")
        print("5. Stok Produk")
        print("6. Expired Date")
        print("7. Kembali")
        pilihan = input("Pilih Yang Ingin Diedit [1/2/3/4/5/6] :")
        if pilihan == "1" :
            nama = input("Masukkan Nama Produk: ")
            df.at[edit-1, 'nama'] = nama
            df.to_csv('dataproduk.csv', index=False)
            loading("Mengedit Data")
            os.system('cls')
            print("Data berhasil diubah!")
            input("Tekan Enter untuk kembali ke menu")
            editdata()
        elif pilihan == "2" :
            namapemilik = input("Masukkan Nama Pemilik Produk: ")
            df.at[edit-1, 'namapemilik'] = namapemilik
            df.to_csv('dataproduk.csv', index=False)
            loading("Mengedit Data")
            os.system('cls')
            print("Data berhasil diubah!")
            input("Tekan Enter untuk kembali ke menu")
            editdata()    
        elif pilihan == "3" :
            jenisProduk = input("Masukkan Jenis Produk: ")
            df.at[edit-1, 'jenisProduk'] = jenisProduk
            df.to_csv('dataproduk.csv', index=False)
            loading("Mengedit Data")
            os.system('cls')
            print("Data berhasil diubah!")
            input("Tekan Enter untuk kembali ke menu")
            editdata()
        elif pilihan == "4" :
            harga = input("Masukkan Harga Produk: ")
            df.at[edit-1, 'harga'] = harga
            df.to_csv('dataproduk.csv', index=False)
            loading("Mengedit Data")
            os.system('cls')
            print("Data berhasil diubah!")
            input("Tekan Enter untuk kembali ke menu")
            editdata()
        elif pilihan == "5" :
            stok = input("Masukkan Stok Produk: ")
            df.at[edit-1, 'stok'] = stok
            df.to_csv('dataproduk.csv', index=False)
            loading("Mengedit Data")
            os.system('cls')
            print("Data berhasil diubah!")
            input("Tekan Enter untuk kembali ke menu")
            editdata()
        elif pilihan == "6" :
            inputan = int(input("Masukan Hari: "))
            hari = datetime.now().date()
            expired = hari + timedelta(days=inputan)
            df.at[edit-1, 'expireddate'] = expired
            df.to_csv('dataproduk.csv', index=False)
            loading("Mengedit Data")
            os.system('cls')
            print("Data berhasil diubah!")
            input("Tekan Enter untuk kembali ke menu")
            editdata()
        elif pilihan == "7" :
            menu_pencatatan()
        else:
            print("Pilihan tidak tersedia")
            input("Tekan Enter untuk kembali ke menu")
            editdata()
    elif pilihan == "0":
        menu_pencatatan()
    


        
#fitur pembelian 
def tambah_pembelian():
    os.system('cls')
    data = pd.read_csv('dataproduk.csv')
    print(data)
    nama = (input("Masukkan Nama Produk Yang Ingin Dibeli: "))
    kondisi = False
    
    data = []
    with open('dataproduk.csv', 'r') as file:
        dataproduk = csv.reader(file, delimiter=',')
        for row in dataproduk:
            data.append({'nama': row[0],'namapemilik': row[1],'jenisbarang': row[2],'harga': row[3],'stok': row[4],'expireddate': row[5]})
    
    for row in data:
        if row['nama'] == nama:
            kondisi = True
            break
        
    if kondisi:
        namapemilik = data[1]
        jenisbarang = data[2]
        harga = data[3]
        jumlah =(input("Masukkan Jumlah Produk: "))
        total =int(harga) * int(jumlah)
        data = pd.read_csv('dataproduk.csv')
        barang = data.loc[data['nama'] == nama]
        stok =(barang['stok'])
        if barang['stok']:
            stok = stok - (jumlah)
            data.loc[data['nama'] == nama, 'stok'] = stok
            data.to_csv('dataproduk.csv', index=False)
        with open('datapembelian.csv', 'a', newline='') as file:
            datapenjualan = csv.writer(file, delimiter=',')
            datapenjualan.writerow([
                nama, namapemilik, jenisbarang, harga, jumlah, total
                ])
            file.close()
            loading("Menambahkan Data")
            os.system('cls')
            print("Data Penjualan berhasil ditambahkan!")
            input("Tekan Enter untuk kembali ke menu")
            menu_pembelian()    
            
    else:
        print("Nama Produk Tidak Terdaftar, Silahkan Masukkan Nama Produk Yang Ingin Dijual")
        nama = input("Masukkan Nama Produk Yang Ingin Dijual: ")
        namapemilik = input("Masukkan Nama Pemilik Produk: ")
        jenisbarang = input("Masukkan Jenis Produk: ")
        harga = input("Masukkan Harga Produk: ")
        stok = input("Masukkan Jumlah Produk: ")
        inputan = int(input("Masukan Berapa Hari Expired: "))
        hari = datetime.now().date()
        expireddate = hari + timedelta(days=inputan)
        total = int(harga) * int(stok)
        with open('dataproduk.csv', 'a', newline='') as file:
            dataproduk = csv.writer(file, delimiter=',')
            dataproduk.writerow([
                nama, namapemilik, jenisbarang, harga, stok, expireddate
                ])
            file.close()
        with open('datapembelian.csv', 'a', newline='') as file:
            datapenjualan = csv.writer(file, delimiter=',')
            datapenjualan.writerow([
                nama, namapemilik, jenisbarang, harga, stok, total
                ])
            file.close()
            loading("Menambahkan Data")
            os.system('cls')
            print("Data Penjualan berhasil ditambahkan!")
            input("Tekan Enter untuk kembali ke menu")
            menu_penjualan()
    
def edit_pembelian():
    os.system('cls')    
    dataproduk = pd.read_csv('datapembelian.csv')
    dataproduk.index = range(1, len(dataproduk)+1)
    tabel = PrettyTable()
    tabel.field_names = dataproduk.columns.tolist()
    for i in dataproduk.values:
        tabel.add_row(i)
        
    print(tabel)
    df=pd.read_csv('datapembelian.csv')
    edit = int(input("pilih nomor yang ingin diedit : "))
    print("========================================")
    print("1. Jumlah Produk")
    print("2. Harga")
    print("3. Kembali")
    pilihan = int(input("Pilih Yang Ingin Diedit [1/2/3] :"))
    if pilihan == 1:
        jumlah = int(input("Masukkan Jumlah Produk: "))
        df.at[edit-1, 'jumlah'] = jumlah
        data = pd.read_csv('datapembelian.csv')
        nama = data.loc[data['nama'] == edit]
        stok = data.at[edit-1,'jumlah']
        harga = data.at[edit-1,'harga']
        total = jumlah * harga
        df.at[edit-1,'total'] = total
        if int(stok) > 0 :
            stok_barang = int(stok) + int(jumlah)
            data.loc[data['nama'] == edit, 'stok'] = stok_barang
            data.to_csv('dataproduk.csv', index=False)
        df.to_csv('datapembelian.csv', index=False)
        loading("Mengedit Data")
        print("Data berhasil diubah!")
        input("Tekan Enter untuk kembali ke menu")
        edit_pembelian()
    elif pilihan == 2:
        harga = int(input('Masukan perubahan harga: '))
        df.at[edit-1, 'harga'] = harga
        jumlah = df.at[edit-1,'jumlah']
        total = int(jumlah) * int(harga)
        df.at[edit-1, 'total'] = total
        df.to_csv('datapembelian.csv', index=False)
        loading("Mengedit Data")
        print("Data berhasil diubah!")
        input("Tekan Enter untuk kembali ke menu")
        edit_pembelian()
    elif pilihan == 3:
        menu_pembelian()
    else:
        print("Pilihan tidak tersedia")
        input("Tekan Enter untuk kembali ke menu")
        edit_pembelian()
        
def hapus_pembelian():
    dataproduk = pd.read_csv('datapembelian.csv')      
    dataproduk.index = range(1, len(dataproduk)+1)
    tabel = PrettyTable()
    tabel.field_names = dataproduk.columns.tolist()
    for i in dataproduk.values:
        tabel.add_row(i)
    
    print(tabel)
    df = pd.read_csv('datapembelian.csv')
    hapus = int(input("pilih nomor yang ingin dihapus : "))
    dataproduk = df.drop(hapus-1)
    df.reset_index(drop=True, inplace=True)
    dataproduk.to_csv('datapenjualan.csv', index=False)
    loading("Menghapus Data")
    print("Data berhasil dihapus")
    input("\n enter untuk lanjutkan")
    menu_pembelian()
    
def struk_pembelian():
    datapembelian = pd.read_csv('datapembelian.csv')
    data_struk = []
    for row in datapembelian.values(range(len(datapembelian)+1)):
        data_struk.append({
            'nama': row[0],'namapemilik': row[1],'jenisbarang': row[2],'harga': row[3], 
            'jumlah': row[4], 'total': row[5]
                    })
    print('\n===================================',
              "\nnama               : ", row[0],
              "\njenis barang       : ", row[2],
              '\njumlah             : ', row[4],
              '\nharga              : ', row[3],
              '\n===================================\n'
              '\nTotal Harga        : Rp', row[5], '\n\n===================================')
    print("Struk Penjualan berhasil ditambahkan!")
    input("Tekan Enter untuk kembali ke menu")
    menu_pembelian()
    
#fitur penjualan
def tambah_penjualan():
    os.system('cls')
    data = pd.read_csv('dataproduk.csv')
    print(data)
    nama = (input("Masukkan Nama Produk Yang Ingin Dijual: "))
    
    kondisi = False
    
    data = []
    with open('dataproduk.csv', 'r') as file:
        dataproduk = csv.reader(file, delimiter=',')
        for row in dataproduk:
            data.append({'nama': row[0],'namapemilik': row[1],'jenisbarang': row[2],'harga': row[3],'stok': row[4],'expireddate': row[5]})
    
    for row in data:
        if row['nama'] == nama:
            kondisi = True
            break
        
    if kondisi:
        namapemilik = data[1]
        jenisbarang = data[2]
        harga = data[3]
        jumlah =(input("Masukkan Jumlah Produk: "))
        total =int(harga) * int(jumlah)
        data = pd.read_csv('dataproduk.csv')
        barang = data.loc[data['nama'] == nama]
        stok =(barang['stok'])
        if barang['stok']:
            stok = stok + (jumlah)
            data.loc[data['nama'] == nama, 'stok'] = stok
            data.to_csv('dataproduk.csv', index=False)
        with open('datapenjualan.csv', 'a', newline='') as file:
            datapenjualan = csv.writer(file, delimiter=',')
            datapenjualan.writerow([
                nama, namapemilik, jenisbarang, harga, jumlah, total
                ])
            file.close()
            loading("Menambahkan Data")
            os.system('cls')
            print("Data Penjualan berhasil ditambahkan!")
            input("Tekan Enter untuk kembali ke menu")
            menu_penjualan()    
            
    else:
        print("Nama Produk Tidak Terdaftar, Silahkan Masukkan Nama Produk Yang Ingin Dijual")
        nama = input("Masukkan Nama Produk Yang Ingin Dijual: ")
        namapemilik = input("Masukkan Nama Pemilik Produk: ")
        jenisbarang = input("Masukkan Jenis Produk: ")
        harga = input("Masukkan Harga Produk: ")
        stok = input("Masukkan Jumlah Produk: ")
        inputan = int(input("Masukan Berapa Hari Expired: "))
        hari = datetime.now().date()
        expireddate = hari + timedelta(days=inputan)
        total = int(harga) * int(stok)
        with open('dataproduk.csv', 'a', newline='') as file:
            dataproduk = csv.writer(file, delimiter=',')
            dataproduk.writerow([
                nama, namapemilik, jenisbarang, harga, stok, expireddate
                ])
            file.close()
        with open('datapenjualan.csv', 'a', newline='') as file:
            datapenjualan = csv.writer(file, delimiter=',')
            datapenjualan.writerow([
                nama, namapemilik, jenisbarang, harga, stok, total
                ])
            file.close()
            loading("Menambahkan Data")
            os.system('cls')
            print("Data Penjualan berhasil ditambahkan!")
            input("Tekan Enter untuk kembali ke menu")
            menu_penjualan()
    
def edit_penjualan():
    os.system('cls')    
    dataproduk = pd.read_csv('datapenjualan.csv')
    dataproduk.index = range(1, len(dataproduk)+1)
    tabel = PrettyTable()
    tabel.field_names = dataproduk.columns.tolist()
    for i in dataproduk.values:
        tabel.add_row(i)
        
    print(tabel)
    df=pd.read_csv('datapenjualan.csv')
    edit = int(input("pilih nomor yang ingin diedit : "))
    print("========================================")
    print("1. Jumlah Produk")
    print("2. Harga")
    print("3. Kembali")
    pilihan = int(input("Pilih Yang Ingin Diedit [1/2/3] :"))
    if pilihan == 1:
        jumlah = int(input("Masukkan Jumlah Produk: "))
        df.at[edit-1, 'jumlah'] = jumlah
        data = pd.read_csv('datapenjualan.csv')
        nama = data.loc[data['nama'] == edit]
        stok = data.at[edit-1,'jumlah']
        harga = data.at[edit-1,'harga']
        total = jumlah * harga
        df.at[edit-1,'total'] = total
        #print(total)
        #print(f"stoknya adalah : {stok}")
        if int(stok) > 0 :
            stok_barang = int(stok) + int(jumlah)
            data.loc[data['nama'] == edit, 'stok'] = stok_barang
            data.to_csv('dataproduk.csv', index=False)
        df.to_csv('datapenjualan.csv', index=False)
        loading("Mengedit Data")
        print("Data berhasil diubah!")
        input("Tekan Enter untuk kembali ke menu")
        edit_penjualan()
    elif pilihan == 2:
        harga = int(input('Masukan perubahan harga: '))
        df.at[edit-1, 'harga'] = harga
        jumlah = df.at[edit-1,'jumlah']
        total = int(jumlah) * int(harga)
        df.at[edit-1, 'total'] = total
        df.to_csv('datapenjualan.csv', index=False)
        loading("Mengedit Data")
        print("Data berhasil diubah!")
        input("Tekan Enter untuk kembali ke menu")
        edit_penjualan()
    elif pilihan == 3:
        menu_penjualan()
    else:
        print("Pilihan tidak tersedia")
        input("Tekan Enter untuk kembali ke menu")
        edit_penjualan()
        
def hapus_penjualan():
    dataproduk = pd.read_csv('datapenjualan.csv')      
    dataproduk.index = range(1, len(dataproduk)+1)
    tabel = PrettyTable()
    tabel.field_names = dataproduk.columns.tolist()
    for i in dataproduk.values:
        tabel.add_row(i)
    
    print(tabel)
    df = pd.read_csv('datapenjualan.csv')
    hapus = int(input("pilih nomor yang ingin dihapus : "))
    dataproduk = df.drop(hapus-1)
    df.reset_index(drop=True, inplace=True)
    dataproduk.to_csv('datapenjualan.csv', index=False)
    loading("Menghapus Data")
    print("Data berhasil dihapus")
    input("\n enter untuk lanjutkan")
    menu_penjualan()
    
def struk_penjualan():
    datapenjualan = pd.read_csv('datapenjualan.csv')
    data_struk = []
    for row in datapenjualan.values(range(len(datapenjualan)+1)):
        data_struk.append({
            'nama': row[0],'namapemilik': row[1],'jenisbarang': row[2],'harga': row[3], 
            'jumlah': row[4], 'total': row[5]
                    })
    print('\n===================================',
              "\nnama               : ", row[0],
              "\njenis barang       : ", row[2],
              '\njumlah             : ', row[4],
              '\nharga              : ', row[3],
              '\n===================================\n'
              '\nTotal Harga        : Rp', row[5], '\n\n===================================')
    print("Struk Penjualan berhasil ditambahkan!")
    input("Tekan Enter untuk kembali ke menu")
    menu_penjualan()

#menu pencaatatan produk
def menu_pencatatan():
    os.system('cls')
    print("===Selamat Datang===")
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Hapus Data")
    print("4. Edit Data")
    print("5. Kembali")
    pilihan = input("Pilih Menu [1/2/3/4/5] :")
    if pilihan == "1" :
        if not(Path('dataproduk.csv').is_file()):
            with open('dataproduk.csv', 'w', newline='') as filecsv:
                header = csv.DictWriter(filecsv, fieldnames=[
                    'nama','namapemilik','jenisbarang','harga','stok','expireddate'
                    ],  delimiter=',') 
                header.writeheader()
        tambahdata()
    if pilihan == "2" :
        lihatdata()
    if pilihan == "3" :
        hapusdata()
    if pilihan == "4" :
        editdata()
    if pilihan == "5" :
        menu_utama()
        
#menu pembelian
def menu_pembelian():
    os.system('cls')
    print("========================================")
    print("Selamat Datang di KoperasiNovasi")
    print("========================================")
    print("1. Tambahan Data Pembelian")
    print("2. Edit Data Pembelian")
    print("3. Hapus Data Pembelian")
    print("4. Struk Pembelian")
    print("5. Kembali")
    pilihan = input("Pilih Menu [1/2/3/4] :")
    if pilihan == "1": 
        tambah_pembelian()
    elif pilihan == "2":
        edit_pembelian()
    elif pilihan == "3":
        hapus_pembelian()
    elif pilihan == "4":
        struk_pembelian()
    elif pilihan == "5":
        menu_utama()    

#fitur absensi
def menu_absensi():
    os.system('cls')
    with open('data_absensi.csv', 'a', newline='' ) as file:
        namakaryawan = input("Nama Karyawan: ")
        shift = input("Shift[pagi/siang]: ")
        tanggal = datetime.now().strftime("%Y-%m-%d")
        waktu = datetime.now().strftime("%H:%M:%S")
        if shift == "pagi":
            if waktu < "7:00:00":
                absen = "Terlambat"
            else:
                absen = "Hadir"
        elif shift == "siang":
            if waktu < "13:00:00":
                absen = "Terlambat"
            else:
                absen = "Hadir"
        else :
            print("Shift Tidak Sesuai")
            menu_absensi()
        data_absensi = csv.writer(file, delimiter=',')
        data_absensi.writerow([
            namakaryawan,shift,tanggal,waktu,absen
            ])
        file.close()
        print("========================================")
        print("Nama Karyawan:",namakaryawan)
        print("Shift        :",shift)
        print("Tanggal      :",tanggal)
        print("Waktu        :",waktu)
        print("Absen        :",absen)
        print("========================================")
        loading("Menambahkan Data Absensi")
        os.system('cls')
        print("Absensi berhasil!")
        input("Tekan Enter untuk kembali ke menu")
        menu_utama()

#menu penjualan
def menu_penjualan():
    os.system('cls')
    print("========================================")
    print("Selamat Datang di KoperasiNovasi")
    print("========================================")
    print("1. Tambahan Data Penjualan")
    print("2. Edit Penjualan")
    print("3. Hapus Data Penjualan")
    print("4. Struk Data Penjualan")
    print("5. Kembali")
    pilihan = input("Pilih Menu [1/2/3] :")
    if pilihan == "1":
        tambah_penjualan()
    if pilihan == "2":
        edit_penjualan()
    if pilihan == "3":
        hapus_penjualan()
    if pilihan == "4":
        struk_penjualan()
    if pilihan == "5":
        menu_utama()
        
#menu transaksi
def menu_transaksi():
    os.system('cls')
    print("========================================")
    print("Selamat Datang di KoperasiNovasi")
    print("========================================")
    print("1. Penjualan")
    print("2. Pembelian")
    print("3. Kembali")
    pilihan = input("Pilih Menu [1/2/3] :")
    if pilihan == "1" :
        if not(Path('datapenjualan.csv').is_file()):
            with open('datapenjualan.csv', 'w', newline='') as filecsv:
                    header = csv.DictWriter(filecsv, fieldnames=[
                    'nama','namapemilik','jenisbarang','harga','jumlah','total'
                    ],  delimiter=',')
                    header.writeheader()
        menu_penjualan()
    if pilihan == "2" :
        if not(Path('datapembelian.csv').is_file()):
            with open('datapembelian.csv', 'w', newline='') as filecsv:
                    header = csv.DictWriter(filecsv, fieldnames=[
                    'nama','namapemilik','jenisbarang','harga','jumlah','total'
                    ],  delimiter=',')
                    header.writeheader()
        menu_pembelian()
    if pilihan == "3" :
        menu_utama()
        
#menu utama
def menu_utama():
    os.system('cls')
    print("========================================")
    print("Selamat Datang di KoperasiNovasi")
    print("========================================")
    print("1. Pencatatan Produk")
    print("2. Transaksi")
    print("3. Absensi")
    print("4. Keluar")
    
    
    print("========================================")
    info_exp = False
    data_exp = []
    with open('dataproduk.csv', 'r') as file:
        dataproduk = csv.reader(file, delimiter=',')
        for row in dataproduk:
            strTgl = str(datetime.now().date())
            if row[5] < strTgl:
                data_exp.append({
                    'nama': row[0],'namapemilik': row[1],'jenisbarang': row[2],'harga': row[3], 
                    'stok': row[4], 'expireddate': row[5]
                    })
                data_exp.remove(data_exp[0])
                dp = pd.DataFrame(data_exp)
                dp.index = range(1, len(dp)+1)
                
                
            else:
                if not info_exp: 
                    data_exp.append({'Informasi produk expired':'Tidak ada produk expired'})
                    info_exp = True
                    dp = pd.DataFrame(data_exp)
                    dp.index = range(1, len(dp)+1)
                    
                    
    print(dp)
    print("========================================")
    print("========================================")
    
    pilihan = input("Pilih Menu [1/2/3/4] :")
    if pilihan == "1" :
        menu_pencatatan()
    if pilihan == "2" :
        menu_transaksi()
    if pilihan == "3" :
        if not(Path('data_absensi.csv').is_file()):
            with open('data_absensi.csv', 'w', newline='') as filecsv:
                header = csv.DictWriter(filecsv, fieldnames=[
                    'namakaryawan','shift','tanggal','waktu','absen'
                    ],  delimiter=',') 
                header.writeheader()
        menu_absensi()
    if pilihan == "4" :
        exit()
        
#menu registrasi dan login
def menu_regislogin():
    print("========================================")
    print(" Selamat Datang di KoperasiNovasi")
    print("1. Register")
    print("2. Login")
    pilihan = input("Register/Login[1/2] : ")
    print("========================================")
    if pilihan == "1":
        if not(Path('data_user.csv').is_file()):
            with open('data_user.csv', 'w', newline='') as filecsv:
                header = csv.DictWriter(filecsv, fieldnames=['Username','Password'],  delimiter=',') 
                header.writeheader()
        if not(Path('dataproduk.csv').is_file()):
            with open('dataproduk.csv', 'w', newline='') as filecsv:
                header = csv.DictWriter(filecsv, fieldnames=[
                    'nama','namapemilik','jenisbarang','harga','stok','expireddate'
                    ],  delimiter=',') 
                header.writeheader()
        register()
    elif pilihan == "2":
        if not(Path('dataproduk.csv').is_file()):
            with open('dataproduk.csv', 'w', newline='') as filecsv:
                header = csv.DictWriter(filecsv, fieldnames=[
                    'nama','namapemilik','jenisbarang','harga','stok','expireddate'
                    ],  delimiter=',') 
                header.writeheader()
        login()
    else:
        print("Pilihan tidak tersedia")
        
if __name__ == "__main__":
    menu_regislogin()