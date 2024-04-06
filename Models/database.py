from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class DBSingleton:
    _instance = None

    def __new__(cls, app=None):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            if app:
                cls._instance.init_app(app)
        return cls._instance

    def init_app(self, app):
        app.config.setdefault('SQLALCHEMY_DATABASE_URI', 'mysql://root:123456@localhost/tramite_escuela2')
        db.init_app(app)
        self.db = db
