# -*- coding:utf-8 -*-
from module.interface.IClassifier import IClassifier
from matplotlib import pyplot
import numpy

class ClassifierBase(IClassifier):
    def __str__(self):
        return self.__class__.__name__

    def __init__(self, mesh_step_size=0.01):
        self.__reset_property()
        self.__mesh_step_size = mesh_step_size
        self.__classifier = None

    def __del__(self):
        self.__reset_property()
        self.__mesh_tep_size = None
        self.__classifier = None

    @property
    def mesh_step_size(self):
        return self.__mesh_step_size

    @mesh_step_size.setter
    def mesh_step_size(self, mesh_step_size):
        self.__mesh_step_size = mesh_step_size

    @property
    def classifier(self):
        pass

    @classifier.setter
    def classifier(self, classifier):
        self.__classifier = classifier

    def fit(self, X, y):
        self.__trainX = X
        self.__trainY = y
        self.__minX = X[:, 0].min() - 1.0
        self.__maxX = X[:, 0].max() + 1.0
        self.__minY = X[:, 1].min() - 1.0
        self.__maxY = X[:, 1].max() + 1.0
        self.__classifier.fit(X, y)

    def visualize_classifier(self, X, y, title):
        (xVals, yVals) = numpy.meshgrid(
            numpy.arange(self.__minX, self.__maxX, self.__mesh_step_size),
            numpy.arange(self.__minY, self.__maxY, self.__mesh_step_size)
        )
        output = self.__classifier.predict(numpy.c_[xVals.ravel(), yVals.ravel()])
        output = output.reshape(xVals.shape)

        pyplot.figure()
        pyplot.title(title)
        
        pyplot.pcolormesh(xVals, yVals, output, cmap=pyplot.cm.gray)
        if X is None or y is None:
            pyplot.scatter(self.__trainX[:, 0], self.__trainX[:, 1], c=self.__trainY, s=75, edgecolors='black', linewidth=1, cmap=pyplot.cm.Paired)
        else:
            pyplot.scatter(X[:, 0], X[:, 1], c=y, s=75, edgecolors='black', linewidth=1, cmap=pyplot.cm.Paired)
        
        pyplot.xlim(xVals.min(), xVals.max())
        pyplot.ylim(yVals.min(), yVals.max())
        
        pyplot.xticks((numpy.arange(int(self.__minX), int(self.__maxX), 1.0)))
        pyplot.yticks((numpy.arange(int(self.__minY), int(self.__maxY), 1.0)))

        pyplot.show()

    def __reset_property(self):
        self.__trainX = None
        self.__trainY = None
        self.__minX = None
        self.__maxX = None
        self.__minY = None
        self.__maxY = None