#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from . import workspace_log


class DashboardHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Read PROJECT_STRUCTURE.md and SUBMODULE_DASHBOARD.md
            try:
                with open('SUBMODULE_DASHBOARD.md', 'r') as f:
                    sub_content = f.read()
                with open('PROJECT_STRUCTURE.md', 'r') as f:
                    struct_content = f.read()
            except Exception:
                sub_content = "Run 'workspace docs' to generate dashboard."
                struct_content = "Run 'workspace docs' to generate structure."

            html = f"""
            <html>
            <head>
                <title>MilkDrop3 Workspace Dashboard</title>
                <style>
                    body {{ font-family: sans-serif; padding: 20px; }}
                    pre {{
                        background: #f4f4f4;
                        padding: 15px;
                        overflow: auto;
                    }}
                </style>
            </head>
            <body>
                <h1>MilkDrop3 Omni-Workspace Monitor</h1>
                <h2>Submodule Status</h2>
                <pre>{sub_content}</pre>
                <h2>Project Structure</h2>
                <pre>{struct_content}</pre>
            </body>
            </html>
            """
            self.wfile.write(html.encode())
        else:
            self.send_error(404)


def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, DashboardHandler)
    workspace_log.info(f"Web dashboard started at http://localhost:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        workspace_log.info("Web dashboard stopped.")
