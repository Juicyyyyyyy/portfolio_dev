from flask import request, render_template
from flask_mail import Mail, Message
from app import app, db
from app import Project, Skill, Category, Experience, Post
from app.tools.prompt_tester import process_prompt
from app.tools.prompt_tester import openai_tool_routes
from app.tools.crypto_correlation_map import crypto_correlation_route
from markdown import markdown

mail = Mail(app)

app.register_blueprint(openai_tool_routes)
app.register_blueprint(crypto_correlation_route)


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

    return render_template('main.html', projects=projects, skills=skills,
                           categories=skills_category, categories_names=categories_names, experiences=experiences)


@app.route("/project/<int:project_id>")
def project(project_id):
    project = Project.query.get(project_id)
    project.description = markdown(project.description)
    return render_template('project.html', project=project)


@app.route("/experience/<int:experience_id>")
def experience(experience_id):
    experience = Experience.query.get(experience_id)
    experience.description = markdown(experience.description)
    return render_template('experience.html', experience=experience)


def crop_article(full_article, max_words=30):
    words = full_article.split()
    cropped_article = ' '.join(words[:max_words])
    return cropped_article

import re
@app.route("/blog")
def blog():
    posts = Post.query.order_by(Post.date_posted.desc()).all()

    for post in posts:
        cropped_article = crop_article(post.content)
        cropped_article_markdown_to_html = markdown(cropped_article)
        clean_text = re.sub('<.*?>', '', cropped_article_markdown_to_html)
        clean_text = re.sub('\s+', ' ', clean_text).strip()
        post.short_description = clean_text


    return render_template('blog.html', posts=posts)


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    post.content = markdown(post.content, extensions=['extra', 'codehilite'])
    recent_posts = Post.query.order_by(Post.date_posted.desc()).limit(5).all()
    return render_template('post.html', title=post.title, post=post, recent_posts=recent_posts, content=post.content)


@app.route('/tools')
def tools():
    return render_template('')


@app.route('/veille')
def veille():
    return render_template('veille.html')
