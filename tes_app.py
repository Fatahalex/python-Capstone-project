class YellowPages:
    def __init__(self):
        self.entries = []

    def add_entry(self, name, phone_number):
        self.entries.append({'nama': name, 'nomor_telepon': phone_number})
        print(f"Added entry: {name}, {phone_number}")

    def display_entries(self):
        print("Yellow Pages Entries:")
        for idx, entry in enumerate(self.entries, start=1):
            print(f"{idx}. Name: {entry['nama']}, Phone Number: {entry['nomor_telepon']}")

    def update_entry(self, index, name, phone_number):
        if index >= 1 and index <= len(self.entries):
            self.entries[index - 1] = {'nama': name, 'nomor_telepon': phone_number}
            print(f"Updated entry at index {index}")
        else:
            print("Invalid index")

    def delete_entry(self, index):
        if index >= 1 and index <= len(self.entries):
            del self.entries[index - 1]
            print(f"Deleted entry at index {index}")
        else:
            print("Invalid index")


def main():
    yellow_pages = YellowPages()

    while True:
        print("\nMenu:")
        print("1. Tambahkan Entri")
        print("2. Tampilkan Entri")
        print("3. Perbarui Entri")
        print("4. Hapus Entri")
        print("5. Keluar")

        choice = input("Masukkan pilihan Anda: ")

        if choice == '1':
            name = input("Masuukkan nama: ")
            phone_number = input("Masukkan nomor telepon: ")
            yellow_pages.add_entry(name, phone_number)
        elif choice == '2':
            yellow_pages.display_entries()
        elif choice == '3':
            index = int(input("Masukkan index entri yang ingin diperbarui: "))
            name = input("Masukkan nama baru: ")
            phone_number = input("Masukkan nomor telepon baru: ")
            yellow_pages.update_entry(index, name, phone_number)
        elif choice == '4':
            index = int(input("Masuukkan entri yang ingin dihapus: "))
            yellow_pages.delete_entry(index)
        elif choice == '5':
            print("Keluar program...")
            break
        else:
            print("Pilihan invalid. Silakan masukkan angka 1 sampai 5.")

if __name__ == "__main__":
    main()
