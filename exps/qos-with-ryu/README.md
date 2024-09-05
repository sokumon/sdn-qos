
# Exp 2 : Qos With Controller

## Linux HTB 

We start a simple rest controller in another terminal

```
ryu-manager ryu.app.rest_qos ryu.app.qos_simple_switch ryu.app.rest_conf_switch
```

Start the mininet topology by 
```
sudo mn --custom topo.py --topo mytopo --controller remote --switch ovsk
```

## OVS Commands for qos