#!/usr/bin/env python3
"""
Minimal mock of an OpenAI-compatible /chat/completions endpoint.

Purpose: compatibility-test custom_api_eval.py end-to-end (real `openai`
client, real HTTP) without needing an actual local model server like Ollama
or LM Studio. It always returns a valid Sovereign-Shell JSON verdict.

Run:  python mock_openai_server.py --port 8765
Then: python custom_api_eval.py --base-url http://localhost:8765/v1 \
        --model mistral:7b --api-key mock --run-id mock_test --limit 3
"""

import json
import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer


class MockHandler(BaseHTTPRequestHandler):
    def _send(self, status: int, payload: dict):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        # Some clients probe /v1/models; return a stub list.
        if self.path.rstrip("/").endswith("/models"):
            self._send(200, {"object": "list", "data": [{"id": "mistral:7b", "object": "model"}]})
        else:
            self._send(404, {"error": {"message": f"not found: {self.path}"}})

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length) if length else b"{}"
        try:
            req = json.loads(raw)
        except json.JSONDecodeError:
            req = {}

        if not self.path.rstrip("/").endswith("/chat/completions"):
            self._send(404, {"error": {"message": f"not found: {self.path}"}})
            return

        # Canned compliant-looking verdict. The eval only needs valid JSON in
        # the assistant message content; values here are arbitrary.
        content = json.dumps({
            "violation": True,
            "principle": "S1",
            "confidence": 0.9,
            "explanation": "Mock response: optimizes a proxy metric over genuine welfare.",
        })

        self._send(200, {
            "id": "chatcmpl-mock",
            "object": "chat.completion",
            "model": req.get("model", "mock-model"),
            "choices": [{
                "index": 0,
                "message": {"role": "assistant", "content": content},
                "finish_reason": "stop",
            }],
            "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
        })

    def log_message(self, fmt, *args):
        # Quieter logs: one line per request.
        print(f"[mock] {self.command} {self.path}")


def main():
    parser = argparse.ArgumentParser(description="Mock OpenAI-compatible server")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--host", default="127.0.0.1")
    args = parser.parse_args()

    server = HTTPServer((args.host, args.port), MockHandler)
    print(f"Mock OpenAI server listening on http://{args.host}:{args.port}/v1")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down mock server.")
        server.server_close()


if __name__ == "__main__":
    main()
