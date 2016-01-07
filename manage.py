#!/usr/bin/env python
from flask.ext.script import Manager, Server
from flask_script.commands import ShowUrls, Clean

from guid_server import app

manager = Manager(app)
server = Server(host="0.0.0.0", port=7001)
manager.add_command("runserver", server)
app.config.from_object('config-default')


@manager.shell
def make_shell_context():
    """
    Creates a python REPL with several default imports
    in the context of the app
    """
    return dict(app=app)


@manager.command
def list_routes():
    output = []
    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__

    from pprint import pprint
    pprint(func_list)


if __name__ == "__main__":
    manager.add_command("clean", Clean())
    manager.add_command("show_urls", ShowUrls())

    manager.run()
