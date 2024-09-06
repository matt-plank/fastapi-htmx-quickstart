from fastapi import Response
from jinja2 import Environment, FileSystemLoader

loader = FileSystemLoader("templates")
environment = Environment(loader=loader, cache_size=0)
environment.globals.update({})


def component(filepath: str, macro_name: str, args: dict, headers: dict = {}):
    """Render a Jinja2 macro as a FastAPI response."""
    macro = environment.get_template(filepath).module.__dict__.get(macro_name)

    if macro is None:
        raise ValueError(f"Macro {macro_name!r} not found in {filepath!r}")

    response_content = macro(**args)

    return Response(
        content=response_content,
        media_type="text/html",
        headers=headers,
    )
