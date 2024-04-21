from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    stored_sensor_data = []

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        sensor_data = json.loads(post_data.decode('utf-8'))

        # Process sensor data
        print("Received sensor data:", sensor_data)
        self.stored_sensor_data.append(sensor_data)

        self._set_headers()
        
        # Include the sent data in the response
        response_message = {'message': f'Data received successfully {sensor_data}'}
        response = json.dumps(response_message)
        
        self.wfile.write(response.encode('utf-8'))

    def do_GET(self):
        self._set_headers()
        response = json.dumps(self.stored_sensor_data)
        self.wfile.write(response.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()