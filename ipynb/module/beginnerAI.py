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

class LogisticModel():
    def __str__(self):
        return self.__class__.__name__

    def __init__(self, mesh_step_size = 0.01, solver='liblinear', C=1, multi_class='auto'):
        self.__reset_cache
        self.__mesh_step_size = mesh_step_size
        self.__solver = solver
        self.__C = C
        self.__multi_class = multi_class
        self.__classifier = linear_model.LogisticRegression(solver=self.__solver, C=self.__C, multi_class=self.__multi_class)

    def __del__(self):
        self.__reset_cache()
        self.__mesh_step_size = None
        self.__solver = None
        self.__C = None
        self.__multi_class = None
        self.__classifier = None

    @property
    def mesh_step_size(self):
        return self.__mesh_step_size

    @mesh_step_size.setter
    def mesh_step_size(self, mesh_step_size):
        self.__mesh_step_size = mesh_step_size

    @property
    def solver(self):
        return self.__solver

    @solver.setter
    def solver(self, solver):
        self.__solver = solver
        self.__classifier = linear_model.LogisticRegression(solver=self.__solver, C=self.__C, multi_class=self.__multi_class)

    @property
    def C(self):
        return self.__C

    @C.setter
    def C(self, C):
        self.__C = C
        self.__classifier = linear_model.LogisticRegression(solver=self.__solver, C=self.__C, multi_class=self.__multi_class)

    @property
    def multi_class(self):
        return self.__multi_class

    @multi_class.setter
    def multi_class(self, multi_class):
        self.__multi_class = multi_class
        self.__classifier = linear_model.LogisticRegression(solver=self.__solver, C=self.__C, multi_class=self.__multi_class)

    def fit(self, X, y):
        self.__trainX = X
        self.__trainY = y
        self.__minX = X[:, 0].min() - 1.0
        self.__maxX = X[:, 0].max() + 1.0
        self.__minY = X[:, 1].min() - 1.0
        self.__maxY = X[:, 1].max() + 1.0
        self.__classifier.fit(X, y)

    def visualize_classifier(self, title=''):
        (xVals, yVals) = numpy.meshgrid(
            numpy.arange(self.__minX, self.__maxX, self.__mesh_step_size),
            numpy.arange(self.__minY, self.__maxY, self.__mesh_step_size)
        )
        output = self.__classifier.predict(numpy.c_[xVals.ravel(), yVals.ravel()])
        output = output.reshape(xVals.shape)

        pyplot.figure()
        pyplot.title(title)
        
        pyplot.pcolormesh(xVals, yVals, output, cmap=pyplot.cm.gray)
        pyplot.scatter(self.__trainX[:, 0], self.__trainX[:, 1], c=self.__trainY, s=75, edgecolors='black', linewidth=1, cmap=pyplot.cm.Paired)
        
        pyplot.xlim(xVals.min(), xVals.max())
        pyplot.ylim(yVals.min(), yVals.max())
        
        pyplot.xticks((numpy.arange(int(self.__minX), int(self.__maxX), 1.0)))
        pyplot.yticks((numpy.arange(int(self.__minY), int(self.__maxY), 1.0)))

        pyplot.show()

    def __reset_cache(self):
        self.__trainX = None
        self.__trainY = None
        self.__minX = None
        self.__maxX = None
        self.__minY = None
        self.__maxY = None

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
    def __str__(self):
        return self.__class__.__name__

    def __init__(self):
        self.object = beginnerAI04()
        self.object = beginnerAI05()

    def __del__(self):
        self.object = None

class beginnerAI04():
    def __str__(self):
        return self.__class__.__name__

    def __init__(self):
        print('start\t{0}'.format(self.__class__.__name__))

    def __del__(self):
        print('end\t{0}'.format(self.__class__.__name__))

class beginnerAI05():
    def __str__(self):
        return self.__class__.__name__

    def __init__(self):
        print('start\t{0}'.format(self.__class__.__name__))

    def __del__(self):
        print('end\t{0}'.format(self.__class__.__name__))

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

