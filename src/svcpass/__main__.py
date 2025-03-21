"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """svcpass."""


if __name__ == "__main__":
    main(prog_name="svcpass-py")  # pragma: no cover
