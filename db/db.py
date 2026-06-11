from setting import settings
import pymysql

def start_db():
    db = pymysql.connect(
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        database=settings.DB_DATABASE,
        charset='utf8'
    )

    cursor = db.cursor()
    
    return db, cursor

def init_db():
    con, cur = start_db()
    cur.execute("CREATE TABLE IF NOT EXISTS lost (id INT AUTO_INCREMENT PRIMARY KEY, context VARCHAR(150), image_link VARCHAR(150), created_at BIGINT)")
    con.commit()
    con.close()
    
def insert_lost_item(context: str, image_link: str, created_at: int):
    con, cur = start_db()
    sql = "INSERT INTO lost (context, image_link, created_at) VALUES (%s, %s, %s)"
    val = (context, image_link, created_at)
    cur.execute(sql, val)
    con.commit()
    con.close()
    
def delete_lost_item(item_id: int):
    con, cur = start_db()
    sql = "DELETE FROM lost WHERE id = %s"
    val = (item_id,)
    cur.execute(sql, val)
    con.commit()
    con.close()
    
def get_lost_items(query: str="", page: int=1, page_size: int=10):
    con, cur = start_db()
    sql = "SELECT * FROM lost WHERE context LIKE %s ORDER BY created_at DESC LIMIT %s OFFSET %s"
    val = (f"%{query}%", page_size, (page - 1) * page_size)
    cur.execute(sql, val)
    results = cur.fetchall()
    con.close()
    return results

def is_exist_lost_item(item_id: int):
    con, cur = start_db()
    sql = "SELECT * FROM lost WHERE id = %s"
    val = (item_id,)
    cur.execute(sql, val)
    result = cur.fetchone()
    con.close()
    return result is not None