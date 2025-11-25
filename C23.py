import matplotlib.pyplot as plt

# Dữ liệu
thang = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6']
doanh_thu = [120, 150, 100, 180, 200, 160]  # Đơn vị: triệu đồng

# Vẽ biểu đồ cột
plt.bar(thang, doanh_thu, color='skyblue')

# Thêm nhãn trục và tiêu đề
plt.xlabel('Tháng')
plt.ylabel('Doanh thu (triệu đồng)')
plt.title('Biểu đồ doanh thu 6 tháng đầu năm')

# Hiển thị giá trị trên đầu cột
for i, v in enumerate(doanh_thu):
    plt.text(i, v + 3, str(v), ha='center')

# Hiển thị lưới ngang
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Hiển thị biểu đồ
plt.show()
