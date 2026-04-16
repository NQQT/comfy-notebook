# test_filebin.py
import time
import unittest

from noobish.web import FileBin


class TestFileBin(unittest.TestCase):
    bin_name = f"noobscript-test-{int(time.time() * 1000)}"
    filename = "hello.txt"
    content = "hello world!"
    filebin = FileBin(bin=bin_name)

    @classmethod
    def setUpClass(cls):
        """Upload the file once before all tests in this class."""
        cls.upload_response = cls.filebin.upload(cls.content, cls.filename)

    def test_1_upload(self):
        """Upload response should have correct metadata."""
        self.assertEqual(self.upload_response, {
            "filename": self.filename,
            "filesize": 12,
            "checksum": "7509e5bda0c762d2bac7f90d758b5b2263fa01ccbc542ab5e3df163be08e6ca9",
        })

    def test_2_list(self):
        """Should return the file listing."""
        file_list = self.filebin.list()
        self.assertEqual(file_list, [
            {
                "filename": self.filename,
                "filesize": 12,
                "checksum": "7509e5bda0c762d2bac7f90d758b5b2263fa01ccbc542ab5e3df163be08e6ca9",
            }
        ])

    def test_3_download(self):
        """Should be able to retrieve the file content."""
        downloaded = self.filebin.download(self.filename)
        self.assertEqual(downloaded, self.content)
