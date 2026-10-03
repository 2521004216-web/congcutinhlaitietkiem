import streamlit as st

# =========================
# CẤU HÌNH TRANG
# =========================

st.set_page_config(
    page_title="Tính lãi gửi tiết kiệm",
    page_icon="💰",
    layout="centered"
)

# Logo
st.image("logo.jpg", width=150)

st.title("💰 TÍNH LÃI GỬI TIẾT KIỆM_Lê Nguyễn Hồng Quyên")
st.write("Nhập thông tin khoản tiền gửi để tính tiền lãi.")

# =========================
# BẢNG LÃI SUẤT CỐ ĐỊNH
# =========================

lai_suat_theo_ky_han = {
    1: 2.0,
    3: 2.5,
    6: 4.0,
    9: 4.5,
    12: 5.0,
    18: 5.5,
    24: 5.8
}

# =========================
# NHẬP SỐ TIỀN GỬI
# =========================

so_tien_gui = st.number_input(
    "💵 Số tiền gửi (VNĐ)",
    min_value=0,
    value=10000000,
    step=1000000
)

# =========================
# CHỌN KỲ HẠN
# =========================

ky_han = st.selectbox(
    "📅 Chọn kỳ hạn",
    list(lai_suat_theo_ky_han.keys()),
    format_func=lambda x: f"{x} tháng"
)

# Tự động lấy lãi suất
lai_suat = lai_suat_theo_ky_han[ky_han]

# Hiển thị lãi suất tương ứng
st.info(
    f"📈 Lãi suất áp dụng cho kỳ hạn {ky_han} tháng: "
    f"**{lai_suat:.2f}%/năm**"
)

# =========================
# HÌNH THỨC NHẬN LÃI
# =========================

hinh_thuc = st.selectbox(
    "💳 Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

# =========================
# NÚT TÍNH LÃI
# =========================

if st.button("🧮 TÍNH LÃI", use_container_width=True):

    # Tổng tiền lãi
    tong_tien_lai = (
        so_tien_gui
        * (lai_suat / 100)
        * (ky_han / 12)
    )

    # Tiền lãi định kỳ
    if hinh_thuc == "Cuối kỳ":

        tien_lai_dinh_ky = tong_tien_lai
        don_vi = "cuối kỳ"

    elif hinh_thuc == "Hàng tháng":

        tien_lai_dinh_ky = (
            so_tien_gui
            * (lai_suat / 100)
            / 12
        )
        don_vi = "mỗi tháng"

    else:

        tien_lai_dinh_ky = (
            so_tien_gui
            * (lai_suat / 100)
            / 4
        )
        don_vi = "mỗi quý"

    # Tổng tiền gốc + lãi
    tong_tien = so_tien_gui + tong_tien_lai

    # =========================
    # HIỂN THỊ KẾT QUẢ
    # =========================

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

    st.subheader("📋 Thông tin khoản gửi")

    st.write(f"**Số tiền gửi:** {so_tien_gui:,.0f} VNĐ")
    st.write(f"**Kỳ hạn:** {ky_han} tháng")
    st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
    st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")

    st.success(
        f"Bạn nhận **{tien_lai_dinh_ky:,.0f} VNĐ** tiền lãi "
        f"{don_vi}."
    )
