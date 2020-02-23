# Prediction of Email Sending Time

In this project, we analyse the relationships between some features and email sending time, build and deploy an machine learningg model to predict the email sending time.

![demo](https://raw.githubusercontent.com/Zaiyong/email_time_prediction/master/images/TS_TO_diff.png)

## Prerequisites
Make sure you have installed all of the following prerequisites on your development machine
* Python 3.7.6 - [Download & Install Python](https://www.python.org/downloads/)
* pip - [Download & Install pip](https://pip.pypa.io/en/stable/installing/)
* Git - [Download & Install Git](https://git-scm.com/downloads)
* virtualenv - user pip to install
    pip3 install virtualenv 
    
## Installing packages
Please create an virtual environment before installing required packages:
```
virtualenv venv
```
Active your virtual environment:
```
source venv/bin/activate
```
Now install required packages with pip:
```
pip install -r requirements.txt
```
## Folder Structure
    .
    ├── requirements.txt                # Python libraries
    ├── README.md                       # readme
    ├── 1.EDA.ipynb                     # the notebook to analyse and preprocess data
    ├── 2.train_test_ml_model.ipynb     # the notebook to train/test machine learning model
    ├── 3.train_test_dl_model.ipynb     # the note book to train/test deep learning model
    ├── client.py                       # a client demo to access RES API of DL model
    ├── model                           # trained models
    │   ├── svm_model.pkl               # SVM regression model
    │   ├── min_max_scaler.joblib       # for min-max normalization
    │   └── dl_model                    # deep learning model
    ├── data                            # raw and processed data
    │   ├── data.csv                    # raw data
    │   ├── clean.csv                   # preprocessed data
    ├── docker_repo                     # docker container
    │   ├── time_predict.py             # the flask file
    │   ├── requirements.txt            # python libraries
    │   ├── Dockerfile                  # docker 
    │   ├── dl_model                    # deep learning model 
    └── ...
## Deployment as REST API

### Download and run Docker Image
```
docker pull zhangqibiao177/time_predict
docker run -d -p 5000:5000 zhangqibiao177/time_predict:latest
```
### Aceess the EndPoint via demo
```
python client.py
```

## Authors

* **Zaiyong Zhnang** - *Main Contributor* - [zaiyongzhang.com](http://zaiyongzhang.com/)

## License

This project is licensed under the MIT License - see the [LICENSE](https://choosealicense.com/licenses/mit/) for details
