import qrcode

# URL to encode
url = "https://shakiraaaaaa.github.io/Health/"

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # size of each box in the QR code grid
    border=4,  # thickness of the border
)

qr.add_data(url)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("healthCare.png")

print("QR code generated and saved as 'health_qr_code.png'")
