import os
from os.path import dirname, join
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

class Test:

    def testRecord(self):
        client = app.test_client()
        url = ''
        response = client.get(url)
        assert response.status_code == 200
