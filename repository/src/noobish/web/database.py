from .services import FileBin, RestServiceResponseBody


# Database structure
class Database():
    # For initiating the microservices
    def __init__(self, name: str):
        # Setting up filebin
        self.filebin = FileBin(name)

    def get(self, primary_key: str) -> RestServiceResponseBody:
        # Selecting with primary key
        return self.filebin.download(primary_key)

    def push(self, primary_key: str, data: dict) -> RestServiceResponseBody:
        # Adding to database with data
        return self.filebin.upload(data, primary_key)

    def list(self):
        return self.filebin.list()

    def delete(self, primary_key: str):
        # Remove an item from the database
        return self.filebin.remove(primary_key)
