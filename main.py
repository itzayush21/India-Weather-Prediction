from flask import Flask, render_template, request
from algo import prediction

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    state_to_index = {
        'Andhra Pradesh': 1, 'Arunachal Pradesh': 2, 'Assam': 3, 'Bihar': 4,
        'Chhattisgarh': 5, 'Goa': 6, 'Gujarat': 7, 'Haryana': 8, 'Himachal Pradesh': 9,
        'Jharkhand': 10, 'Karnataka': 11, 'Kerala': 12, 'Madhya Pradesh': 13,
        'Maharashtra': 14, 'Manipur': 15, 'Meghalaya': 16, 'Mizoram': 17, 'Nagaland': 18,
        'Odisha': 19, 'Punjab': 20, 'Rajasthan': 21, 'Sikkim': 22, 'Tamil Nadu': 23,
        'Telangana': 24, 'Tripura': 25, 'Uttar Pradesh': 26, 'Uttarakhand': 27, 'West Bengal': 28}
    if request.method == 'POST':
        state = request.form['state']
        temp_c = request.form['temp_c']
        wind_kph = request.form['wind_kph']
        pressure_mb = request.form['pressure_mb']
        precip_mm = request.form['precip_mm']
        humidity = request.form['humidity']
        cloud = request.form['cloud']
        feelslike_c = request.form['feelslike_c']
        vis_km = request.form['vis_km']
        s = state_to_index[state]
        data = {
            'temp_c': [temp_c],
            'wind_kph': [wind_kph],
            'pressure_mb': [pressure_mb],
            'precip_mm': [precip_mm],
            'humidity': [humidity],
            'cloud': [cloud],
            'feelslike_c': [feelslike_c],
            'vis_km': [vis_km]
        }
        w, y = prediction([temp_c, wind_kph, pressure_mb,
                          precip_mm, humidity, cloud, feelslike_c, vis_km, s])
        return render_template('index.html', w=w, d=data)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
