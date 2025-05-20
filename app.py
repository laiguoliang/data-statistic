from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)

# 原本功能：查詢每月銷售總額
def query_sales():
    conn = sqlite3.connect("sales_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT strftime('%Y-%m', 日期) AS 月份, SUM(金額) AS 銷售總額
        FROM 銷售資料
        GROUP BY 月份 ORDER BY 月份;
    """)
    rows = cursor.fetchall()
    conn.close()
    return [{"月份": r[0], "銷售總額": r[1]} for r in rows]

# 🆕 查詢分類金額（給報表用）
def query_sales_by_category():
    conn = sqlite3.connect("sales_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 分類, SUM(金額) AS 金額
        FROM 銷售資料
        GROUP BY 分類
        ORDER BY 金額 DESC;
    """)
    rows = cursor.fetchall()
    conn.close()
    return [{"分類": r[0], "金額": r[1]} for r in rows]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report_page():
    return render_template("sales_report.html")  # 指向 templates/sales_report.html

@app.route("/api/sales")
def sales_api():
    return jsonify(query_sales())

@app.route("/api/sales_summary")
def sales_summary_api():
    return jsonify(query_sales_by_category())

if __name__ == "__main__":
    app.run(debug=True)
