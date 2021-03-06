import unittest
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Abstrct class for database dependent test cases.
class AbstractDatabaseTestCase(unittest.TestCase):
    def setUp(self):
        """
        Creates engine and session_factory before each test.
        """
        self.engine = create_engine(os.getenv("TRYPPERDB_TEST_DB_URL"), echo=False)
        self.session_factory = sessionmaker(bind=self.engine)

    def tearDown(self):
        """
        Removes data from all tables after each tests.
        """
        with self.engine.connect() as db_connection:
            for table in ['proteins_peptides', 'peptides', 'proteins', 'protein_merges','taxonomies', 'taxonomy_merges']:
                db_connection.execute(f"delete from {table};")