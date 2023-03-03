import random
import os
import time


def shell(data_kosong):
    n = len(data_kosong)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = data_kosong[i]
            j = i
            while j >= gap and data_kosong[j-gap] > temp:
                data_kosong[j] = data_kosong[j-gap]
                j -= gap

            data_kosong[j] = temp
        gap //= 2

    return data_kosong


def mergeSort(data_kosong):
    if len(data_kosong) > 1:
        mid = len(data_kosong) // 2
        left_data = data_kosong[:mid]
        right_data = data_kosong[mid:]

        mergeSort(left_data)
        mergeSort(right_data)

        b = i = j = 0

        while b < len(left_data) and i < len(right_data):
            if left_data[b] < right_data[i]:
                data_kosong[j] = left_data[b]
                b += 1
            else:
                data_kosong[j] = right_data[i]
                i += 1
            j += 1
        while b < len(left_data):
            data_kosong[j] = left_data[b]
            b += 1
            j += 1
        while i < len(right_data):
            data_kosong[j] = right_data[i]
            i += 1
            j += 1


data_kosong = []
for i in range(10):
    data_kosong.append(random.randint(1, 100))

print("Angka Random:", data_kosong)
print("")

while True:
    print(''' 
          \tMengurutkan angka random 
          \t---Menu sorting---
          \t1. MergeSort
          \t2. Shellsort
          \t3. Keluar''')
    menu = int(input("Pilih sort apa yang ingin dilakukan(1/2): "))
    if menu == 1:
        print(" mergeSort")
        print(" Angka sebelum di sort:", data_kosong)
        mergeSort(data_kosong)
        print(" Angka sesudah di sort:", data_kosong)
        input("Tekan apapun untuk kembali menu:")
        data_kosong.clear()
        for i in range(10):
            data_kosong.append(random.randint(1, 100))

    elif menu == 2:
        print("shellsort")
        print(f" Angka sebelum di sort: {data_kosong}")
        result = shell(data_kosong)
        print(f" Angka sesudah di sort: {result}")
        input("Tekan apapun untuk kembali menu:")
        data_kosong.clear()
        for i in range(10):
            data_kosong.append(random.randint(1, 100))

    elif menu == 3:
        print("Anda telah keluar")
        break

    else:
        print("Inputan salah, mohon input ulang pilihan anda")
        time.sleep(3)
        os.system('cls')
