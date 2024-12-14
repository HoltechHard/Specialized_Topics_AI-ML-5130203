# Specialized_Topics_AI-ML-5130203  

### Main Goals of Course  
  
The main purpose of the course is offer to the students of professional carreer **Интеллектуальные информационные системы и обработка данных** (Intelligent-information systems and data processing - 5130203/20101 and 20102), the capacity to have precise understanding about the theoretical/math fundamentals and technical-practical capabilities to implement models of the most known subfields of Artificial Intelligence (Machine Learning, Deep Learning and Reinforcement Learning), concluding with the integration of these AI-models into real useful information systems.  
  
### Repository with Materials  
  
The repository will contain all the slides of lectures and the necessary files to can complete the assigned tasks, and it will be updated each friday of the week.  
Link of the repository:  
https://drive.google.com/drive/folders/1yMlQ84DXPC5XFxwZYOjCkUy0HjL5DsTR?usp=sharing  

### Partial scores (Sep-Oct) of Homeworks (scale [0-100])  
Link of score results for groups 20101 and 20102:    
https://docs.google.com/spreadsheets/d/1CVksCzIFo023JQiaenIKWVeGO736eXYZ/edit?usp=sharing&ouid=102162186379183170525&rtpof=true&sd=true      

### Final Project for Course (курсовая работа)   
----------------------------------------------    
**Presentation Day:**  
- For group 5130203/20101:  
  * day 01: 21.12.2024 at 14:00 - 16:40 pm; room: 11k-324   
  * day 02: 14.01.2025 at 14:00 - 17:00 pm; room: 11k-324   
- For group 5130203/20102:   
  * day 01: 21.12.2024 at 10:00 - 12:40 pm; room: 11k-324   
  * day 02: 14.01.2025 at 11:00 - 14:00 pm; room: 11k-324   
   
**Task Definition:**   
* For the completion of the final course project, the students will organize in groups of 4 students, which each one will play one or more of the next roles:  
  - Project Manager: responsible for structure the project, the definition of the use-case problem and what technologies used for system development (frameworks, libraries, databases, models, etc.), and redaction of the final report;  
  - Software Engineer - Frontend: responsible for design the frontend development and validation of aplication;  
  - Software Engineer - Backend: responsible for integration of frontend with backend and database;   
  - Machine Learning Engineer: responsible for machine learning operations (dataset loading, preprocessing, design of model architecture, training, testing, validation, inference process and ai-model deployement)  

* The students will need select one specific use case with their respective dataset (financial, medical, comercial, educational, industrial, etc.) and fix this problem through the implementation of a small intelligent information system that contains frontend, backend, small database and AI-model. In the session of exams (сессия по зкзамене) each group will make presentation (доклад) of the next products:   
  - report between 4-8 pages (Responsible: Project Manager) in format of paper following the structure: 1- Problem Statement; 2- Methodology of Solution; 3- Results; 4- Conclusions;   
  - information system (Responsible: Software Engineers) which contains frontend, and backend with connection with small database;   
  - trained AI-model (Responsible: Machine Learning Engineer) with jupyter notebook source code, experiments of inference and performance results.  
  
* In MLOps is necessary make benchmark of 2 ML/DL models and compare the performance using the metrics related with the task (regression or classification).  
* In System development you will deploy just the best model to work integrated with system.  

**Instructions for presentation:**   

The project of end semester (курсовая работа) will split in 2 parts:  
     
   **Part 01: MLOps**  
   - Jupyter Notebook file with pipeline of task solution, benchmarks of metrics (min 2 models need compare) and inference using weights and biases of model (file will store in .pt, .pth, .pkl, .pickle, etc...)   
   - Report between 4-8 pages in format of paper *in english language* following the structure: 1- Problem Statement; 2- Methodology of Solution; 3- Results; 4- Conclusions;  
   - Group presentation (All members must be present): score is individual, depending of comprehension of your task, the solution and answers to professor questions   
   - Comments: is not necessary make slides. Jupyter notebook + Report is enough  
       
   **Part 02: System Development**   
   - Integrated system with ML model + frontend + backend + small database   
   - Group presentation (All members must be present): score is collective, expose system running with web interface and explain the components of system and explain the technologies used   
   - Comments: is not necessary make slides. Running system + source code published in GitHub repo of project manager is enough   


### Lesson 08 - Deep Learning IV: Multimodal Intelligent System  
----------------------------------------------------------------   
**Topics:**   
  
1) Visual Encoder-Decoder ViT + GPT-2 Architecture   
2) **Laboratory**: Case of study - Multimodal Intelligent System for generating captions from uploaded images  
3) Repo of project: https://github.com/HoltechHard/CaptionGeneratorApp  

**News:**  
1) Each group need define the next aspects of project (for next week):  
   - name of topic  
   - what dataset will use for MLOps  
   - list of technologies used to implement MLOps and System Development     
   
### Lesson 07 - Deep Learning III: Computer Vision   
--------------------------------------------------
**Topics:**  

1) Deep Neural Nets applied for multiclassification of images  
2) Convolutional Neural Networks (CNN)
3) Vision Transformer (ViT)  
  
### Lesson 06 - Deep Learning II: Building and Training Deep Neural Nets with Pytorch   
---------------------------------------------------------------------------------------    
**Topics:**  

1) Introduction of Pytorch
2) Deep Neural Nets applied to Regression Problem
3) Deep Neural Nets applied to Classification Problem
4) **Laboratory:** Case of study - prediction of fuel consumption with dim = [398 x 8]; and breast cancer classification with dim = [569 x 32]  
  
**Homework (from 27.11 until 08.12):**   
1) Report about Neural Networks as paradigm to simulate human intelligence  
   - Working individually, read the article "**The Nobel Prize in Physics 2024 - Geoffrey Hinton & John Hopfield**"  
     link: https://www.nobelprize.org/prizes/physics/2024/popular-information/   
   - Watch the interview to Geoffrey Hinton did by Royal Institute of UK, titled: "**On working with Ilya Sutskever, choosing problems, and the power of intuition**"  
     link: https://www.youtube.com/watch?v=n4IQOBka8bc   
   - Make a pdf report (1 page) answering the next questions:    
       a) What led Geoffrey Hinton to believe in neural networks as the right path to understanding and simulating human intelligence?   
       b) How physics fundamentals help Geoffrey Hinton to obtain the necessary insights to develop his research and discoveries related with Neural Nets?   
    
### Lesson 05 - Deep Learning I: Neural Networks  
---------------------------------------------------  
**Topics:**  
   
1) Perceptron  
2) Logistic Regression  
3) Multilayer Perceptron
4) **Laboratory:** Case of study - implementation from scratch of internal math mechanisms of neural nets and train/testing it on known datasets

**Homework (from 07.11 until 01.12):**  
1) Report about Neural Networks  
   - Working individually, make a pdf report (maximum 3 pages, 1 page for each model) with the mathematical formulation of algorithms **Perceptron**, **Logistic Regression** and **Multilayer Perceptron**  
   - The report need contains the next points for both algorithms:  
      * draw of model architecture  
      * vector representation of data (inputs and outputs)  
      * math formulation of linear combination, activation function and loss function
      * math formulation of how neural nets calculate the predictions (y_hat)  
      * explanation of gradient descendent algorithm      
      * formulas of gradients and weights/biases updates  
  
2) Experiments with Neural Networks  
   - Working in your team of 4-5 students (groups of курсовая работа), choose 1 dataset for linear separable problem for perceptron and 1 dataset for non-linear separable problem for multilayer perceptron and follow the pipeline to solve a CLASSIFICATION PROBLEM (could be binary or multiclass). If you want, you can generate data synthetically using Python math functions, but make sure that the data set will follow a linear pattern to be able to use the perceptron and a non-linear pattern to use the MLP.  
   - Use the algorithms in files **lesson05/scripts/perceptron.py** for perceptron and **lesson05/scripts/mlp.py** for MLP like class templates to build your neural networks architectures, train and test the models. You can adapt these codes according your needs. Don't use frameworks like pytorch or tensorflow yet.   
   - Use the necessary scripts of folder **lesson04/scripts** to build your confusion matrix and calculate the metrics of classification: accuracy, precision, recall, specificity and f1-score for your classification problem applying your datasets.      
   - The project manager (leader of group) need publish the project in Github. Professor will revise the Github repo just from project manager. You need present your jupyter notebook with all your results together with your python scripts used in your project.  
   
### Lesson 04 - Machine Learning II: Classification  
---------------------------------------------------  
**Topics:**   
  
1) Math definition of classification problem
2) Loss functions and evaluation metrics for classifiers
3) K-Nearest Neighboors
4) Support Vector Machines
5) Decision Trees and Ensemble Models based on trees
6) **Laboratory:** Case of study - classification model to predict predict score assignation based on US financial DB of customers; dim = [100000 x 27]  

**Homework (from 30.10 until 10.11):**    
1) Choose 1 machine learning task: REGRESSION or CLASSIFICATION;  
2) Take as template the jupyter notebook **lesson03/lab03.ipynb** for REGRESSION PROBLEM or the notebook **lesson04/lab04.ipynb** for CLASSIFICATION PROBLEM and their support python scripts, following the steps described and adapting to your choosed problem and dataset;  
3) Select one dataset with tabular data structure, which contains numerical and categorical type of data (need both necessarily). Dataset need have minimum 500 rows and number of columns (features) min = 6 and max = 50. You can use your own datasets from your past projects, your company or take one of the public datasets in the most popular repositories UCI (https://archive.ics.uci.edu/datasets); Kaggle (https://www.kaggle.com/datasets) or Google Dataset Search (https://datasetsearch.research.google.com). Your dataset can have format of file like .csv, .xls, .json, .sql, .data, .txt ... etc;  
4) In your team of 4-5 students (groups of курсовая работа), support your ML Engineers, apply the entire pipeline of supervised learning and get as result a benchmark of metrics evaluating the quality of your model applied to your task choosing 3 algorithms to compare in your benchmark. OBS: members of team must reach a consensus on choosing 1 single problem and 1 dataset to all team work;  
5) The professor will revise and analyze just the repository of Project Manager, which have the responsability of master coordination of the group and publish final results of homework coordinating with team. 
    
### Lesson 03 - Machine Learning I: Regression  
----------------------------------------------  
**Topics:**
  
1) Pipeline methodology of Machine Learning for supervised learning problems
2) Mathematical definition of Regression Problem
3) True risk, empirical risk and loss functions for regression problem
4) XGBoost Regressor architecture
5) LightGBM Regressor architecture
6) **Laboratory:** Case of study - regression model to predict Melborne (AUS) Housing Prices; dim = [34857 x 21]  
  
### Lesson 02 - Fundamentals of Machine Learning and Statistical Learning  
--------------------------------------------------------------------------  
**Topics:**
  
1) Definition of Learning in computer science point of view
2) Definition and fundamentals of ML
3) Supervised Learning and Unsupervised Learning
4) Generalization bounds and Statistical Learning Theory
5) Underfitting and Overfitting problems
6) **Laboratory:** Case of study - statistical analysis of numerical and categorical variables in US census salary income dataset; dim = [32561 x 15]   
  
**Homework (from 26.09 until 09.10):**    
  
1) Project of Statistical Analysis for tabular data
   - Take as template the jupyter notebook **lesson02/lab02.ipynb** worked in laboratory to make Statistical Analysis for Numerical and Categorical features;
   - Select one dataset with tabular data structure, which contains numerical and categorical type of data (need both necessarily). Dataset need have minimum 500 rows and number of columns (features) min = 6 and max = 50. You can use your own datasets from your past projects, your company or take one of the public datasets in the most popular repositories UCI (https://archive.ics.uci.edu/datasets); Kaggle (https://www.kaggle.com/datasets) or Google Dataset Search (https://datasetsearch.research.google.com). Your dataset can have format of file like .csv, .xls, .json, .sql, .data, .txt ... etc;  
   - Publish your own statistical analysis project in Github repo. Need have 1 folder which contains the dataset files and 1 jupyter notebook file .ipynb, which contains the python source code;  
   - Define the Metadata, Load the dataset as dataframe and take care the missing values;  
   - Make Descriptive Statistical Analysis for Numerical Variables: plot histogram of frequencies, histogram of densities, box plot, calculate the statistical metrics, plot the correlation table of numerical features and detect outliers;  
   - Make Descriptive Statistical Analysis for Categorical Variables: plot bar chart with absolute frequencies for each instance using all categorical variables, plot the pie chart with relative frequencies for each instance using all categorical variables;  
   - Make Descriptive Statistical Analysis for Groups of Categorical Variables: choose 2 categorical variables of your dataset. Create groups using the instances of these 2 categories and count the number of samples for each of these combined instances. Plot the grouped absolute frequencies using bar chart and grouped relative frequencies using pie chart.
   - Using the Markdowns of jupyter after each drawn diagram, make a commentary in short words about the interpretation of this plot.
  
2) Report about Statistical Learning Theory (SLT)  
   - Read the paper titled **Statistical Learning Theory: Models, Concepts, and Results (von Luxburg, Scholkopf)** the topics 1, 2.1, 2.2 in google drive repository;  
   - Link of paper: https://drive.google.com/file/d/1ZBTLqKeAUFw5rPBX_9tHAv06gQbhyohe/view?usp=drive_link  
   - Make report of 1 page in pdf format (publish it in GitHub) explaining the problem of binary classification (in formal math way). Answer the question: How SLT offer math basic framework to solve the problem of binary classification in Machine Learning?  

### Lesson 01 - Introduction to the fundamentals of AI    
-------------------------------------------------------  
**Topics:**  
  
1) Basic concepts of SW + Data and AI algorithms integration  
2) Research fields of AI  
3) AI Ecossystem  
4) Introductory concepts of Machine Learning and Deep Learning  
5) Notions of Transformers, Attention Mechanism and LLM  
  
**Homework (from 13.09 until 20.09):**    
  
1) Analyze the slides in the file conference-ai-11-09-2024.pdf and do some more research by your own about the topics covered in the week 01. In a brief 1-page summary (in English pdf format and individually), comment on what you understood from the first class and select from the list of AI subfields described in slide 5, the topic which you think it's the most interesting for you and what previous knowledge and experience you have with this topic and expectations that you have related to what you will learn in our course.  
2) Define groups of 4 students and the roles that each student will play in the final project. Send the group list to Farida (leader of the group 20101) and Kristina (leader of the group 20102). **Still it's not necessary to define the project topic, this will define around week 9-10**.
    
### Organization of the Lectures  
---------------------------------    
- First 10 lectures (related with theory and labs): Will be seletect 5 specialized AI and ML topics from document **list_topics.txt** distributed and discussed in 2 weeks with theory and practice in both;  
- Last 3 lectures (related with final project): Laboratories about software implementation and integration of information system with AI-models.  
  
  
