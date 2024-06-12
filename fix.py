import csv
import subprocess

# Function to read CSV file
def read_csv(csv_file_path):
    projects = []
    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row)
            projects.append(row)
    return projects

# Function to execute shell commands
def execute_shell_command(project_id, project_quota):
    command = f"gcloud beta billing budgets create --billing-account=01BEE5-28ED9C-97FE34 \
                --display-name=budget-{project_id} --budget-amount={project_quota} \
                --filter-projects=projects/{project_id}"
    
    # Execute the command
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Command executed successfully for project {project_id}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the command for project {project_id}: {e}")

def main():
    # Path to the CSV file
    csv_file_path = 'projects.csv'
    
    # Read the CSV file
    projects = read_csv(csv_file_path)
    
    # Loop through each project and execute the shell command
    for project in projects:
        project_id = project['project_id']
        project_quota = project['project_quota']
        execute_shell_command(project_id, project_quota)

if __name__ == "__main__":
    main()
