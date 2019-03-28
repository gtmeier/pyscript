import inspect
import os
import unittest


class ShapeTestCase(unittest.TestCase):

    _postscript_code_path = os.path.join('tests', 'postscript-code')
    _test_file_path = os.path.join(_postscript_code_path, 'test.ps')

    def tearDown(self):
        if os.path.exists(self._test_file_path):
            assert os.path.isfile(self._test_file_path)
            os.remove(self._test_file_path)

    def _test_export_postscript(self, shape, center):
        # Use plain assert because this is a precondition, not a test
        # assertion.
        assert not os.path.exists(self._test_file_path)

        shape.export_postscript(center=center, filename=self._test_file_path)
        self.assertTrue(os.path.isfile(self._test_file_path))

        with open(self._test_file_path, 'r') as test_file:
            test_code = test_file.read()

        expected_output_file_path = os.path.join(
            self._postscript_code_path,
            self._get_test_case_name(),  # TODO: set in constructor
            self._get_current_test_name() + '.ps'
        )
        with open(expected_output_file_path, 'r') as expected_output_file:
            expected_code = expected_output_file.read()

        self.assertEqual(test_code, expected_code)

    def _get_current_test_name(self):
        test_prefix = 'test_export_postscript_'
        current_test_full_name = (
            inspect.currentframe().f_back.f_back.f_code.co_name
        )
        assert current_test_full_name.startswith(test_prefix)
        return current_test_full_name[len(test_prefix):]

    def _get_test_case_name(self):
        test_case_suffix = 'TestCase'
        test_case_full_name = type(self).__name__
        assert test_case_full_name.endswith(test_case_suffix)
        test_case_name_len = len(test_case_full_name) - len(test_case_suffix)
        return test_case_full_name[:test_case_name_len]
