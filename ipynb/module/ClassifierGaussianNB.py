# -*- coding:utf-8 -*-
from module.base.ClassifierBase import ClassifierBase
from sklearn.naive_bayes import GaussianNB

class ClassifierGaussianNB(ClassifierBase):
    def __str__(self):
        return super().__str__()

    def __init__(self, mesh_step_size=0.01):
        super().__init__(mesh_step_size)
        self.classifier = GaussianNB()

    def __del__(self):
        super().__del__()

    def fit(self, X, y):
        super().fit(X, y)

    def visualize_classifier(self, X=None, y=None, title=''):
        super().visualize_classifier(X=X, y=y, title=title)