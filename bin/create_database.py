#!/usr/bin/env python3

from pathlib import Path

import typer

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
app = typer.Typer(help="Generate mock database", add_completion=False)


@app.command()
def main():
    return


if __name__ == "__main__":
    app()