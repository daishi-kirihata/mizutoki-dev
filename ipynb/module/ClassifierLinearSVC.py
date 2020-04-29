# -*- coding:utf-8 -*-
from module.base.ClassifierBase import ClassifierBase
from sklearn.svm import LinearSVC

class ClassifierLinearSVC(ClassifierBase):
    def __str__(self):
        return super().__str__()

    def __init__(self, mesh_step_size=0.01, random_state=0):
        super().__init__(mesh_step_size)
        self.__random_state = random_state
        self.classifier = LinearSVC(random_state=self.__random_state)

    def __del__(self):
        super().__del__()
        self.__random_state = None

    @property
    def random_state(self):
        return self.__random_state

    @random_state.setter
    def random_state(self, random_state):
        self.__random_state = random_state
        self.classifier = LinearSVC(random_state=self.__random_state)

    def fit(self, X, y):
        super().fit(X, y)

    def visualize_classifier(self, X=None, y=None, title=''):
            super().visualize_classifier(X=X, y=y, title=title)