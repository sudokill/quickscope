# quickscope

Windows-only Python app that will start a system tray application that checks your clipboard for any readable text in an image. It will then perform OCR and open the Google search results into a new tab in your web broswer.

Used for capturing non-selectable text in various media: streams, videos, PDFs, etc. Has the potential to be faster than selecting normal text with tradtional copy + paste operations.

## Usage

Windows installation of tesseract-OCR is required. Get it here:

[https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
## Features

- system tray menu
- ignores non-images and images without text
- start/pause detection
- fast
- consumes ~30MB of RAM

![Logo](https://github.com/sudokill/quickscope/blob/main/qs.png?raw=true)
