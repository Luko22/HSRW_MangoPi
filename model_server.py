from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import numpy as np
from sklearn.preprocessing import StandardScaler
from keras.models import load_model

model=load_model('Model/NNModel.h5') #parameters

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        sensor_data = json.loads(post_data.decode('utf-8'))

        # Process sensor data
        print("Received sensor data:", sensor_data)
        self._set_headers()

        risk_severity = None

        if sensor_data:
            risk_severity=risk_model.send_data_to_model(sensor_data)

        print("calculatedd risk_severity")

        if risk_severity:
        # Include the sent data in the response
            print(f"Sending risk severity ={risk_severity}")
            response_message = {'message': {risk_severity}}
        else:
            print("Error, could not send risk severity")
            response_message = {'message': f'Error Risk severity was not calculated'}
        response = json.dumps(response_message)
        self.wfile.write(response.encode('utf-8'))


class risk_model():

    @staticmethod
    def send_data_to_model(sensor_data):
        risk_model.run_risk_model(sensor_data['Temperature'],sensor_data['Humidity'],sensor_data['Light'],sensor_data['Longitude'],sensor_data['Latitude'],sensor_data['Day'], sensor_data['Month'],sensor_data['Hour'])
    @staticmethod
    def run_risk_model(temp, hum, light, lon, lat, day, month, hour):
        quadrant = risk_model.calculate_quadrant(rtv_lat=lat,rtv_lon=lon)
        rc = risk_model.calculate_road_condition(temp=temp,hum=hum)
        model_risk = risk_model.calc_model_risk(month=month, hour=hour, day=day, light=light, rc=rc,quadrant=quadrant)
        return model_risk

    @staticmethod
    def calculate_quadrant(rtv_lat,rtv_lon): #script from asssigner to convert coordinates to quadrant
        berlin_latitude_range = (52.336724, 52.675287)
        berlin_long_range = (13.090365, 13.756247)
        multiplication_factor = 1000000
        lat_range = (int(berlin_latitude_range[0] * multiplication_factor), int(berlin_latitude_range[1] * multiplication_factor))
        lon_range = (int(berlin_long_range[0] * multiplication_factor), int(berlin_long_range[1] * multiplication_factor))
        step = 100
        lat_range=np.linspace(lat_range[0],lat_range[1],step)
        lat_range=lat_range.flatten()
        lon_range=np.linspace(lon_range[0],lon_range[1],step)
        lat_delta = lat_range[1]-lat_range[0]
        lon_delta = lon_range[1]-lon_range[0]

        quadrant_code = 0
        for lon in lon_range:
            for lat in lat_range:
                quadrant_code=quadrant_code+1
                if lon <= rtv_lon*multiplication_factor <= lon + lon_delta and lat <= rtv_lat*multiplication_factor <= lat + lat_delta:
                    return quadrant_code
        return None

    @staticmethod
    def calculate_road_condition(temp=None, hum=None): #use nicologic to convert temp and humidity to road condition (0:dry,1,wet,2:icy)
            if temp < 0:
                return 2
            elif temp < 10 and hum > 70:
                return 2
            elif temp < 10:
                return 1
            elif temp >= 30 and hum < 30:
                return 0
            elif temp >= 30:
                return 1
            else:
                return 0

    @staticmethod
    def calc_model_risk(month=None, hour=None, day=None, light=None, rc=None, quadrant=None): #run model with follow parameters: month, hour, day, light condition, road condition, quadrant,
        print("running model")
        rtv_values_raw = np.array([[month,hour,day,light,rc,quadrant]]) #month, hour, day, light condition, road condition, quadrant_rank,
        rtv_vales_scaled = StandardScaler().transform(rtv_values_raw)
        model_severity=model.predict(rtv_vales_scaled)
        print(model_severity[0][0])
        return model_severity[0][0]


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

