#!/bin/bash

# Extract all _uuids from ovs-vsctl list qos
all_uuids=$(ovs-vsctl list qos | awk '/_uuid/{print $3}')

# Loop over each UUID
for uuid in $all_uuids; do
    echo "Processing QoS UUID: $uuid"
    ovs-vsctl destroy qos "$uuid"
    # Add your processing logic here, for example:
    # ovs-vsctl commands or any other operations
done

# Extract all _uuids from ovs-vsctl list queue
all_uuids_queues=$(ovs-vsctl list queue | awk '/_uuid/{print $3}')

# Loop over each UUID
for uuid in $all_uuids_queues; do
    echo "Processing Queue UUID: $uuid"
    ovs-vsctl destroy queue "$uuid"
    # Add your processing logic here, for example:
    # ovs-vsctl commands or any other operations
done

