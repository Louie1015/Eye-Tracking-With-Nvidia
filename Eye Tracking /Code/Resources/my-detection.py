import jetson.inference
import jetson.utils

net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson.utils.videoSource("csi://0")
display = jetson.utils.videoOutput("display://0")

while display.IsStreaming():
	img= camera.Capture()
	detections = net.Detect(img)
	display.Render(img)
	display.SetStatus("Object Detection | Networks{:.0f} FPS".format(net.GetNetworkFPS()))
	