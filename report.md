## The idea of modeling
To create a model, which predicts the sending time TS so that opening time TO will be as early as possible, the direct way is focusing on the data with low TS TO difference. Now we can abstract the problem into a standard machine learning problem with filtered dataset.
* Feature: X1, X2, X3  
* Target: TS  
* Dataset: df.TS_TO_diff_minutes<TS_TO_diff_threshold  

## What I did

### Preprocess:
1. Reshape the dataset.
2. One hot-encoding on X3.   
3. Normalize X1, X2.  

### EDA
1. Visualize the distribution and correlations among the dataset.   
2. Calculation the pearson correlatons.  

### Train/Test with machine learning 
**Train the data with following regression models:**  
1. RandomForest  
2. AdaBoost  
3. GradientBoost  
4. SVM  

**Use cross-validation to evaluate the models.**  
**Use grid search to tuning the models.**  
**Save the models as files.**  

### Train/Test with deep learning 
1. define a simple deep neural network
2. Use cross-validation to evaluate the model.
3. Save he model locally.

### 🚀★Bonus★:
1. Build a Docker image that serve the DL model as REST API with flask.
2. Publish the docker image on docker hub.


## How to improve the model
1. this is a typical underfitting problem due to limited feature size. The best way to improve the model is adding more features.
2. implement a particular loss function baseon the TO-TS, since is the final target.
2. do a deep engineering to extract more infomration from existing data.
3. design a better deep learning model.
