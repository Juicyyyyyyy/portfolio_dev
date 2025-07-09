import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
admin = Admin(template_mode='bootstrap3')

# Import all models so they are registered with SQLAlchemy
from app.models.experience import Experience
from app.models.post import Post
from app.models.project import Project
from app.models.skill import Skill
from app.models.skill_category import Category

def populate_database():
    """Populate the database with fake data"""
    try:
        # Check if data already exists
        if Project.query.first() is not None:
            print("Database already populated, skipping...")
            return

        # Create skill categories
        categories = [
            Category(name="Programming Languages", order=1),
            Category(name="Frameworks", order=2),
            Category(name="Databases", order=3),
            Category(name="Tools", order=4)
        ]
        
        for category in categories:
            db.session.add(category)
        db.session.commit()
        print("Created skill categories")

        # Create skills
        skills = [
            Skill(name="Python", icon="🐍", category_id=1),
            Skill(name="JavaScript", icon="📜", category_id=1),
            Skill(name="PHP", icon="🐘", category_id=1),
            Skill(name="Flask", icon="🔥", category_id=2),
            Skill(name="Django", icon="🎸", category_id=2),
            Skill(name="Laravel", icon="🚀", category_id=2),
            Skill(name="MySQL", icon="🐬", category_id=3),
            Skill(name="PostgreSQL", icon="🐘", category_id=3),
            Skill(name="Docker", icon="🐳", category_id=4),
            Skill(name="Git", icon="📚", category_id=4)
        ]
        
        for skill in skills:
            db.session.add(skill)
        db.session.commit()
        print("Created skills")

        # Create projects
        projects = [
            Project(
                title="Portfolio Website",
                short_description="A personal portfolio built with Flask and modern web technologies",
                description="This is a comprehensive portfolio website showcasing my skills and projects. Built with Flask, SQLAlchemy, and modern frontend technologies including Tailwind CSS and JavaScript animations.",
                image_url="https://picsum.photos/800/600?random=1",
                video_url="/static/videos/portfolio_artist.mp4",
                link_url="https://github.com/yourusername/portfolio",
                languages_used="Python, Flask, SQLAlchemy, HTML, CSS, JavaScript"
            ),
            Project(
                title="E-commerce Platform",
                short_description="Full-stack e-commerce solution with payment integration",
                description="A complete e-commerce platform with user authentication, product management, shopping cart functionality, and payment processing. Features include order tracking, inventory management, and admin dashboard.",
                image_url="https://picsum.photos/800/600?random=2",
                video_url="/static/videos/multi_indicator.mp4",
                link_url="https://github.com/yourusername/ecommerce",
                languages_used="Python, Django, PostgreSQL, JavaScript, Stripe API"
            ),
            Project(
                title="Task Management App",
                short_description="Collaborative task management with real-time updates",
                description="A real-time task management application that allows teams to collaborate on projects. Features include task assignment, progress tracking, file sharing, and real-time notifications using WebSockets.",
                image_url="https://picsum.photos/800/600?random=3",
                video_url="/static/videos/november.mp4",
                link_url="https://github.com/yourusername/taskmanager",
                languages_used="Python, Flask, SQLAlchemy, WebSockets, JavaScript"
            )
        ]
        
        for project in projects:
            db.session.add(project)
        db.session.commit()
        print("Created projects")

        # Create experiences
        experiences = [
            Experience(
                name="Software Engineer at TechCorp",
                short_description="Full-stack development with modern technologies",
                description="Led development of multiple web applications using Python, Django, and React. Implemented CI/CD pipelines, improved application performance by 40%, and mentored junior developers.",
                url="https://techcorp.com",
                img_src="https://picsum.photos/400/300?random=4",
                languages_used="Python, Django, React, PostgreSQL, Docker"
            ),
            Experience(
                name="Backend Developer at StartupXYZ",
                short_description="API development and database optimization",
                description="Developed RESTful APIs and microservices architecture. Optimized database queries resulting in 60% faster response times. Implemented automated testing and deployment processes.",
                url="https://startupxyz.com",
                img_src="https://picsum.photos/400/300?random=5",
                languages_used="Python, Flask, MySQL, Redis, AWS"
            ),
            Experience(
                name="Freelance Web Developer",
                short_description="Custom web solutions for various clients",
                description="Built custom websites and web applications for diverse clients. Specialized in e-commerce solutions, content management systems, and responsive design. Managed client relationships and project delivery.",
                url="https://freelance-portfolio.com",
                img_src="https://picsum.photos/400/300?random=6",
                languages_used="PHP, Laravel, JavaScript, MySQL, HTML/CSS"
            )
        ]
        
        for experience in experiences:
            db.session.add(experience)
        db.session.commit()
        print("Created experiences")

        # Create blog posts
        posts = [
            Post(
                title="Getting Started with Flask",
                content="Flask is a lightweight web framework for Python that makes it easy to build web applications. In this post, we'll explore the basics of Flask and how to create your first web application.\n\n## Installation\n\nFirst, install Flask using pip:\n\n```bash\npip install flask\n```\n\n## Basic Application\n\nHere's a simple Flask application:\n\n```python\nfrom flask import Flask\n\napp = Flask(__name__)\n\n@app.route('/')\ndef hello_world():\n    return 'Hello, World!'\n\nif __name__ == '__main__':\n    app.run()\n```\n\nThis creates a basic web server that responds with 'Hello, World!' when you visit the root URL.",
                date_posted=datetime.utcnow(),
                image_url="/static/img/profile_pictures/blog_post_profile_pic_cropped.png"
            ),
            Post(
                title="Database Design Best Practices",
                content="Good database design is crucial for the performance and maintainability of your applications. Here are some best practices to follow when designing your database schema.\n\n## Normalization\n\nNormalize your data to reduce redundancy and improve data integrity. However, don't over-normalize as it can impact performance.\n\n## Indexing\n\nCreate indexes on columns that are frequently used in WHERE clauses, JOIN conditions, and ORDER BY clauses.\n\n## Relationships\n\nUse foreign keys to establish relationships between tables and maintain referential integrity.\n\n## Naming Conventions\n\nUse consistent naming conventions for tables, columns, and constraints to make your schema more readable and maintainable.",
                date_posted=datetime.utcnow(),
                image_url="/static/img/profile_pictures/blog_post_profile_pic_cropped.png"
            ),
            Post(
                title="Docker for Development",
                content="Docker has revolutionized how we develop and deploy applications. It provides a consistent environment across different machines and makes it easy to manage dependencies.\n\n## Benefits\n\n- **Consistency**: Same environment across development, staging, and production\n- **Isolation**: Each application runs in its own container\n- **Portability**: Easy to move applications between different environments\n- **Scalability**: Simple to scale applications horizontally\n\n## Basic Commands\n\n```bash\n# Build an image\ndocker build -t myapp .\n\n# Run a container\ndocker run -p 5000:5000 myapp\n\n# Stop a container\ndocker stop <container_id>\n```",
                date_posted=datetime.utcnow(),
                image_url="/static/img/profile_pictures/blog_post_profile_pic_cropped.png"
            )
        ]
        
        for post in posts:
            db.session.add(post)
        db.session.commit()
        print("Created blog posts")

        print("Database populated successfully!")
        
    except Exception as e:
        print(f"Error populating database: {e}")
        db.session.rollback()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)

    with app.app_context():
        try:
            db.create_all()
            print("Database tables created successfully")
            populate_database()
        except Exception as e:
            print(f"Error creating tables: {e}")

    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
