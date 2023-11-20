import sqlite3


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('lab.db')

    def load_data(self):
        request = "SELECT question, answer FROM Question"
        info = self.conn.execute(request).fetchall()
        data = []
        for i in range(len(info)):
            data.append({'id': i, 'question': info[i][0], 'correct_answer': info[i][1], 'answer': '', 'is_showed': 0})
        print(data)
        return data
