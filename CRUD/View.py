from . import Operasi

def delete_console():
    read_console()
    while(True):
        print("Silahkan Pilih nomor buku yang akan didelete")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

            # data yang ingin diupdate
            print("\n"+"="*100)
            print("Data yang ingin anda Hapus")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")
            is_done = input("Apakah anda yakin (Y/N)?")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_buku)
                break
        else:
            print("Nomor buku tidak valid, silahkan input kembali: ")
    
    print("Data berhasil dihapus")
    
        
def update_console():
    read_console()
    while(True):
        print("Silahkan Pilih nomor buku yang akan diupdate")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("Nomor buku tidak valid, silahkan input kembali: ")
    
    data_break = data_buku.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]
    
    while(True):
        # data yang ingin diupdate
        print("\n"+"="*100)
        print("Silahkan pilih data apa yang ingin anda ubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        #memilih mode untuk update
        user_option = input("Pilih data [1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1": judul = input("Judul\t: ")
            case "2": penulis = input("Penulis\t: ")
            case "3": 
                while(True):
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:       
                            print("Tahun harus angka dan 4 karakter, Silahkan masukkan tahun kembali (yyyy)")    
                    except:
                        print("Tahun harus angka, Silahkan masukkan tahun kembali (yyyy)")
            case _: print("Index yang anda input tidak cocok")
        
        print("Data terbaru Anda")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        is_done = input("Apakah Data sudah sesuai (Y/N)?")
        if is_done == "y" or is_done == "Y":
            break
    Operasi.update(no_buku,pk,data_add,tahun,judul,penulis)        



def create_console():
    print("\n\n"+"="*100)
    print("\nSilahkan tambah data buku\n")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:       
                print("Tahun harus angka dan 4 karakter, Silahkan masukkan tahun kembali (yyyy)")    
        except:
            print("Tahun harus angka, Silahkan masukkan tahun kembali (yyyy)")
    Operasi.create(tahun,judul,penulis)
    print("\nBerikut adalah data baru anda")
    read_console()


def read_console():
    data_file = Operasi.read()

    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("\n"+"="*100+"\n")
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)
    
    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(',')
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")
    #Footer
    print("="*100+"\n")



    