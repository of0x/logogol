from logogol.test_base import BaseTestCase

import unittest
from flask import json, url_for


class IndexTestCase(BaseTestCase):

    def setUp(self):
        BaseTestCase.setUp(self)
        self.data = dict(url='http://www.example.com')
        self.app.post(url_for("index"),
                      data=json.dumps(self.data), content_type="application/json")

    def test_index(self):
        response = self.app.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_cors_headers(self):
        response = self.app.get(url_for('index'), headers={'Origin': 'www.example.com'})
        self.assertEqual(response.headers['Access-Control-Allow-Origin'], 'www.example.com')

    def test_index_allows_posts(self):
        data = dict(url='https://example.com')
        response = self.app.post(url_for('index'),
                data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_index_returns_lists(self):
        response = self.app.get(url_for('index') )
        self.assertIsInstance(json.loads(response.data.decode('utf-8')), list)

    def test_index_returns_entry(self):
        data = dict(url='https://another.example.com/thing')
        response = self.app.post(url_for('index'),
                data=json.dumps(data), content_type='application/json')
        self.assertEqual(data['url'], json.loads(response.data)['url'])

    def test_index_allows_delete(self):
        response = self.app.delete(url_for('link', link_id=1))  # id 1 is in setup
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), '{}\n')

    def test_index_saves_posted_data(self):
        data = dict(url='https://another.example.com')
        self.app.post(url_for('index'), data=json.dumps(data), content_type='application/json')
        response = self.app.get(url_for('link', link_id=2))
        response_data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_data['url'], data['url'])


if __name__ == '__main__':
    unittest.main()
