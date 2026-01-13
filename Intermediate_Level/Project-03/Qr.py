# QR Code Generator
# A comprehensive Python application for generating various types of QR codes

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, CircleModuleDrawer, SquareModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image
import os

class QRCodeGenerator:
    """
    A class to generate different types of QR codes with customization options.
    """
    
    def __init__(self):
        self.qr = qrcode.QRCode(
            version=1,  # Controls the size (1-40)
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
    
    def generate_basic_qr(self, data, filename="qr_basic.png"):
        """Generate a basic QR code"""
        self.qr.clear()
        self.qr.add_data(data)
        self.qr.make(fit=True)
        
        img = self.qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        print(f"✓ Basic QR code saved as {filename}")
        return img
    
    def generate_colored_qr(self, data, fill_color="blue", back_color="yellow", 
                           filename="qr_colored.png"):
        """Generate a colored QR code"""
        self.qr.clear()
        self.qr.add_data(data)
        self.qr.make(fit=True)
        
        img = self.qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(filename)
        print(f"✓ Colored QR code saved as {filename}")
        return img
    
    def generate_styled_qr(self, data, style="rounded", color="black", 
                          filename="qr_styled.png"):
        """Generate a styled QR code with different module shapes"""
        self.qr.clear()
        self.qr.add_data(data)
        self.qr.make(fit=True)
        
        # Choose style
        module_drawer = {
            "rounded": RoundedModuleDrawer(),
            "circle": CircleModuleDrawer(),
            "square": SquareModuleDrawer()
        }.get(style, SquareModuleDrawer())
        
        img = self.qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=module_drawer,
            color_mask=SolidFillColorMask(front_color=color)
        )
        img.save(filename)
        print(f"✓ Styled QR code saved as {filename}")
        return img
    
    def generate_qr_with_logo(self, data, logo_path, filename="qr_with_logo.png"):
        """Generate a QR code with a logo in the center"""
        self.qr.clear()
        self.qr.add_data(data)
        self.qr.make(fit=True)
        
        # Create QR code image
        qr_img = self.qr.make_image(fill_color="black", back_color="white").convert('RGB')
        
        # Open and resize logo
        try:
            logo = Image.open(logo_path)
            
            # Calculate logo size (should be about 1/5 of QR code)
            qr_width, qr_height = qr_img.size
            logo_size = qr_width // 5
            
            # Resize logo
            logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
            
            # Calculate position to paste logo
            logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
            
            # Paste logo onto QR code
            qr_img.paste(logo, logo_pos)
            
            qr_img.save(filename)
            print(f"✓ QR code with logo saved as {filename}")
            return qr_img
        except FileNotFoundError:
            print(f"✗ Logo file not found: {logo_path}")
            return None
    
    def generate_wifi_qr(self, ssid, password, security="WPA", hidden=False, 
                        filename="qr_wifi.png"):
        """Generate a WiFi QR code"""
        # WiFi QR code format
        wifi_data = f"WIFI:T:{security};S:{ssid};P:{password};H:{'true' if hidden else 'false'};;"
        return self.generate_basic_qr(wifi_data, filename)
    
    def generate_vcard_qr(self, name, phone, email, organization="", 
                         filename="qr_vcard.png"):
        """Generate a vCard (contact) QR code"""
        vcard_data = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
ORG:{organization}
END:VCARD"""
        return self.generate_basic_qr(vcard_data, filename)
    
    def generate_url_qr(self, url, filename="qr_url.png"):
        """Generate a URL QR code"""
        return self.generate_basic_qr(url, filename)
    
    def generate_email_qr(self, email, subject="", body="", filename="qr_email.png"):
        """Generate an email QR code"""
        email_data = f"mailto:{email}?subject={subject}&body={body}"
        return self.generate_basic_qr(email_data, filename)
    
    def generate_sms_qr(self, phone, message="", filename="qr_sms.png"):
        """Generate an SMS QR code"""
        sms_data = f"SMSTO:{phone}:{message}"
        return self.generate_basic_qr(sms_data, filename)
    
    def batch_generate(self, data_list, prefix="qr_batch"):
        """Generate multiple QR codes from a list"""
        for idx, data in enumerate(data_list, 1):
            filename = f"{prefix}_{idx}.png"
            self.generate_basic_qr(data, filename)
        print(f"✓ Generated {len(data_list)} QR codes")


def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("    QR CODE GENERATOR - INTERMEDIATE PROJECT")
    print("="*50)
    print("\n1.  Generate Basic QR Code")
    print("2.  Generate Colored QR Code")
    print("3.  Generate Styled QR Code")
    print("4.  Generate QR Code with Logo")
    print("5.  Generate WiFi QR Code")
    print("6.  Generate vCard (Contact) QR Code")
    print("7.  Generate URL QR Code")
    print("8.  Generate Email QR Code")
    print("9.  Generate SMS QR Code")
    print("10. Batch Generate QR Codes")
    print("0.  Exit")
    print("="*50)


def main():
    """Main function to run the QR code generator"""
    generator = QRCodeGenerator()
    
    # Create output directory
    if not os.path.exists("qr_outputs"):
        os.makedirs("qr_outputs")
        print("✓ Created 'qr_outputs' directory")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (0-10): ").strip()
        
        if choice == "0":
            print("\nThank you for using QR Code Generator!")
            break
        
        elif choice == "1":
            data = input("Enter text/data for QR code: ")
            filename = input("Enter filename (default: qr_basic.png): ") or "qr_basic.png"
            generator.generate_basic_qr(data, f"qr_outputs/{filename}")
        
        elif choice == "2":
            data = input("Enter text/data: ")
            fill = input("Enter fill color (default: blue): ") or "blue"
            back = input("Enter background color (default: yellow): ") or "yellow"
            filename = input("Enter filename (default: qr_colored.png): ") or "qr_colored.png"
            generator.generate_colored_qr(data, fill, back, f"qr_outputs/{filename}")
        
        elif choice == "3":
            data = input("Enter text/data: ")
            print("\nStyles: rounded, circle, square")
            style = input("Enter style (default: rounded): ") or "rounded"
            color = input("Enter color (default: black): ") or "black"
            filename = input("Enter filename (default: qr_styled.png): ") or "qr_styled.png"
            generator.generate_styled_qr(data, style, color, f"qr_outputs/{filename}")
        
        elif choice == "4":
            data = input("Enter text/data: ")
            logo_path = input("Enter logo image path: ")
            filename = input("Enter filename (default: qr_with_logo.png): ") or "qr_with_logo.png"
            generator.generate_qr_with_logo(data, logo_path, f"qr_outputs/{filename}")
        
        elif choice == "5":
            ssid = input("Enter WiFi SSID: ")
            password = input("Enter WiFi Password: ")
            security = input("Enter Security (WPA/WEP/nopass, default: WPA): ") or "WPA"
            hidden = input("Is network hidden? (yes/no, default: no): ").lower() == "yes"
            filename = input("Enter filename (default: qr_wifi.png): ") or "qr_wifi.png"
            generator.generate_wifi_qr(ssid, password, security, hidden, f"qr_outputs/{filename}")
        
        elif choice == "6":
            name = input("Enter full name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            org = input("Enter organization (optional): ")
            filename = input("Enter filename (default: qr_vcard.png): ") or "qr_vcard.png"
            generator.generate_vcard_qr(name, phone, email, org, f"qr_outputs/{filename}")
        
        elif choice == "7":
            url = input("Enter URL: ")
            filename = input("Enter filename (default: qr_url.png): ") or "qr_url.png"
            generator.generate_url_qr(url, f"qr_outputs/{filename}")
        
        elif choice == "8":
            email = input("Enter email address: ")
            subject = input("Enter subject (optional): ")
            body = input("Enter body (optional): ")
            filename = input("Enter filename (default: qr_email.png): ") or "qr_email.png"
            generator.generate_email_qr(email, subject, body, f"qr_outputs/{filename}")
        
        elif choice == "9":
            phone = input("Enter phone number: ")
            message = input("Enter message (optional): ")
            filename = input("Enter filename (default: qr_sms.png): ") or "qr_sms.png"
            generator.generate_sms_qr(phone, message, f"qr_outputs/{filename}")
        
        elif choice == "10":
            print("\nEnter data items (one per line, empty line to finish):")
            data_list = []
            while True:
                item = input()
                if not item:
                    break
                data_list.append(item)
            
            if data_list:
                prefix = input("Enter filename prefix (default: qr_batch): ") or "qr_batch"
                generator.batch_generate(data_list, f"qr_outputs/{prefix}")
            else:
                print("No data entered!")
        
        else:
            print("Invalid choice! Please try again.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()