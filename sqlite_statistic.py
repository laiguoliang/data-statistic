# 匯入套件
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3  # 若改用 MySQL 可換成 import pymysql 或 pyodbc

# 設定字型
plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.rcParams['axes.unicode_minus'] = False

# 建立 SQLite 連線（也可改連 MSSQL/MySQL）
conn = sqlite3.connect("sales_data.db")

# 撰寫 SQL 查詢語句：統計各月份總銷售金額
sql = """
SELECT strftime('%Y-%m', 日期) AS 月份, SUM(金額) AS 銷售總額
FROM 銷售資料
GROUP BY 月份
ORDER BY 月份;
"""

# 執行查詢並轉為 DataFrame
df = pd.read_sql_query(sql, conn)

# 顯示查詢結果
print("月份銷售統計：")
print(df)

# 畫出折線圖
plt.figure(figsize=(8, 5))
plt.plot(df["月份"], df["銷售總額"], marker='o', color='blue')
plt.title("每月銷售趨勢")
plt.xlabel("月份")
plt.ylabel("銷售總額")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.show()

# 匯出結果為 Excel
df.to_excel("monthly_sales_summary.xlsx", index=False)

print("\n分析完成：已匯出 Excel 與圖表圖片。")
