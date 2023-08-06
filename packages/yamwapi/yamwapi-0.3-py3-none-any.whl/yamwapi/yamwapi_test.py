import yamwapi

import mock
import requests_mock
import unittest
import urllib.parse

class MediaWikiAPITest(unittest.TestCase):
    TEST_API_URL = 'http://w.org/api.php'
    TEST_USER_AGENT = 'user agent'

    def setUp(self):
        self._api = yamwapi.MediaWikiAPI(self.TEST_API_URL, self.TEST_USER_AGENT)

    def test_default_options(self):
        self.assertEqual(self._api.options.maxlag, 5)
        self.assertEqual(self._api.options.max_retries_maxlag, 3)
        self.assertEqual(self._api.options.http_retries, 3)

    def test_session_options(self):
        self._api.options.http_retries = 5
        self.assertEqual(
            self._api.session.adapters['http://'].max_retries.total,
            self._api.options.http_retries)
        self.assertEqual(
            self._api.session.adapters['https://'].max_retries.total,
            self._api.options.http_retries)

    def test_simple_query_with_options(self):
        self._api.options.maxlag = 3
        expected_request = {
            'pageids': '12345',
            'format': 'json',
            'continue': '',
            'maxlag': '3',
            'action': 'query',
            'utf8': ''
        }
        with requests_mock.mock() as m:
            m.post(self.TEST_API_URL, json = {})
            self.assertEqual(next(self._api.query({'pageids': '12345'})), {})
            request = m.request_history[0]
            sent = urllib.parse.parse_qsl(request.text, keep_blank_values = True)
            self.assertEqual(dict(sent), expected_request)
            self.assertEqual(
                request.headers['User-Agent'], self.TEST_USER_AGENT)

    def test_simple_parse_with_options(self):
        self._api.options.maxlag = 3
        expected_request = {
            'text': '{{ cn }}',
            'format': 'json',
            'maxlag': '3',
            'action': 'parse',
            'utf8': ''
        }
        with requests_mock.mock() as m:
            m.post(self.TEST_API_URL, json = {})
            self.assertEqual(self._api.parse({'text': '{{ cn }}'}), {})
            request = m.request_history[0]
            sent = urllib.parse.parse_qsl(request.text, keep_blank_values = True)
            self.assertTrue(dict(sent), expected_request)
            self.assertEqual(
                request.headers['User-Agent'], self.TEST_USER_AGENT)

    def test_retry_after_once(self):
        with mock.patch.object(self._api.session, 'post') as mock_post:
            with mock.patch.object(yamwapi.time, 'sleep') as mock_sleep:
                mock_retry_after_response = mock.MagicMock()
                mock_retry_after_response.headers = {'Retry-After': '3.5'}
                mock_post.side_effect = [
                    mock_retry_after_response, mock.MagicMock()]
                self._api.parse({'text': 'x'})
                mock_sleep.assert_called_once_with(3.5)
                self.assertEqual(mock_post.call_count, 2)

    def test_retry_after_too_many(self):
        self._api.options.max_retries_maxlag = 1
        with mock.patch.object(self._api.session, 'post') as mock_post:
            with mock.patch.object(yamwapi.time, 'sleep') as mock_sleep:
                mock_retry_after_response = mock.MagicMock()
                mock_retry_after_response.headers = {'Retry-After': '3.5'}
                mock_post.side_effect = [
                    mock_retry_after_response, mock_retry_after_response,
                    mock.MagicMock()]
                with self.assertRaises(yamwapi.MediaWikiAPIError):
                    self._api.parse({'text': 'x'})
                mock_sleep.assert_called_once_with(3.5)

    def test_cache_maxlag_retry(self):
        with mock.patch.object(self._api.session, 'post') as mock_post:
            with mock.patch.object(yamwapi.time, 'sleep') as mock_sleep:
                mock_maxlag_response = mock.MagicMock()
                mock_maxlag_response.json.return_value = {
                    'error': {
                        'code': 'maxlag',
                        'info': 'Waiting for host: 3.5 seconds lagged'}
                }
                mock_post.side_effect = [
                    mock_maxlag_response, mock.MagicMock()]
                self._api.parse({'text': 'x'})
                mock_sleep.assert_called_once_with(3.5)
                self.assertEqual(mock_post.call_count, 2)

    def test_no_retries_fail(self):
        self._api.options.max_retries_maxlag = 0
        with mock.patch.object(self._api.session, 'post') as mock_post:
            with mock.patch.object(yamwapi.time, 'sleep') as mock_sleep:
                mock_retry_after_response = mock.MagicMock()
                mock_retry_after_response.headers = {'Retry-After': '3.5'}
                mock_post.side_effect = [
                    mock_retry_after_response, mock_retry_after_response,
                    mock.MagicMock()]
                with self.assertRaises(yamwapi.MediaWikiAPIError):
                    self._api.parse({'text': 'x'})
                mock_sleep.assert_not_called()  # just raise the exception

    def test_no_retries_success(self):
        self._api.options.max_retries_maxlag = 0
        with mock.patch.object(self._api.session, 'post') as mock_post:
            with mock.patch.object(yamwapi.time, 'sleep') as mock_sleep:
                mock_post.return_value = mock.MagicMock()
                self._api.parse({'text': 'x'})
                mock_sleep.assert_not_called()

if __name__ == '__main__':
    unittest.main()
