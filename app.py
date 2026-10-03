import streamlit as st

st.set_page_config(
    page_title="Tính lãi gửi tiết kiệm",
    page_icon="💰",
    layout="centered"
)

st.title("💰 TÍNH LÃI GỬI TIẾT KIỆM_Lê Nguyễn Hồng Quyên")
st.write("Nhập thông tin khoản tiền gửi để tính tiền lãi.")

# Nhập số tiền gửi
so_tien_gui = st.number_input(
    "💵 Số tiền gửi (VNĐ)",
    min_value=0,
    value=10000000,
    step=1000000
)

# Nhập kỳ hạn
ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    max_value=120,
    value=12,
    step=1
)

# Nhập lãi suất
lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    max_value=100.0,
    value=5.0,
    step=0.1
)

# Chọn hình thức nhận lãi
hinh_thuc = st.selectbox(
    "💳 Hình thức nhận lãi",
    ["Cuối kỳ", "Hàng tháng", "Hàng quý"]
)

# Nút tính
if st.button("🧮 TÍNH LÃI", use_container_width=True):

    # Tính tổng tiền lãi
    tong_tien_lai = (
        so_tien_gui
        * (lai_suat / 100)
        * (ky_han / 12)
    )

    # Tính tiền lãi định kỳ
    if hinh_thuc == "Cuối kỳ":
        tien_lai_dinh_ky = tong_tien_lai

    elif hinh_thuc == "Hàng tháng":
        tien_lai_dinh_ky = (
            so_tien_gui
            * (lai_suat / 100)
            / 12
        )

    else:
        tien_lai_dinh_ky = (
            so_tien_gui
            * (lai_suat / 100)
            / 4
        )

    # Tổng gốc + lãi
    tong_tien = so_tien_gui + tong_tien_lai

    st.divider()
    st.subheader("📊 KẾT QUẢ")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "💰 Tiền lãi định kỳ",
            f"{tien_lai_dinh_ky:,.0f} VNĐ"
        )

    with col2:
        st.metric(
            "📈 Tổng tiền lãi",
            f"{tong_tien_lai:,.0f} VNĐ"
        )

    st.metric(
        "💵 Tổng tiền gốc + tiền lãi",
        f"{tong_tien:,.0f} VNĐ"
    )

    st.divider()

    st.write(f"**Số tiền gửi:** {so_tien_gui:,.0f} VNĐ")
    st.write(f"**Kỳ hạn:** {ky_han} tháng")
    st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
    st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")
