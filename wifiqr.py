import qrcode
import json
import logging
import os
from PIL import Image

class WiFiQR:
    def __init__(self):
        self.ssid = None
        self.password = None
        self.filename = None
        self.display_image = None
        self.config_file = "config.json"
        logging.basicConfig(level=logging.INFO)

    def main(self):
        os.system('clear')
        self.load_config()
        self.generate_qr()

    def load_config(self):
        logging.info("[+] Looking for config file to load.")
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as jsonfile:
                data = json.load(jsonfile)
                self.ssid = data["ssid"]
                self.password = data["password"]
                self.filename = data['filename']
                self.display_image = data['display_qr']
                logging.info("[+] Config loaded.")
        else:
            logging.info("[!] Config file is missing!, exiting.")
            exit()


    def generate_qr(self):
        logging.info("[+] Generating QR code.")
        # Data to encode within the QR code.
        input_data = f"WIFI:S:{self.ssid};T:WPA;P:{self.password};H:false;;"
        # Creating an instance of qrcode
        qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=5)
        qr.add_data(input_data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(self.filename)
        logging.info("[+] QR code generated.")

        if self.display_image:
            self.display_qr()

    def display_qr(self):
        im = Image.open(self.filename)
        im.show()

if __name__ == "__main__":
    wifiqr = WiFiQR()
    wifiqr.main()
