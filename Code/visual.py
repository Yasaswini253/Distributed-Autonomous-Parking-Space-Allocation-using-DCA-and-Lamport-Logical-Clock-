from flask import Flask, render_template_string, redirect

app = Flask(__name__)

MAX_CAPACITY = 4

def get_slots():
    try:
        with open("slots.txt", "r") as f:
            return list(map(int, f.read().split(",")))
    except:
        return [0,0,0]

def save_slots(slots):
    with open("slots.txt", "w") as f:
        f.write(",".join(map(str, slots)))

@app.route('/add/<int:i>')
def add(i):
    slots = get_slots()
    if slots[i] < MAX_CAPACITY:
        slots[i] += 1
    save_slots(slots)
    return redirect('/')

@app.route('/remove/<int:i>')
def remove(i):
    slots = get_slots()
    if slots[i] > 0:
        slots[i] -= 1
    save_slots(slots)
    return redirect('/')

HTML = """
<!DOCTYPE html>
<html>
<head>
<style>
body {background:#111;color:white;text-align:center;font-family:Arial;}
.container {display:flex;justify-content:center;gap:40px;margin-top:40px;}
.slot {width:180px;height:240px;border-radius:10px;padding:10px;}
.free {background:#2ecc71;}
.full {background:#e74c3c;}
.car {font-size:25px;}
button {margin:5px;padding:5px;}
</style>
</head>

<body>
<h1>🚗 Smart Parking System</h1>

<div class="container">
{% for i in range(3) %}
<div class="slot {{ 'full' if slots[i]==4 else 'free' }}">
<h3>Slot {{i+1}}</h3>

<div>
{% for j in range(slots[i]) %}
<span class="car">🚗</span>
{% endfor %}
</div>

<p>{{slots[i]}} / 4</p>

<a href="/add/{{i}}"><button>Add</button></a>
<a href="/remove/{{i}}"><button>Remove</button></a>
</div>
{% endfor %}
</div>

<meta http-equiv="refresh" content="2">
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML, slots=get_slots())

app.run(host='0.0.0.0', port=5000)