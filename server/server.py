
from flask import Flask, request, jsonify
from OSC import OSCClient, OSCMessage
import time

app = Flask(__name__)

# MDCX Configuration
MDCX_HOST = "127.0.0.1"
MDCX_OSC_PORT = 7475

# Setup OSC client
mdcx_osc = OSCClient()
mdcx_osc.connect((MDCX_HOST, MDCX_OSC_PORT))

def oscsender(obj, topic, msg):
    try:
        if msg is None:
            obj.send(OSCMessage(topic))
            print("OSC LOG: TOPIC" + topic)
        else:
            obj.send(OSCMessage(topic, msg))
            print("OSC LOG: TOPIC " + topic + 
                  " MSG " + msg)
    except Exception as e:
        print("OSC ERROR - failed to send! " + e)

@app.route('/preset', methods=['GET'])
def send_preset():
    q = request.args.get('preset')
    if not q:
        return jsonify({"error": "Missing required query parameter 'q'"}), 400

    topic = "/mdc_layer1_" + q
    
    oscsender(mdcx_osc, topic, 1.0)
    
    # Optional delay or follow-up message
    time.sleep(1)  # Adjust/remove if not needed
    # oscsender(mdcx_osc, "/another_topic", 1.0)

    return jsonify({"status": "sent", "topic": topic})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
