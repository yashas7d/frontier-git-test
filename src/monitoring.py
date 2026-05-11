import time
from datetime import datetime, timezone


def timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def measure(fn):
    def wrapper(*args, **kwargs):
        start = time.monotonic()
        result = fn(*args, **kwargs)
        elapsed_ms = int((time.monotonic() - start) * 1000)
        print(f"[{timestamp()}] {fn.__name__} completed in {elapsed_ms}ms")
        return result
    return wrapper


class EventLogger:
    def __init__(self, service: str):
        self.service = service
        self._events: list[dict] = []

    def log(self, event: str, metadata: dict | None = None) -> None:
        self._events.append({
            "service": self.service,
            "event": event,
            "ts": timestamp(),
            "metadata": metadata or {},
        })

    def flush(self) -> list[dict]:
        events, self._events = self._events, []
        return events
