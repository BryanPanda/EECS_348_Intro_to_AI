from __future__ import print_function
import math
import random

class Bayes_Classifier:

    def __init__(self):
        # number of positive reviews
        self.numPos = 0
        # number of negative reviews
        self.numNeg = 0
        # number of words in a class
        self.numWordClass = {}
        # the number of words in positive class
        self.numWordPos = 0
        # the number of words in negative class
        self.numWordNeg = 0
        # vocabulary of all the docs
        self.voc = set([])

    def train(self,filename):
        # code to be completed by students to extract features from training file, and
        # to train naive bayes classifier.

        with open(filename, 'rt') as f:
            lines = f.readlines()

        for line in lines:
            line = line.replace('\n', '')
            fields = line.split('|')
            sentiment = fields[1]
            text = fields[2]
            words = text.split(' ')

            for word in words:
                key = sentiment + word
                self.voc.add(word)
                if self.numWordClass.get(key) == None:
                    self.numWordClass[key] = 1
                else:
                    self.numWordClass[key] += 1

            if sentiment == "1":
                self.numNeg += 1
                self.numWordNeg += len(words)
            else:
                self.numPos += 1
                self.numWordPos += len(words)

    def classify(self,filename):
        # code to be completed by student to classifier reviews in file using naive bayes
        # classifier previously trains.  member function must return a list of predicted
        # classes with '5' = positive and '1' = negative

        numVoc = len(self.voc)
        predict = []

        with open(filename, 'rt') as f:
            lines = f.readlines()

        for line in lines:
            line = line.replace('\n', '')
            fields = line.split('|')
            text = fields[2]
            words = text.split(' ')

            pPos = float(self.numPos) / float((self.numPos + self.numNeg))
            pNeg = float(self.numNeg) / float((self.numPos + self.numNeg))
            pWordClassNeg = 0
            pWordClassPos = 0

            for word in words:
                if self.numWordClass.get("1" + word) == None:
                    pWordClassNeg = 1.0 / float((self.numWordNeg + numVoc))
                else:
                    pWordClassNeg = float((self.numWordClass["1" + word] + 1)) / float((self.numWordNeg + numVoc))
                if self.numWordClass.get("5" + word) == None:
                    pWordClassPos = 1.0 / float((self.numWordPos + numVoc))
                else:
                    pWordClassPos = float((self.numWordClass["5" + word] + 1)) / float((self.numWordPos + numVoc))

                pNeg *= pWordClassNeg
                pPos *= pWordClassPos

            if pNeg > pPos:
                predict.append("1")
            else:
                predict.append("5")

        return predict



    
