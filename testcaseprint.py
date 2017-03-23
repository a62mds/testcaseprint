import unittest


class TestCasePrint(unittest.TestCase):
    """Extends unittest.TestCase, providing functionality to test the output
    printed using print() against an expected string
    """
    @contextmanager
    def captured_output(self):
        """
        Temporarily captures output by redirecting sys.stdout and sys.stderr
        to StringIO() objects. Resets stdout and stderr before exiting context.
        """
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    def assertPrints(self, printing_method, expected_output):
        """
        Asserts that a function prints a given string. String may be multiline
        """
        with self.captured_output() as (output, error):
            printing_method()
            output = output.getvalue().strip()
            self.assertEqual(output, expected_output)

# Adapted from http://stackoverflow.com/questions/4219717/how-to-assert-output-with-nosetest-unittest-in-python
# M. Sullivan. March, 2017
