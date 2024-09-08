
# Exp 2 : Qos With Controller

## Linux HTB 


We start a some custom rest qos controller
```
ryu-manager ryu.app.rest_qos ryu.app.qos_simple_switch_13 ryu.app.rest_conf_switch
```

Start the mininet topology by 
```
sudo mn --custom topo.py --topo mytopo --controller remote --switch ovsk --mac
```

Do this for all switches in topo
```
sh ovs-vsctl set Bridge s1 protocols=OpenFlow13
sh ovs-vsctl set-manager ptcp:6632
```

So there is a tool called cmd_gen.py
```
python cmd_gen.py ovsdb
```

```
python cmd_gen.py qosqueue
```

In the prompt give linux-htb or linux-hfsc before that create a file for it