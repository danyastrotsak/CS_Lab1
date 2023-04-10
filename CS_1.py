import numpy as np
import os
import codecs

class Lab1:
    filePath = ""
    fileBitCount = 0
    fileContent = ""
    contentLength = 0
    alphabetta = {}
    probability = []
    entropia = 0
    informationAmount = 0

    def __init__(self, filePath):
        self.filePath = filePath
        file = codecs.open(filePath, "r", encoding='utf-8')
        fileContent = file.read()
        file.close()
        self.fileContent = fileContent
        self.contentLength =int(len(fileContent))
        self.CalculateAlphabettaProbability()
        self.CalculateEntropia()
        self.fileBitCount = os.path.getsize(filePath) * 8
        self.Output()
        print(str(self.entropia) + "\n" + str(self.probability) )

    def CalculateEntropia(self):
        log = np.log2(self.probability)
        self.entropia = (-1)*np.sum(self.probability * log)
        self.informationAmount = self.entropia * self.contentLength


    def CalculateAlphabettaProbability(self):
        chars = list(set(self.fileContent))
        frequency = []
        temporary = []

        for i in range(0, len(chars)):
            frequency.append(self.fileContent.count(chars[i]))
        for i in range(0, len(chars)):
            temporary.append((chars[i], frequency[i]))

        self.alphabetta = dict(temporary)
        for i in range(0, len(chars)):
            self.probability.append(int(frequency[i]) / self.contentLength)

    def Compare(self):
        if(self.fileBitCount > self.entropia):
            line = "file size is bigger then entropia \n " + str(self.fileBitCount) + " > " + str(self.informationAmount) + "\n"
            return line
        else:
            line = "entropia is bigger then file size \n " + str(self.informationAmount) + " > " + str(self.fileBitCount) + "\n"
            return line

    def Output(self):
        size = str(os.path.getsize(self.filePath)) + "\n"
        title = "Entropia = " + str(self.entropia) + "\n" + "Data amount = " + str(self.informationAmount / 8) + "\n" + self.Compare()
        outputPath = self.filePath.replace(".txt", "_result.txt")
        content = str(self.alphabetta)
        output = title + "\n \n" + content + "\n \n"
        output += size

        with codecs.open(outputPath, "w", encoding='utf-8') as file:
            file.write(output)



#path1 = "G:/Dania/1_base.txt"
path2 = "G:/Dania/3bz2_base.txt"
#Text = Lab1(path1)
Base = Lab1(path2)
