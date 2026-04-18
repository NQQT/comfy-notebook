from .services import FileBin, RestServiceResponseBody


class Database():
    def __init__(self, name: str):
        try:
            self.filebin = FileBin(name)
        except Exception:
            self.filebin = None

    def get(self, primary_key: str):
        try:
            return self.filebin.download(primary_key)
        except Exception:
            return None

    def push(self, primary_key: str, data: dict):
        try:
            return self.filebin.upload(data, primary_key)
        except Exception:
            return None

    def list(self):
        try:
            return self.filebin.list()
        except Exception:
            return None

    def delete(self, primary_key: str):
        try:
            return self.filebin.remove(primary_key)
        except Exception:
            return None