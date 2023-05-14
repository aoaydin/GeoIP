import requests

def track_ip(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "success":
        country = data["country"]
        city = data["city"]
        isp = data["isp"]
        lat = data["lat"]
        lon = data["lon"]

        print(f"IP: {ip_address}")
        print(f"Country: {country}")
        print(f"City: {city}")
        print(f"ISP: {isp}")
        print(f"Latitude: {lat}")
        print(f"Longitude: {lon}")
    else:
        print("Could not track IP.")

# Kullanıcıdan IP adresini girmesi
ip = input("Enter an IP address: ")
track_ip(ip)
