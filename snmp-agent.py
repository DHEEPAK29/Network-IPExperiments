import pyagentx3

class CustomDataUpdater(pyagentx3.Updater):
    def update(self):
        # Set a custom integer value at a specific OID
        self.set_INTEGER('1.0', 42) 
        self.set_OCTETSTRING('2.0', 'Miniature Python Agent Status: OK')

class MyMiniAgent(pyagentx3.Agent):
    def setup(self):
        # Register the updater for a specific MIB subtree
        self.register('1.3.6.1.4.1.8072.9999', CustomDataUpdater)

# To run, ensure your system snmpd is configured as an AgentX master
a = MyMiniAgent()
a.start()
