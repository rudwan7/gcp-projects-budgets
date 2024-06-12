#!/bin/bash

# Set variables
project_id_ID="your-project_id-id"
BUDGET_ID="your-budget-id"
BILLING_ACCOUNT_ID="your-billing-account-id"

# Create the budget
gcloud beta billing budgets create $BUDGET_ID \
    --billing-account=$BILLING_ACCOUNT_ID \
    --project_id=$project_id_ID \
    --display-name="Budget for $project_id_ID" \
    --amount=1000 \
    --currency=USD \
    --threshold-rule=spend-amount \
    --threshold-percent=100

# Verify the budget
gcloud beta billing budgets describe $BUDGET_ID


gcloud beta billing budgets create --billing-account=BILLING_ACCOUNT --display-name=DISPLAY_NAME (--budget-amount=BUDGET_AMOUNT | --last-period-amount) [optional flags]

gcloud beta billing budgets create --billing-account=YOUR_BILLING_ACCOUNT_ID --display-name="My Budget" --budget-amount=100.00 --threshold-rule=0.50 --threshold-rule=0.90 --threshold-rule=1.00
gcloud beta billing budgets create --billing-account=01BEE5-28ED9C-97FE34 --display-name="My-sql-project_quota" --budget-amount=20.00 --threshold-rule=0.50 --threshold-rule=0.90 --threshold-rule=1.00
gcloud beta billing budgets create --billing-account=01BEE5-28ED9C-97FE34 --display-name="My-sql-project_quota" --budget-amount=20.00 --threshold-rule=[0.50] --threshold-rule=[0.90] --threshold-rule=[1.00]
gcloud beta billing budgets create --billing-account=01BEE5-28ED9C-97FE34 --display-name="My-sql-project_quota" --budget-amount=20.00 --threshold-rule=0.50 --threshold-rule=0.90 --threshold-rule=1.00
gcloud beta billing budgets create --billing-account=01BEE5-28ED9C-97FE34 --display-name="My-sql-project_quota" --budget-amount=20.00 --threshold-rule=threshold-percent=0.50 --threshold-rule=threshold-percent=0.90 --threshold-rule=threshold-percent=1.00
gcloud beta billing budgets create --budget-amount=100.75USD --billing-account=01BEE5-28ED9C-97FE34 --display-name="BUDGET1"
gcloud beta billing budgets create --budget-amount=100 --billing-account=01BEE5-28ED9C-97FE34 --display-name=budget1*
gcloud beta billing budgets create --budget-amount=100 --billing-account=01BEE5-28ED9C-97FE34 --display-name=budget1 --filter-project_ids=mysql-1-372704 x
gcloud beta billing budgets create --budget-amount=100 --billing-account=01BEE5-28ED9C-97FE34 --display-name=budget1 --filter-project_ids=[FILTER_project_idS,...]
gcloud beta billing budgets create --budget-amount=100 --billing-account=01BEE5-28ED9C-97FE34 --display-name=budget1 --filter-project_ids=[mysql-1-372704,...]
gcp-project_quotas % gcloud beta billing budgets create --budget-amount=100 --billing-account=01BEE5-28ED9C-97FE34 --display-name=budget1 --project_id=mysql-1-372704
gcloud beta billing budgets create --budget-amount=20 --billing-account=01BEE5-28ED9C-97FE34 --display-name=budget1 --filter-projects=projects/mysql-1-372704

EXAMPLES
    To create a budget with the display name 'BUDGET1' in the amount of 100.75
    in the default currency ('USD'), to receive notifications when 50% of the
    current budget or 75% of the forecasted budget is spent in the account
    '123', run:



$ gcloud beta billing budgets create --billing-account=01BEE5-28ED9C-97FE34 \
            --display-name="my-sql-project_quota" --budget-amount=20USD \
            --threshold-rule=percent=0.50 \
            --threshold-rule=percent=0.75,basis=forecasted-spend

            chmod +x project_quota.sh

‌

command been used so far to get there

gcloud init

gcloud config list

gcloud project_ids list

“mysql-1-372704”

gcloud config set project_id mysql-1-372704

gcloud help -- project_id project_quota

gcloud components list

gcloud components install beta

gcloud billing project_ids --help

gcloud beta billing budgets create --help

gcloud beta billing budgets create --budget-amount=20 --billing-account=01BEE5-28ED9C-97FE34 --display-name=budget1
gcloud init
gcloud auth login
gcloud config list
gcloud auth list
gcloud project_ids list
gcloud auth activate-service-account
gcloud config set project_id
gcloud config set compute/region
gcloud config set compute/zone
