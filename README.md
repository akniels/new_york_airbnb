
# Predictive Analytics with Airbnb Data

This contains the raw code that was used for an explanation for a Medium Article explaining the data science process. The analysis looks at coorelations found within the data, shows the process of cleaning the data, and highlights the iterative process in data science. 

# Blog Post

https://datasciencetipsandtricks.com/?p=1

# New York Air BnB

Machine learning can be applied to almost any set of data. [Kaggle](https://www.kaggle.com/) is a great resource get free data sources to apply machine learning. This file takes data source from Air bnb in new york and uses predictive analytics to determine the price range of the apartment based on the data. The full data science is showcsed including the data engineering and data cleansing portion.

The motivation behind this project was to show the process of machine learning from start to finish. Raw data can be found just about anywhere and machine learning can predict just close to everything. Pricing is something that most companies are working diligintly to understand and predict. Predicting price for the Airbnb data shows the value in machine learning

The first portion reads in the data and then looks at the null count. It then highlights the strategies used to take care of the null values. After the null values are taken care of the outliers are removed and the numerical data is normalized (changed to values between 0 and 1). Dummy variables are then created for all data fields that are categorical. The distribution of the dependant variable is shown and then changed into a categorical price broken into 5 buckets based on the normalized data. Basic linear regressions are shown and highlight that more variables result in a higher score for the normal price prediction. Correlations are analyzed and highlighted, and predictions are made based off the highest correalted items. However, the best model contains all of the data points. A greidsearch is created to see if there are better models and then a squential Tenserflow is highlighted. Out of all the models, the Tensorflow sequential models shows shows the best results.

#### Libraries Used
* Scipy
* Numpy
* Matplotlib
* Sklearn
* Pandas

### Acknowledgements
Some of the functions found in the Udacity Data Science Nanodegree prorgram were used
* [Data Science Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025)
Teras functions were modeled after what was shown in this course
* [Keras with Tensorflow Course](https://www.youtube.com/watch?v=qFJeN9V1ZsI)
Grid search was modeled various sources
* https://medium.com/@erikgreenj/k-neighbors-classifier-with-gridsearchcv-basics-3c445ddeb657
* https://stats.stackexchange.com/questions/431022/error-while-performing-multiclass-classification-using-gridsearch-cv
* https://stackoverflow.com/questions/52580023/how-to-get-the-best-estimator-parameters-out-from-pipelined-gridsearch-and-cro
Outlier analysis was modeled after the following code
* https://www.kite.com/python/answers/how-to-remove-outliers-from-a-pandas-dataframe-in-python
* https://machinelearningmastery.com/model-based-outlier-detection-and-removal-in-python/

