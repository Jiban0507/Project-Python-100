# URL Shortener 🔗  ![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=yellow)

A full-featured URL shortening web application built with Flask. This project demonstrates database management with SQLite, hashing algorithms for code generation, and modern web development practices.

## 📋 Features

### Core Functionality
- 🔗 **URL Shortening**: Convert long URLs to short, memorable links
- 🎯 **Custom Codes**: Create personalized short codes
- 📊 **Analytics**: Track clicks and view detailed statistics
- 🔐 **Hashing**: MD5-based short code generation
- 💾 **Database**: SQLite for persistent data storage
- 🌐 **Web Interface**: Beautiful, responsive UI

### Advanced Features
- **Click Tracking**: Record every click with metadata
- **Statistics Dashboard**: View all URLs and their performance
- **Referrer Tracking**: See where clicks come from
- **IP Logging**: Track user IP addresses
- **Timestamp Tracking**: Creation and last access times
- **Duplicate Detection**: Prevent duplicate custom codes
- **URL Validation**: Automatic URL format validation
- **API Endpoints**: RESTful API for programmatic access

### Security & Validation
- Custom code validation (alphanumeric, hyphens, underscores)
- URL format validation and normalization
- SQL injection protection (parameterized queries)
- Unique constraint enforcement

## 🎓 Learning Objectives

This project demonstrates:

1. **Database Management (SQLite)**:
   - Creating database schemas
   - CRUD operations (Create, Read, Update, Delete)
   - Foreign key relationships
   - Query optimization
   - Transaction management
   - Database indexing with UNIQUE constraints

2. **Hashing Algorithms**:
   - MD5 hashing for code generation
   - Hash-to-alphanumeric conversion
   - Collision handling
   - Randomization techniques
   - Base62 encoding concepts

3. **Web Development (Flask)**:
   - Routing and URL mapping
   - Request handling (GET, POST)
   - JSON API responses
   - Template rendering
   - Form handling
   - Redirects
   - Error handling

4. **Additional Concepts**:
   - RESTful API design
   - Data validation
   - Analytics tracking
   - Responsive web design
   - JavaScript fetch API
   - Client-server communication

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Install Dependencies

```bash
pip install flask
```

That's it! SQLite is included with Python.

### Project Structure

```
url-shortener/
├── app.py                # Main application file
├── urls.db              # SQLite database (auto-created)
├── README.md            # This file
└── requirements.txt     # Python dependencies
```

## 💻 Usage

### Starting the Server

```bash
python app.py
```

The server will start on `http://127.0.0.1:5000`

### Accessing the Application

1. **Home Page**: `http://127.0.0.1:5000`
   - Shorten URLs
   - Create custom short codes

2. **Dashboard**: `http://127.0.0.1:5000/dashboard`
   - View all shortened URLs
   - See click statistics
   - Access individual URL stats

3. **Statistics**: `http://127.0.0.1:5000/stats/<short_code>`
   - View detailed analytics for a specific URL
   - See recent clicks
   - Track referrers

4. **API Endpoint**: `http://127.0.0.1:5000/api/urls`
   - Get all URLs in JSON format

### Using the URL Shortener

#### 1. Shorten a URL

**Via Web Interface:**
- Go to home page
- Enter long URL
- (Optional) Enter custom short code
- Click "Shorten URL"
- Copy the generated short URL

**Via API:**
```bash
curl -X POST http://127.0.0.1:5000/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/very/long/url"}'
```

**With Custom Code:**
```bash
curl -X POST http://127.0.0.1:5000/shorten \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com", "custom": "my-link"}'
```

#### 2. Access Shortened URL

Simply visit: `http://127.0.0.1:5000/<short_code>`

You'll be redirected to the original URL, and the click will be recorded.

#### 3. View Statistics

Visit: `http://127.0.0.1:5000/stats/<short_code>`

You'll see:
- Original URL
- Creation date
- Total clicks
- Recent click history with IP and referrer

## 📸 Screenshots

### Home Page
```
┌─────────────────────────────────────────┐
│         🔗 URL SHORTENER                │
│   Shorten your long URLs instantly!     │
├─────────────────────────────────────────┤
│                                         │
│  Enter Long URL                         │
│  [https://example.com/long/url____]    │
│                                         │
│  Custom Short Code (Optional)           │
│  [my-link_______________________]       │
│                                         │
│        [✨ Shorten URL]                 │
│                                         │
│  ✅ Success!                            │
│  Your shortened URL:                    │
│  http://localhost:5000/abc123           │
│        [📋 Copy to Clipboard]           │
│                                         │
└─────────────────────────────────────────┘
```

## 🔧 Code Structure

### Database Schema

```sql
-- URLs Table
CREATE TABLE urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    original_url TEXT NOT NULL,
    short_code TEXT UNIQUE NOT NULL,
    custom_code TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    clicks INTEGER DEFAULT 0,
    last_accessed TIMESTAMP,
    user_ip TEXT,
    is_active INTEGER DEFAULT 1
);

-- Clicks Table
CREATE TABLE clicks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    short_code TEXT NOT NULL,
    clicked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_ip TEXT,
    user_agent TEXT,
    referrer TEXT,
    FOREIGN KEY (short_code) REFERENCES urls(short_code)
);
```

### Main Functions

```python
# Database Operations
def init_db()                              # Initialize database schema
def get_db()                               # Get database connection

# Hashing & Code Generation
def generate_short_code(url, length=6)     # Generate hash-based code
def generate_random_code(length=6)         # Generate random code
def is_valid_custom_code(code)             # Validate custom codes

# URL Operations
def shorten_url(url, custom, ip)           # Create short URL
def get_original_url(short_code)           # Retrieve original URL
def record_click(code, ip, agent, ref)     # Log click analytics
def get_url_stats(short_code)              # Get URL statistics
def get_all_urls()                         # Get all URLs

# Web Routes
@app.route('/')                            # Home page
@app.route('/shorten')                     # Shorten endpoint
@app.route('/<short_code>')                # Redirect endpoint
@app.route('/stats/<short_code>')          # Statistics page
@app.route('/dashboard')                   # Dashboard page
@app.route('/api/urls')                    # API endpoint
```

## 🔐 Hashing Algorithm Explained

### MD5-Based Code Generation

```python
def generate_short_code(url, length=6):
    # 1. Create unique input (URL + timestamp)
    hash_input = f"{url}{datetime.now().isoformat()}"
    
    # 2. Generate MD5 hash
    hash_object = hashlib.md5(hash_input.encode())
    hash_hex = hash_object.hexdigest()
    # Result: "5d41402abc4b2a76b9719d911017c592"
    
    # 3. Convert to base62 (alphanumeric)
    chars = string.ascii_letters + string.digits
    # chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    short_code = ''
    for i in range(length):
        # Use hex pairs to select characters
        index = int(hash_hex[i:i+2], 16) % len(chars)
        short_code += chars[index]
    
    return short_code  # e.g., "aB3xY9"
```

**Why MD5?**
- Fast computation
- Consistent output length (32 hex characters)
- Good distribution of values
- Sufficient for non-cryptographic use case

**Collision Handling:**
- Check database for existing code
- If collision detected, generate new random code
- Retry up to 10 times

## 💾 Database Operations

### Inserting a URL

```python
def shorten_url(original_url, custom_code, user_ip):
    db = get_db()
    
    # Generate or use custom code
    short_code = custom_code or generate_short_code(original_url)
    
    # Insert into database
    db.execute(
        '''INSERT INTO urls (original_url, short_code, custom_code, user_ip)
           VALUES (?, ?, ?, ?)''',
        (original_url, short_code, custom_code, user_ip)
    )
    db.commit()
    db.close()
    
    return short_code
```

### Retrieving a URL

```python
def get_original_url(short_code):
    db = get_db()
    
    # Query database
    url_data = db.execute(
        'SELECT * FROM urls WHERE short_code = ? AND is_active = 1',
        (short_code,)
    ).fetchone()
    
    if url_data:
        # Update click count
        db.execute(
            'UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?',
            (short_code,)
        )
        db.commit()
    
    db.close()
    return url_data
```

### Recording Analytics

```python
def record_click(short_code, user_ip, user_agent, referrer):
    db = get_db()
    
    db.execute(
        '''INSERT INTO clicks (short_code, user_ip, user_agent, referrer)
           VALUES (?, ?, ?, ?)''',
        (short_code, user_ip, user_agent, referrer)
    )
    
    db.commit()
    db.close()
```

## 🌐 API Documentation

### Shorten URL

**Endpoint:** `POST /shorten`

**Request Body:**
```json
{
  "url": "https://example.com/very/long/url",
  "custom": "my-link"  // optional
}
```

**Response (Success):**
```json
{
  "success": true,
  "short_code": "abc123",
  "short_url": "http://localhost:5000/abc123",
  "original_url": "https://example.com/very/long/url"
}
```

**Response (Error):**
```json
{
  "error": "Custom code already in use"
}
```

### Get All URLs

**Endpoint:** `GET /api/urls`

**Response:**
```json
[
  {
    "id": 1,
    "original_url": "https://example.com",
    "short_code": "abc123",
    "clicks": 42,
    "created_at": "2024-12-31 10:30:00"
  },
  ...
]
```

## 🎨 Customization

### Change Short Code Length

```python
def generate_short_code(url, length=6):  # Change length here
    # ...
```

### Modify Allowed Custom Code Characters

```python
def is_valid_custom_code(code):
    # Current: letters, numbers, -, _
    # Modify pattern here
    if not all(c in string.ascii_letters + string.digits + '-_' for c in code):
        return False
```

### Change Hash Algorithm

```python
# Replace MD5 with SHA256
import hashlib

hash_object = hashlib.sha256(hash_input.encode())
```

### Custom URL Expiration

Add expiration logic:

```python
# In database schema
CREATE TABLE urls (
    ...
    expires_at TIMESTAMP,
    ...
);

# In get_original_url()
if url_data and url_data['expires_at']:
    if datetime.now() > datetime.fromisoformat(url_data['expires_at']):
        return None  # URL expired
```

### Add QR Code Generation

```python
# Install: pip install qrcode[pil]
import qrcode

def generate_qr(short_url):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(short_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img
```

## 🐛 Troubleshooting

### Database Locked Error

**Error:** `sqlite3.OperationalError: database is locked`

**Solution:**
- Close all database connections properly
- Use `db.close()` after operations
- Don't hold connections open too long

### Import Error: No module named 'flask'

**Error:** `ModuleNotFoundError: No module named 'flask'`

**Solution:**
```bash
pip install flask
```

### Port Already in Use

**Error:** `OSError: [Errno 48] Address already in use`

**Solution:**
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9

# Or use different port
app.run(port=5001)
```

### URL Not Redirecting

**Issue:** Short URL returns 404

**Solutions:**
- Check if URL exists in database
- Verify `is_active` flag is 1
- Check browser console for errors
- Ensure short_code matches exactly

### Custom Code Validation Failing

**Issue:** Custom code rejected

**Solutions:**
- Use only letters, numbers, -, _
- Length must be 3-20 characters
- Code must be unique
- Check for spaces (not allowed)

## 📚 Learning Resources

### SQLite & Databases
- [SQLite Python Documentation](https://docs.python.org/3/library/sqlite3.html)
- [SQL Tutorial](https://www.w3schools.com/sql/)
- Database normalization
- Index optimization

### Hashing
- [Python hashlib Documentation](https://docs.python.org/3/library/hashlib.html)
- Hash functions comparison
- Base conversion algorithms
- Collision resolution strategies

### Flask Web Development
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- REST API design
- Template engines

## 🎯 Practice Challenges

1. **Add URL Expiration**: Implement time-based URL expiration
2. **QR Code Generation**: Generate QR codes for short URLs
3. **User Authentication**: Add user accounts and private URLs
4. **Rate Limiting**: Limit requests per IP address
5. **Advanced Analytics**: Track geographic location, device types
6. **URL Categories**: Organize URLs by category/tags
7. **Bulk Shortening**: Process multiple URLs at once
8. **Export Data**: Export statistics to CSV/PDF
9. **Custom Domains**: Support multiple domain names
10. **API Authentication**: Add API keys for programmatic access

## 🚀 Advanced Features to Add

### 1. URL Preview
```python
def get_url_preview(url):
    # Fetch Open Graph meta tags
    # Display title, description, image
    pass
```

### 2. Link Password Protection
```python
# Add password field to database
CREATE TABLE urls (
    ...
    password_hash TEXT,
    ...
);

# Verify before redirect
def verify_password(short_code, password):
    # Check hashed password
    pass
```

### 3. Branded Short Domains
```python
CUSTOM_DOMAINS = {
    'example.com': 'ex.co',
    'mycompany.com': 'my.co'
}

def get_branded_url(domain, short_code):
    return f"{CUSTOM_DOMAINS.get(domain)}/{short_code}"
```

### 4. A/B Testing
```python
# Create multiple versions of same URL
# Randomly redirect to different destinations
# Track conversion rates
```

### 5. Link Expiration Notifications
```python
# Send email before link expires
# Allow link renewal
```

## 📝 Project Files

```
url-shortener-project/
├── app.py                 # Main Flask application
├── urls.db               # SQLite database
├── requirements.txt      # Dependencies
├── README.md            # Documentation
└── static/              # Optional: CSS, JS, images
    ├── style.css
    └── script.js
```

### requirements.txt

```txt
Flask==3.0.0
```

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Additional hash algorithms
- Better UI/UX design
- More analytics features
- API rate limiting
- User authentication
- Link categories/folders
- Bulk operations
- Unit tests

## 📄 License

This project is open source and available for educational purposes.

## 🌟 Acknowledgments

- Built with Flask web framework
- Uses SQLite for data persistence
- MD5 hashing for code generation
- Responsive CSS design

---

**Happy URL Shortening! 🔗✨**

Made with ❤️ for learning Database Management, Hashing, and Web Development