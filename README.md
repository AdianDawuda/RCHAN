# Automated Road Segmentation for Change Detection in Cologne

![sample](https://github.com/AdianDawuda/RCHAN/blob/main/display%20images/1_19.png)

## Contents

- [Abstract](#abstract)
- [Wiki](#wiki)
- [License](#license)

## Abstract

Through growingly accessible computing power and frameworks, deep learning has emerged as a promising approach to automatically extract information from images, thereby saving time and resources. This project combines earth observation (EO) data analysis with deep learning to highlight changes in the city of Cologne’s road network between the years 1998 and 2019. A U-Net architecture-based convolutional neural network is used to identify roads in areal images from the two years. The generated road maps are then compared to detect changes between the years. Due to the lack of available datasets for the study area, an aerial image road dataset of Massachusetts is used to train the deep learning model. The model interacts with the imagery data in a Python environment and is built using the TensorFlow framework. The results show significant changes in the road network. However, future research is needed to further improve the quality of the segmented road maps. The low time and effort required to generate road segmentations using the proposed approach may make it well-suited for time-sensitive mapping tasks. Future improvement of the methodology could enable usage for disaster response mapping or precise mapping of newly developing areas that lack road data. This interdisciplinary project has applications in urbanization, image understanding, and change detection. It contributes to the growing field of earth observation and deep learning. The code and pre-trained model are available on GitLab.

**Keywords**: Deep Learning, Semantic Segmentation, Road Network, Change Detection

## Wiki

The project's wiki can be found [here](https://github.com/AdianDawuda/RCHAN/wiki/RCHAN). It provides more in-depth information about the project, its status, and how to replicate the results.

## License

See the [LICENSE](https://git.sbg.ac.at/st22_512323/i3-project-st23-dawuda/-/blob/main/LICENSE) file for license rights and limitations ([GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)).
