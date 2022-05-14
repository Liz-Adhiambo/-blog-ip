from blogip import create_app,db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager,Server
from blogip.models import Subscriber, User,Post,Comment





app = create_app()

migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('server',Server)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Comment = Comment, Post=Post,Subscriber=Subscriber) 

if __name__ == '__main__':
    manager.run()