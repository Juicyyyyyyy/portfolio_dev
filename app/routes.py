from app.models.post import Post

from flask import Blueprint, render_template
import re

main_bp = Blueprint('main', __name__)

from markdown import markdown
import re


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    # Get recent blog posts for the homepage
    recent_posts = Post.query.order_by(Post.date_posted.desc()).limit(6).all()
    
    # Process posts for display
    for post in recent_posts:
        cropped_article = crop_article(post.content)
        cropped_article_markdown_to_html = markdown(cropped_article)
        clean_text = re.sub('<.*?>', '', cropped_article_markdown_to_html)
        clean_text = re.sub('\\s+', ' ', clean_text).strip()
        post.short_description = clean_text

    return render_template('main.html', recent_posts=recent_posts)


def crop_article(full_article, max_words=30):
    words = full_article.split()
    cropped_article = ' '.join(words[:max_words])
    return cropped_article


@main_bp.route("/blog")
def blog():
    posts = Post.query.order_by(Post.date_posted.desc()).all()

    for post in posts:
        cropped_article = crop_article(post.content)
        cropped_article_markdown_to_html = markdown(cropped_article)
        clean_text = re.sub('<.*?>', '', cropped_article_markdown_to_html)
        clean_text = re.sub('\\s+', ' ', clean_text).strip()
        post.short_description = clean_text

    return render_template('blog.html', posts=posts)


@main_bp.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    post.content = markdown(post.content, extensions=['extra', 'codehilite'])
    recent_posts = Post.query.order_by(Post.date_posted.desc()).limit(5).all()
    post.date_posted = post.date_posted.strftime('%Y-%m-%d')
    return render_template('post.html', title=post.title, post=post, recent_posts=recent_posts, content=post.content)

