from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("openapi_trace_ui/templates"))


def render_app(spec: dict):
    template = env.get_template("index.html")
    return template.render(spec=spec)
