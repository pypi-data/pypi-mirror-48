from urllib.request import urlretrieve
import h5py
import numpy as np
from tqdm import tqdm
import scipy
import scipy.io as scio
import pandas as pd


"""
    CWAES collected from ChipWhisperer-Lite, AES-128.
    >> https://github.com/DonggeunKwon/dlsca/raw/master/trace/
       cw-xmega-AES-ppc4-dwt3-38000.mat
    
    - Target board: CW308T-XMEGA, Atmel XMEGA128(8-bit)
    - Fixed clock frequency: 7.37MHz
    - Sampling rate: 29.538MS/s
    - Captured: AES-128 1round
    - Preprocess: Discrete wavelet transform level 4
"""
def CWAES(path='./'):
    file='cw-xmega-AES-ppc4-dwt3-38000.mat'
    url = 'https://github.com/DonggeunKwon/dlsca/raw/master/trace/' + file
    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, 
              miniters=1, desc='CWAES') as t:
        urlretrieve(url=url, 
                    filename=path+file, 
                    reporthook=TqdmUpTo(t))
    tmp = h5py.File(path + file, 'r')
    
    print('return trace, plaintext')
    return (np.array(tmp['trace']), np.array(tmp['pt']))


"""
    ANSSI SCA Databases(ASCAD)
    
    https://www.data.gouv.fr/s/resources/ascad/20180530-163000/ASCAD_data.zip
    >> https://github.com/DonggeunKwon/dlsca/raw/master/trace/ASCAD.mat
    
Copyright (C) 2018, ANSSI and CEA

The databases, the Deep Learning models and the companion 
python scripts of this repository are placed into the public domain.
"""
def ASCAD(path='./', desyn=''):
    if desyn=='_desync50' or desyn=='_desync100':
        file = 'ASCAD'+ desyn +'.mat'
    else :
        file = 'ASCAD.mat'
    
    try:    
        tmp = h5py.File(path + file, 'r')
    except:
        url = 'https://github.com/DonggeunKwon/dlsca/raw/master/trace/' + file
        with tqdm(unit='B', unit_scale=True, unit_divisor=1024, 
                  miniters=1, desc='ASCAD') as t:
            urlretrieve(url=url, 
                        filename=path+file, 
                        reporthook=TqdmUpTo(t))
            
        tmp = h5py.File(path + file, 'r')
    
    print('return (trace, label)')
    return (np.array(tmp['trace']), np.array(tmp['label']))


"""
    Datasets from CHES papers on random delays
    
    https://github.com/ikizhvatov/randomdelays-traces/raw/master/
    ctraces_fm16x4_2.mat
    
This work is licensed under a Creative Commons 
Attribution-NonCommercial 4.0 International License
"""
def RandomDelay(path='./', desyn=''):
    file = 'ctraces_fm16x4_2.mat'
    url = 'https://github.com/ikizhvatov/randomdelays-traces/raw/master/' +file
    
    try:
        tmp = scio.loadmat(path+file)
    except:        
        with tqdm(unit='B', unit_scale=True, unit_divisor=1024, 
                  miniters=1, desc='RD') as t:
            urlretrieve(url=url, 
                        filename=path+file, 
                        reporthook=TqdmUpTo(t))
            
        tmp = scio.loadmat(path+file)
    
    print('return (trace, plaintext)')
    return (np.array(tmp['CompressedTraces']).T, np.array(tmp['plaintext']))


"""
    FPGA SASEBO GII (Hardware) AES Dataset
    
    https://github.com/AESHD/AES_HD_Dataset

All datasets are in csv format where each row corresponds to one measurement.
Features are comma separated.
No pre-processing is done.
Separate csv file with labels.

Sample sizes:
AES HD: 100.000 traces, 1250 features max (whole trace)
Traces are divided into 5 smaller sets (20000 each)
"""
def AESHD(path='./'):
    file = ['traces_1.csv', 'traces_2.csv','traces_3.csv',
            'traces_4.csv','traces_5.csv','labels.csv']
    url = 'https://github.com/AESHD/AES_HD_Dataset/raw/master/'
    
    data = []
    
    for i in range(len(file)):
        try:
            dat = pd.read_csv(path+file[i], header=None)
            print('\r' + file[i] + ' already exists...')
        except:
            with tqdm(unit='B', unit_scale=True, unit_divisor=1024, 
              miniters=None, desc='RD') as t:
                t.set_description('RD-' + file[i])
                urlretrieve(url=url+file[i], 
                        filename=path+file[i], 
                        reporthook=TqdmUpTo(t))
            dat = pd.read_csv(path+file[i], header=None)
            
        if i!=len(file)-1:
            data.append(np.array([[int(i) for i in dat[0][j].split(' ')] 
            for j in range(len(dat[0]))]))
        else:
            data.append(dat.values)
    
    print('\r' + 'return (trace, label)')
    return (np.concatenate([data[i] for i in range(len(file)-1)]), data[-1])


# ProgressBar with tqdm
def TqdmUpTo(t):
    last_b = [0]
    def update_to(b=1, bsize=1, tsize=None):
        if tsize is not None:
            t.total = tsize
        t.update((b - last_b[0]) * bsize)
        last_b[0] = b
    return update_to