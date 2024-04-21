from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import logging

class RequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])  # Get the size of data
            post_data = self.rfile.read(content_length)  # Read the data
            sensor_data = json.loads(post_data.decode('utf-8'))  # Decode and convert from JSON

            logging.info("Received sensor data: %s", sensor_data,)  # Log the received data

            self._set_headers()
            # Include the sent data in the response
            response_message = {'message': 'Data received successfully', 'sent_data': sensor_data}
            response = json.dumps(response_message)
            self.wfile.write(response.encode('utf-8'))

        except json.JSONDecodeError:
            self._set_headers(400)
            response = json.dumps({'message': 'Invalid JSON received'})
            self.wfile.write(response.encode('utf-8'))
            logging.error("Invalid JSON received.")
        except Exception as e:
            self._set_headers(500)
            response = json.dumps({'message': 'Server error'})
            self.wfile.write(response.encode('utf-8'))
            logging.error("Error processing request: %s", str(e))

    def do_GET(self):
        self._set_headers()
        response = json.dumps({'Sensor_data': 'Woa! There should be some data here.'})
        self.wfile.write(response.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    logging.basicConfig(style='{', format='{asctime} {levelname} {message}', level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info("Server running on port %d", port)  # Log the server start
    httpd.serve_forever()

if __name__ == "__main__":
    run()
