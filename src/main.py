import typer
import tomlkit
from pathlib import Path
from utils.prompt import success, failure
from core.initializer import init_project
from core.assigner import assign_url
from core.revealer import reveal_project


app = typer.Typer()

@app.command()
def init(name: str = typer.Argument(None)):
    try:
        path = init_project(name)
        success("Initialized project at", path)
    except FileExistsError as e:
        failure("Project already exist at", Path(str(e)))
        raise typer.Exit(code=1)

@app.command()
def set(url: str):
    try:
        path = assign_url(url)
        success("URL saved to", path)
    except FileNotFoundError as e:
        failure("No project found at", Path(str(e)))
        raise typer.Exit(code=1)

@app.command()
def reveal():
    try:
        doc = reveal_project()
        typer.echo(tomlkit.dumps(doc))
    except FileNotFoundError as e:
        failure("No project found at", Path(str(e)))
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
