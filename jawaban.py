def tipe_data_python():
    # Tipe data numerik
    tipe_int = 12345  # int: bilangan bulat, contoh: 1, 0, -100
    tipe_float = 3.14  # float: bilangan desimal, contoh: 3.14, -0.5
    tipe_complex = 2 + 3j  # complex: bilangan kompleks dengan bagian real dan imajiner, contoh: 2+3j

    # Tipe data teks
    tipe_str = "Ini contoh tipe data String!"  # str: untuk menyimpan teks, contoh: "Hello World"

    # Tipe data boolean
    tipe_bool = True  # bool: hanya memiliki dua nilai, True atau False

    # Tipe data urutan
    tipe_list = [1, 2, 3, 4, 5]  # list: koleksi yang dapat diubah (mutable), elemen boleh duplikat
    tipe_tuple = (10, 20, 30)  # tuple: koleksi yang tidak dapat diubah (immutable)
    tipe_range = range(1, 6)  # range: menghasilkan urutan angka, biasanya digunakan dalam perulangan

    # Tipe data set
    tipe_set = {1, 2, 3, 4, 5}  # set: kumpulan elemen unik yang tidak terurut
    tipe_frozenset = frozenset([10, 20, 30])  # frozenset: versi tidak dapat diubah dari set

    # Tipe data mapping
    tipe_dict = {"nama": "Hanief", "umur": 37}  # dict: menyimpan pasangan kunci-nilai, contoh: {"key": "value"}

    # Menampilkan nilai dari tiap tipe data
    print("Contoh Tipe Data di Python:")
    print(f"1. int        : {tipe_int}")
    print(f"2. float      : {tipe_float}")
    print(f"3. complex    : {tipe_complex}")
    print(f"4. str        : '{tipe_str}'")
    print(f"5. bool       : {tipe_bool}")
    print(f"6. list       : {tipe_list}")
    print(f"7. tuple      : {tipe_tuple}")
    print(f"8. range      : {list(tipe_range)}")
    print(f"9. set        : {tipe_set}")
    print(f"10. frozenset : {tipe_frozenset}")
    print(f"11. dict      : {tipe_dict}")

tipe_data_python()
