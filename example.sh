 gcloud beta billing budgets create --billing-account=01BEE5-28ED9C-97FE34 \
            --display-name=budget2 --budget-amount=20 \
            --threshold-rule=percent=0.50 \
            --threshold-rule=percent=0.75,basis=forecasted-spend
            --filter-projects=projects/mysql-1-372704
           




 gcloud beta billing budgets create --billing-account=01BEE5-28ED9C-97FE34 \
            --display-name=budget-{project_id} --budget-amount={project_quota} \
            --filter-projects=projects/{project_id}