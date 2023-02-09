# 建立資料庫 demo.db
import sqlite3


# 建立資料庫, 若 demo.db 不在 會自動建立
conn = sqlite3.connect('demo.db')
print('連接資料庫成功')
conn.close()  # 關閉連線,資料庫不會關閉,但可以斷線




