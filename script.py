import requests
import webbrowser
#Retrieve text information from endpoints
e1 = requests.get('https://assess.cyber-fasttrack.org/challenge-files/clock-pt1?verify=qq%2BPCsoF%2F2V77cHg67%2FP1A%3D%3D')
e2 = requests.get('https://assess.cyber-fasttrack.org/challenge-files/clock-pt2?verify=qq%2BPCsoF%2F2V77cHg67%2FP1A%3D%3D')
e3 = requests.get('https://assess.cyber-fasttrack.org/challenge-files/clock-pt3?verify=qq%2BPCsoF%2F2V77cHg67%2FP1A%3D%3D')
e4 = requests.get('https://assess.cyber-fasttrack.org/challenge-files/clock-pt4?verify=qq%2BPCsoF%2F2V77cHg67%2FP1A%3D%3D')
e5 = requests.get('https://assess.cyber-fasttrack.org/challenge-files/clock-pt5?verify=qq%2BPCsoF%2F2V77cHg67%2FP1A%3D%3D')

#Collect text information from endpoints
secretKey = (e1.text + e2.text + e3.text + e4.text + e5.text)

#Open a url in browser
final = ('https://assess.cyber-fasttrack.org/challenge-files/get-flag?verify=qq%2BPCsoF%2F2V77cHg67%2FP1A%3D%3D&string='+secretKey)
webbrowser.open_new_tab(final)