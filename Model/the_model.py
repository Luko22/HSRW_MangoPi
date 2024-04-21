import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow import keras
from keras.callbacks import EarlyStopping


df=pd.read_csv("accidents_21_19.csv")
#defien the Y :
def calculate_severity(row):
    severity = 0
    
    # AccidentCategory
    if row['AccidentCategory'] == 1:
        severity += 10
    elif row['AccidentCategory'] == 2:
        severity += 5
    else:
        severity += 1
    
    # AccidentType and AccidentTypeDetail
    if row['AccidentType'] in [4, 6]:  # Collision with oncoming vehicle or pedestrian
        severity += 5
    elif row['AccidentTypeDetail'] in [1, 2, 3]:  # Driving, turning, or turning/crossing accident
        severity += 3
    else:
        severity += 1

    # Involving parameters
    if row['InvolvingPedestrian'] == 1:
        severity += 5
    if row['InvolvingMotorcycle'] == 1:
        severity += 4
    if row['InvolvingBike'] == 1:
        severity += 3
    if row['InvolvingCar'] == 1:
        severity += 2
    if row['InvolvingHGV'] == 1:
        severity += 2
    
    return severity


df['Severity'] = df.apply(calculate_severity, axis=1)


X = df[['AccidentMonth', 'AccidentHour', 'DayOfWeek', 'LightingCondition','RoadCondition' ,'quadrant']]
y = df['Severity']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)






# Define your neural network model
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    keras.layers.Dense(32, activation='relu', kernel_regularizer=keras.regularizers.l2(0.01)),
    keras.layers.Dense(16, activation='relu', kernel_regularizer=keras.regularizers.l2(0.01)),
    keras.layers.Dense(1)  # Output layer for regression
])

# Compile the model
model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.001),
              loss='mean_squared_error',
              metrics=['mean_absolute_error'])

# Define early stopping
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Define batch size and number of epochs
batch_size = 32
epochs = 100

# Train the model with early stopping
history = model.fit(X_train_scaled, y_train, epochs=epochs, batch_size=batch_size,
                    validation_split=0.2, callbacks=[early_stopping])

# Evaluate on test data
test_loss, test_mae = model.evaluate(X_test_scaled, y_test)
print('Test MAE:', test_mae)

# Save the model
model.save('the_model.h5')
