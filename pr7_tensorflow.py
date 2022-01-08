from tensorflow import nn
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve, auc
from matplotlib import pyplot as plt

NUM_EPOCHS = 250

def load_data(file_name):
    inputs = list()
    outputs = list()
    file = open(file_name)
    for line in file:
        a, b, c, out = list(map(int, line.split(',')))
        inputs.append([a,b,c])
        outputs.append(0 if out == 1 else 1)
    file.close()
    return np.array(inputs), np.array(outputs)

(trainX, trainY), (testX, testY) = load_data('pr7_dataset.csv'), load_data('pr7_dataset_test.csv')

model = Sequential([
    Flatten(input_dim=3),
    Dense(10, activation=nn.sigmoid),
    Dense(2, activation=nn.sigmoid)
])

model.compile(optimizer="SGD",
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy']
)
model.fit(trainX, trainY, 
          epochs=NUM_EPOCHS, 
          batch_size=10,
          verbose=1,
          validation_data=(testX, testY)
)

print("Evaluate on test data")
'''
http://bazhenov.me/blog/2012/07/21/classification-performance-evaluation.html
'''
predictions = model.predict(testX)
# сохраняем вероятности только для исхода 1
probs = predictions[:, 1]
TP, FP, FN, TN = 0,0,0,0
for i in range(len(testY)):
    true = testY[i]
    pred = np.argmax(predictions[i])
    if true == pred:
        if true == 0:
            TP += 1
        else:
            TN += 1
    else:
        if true == 1:
            FP += 1
        else:
            FN += 1    
recall = TPR = TP / (TP + FN) # True Possitive Rate
precision = TP / (TP + FP)
FRP = FP / (FP + TN) # False Possitive Rate
O1 = ((testY==0).sum() / len(testY)) / ((testY==1).sum() / len(testY)) * recall * (1/precision - 1)
O2 = 1 - recall
lr_auc = roc_auc_score(testY, probs)
print('LogisticRegression: ROC AUC=%.3f' % (lr_auc))
fpr, tpr, treshold = roc_curve(testY, probs)
roc_auc = auc(fpr, tpr)
plt.plot(fpr, tpr, color='darkorange',
         label='ROC кривая (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.show()
print(f'recall: {recall}, precision: {precision}, O1: {O1}, O2: {O2}')