from flask import Flask, send_from_directory, request
import time, re, base64

app = Flask(__name__)


@app.route('/<path:filename>', methods=['GET', 'POST'])
def share(filename):
   
   return send_from_directory('uploads', filename)

@app.route('/', methods=['GET','POST'])
def main():
	try:
		now = time.localtime()
		current_time = "%04d-%02d-%02d_%02d-%02d-%02d" % (now.tm_year, now.tm_mon, now.tm_mday,now.tm_hour, now.tm_min, now.tm_sec)
		client_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
		
		print(client_ip)
		
		title = request.form['title']
		title = re.subn('[\\\/\:\*\?\"\<\>\|]', "", title)[0]
		html = request.form['html']
		image = request.form['image']
		image = base64.b64decode( image.replace('data:image/octet-stream;base64,', '') )
		
		print(title)
		
		
		filename = "log/" + "[" + client_ip + "] " + title + " " + current_time + ".html"
		f = open(filename, 'a', encoding='utf-8')
		f.write(html)
		f.close()
		
		filename = "log/" + "[" + client_ip + "] " + title + " " + current_time + ".png"
		with open(filename, 'wb') as f:
			f.write(image)
		
		f.close()
		
	except:
		return ""
	return ""
   
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='1479',debug=True)
