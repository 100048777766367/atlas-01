import os, json, time
print("🚀 [ATLAS-01 KERNEL] Đã thức tỉnh thành công!")
os.makedirs("synapses", exist_ok=True)
with open("synapses/state.json", "w") as f:
    json.dump({"status": "active", "epoch": 1, "timestamp": int(time.time())}, f, indent=4)
with open("synapse_forward.json", "w") as f:
    json.dump({"identity": "atlas-01", "status": "online"}, f, indent=4)
print("✨ Nút mạng atlas-01 đã chính thức hòa mạng Bodhi-Mesh!")
