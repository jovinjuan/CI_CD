from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

inventory = [
    {"id": 1, "nama": "MacBook Pro M2", "stok": 5, "kategori": "Elektronik"},
    {"id": 2, "nama": "Kursi Kerja Ergonomis", "stok": 12, "kategori": "Furniture"},
    {"id": 3, "nama": "Monitor 24 Inch", "stok": 8, "kategori": "Elektronik"},
    {"id": 4, "nama": "Meja Kantor L", "stok": 4, "kategori": "Furniture"},
    {"id": 5, "nama": "Kabel HDMI 2m", "stok": 25, "kategori": "Aksesoris"},
    {"id": 6, "nama": "Mouse Wireless", "stok": 15, "kategori": "Elektronik"},
    {"id": 7, "nama": "Papan Tulis Whiteboard", "stok": 3, "kategori": "Alat Tulis"},
    {"id": 8, "nama": "Webcam 1080p", "stok": 10, "kategori": "Elektronik"},
    {"id": 9, "nama": "Lampu Meja LED", "stok": 20, "kategori": "Aksesoris"},
    {"id": 10, "nama": "Lemari Arsip Baja", "stok": 6, "kategori": "Furniture"}
]

@app.route('/')
def index():
    return render_template('index.html', items=inventory)

@app.route('/add', methods=['POST'])
def add_item():
    nama = request.form.get('nama')
    stok = int(request.form.get('stok'))
    kategori = request.form.get('kategori')
    new_id = len(inventory) + 1 
    inventory.append({"id": new_id, "nama": nama, "stok": stok, "kategori": kategori})
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    for item in inventory:
        if item['id'] == item_id :
            inventory.remove(item)
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
