# AbAgIntPre
AbAgIntPre is a deep learning-assisted web server for fast identification of antibody-antigen interactions that only relies on amino acid sequences. By using a Siamese-like convolutional neural network with the amino acid composition encoding scheme, AbAgIntPre achieved satisfactory performance with the Area Under Curve (AUC) of 0.82 on a high-quality generic independent test dataset. Besides, this approach also showed competitive performance on the more specific SARS-CoV dataset. We expect that AbAgIntPre can serve as an important complement to traditional experimental methods for antibody screening and effectively reduce the workload of antibody design. The web server of AbAgIntPre is freely available at [here](http://www.zzdlab.com/AbAgIntPre).
## Network Architecture
![Network Architecture](https://github.com/emersON106/AbAgIntPre/blob/main/img/Network%20Architecture.png)
You can find the source code of siamese CNN architechture and CKSAAP encoding strategy in `model` folder.
## Dataset
The binding samples we used in our study were from two public databases: [SAbDab](http://opig.stats.ox.ac.uk/webapps/newsabdab/sabdab/) and [CoV-AbDab](http://opig.stats.ox.ac.uk/webapps/covabdab/).
Folder `SAbDab` stores all the PDB ID used in our generic model training. Folder 'CoV-AbDab' stores the cross validation dataset and independent dataset used in our CoV-specific model traning.
## Acknowledgments
We would like to thank the [SAbDab](http://opig.stats.ox.ac.uk/webapps/newsabdab/sabdab/) and [CoV-AbDab](http://opig.stats.ox.ac.uk/webapps/covabdab/)  for the antibody-antigen binding data support.
