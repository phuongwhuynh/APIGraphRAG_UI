from jinja2 import Environment, FileSystemLoader
from openapi_trace_ui.utils import helpers
import inspect

env = Environment(loader=FileSystemLoader("openapi_trace_ui/templates"))

# Register all helper functions from the helpers module as Jinja globals
for name, obj in inspect.getmembers(helpers, inspect.isfunction):
    env.globals[name] = obj


def render_app(spec):
    template = env.get_template("index.html")

    return template.render(
        spec=spec,
    )
