import socket
import threading
import time
import random

node_id = int(input("Enter Node ID: "))
port = 5000 + node_id

peers = [5001, 5002, 5003]

# ===== GLOBALS =====
clock = 0
requesting = False
replies = 0
request_time = 0
leader = None

MAX_CAPACITY = 4

# ===== FILE =====
def get_slots():
    try:
        with open("slots.txt","r") as f:
            return list(map(int,f.read().split(",")))
    except:
        return [0,0,0]

def save_slots(slots):
    with open("slots.txt","w") as f:
        f.write(",".join(map(str,slots)))

# ===== LAMPORT =====
def update_clock(t=None):
    global clock
    if t is None:
        clock += 1
    else:
        clock = max(clock, t) + 1

# ===== LEADER ELECTION (BULLY SIMPLIFIED) =====
def elect_leader():
    global leader
    leader = max([p-5000 for p in peers])
    print(f"\n👑 Leader elected: Node {leader}")

# ===== RECEIVE =====
def receive():
    global replies

    s = socket.socket()
    s.bind(('0.0.0.0',port))
    s.listen(5)

    while True:
        conn,_ = s.accept()
        msg = conn.recv(1024).decode().split(',')

        mtype = msg[0]
        t = int(msg[1])
        nid = int(msg[2])

        update_clock(t)

        if mtype == "REQUEST":
            send_reply(nid)

        elif mtype == "REPLY":
            replies += 1

        elif mtype == "COMMIT":
            print("\n✅ Commit confirmed by leader")

        elif mtype == "SNAPSHOT":
            print(f"\n📸 Snapshot: Slots={get_slots()} Clock={clock}")

        conn.close()

# ===== SEND =====
def send_reply(nid):
    try:
        s=socket.socket()
        s.connect(('127.0.0.1',5000+nid))
        s.send(f"REPLY,{clock},{node_id}".encode())
        s.close()
    except:
        pass

# ===== 2PC =====
def two_phase_commit():
    print("\n🟡 Phase 1: Prepare")
    time.sleep(1)
    print("🟢 Phase 2: Commit")

# ===== SNAPSHOT =====
def take_snapshot():
    print("\n📸 Taking Snapshot")
    for p in peers:
        if p != port:
            try:
                s=socket.socket()
                s.connect(('127.0.0.1',p))
                s.send(f"SNAPSHOT,{clock},{node_id}".encode())
                s.close()
            except:
                pass

# ===== REQUEST =====
def send_request():
    global requesting, replies, request_time

    update_clock()
    requesting = True
    replies = 0
    request_time = clock

    print(f"\n📡 Node {node_id} requesting parking (time={clock})")

    for p in peers:
        if p != port:
            try:
                s=socket.socket()
                s.connect(('127.0.0.1',p))
                s.send(f"REQUEST,{clock},{node_id}".encode())
                s.close()
            except:
                pass

    while replies < len(peers)-1:
        time.sleep(0.2)

    two_phase_commit()
    allocate_parking()
    requesting = False

# ===== ALLOCATE =====
def allocate_parking():
    slots = get_slots()

    for i in range(len(slots)):
        if slots[i] < MAX_CAPACITY:
            slots[i]+=1
            save_slots(slots)

            print(f"\n🚗 Node {node_id} parked in Slot {i+1}")
            print(f"📊 Slots: {slots}")

            threading.Thread(target=auto_release,args=(i,),daemon=True).start()
            return

    print("\n❌ FULL")

# ===== AUTO RELEASE =====
def auto_release(i):
    time.sleep(random.randint(5,10))
    slots = get_slots()

    if slots[i]>0:
        slots[i]-=1
        save_slots(slots)

        print(f"\n🚙 Car left Slot {i+1}")
        print(f"📊 Updated Slots: {slots}")

# ===== START =====
threading.Thread(target=receive,daemon=True).start()

elect_leader()

while True:
    cmd = input("\n1=Request Parking  2=Snapshot\n")

    if cmd == "1":
        send_request()
    elif cmd == "2":
        take_snapshot()