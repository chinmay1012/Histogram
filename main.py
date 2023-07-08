import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('ggplot')


data=pd.read_csv(r'E:\Masters\Studies\Semester 3\Thesis Work\Hahn Automation\Cycle time csv\Histogram_Cycletime.csv')
plt.figure(figsize=(10, 5))

def Histo():
    plt.subplot(2, 2, 1)
    Runtime = data['300Ms']
    bins = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6]
    plt.hist(Runtime, bins=bins, edgecolor = "black", color = "red")
    plt.title('300 samples Histogram')
    plt.xlabel('Runtime(Ms)')
    plt.ylabel('No of Occurances')

    plt.subplot(2, 2, 2)
    Runtime1 = data['5000Ms']
    bins1 = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6]
    plt.hist(Runtime1, edgecolor="black", bins=bins1, color="Green")
    plt.title('5000 samples Histogram')
    plt.xlabel('Runtime(Ms)')
    plt.ylabel('No of Occurances')

    plt.subplot(2, 2, 3)
    Runtime2 = data['10000Ms']
    bins2 = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6]
    plt.hist(Runtime2, edgecolor="black", bins=bins2, color="Blue")
    plt.title('10000 samples Histogram')
    plt.xlabel('Runtime(Ms)')
    plt.ylabel('No of Occurances')

    plt.subplot(2, 2, 4)
    Runtime3 = data['15000Ms']
    bins3 = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6]
    plt.hist(Runtime3, edgecolor="black", bins=bins3, color="Purple")
    plt.title('15000 samples Histogram')
    plt.xlabel('Runtime(Ms)')
    plt.ylabel('No of Occurances')

    plt.tight_layout()
    plt.show()

Histo()



def Histo20000samples():
    #plt.subplot(2, 2, 4)
    #plt.figure(figsize=(15,5))
    Runtime1 = data['20000Ms']
    bins = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6]
    plt.hist(Runtime1, edgecolor="black", bins=bins, color="Brown")

    plt.title('20000 samples Histogram')
    plt.xlabel('Runtime(Ms)')
    plt.ylabel('No of Occurances')

    plt.tight_layout()

    plt.show()

Histo20000samples()

def Histo25000samples():
    #plt.subplot(1, 2, 2)
    #plt.figure(figsize=(15,5))
    Runtime1 = data['25000Ms']
    bins = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6]
    plt.hist(Runtime1, edgecolor="black", bins=bins, color="Grey")

    plt.title('25000 samples Histogram')
    plt.xlabel('Runtime(Ms)')
    plt.ylabel('No of Occurances')

    plt.tight_layout()

    plt.show()

Histo25000samples()

