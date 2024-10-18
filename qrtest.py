import qrcode

# Dữ liệu cần mã hóa vào mã QR
data = "2"

# Tạo QR code
qr = qrcode.QRCode(
    version=1,  # phiên bản của mã QR, càng lớn thì càng phức tạp
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # mức độ sửa lỗi
    box_size=10,  # kích thước của mỗi ô trong mã QR
    border=4,  # độ dày của viền ngoài
)

qr.add_data(data)
qr.make(fit=True)

# Tạo ảnh QR code
img = qr.make_image(fill_color="black", back_color="white")

# Lưu ảnh QR code
img.save("qrcode.png")