# MALARIA CELL CLASSIFICATION WITH VGG-19 AND INCEPTION-RESNET

In recent years, there has been increasing interest in using machine learning algorithms to
automate the diagnosis of malaria from digital images of blood smears. The goal of malaria
cell classification is to classify blood cell images into two classes: uninfected and parasitized.
Uninfected cells are those that do not contain the malaria parasite in RBC, while parasitized
cells are those in which RBC is infected with the parasite. By correctly identifying parasitized
cells, a machine learning algorithm can provide a fast and accurate diagnosis of malaria, which
can lead to better treatment outcomes and ultimately save lives.

## DATASET

The dataset for this project was taken from kaggle, Malaria Cell Images Dataset. The dataset can be downloaded from the link, https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria


## RUN THE PROGRAM

To run the program, first download the models from https://drive.google.com/drive/folders/1zR_L2XBShEancMoko044IMNvXpAnuTez?usp=share_link and put it in models folder.

For training
```
run classification.ipynb
```
For checking single image
```
run single.ipynb and run all cell
```
For CAM
```
run Class Activation Map(CAM).ipynb
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
