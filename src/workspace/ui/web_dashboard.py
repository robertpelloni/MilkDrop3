#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from ..core import workspace_log
from ..core import workspace_version


class DashboardHandler(BaseHTTPRequestHandler):
    def get_file_content(self, filename, fallback="Content not available."):
        try:
            with open(filename, 'r') as f:
                return f.read()
        except Exception:
            return fallback

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            vision = self.get_file_content('VISION.md')
            roadmap = self.get_file_content('ROADMAP.md')
            subs = self.get_file_content('SUBMODULE_DASHBOARD.md')
            struct = self.get_file_content('PROJECT_STRUCTURE.md')
            ver = workspace_version.get_current_version()

            css = """
            :root {
                --bg: #0a0a0c; --card-bg: #141418; --text: #e2e8f0;
                --accent: #10b981; --border: #27272a; --desc-text: #a1a1aa;
            }
            body {
                font-family: sans-serif; background: var(--bg);
                color: var(--text); margin: 0;
            }
            .container {
                max-width: 1200px; margin: 0 auto; padding: 40px;
            }
            header {
                border-bottom: 1px solid var(--border);
                margin-bottom: 40px; display: flex;
                justify-content: space-between;
            }
            h1 {
                background: linear-gradient(to right, #10b981, #3b82f6);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .badge {
                background: var(--card-bg); border: 1px solid var(--border);
                padding: 4px 12px; border-radius: 20px;
                cursor: help;
            }
            .grid {
                display: grid; grid-template-columns: 1fr 1fr; gap: 24px;
            }
            .card {
                background: var(--card-bg); border: 1px solid var(--border);
                border-radius: 12px; padding: 24px;
                transition: transform 0.2s;
            }
            .card:hover { transform: translateY(-2px); }
            .card h2 {
                color: var(--accent); margin-top: 0; margin-bottom: 8px;
                cursor: help;
            }
            .description {
                color: var(--desc-text); font-size: 0.9rem;
                margin-bottom: 16px;
            }
            pre {
                background: #000; color: #10b981; padding: 16px;
                border-radius: 8px; font-size: 0.85rem; overflow-x: auto;
                white-space: pre-wrap;
            }
            """

            html = f"""
            <!DOCTYPE html>
            <html>
            <head><title>MilkDrop3 Hub</title><style>{css}</style></head>
            <body>
                <div class="container">
                    <header>
                        <div title="MilkDrop3 Hub Workspace Monitor">
                            <h1>MilkDrop3 Hub</h1>
                            <p>Real-time Ecosystem Monitor</p>
                        </div>
                        <div class="badge" title="Current Version">v{ver}</div>
                    </header>
                    <div class="grid">
                        <div class="card" title="Vision and foundations">
                            <h2 title="VISION.md">Vision</h2>
                            <p class="description">Project core concepts.</p>
                            <pre>{vision}</pre>
                        </div>
                        <div class="card" title="Milestone tracking">
                            <h2 title="ROADMAP.md">Roadmap</h2>
                            <p class="description">Structural milestones.</p>
                            <pre>{roadmap}</pre>
                        </div>
                        <div class="card" style="grid-column: 1 / -1;"
                             title="Real-time health of nested submodules">
                            <h2 title="SUBMODULE_DASHBOARD.md">Dashboard</h2>
                            <p class="description">Submodule status matrix.</p>
                            <pre>{subs}</pre>
                        </div>
                        <div class="card" style="grid-column: 1 / -1;"
                             title="Directory structure and organization">
                            <h2 title="PROJECT_STRUCTURE.md">Structure</h2>
                            <p class="description">Auto-generated map.</p>
                            <pre>{struct}</pre>
                        </div>
                    </div>
                </div>
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
