from pathlib import Path
import fusexp

def pytest_report_header(config):
    """Add information on the package version used in the tests.
    """
    modpath = Path(fusexp.__file__).resolve().parent
    return [ "fusexp: %s" % (fusexp.__version__),
             "           %s" % (modpath)]
