# AudioSetZSL
This repsoitory conatins the audio-visual dataset proposed for the task of multi-modal zeroshot learning.

The dataset is curated from a large dataset, [AudioSet](https://research.google.com/audioset/). 
While the original dataset was multilabel, the example videos were selected such that every video in AudioSetZSL has only one label, ie. it is a multiclass dataset. For more details on creation of the dataset, refer to our [paper](http://openaccess.thecvf.com/content_WACV_2020/papers/Parida_Coordinated_Joint_Multimodal_Embeddings_for_Generalized_Audio-Visual_Zero-shot_Classification_and_WACV_2020_paper.pdf).


Here, we provide the Youtube IDs for each class in the folder ``` youtube-id```.
The dataset is divided into 2-parts for a broader use for both the task of classification and zero-shot learning.

The examples for each class has been divided into three subsets namely, train, test and val.

Similary, for the task of ZSL the classes in the dataset is divided into seen and unseen.

We also provide the pre-trained features for both audio and video. The features are so obtained that it can be used for the task of ZSL as there is no unseen class overlap with the pre-training of the network (refer to our [paper](http://openaccess.thecvf.com/content_WACV_2020/papers/Parida_Coordinated_Joint_Multimodal_Embeddings_for_Generalized_Audio-Visual_Zero-shot_Classification_and_WACV_2020_paper.pdf) for the detailed process of the dataset split).
To download the pretrained feature follow the link : [Download](https://drive.google.com/open?id=1C5c8K0ZkPhzz-RX1qkPgkGejAssSA72v)

## Contact
Kindly contact kranti@cse.iitk.ac.in for any issues, comments etc. 


## Disclaimer
1. The dataset collection was done at IIT Kanpur. 
2. The dataset is intended to be used for academic research only. 
3. The links are YouTube links and the user is responsible for compliance with YouTube's terms and conditions. 
4. The videos are the property of the respective YouTube uploader. If any video belongs to you and you would like to have it removed kindly let us know and we will remove it from the dataset.
