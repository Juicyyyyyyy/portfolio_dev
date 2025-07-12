import os
from flask import Flask, request, render_template, redirect, url_for, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from dotenv import load_dotenv
from datetime import datetime
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from app.models.user import User

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
admin = Admin(template_mode='bootstrap3')
login_manager = LoginManager()
login_manager.login_view = 'login'

# Import all models so they are registered with SQLAlchemy
from app.models.experience import Experience
from app.models.post import Post
from app.models.project import Project
from app.models.skill import Skill
from app.models.skill_category import Category

@login_manager.user_loader
def load_user(user_id):
    if user_id == os.getenv('ADMIN_USERNAME'):
        return User(user_id)
    return None

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
                image_url="https://www.ubuntumint.com/wp-content/uploads/2022/06/Debian-Linux.png"
            ),
            Post(
                title="Database Design Best Practices",
                content="Good database design is crucial for the performance and maintainability of your applications. Here are some best practices to follow when designing your database schema.\n\n## Normalization\n\nNormalize your data to reduce redundancy and improve data integrity. However, don't over-normalize as it can impact performance.\n\n## Indexing\n\nCreate indexes on columns that are frequently used in WHERE clauses, JOIN conditions, and ORDER BY clauses.\n\n## Relationships\n\nUse foreign keys to establish relationships between tables and maintain referential integrity.\n\n## Naming Conventions\n\nUse consistent naming conventions for tables, columns, and constraints to make your schema more readable and maintainable.",
                date_posted=datetime.utcnow(),
                image_url="https://www.ubuntumint.com/wp-content/uploads/2022/06/Debian-Linux.png"
            ),
            Post(
                title="Docker for Development",
                content="Docker has revolutionized how we develop and deploy applications. It provides a consistent environment across different machines and makes it easy to manage dependencies.\n\n## Benefits\n\n- **Consistency**: Same environment across development, staging, and production\n- **Isolation**: Each application runs in its own container\n- **Portability**: Easy to move applications between different environments\n- **Scalability**: Simple to scale applications horizontally\n\n## Basic Commands\n\n```bash\n# Build an image\ndocker build -t myapp .\n\n# Run a container\ndocker run -p 5000:5000 myapp\n\n# Stop a container\ndocker stop <container_id>\n```",
                date_posted=datetime.utcnow(),
                image_url="https://www.ubuntumint.com/wp-content/uploads/2022/06/Debian-Linux.png"
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
    app.secret_key = os.getenv('SECRET_KEY', 'dev')

    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    login_manager.init_app(app)

    # Register models with Flask-Admin, restrict to logged-in users
    class AdminModelView(ModelView):
        def is_accessible(self):
            return current_user.is_authenticated
        def inaccessible_callback(self, name, **kwargs):
            from flask import redirect, url_for
            return redirect(url_for('login'))

    class ImageUploadView(BaseView):
        def is_accessible(self):
            return current_user.is_authenticated
        def inaccessible_callback(self, name, **kwargs):
            from flask import redirect, url_for
            return redirect(url_for('login'))

        def get_folders(self):
            """Get list of folders in the posts directory"""
            upload_dir = os.path.join(app.static_folder, 'img', 'posts')
            folders = []
            
            if os.path.exists(upload_dir):
                for item in os.listdir(upload_dir):
                    item_path = os.path.join(upload_dir, item)
                    if os.path.isdir(item_path):
                        folders.append(item)
            
            return sorted(folders)

        @expose('/', methods=['GET', 'POST'])
        def index(self):
            folders = self.get_folders()
            
            if request.method == 'POST':
                if 'file' not in request.files:
                    flash('No file selected', 'error')
                    return self.render('admin/image_upload.html', folders=folders)
                
                file = request.files['file']
                if file.filename == '':
                    flash('No file selected', 'error')
                    return self.render('admin/image_upload.html', folders=folders)
                
                if file:
                    # Validate file type
                    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
                    filename = secure_filename(file.filename)
                    file_ext = filename.rsplit('.', 1)[1].lower() if '.' in filename else ''
                    
                    if file_ext not in allowed_extensions:
                        flash('Invalid file type. Allowed: PNG, JPG, JPEG, GIF, WebP', 'error')
                        return self.render('admin/image_upload.html', folders=folders)
                    
                    # Validate file size (10MB limit)
                    file.seek(0, 2)  # Seek to end
                    file_size = file.tell()
                    file.seek(0)  # Reset to beginning
                    
                    if file_size > 10 * 1024 * 1024:  # 10MB
                        flash('File size too large. Maximum size is 10MB', 'error')
                        return self.render('admin/image_upload.html', folders=folders)
                    
                    # Get selected folder
                    selected_folder = request.form.get('folder', '').strip()
                    
                    # Ensure the upload directory exists
                    upload_dir = os.path.join(app.static_folder, 'img', 'posts')
                    if selected_folder:
                        upload_dir = os.path.join(upload_dir, selected_folder)
                    os.makedirs(upload_dir, exist_ok=True)
                    
                    # Check if file already exists and add number if needed
                    base_name, ext = os.path.splitext(filename)
                    counter = 1
                    while os.path.exists(os.path.join(upload_dir, filename)):
                        filename = f"{base_name}_{counter}{ext}"
                        counter += 1
                    
                    file_path = os.path.join(upload_dir, filename)
                    file.save(file_path)
                    
                    # Return the URL path for easy copying
                    if selected_folder:
                        image_url = f"/static/img/posts/{selected_folder}/{filename}"
                    else:
                        image_url = f"/static/img/posts/{filename}"
                    
                    flash(f'Image uploaded successfully! URL: {image_url}', 'success')
                    return self.render('admin/image_upload.html', uploaded_url=image_url, folders=folders)
            
            return self.render('admin/image_upload.html', folders=folders)

        @expose('/create_folder', methods=['GET', 'POST'])
        def create_folder(self):
            """Create a new folder"""
            if request.method == 'POST':
                folder_name = request.form.get('folder_name', '').strip()
                
                if not folder_name:
                    flash('Folder name is required', 'error')
                    return redirect(url_for('image_upload.index'))
                
                # Validate folder name (alphanumeric and hyphens only)
                import re
                if not re.match(r'^[a-zA-Z0-9_-]+$', folder_name):
                    flash('Folder name can only contain letters, numbers, hyphens, and underscores', 'error')
                    return redirect(url_for('image_upload.index'))
                
                # Create folder
                upload_dir = os.path.join(app.static_folder, 'img', 'posts')
                folder_path = os.path.join(upload_dir, folder_name)
                
                if os.path.exists(folder_path):
                    flash(f'Folder "{folder_name}" already exists', 'error')
                    return redirect(url_for('image_upload.index'))
                
                try:
                    os.makedirs(folder_path, exist_ok=True)
                    flash(f'Folder "{folder_name}" created successfully!', 'success')
                except Exception as e:
                    flash(f'Error creating folder: {str(e)}', 'error')
                
                return redirect(url_for('image_upload.index'))
            
            return self.render('admin/create_folder.html')

        @expose('/list')
        def list_images(self):
            """List all uploaded images"""
            upload_dir = os.path.join(app.static_folder, 'img', 'posts')
            images = []
            folders = []
            
            if os.path.exists(upload_dir):
                for item in os.listdir(upload_dir):
                    item_path = os.path.join(upload_dir, item)
                    if os.path.isdir(item_path):
                        folders.append(item)
                        # Get images in this folder
                        for filename in os.listdir(item_path):
                            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                                file_path = os.path.join(item_path, filename)
                                file_size = os.path.getsize(file_path)
                                images.append({
                                    'filename': filename,
                                    'folder': item,
                                    'url': f"/static/img/posts/{item}/{filename}",
                                    'size': file_size,
                                    'size_mb': round(file_size / (1024 * 1024), 2)
                                })
                    elif item.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                        # Images in root directory
                        file_path = os.path.join(upload_dir, item)
                        file_size = os.path.getsize(file_path)
                        images.append({
                            'filename': item,
                            'folder': 'Root',
                            'url': f"/static/img/posts/{item}",
                            'size': file_size,
                            'size_mb': round(file_size / (1024 * 1024), 2)
                        })
            
            # Sort by folder, then by filename
            images.sort(key=lambda x: (x['folder'], x['filename']))
            return self.render('admin/image_list.html', images=images, folders=folders)

    admin.add_view(ImageUploadView(name='Image Upload', endpoint='image_upload'))
    admin.add_view(AdminModelView(Skill, db.session))
    admin.add_view(AdminModelView(Category, db.session))
    admin.add_view(AdminModelView(Experience, db.session))
    admin.add_view(AdminModelView(Project, db.session))
    admin.add_view(AdminModelView(Post, db.session))

    # Login route
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            if username == os.getenv('ADMIN_USERNAME') and password == os.getenv('ADMIN_PASSWORD'):
                user = User(username)
                login_user(user)
                return redirect(url_for('admin.index'))
            else:
                flash('Invalid credentials', 'danger')
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('login'))

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
