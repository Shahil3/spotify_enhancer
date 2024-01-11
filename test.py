import http.server
import socketserver
from main import exchange_code_for_tokens;

# Define the port on which your local server will run
port = 3000  # You can choose any available port

# Define the callback route (e.g., "/callback")
callback_route = "/callback"

# Create a simple request handler to handle the callback
class CallbackHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith(callback_route):
            # Extract the authorization code from the query parameters
            authorization_code = self.path.split("=")[1]
            # Call the function to exchange the code for tokens
            exchange_code_for_tokens(authorization_code)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Authorization successful. You can close this window.")
        else:
            super().do_GET()

try:
    # Start the local server
    with socketserver.TCPServer(("localhost", port), CallbackHandler) as httpd:
        print(f"Serving on port {port}")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer terminated by user.")