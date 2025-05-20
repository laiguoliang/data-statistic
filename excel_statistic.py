# 匯入所需的套件
import pandas as pd
import matplotlib.pyplot as plt

# 設定字型
plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.rcParams['axes.unicode_minus'] = False

# 讀取 Excel 銷售資料
df = pd.read_excel("sales_data.xlsx")

# 顯示前幾列確認資料格式
print("原始資料預覽：")
print(df.head())

# 按照「分類」統計銷售金額總和
category_summary = df.groupby("分類")["金額"].sum().sort_values(ascending=False)

# 顯示統計結果
print("\n分類銷售總額：")
print(category_summary)

# 畫出長條圖
plt.figure(figsize=(8, 5))
category_summary.plot(kind="bar", color="#4CAF50")
plt.title("各分類銷售總額（長條圖）")
plt.ylabel("金額")
plt.xlabel("分類")
plt.tight_layout()
plt.savefig("bar_chart.png")  # 儲存圖片
plt.show()

# 畫出圓餅圖
plt.figure(figsize=(6, 6))
category_summary.plot(kind="pie", autopct="%.1f%%", colors=plt.cm.Paired.colors)
plt.title("各分類銷售比例（圓餅圖）")
plt.ylabel("")
plt.tight_layout()
plt.savefig("pie_chart.png")
plt.show()

# 將統計結果存成 Excel
category_summary.to_excel("sales_summary.xlsx")

print("\n分析完成，已輸出報表與圖表圖片。")
