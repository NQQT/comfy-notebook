# filebin.py
from .classes import RestService, RestServiceResponseBody


def _as_filebin_file(content: dict) -> dict:
    return {
        "filename": content.get("filename"),
        "filesize": content.get("bytes"),
        "checksum": content.get("sha256"),
    }


class FileBin(RestService):
    def __init__(self, bin: str):
        self._host = f"https://filebin.net/{bin}/"

    @property
    def host(self) -> str:
        return self._host

    def list(self) -> list:
        result = self.get("")
        return [_as_filebin_file(file) for file in (result.get("files") or [])]

    def upload(self, data: str, filename: str) -> RestServiceResponseBody:
        """
        Uploads file content to the configured Filebin bin.
        :param data: The raw file content as a string.
        :param filename: The name to give the file on Filebin.
        :returns: A dict with filename, filesize, and checksum.
        """
        content = self.post(
            filename,
            header={
                "Content-Type": "application/octet-stream",
                "filename": filename,
            },
            body=data,
        )
        return _as_filebin_file(content.get("file", {}))

    def download(self, filename: str) -> str:
        """
        Downloads a file from the configured Filebin bin.
        :param filename: The name of the file to retrieve.
        :returns: The raw file content as a string.
        """
        response = self.get(
            filename,
            header={
                "Cookie": "verified=2024-05-24",
                "Accept": "*/*",
            },
        )
        return response.get("data", "")

    def remove(self, filename: str):
        # Remove an item from the server
        remove.delete(
            filename,
            header={
                "Cookie": "verified=2024-05-24",
                "Accept": "*/*",
            },
        )
