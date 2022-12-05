[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9337582&assignment_repo_type=AssignmentRepo)

![ML Tests](https://github.com/software-students-fall2022/containerized-app-exercise-team5/actions/workflows/mlc-testing.yml/badge.svg)
![Web App Tests](https://github.com/software-students-fall2022/containerized-app-exercise-team5/actions/workflows/web-app-testing.yml/badge.svg)

# Containerized App Exercise

Build a containerized app that uses machine learning. See [instructions](./instructions.md) for details.

## Introduction

This web application takes user input of speech and translates into text. This speech-to-text program then analyzes the sentiment of the speech, whether it is positive or negative. Then it shows the results of the sentiment analysis along with both negative and positive words.

## Authors

- Victoria Zhang: [Github](https://github.com/Ruixi-Zhang)
- Jenny Shen: [Github](https://github.com/JennyShen10792)
- Tiffany Lee: [Github](https://github.com/les5185)
- Leah Durrett: [Github](https://github.com/howtofly-lab)
- Ian Liao: [Github](https://github.com/ian-Liaozy)
- Charlie Xiang: [Github](https://github.com/xiang-charlie)

## How to Run the Program

1. Make sure Docker Desktop is installed. If not, (click [here](https://docs.docker.com/desktop/install/windows-install/) for windows and [here](https://docs.docker.com/desktop/install/mac-install/) for mac)
2. Clean the unused mongo DB containers on Docker Desktop
3. Pull the latest version on the main branch
4. Go to the root folder and build the docker container
   ```
   docker compose build
   ```
5. Go to the root folder and run the docker container
   ```
   docker compose up -–remove-orphans
   ```
6. Now two apps are started. The ML client will run at http://0.0.0.0:5001/. The Web-app will run at http://0.0.0.0:4001/sentiment-list-view. There is also a container for the database.
7. In the ML client, you can press the record button to store the speech. Then speech will change to text and show on the screen with the sentiment analysis of the speech (text). The sentiment analysis contains whether the sentiment is positive or negative and will also show both positive and negative words.
8. After analyzing different sentiments with the ML client, you can view all past results in a list view. Once you click one sentiment analysis item, it’ll show you the text and sentiment analysis for that specific item.

## How to Run Pytests

### 1. Active virtual environment

Activate a virtual environmennt in the root directory by using this command line

```
python3 -m venv env
source env/bin/activate
```

### 2. Install dependencies

Install the dependencies to run pytest by using the following command line

```
pip install -r requirements.txt
```

### 3. Go to the directory you want to test

#### Web app

Go to the web-app directory

```
cd web-app
```

#### Machine Learning Client

Go to the machine-learning-client directory

```
cd machine-learning-client
```

### 4. Run pytest

Run the following command line

```
python3 -m pytest
```

### 5. Check the code coverage report

Run the following commannd line to see the code coverage report

```
coverage report -m
```

Below is the example code coverage report

```
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
app.py                   20      6    70%   20-22, 26-29, 34
tests/__init__.py         0      0   100%
tests/test_app.py         7      0   100%
tests/test_utils.py      14      0   100%
utils.py                  2      0   100%
---------------------------------------------------
TOTAL                    43      6    86%
```

##### Code coverage for this project

Machine Learning Client code coverage:

Web App code coverage: 86%
