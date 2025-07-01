from flask import Flask, request
from dotenv import load_dotenv
import os
from config import Config
from extensions import db, migrate

# Load environment variables from .env
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from routes import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/add_user', methods=['GET', 'POST'])
    def add_user():
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            from models import User
            user = User(username=username, email=email)
            db.session.add(user)
            db.session.commit()
            return "User added!"
        return '''
            <form method="post">
                Username: <input name="username"><br>
                Email: <input name="email"><br>
                <input type="submit" value="Add User">
            </form>
        '''

    @app.route('/list_users')
    def list_users():
        from models import User
        from extensions import db
        users = User.query.all()
        table = '<table border="1"><tr><th>ID</th><th>Username</th><th>Email</th></tr>'
        for user in users:
            table += f'<tr><td>{user.id}</td><td>{user.username}</td><td>{user.email}</td></tr>'
        table += '</table>'
        return f'<h2>All Users</h2>{table}'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True) 