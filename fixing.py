import streamlit as st
import pandas as pd

# Load data
data = pd.read_excel('Lỗi_Phươngánxửlílỗi.xlsx')  # Replace with your file name
data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)  # Remove trailing spaces

st.title("Lỗi & Phương án xử lí lỗi")

# Step 1: Select Product
products = sorted(data['Sản phẩm'].dropna().unique())
product_selected = st.selectbox("📦 Chọn loại sản phẩm", products)

# Filter by product
product_data = data[data['Sản phẩm'] == product_selected]

# Step 2: Select Nơi bị lỗi
parts = sorted(product_data['Nơi bị lỗi'].dropna().unique())
part_selected = st.selectbox("🧩 Chọn nơi bị lỗi)", parts)

# Filter by part
part_data = product_data[product_data['Nơi bị lỗi'] == part_selected]

# Step 3: Select Error Type
errors = sorted(part_data['Lỗi'].dropna().unique())
error_selected = st.selectbox("⚠️ Chọn lỗi)", errors)

# Step 4: Show Fixing Method
fix_data = part_data[part_data['Lỗi'] == error_selected]
fix_methods = fix_data['Phương án xử lí'].dropna().unique()

st.subheader("🛠️ Suggested Fixing Method(s):")
for fix in fix_methods:
    st.success(f"✅ {fix}")
