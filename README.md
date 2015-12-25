This repository contains code for an implementation of a multinomial Naive Bayes classifier with a GUI. The tool will allow you to train as many categories as you want with various documents, and then classify new documents.

The tool can also graph the log likelihoods of all words in your training data, given each category. However, because I was personally only dealing with the binary case, it will only do this for the first TWO classes -- however, feel free to fork or expand as you wish. For now, the graphing code is commented. 

This application is not specific to my problem; you can use it out of the box for any classification problem you wish. Feel free to get in touch with me if you have any comments or questions!

Tested with python 2.7 on Mac OSX. 
matplotlib is required(for plotting log likelihoods after a classificationi ONLY).
TKinter is required, but should be come with your python installation.
