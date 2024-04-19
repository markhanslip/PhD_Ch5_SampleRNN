## This is just a Colab notebook I made for convenience during my PhD project - the idea was to do the following: 

### 1) take some saxophone recordings 
### 2) augment them with time-stretch and polarity inversion
### 3) model the resulting dataset with SampleRNN  
### 4) generate some fake saxophone improv from the trained model 
### 5) make some music with the result 

The code in this repo will get you as far as step 4 ;) 

The colab notebook linked below pulls in one of my datasets from HuggingFace, does all the data pre-processing, trains a model and generates some new outputs. You just need a Google account and a HuggingFace account.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/markhanslip/PhD_Ch5_SampleRNN/blob/main/Chapter_5_Notebook_SampleRNN.ipynb)

It's my hope that some practicing musicians might find this a useful starting point for training models of their own recordings. No-one tells you that to get a decent model out of SampleRNN, you generally need quite a lot (ideally a few hours) of very consistently-recorded, consistent-sounding audio. There are other factors beyond just the size of the dataset, but provided the input audio is fairly clean and consistent, the augmentations provided in this notebook should result in a decent model from ~1 hour of source audio. 
