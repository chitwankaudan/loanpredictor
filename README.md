# Lending Club Loan Predictor 
Lenders know that not everyone they loan money to will pay them back in full. That's why before you can recieve a loan banks look at your credit score, your credit history, outstanding balances, income, etc. to determine what type of risk you pose to the bank. In the past, we've seen that when these thresholds are relaxed too much, defaults skyrocket sometimes with disastrous implications on the economy (i.e. housing market crash & '08 crisis). So we know these thresholds banks impose help weed out bad risk.

But what about loans that pass all the thresholds? Of these loans, can we predict which loans will default and which won't? Is it true that lenders closer to the threshold cut offs tend default more often? With what accuracy can we make these predictions? Which metrics are the most important our predictions?

## Required Installations
The only installation needed to run this repo is Anaconda. Click here to learn about how to install Anaconda. Once installed, you should be good to go!

## Getting Started
You're in luck, this project is easily reproducible! To get started first download or clone this repo and cd into where you saved it. Make sure you are in a directory entitled "loanpredictor". Once there create an empty data directory using the following command:

```bash
mkdir data/
```
Once created, navigate to Lending Club's Statistics [site](https://www.lendingclub.com/info/download-data.action) and download loan data files into the data directory you just created. Feel free to downlad any or all loan data after 2011 in a csv format. (Note all other formats will be ignored, so all data is in a csv format)

Once your data is in the data/ directory, you're just a couple commands away completing the analysis. Switch back into the loanpredictor directory before moving on.

## Running the Analysis
First, create and activate your environment using the following commands:
```bash
make env
source activate loans
```

Then run process and clean you data:
```bash
make process
```

Finally run your predictions:
```bash
make predict
```
It will take a second to run but you should see an accuracy score, false negative and false positive rate printed out in your terminal. 

Feel free to customize the analysis anywhere you feel. You can change the number ofr folds used in setting.py or the variables in the model in assemble.py. All scripts are well annotated so you can directly play around with those. Also, feel free to checkout more detials about the project in the my analysis directory. 
