import requests

if __name__ == "__main__":
	host = "https://twinpines-9429794e.influxcloud.net:8086/write?db=house_data&u=xiaogu&p=123q456w"
	with open("result.influxdb") as file:
		text = ''
		count = 0
		for line in file:
			if count == 5000:
				response = requests.post(host, data=text.encode('utf-8'))
				print(response)
				text = ''
				count = 0
			count = count+1
			text += line
		response = requests.post(host, data=text.encode('utf-8'))
		print(response)

