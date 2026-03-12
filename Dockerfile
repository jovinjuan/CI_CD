# 1. Gunakan image dasar Python
FROM python:3.12-slim

# 2. Set folder kerja di dalam container
WORKDIR /app

# 3. Instal pipenv
RUN pip install pipenv

# 4. Salin file dependensi (Pipfile) ke container
COPY Pipfile Pipfile.lock ./

# 5. Instal dependensi langsung ke sistem container (tanpa virtualenv baru)
RUN pipenv install --system --deploy

# 6. Salin semua kode aplikasi kita (app.py, templates, dll)
COPY . .

# 7. Beritahu Docker port mana yang digunakan
EXPOSE 5000

# 8. Jalankan aplikasi menggunakan Flask
CMD ["python", "app.py"]