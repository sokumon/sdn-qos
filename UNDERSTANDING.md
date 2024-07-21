# Understanding and commands to operate openVswitch
this file is mostly personal reference
ovs-ofctl add-flow s1 action=normal
ovs-ofctl add-flow s2 action=normal

# Actually set controller to None
ovs-vsctl set-controller s1 
ovs-vsctl set-controller s2 

# QOS creation with Queue
-- --id=@newqos create Qos type=linux-htb queues:0=@q0 -- --id=@q0 create Queue other-config:min-rate=10
# queue creation 
ovs-vsctl -- --id=@q0 create Queue other-config:min-rate=10

#Adding flow manuyally 


### Use ofports to write flows
```
sh ovs-vsctl -- --columns=name,ofport list Interface
```

### To delete qos properly
```
sh ovs-vsctl clear Port s1-eth4 qos
```

```
sh ovs-vsctl -- --all destroy queue  -- --all destroy qos
```

## To add flows 
- Flows are probably about 2 things flow match + flow action
- Flows with same flow match are overwriiten 
