# -*- coding: cp1252 -*-
from collections import Counter
from Tkinter import *
import tkFileDialog
from ttk import *
import math
import string
import matplotlib.pylab as plt

class NaiveBayes:

    def __init__(self):
        # create a menu
        menu = Menu(root)
        root.config(menu=menu)
        root.title("Naive Bayes Classifier")
        self.totalWordProbs = Counter()
        self.classProbs = Counter()
        self.classWordProbs = {}
        self.classWordLogProbs = {}

        # some NLP setup
        self.goodChars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "'"]
        self.stopWords = ["no", "it's", "i", "just", "", "a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount", \
                          "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are",\
                          "around", "as", "at", "back","be","became", "because","become","becomes", "becoming",\
                          "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between",\
                          "beyond", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con",\
                          "could", "couldnt", "cry", "de", "do", "done", "down", "due", "during",\
                          "each", "eg", "eight", "either", "eleven","else", "elsewhere", "enough", "etc", "even",\
                          "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill",\
                          "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from",\
                          "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence",\
                          "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself",\
                          "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is",\
                          "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many",\
                          "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move",\
                          "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next",\
                          "nine", "nobody", "none", "noone", "nor", "nothing", "now", "nowhere", "of", "off",\
                          "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our",\
                          "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather",\
                          "re", "same", "see", "seem", "seemed", "seeming", "seems", "several", "she", "should",\
                          "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone",\
                          "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten",\
                          "than", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter",\
                          "thereby", "therefore", "therein", "thereupon", "these", "they", "third",\
                          "this", "though", "three", "through", "throughout", "thru", "thus", "to", "together",\
                          "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon",\
                          "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever",\
                          "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which",\
                          "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within",\
                          "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Exit", command=quit)

        # graphics
        className = Label(root, text="Class name:").grid(row=0,column=0, sticky="W S", padx=10, pady=2)
        self.classInput = Entry(root,width=60)
        self.classInput.grid(row=1, column=0, padx=10,pady=2, columnspan=6, sticky="W")
        trainingLabel = Label(root,text="Choose files to train for this class:")
        trainingLabel.grid(row=2,columnspan=3,column=0,padx=10,pady=2,sticky="W")
        self.trainingFiles = Text(root, width=45, height=10)
        self.trainingFiles.grid(row=3,column=0,padx=10,pady=2, columnspan=6)

        self.add = Button(root, text="Add...", width=10,
                          command = self.addFiles
                          )
        self.add.grid(row=4, column=4, padx = 2, pady=7, sticky="E")

        self.train = Button(root, text="Train", width=10,
                       command = self.train
                       )
        self.train.grid(row=4, column=5, padx = 2, pady=7, sticky="W")

        classifyButton = Button(root, text="Let's classify a document!",width=30, command=self.classify)
        classifyButton.grid(row=5,columnspan = 6,padx=10, column=0,pady=7)
        self.v = StringVar()

        resultLabel = Label(root,textvariable=self.v, width=30, font=15)
        self.v.set("Result:")
        resultLabel.grid(row=6,column=2,columnspan=6, pady=10)

        # begin application mainloop
        mainloop()

    def Quit(self):
        sys.exit()

    def parseWord(self, word):
        newString = ""
        for c in word:
            if c in self.goodChars:
                newString = newString + c
        return newString

    def addFiles(self):
        locations = tkFileDialog.askopenfilename(multiple=True) #open dialog
        for location in locations:
            self.trainingFiles.insert(END,location + "\n")

    def train(self):
        className = self.classInput.get()
        self.classWordProbs[className] = Counter()
        locations = self.trainingFiles.get(1.0, END)
        locationsList = locations.split("\n")
        for location in locationsList:
            if location != "":
                string.replace(location,"{","")
                string.replace(location,"}","")
                self.classProbs[className] += 1
                doc = open(location)
                for line in doc:
                    wordList = line.split(" ")
                    for word in wordList:
                        word = word.splitlines()
                        if len(word) > 0:
                            word = word[0]
                            word = word.lower()
                            word = self.parseWord(word)
                            if word not in self.stopWords and word != "":
                                self.totalWordProbs[word] += 1
                                self.classWordProbs[className][word] += 1

    def classify(self):
        location = tkFileDialog.askopenfilename() #open dialog
        maxsofar = -99999999999
        bestClassSoFar = None
        for category in self.classProbs:
            doc = open(location)
            totalWords = 0
            for item in self.classWordProbs[category]:
                totalWords += self.classWordProbs[category][item] + 1
            categoryProb = self.classProbs[category] / float(sum(self.classProbs.values()))
            documentGivenCategory = 0.0
            for line in doc:
                wordList = line.split(" ")
                for word in wordList:
                    word = word.splitlines()

                    if len(word) > 0:
                        word = word[0]
                        word = word.lower()
                        word = self.parseWord(word)
                        if word not in self.stopWords and word != "":
                            documentGivenCategory += (float(math.log(float(self.classWordProbs[category][word] + 1))) - float(math.log(float(totalWords + 1))))
            curCategoryGivenDocument = (documentGivenCategory  + math.log(categoryProb))


            if curCategoryGivenDocument > maxsofar:
                maxsofar = curCategoryGivenDocument
                bestClassSoFar = category
        self.v.set("Result: " + str(bestClassSoFar))

        # To graph the statistics for the first two classes, uncomment the code below.
        """
        resultsfile = open("results.txt","w")
        resultsfile.write(str(self.classWordProbs.values()[0]))
        resultsfile.write("\n")
        resultsfile.write(str(self.classWordProbs.values()[1]))

        graphedy = []
        graphedx = []
        f1 = plt.figure()
        f2 = plt.figure()
        totalWordsDict = {}
        classNames= self.classProbs.keys()
        for classObject in classNames:
            totalWords= 0
            for item in self.classWordProbs[classObject]:
                totalWords += self.classWordProbs[classObject][item]
            totalWordsDict[classObject] = totalWords

        for classObject in classNames:

            classWordList = []
            classCountList = []
            for word in self.classWordProbs[classObject]:
                classWordList.append(word)
                classCountList.append((float(math.log(self.classWordProbs[classObject][word])) - float(math.log(totalWordsDict[classObject]))))
            graphedy.append(classCountList)
            graphedx.append(classWordList)
        sf1 = f1.add_subplot(111)
        sf1.plot([i for i in range(0,len(graphedx[0]))], graphedy[0], '.')
        sf1.grid(True)
        sf1.set_xlabel("Word index(arbitrary)")
        sf1.set_ylabel("Log likelihood")
        sf2 = f2.add_subplot(111)
        sf2.set_xlabel("Word index(arbitrary)")
        sf2.set_ylabel("Log likelihood")
        sf2.plot([i for i in range(0,len(graphedx[1]))], graphedy[1], '.')


        for i in range(0,len(graphedx)):
            pairs = {}
            for j in range(len(graphedy[i])):
                if graphedy[i][j] > -6:
                    pairs[graphedx[i][j]] = graphedy[i][j]
            orderedPairs = sorted(pairs, key=pairs.get)
            for n in range(0,len(orderedPairs)):
                orderedPairs[n] += "," + str(graphedy[i][graphedx[i].index(orderedPairs[n])])

        sf2.grid(True)
        plt.show()
        """


if __name__ == "__main__":


    ## WINDOW SETUP ##
    root = Tk()
    app = NaiveBayes()
    root.mainloop()

