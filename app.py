import streamlit as st
st.image("logo.jpg.jpg", width=200)

import streamlit as st
import pandas as pd
import numpy as np

# 1. Giả lập dữ liệu tiền lãi tăng trưởng bắt đầu từ số 0 (Không bị âm)
# Thay vì lấy số ngẫu nhiên có cả âm cả dương, ta chỉ lấy số dương ngẫu nhiên
so_buoc_thoi_gian = 20 
cac_khoan_lai_cong_them = np.random.uniform(10, 50, size=(so_buoc_thoi_gian, 1))

# Tạo mảng bắt đầu bằng số 0 và cộng dồn tiền lãi tăng trưởng theo thời gian
du_lieu_goc = np.vstack([ [0], cac_khoan_lai_cong_them.cumsum(axis=0) ])

# 2. Đưa dữ liệu vào bảng (DataFrame) để hiển thị
data = pd.DataFrame(
    du_lieu_goc,
    columns=['Tiền lãi tích lũy (VNĐ)']
)

# 3. Câu lệnh hiển thị đồ thị đường sinh động, bắt đầu từ gốc số 0
st.subheader("📈 Biểu đồ tăng trưởng tiền lãi tích lũy")
st.line_chart(data)

# Thêm hiệu ứng nền Gradient cho trang web
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135px, #1e293b 0%, #0f172a 100%);
        color: #f8fafc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Tiêu đề app
st.title("APP TÍNH TIỀN GỬI TIẾT KIỆM_ĐỀ TÀI 2_Huỳnh Thị Cẩm Duyên")

# Nhập dữ liệu
C = st.number_input(
    "Nhập số tiền gửi (triệu đồng)",
    min_value=0.0,
    value=100.0
)

i = st.number_input(
    "Nhập lãi suất tiết kiệm theo năm (%)",
    min_value=0.0,
    value=6.0
)

n = st.number_input(
    "Nhập số tháng gửi",
    min_value=1,
    value=12
)

# Đổi % sang số thập phân
i = i / 100

# Nút tính toán
if st.button("Tính toán"):
    
    # Lãi đơn
    A = C * (1 + i * n / 12)

    # Lãi kép
    B = C * (1 + i / 12) ** n

    st.subheader("Kết quả")

    st.success(
        f"Tổng tiền nhận được theo lãi đơn: {A:,.4f} triệu đồng"
    )

    st.success(
        f"Tổng tiền nhận được theo lãi kép: {B:,.4f} triệu đồng"
    )
