from flask import Flask, request, url_for, redirect
from flask import render_template

app = Flask(__name__)
posts = {
    0: {'post_id': 0,
        'title': 'Hello, word',
        'content': 'This is my firs blog post!'
        }
}


@app.route('/')
def home():
    return '<h1>Hello, world</h1>'


@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts.get(post_id)
    if not post:
        return render_template('404.html', message=f'A post with id {post_id} is no\'t found.')
    return render_template('post.html', post=post)


@app.route('/post/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        posts[post_id] = {'id': post_id, 'title': title, 'content': content}
        return redirect(url_for('post', post_id=post_id))
    return render_template('create.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
