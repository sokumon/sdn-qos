# To implement qos without controller

- start the topology in mininet
```
sudo mn --custom simple.py --topo mytopo --controller=none
```

- Go and remove the reference controller  with ovs-vsctl 

- add flows
For s1
```
sh ovs-ofctl add-flows s1 flows.txt
```

For s2
```
sh ovs-ofctl add-flows s2 flows_s2.txt
```
- Add queue
```
sh ovs-vsctl set port s1-eth4 qos=@newqos -- --id=@newqos create Qos type=linux-htb queues:123=@q0 queues:234=@q1 queues:345=@q2 -- --id=@q0 create Queue other-config:priority=1 other-config:max-rate=50000000 -- --id=@q1 create Queue other-config:priority=2 other-config:max-rate=25000000 -- --id=@q2 create Queue other-config:priority=3 other-config:max-rate=25000000
```

