from flask import Flask, render_template

app = Flask(__name__)

datos = {
    "imagen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHzGODsHiMdFoatp9jqe6QAE8K2zV8hR7ow2C_PSvexA&s=10",
    "nombre": "Andres Felipe Bravo Navarro",
    "bios": {"github": "https://github.com/Andres-Developer-23", "linkedin": "https://linkedin.com/", "correo": "andres01032001@gmail.com"},
    "profesion": "Full-Stack Web Engineer & Python Developer "
}

@app.route("/")
def perfil():
    return render_template('tarjeta.html', datos=datos)

if __name__ == "__main__":
    app.run(debug=True)