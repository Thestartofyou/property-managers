class Property:
    def __init__(self, address, tenants):
        self.address = address
        self.tenants = tenants

class PropertyManager:
    def __init__(self, properties):
        self.properties = properties
    
    def add_property(self, property):
        self.properties.append(property)
    
    def remove_property(self, property):
        self.properties.remove(property)
    
    def get_property(self, address):
        for property in self.properties:
            if property.address == address:
                return property
    
    def get_all_properties(self):
        return self.properties
    
    def get_all_tenants(self):
        tenants = []
        for property in self.properties:
            tenants.extend(property.tenants)
        return tenants

# Sample usage
if __name__ == "__main__":
    p1 = Property("123 Main St", ["John Doe", "Jane Doe"])
    p2 = Property("456 Oak St", ["Bob Smith"])
    properties = [p1, p2]
    pm = PropertyManager(properties)
    
    pm.add_property(Property("789 Pine St", ["Alice Johnson"]))
    
    pm.remove_property(p2)
    
    print(pm.get_property("123 Main St").tenants)
    
    print(pm.get_all_properties())
    
    print(pm.get_all_tenants())
