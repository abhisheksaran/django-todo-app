# Ansible configuration
- The main config ansible config file it present in home directory 
    > ~/.ansible-config 
- The config file mentions the default inventory file to be used 
- Inventory file contains the config info regarding hosts to be connected
 
# Commands
- to run a playbook 
    ```
    ansible-playbook helloworld.yml
    ```
- you can allow cutom host file with -i option 
    ```
    ansible-playbook helloworld.yml -i customhostfile
    ```
    By default it takes the inventory file in ~/.ansible directory.
- to run it with a module 
    ```
    ansible-playbook file-name.yml -m ping

# Examples
- We have helloworld.yml which just uses shell module to echo the helloworld. We store the output using ***register*** keyword in variable ***output*** and print the output on stdout using the output varaible. We can also specify the name of task using ***name*** keyword.
- Another example find files in the directory specified by path. You can further provide options such as file types and patterns to find particular files. 