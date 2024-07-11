from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
df = pd.read_csv("data/data2.csv")
x = df.drop("condition", axis=1)
y = df["condition"]
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42)
rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(x_train, y_train)


def prediction(x):
    condition_to_index = {'Clear': 0, 'Sunny': 1, 'Patchy rain possible': 2, 'Light rain shower': 3, 'Partly cloudy': 4, 'Cloudy': 5, 'Moderate rain': 6, 'Moderate or heavy rain shower': 7, 'Patchy light rain': 8, 'Patchy light drizzle': 9, 'Mist': 10, 'Overcast': 11, 'Thundery outbreaks possible': 12,
                          'Moderate or heavy snow with thunder': 13, 'Light snow showers': 14, 'Patchy light snow with thunder': 15, 'Light drizzle': 16, 'Light rain': 17, 'Fog': 18, 'Moderate rain at times': 19, 'Heavy rain': 20, 'Patchy light rain with thunder': 21, 'Torrential rain shower': 22}

    def get_key_by_value(dictionary, value):
        for key, val in dictionary.items():
            if val == value:
                return key
        return None
    x = np.array(x)
    x = x.reshape(1, 9)
    y_pred = rfc.predict(x)
    key = get_key_by_value(condition_to_index, y_pred)
    return key, y_pred
