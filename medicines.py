import sqlite3


def get_medicine(med_title):
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor()
    
    sql_query = "SELECT ROW_NUMBER() OVER(ORDER BY title, id) AS rn, title, agent, form, usage, balance FROM first_aid WHERE title LIKE '%{0}%' ORDER BY title, id".format(med_title)
    
    cur.execute(sql_query)
    
    medicines = cur.fetchall()
    info_msg = ''
    for medicine in medicines:
        info_msg += f'{medicine[0]}. {medicine[1]}, осталось {medicine[5]}\n'
    if info_msg == '':
        info_msg = 'Такого лекарства нет'
    
    cur.close()
    conn.close()
    
    return info_msg