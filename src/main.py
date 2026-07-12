import typer
from core.initializer import init_project
from core.assigner import assign_url

app = typer.Typer()

@app.command()
def init(name: str = typer.Argument(None)):
    try:
        path = init_project(name)
        typer.echo(f"✓ Initialized project at {path}")
    except FileExistsError as e:
        typer.echo(f"✗ {e}", err=True)
        raise typer.Exit(code=1)

@app.command()
def set(url: str):
    try:
        path = assign_url(url)
        typer.echo(f"✓ URL saved to {path.name}")
    except FileNotFoundError as e:
        typer.echo(f"✗ {e}", err=True)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
