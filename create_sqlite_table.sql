import sqlite3

# 创建数据库连接
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# 创建表
cursor.execute('''
CREATE TABLE IF NOT EXISTS 銷售資料 (
    日期 TEXT,
    品項 TEXT,
    分類 TEXT,
    金額 INTEGER
)
''')

# 插入数据
sales_data = [
    ('2024-01-01 00:00:00', '鉛筆', '文具', 30),
    ('2024-01-02 00:00:00', '原子筆', '文具', 50),
    ('2024-01-02 00:00:00', '檸檬水', '飲料', 25),
    ('2024-01-03 00:00:00', '咖啡', '飲料', 45),
    ('2024-01-04 00:00:00', '計算機', '電子', 300)
]

cursor.executemany('INSERT INTO 銷售資料 VALUES (?, ?, ?, ?)', sales_data)

# 提交更改并关闭连接
conn.commit()
conn.close()