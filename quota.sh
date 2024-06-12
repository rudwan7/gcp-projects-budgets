#!/bin/bash

# Set variables
project_id_ID="mysql-1-372704"
BUDGET_ID="project_quota"
BILLING_ACCOUNT_ID="01BEE5-28ED9C-97FE34"

# Create the budget
gcloud beta billing budgets create $BUDGET_ID \
    --billing-account=$BILLING_ACCOUNT_ID \
    --project_id=$project_id_ID \
    --display-name="Budget for $project_id_ID" \
    --amount=20 \
    --currency=USD \
    --threshold-rule<=20\
    --threshold-percent=100
