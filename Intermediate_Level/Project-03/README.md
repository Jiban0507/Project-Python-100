# QR Code Generator ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=yellow)

## 📋 Project Overview

A comprehensive Python application for generating various types of QR codes with customization options. This intermediate-level project demonstrates working with external libraries, image processing, and building a feature-rich CLI application.

## 🎯 Learning Objectives

- **Library Integration**: Work with external Python libraries (`qrcode`, `Pillow`)
- **Image Processing**: Manipulate and combine images programmatically
- **Object-Oriented Programming**: Design and implement classes
- **File I/O**: Save and load image files
- **User Interaction**: Create an interactive command-line interface
- **Error Handling**: Manage exceptions and edge cases

## 🚀 Features

### Basic Features
1. **Basic QR Code Generation** - Simple black and white QR codes
2. **Colored QR Codes** - Custom foreground and background colors
3. **Styled QR Codes** - Different module shapes (rounded, circle, square)
4. **QR with Logo** - Embed a logo in the center of QR code

### Specialized QR Codes
5. **WiFi QR Code** - Connect to WiFi by scanning
6. **vCard QR Code** - Share contact information
7. **URL QR Code** - Direct link to websites
8. **Email QR Code** - Pre-filled email composition
9. **SMS QR Code** - Pre-filled text messages
10. **Batch Generation** - Create multiple QR codes at once

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Install Required Libraries

```bash
pip install qrcode[pil]
pip install Pillow
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

### Step 2: Download the Project

Save the `qr_code_generator.py` file to your project directory.

### Step 3: Run the Application

```bash
python qr_code_generator.py
```

## 📚 Requirements File

Create a `requirements.txt` file:

```
qrcode[pil]==7.4.2
Pillow==10.1.0
```

## 🎮 Usage Guide

### Interactive Mode

Run the program and follow the menu:

```bash
python qr_code_generator.py
```

### Example Use Cases

#### 1. Basic QR Code
```python
from qr_code_generator import QRCodeGenerator

generator = QRCodeGenerator()
generator.generate_basic_qr("Hello, World!", "hello.png")
```

#### 2. WiFi QR Code
```python
generator.generate_wifi_qr(
    ssid="MyWiFi",
    password="SecurePassword123",
    security="WPA",
    filename="wifi_qr.png"
)
```

#### 3. Contact Card (vCard)
```python
generator.generate_vcard_qr(
    name="John Doe",
    phone="+1234567890",
    email="john@example.com",
    organization="Tech Corp",
    filename="contact.png"
)
```

#### 4. Styled QR with Custom Colors
```python
generator.generate_styled_qr(
    data="https://example.com",
    style="rounded",
    color="darkblue",
    filename="styled_qr.png"
)
```

#### 5. QR Code with Logo
```python
generator.generate_qr_with_logo(
    data="https://mycompany.com",
    logo_path="company_logo.png",
    filename="branded_qr.png"
)
```

## 🔧 Technical Details

### QR Code Parameters

- **Version**: Size of the QR code (1-40), auto-adjusted if set to 1
- **Error Correction**: 
  - `ERROR_CORRECT_L`: ~7% correction
  - `ERROR_CORRECT_M`: ~15% correction (default)
  - `ERROR_CORRECT_Q`: ~25% correction
  - `ERROR_CORRECT_H`: ~30% correction
- **Box Size**: Size of each box in pixels
- **Border**: Thickness of the border in boxes (minimum 4)

### WiFi QR Format

```
WIFI:T:[WPA|WEP|nopass];S:[SSID];P:[Password];H:[true|false];;
```

### vCard Format

```
BEGIN:VCARD
VERSION:3.0
FN:[Full Name]
TEL:[Phone]
EMAIL:[Email]
ORG:[Organization]
END:VCARD
```

## 📁 Project Structure

```
qr-code-generator/
│
├── qr_code_generator.py    # Main application file
├── README.md                # This file
├── requirements.txt         # Python dependencies
├── qr_outputs/             # Generated QR codes (auto-created)
│   ├── qr_basic.png
│   ├── qr_wifi.png
│   └── ...
└── assets/                 # Optional: logos and images
    └── logo.png
```

## 🎓 Learning Path

### Beginner Exercises
1. Generate a QR code with your name
2. Create a QR code that opens your favorite website
3. Make a WiFi QR code for your home network

### Intermediate Challenges
1. Add a new function to generate calendar event QR codes
2. Implement QR code size validation
3. Add command-line arguments support using `argparse`
4. Create a function to read existing QR codes (using `pyzbar`)

### Advanced Extensions
1. Build a GUI using `tkinter` or `PyQt`
2. Add QR code analytics (track scans using URL shortener)
3. Implement dynamic QR codes that can be updated
4. Create a web API using Flask or FastAPI
5. Add QR code customization (patterns, gradients, images)

## 🛠️ Customization Ideas

### Color Schemes
```python
# Neon style
generator.generate_colored_qr(data, fill_color="#FF00FF", back_color="#000000")

# Pastel style
generator.generate_colored_qr(data, fill_color="#FFB6C1", back_color="#FFF8DC")

# Corporate style
generator.generate_colored_qr(data, fill_color="#003366", back_color="#FFFFFF")
```

### Module Styles
- **Rounded**: Smooth, modern look
- **Circle**: Dotted appearance
- **Square**: Traditional QR style

## 🐛 Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'qrcode'`
- **Solution**: Run `pip install qrcode[pil]`

**Issue**: QR code with logo not working
- **Solution**: Ensure logo file exists and path is correct
- Use PNG format with transparent background for best results

**Issue**: QR code not scannable
- **Solution**: Increase error correction level or reduce data size
- Ensure sufficient contrast between colors

**Issue**: PIL/Pillow errors
- **Solution**: Update Pillow: `pip install --upgrade Pillow`

## 📊 Performance Tips

1. **Optimize for size**: Use lower error correction for simple data
2. **Batch processing**: Use `batch_generate()` for multiple codes
3. **Logo sizing**: Keep logos small (1/5 of QR size) for scannability
4. **Color contrast**: Ensure dark foreground and light background

## 🔐 Security Considerations

- **WiFi Passwords**: QR codes are not encrypted; use for guest networks
- **Sensitive Data**: Avoid embedding confidential information
- **URL Safety**: Validate URLs before generating QR codes
- **Phishing**: Be cautious when sharing QR codes publicly

## 🌟 Real-World Applications

1. **Business Cards**: Add QR code with contact info
2. **Restaurant Menus**: Digital menu access
3. **Product Packaging**: Link to product information
4. **Event Check-in**: Quick registration and ticketing
5. **Marketing**: Track campaign engagement
6. **Education**: Share resources and assignments
7. **Payments**: Mobile payment integration

## 📖 Additional Resources

### Documentation
- [Python qrcode library](https://github.com/lincolnloop/python-qrcode)
- [Pillow documentation](https://pillow.readthedocs.io/)
- [QR Code specification](https://www.qrcode.com/en/about/standards.html)

### Learning Resources
- [QR Code Tutorial](https://www.qr-code-generator.com/)
- [Image Processing with Python](https://realpython.com/image-processing-with-the-python-pillow-library/)
- [Building CLI Applications](https://realpython.com/command-line-interfaces-python-argparse/)

## 🤝 Contributing

This is a learning project! Feel free to:
- Add new features
- Improve error handling
- Enhance the user interface
- Add unit tests
- Optimize performance

## 📝 License

This project is created for educational purposes. Feel free to use and modify for your learning journey.

## 🎯 Next Steps

After mastering this project, consider:
1. Building a web interface with Flask/Django
2. Creating a mobile app version
3. Adding QR code reader functionality
4. Implementing database storage for generated codes
5. Adding analytics and tracking features

---

**Happy Coding! 🚀**

*This project is designed for intermediate Python learners focusing on library integration and image processing.*