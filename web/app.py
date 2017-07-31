import os

from flask import Flask
from flask_script import Manager

from commands.places import manager as places_manager
from commands.es import manager as es_manager


app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS_FILE',
                                 'settings.DevelopmentConfig'))
manager = Manager(app)
manager.add_command("foursquare", places_manager)
manager.add_command("elasticsearch", es_manager)


if __name__ == "__main__":
    manager.run()
