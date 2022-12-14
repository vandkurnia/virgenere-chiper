#Fahrizal Wisnu Panggalih
#V3921010
#TI-D

huruf_alfabet = "abcdefghijklmnopqrstuvwxyz" #Mendeklasikan variabel huruf yang berisi huruf alfabet (a-z) yang berjumlah 26

huruf_ke_index = dict(zip(huruf_alfabet, range(len(huruf_alfabet)))) #Menerjemahkan huruf ke index (Contoh : a = 0, b = 1, dst)
index_ke_huruf = dict(zip(range(len(huruf_alfabet)), huruf_alfabet)) #Menerjemahkan index ke huruf


#Membuat fungsi enkripsi
def enkripsi(plain, key):
    encrypted = ""
    split_plaintext = [plain[i : i + len(key)] for i in range(0, len(plain), len(key))] #Memisahkan plain dengan panjang dari key

    #Mengubah plainteks menjadi indek dan menambah kunci (modulus 26)
    for each_split in split_plaintext:
        i = 0
        for huruf in each_split:
            nomor = (huruf_ke_index[huruf] + huruf_ke_index[key[i]]) % len(huruf_alfabet)
            encrypted += index_ke_huruf[nomor]
            i += 1 
    
    return encrypted #Mengembalikan nilai dari variabel encrypted


def deskripsi(cipher, key):
    decrypted = ""
    split_encrypted = [cipher[i : i + len(key)] for i in range(0, len(cipher), len(key))] #Memisahkan chiper dengan panjang dari key

    #Mengubah chiper menjadi indek dan mengurangi kunci (modulus 26)
    for each_split in split_encrypted:
        i = 0
        for huruf in each_split:
            nomor = (huruf_ke_index[huruf] - huruf_ke_index[key[i]]) % len(huruf_alfabet)
            decrypted += index_ke_huruf[nomor]
            i += 1

    return decrypted #Mengembalikan nilai dari variabel decrypted

#Membuat fungsi untuk menampilkan program
def tampilkan():
    input = "DEVAN" #Memaasukkan kata yang ingin di enkripsi
    key = "JATIM" #key atau kunci pergeseran
    ciphertext = enkripsi(input, key) #Melakukan pemanggilan fungsi enkripsi dengan parameter input dan key yang telah dimasukkan 
    plaintext = deskripsi(ciphertext, key) ##Melakukan pemanggilan fungsi enkripsi dengan parameter ciphertext dan key yang telah dimasukkan 


    #Mencetak ke output
    print("Plaintext : " + input)
    print("Key       : " + key)
    print("========================")
    print("Enkripsi  : " + ciphertext)
    print("Deskripsi : " + plaintext)


tampilkan() #Memanggil fungsi tampilkan atau melihat hasil (output)