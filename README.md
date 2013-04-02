This is a personal project I did on hypnotic linguistics. I was interested in whether I could isolate key important features of hypnotic language from hypnotic documents using a simple classifying technique like naive bayes. This would be useful because there is not very much literature on how to properly conduct a hypnotic induction and there is a lot of myth surrounding hypnosis in general. However, hypnosis is a scientific phenomenon that we simply do not know very much about, and it is potentially very useful, so I was interested in exploring the way it works from a computational perspective. The paper in this repo shows my results (successful!). 

Additionally you will find a multinomial naive bayes implementation with Laplace smoothing, complete with a GUI. This tool will allow you to train as many categories as you want, and then classify new documents.

The tool can also graph the log likelihoods of all words in your training data, given each category. However, because I was only dealing with the binary case, it will only do this for the first TWO classes -- feel free to take this code and expand on it. For now the graphing code is commented out. 

This application is not specific to my problem; you can use it out of the box for any classification problem you wish. Feel free to get in touch with me if you have any comments or questions!

Tested with python 2.7 on Mac OSX. 
matplotlib is required(for plotting log likelihoods after a classificationi ONLY).
TKinter is required, but should be come with your python installation.
