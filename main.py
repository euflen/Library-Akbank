class Library:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(self.file_name, 'a+')  # file açma
    def __del__(self):
        self.file.close()  # object kaldırılınca file kapat

    def list_books(self):
        self.file.seek(0)  # imleci başa alma sarma
        books = self.file.readlines()
        if not books:
            print("Kütüphane boş.")
        else:
            print("Kütüphanede Mevcut Olan Kitaplar:")
            for book in books:
                title, author, *_ = book.strip().split(', ')
                print(f"- {title} - {author}")

    def add_book(self):
        title = input("Kitabın Adı: ")
        author = input("Kitabın Yazarı: ")
        release_year = input("Yayımlanma Tarihi: ")
        pages = input("Sayfa Sayısı: ")
        book_info = f"{title}, {author}, {release_year}, {pages}\n"
        self.file.write(book_info)
        print(f" '{title}' kütüphanenize eklendi.")

    def remove_book(self):
        title_to_remove = input("Kaldırmak İstedğiniz Kitabın Adı : ")
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []
        removed = False
        for book in books:
            if title_to_remove not in book:
                updated_books.append(book)
            else:
                removed = True
        if not removed:
            print(f" '{title_to_remove}' adındaki kitap bulunamadı.")
        else:
            self.file.seek(0)
            self.file.truncate()  # temizleme
            self.file.writelines(updated_books)
            print(f" '{title_to_remove}' başarıyla kaldırıldı.")

# lib object
lib = Library("books.txt")

# Menu
while True:
    print("\n*** MENU ***")
    print("1) Kitapları Listele")
    print("2) Kitap Ekle")
    print("3) Kitap Kaldır")
    print("q) Çıkış")
    choice = input("Seçimizi giriniz (1-q): ")
    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == 'q':
        del lib  # çıkış
        break
    else:
        print("Geçersiz işlem. Lütfen 1 ile q arasında bir işlem seçin.")