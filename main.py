from turtle import width

from converter import image_to_ascii
import os

IMAGE_FOLDER = "images"
OUTPUT_FOLDER = "output"


def get_images():
    # Mengambil semua file gambar dari folder images.

    supported_formats = (".jpg", ".jpeg", ".png", ".webp")

    images = []

    for file in os.listdir(IMAGE_FOLDER):
        if file.lower().endswith(supported_formats):
            images.append(file)

    return images


def choose_image(images):
    # Menampilkan daftar gambar dan meminta user memilih.

    print("Available images:")
    print()

    for i, image in enumerate(images, start=1):
        print(f"{i}. {image}")

    print()

    while True:
        try:
            choice = int(input("Pilih gambar: "))

            if 1 <= choice <= len(images):
                return images[choice - 1]

            print("Pilihan tidak tersedia!")

        except ValueError:
            print("Masukkan nomor yang valid!")


def choose_width():
    # Memilih ukuran ASCII Art.

    print()
    print("Pilih ukuran ASCII:")
    print()
    print("1. Small")
    print("2. Medium")
    print("3. Large")
    print()

    while True:
        choice = input("Pilihan: ")

        if choice == "1":
            return 40

        elif choice == "2":
            return 60

        elif choice == "3":
            return 80

        else:
            print("Pilihan tidak tersedia.")

def choose_style():
    # Memilih style ASCII Art.

    print()
    print("Pilih style:")
    print()
    print("1. Classic")
    print("2. Minimal")
    print("3. Blocks")
    print()

    while True:
        choice = input("Pilihan: ")

        if choice == "1":
            return "classic"

        elif choice == "2":
            return "minimal"

        elif choice == "3":
            return "blocks"

        else:
            print("Pilihan tidak tersedia!")

def save_ascii(ascii_art, image_name):
    # Menyimpan ASCII Art ke file TXT.

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    base_name = os.path.splitext(image_name)[0]
    output_path = os.path.join(
        OUTPUT_FOLDER,
        f"{base_name}_ascii.txt"
    )

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(ascii_art)

    return output_path          
def main():

    print("~" * 60)
    print(" " * 20 + "PIC2ASCII")
    print(" " * 13 + "Turn your picture into text")
    print("~" * 60)
    print()

    images = get_images()

    if not images:
        print("Tidak ada gambar di folder images.")
        return

    selected_image = choose_image(images)

    width = choose_width()
    
    style = choose_style()
    image_path = os.path.join(IMAGE_FOLDER, selected_image)

    print()
    print("~" * 60)
    print("Processing...")
    print("~" * 60)
    print()
    
    print(f"Image : {selected_image}")
    print(f"Width : {width}")
    print(f"Style : {style.title()}")

    print()
    print("Generating ASCII Art...")
    print()

    ascii_art = image_to_ascii(
        image_path,
        width=width,
        style=style
    )

    print()
    print(ascii_art)

    output_path = save_ascii(ascii_art, selected_image)

    print()
    print("~" * 60)
    print("              ASCII ART BERHASIL DIBUAT!")
    print("~" * 60)

    print()
    print(f"Image  : {selected_image}")
    print(f"Style  : {style.title()}")
    print(f"Width  : {width}")
    print(f"Output : {output_path}")

    print()
    print("Thanks for using PIC2ASCII! <3")
    print("~" * 60)


if __name__ == "__main__":
    main()