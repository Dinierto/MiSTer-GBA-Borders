# README

This repository contains community-made borders, along with extracted Game Boy Player borders, converted for use with the MiSTer Game Boy Advance core.

## Installation

Files must be in `.bor` format.  By default, the GBA core looks for borders in `/games/GBA`; I recommend creating a subfolder inside that directory, such as `/games/GBA/Borders`, to help keep things organized.  

Once you’ve copied your `.bor` files over, open the core menu and go to **Video & Audio → Borders: On** to enable them.

If you’d like your Downloader script to automatically grab the latest borders from this repository, add this line to the end of your `downloader.ini`:

```
[Dinierto/MiSTer-GBA-Borders]
db_url = https://raw.githubusercontent.com/Dinierto/MiSTer-GBA-Borders/db/db.json.zip
```

## Template

Inside the `Tools` folder, you’ll find a Photoshop template (`MiSTer GBA Border Template.psd`) for creating your own borders. It includes guides for image center (yellow), GBA display area (green), and overscan (red).  

Try to avoid placing important details outside the red lines, as they may be cut off by CRT overscan. When you’re done, export your image as a **bitmap (.bmp)** file.

## Creating borders

There are two scripts in the `Tools` folder for generating border files: `convertBorder.py` and `convertfolder.py`. Both require your input image(s) to be a 320x240 **.bmp** file.

To convert a single `.bmp` file:

```
convertBorder.py <input_file.bmp> <output_file.bor>
```

To convert all `.bmp` files in the folder:

```
convertfolder.py
```

Depending on your operating system, you may be able to run `convertfolder.py` directly from your file explorer without opening a command prompt.

Warning!  You may get the following error:

```
Traceback (most recent call last):
  File "<convertBorder.py path>", line 2, in <module>
    from PIL import Image # pip install Pillow
```

If so then you will need to go to the command line and type in the following command to install Pillow:

```
pip install Pillow
```

## Screen alignment tool

The `Tools` folder also includes a special border called `Alignment test.bor`. This is useful for adjusting the screen alignment in the latest GBA core, which allows tweaking horizontal and vertical positioning. The border features alternating color bars every 5 pixels to help with alignment.

## Contributers

**FPGAzumSpass**- Core developer, border conversion scripts

**Dinierto**- Github repository, border template, alignment test border, border conversions, borders (Metallic, Solid, Brushed Steel, Wood Grain)

**tunnotron3000**- Borders (Misterkun)

**Richard Webster**- Borders (RW Gameboy Advance, Super Gameboy Advance)

**Anime0t4ku**- Borders (Anime0t4ku Border Pack)
