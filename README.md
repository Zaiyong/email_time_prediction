# Prediction of Email Sending Time

In this project, we analyse the relationships between some features and email sending time, build and deploy an machine learningg model to predict the email sending time.


### Prerequisites
Make sure you have installed all of the following prerequisites on your development machine
* Python 3.7.6 - [Download & Install Python](https://www.python.org/downloads/)
* pip - [Download & Install pip](https://pip.pypa.io/en/stable/installing/)
* Git - [Download & Install Git](https://git-scm.com/downloads)
* virtualenv - user pip to install
    pip3 install virtualenv 
    
### Installing packages
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
### Folder Structure

## Deployment

## Download and run Docker Image
```
docker push zhangqibiao177/time_predict:tagname
docker run -d -p 5000:5000 zhangqibiao177/time_predict:latest
```
## Authors

* **Zaiyong Zhnang** - *Main Contributor* - [zaiyongzhang.com](http://zaiyongzhang.com/)

## License

This project is licensed under the MIT License - see the [LICENSE](https://choosealicense.com/licenses/mit/) for details
