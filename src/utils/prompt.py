from pathlib import Path
from rich.console import Console


console = Console()

def display_path(path: Path) -> str:
    cwd = Path.cwd()
    try:
        rel = path.relative_to(cwd)
    except ValueError:
        rel = Path(f"{path.parent.name}/{path.name}")

    result = str(rel)
    if path.is_dir() and not result.endswith("/"):
        result += "/"

    return result

def success(message: str, path: Path | None = None) -> None:
    """Prints a success message with a relative path."""
    if path is not None:
        console.print(f"[green]✓[/green] {message} [blue]{display_path(path)}[/blue]")
    else:
        console.print(f"[green]✓[/green] {message}")

def failure(message: str, path: Path | None = None) -> None:
    """Prints a failure message with a relative path."""
    if path is not None:
        console.print(f"[red]✗[/red] {message} [yellow]{display_path(path)}[/yellow]")
    else:
        console.print(f"[red]✗[/red] {message}")
