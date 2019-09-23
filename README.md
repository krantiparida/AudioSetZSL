# AudioSetZSL
This repsoitory conatins the audio-visual dataset proposed for the task of multi-modal zershot learning.

The dataset is curated from a large dataset, [AudioSet](https://research.google.com/audioset/). 
While the original dataset was multilabel, the example videos were selected such that every video in AudioSetZSL has only one label, ie. it is a multiclass dataset. For more details on creation of the dataset, refer to our paper.


Here, we provide the Youtube IDs for each class in the folder ``` youtube-id```.
The dataset is divided into 2-parts for a broader use for both the task of classification and zero-shot learning.

The examples for each class has been divided into three subsets namely, train, test and val.

Similary, for the task of ZSL the dataset is divided into see and unseen.

We also provide the pre-trained features for both audio and the features are so obtained that it can be used for the tsak of ZSL as there is no unseen class overlap with the pre-training of the network.