from flask import Flask, Response, render_template
import cv2

app = Flask(__name__)

def gen_frames():
	# Replace with your RTSP URL (including username/password if applicable)
	#url = "rtsp://:8554/stream"
	#cap = cv2.VideoCapture(url)
	ip_address = "192.168.137.36"
	port = 8080
	src = f'tcp://{ip_address}:{port}'
	cap = cv2.VideoCapture(src)
	
	while True:
		ret, frame = cap.read()
		print("Frame captured successfully")
		if not ret:
			break
		# Convert frame to bytes for streaming
		ret, buffer = cv2.imencode('.jpg', frame)
		frame = buffer.tobytes()
		yield (b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
	cap.release()

@app.route('/video_feed')
def video_feed():
  return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
  """Video streaming home page."""
  return render_template('index.html')  # Using render_template here

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

