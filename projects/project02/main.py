import qrcode

# متن یا URL
data = "https://example.com"

# ساخت QR code
img = qrcode.make(data)

# ذخیره تصویر داخل پوشه screenshots
img.save("screenshots/project02.png")

print("QR code saved to screenshots/project02.png")
