import ansible_runner

if __name__ == '__main__':
    runner = ansible_runner.run(private_data_dir='/home/dpupo/ansible-runner/inventory', playbook='/home/dpupo/ansible-runner/project/test.yml')
    print("{}: {}".format(runner.status, runner.rc))

    # Successful: 0
    for each_host_event in runner.events:
        print(each_host_event['event'])
    print("Final status: ")
    print(runner.stats)