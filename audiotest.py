#!/usr/bin/env python 

import numpy as np

import matplotlib.pyplot as plt



import soundfile as sf


def readKiku():
    pass









def insertPulse(array, per, int):

    array[::per] = array[::per] + int
    return array





def creatSim(nSamples = 100):
    

    

    np.random.seed(666)
    array = np.random.random(nSamples)

    print (array)

    per = nSamples // 10
    array = insertPulse(array, per, 3.0)

    array = insertPulse(array, nSamples // 17, 2.0 )
    return array




def testBpm():

    #read file
    data, samplerate = sf.read('C:\\git-repos\\kikucut.wav')
    data = data[:,0:].flatten() #TODO, why this, what if more channels?
    nSamples = len(data)


    print (samplerate)

    print ('data')
    print (data)
    print (len(data))
    print (len(data) / samplerate)

    print ( np.max(data))

    isHere = int(np.where(data == np.max(data))[0])

    print (isHere)






    #run the coorelation
    #window = int(samplerate * 2)

    #cor = np.correlate(data[isHere:isHere+100],data[isHere:isHere+100],"full")


    #pick a small window and downsample    
    #window = data[isHere:isHere+5*samplerate]
    window = data
    window = window[::500]#todo be smarter


    cor = np.correlate(window[:],window[:],"full")


    print ( cor )
    
    #plot stuff
    plt.plot(window)
    plt.ylabel('some numbers')

    #plt.ylabel('some numbers')


    #find peaks in coorelation
    nPeaks = 20
    peaks = window.argsort()[:nPeaks]
    print ( peaks,flush = True)

    peakPlt = np.zeros(len(window))
    for i in peaks:
        peakPlt [i] = 1.0

    plt.plot(peakPlt)


    plt.figure()
    plt.plot(cor[:])
    #plt.plot(cor[len(cor)//2 : len(cor)])
    plt.show()

#"same")
#array([2. ,  3.5,  3. ])
#np.correlate([1, 2, 3], [0, 1, 0.5]#, "full")


if __name__ == "__main__":
    testBpm()
    pass


   



