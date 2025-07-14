import streamlit as st
from PIL import Image
from io import BytesIO
import os

# Mengatur konfigurasi halaman agar terlihat profesional
st.set_page_config(
    page_title="Informasi & Tutorial",
    page_icon="📖",
    layout="wide"
)

# Fungsi untuk memuat gambar dari path lokal dan menyiapkannya untuk diunduh
# @st.cache_data # Cache data agar tidak membaca file berulang kali
def get_local_image(path):
    """Membuka gambar dari path lokal dan mengembalikannya sebagai object Image dan bytes."""
    try:
        # Buka gambar menggunakan Pillow
        image = Image.open(path)
        
        # Siapkan bytes untuk tombol unduh
        buf = BytesIO()
        image.save(buf, format="JPEG") # Simpan ke buffer dalam format JPEG
        byte_im = buf.getvalue()
        
        return image, byte_im
    except FileNotFoundError:
        st.error(f"File gambar tidak ditemukan di path: {path}. Harap pastikan folder 'img' dan gambarnya ada.")
        return None, None

# --- BAGIAN UTAMA HALAMAN ---

st.title("📖 Informasi Penyakit & Tutorial Penggunaan")
st.write("Temukan informasi detail mengenai setiap penyakit, unduh gambar contoh untuk pengujian, dan pelajari cara menggunakan aplikasi ini.")

# --- BAGIAN TUTORIAL ---
st.header("💡 Cara Menggunakan Aplikasi", divider='rainbow')

col1, col2 = st.columns([1,1])

with col1:
    st.info("**Langkah 1: Siapkan Gambar**")
    st.write("""
    - Pindah ke halaman **'Halaman Utama'** dari menu di samping.
    - Anda bisa **mengunggah file gambar** (JPG, JPEG, PNG) dari perangkat Anda.
    - Atau, gunakan fitur **kamera** untuk mengambil foto daun mentimun secara langsung.
    - **Tidak punya gambar?** Tidak masalah! Anda bisa mengunduh gambar contoh yang telah kami sediakan di bawah.
    """)

with col2:
    st.info("**Langkah 2: Lakukan Klasifikasi**")
    st.write("""
    - Setelah gambar Anda muncul di layar, klik tombol **'Klasifikasikan!'**.
    - Tunggu beberapa saat hingga model selesai menganalisis gambar.
    - Hasil klasifikasi beserta tingkat keyakinan model akan ditampilkan.
    - Jika model tidak cukup yakin atau gambar tidak relevan, sebuah pesan akan muncul.
    """)


# --- BAGIAN GALERI PENYAKIT ---
st.header("🖼️ Galeri & Informasi Penyakit", divider='rainbow')

# Path ke gambar contoh di folder lokal
# Pastikan Anda membuat folder 'img' dan meletakkan file-file ini di dalamnya
image_paths = {
    "Fresh Leaf": os.path.join("img", "Contoh_Fresh_Leaf.jpg"),
    "Anthracnose": os.path.join("img", "Contoh_Anthracnose.jpg"),
    "Bacterial Wilt": os.path.join("img", "Contoh_Bacterial_Wilt.jpg"),
    "Downy Mildew": os.path.join("img", "Contoh_Downy_Mildew.jpg"),
    "Gummy Stem Blight": os.path.join("img", "Contoh_Gummy_Stem_Blight.jpg")
}

# --- Daun Sehat (Fresh Leaf) ---
with st.expander("✅ Fresh Leaf (Daun Sehat)"):
    img_col, text_col = st.columns([1, 3])
    with img_col:
        image, img_bytes = get_local_image(image_paths["Fresh Leaf"])
        if image and img_bytes:
            st.image(image, caption="Contoh Daun Sehat")
            st.download_button(
                label="Unduh Gambar Ini",
                data=img_bytes,
                file_name="contoh_fresh_leaf.jpg",
                mime="image/jpeg"
            )
    with text_col:
        st.subheader("Karakteristik Daun Sehat")
        st.write("""
        Daun yang sehat merupakan indikator utama dari tanaman mentimun yang tumbuh dengan baik.
        
        - **Ciri-ciri Utama:**
            - Warna hijau cerah, segar, dan merata di seluruh permukaan daun.
            - Permukaan daun terasa mulus, tanpa ada bercak, lubang, atau perubahan warna yang tidak wajar.
            - Tepi daun terlihat normal, tidak keriting, kering, ataupun menguning.
        """)


# --- Penyakit Anthracnose ---
with st.expander("⚫ Anthracnose (Antraknosa)"):
    img_col, text_col = st.columns([1, 3])
    with img_col:
        image, img_bytes = get_local_image(image_paths["Anthracnose"])
        if image and img_bytes:
            st.image(image, caption="Contoh Penyakit Anthracnose")
            st.download_button(
                label="Unduh Gambar Ini",
                data=img_bytes,
                file_name="contoh_anthracnose.jpg",
                mime="image/jpeg"
            )
    with text_col:
        st.subheader("Deskripsi Penyakit")
        st.write("""
        - **Penyebab:** Disebabkan oleh cendawan _Colletotrichum lagenarium_.
        - **Gejala:** Ditandai dengan munculnya bercak kecil berwarna cokelat pada daun yang kemudian membesar hingga menyebabkan daun mati. Pada batang, gejalanya berupa bercak cokelat tua yang memanjang, sedangkan pada buah tampak bercak bulat dan basah.
        - **Pengendalian:** Dapat dilakukan melalui perendaman benih dalam larutan _Pseudomonas fluorescens_ sebelum tanam dan dengan melakukan pergiliran tanaman.
        
        _Sumber: Direktorat Budidaya Tanaman Sayuran and Biofarmaka, 2008._
        """)

# --- Penyakit Bacterial Wilt ---
with st.expander("🍂 Bacterial Wilt (Layu Bakteri)"):
    img_col, text_col = st.columns([1, 3])
    with img_col:
        image, img_bytes = get_local_image(image_paths["Bacterial Wilt"])
        if image and img_bytes:
            st.image(image, caption="Contoh Penyakit Bacterial Wilt")
            st.download_button(
                label="Unduh Gambar Ini",
                data=img_bytes,
                file_name="contoh_bacterial_wilt.jpg",
                mime="image/jpeg"
            )
    with text_col:
        st.subheader("Deskripsi Penyakit")
        st.write("""
        - **Penyebab:** Disebabkan oleh bakteri _Ralstonia solanacearum_ yang penyebarannya berlangsung melalui air.
        - **Gejala:** Gejala awal yang muncul adalah tanaman layu, dimulai dari bagian pucuk yang kemudian menjalar ke bawah hingga seluruh daun layu dan akhirnya tanaman mati. Penyakit ini cenderung berkembang pesat pada musim hujan.
        - **Inang Lain:** Cabai, tomat, dan kentang.
        
        _Sumber: Tonny, K., et al., 2014._
        """)

# --- Penyakit Downy Mildew ---
with st.expander("🟡 Downy Mildew (Embun Bulu)"):
    img_col, text_col = st.columns([1, 3])
    with img_col:
        image, img_bytes = get_local_image(image_paths["Downy Mildew"])
        if image and img_bytes:
            st.image(image, caption="Contoh Penyakit Downy Mildew")
            st.download_button(
                label="Unduh Gambar Ini",
                data=img_bytes,
                file_name="contoh_downy_mildew.jpg",
                mime="image/jpeg"
            )
    with text_col:
        st.subheader("Deskripsi Penyakit")
        st.write("""
        - **Penyebab:** Disebabkan oleh cendawan _Pseudoperonospora cubensis_.
        - **Gejala:** Ditandai dengan munculnya bercak-bercak kuning pada daun dengan bentuk yang tidak beraturan dan agak tersudut. Seiring perkembangan, bercak tersebut berubah warna menjadi cokelat kemerahan.
        - **Pengendalian:** Dapat dilakukan melalui pergiliran tanaman, penanaman dengan jarak tanam yang tepat, sanitasi kebun, serta pengaturan drainase yang baik.

        _Sumber: Direktorat Budidaya Tanaman Sayuran and Biofarmaka, 2008._
        """)
        
# --- Penyakit Gummy Stem Blight ---
with st.expander("🕸️ Gummy Stem Blight (Busuk Batang Bergetah)"):
    img_col, text_col = st.columns([1, 3])
    with img_col:
        image, img_bytes = get_local_image(image_paths["Gummy Stem Blight"])
        if image and img_bytes:
            st.image(image, caption="Contoh Gummy Stem Blight")
            st.download_button(
                label="Unduh Gambar Ini",
                data=img_bytes,
                file_name="contoh_gummy_stem_blight.jpg",
                mime="image/jpeg"
            )
    with text_col:
        st.subheader("Deskripsi Penyakit")
        st.write("""
        - **Penyebab:** Disebabkan oleh jamur Ascomycota seperti _Didymella bryoniae_.
        - **Gejala:** Gejala awal berupa luka sayatan pada buah, sulur, atau akar lateral yang dapat memanjang hingga ke batang, sehingga menyebabkan tanaman layu lalu mati. Umumnya muncul pada masa pematangan buah.
        - **Pengendalian:** Penyemprotan fungisida seperti azoxystrobin dan kresoxym-methyl, serta pemuliaan tanaman untuk menghasilkan varietas yang tahan.

        _Sumber: Aristya, G., Rahmawati, N. and Daryono, B.S., 2017._
        """)

# --- BAGIAN UNDUH DATASET LEBIH BANYAK ---
st.header("📂 Unduh Dataset Tambahan", divider='rainbow')
st.write("Butuh lebih banyak gambar untuk pengujian? Anda dapat mengunduh koleksi gambar untuk setiap kelas melalui tautan Google Drive di bawah ini.")

gdrive_cols = st.columns(5)
with gdrive_cols[0]:
    st.link_button("Anthracnose", "https://drive.google.com/drive/folders/1pQZ1mmmu_nA1rc_LHvOcWpZOMoVq8jpo?usp=drive_link", help="Ganti dengan link Google Drive Anda")
with gdrive_cols[1]:
    st.link_button("Bacterial Wilt", "https://drive.google.com/drive/folders/1R-huLQ5_P91xiZyZb90RmF-vJqk_dUhm?usp=drive_link", help="Ganti dengan link Google Drive Anda")
with gdrive_cols[2]:
    st.link_button("Downy Mildew", "https://drive.google.com/drive/folders/1F3k_SVNxEjDTmI0sGzoY8lNYIPNqJecI?usp=drive_link", help="Ganti dengan link Google Drive Anda")
with gdrive_cols[3]:
    st.link_button("Gummy Stem", "https://drive.google.com/drive/folders/18qPDBP5vzXgwBIOcsWOmWlit0Tq2Xgxf?usp=drive_link", help="Ganti dengan link Google Drive Anda")
with gdrive_cols[4]:
    st.link_button("Fresh Leaf", "https://drive.google.com/drive/folders/1brpUGbBuF1bFKgvys1rtMlsy2qhL_Y2f?usp=drive_link", help="Ganti dengan link Google Drive Anda")
