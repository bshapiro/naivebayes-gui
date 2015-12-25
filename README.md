Naive Bayes GUI
===============

This repository contains code for an implementation of a multinomial Naive Bayes classifier with a GUI. The tool will allow you to train as many categories as you want with various documents, and then classify new documents.

The tool can also graph the log likelihoods of all words in your training data, given each category. However, I have only dealt with the binary case; it can only graph the log likelihoods for the first two classes. Feel free to fork or expand as you wish. For now, the graphing code is commented. 

Tested with python 2.7 on Mac OSX. 
matplotlib is required(for plotting log likelihoods after a classificationi ONLY).
TKinter is required, but should be come with your python installation.
