import subprocess

datacsv = """
project_id project_quota
firebasea 10
larrys-hacking-vm 20                    
ai-orojects 10                                        
clean-pilot-402718 10                            
fir-prj2-d3f88 20                                    
firebasea 20                                    
fourth-palisade-410722 20                       
larrys-hacking-vm 20                            
logging-gn573-bj547 20                                   
monitoring-101 20                                  
monitoring-dev-gn573-bj547 20                      
monitoring-nonprod-gn573-bj547 15              
monitoring-prod-gn573-bj547 20                    
mysql-1-372704 20                                         
obsidianplugin-394603 20                           
product-documentation-2-qk 20          
python-logging-test-381022 10                 
qk-pictures-c2f56 20                                                                        
qkdraft 20                                   
seenas-stuff 20                    
serious-fabric-413415 20           
sys-55316638511631812412670958 20  
uplifted-logic-369521 20         
vpc-host-dev-gn573-bj547 20       
vpc-host-nonprod-gn573-bj547 20    
vpc-host-prod-gn573-bj547 20
"""

def parse_datacsv(datacsv):
    # Split the data into lines and strip whitespace
    lines = [line.strip() for line in datacsv.strip().split('\n')]
    
    # Split each line by whitespace and create a list of tuples
    projects = [tuple(line.split()) for line in lines]
    return projects

def run_shell_commands(projects):
    # Skip the header row
    for project in projects[1:]:
        project_id, project_quota = project

        # Construct the shell command
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

# Parse the datacsv string
projects = parse_datacsv(datacsv)

# Run the function
run_shell_commands(projects)
