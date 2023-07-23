from flask import Flask, render_template, url_for

app = Flask('Psychology Tester')


@app.route('/')
def index_page():
    return render_template("index.html")


@app.route('/introduction')
def introduction():
    return render_template("introduction.html")


def main():
    app.run(
        debug=True
    )


if __name__ == '__main__':
    main()
