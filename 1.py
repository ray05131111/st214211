import streamlit as st
import pandas as pd
import plotly.graph_objects as go  # 確保這裡使用 go
import matplotlib.pyplot as plt  # plt 保留給 matplotlib

# 顯示標題和圖片
st.title('西洋棋')
st.write('## 西洋棋棋盤')
st.image(r"C:\Users\User\Desktop\st\phphK5JVu.png")

# 假設你已經將數據讀取到一個 pandas DataFrame 中
df = pd.read_csv(r"C:\Users\User\Desktop\st\openings.csv")

# 統計白方和黑方第一步的數量
white_moves = df['move1w'].value_counts()
black_moves = df['move1b'].value_counts()

# 將結果合併
all_moves = pd.concat([white_moves, black_moves], axis=1)
all_moves.columns = ['White Moves', 'Black Moves']

# 將所有移動統一放入一個數據框中
all_moves = all_moves.fillna(0)  # 將 NaN 替換為 0
all_moves = all_moves.astype(int)  # 確保為整數類型
all_moves_total = all_moves.sum(axis=1)  # 合併白方和黑方的數據

# 計算比例
percentages = all_moves_total / all_moves_total.sum() * 100

# 將小於3%的步數合併為“其他”
labels = []
sizes = []
for label, percentage in zip(percentages.index, percentages):
    if percentage < 3:
        if '其他' not in labels:
            labels.append('其他')
            sizes.append(percentage)
        else:
            sizes[-1] += percentage  # 將其加到“其他”
    else:
        labels.append(label)
        sizes.append(percentage)

# 在 Streamlit 中顯示標題
st.title('Distribution of First Moves in Chess Openings')

# 繪製圓餅圖
plt.figure(figsize=(12, 10))  # 增加圖表大小
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # 確保圓餅圖是圓形

# 顯示圖表到 Streamlit
st.pyplot(plt)  # 使用 st.pyplot() 顯示 Matplotlib 圓餅圖 