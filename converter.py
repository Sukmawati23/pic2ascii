from PIL import Image

ASCII_STYLES = {
    "classic": "@%#*+=-:. ",
    "minimal": "@#*:. ",
    "blocks": "█▓▒░ "
}


def image_to_ascii(image_path, width=80, style="classic"):
    # Membuka gambar
    image = Image.open(image_path)

    # Menentukan tinggi baru agar proporsi gambar tetap terlihat
    aspect_ratio = image.height / image.width
    height = int(width * aspect_ratio * 0.45)

    # Mengubah ukuran gambar
    image = image.resize((width, height))

    # Mengubah gambar menjadi grayscale
    image = image.convert("L")

    # Mengubah pixel menjadi karakter ASCII
    pixels = image.getdata()

    ascii_art = ""

    for pixel in pixels:
        chars = ASCII_STYLES.get(style, ASCII_STYLES["classic"])
        index = pixel * len(chars) // 256
        ascii_art += chars[index]

    lines = [
        ascii_art[i:i + width]
        for i in range(0, len(ascii_art), width)
    ]

    return "\n".join(lines)