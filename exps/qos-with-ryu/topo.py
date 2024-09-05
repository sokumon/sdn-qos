from mininet.topo import Topo

class MyTopo(Topo):
    "Simple topology example."

    def build(self):
        "Create custom topo."

        # Add hosts and switches
        leftHost_1 = self.addHost('h1')
        leftHost_2 = self.addHost('h2')
        leftHost_3 = self.addHost('h3')
       
        rightHost_1 = self.addHost('h4')
        rightHost_2 = self.addHost('h5')
        rightHost_3 = self.addHost('h6')
        
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')


        # Add links
        self.addLink(leftHost_1, s1)
        self.addLink(leftHost_2, s1)
        self.addLink(leftHost_3, s1)

        
        self.addLink(rightHost_1, s3)
        self.addLink(rightHost_2, s3)
        self.addLink(rightHost_3, s3)

        self.addLink(s1,s2)
        self.addLink(s2,s5)
        self.addLink(s5,s3)
        self.addLink(s3,s4)
        self.addLink(s4,s1)

# Define the 'topos' dictionary correctly
topos = { 'mytopo': (lambda: MyTopo()) }
