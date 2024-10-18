import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Nhập dữ liệu trọng lượng
trong_luong_do_dac = np.array([19.73, 20.76, 21.48, 27.96, 24.31, 22.08, 19.32, 17.69, 
                                21.57, 25.08, 21.07, 19.04, 24.5, 22.12, 26.29, 24.2, 
                                26.1, 32.36, 18.3])
trong_luong_thuc_te = np.array([20.88, 20.08, 21.03, 26.92, 24.21, 22.67, 20.88, 19.02, 
                                 20.74, 24.22, 20.93, 18.86, 24.77, 23.63, 28.3, 25.4, 
                                 28.8, 33.55, 17.6])

# Tạo mô hình hồi quy tuyến tính
model = LinearRegression()
trong_luong_do_dac = trong_luong_do_dac.reshape(-1, 1)
model.fit(trong_luong_do_dac, trong_luong_thuc_te)

# Dự đoán giá trị thực tế
thuc_te_du_doan = model.predict(trong_luong_do_dac)

# Tính sai số
sai_so = trong_luong_thuc_te - thuc_te_du_doan

# Vẽ biểu đồ sai số
plt.figure(figsize=(10, 6))
plt.scatter(thuc_te_du_doan, sai_so, color='blue', alpha=0.7)
plt.axhline(0, color='red', linestyle='--')
plt.title('Biểu đồ sai số')
plt.xlabel('Trọng lượng thực tế (g)')
plt.ylabel('Sai số (Trọng lượng thực tế - Dự đoán)')
plt.grid()
plt.show()
