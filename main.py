# 1. Database: Petakan nama kantin ke URL link gambar menu masing-masing
# Ganti 'https://link-gambar-menu-...' dengan URL asli menu kantin Anda
database_kantin = {
    "https://canva.link/8prd4mx2yaq5mfb": "https://canva.link/u0lmn6bp0lct6sj.jpg",
    "https://canva.link/a9iv0jidq4lv2gb": "https://canva.link/a9iv0jidq4lv2gb.jpg",
    "https://canva.link/xamk8t3p4qn6267": "https://canva.link/xamk8t3p4qn6267.jpg",
    "https://canva.link/5ep8ae0yl57tzbf": "https://canva.link/p14znnkxdtihzdj.jpg",
    "https://canva.link/vs0q6x0rgq8n8hs": "https://canva.link/5x20lyckrkqbmn4.jpg",
    "https://canva.link/wg0q578y03vp2fp": "https://canva.link/spxhomzd9l30r1r.jpg",
    "https://canva.link/gijsspl4vw8hhwl": "https://canva.link/up7tj1m0p3vkqqq.jpg",
    "https://canva.link/46gwk5qkiheedqv": "https://canva.link/s5iiw9gk03ncp6r.jpg",
    "https://canva.link/dr7iulsaq95b4jk": "https://canva.link/1iinggq4vfj8um6.jpg",
    "https://canva.link/tit31oju9gtpxlq": "https://canva.link/2rgzh693d4pyfij.jpg",
 }



# 4. Fungsi yang berjalan otomatis saat pilihan dropdown berubah
def ketika_kantin_dipilih(change):
    nama_kantin = change['new']
    link_menu = database_kantin[nama_kantin]

    with output_area:
        output_area.clear_output()
        # Menampilkan teks berupa link yang bisa diklik + preview gambar otomatis
        (HTML(f"""
            <div style="margin-top: 15px; padding: 10px; border-left: 4px solid #8a2be2; background-color: #f9f9f9;">
                <p>Anda memilih: <strong>{nama_kantin}</strong></p>
                <p>🔗 <a href="{link_menu}" target="_blank" style="color: #8a2be2; font-weight: bold;">Klik di sini untuk melihat Menu</a></p>
                <br>
                <p style="font-size: 12px; color: gray;">Preview Menu:</p>
                <img src="{link_menu}" alt="Gambar Menu {nama_kantin}" style="max-width: 400px; border-radius: 8px; border: 1px solid #ddd;">
            </div>
        """))


# 6. Menampilkan antarmuka ke layar
print("--- APLIKASI PEMILIHAN MENU KANTIN ---")

