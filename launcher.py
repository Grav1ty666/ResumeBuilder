import http.server
import socketserver
import webbrowser
import os
import base64
import threading
import pystray
from PIL import Image, ImageDraw
from assets_data import ASSETS

TYPES = {
    '.html': 'text/html; charset=utf-8',
    '.css': 'text/css; charset=utf-8',
    '.js': 'text/javascript; charset=utf-8',
    '.json': 'application/json; charset=utf-8',
    '.woff': 'font/woff',
    '.woff2': 'font/woff2',
    '.ttf': 'font/ttf',
    '.otf': 'font/otf',
    '.ttc': 'font/collection',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.svg': 'image/svg+xml',
}

PORT = 0


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        p = self.path.split('?', 1)[0]
        key = 'index.html' if p in ('', '/') else p.lstrip('/').replace('\\', '/')
        data = ASSETS.get(key)
        if data is None:
            self.send_error(404, 'Not found: ' + key)
            return
        ext = os.path.splitext(key)[1].lower()
        body = base64.b64decode(data)
        self.send_response(200)
        self.send_header('Content-Type', TYPES.get(ext, 'application/octet-stream'))
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


def make_icon():
    img = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([6, 6, 58, 58], radius=14, fill=(37, 99, 235, 255))
    return img


def open_browser():
    webbrowser.open('http://127.0.0.1:%d/' % PORT)


def main():
    global PORT
    PORT = int(os.environ.get('RB_PORT') or 0)
    srv = Server(('127.0.0.1', PORT), Handler)
    PORT = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    try:
        webbrowser.open('http://127.0.0.1:%d/' % PORT)
    except Exception:
        pass
    menu = pystray.Menu(
        pystray.MenuItem('打开简历生成器', lambda icon: open_browser()),
        pystray.MenuItem('退出', lambda icon: (srv.shutdown(), icon.stop())),
    )
    icon = pystray.Icon('ResumeBuilder', icon=make_icon(), title='ResumeBuilder', menu=menu)
    icon.run()


if __name__ == '__main__':
    main()
