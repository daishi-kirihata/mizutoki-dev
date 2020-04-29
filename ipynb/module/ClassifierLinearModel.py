# -*- coding:utf-8 -*-
from module.base.ClassifierBase import ClassifierBase
from sklearn import linear_model

class ClassifierLinearModel(ClassifierBase):
    def __str__(self):
        return super().__str__()

    def __init__(self, mesh_step_size=0.01, solver='liblinear', C=1, multi_class='auto'):
        super().__init__(mesh_step_size)
        self.__solver = solver
        self.__C = C
        self.__multi_class = multi_class
        self.classifier = linear_model.LogisticRegression(solver=self.__solver, C=self.__C, multi_class=self.__multi_class)

    def __del__(self):
        super().__del__()
        self.__solver = None
        self.__C = None
        self.__multi_class = None

    @property
    def solver(self):
        return self.__solver

    @solver.setter
    def solver(self, solver):
        self.__solver = solver
        self.classifier = linear_model.LogisticRegression(solver=self.__solver, C=self.__C, multi_class=self.__multi_class)

    @property
    def C(self):
        return self.__C

    @C.setter
    def C(self, C):
        self.__C = C
        self.classifier = linear_model.LogisticRegression(solver=self.__solver, C=self.__C, multi_class=self.__multi_class)

    @property
    def multi_class(self):
        return self.__multi_class

    @multi_class.setter
    def multi_class(self, multi_class):
        self.__multi_class = multi_class
        self.classifier = linear_model.LogisticRegression(solver=self.__solver, C=self.__C, multi_class=self.__multi_class)

    def fit(self, X, y):
        super().fit(X, y)

    def visualize_classifier(self, X=None, y=None, title=''):
        super().visualize_classifier(X=X, y=y, title=title)