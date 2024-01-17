import numpy as np 
import pandas as pd 
import pickle
df=pd.read_csv("Dataset of Diabetes .csv")

df.head(10)
df.drop(['ID','No_Pation'],axis=1,inplace=True)
df['Gender']=df['Gender'].map({'M':0,'m':0,'F':1,'f':1})

df['Gender'] = df['Gender'].astype(int)
df['CLASS']=df['CLASS'].map({'N':0,'N ':0,'P':1,'Y':2,'Y ':2})
df['CLASS']=df['CLASS'].astype(int)
Y=df['CLASS']
X=df.drop(['CLASS'],axis=1)
Y.value_counts(normalize=True)
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
# One-hot encode the target variables
y_train_one_hot = to_categorical(y_train)
y_test_one_hot = to_categorical(y_test)

# Build the model
model = Sequential()
model.add(Dense(units=64, activation='relu', input_dim=X_train.shape[1]))
model.add(Dense(units=3, activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',  # You can use other optimizers like 'adam'
              metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train_one_hot, epochs=10, batch_size=32, validation_data=(X_test, y_test_one_hot))

# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test, y_test_one_hot)

# Print the accuracy
print(f'Test Accuracy: {accuracy:.4f}')
# Saving model to disk
pickle.dump(model, open('model.pkl','wb'))

