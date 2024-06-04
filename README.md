# QR Code Generator and Decoder

This project demonstrates how to create and decode QR codes using Python. It utilizes the `qrcode` library to generate QR codes and the `pyzbar` library to decode them.

## Requirements

- Python 3.x
- `qrcode` library
- `pyzbar` library
- `opencv-python` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/qrcode-generator-decoder.git
    cd qrcode-generator-decoder
    ```

2. Install the required packages:

    ```bash
    pip install qrcode[pil]
    pip install pyzbar
    pip install opencv-python
    ```

## Usage

1. **Generate QR Codes:**

    The script generates two QR codes: one from a URL and another from arbitrary data.

    ```python
    import qrcode
    from pyzbar.pyzbar import decode
    import cv2

    # Create and save the QR code images
    img_link = qrcode.make("https://example.com")
    img_link.save("img1.jpg")

    img_data = qrcode.make("Some data here")
    img_data.save("img2.jpg")
    ```

2. **Decode QR Codes:**

    The script reads and decodes the generated QR code images.

    ```python
    # Read and decode the QR code images
    image1 = cv2.imread("img1.jpg")
    image2 = cv2.imread("img2.jpg")

    decoded_data1 = decode(image1)
    decoded_data2 = decode(image2)

    # Print the decoded data
    print("Decoded data from img1.jpg:", decoded_data1)
    print("Decoded data from img2.jpg:", decoded_data2)
    ```

3. **Run the Script:**

    ```bash
    python qrcode_generator_decoder.py
    ```

    This will generate two QR code images (`img1.jpg` and `img2.jpg`) and print the decoded data from each image.

## Example Output

