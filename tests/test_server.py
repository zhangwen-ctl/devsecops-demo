import json
import unittest
from http.client import HTTPConnection
from threading import Thread

from app.server import RequestHandler, ThreadingHTTPServer


class ServerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), RequestHandler)
        cls.thread = Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.port = cls.server.server_address[1]

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def get_json(self, path):
        connection = HTTPConnection("127.0.0.1", self.port)
        connection.request("GET", path)
        response = connection.getresponse()
        payload = json.loads(response.read())
        connection.close()
        return response.status, payload

    def test_health_endpoint(self):
        status, payload = self.get_json("/health")
        self.assertEqual(status, 200)
        self.assertEqual(payload["status"], "UP")

    def test_version_endpoint(self):
        status, payload = self.get_json("/version")
        self.assertEqual(status, 200)
        self.assertEqual(payload["service"], "devsecops-demo")

    def test_unknown_endpoint(self):
        status, payload = self.get_json("/missing")
        self.assertEqual(status, 404)
        self.assertEqual(payload["error"], "not found")