class OSPFNeighbor:
    def __init__(self, router_id):
        self.router_id = router_id
        # States: Down, Init, 2-Way, ExStart, Exchange, Loading, Full
        self.state = "Down"

    def handle_hello(self):
        if self.state == "Down":
            self.state = "Init"
            print(f"Neighbor {self.router_id} is now Init")
        elif self.state == "Init":
            self.state = "2-Way"
            print(f"Neighbor {self.router_id} reached 2-Way (Bidirectional)")

# Simulation of a neighbor relationship
neighbor = OSPFNeighbor("10.0.0.1")
neighbor.handle_hello()
neighbor.handle_hello()
