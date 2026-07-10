import typer
from core.initializer import init_project


app = typer.Typer()

@app.command()
def init(name: str = typer.Argument(None)):
    try:
        init_project(name)
        typer.echo(f"✓ Initialized project at {name or '.'}")
    except FileExistsError as e:
        typer.echo(f"● {e}", err=True)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
