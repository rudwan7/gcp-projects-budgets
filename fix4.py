import csv
import subprocess

# Path to the CSV file
csv_file_path = 'data.csv'

# Read the CSV file
with open(csv_file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    # Iterate through each row in the CSV
    for row in csv_reader:
        print(row)
        project_id = row['project_id']
        project_quota = row['project_quota']
        # Construct the shell command
        #shell_command = f"rate_project {project_id} {quota}"
        shell_command = f"gcloud beta billing budgets create --budget-amount=20 --billing-account=01BEE5-28ED9C-97FE34 --display-name=budget6 --filter-projects=project/mysql-1-372704"

        
        # Execute the shell command
        try:
            result = subprocess.run(shell_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Output for {project_id}: {result.stdout.decode('utf-8')}")
        except subprocess.CalledProcessError as e:
            print(f"Error for {project_id}: {e.stderr.decode('utf-8')}")
