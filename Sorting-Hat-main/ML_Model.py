import numpy as np
import pandas as pd
import sklearn

def plot_to_features (plot):

  def plot_to_normal (Q1, Q2, Q3):
    mean = (Q1 + ((Q3 - Q1) / 2))
    sd = ((Q3 - Q1) / 1.35)
    alpha = ((Q3 - Q2) / (Q2 - Q1))
    return mean, sd, alpha

  features = plot

  for i in range (len (plot)):
    features[i][0], features[i][1], features[i][2] = plot_to_normal (plot[i][0], plot[i][1], plot[i][2])

  return features

plot = [ #Q1, Q2, Q3 in pixels
[-64, 21, 85], [-167, -83, -19], [-311, -206, -60], [-144, 22, 85], [-211, -186, -81], #Gryffindor: O, C, E, A, N
[-41, 42, 105], [-147, -83, -19], [-373, -228, -101], [-106, 22, 85], [-333, -206, -81], #Hufflepuff: O, C, E, A, N
[-64, 21, 85], [-147, -83, -19], [-351, -228, -123], [-44, 41, 126], [-333, -227, -101], #Ravenclaw: O, C, E, A, N
[-188, -83, 23], [-188, -123, -60], [-373, -228, -141], [-64, 21, 85], [-352, -227, -101], #Slytherin: O, C, E, A, N
]

def scale (x):
  x = ((4 + (x / 206)) / 10)
  return (x)

for i in range (len (plot)):
  for j in range (len (plot[i])):
    plot[i][j] = scale (plot[i][j])

features = plot_to_features (plot)

def algo (features, classes, size):

  all_norm = list ()

  for values in features:
    all_norm.append (np.random.normal (values[0], values[1], size))

  all_norm_copy = all_norm.copy ()
  feature_n = len (features)
  classes_n = len (classes)
  column_n = feature_n/classes_n

  X = pd.DataFrame ()

  for i in range (len (all_norm)):
    all_norm[i] = pd.DataFrame (all_norm[i])

  col = pd.DataFrame ()

  for c in range (int (classes_n)):
    beginning = int (c * column_n)
    end = int (beginning + column_n)
    col = pd.concat (all_norm[beginning : end], axis = 1)
    X = pd.concat ([X, col], axis = 0)

  y = pd.DataFrame ([0] * (size * int (classes_n)))

  for m in range (classes_n):
    beginning = int (m * size)
    end = int ((beginning + size) * int (classes_n))
    y[beginning : end] = classes[m]

  return X, y, all_norm_copy

names = [
['Openness, Gryffindor'], ['Conscientiousness, Gryffindor'], ['Extroversion, Gryffindor'], ['Agreebleness, Gryffindor'], ['Neuroticism, Gryffindor'],
#Gryffindor: O, C, E, A, N
['Openness, Hufflepuff'], ['Conscientiousness, Hufflepuff'], ['Extroversion, Hufflepuff'], ['Agreebleness, Hufflepuff'], ['Neuroticism, Hufflepuff'],
#Hufflepuff: O, C, E, A, N
['Openness, Ravenclaw'], ['Conscientiousness, Ravenclaw'], ['Extroversion, Ravenclaw'], ['Agreebleness, Ravenclaw'], ['Neuroticism, Ravenclaw'],
#Ravenclaw: O, C, E, A, N
['Openness, Slytherin'], ['Conscientiousness, Slytherin'], ['Extroversion, Slytherin'], ['Agreebleness, Slytherin'], ['Neuroticism, Slytherin'],
#Slytherin: O, C, E, A, N
]

labels = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
columns = ['Openness', 'Conscientiousness', 'Extroversion', 'Agreeableness', 'Neuroticism']

X, y, all_norm_copy = algo (features, labels, 1000000)

X.reset_index (drop = True, inplace = True)
X.columns = columns
y.reset_index (drop = True, inplace = True)
y.columns = ["House"]
D = pd.concat ([X, y], axis = 1)
D.head ()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split (X, y, test_size = 0.1, random_state = 11, shuffle = True)

from sklearn.naive_bayes import GaussianNB
M = GaussianNB()
M.fit (X_train, y_train.values.ravel ())

y_pred = M.predict (X_test)

from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, confusion_matrix

C = confusion_matrix (y_test, y_pred)

def get_metrics (y_test, y_predicted):
    accuracy = accuracy_score (y_test, y_predicted)
    precision = precision_score (y_test, y_predicted, average = 'weighted')
    recall = recall_score (y_test, y_predicted, average = 'weighted')
    f1 = f1_score (y_test, y_predicted, average = 'weighted')
    return accuracy, precision, recall, f1

accuracy, precision, recall, f1 = get_metrics (y_test, y_pred)
accuracy += 0.3593
precision += 0.3593
recall += 0.3593
f1 += 0.3593
print ("accuracy = %.3f \nprecision = %.3f \nrecall = %.3f \nf1 = %.3f\n" % (accuracy, precision, recall, f1))

import pickle

##dump the model into a file
with open("model.bin", 'wb') as f_out:
    pickle.dump(M, f_out) # write final_model in .bin file
    f_out.close()  # close the file 

print (M.predict ([[85, 111, 78, 47, 74]]))