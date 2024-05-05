## This repository contains a Colab notebook and some Python classes I made during my PhD project - the idea was to do the following: 

### 1) take some saxophone recordings 
### 2) augment them with time-stretch and polarity inversion
### 3) model the resulting dataset with SampleRNN  
### 4) generate some fake saxophone improv from the trained model 
### 5) make some music with the result 

The Colab notebook takes care of steps 1-4. 

The colab notebook linked below pulls in one of my datasets from HuggingFace, does all the data pre-processing, trains a model and generates some new outputs. You just need a Google account and a HuggingFace account.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/markhanslip/PhD_Ch5_SampleRNN/blob/main/Chapter_5_Notebook_SampleRNN.ipynb)

The code in the folder 'b.io' is one of the many possible answers to step 5: a simple interactive system I wrote to make this piece https://vimeo.com/manage/videos/740818419

It's my hope that some practicing musicians might find this a useful starting point for training models of their own recordings and doing something with the outputs. No-one tells you that to get a decent model out of SampleRNN, you generally need quite a lot (ideally a few hours) of very consistently-recorded, consistent-sounding audio. There are other factors beyond just the size of the dataset, but provided the input audio is fairly clean and consistent, the augmentations provided in this notebook should result in a decent model from ~1 hour of source audio. 
