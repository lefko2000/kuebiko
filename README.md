# kuebiko - mansa data coding challenge

This is the repository for the Mansa Data Science Coding Challenge.

## Goal:

To test your ability to deal with time-series data, building a model, and serving a model using an API framework.


## Details:

You will find two `csv` files containing real anonymized data from transactions and accounts. The `transactions.csv` contains a set of transactions with an amount (in eur) and the date of the day they were added. The `accounts.csv` contains a list of balances for the accounts that the transactions pertain to. 

Provided with this repo is also a `main.py` file with a minimal [FastAPI](https://fastapi.tiangolo.com/) demo. Once you have installed the `requirements.txt` in your python environment you will be able to run the main file by simply calling `uvicorn main:app` inside your directory. This should start the local server and you should be able to see the automatically generated API docs at `http://127.0.0.1:8000/docs`. 

## The Task

Your task is to use this data to make a model capable of making predictions. This model should then be served through the small [FastAPI](https://fastapi.tiangolo.com/) file provided. Feel free to extend the or split the file as needed.

You have several options for the model to build:

### Option A: Predict the next month's income

Set up a prediction function that takes a list of transactions and an account and ouputs a prediction for the aggregated next monthly income. 

### Option B: Predict the next week's outgoing

Set up a prediction function that takes a list of transactions and an account and ouputs a prediction for the aggregated next weekly outgoing. 
    
### Option C: Detect outlier accounts

Set up a prediction function that takes a list of transactions and an account and returns a prediction of "closeness" to the rest of the accounts. This is a more open-ended question and we make no guarantees that the data provided does or does not already contain outliers. If you opt for building this model, we expect you to provide plots showing the outliers vs non-outliers.


### For all options:

The preprocessing/algorithms/loss functions are yours to decide, as well as the separation between train/validation/test set. 

Specific design choices must be justified, whether that be qualitatively through plots or quantitatively through metrics. We want you to show us how good is your solution.

Tip: By combining the transactions and accounts data you should be able to reverse the balance of the account back through time (back to the oldest transaction date for the account). This information might be useful depending on what you choose to predict.


## What we expect:

- Use of Python (3.6+)
- Clearly documented code or explanations with each function. **You need to be able to justify your design choices** - from data processing to algorithnm decisions.
- Use of the FastAPI format for routes and for serving your prediction model and use of pydantic/typing for input/output validation
- Unitesting where possible


You can use whatever other external software libraries you think are appropriate. Pandas/numpy/scikit-learn are encouraged! Please don't spend more than 4-6 hours on this test.

Your solution must be able to run and respond to requests. You can imagine it as a micro-service that could be run independently on a server. Additional notebooks, analysis or plots to accompany your model will be very welcomed!

We look forward to your solution 🙂

### Why kuebiko ?

Kuebiko is the japanese god of knowledge. Early on in our creation, we took to naming our "katas" or coding challenges after japanese mythology. 

We hope to challenge you as you will be challenged in your daily work at Mansa and so designed this test with this in mind. It is important to us to gather feedback on this process as well, and so please don't hesitate to let us know what you think!
