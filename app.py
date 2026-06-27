import streamlit as st
st.image("logo.jpg.jpg", width=200)

import pandas as pd
import numpy as np

# Giả lập dữ liệu tiền lãi tăng trưởng để vẽ đồ thị
# (Bạn có thể thay thế đống số này bằng công thức tính lãi thực tế của bạn)
data = pd.DataFrame(
    np.random.randn(20, 1).cumsum(axis=0) + 50,
    columns=['Tiền lãi tích lũy']
)

# Câu lệnh hiển thị đồ thị đường cực kỳ chuyên nghiệp
st.subheader("📈 Biểu đồ tăng trưởng tiền lãi theo thời gian")
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
