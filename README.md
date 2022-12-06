[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=9337582&assignment_repo_type=AssignmentRepo)

![ML Tests](https://github.com/software-students-fall2022/containerized-app-exercise-team5/actions/workflows/mlc-testing.yml/badge.svg)
![Web App Tests](https://github.com/software-students-fall2022/containerized-app-exercise-team5/actions/workflows/web-app-testing.yml/badge.svg)

# Containerized App Exercise

Build a containerized app that uses machine learning. See [instructions](./instructions.md) for details.

## Introduction

This console recording app takes user input of speech to record the audio file. Then the web translates the audio recording into text. This machine-learning web app then analyzes the sentiment of the speech, whether it is positive or negative. Then it shows the results of the sentiment analysis along with both negative and positive words. The web app also shows the past history of all sentiment analysis results.

## Authors

- Victoria Zhang: [Github](https://github.com/Ruixi-Zhang)
- Jenny Shen: [Github](https://github.com/JennyShen10792)
- Tiffany Lee: [Github](https://github.com/les5185)
- Leah Durrett: [Github](https://github.com/howtofly-lab)
- Ian Liao: [Github](https://github.com/ian-Liaozy)
- Charlie Xiang: [Github](https://github.com/xiang-charlie)

## Installations

1. Make sure Docker Desktop is installed. If not, (click [here](https://docs.docker.com/desktop/install/windows-install/) for windows and [here](https://docs.docker.com/desktop/install/mac-install/) for mac)
2. Make sure PyAudio is installed. Find the instructions for how to install PyAudio [here](https://pypi.org/project/PyAudio/).

## How to Run the Program

1. Clean the unused mongo DB containers on Docker Desktop
2. Pull the latest version on the main branch
3. Go to the root folder and build the docker container
   ```
   docker compose build
   ```
4. Go to the root folder and run the docker container
   ```
   docker compose up -–remove-orphans
   ```
5. Now two apps are started. The ML client will run at http://0.0.0.0:5001/. The Web App will run at http://0.0.0.0:4001/sentiment-list-view. There is also a container for the database.
6. In the terminal, navigate to the ML client directory and run the recording function by entering the following command:

```
python3 record.py
```

This will allow you to record a `.wav` file, which will be saved into the current directory.

7. In the ML client, you can upload the voice recording from your local machine. The recording will change to text and will be displayed on the screen. When you are satisfied with what the text says, click the submit button.
8. Following submission, there are two links displayed on the screen, one of which redirects you to the Web App and allows you to view the result of the sentiment analysis.
9. Click on a statement to see the specifics of the sentiment analysis results. This includes whether the sentiment is positive or negative, and will also show both positive and negative words.

## How to Run Pytests

### 1. Active virtual environment

Activate a virtual environment in the root directory by using this command line

```
python3 -m venv env
source env/bin/activate
```

### 2. Go to the directory you want to test

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

### 3. Install dependencies

Install the dependencies to run pytest by using the following command line

```
pip install -r requirements.txt
```

### 4. Run pytest

Run the following command line. Make sure pytest is downloaded (`pip install pytest`)

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

<b> Code coverage for this project </b>

Machine Learning Client code coverage:

Web App code coverage: 86%
