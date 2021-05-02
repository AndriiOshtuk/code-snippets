""" Code from lldpd/tests/integration/fixtures/namespaces.py
https://github.com/lldpd/lldpd/blob/11c5322cdce727219f88806dbada7795175aa319/tests/integration/fixtures/namespaces.py#L145
"""
import contextlib

@contextlib.contextmanager
def keep_directory():
    """Restore the current directory on exit."""
    pwd = os.getcwd()
    try:
        yield
    finally:
        os.chdir(pwd)
        
 with keep_directory():
    pass
