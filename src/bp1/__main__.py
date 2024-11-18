"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """bestie1."""


if __name__ == "__main__":
    main(prog_name="bp1")  # pragma: no cover
