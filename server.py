# -*- coding: utf-8 -*-
import http.server
import json
import urllib.parse
import os
import time
import socketserver

ROOMS = {}

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def send_json(self, data):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))

    def do_OPTIONS(self):
        self.send_json({})

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        params = urllib.parse.parse_qs(parsed.query)

        if path == '/api/msgs':
            room = params.get('room', ['default'])[0]
            since = int(params.get('since', [0])[0])
            msgs = ROOMS.get(room, [])
            new_msgs = msgs[since:]
            self.send_json({'msgs': new_msgs, 'total': len(msgs)})
            return

        if path == '/api/admin':
            data = {}
            for room, msgs in ROOMS.items():
                data[room] = {'msgs': msgs, 'total': len(msgs)}
            self.send_json(data)
            return

        if path == '/api/clear':
            room = params.get('room', ['default'])[0]
            ROOMS[room] = []
            self.send_json({'ok': True})
            return

        if path == '/api/health':
            self.send_json({'status': 'ok', 'rooms': len(ROOMS)})
            return

        # Serve static files
        file_path = os.path.join(DIR, path.lstrip('/') or 'mini.html')
        if os.path.isfile(file_path):
            self.send_response(200)
            ct = 'text/html'
            if file_path.endswith('.css'): ct = 'text/css'
            elif file_path.endswith('.js'): ct = 'application/javascript'
            self.send_header('Content-Type', ct + '; charset=utf-8')
            self.end_headers()
            with open(file_path, 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'<h1>Mini Mateuzinho API</h1><p>Servidor rodando!</p>')

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == '/api/send':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            data = json.loads(body)
            room = data.get('room', 'default')
            msg = {
                'de': data['de'],
                'msg': data['msg'],
                'h': time.strftime('%H:%M:%S')
            }
            ROOMS.setdefault(room, []).append(msg)
            self.send_json({'ok': True, 'total': len(ROOMS[room])})
            return

        self.send_response(404)
        self.end_headers()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    os.chdir(DIR)
    server = socketserver.TCPServer(('0.0.0.0', port), Handler)
    server.allow_reuse_address = True
    print(f'✅ SERVIDOR MINI MATEUZINHO RODANDO NA PORTA {port}')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        print('\nServidor encerrado.')
