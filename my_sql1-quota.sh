

 gcloud beta billing budgets create --billing-account=01BEE5-28ED9C-97FE34 \
            --display-name="my-sql-project_quota" --budget-amount=20USD \
            --threshold-rule=percent=0.50 \
            --threshold-rule=percent=0.75,basis=forecasted-spend