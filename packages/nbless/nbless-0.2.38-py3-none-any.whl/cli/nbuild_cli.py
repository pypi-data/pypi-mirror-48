import sys
from typing import List

import click
import nbformat

from nbless.nbuild import nbuild


@click.command()
@click.argument("in_files", nargs=-1, required=True, type=click.Path(exists=True))
@click.option("-o", "--out_file", "out_file")
def nbuild_cli(in_files: List[str], out_file: str) -> None:
    """Create an unexecuted Jupyter notebook from markdown and code files.

    :param in_files: The source files used to create a Jupyter notebook file.
    :param out_file: The name of the output Jupyter notebook file.
    """
    nb = nbuild(in_files)
    if out_file:
        nbformat.write(nb, out_file, version=4)
    else:
        sys.stdout.write(nbformat.writes(nb))
