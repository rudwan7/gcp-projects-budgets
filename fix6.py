import subprocess

datacsv = """
            project_id project_quota
            firebasea 10
            larrys-hacking-vm 20
"""
            

def run_shell_commands(projects):
    # Skip the header row
    for project in projects[1:]:
        #print(project)
        project_id, project_quota = project

        # Construct the shell command
        #command = f" echo {project_id} {project_quota}"
        #command = f"gcloud beta billing budgets create --budget-amount=20 --billing-account=01BEE5-28ED9C-97FE34 --display-name=budget1 --filter-projects=projects/mysql-1-372704"
        #command = f"gcloud beta billing budgets create --budget-amount={project_quota} --billing-account=01BEE5-28ED9C-97FE34 --display-name=budget-{project_id} --filter-projects=projects/{project_id}"
        #command = f"gcloud beta billing budgets create --budget-amount={project_quota} --billing-account=01BEE5-28ED9C-97FE34 --display-name=budget-{project_id} --project={project_id}"
        #command = f"gcloud beta billing budgets create --budget-amount={project_quota} --billing-account=01BEE5-28ED9C-97FE34 --display-name=budget-{project_id}"
        command = f"gcloud beta billing budgets create --billing-account=01BEE5-28ED9C-97FE34 \
            --display-name=budget-{project_id} --budget-amount={project_quota} \
            --filter-projects=projects/{project_id}"
        try:
            # Execute the shell command
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # Print the command's output
            print(f"Output for {project_id}: {result.stdout.decode()}")
        except subprocess.CalledProcessError as e:
            print(f"Error for {project_id}: {e.stderr.decode()}")

# Run the function
run_shell_commands(projects)
