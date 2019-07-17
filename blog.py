from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Yucehan Kucukmotor',
        'title': 'First Post',
        'content': 'What does the first post say?',
    },
    {
        'author': 'Emircan Kucukmotor',
        'title': 'Second Post',
        'content': 'What does the second post say?',
    }
]

@app.route('/')         # both routes are feeding the same view functions
@app.route('/home')
def home_page():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about_page():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
