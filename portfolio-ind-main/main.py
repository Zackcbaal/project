#Импорт
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Fungsi untuk membuat tabel dalam database SQLite
def create_table():
    conn = sqlite3.connect('feedback.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS feedback 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 email TEXT, 
                 comment TEXT)''')
    conn.commit()
    conn.close()

# Panggil fungsi create_table() saat aplikasi dijalankan
if __name__ == "__main__":
    create_table()

# Halaman Konten Berjalan
@app.route('/')
def index():
    return render_template('index.html')

#Keterampilan Dinamis
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', 
                           button_python=button_python,
                           button_discord=button_discord,
                           button_html=button_html,
                           button_db=button_db,)
    
# Fungsi untuk menangani formulir umpan balik
@app.route('/feedback', methods=['POST'])
def feedback():
    if request.method == 'POST':
        email = request.form['email']
        comment = request.form['text']
        # Simpan informasi ke dalam database SQLite
        conn = sqlite3.connect('feedback.db')
        c = conn.cursor()
        c.execute("INSERT INTO feedback (email, comment) VALUES (?, ?)", (email, comment))
        conn.commit()
        conn.close()
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

