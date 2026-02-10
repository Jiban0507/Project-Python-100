# Image Resizer Tool

A professional-grade desktop application for batch resizing images with an intuitive graphical user interface built using Python and Tkinter.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Resize Modes](#resize-modes)
- [Technical Details](#technical-details)
- [Error Handling](#error-handling)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Overview

The Image Resizer Tool is a Python application designed to streamline the process of resizing multiple images simultaneously. Whether you need to maintain consistent image dimensions, reduce file sizes, or prepare images for web publishing, this tool provides an easy-to-use interface for batch processing.

With support for multiple image formats and flexible resizing options, it's suitable for photographers, web developers, content creators, and anyone who needs to manage image collections efficiently.

## Features

- **Batch Image Processing**: Select and resize multiple images in a single operation
- **Multiple Resize Modes**:
  - Fixed dimensions (width × height)
  - Percentage-based scaling
- **Multi-Format Support**: Compatible with JPG, JPEG, and PNG image formats
- **High-Quality Output**: Uses LANCZOS resampling algorithm for superior image quality
- **Progress Tracking**: Visual progress bar to monitor batch operations
- **User-Friendly GUI**: Intuitive graphical interface built with Tkinter
- **Error Resilience**: Gracefully handles unsupported files without interrupting the batch process
- **Output Folder Selection**: Choose custom output directory for resized images
- **Success Notification**: Confirmation message showing number of successfully resized images

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- Pillow (PIL) - Python Imaging Library

## Installation

### 1. Ensure Python is Installed

```bash
python --version
```

### 2. Install Required Dependencies

Install the Pillow library using pip:

```bash
pip install Pillow
```

### 3. Run the Application

Navigate to the project directory and execute:

```bash
python "Resizer Image.py"
```

## Usage

### Step-by-Step Guide

1. **Launch the Application**
   - Run the script to open the Image Resizer Tool window

2. **Select Images**
   - Click the "Select Images (Gallery)" button
   - Browse and select one or multiple image files (JPG, JPEG, PNG)
   - Confirmation message displays the number of selected images

3. **Choose Resize Mode**
   - Select either **Width & Height** or **Percentage Based** option

4. **Configure Resize Parameters**
   - **For Width & Height Mode**: Enter maximum width and height values in pixels
   - **For Percentage Mode**: Enter the scaling percentage (e.g., 50 for 50% of original size)

5. **Select Output Folder**
   - Click "Resize Images" button
   - Choose the destination folder for resized images
   - Files will be saved with their original names

6. **Monitor Progress**
   - Watch the progress bar as images are being processed
   - A success message will appear upon completion

## Resize Modes

### Mode 1: Width & Height (Fixed Dimensions)
Creates thumbnail images that fit within your specified dimensions while maintaining aspect ratio.

**Example**: Setting width=800px and height=600px will resize images to fit within these bounds.

### Mode 2: Percentage Based (Proportional Scaling)
Scales all images by the specified percentage relative to their original dimensions.

**Example**: Setting percentage=50 will resize images to 50% of their original size.

## Technical Details

### Image Processing
- **Algorithm**: LANCZOS resampling for high-quality output
- **Supported Formats**: JPEG, JPG, PNG
- **Input**: Multiple image files from user selection
- **Output**: Original filename preserved in destination folder

### GUI Components
- Label fields for status and configuration
- Radio buttons for resize mode selection
- Text entry fields for parameter input
- Progress bar for batch operation tracking
- Dialog boxes for file selection and notifications

### Architecture
```
InputFiles → ProcessingLoop → ImageOpen → Resize → Save → UpdateProgress
```

## Error Handling

The application handles the following scenarios gracefully:

- **No images selected**: Prompts user to select images before resizing
- **Invalid input values**: Displays error message for non-numeric entries
- **Corrupted image files**: Skips problematic files and continues processing
- **Invalid output directory**: Allows user to cancel and reselect

All errors are communicated through user-friendly dialog messages.

## Troubleshooting

### Issue: Pillow library not found
**Solution**: Install Pillow using the command:
```bash
pip install Pillow
```

### Issue: File dialog not opening
**Solution**: Ensure Tkinter is installed. For some Linux distributions:
```bash
sudo apt-get install python3-tk
```

### Issue: Images not saving to output folder
**Solution**: 
- Verify you have write permissions to the selected output folder
- Check disk space availability
- Ensure output folder path doesn't contain special characters

### Issue: Image quality appears reduced
**Solution**: This is normal when scaling down large images. For best results, keep percentage values at 75% or higher for noticeable quality preservation.

## License

This project is open-source and available under the MIT License. See the LICENSE file for more details.

---

**Version**: 1.0  
**Last Updated**: February 2026  
**Author**: Python 100 Projects Community

## Contributing

Contributions and suggestions for improvements are welcome. Feel free to fork and submit pull requests for any enhancements.

## Support

For issues, questions, or suggestions, please refer to the project documentation or open an issue in the project repository.
