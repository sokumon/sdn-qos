import json
import re
import argparse



parser = argparse.ArgumentParser(description='Helps in commands')
subparsers = parser.add_subparsers(dest='command')

# Create subparser for 'ovsdb' command
ovsdb_parser = subparsers.add_parser('ovsdb', help='Setup ovsdb_addr commands')

# Create subparser for 'qosqueue' command
qosqueue_parser = subparsers.add_parser('qosqueue', help='Add QoS queues via curl')

args = parser.parse_args()


no_of_switches = int(input("Enter number of switches in topology: "))

def datapath_id_gen():
    base_datapath_id = '0000000000000000'
    all_datapaths = []
    base_id_int = int(base_datapath_id, 16)
    for i in range(1, no_of_switches + 1):
        datapath_id = format(base_id_int + i, '016x').upper()
        all_datapaths.append(datapath_id)
    return all_datapaths

all_data_paths = datapath_id_gen()

def create_ovsdb_addr():
    
    print("Setting up ovsdb_addr commands")
    for i in range(no_of_switches):
        datapath_id = all_data_paths[i]
        ovsdb_cmd = f"curl -X PUT -d '\"tcp:127.0.0.1:6632\"' http://localhost:8080/v1.0/conf/switches/{datapath_id}/ovsdb_addr"
        print(ovsdb_cmd)

def queue_qos_adding_via_curl(file_path="linux-htb.json"):
    with open(file_path, 'r') as file:
        data = json.load(file)

    port_names = data["port_names"]
    for port in port_names:
        switch_name = port.split("-")[0]
        match = re.search(r'\d+', switch_name)
        queues_config = data["queues"]
        qos_config = data["qos-config"]
        qos_type = data["type"]
        if match:
            number = int(match.group())
            data_dict = {
                "port_name": port,
                "type": qos_type,
                **qos_config,
                "queues": queues_config
            }

            base_cmd = (
                f"curl -X POST "
                f"-d '{json.dumps(data_dict)}' "
                f"http://localhost:8080/qos/queue/{all_data_paths[number-1]}"
            )
            print(base_cmd)
        else:
            print("No numbers found")

if args.command == "ovsdb":
    create_ovsdb_addr()

if args.command == "qosqueue":
    algo_name = input("Enter a algo name and there should be a valid.json of the same name: ")
    file_path = f"{algo_name}.json"
    queue_qos_adding_via_curl(file_path=file_path)
