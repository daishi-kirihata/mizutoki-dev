# -*- coding:utf-8 -*-
from sklearn import datasets
from sklearn import preprocessing
from sklearn import linear_model
from matplotlib import pyplot
import numpy

class beginnerAI01():
    def __init__(self):
        self.housePrices = datasets.load_boston()
        self.digits = datasets.load_digits()

    def __del__(self):
        self.housePrices = None
        self.digits = None

    def GetData(self):
        return self.housePrices.data

    def GetTarget(self):
        return self.housePrices.target

    def GetImages(self):
        return self.digits.images

class beginnerAI02():
    def __init__(self):
        self.inputData = numpy.array([
            [5.1, -2.9, 3.3],
            [-1.2, 7.8, -6.1],
            [3.9, 0.4, 2.1],
            [7.3, -9.9, -4.5]
        ])
        self.inputLabels = [
            'red',
            'black',
            'red',
            'green',
            'black',
            'yellow',
            'white'
        ]
        self.encoder = preprocessing.LabelEncoder()
        self.encoder.fit(self.inputLabels)
        self.classifier = linear_model.LogisticRegression(solver='liblinear', C=1, multi_class='auto')
        self.meshStepSize = 0.01

    def __del__(self):
        self.inputData = None
        self.classifier = None
        self.meshStepSize = None

    def ShowRawData(self):
        return self.inputData

    def BinarizeData(self, threshold=2.1):
        return preprocessing.Binarizer(threshold=threshold).transform(self.inputData) 

    def MeanData(self):
        return self.inputData.mean(axis=0)

    def StdData(self):
        return self.inputData.std(axis=0)
    
    def Scaling(self):
        dataScalerMinMax = preprocessing.MinMaxScaler(feature_range=(0, 1))
        return dataScalerMinMax.fit_transform(self.inputData)
    
    def Normalize(self, norm='l1'):
        return preprocessing.normalize(self.inputData, norm=norm)

    def Transform(self, listOfLabel):
        return list(self.encoder.transform(listOfLabel))

    def InverseTransform(self, listOfIndex):
        return list(self.encoder.inverse_transform(listOfIndex))

    def Fit(self, trainX, trainY):
        self.data = trainX
        self.labels = trainY
        self.minX, self.maxX = self.data[:, 0].min() - 1.0, self.data[:, 0].max() + 1.0
        self.minY, self.maxY = self.data[:, 1].min() - 1.0, self.data[:, 1].max() + 1.0
        self.classifier.fit(trainX, trainY)

    def visualizeClassifier(self, title=''):
        xVals, yVals = numpy.meshgrid(
            numpy.arange(self.minX, self.maxX, self.meshStepSize),
            numpy.arange(self.minY, self.maxY, self.meshStepSize)
        )
        output = self.classifier.predict(numpy.c_[xVals.ravel(), yVals.ravel()])
        output = output.reshape(xVals.shape)
        pyplot.figure()
        pyplot.title(title)
        pyplot.pcolormesh(
            xVals,
            yVals,
            output,
            cmap=pyplot.cm.gray
        )
        pyplot.scatter(self.data[:, 0], self.data[:, 1], c=self.labels, s=100, edgecolors='black', linewidth=1, cmap=pyplot.cm.Paired)
        pyplot.xlim(xVals.min(), xVals.max())
        pyplot.ylim(yVals.min(), yVals.max())
        pyplot.xticks((numpy.arange(int(self.minX), int(self.maxX), 1.0)))
        pyplot.yticks((numpy.arange(int(self.minY), int(self.maxY), 1.0)))
        pyplot.show()

class beginnerAI03():
    def __init__(self):
        pass

    def __del__(self):
        pass

class beginnerAI04():
    def __init__(self):
        pass

    def __del__(self):
        pass

class beginnerAI05():
    def __init__(self):
        pass

    def __del__(self):
        pass

class beginnerAI06():
    def __init__(self):
        pass

    def __del__(self):
        pass

class beginnerAI07():
    def __init__(self):
        pass

    def __del__(self):
        pass

class beginnerAI08():
    def __init__(self):
        pass

    def __del__(self):
        pass

class beginnerAI09():
    def __init__(self):
        pass

    def __del__(self):
        pass

class beginnerAI10():
    def __init__(self):
        pass

    def __del__(self):
        pass

class beginnerAI11():
    def __init__(self):
        pass

    def __del__(self):
        pass

class beginnerAI12():
    def __init__(self):
        pass

    def __del__(self):
        pass

class beginnerAI13():
    def __init__(self):
        pass

    def __del__(self):
        pass

class beginnerAI14():
    def __init__(self):
        pass

    def __del__(self):
        pass

