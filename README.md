# SDAD
Streaming Data - Anomaly Detection

## Project Goal
Deliver a user interface with real time anomaly detection on time series data from various streaming sources (IoT sensors, social media, monitoring systems, market data, …). The input time series are expected to be multivariate and non stationary with more or less noise. 
The implementation will include an explainability module through anomaly clustering.
The project is challenging on three aspects: 
Multivariate, non-stationary time series as input data
Unbalanced data with little volume of anomalies
Unlabeled real life streaming data (Self Supervised approach)

## Datasets
NAB (https://numenta.com/machine-intelligence-technology/numenta-anomaly-benchmark/) offers a robust framework for anomaly detection research. It provides datasets (https://github.com/numenta/NAB ) that will be used for training the model. Its synthetic datasets are provided with various levels of noise and some real life datasets are provided with labeled data.
Real life streaming data provided  by the Singapore government will be used for model fine-tuning and model serving:
Streaming transport data API (https://data.gov.sg/dataset?q=&res_format=API&groups=transport ) 
Streaming Environmental data API (https://data.gov.sg/dataset?q=&res_format=API&groups=environment )


## Baseline 
NAB framework provides a leaderboard and benchmark models as a baseline (https://arxiv.org/pdf/1510.03336v4.pdf ).

## model architecture 
For the first iterations, the model architecture will be based on an auto-encoder model with a clustering of the reconstructed error outliers (i.e. anomalies). Later, the representation learning model is expected to evolve towards a transformer architecture.   

## Output
A web interface where users can visualise anomaly advanced analytics (e.g. clustering representation with factor analysis) on a selected source of streaming data.

## Stretch goal
Implement a self explainable neural network architecture for real time explainability on the detected anomalies.
