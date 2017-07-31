from flask_script import Manager


manager = Manager(usage="ElasticSearch")


@manager.command
def build():
    """
    Create elasticsearch Indexes
    """
