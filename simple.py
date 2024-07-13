"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        leftHost_1 = self.addHost( 'h1' )
	leftHost_2 = self.addHost( 'h2' )
	leftHost_3 = self.addHost( 'h3' )
       	
	rightHost_1 = self.addHost( 'h4' )
 	rightHost_2 = self.addHost( 'h5' )
 	rightHost_3 = self.addHost( 'h6' )
        
	leftSwitch = self.addSwitch( 's1' )
        rightSwitch = self.addSwitch( 's2' )

        # Add links
        
	self.addLink( leftHost_1, leftSwitch )
	self.addLink( leftHost_2, leftSwitch )
	self.addLink( leftHost_3, leftSwitch )
        
       	self.addLink(rightHost_1 , rightSwitch )
	self.addLink(rightHost_2 , rightSwitch )
 	self.addLink(rightHost_3 , rightSwitch )
	
	self.addLink(leftSwitch,rightSwitch)

topos = { 'mytopo': ( lambda: MyTopo() ) }
