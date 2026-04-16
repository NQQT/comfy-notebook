# rest_service.py
import json
import urllib.parse
import urllib.request
from abc import ABC, abstractmethod
from typing import Any, Optional

RestServiceResponseBody = Any


class RestService(ABC):
    """
    Base class for implementing REST service clients.
    Extend this class and set the `host` property.
    """

    @property
    @abstractmethod
    def host(self) -> str:
        """Subclasses must define the base host URL."""
        ...

    def get(self, endpoint: str, header: Optional[dict] = None, body: Optional[dict] = None) -> RestServiceResponseBody:
        url = self._build_url(endpoint, body)
        req = urllib.request.Request(url, headers=self._build_headers(header), method="GET")
        return self._handle_response(req)

    def post(self, endpoint: str, header: Optional[dict] = None, body: Any = None) -> RestServiceResponseBody:
        url = f"{self.host}{endpoint}"
        encoded_body = self._build_body(body)
        req = urllib.request.Request(url, headers=self._build_headers(header), data=encoded_body, method="POST")
        return self._handle_response(req)

    def delete(self, endpoint: str, header: Optional[dict] = None,
               body: Optional[dict] = None) -> RestServiceResponseBody:
        url = self._build_url(endpoint, body)
        req = urllib.request.Request(url, headers=self._build_headers(header), method="DELETE")
        return self._handle_response(req)

    def patch(self, endpoint: str, header: Optional[dict] = None, body: Any = None) -> RestServiceResponseBody:
        url = f"{self.host}{endpoint}"
        encoded_body = self._build_body(body)
        req = urllib.request.Request(url, headers=self._build_headers(header), data=encoded_body, method="PATCH")
        return self._handle_response(req)

    def put(self, endpoint: str, header: Optional[dict] = None, body: Any = None) -> RestServiceResponseBody:
        url = f"{self.host}{endpoint}"
        encoded_body = self._build_body(body)
        req = urllib.request.Request(url, headers=self._build_headers(header), data=encoded_body, method="PUT")
        return self._handle_response(req)

    # --- Private helpers ---

    def _build_headers(self, header: Optional[dict] = None) -> dict:
        defaults = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        if header:
            defaults.update(header)
        return defaults

    def _build_body(self, body: Any) -> Optional[bytes]:
        if body is None:
            return None
        if isinstance(body, (bytes, bytearray)):
            return body
        if isinstance(body, str):
            return body.encode("utf-8")
        # Plain dict — serialize to JSON
        return json.dumps(body).encode("utf-8")

    def _build_url(self, endpoint: str, body: Optional[Any] = None) -> str:
        url = f"{self.host}{endpoint}"
        if body and isinstance(body, dict):
            params = {k: str(v) for k, v in body.items() if v is not None and not isinstance(v, dict)}
            if params:
                url += "?" + urllib.parse.urlencode(params)
        return url

    def _handle_response(self, req: urllib.request.Request) -> RestServiceResponseBody:
        try:
            with urllib.request.urlopen(req) as response:
                content_type = response.headers.get("Content-Type", "")
                raw = response.read()
                if "application/json" in content_type:
                    return json.loads(raw)
                return {"data": raw.decode("utf-8")}
        except urllib.error.HTTPError as e:
            raise Exception(f"HTTP error: {e.code} {e.reason}")
