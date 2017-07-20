#!/bin/env python3
#
# dmenu-docker
#
# (c) 2017 - Daniel Jankowski


# imports
import os
import docker
import subprocess


'''
Get all docker containers from the docker api.
'''
def getDockerContainer():
    # connect to the docker api
    client = docker.from_env()

    # get a list of all containers
    containers = client.containers.list(all=True)

    # get a list of all running containers
    running_containers = client.containers.list()

    # return both values
    return containers, running_containers


'''
Start a docker container and its linked containers
'''
def startDockerContainer(selected_container, containers):
    # an array to save all links
    linked_containers = []

    # iterate throygh containers
    for container in containers:
        # if we found the selected container
        if selected_container == container.attrs['Name']:
            # save the container object..
            container_object = container

            # ...and its linked containers
            if container.attrs['HostConfig']['Links'] is not None:
                # iterate through the links
                for link in container.attrs['HostConfig']['Links']:
                    # save the name of the link
                    linked_containers.append(link.split(':')[0])

    # iterate throygh containers
    for container in containers:
        if container.attrs['Name'] in linked_containers:
            # start the linked containers
            container.start()

    # start the selected container
    container_object.start()


'''
Stop the selected docker container. Linked containers will run in order to
prevent breaking dependencies to other running containers.
'''
def stopDockerContainer(selected_container, containers):
    # iterate through all containers...
    for c in containers:
        # ...in order to find the selected one...
        if selected_container == c.attrs['Name']:
            # ...and stop it.
            c.stop()


'''
Show dmenu with the container names and return the selected result.
'''
def showDmenu(line):
    exec_path = os.path.realpath(__file__).rstrip('dmenu-docker.py')
    # build the command array with the dmenu.sh and the dmenu line we generated
    cmd = [exec_path + 'dmenu.sh', line]

    # start the process
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    # get the result through a pipe, ...
    result = process.communicate()

    # ...decode and return it
    return result[0].decode('utf-8')[:-1]


'''
Main function
'''
def main():
    # get all containers and all running containers
    containers, running_containers = getDockerContainer()

    # placeholder variables
    names = {}
    dmenu_line = ''
    
    # iterate through containers
    for container in containers:
        # check if the container is running
        if container in running_containers:
            # if it runs, save it in the names dict...
            names[container.attrs['Name']] = True

            # ...and add the name to the dmenu line
            dmenu_line += container.attrs['Name'] + ' [running]\n'
        else:
            # if the container is not running, save the state...
            names[container.attrs['Name']] = False

            # ...and add the name to the dmenu line
            dmenu_line += container.attrs['Name'] + '\n'

    # display dmenu and get the result
    selected_container = showDmenu(dmenu_line[:-1])

    # if no container is selected, just return
    if selected_container == '':
        return

    # check if the container is running
    if names[selected_container.rstrip(' [running]')]:
        # stop the container if its running
        stopDockerContainer(selected_container.rstrip(' [running]'), containers)
    else:
        # start the container if it is not running
        startDockerContainer(selected_container, containers)


# entry point
if __name__ == '__main__':
    main()
