import os
from pathlib import Path
from argparse import ArgumentParser


REDIR_TEMPLATE = """
<!doctype html>
<html>
<head>
    <link rel="canonical" href="//www.winningslowly.org/{number}/" />
    <meta http-equiv="refresh" content="0; url=//www.winningslowly.org/{number}/" />
</head>
</html>
"""

DEFAULT_ROOT = Path('show-notes') / 'root'


def root_redirects(items, root):
    """Add EXTRA_PATH_METADATA for automatically generating root files.

    Args:
        items: A list of files to use as the basis for the redirects.
        root: The directory in which to put the files.

    Returns:
        A modified copy of extra_path_metadata.

    Note:
        Assumes the file name of the items in `items` should be the same as
        the file name generated.

    """
    # Make sure the root directory exists to write the files to.
    if not root.exists():
        root.mkdir(parents=True)

    elif not root.is_dir():
        raise Exception("`root` ({}) is not a directory!".format(root.name))

    # Generate any redirects that need to be generated. Assume existing files
    # are pre-existing redirects and should be left alone.
    for i in items:
        root_i = root / i.with_suffix('.html').name
        if not root_i.exists():
            with root_i.open('w') as root_i_fd:
                root_i_fd.write(REDIR_TEMPLATE.format(number=i.stem))

    # Add all the root files to the metadata copy.
    root_metadata = {}
    redir_files = root.glob('*.html')
    for f in redir_files:
        key = root.name + '/' + f.name
        value = {'path': f.name}
        root_metadata[key] = value

    return root_metadata
