from flask import Flask


app = Flask(__name__)


@app.route('/hello/')
def hello():
    products = [
        (2, 'bmv', 'czarne', '999.00', None ),
        (3, 'rower', 'bmx', 100.00, None)
    ]

    # budujemy odpowiedź
    response = "<h3>Lista produktów</h3><ul>"
    for product in products:
        response += f"<li>{product[1]}</li>"
    response += "</ul>"

    return response


if __name__ == "__main__":
    app.run(debug=True)
