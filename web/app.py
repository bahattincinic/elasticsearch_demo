import os

from flask import Flask
from flask_script import Manager

from commands.places import manager as places_manager


app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS_FILE',
                                 'settings.DevelopmentConfig'))
manager = Manager(app)
manager.add_command("places", places_manager)


if __name__ == "__main__":
    manager.run()
