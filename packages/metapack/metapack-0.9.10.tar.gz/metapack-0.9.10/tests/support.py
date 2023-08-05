import unittest


def test_data(*paths):
    from os.path import dirname, join, abspath
    import metapack
    import test_data

    return join(dirname(abspath(test_data.__file__)), *paths)


def cache_fs():

    from fs.tempfs import TempFS

    return TempFS('rowgenerator')

def get_cache():
    return cache_fs()

class MetapackTest(unittest.TestCase):
    """Test Metapack AppUrls and Row Generators"""

    def setUp(self):
        import warnings
        warnings.simplefilter('ignore')
