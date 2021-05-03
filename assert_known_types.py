""" From lldpd/tests/integration/fixtures/namespaces.py
https://github.com/lldpd/lldpd/blob/11c5322cdce727219f88806dbada7795175aa319/tests/integration/fixtures/namespaces.py#L145
"""
# All allowed namespace types
NAMESPACE_FLAGS = dict(mnt=0x00020000,
                       uts=0x04000000,
                       ipc=0x08000000,
                       user=0x10000000,
                       pid=0x20000000,
                       net=0x40000000)

class Namespace(object):

    def __init__(self, *namespaces):
        self.namespaces = namespaces
        for ns in namespaces:
            assert ns in NAMESPACE_FLAGS
