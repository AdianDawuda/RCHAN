# Deep learning-based road segmentation using aerial imagery for automated change detection

## Contents

- [Wiki](#wiki)
- [Abstract](#abstract)
- [Run the Analysis](#run-the-analysis)
- [License](#license)

## Wiki

The project's wiki can be found [here](https://git.sbg.ac.at/st22_512323/i3-project-st23-dawuda/-/wikis/Deep-learning-based-road-segmentation-using-aerial-imagery-for-automated-change-detection)

## Abstract

The field of earth observation (EO) provides a growing amount of earth data, including satellite and aerial imagery. EO data may be used to monitor the earth’s surface and identify potential changes for numerous application domains such as urbanization and planning, disaster management, defence, agriculture, etc. Through growingly accessible computing power and frameworks, deep learning has emerged as a promising approach to automatically extract information from images. This project aims to identify roads from aerial images using a U-Net architecture-based convolutional neural network (CNN) model. Automating such laborious and manually time-consuming mapping tasks has great potential to improve work efficiency and resource allocation. Aerial images from different locations worldwide are used during the training and testing phases. The choice of training data and the model’s hyperparameters shall be crucial for accurate road detection. After evaluating and optimizing the model’s overall performance, it is applied to a real-world change detection example in Cologne, Germany. The deep learning model is built using the TensorFlow framework and interacts with the imagery data in a Python environment. Given the interdisciplinary application domains of image understanding and change detection, this project may provide valuable findings for a broad range of actors and contributes to the growing field of earth observation and deep learning. The processes and findings of this project are outlined in this paper. The code and pre-trained model are available on GitHub and Google Collab <mark> Insert link </mark>.

## Run the Analysis

All analysis steps can be found in a Jupyter Notebook on Google Colab. <mark> Insert link </mark>. To perform the analysis, the notebook needs access to a Google Drive account hosting the imagery. To use the final model to make predictions, the pretrained model with saved weights can be loaded.<mark> Insert link </mark>. To do this, skip all training steps and run the following block<mark> Insert image </mark>. In case you want to re-train the model the training data must also be hosted on Google Drive.

## License

See the [LICENSE](https://git.sbg.ac.at/st22_512323/i3-project-st23-dawuda/-/blob/main/LICENSE) file for license rights and limitations ([GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)).
