from logogol.test_base import BaseTestCase

from logogol.models import Link
from logogol.database import db_session


class LinkTestCase(BaseTestCase):

    def test_string_representation(self):
        text = "some text"
        entry = Link(text)
        db_session.add(entry)
        db_session.commit()
        query = Link.query.all()[0]
        self.assertEqual(str(query), "<Link: " + text + ">")

    def test_all_fields_created_and_queriable(self):
        expected_description = "description"
        expected_paths = "path1, path2, path3"
        expected_tags = "tag1, tag2, tag3"
        expected_url = "http://example.com"
        entry = Link(expected_url, description=expected_description, paths=expected_paths, tags=expected_tags)
        db_session.add(entry)
        db_session.commit()
        query = Link.query.filter(Link.description == expected_description).first()
        self.assertEqual(entry, query, "mismatched description")
        query = Link.query.filter(Link.paths == expected_paths).first()
        self.assertEqual(entry, query, "mismatched paths expected {0} query returned {1}".format(expected_paths, query))
        query = Link.query.filter(Link.tags == expected_tags).first()
        self.assertEqual(entry, query, "mismathced tags")
        query = Link.query.filter(Link.url == expected_url).first()
        self.assertEqual(entry, query, "mismatched url")
