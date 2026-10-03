"""Injected by the deploy bot. Do not edit.

Render web services must listen on $PORT. Most Telegram bots use long polling and
open no port, so this wrapper serves a tiny health endpoint (GET/HEAD /) in a
background thread -- which is also what UptimeRobot pings -- and then runs the
user's entry point unchanged.
"""
import os
import runpy
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class _Health(BaseHTTPRequestHandler):
    def _respond(self, body: bytes) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def do_GET(self):
        self._respond(b"OK")

    def do_HEAD(self):
        self._respond(b"OK")

    def log_message(self, *args):  # keep logs clean
        pass


def _serve() -> None:
    port = int(os.environ.get("PORT", "10000"))
    try:
        ThreadingHTTPServer(("0.0.0.0", port), _Health).serve_forever()
    except OSError as exc:  # e.g. the user's bot already binds $PORT itself
        print(f"[wrapper] health server not started: {exc}", file=sys.stderr)


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("usage: python _render_wrapper.py <entry_point.py>")
    entry = sys.argv[1]
    threading.Thread(target=_serve, daemon=True).start()
    sys.path.insert(0, os.getcwd())
    sys.argv = [entry]
    runpy.run_path(entry, run_name="__main__")


if __name__ == "__main__":
    main()
