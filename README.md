# PIC2ASCII

"Turn your pictures into pixels of personality"

PIC2ASCII is a lightweight Python-based ASCII Art Generator that transforms ordinary images into text-based artwork directly from your terminal.

Pick an image, choose your preferred size and style, and let PIC2ASCII turn it into ASCII Art — then save your creation as a .txt file.

## Features

- Convert images into ASCII Art
- Automatically detect images from the images folder
- Choose from 3 ASCII sizes:
  - Small
  - Medium
  - Large

- Choose from 3 ASCII styles:
  - Classic
  - Minimal
  - Blocks

- Preview ASCII Art directly in the terminal
- Automatically save generated ASCII Art as a .txt file
- Simple interactive terminal interface

## Built With

- Python 3
- Pillow

## How It Works

```text
Image
  ↓
Resize
  ↓
Grayscale
  ↓
Pixel Mapping
  ↓
ASCII Art
```

PIC2ASCII analyzes the brightness of each pixel and maps it to different characters to create the final ASCII artwork.

## Run the Project

Install the required dependency:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python main.py
```

Choose an image, select the ASCII size and style, and let PIC2ASCII do the rest.

## Output

Generated ASCII Art is automatically saved in the output folder as a .txt file.

Example:

```text
output/
└── bungaMawar_ascii.txt
```

## Why PIC2ASCII?

A picture doesn't always need complex graphics to be interesting.

PIC2ASCII turns ordinary images into something simple, text-based, and a little different.

"One image. One terminal. A whole lot of characters."
