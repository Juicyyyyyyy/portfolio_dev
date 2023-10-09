from flask import request, render_template
from flask_mail import Mail, Message
from app import app, db
from app import Project, Skill, Category, Experience, Post

mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def index():

    def truncate_words(s, count=20):
        words = s.split()
        if len(words) > count:
            words = words[:count] + ['...']
        return ' '.join(words)

    app.jinja_env.filters['truncatewords'] = truncate_words


    def truncate_chars(s, count=100):
        if len(s) > count:
            return s[:count] + '...'
        return s

    app.jinja_env.filters['truncatechars'] = truncate_chars

    projects = Project.query.all()
    skills = Skill.query.all()
    skills_category = Category.query.order_by(Category.order).all()
    categories_names = [category.name.lower() for category in skills_category]
    experiences = Experience.query.all()
    message_status = None
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(
            subject="Contact Form Submission",
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
            sender=app.config['MAIL_USERNAME'],
            recipients=['corentin.dupaigne@gmail.com'],
        )

        ing = "100%"

        html_template = '''
                                <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>Confirmation Email</title>
                            <style>
                                .bg-gray-100 {
                                    background-color: #F3F4F6;
                                }
                                .container {
                                    margin-left: auto;
                                    margin-right: auto;
                                    padding-left: 1rem;
                                    padding-right: 1rem;
                                    padding-top: 2.5rem;
                                    padding-bottom: 2.5rem;
                                    max-width: 28rem;
                                    background-color: #FFF;
                                    border-width: 1px;
                                    border-style: solid;
                                    border-color: #D1D5DB;
                                    border-radius: 0.375rem;
                                }
                                .text-2xl {
                                    font-size: 1.5rem;
                                    line-height: 2rem;
                                    font-weight: 600;
                                }
                                .font-bold {
                                    font-weight: 700;
                                }
                                .text-gray-700 {
                                    color: #4B5563;
                                }
                                .mb-4 {
                                    margin-bottom: 2rem;
                                }
                                .flex {
                                    display: flex;
                                }
                                .justify-center {
                                    justify-content: center;
                                }
                                .mb-6 {
                                    margin-bottom: 1.5rem;
                                }
                                .w-40 {
                                    width: 10rem;
                                }
                                .h-auto {
                                    height: auto;
                                }
                                .rounded {
                                    border-radius: 0.375rem;
                                }
                                .content {
                                    margin-bottom: 2rem;
                                }
                                .text-base {
                                    font-size: 1rem;
                                    line-height: 1.5rem;
                                }
                                .text-gray-600 {
                                    color: #6B7280;
                                }
                                .signature {
                                    margin-bottom: 0;
                                }
                            </style>
                        </head>
                        <body class="bg-gray-100">
                            <div class="container mx-auto px-4 py-10 bg-white max-w-md rounded-lg border border-gray-300">
                                <h1 class="text-2xl font-bold text-gray-700 mb-4" style="text-align: center;">
                                    Your message has been received
                                </h1>

                                <table width="%s" cellspacing="0" cellpadding="0" border="0">
                                <tr>
                                    <td align="center">
                                        <img src="https://cdn.discordapp.com/attachments/780634443157078026/1098997677213110272/best.png" alt="Corentin Dupaigne" class="w-40 h-auto rounded">
                                    </td>
                                </tr>
                            </table>


                                <div class="content mb-8">
                                    <p class="text-base text-gray-600">
                                        Hi %s,<br><br>
                                        Thank you for reaching out through my portfolio. I've received your message and will get back to you shortly.
                                        <br><br>
                                        Best regards,
                                    </p>
                                </div>
                                <div class="signature">
                                    <p class="text-base font-bold text-gray-700">
                                        Corentin Dupaigne
                                    </p>
                                </div>
                            </div>
                        </body>
                        </html> 




        ''' % (ing, name)

        confirmation_msg = Message(
            subject="Contact Form Submission Received",
            html=html_template,
            sender=app.config['MAIL_USERNAME'],
            recipients=[email],
        )

    try:
        mail.send(msg)
        mail.send(confirmation_msg)
        message_status = 'success'
    except:
        message_status = 'failure'

    return render_template('main.html', message_status=message_status, projects=projects, skills=skills,
                           categories=skills_category, categories_names=categories_names, experiences=experiences)


@app.route("/blog")
def blog():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('blog.html', posts=posts)


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    recent_posts = Post.query.order_by(Post.date_posted.desc()).limit(5).all()
    return render_template('post.html', title=post.title, post=post, recent_posts=recent_posts,
                           header=post.header, introduction=post.introduction, body=post.body, conclusion=post.conclusion)


