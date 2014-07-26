from __future__ import absolute_import

from auth.auth import AuthEnabledRequestHandler
from settings import settings
from jinja2 import Environment, FileSystemLoader

import json

TEMPLATE_ENV = Environment(
    loader=FileSystemLoader(settings.secure.templates_path)
)


class BaseHandler(AuthEnabledRequestHandler):

    def render(self, template_filename, context={}):
        template = TEMPLATE_ENV.get_template(template_filename)
        output = template.render(context)
        self.write(output)

    def writeln(self, s=''):
        self.write('%s\n' % s)

class TemplateHandler(BaseHandler):

    def initialize(self, template_filename, context={}):
        self.template_filename = template_filename
        self.context = context

    def get(self):
        self.render(self.template_filename, self.context)

def json_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    elif hasattr(obj, 'total_seconds'):
        return obj.total_seconds()
    else:
        raise TypeError, 'Object of type %s with value of %s is not JSON serializable' % (type(obj), repr(obj))

def dumps(obj):
    return json.dumps(obj, default=json_handler)
