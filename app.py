from flask import Flask, render_template_string

app = Flask(__name__)

database_kantin = {
    "mba dila": "https://canva.link/u0lmn6bp0lct6sj",
    "mang atap": "https://canva.link/23gd8lad70bkzv8",
    "ceu siti": "https://canva.link/bke5w324a91pzwo",
    "kang udin": "https://canva.link/p14znnkxdtihzdj",
    "pak kumis": "https://canva.link/5x20lyckrkqbmn4",
    "bu susi": "https://canva.link/spxhomzd9l30r1r",
    "mass pi": "https://canva.link/up7tj1m0p3vkqqq",
    "hafy 57": "https://canva.link/s5iiw9gk03ncp6r",
    "mamilo": "https://canva.link/1iinggq4vfj8um6",
    "pak iwan": "https://canva.link/2rgzh693d4pyfij"
}

@app.route("/")
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Menu Kantin Sapta Eka</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                padding: 20px;
                background-color: #f5f5f5;
            }

            h1 {
                color: #6a0dad;
            }

            .kantin {
                background: white;
                margin: 10px 0;
                padding: 15px;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }

            a {
                text-decoration: none;
                color: white;
                background: #6a0dad;
                padding: 8px 12px;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>

        <h1>🍽️ Menu Kantin Sapta Eka</h1>

        {% for nama, link in kantin.items() %}
        <div class="kantin">
            <h3>{{ nama }}</h3>
            <a href="{{ link }}" target="_blank">Lihat Menu</a>
        </div>
        {% endfor %}

    </body>
    </html>
    """

    return render_template_string(html, kantin=database_kantin)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)