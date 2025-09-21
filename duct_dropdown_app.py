# ==============================
# 📌 Duct Measurement Calculator with Dropdown
# Language: Python
# Framework: Streamlit
# ==============================

import streamlit as st

st.title("📏 Duct Measurement Calculator (Inch & mm Support)")

# ✅ Unit Selection
unit = st.radio("Select Unit", ["Inch", "Millimeter"])

# Dropdown selection
option = st.selectbox(
    "Select Component",
    ["Straight Duct", "Elbow", "Reducer", "Shoe,Neck", "Offset", "Duct with End Cap", "End Cap"]
)

# ✅ Helper function: mm → inch
def to_inch(value):
    return value if unit == "Inch" else value / 25.4


# -----------------------------
# 🔹 Straight Duct
# -----------------------------
if option == "Straight Duct":
    width = st.number_input(f"Enter Width ({unit})", min_value=0.0, format="%.2f", key="duct_width")
    height = st.number_input(f"Enter Height ({unit})", min_value=0.0, format="%.2f", key="duct_height")
    length = st.number_input(f"Enter Length ({unit})", min_value=0.0, format="%.2f", key="duct_length")
    qty = st.number_input("Quantity", min_value=1, step=1, value=1, key="duct_qty")

    if st.button("Calculate Duct Area"):
        if width <= 0 or height <= 0 or length <= 0:
            st.error("Please enter positive numbers for width, height and length.")
        else:
            w_in, h_in, l_in = to_inch(width), to_inch(height), to_inch(length)
            single_area = (2 * (w_in + h_in) * l_in) / 144.0
            total_area = single_area * qty

            st.success(f"✅ Single Duct Area: {single_area:.2f} sq.ft")
            st.success(f"📦 Total Area ({int(qty)} pcs): {total_area:.2f} sq.ft")

# -----------------------------
# 🔹 Elbow
# -----------------------------
elif option == "Elbow":
    width = st.number_input(f"Enter Width ({unit})", min_value=0.0, format="%.2f", key="elbow_width")
    height = st.number_input(f"Enter Height ({unit})", min_value=0.0, format="%.2f", key="elbow_height")
    length = st.number_input(f"Enter Length ({unit})", min_value=0.0, format="%.2f", key="elbow_length")
    qty = st.number_input("Quantity", min_value=1, step=1, value=1, key="elbow_qty")

    if st.button("Calculate Elbow Area"):
        if width <= 0 or height <= 0 or length <= 0:
            st.error("Please enter positive numbers for width, height and length.")
        else:
            w_in, h_in, l_in = to_inch(width), to_inch(height), to_inch(length)
            single_area = (2 * (w_in + h_in) * l_in) / 144.0
            total_area = single_area * qty

            st.success(f"✅ Single Elbow Area: {single_area:.2f} sq.ft")
            st.success(f"📦 Total Area ({int(qty)} pcs): {total_area:.2f} sq.ft")

# -----------------------------
# 🔹 Reducer
# -----------------------------
elif option == "Reducer":
    big_width = st.number_input(f"Enter Big Side Width ({unit})", min_value=0.0, step=0.1, key="reducer_big_width")
    big_height = st.number_input(f"Enter Big Side Height ({unit})", min_value=0.0, step=0.1, key="reducer_big_height")
    small_width = st.number_input(f"Enter Small Side Width ({unit})", min_value=0.0, step=0.1, key="reducer_small_width")
    small_height = st.number_input(f"Enter Small Side Height ({unit})", min_value=0.0, step=0.1, key="reducer_small_height")
    length = st.number_input(f"Enter Length ({unit})", min_value=0.0, step=0.1, key="reducer_length")
    qty = st.number_input("Quantity", min_value=1, step=1, key="reducer_qty")

    if st.button("Calculate Reducer Area"):
        per_big = 2 * (to_inch(big_width) + to_inch(big_height))
        per_small = 2 * (to_inch(small_width) + to_inch(small_height))
        single_area = ((per_big + per_small) / 2) * to_inch(length) / 144
        total_area = single_area * qty

        st.success(f"✅ Single Reducer Area: {single_area:.2f} sq.ft")
        st.success(f"📦 Total Area ({qty} pcs): {total_area:.2f} sq.ft")

# -----------------------------
# 🔹 Shoe, Neck
# -----------------------------
elif option == "Shoe,Neck":
    big_width = st.number_input(f"Enter Big Side Width ({unit})", min_value=0.0, step=0.1, key="shoe_big_width")
    big_height = st.number_input(f"Enter Big Side Height ({unit})", min_value=0.0, step=0.1, key="shoe_big_height")
    small_width = st.number_input(f"Enter Small Side Width ({unit})", min_value=0.0, step=0.1, key="shoe_small_width")
    small_height = st.number_input(f"Enter Small Side Height ({unit})", min_value=0.0, step=0.1, key="shoe_small_height")
    length = st.number_input(f"Enter Length ({unit})", min_value=0.0, step=0.1, key="shoe_length")
    qty = st.number_input("Quantity", min_value=1, step=1, key="shoe_qty")

    if st.button("Calculate Shoe,Neck Area"):
        per_big = 2 * (to_inch(big_width) + to_inch(big_height))
        per_small = 2 * (to_inch(small_width) + to_inch(small_height))
        single_area = ((per_big + per_small) / 2) * to_inch(length) / 144
        total_area = single_area * qty

        st.success(f"✅ Single Shoe,Neck Area: {single_area:.2f} sq.ft")
        st.success(f"📦 Total Area ({qty} pcs): {total_area:.2f} sq.ft")

# -----------------------------
# 🔹 Offset
# -----------------------------
elif option == "Offset":
    width = st.number_input(f"Enter Width ({unit})", min_value=0.0, step=0.1, key="offset_width")
    height = st.number_input(f"Enter Height ({unit})", min_value=0.0, step=0.1, key="offset_height")
    offset = st.number_input(f"Enter Offset Length ({unit})", min_value=0.0, step=0.1, key="offset_length")
    qty = st.number_input("Quantity", min_value=1, step=1, key="offset_qty")

    if st.button("Calculate Offset Area"):
        single_area = (2 * (to_inch(width) + to_inch(height)) * to_inch(offset)) / 144
        total_area = single_area * qty

        st.success(f"✅ Single Offset Area: {single_area:.2f} sq.ft")
        st.success(f"📦 Total Area ({qty} pcs): {total_area:.2f} sq.ft")

# -----------------------------
# 🔹 Duct with End Cap
# -----------------------------
elif option == "Duct with End Cap":
    width = st.number_input(f"Enter Width ({unit})", min_value=0.0, step=0.1, key="endcapduct_width")
    height = st.number_input(f"Enter Height ({unit})", min_value=0.0, step=0.1, key="endcapduct_height")
    length = st.number_input(f"Enter Length ({unit})", min_value=0.0, step=0.1, key="endcapduct_length")
    qty = st.number_input("Quantity", min_value=1, step=1, key="endcapduct_qty")

    if st.button("Calculate Duct with End Cap Area"):
        total_area = ((2 * (to_inch(width) + to_inch(height)) * to_inch(length)) + (to_inch(width) * to_inch(height))) * qty / 144
        single_area = total_area / qty

        st.success(f"✅ Single Duct with End Cap Area: {single_area:.2f} sq.ft")
        st.success(f"📦 Total Area ({qty} pcs): {total_area:.2f} sq.ft")

# -----------------------------
# 🔹 End Cap
# -----------------------------
elif option == "End Cap":
    width = st.number_input(f"Enter Width ({unit})", min_value=0.0, step=0.1, key="endcap_width")
    height = st.number_input(f"Enter Height ({unit})", min_value=0.0, step=0.1, key="endcap_height")
    qty = st.number_input("Quantity", min_value=1, step=1, key="endcap_qty")

    if st.button("Calculate End Cap Area"):
        single_area = (to_inch(width) * to_inch(height)) / 144
        total_area = single_area * qty

        st.success(f"✅ Single End Cap Area: {single_area:.2f} sq.ft")
        st.success(f"📦 Total Area ({qty} pcs): {total_area:.2f} sq.ft")




