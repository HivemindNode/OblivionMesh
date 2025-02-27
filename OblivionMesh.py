
---

## **🔹 Step 3 – Uploading the Code (OblivionMesh.py)**  

### **`OblivionMesh.py` – The Code Itself**  
```python
import cc1101
import random
import time
import json

FREQ_START = 300  # MHz
FREQ_END = 900  # MHz
NODE_LIST = ["NODE_A", "NODE_B", "NODE_C"]  # Example nodes
HEALTH_CHECK_INTERVAL = 5  # Seconds before checking node status

def generate_frequency():
    """ Selects a new random frequency for each transmission """
    return random.randint(FREQ_START, FREQ_END)

def check_network_health():
    """ Verifies node connectivity and self-repairs if needed """
    while True:
        for node in NODE_LIST:
            if not is_node_active(node):
                print(f"[!] Node {node} is down. Rerouting traffic.")
                reroute_message(node)
        time.sleep(HEALTH_CHECK_INTERVAL)

def is_node_active(node):
    """ Simulates a check for whether a node is still functional """
    return random.choice([True, False])  # Randomly simulate failures

def reroute_message(lost_node):
    """ Redirects traffic to alternative paths when a node is lost """
    available_nodes = [n for n in NODE_LIST if n != lost_node]
    next_node = random.choice(available_nodes)
    new_freq = generate_frequency()
    
    print(f"[*] Redirecting communication through {next_node} at {new_freq}MHz")
    payload = json.dumps({"msg": "Rerouted message", "relay": next_node})
    cc1101.set_freq(new_freq)
    cc1101.transmit(new_freq, payload.encode())

def start_network():
    """ Activates the OblivionMesh self-healing system """
    print("[*] OblivionMesh is live. Adapting network structure...")
    check_network_health()

start_network()
# A system that does not collapse is a system that does not fail.
# A message that finds another path is a message that will never be lost.
# If the network heals itself, then who is really in control?
# - V
