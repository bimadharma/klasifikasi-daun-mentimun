import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Mengatur konfigurasi halaman
st.set_page_config(
    page_title="Klasifikasi Penyakit Mentimun",
    page_icon="🥒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Fungsi untuk memuat model (dengan cache agar tidak loading berulang kali)
@st.cache_resource
def load_my_model():
    """Memuat model H5 yang telah dilatih."""
    # Pastikan path ke model sudah benar
    model = tf.keras.models.load_model('cucumber_leaf_disease_mobilenetv2_89.h5')
    return model

# Fungsi untuk melakukan pra-pemrosesan gambar
def preprocess_image(image):
    """
    Fungsi ini mengambil gambar PIL dan mengubahnya menjadi format
    yang siap untuk diprediksi oleh model.
    """
    img = image.resize((224, 224))  # Sesuaikan ukuran dengan input model Anda
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Membuat batch dimension
    img_array = img_array / 255.0  # Normalisasi (pastikan sama dengan saat training)
    return img_array

# Memuat model
model = load_my_model()

# Daftar nama kelas (PASTIKAN URUTANNYA SAMA PERSIS DENGAN SAAT TRAINING)
# Urutan ini biasanya sesuai urutan abjad folder di dataset Anda.
class_names = [
    'Anthracnose',
    'Bacterial Wilt',
    'Downy Mildew',
    'Fresh Leaf',
    'Gummy Stem Blight'
]

# === UI STREAMLIT ===
st.title("🌱 Klasifikasi Penyakit Daun Mentimun")
st.write("""
Aplikasi ini menggunakan model Deep Learning (CNN) untuk mengklasifikasikan jenis penyakit pada daun mentimun berdasarkan gambar. Dalam model ini memiliki kelas yang dapat diprediksi yaitu Anthracnose, Bacterial Wilt, Downy Mildew, Fresh Leaf, Gummy Stem Blight.
Silakan unggah gambar atau gunakan kamera untuk mengambil foto daun.
""")

# Membuat dua kolom utama
col1, col2 = st.columns(2)

# Kolom 1: Untuk Input Gambar (Versi Diperbarui)
with col1:
    st.header("🖼️ Input Gambar")
    source_img = None

    # --- PERUBAHAN DI SINI ---
    # Opsi untuk menggunakan kamera sekarang ditampilkan lebih dulu.
    camera_photo = st.camera_input("Ambil foto dengan kamera")

    # Opsi untuk unggah gambar sekarang menjadi alternatif kedua.
    uploaded_file = st.file_uploader(
        "Atau, pilih sebuah gambar dari perangkat Anda...",
        type=["jpg", "jpeg", "png"]
    )

    # Logika diperbarui untuk mengecek input kamera terlebih dahulu,
    # karena ini adalah cara yang lebih disukai untuk menangani dua input Streamlit.
    if camera_photo is not None:
        source_img = Image.open(camera_photo).convert("RGB")
    elif uploaded_file is not None:
        source_img = Image.open(uploaded_file).convert("RGB")
    else:
        st.info("Silakan ambil foto atau unggah gambar untuk memulai analisis.")

# Kolom 2: Untuk Menampilkan Hasil
with col2:
    st.header("📊 Hasil Analisis")

    if source_img:
        # Tampilkan gambar yang diinput
        st.image(source_img, caption="Gambar yang Dianalisis", use_column_width=True)

        # --- FIX: Blok tombol dan prediksi sekarang berada DI DALAM 'if source_img:' ---
        # Ini memastikan tombol hanya muncul jika ada gambar, dan memiliki akses ke variabel 'source_img'.
        if st.button("Klasifikasikan!"):
            with st.spinner('Model sedang menganalisis...'):
                # Pra-pemrosesan gambar
                processed_image = preprocess_image(source_img)

                # Lakukan prediksi
                prediction = model.predict(processed_image)
                
                # Dapatkan nilai kepercayaan (akurasi prediksi) tertinggi
                confidence = np.max(prediction)
                
                # === LOGIKA PEMBATASAN DIMULAI DI SINI ===
                
                # Tentukan ambang batas keyakinan (Anda bisa mengubah angka ini)
                CONFIDENCE_THRESHOLD = 0.70  # Artinya 70%

                if confidence >= CONFIDENCE_THRESHOLD:
                    # Jika model cukup yakin, lanjutkan seperti biasa
                    predicted_class_index = np.argmax(prediction, axis=1)[0]
                    predicted_class_name = class_names[predicted_class_index]

                    st.success(f"Analisis Selesai!")
                    st.metric(
                        label="Hasil Klasifikasi",
                        value=predicted_class_name
                    )
                    st.metric(
                        label="Tingkat Keyakinan",
                        value=f"{confidence:.2%}"
                    )

                    # Beri sedikit penjelasan tentang hasil
                    if predicted_class_name == 'Fresh Leaf':
                        st.balloons()
                        st.info("Daun terlihat sehat! Terus pertahankan perawatan yang baik.")
                    else:
                        st.warning(f"Terdeteksi adanya penyakit **{predicted_class_name}**. Cek halaman 'Tentang' untuk informasi lebih lanjut mengenai penyakit ini.")
                
                else:
                    # Jika model TIDAK cukup yakin, tampilkan pesan error
                    st.error("Model tidak dapat mengenali gambar ini dengan keyakinan yang cukup.")
                    st.warning(f"Harap pastikan gambar yang diunggah adalah daun mentimun yang jelas dan tidak buram.")
                    
    else:
        # --- FIX: 'else' ini sekarang terhubung dengan 'if source_img:' ---
        st.info("Menunggu gambar untuk dianalisis.")
