"""
URL Shortener Application
Demonstrates: Database (SQLite), Hashing, Web Development (Flask)

Setup:
pip install flask
"""

from flask import Flask, render_template_string, request, redirect, url_for, jsonify
import sqlite3
import hashlib
import string
import random
from datetime import datetime
import os

app = Flask(__name__)
app.config['DATABASE'] = 'urls.db'

# ==================== DATABASE FUNCTIONS ====================

def get_db():
    """Get database connection"""
    db = sqlite3.connect(app.config['DATABASE'])
    db.row_factory = sqlite3.Row
    return db

def init_db():
    """Initialize the database"""
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_code TEXT UNIQUE NOT NULL,
            custom_code TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            clicks INTEGER DEFAULT 0,
            last_accessed TIMESTAMP,
            user_ip TEXT,
            is_active INTEGER DEFAULT 1
        )
    ''')
    
    db.execute('''
        CREATE TABLE IF NOT EXISTS clicks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short_code TEXT NOT NULL,
            clicked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            user_ip TEXT,
            user_agent TEXT,
            referrer TEXT,
            FOREIGN KEY (short_code) REFERENCES urls (short_code)
        )
    ''')
    
    db.commit()
    db.close()
    print("✓ Database initialized successfully")

# ==================== HASHING & ENCODING FUNCTIONS ====================

def generate_short_code(url, length=6):
    """Generate a short code using hashing"""
    # Create hash of the URL + timestamp for uniqueness
    hash_input = f"{url}{datetime.now().isoformat()}"
    hash_object = hashlib.md5(hash_input.encode())
    hash_hex = hash_object.hexdigest()
    
    # Convert hex to base62 (alphanumeric)
    chars = string.ascii_letters + string.digits
    short_code = ''
    
    # Use hash to generate short code
    for i in range(length):
        index = int(hash_hex[i:i+2], 16) % len(chars)
        short_code += chars[index]
    
    return short_code

def generate_random_code(length=6):
    """Generate a random alphanumeric code"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def is_valid_custom_code(code):
    """Validate custom short code"""
    if not code:
        return False
    if len(code) < 3 or len(code) > 20:
        return False
    if not all(c in string.ascii_letters + string.digits + '-_' for c in code):
        return False
    return True

# ==================== URL OPERATIONS ====================

def shorten_url(original_url, custom_code=None, user_ip=None):
    """Shorten a URL and store in database"""
    db = get_db()
    
    # Check if custom code is provided
    if custom_code:
        if not is_valid_custom_code(custom_code):
            return None, "Invalid custom code. Use 3-20 characters (letters, numbers, -, _)"
        
        # Check if custom code already exists
        existing = db.execute(
            'SELECT * FROM urls WHERE custom_code = ? OR short_code = ?',
            (custom_code, custom_code)
        ).fetchone()
        
        if existing:
            return None, "Custom code already in use"
        
        short_code = custom_code
    else:
        # Generate short code
        short_code = generate_short_code(original_url)
        
        # Ensure uniqueness
        attempts = 0
        while attempts < 10:
            existing = db.execute(
                'SELECT * FROM urls WHERE short_code = ?',
                (short_code,)
            ).fetchone()
            
            if not existing:
                break
            
            short_code = generate_random_code()
            attempts += 1
        
        if attempts >= 10:
            return None, "Failed to generate unique code"
    
    # Insert into database
    try:
        db.execute(
            '''INSERT INTO urls (original_url, short_code, custom_code, user_ip)
               VALUES (?, ?, ?, ?)''',
            (original_url, short_code, custom_code, user_ip)
        )
        db.commit()
        return short_code, None
    except sqlite3.IntegrityError:
        return None, "Short code already exists"
    finally:
        db.close()

def get_original_url(short_code):
    """Retrieve original URL from short code"""
    db = get_db()
    
    url_data = db.execute(
        'SELECT * FROM urls WHERE (short_code = ? OR custom_code = ?) AND is_active = 1',
        (short_code, short_code)
    ).fetchone()
    
    if url_data:
        # Update click count
        db.execute(
            'UPDATE urls SET clicks = clicks + 1, last_accessed = ? WHERE short_code = ?',
            (datetime.now(), url_data['short_code'])
        )
        db.commit()
    
    db.close()
    return dict(url_data) if url_data else None

def record_click(short_code, user_ip, user_agent, referrer):
    """Record click analytics"""
    db = get_db()
    db.execute(
        '''INSERT INTO clicks (short_code, user_ip, user_agent, referrer)
           VALUES (?, ?, ?, ?)''',
        (short_code, user_ip, user_agent, referrer)
    )
    db.commit()
    db.close()

def get_url_stats(short_code):
    """Get statistics for a short URL"""
    db = get_db()
    
    url_data = db.execute(
        'SELECT * FROM urls WHERE short_code = ? OR custom_code = ?',
        (short_code, short_code)
    ).fetchone()
    
    if not url_data:
        db.close()
        return None
    
    clicks = db.execute(
        'SELECT * FROM clicks WHERE short_code = ? ORDER BY clicked_at DESC LIMIT 10',
        (url_data['short_code'],)
    ).fetchall()
    
    db.close()
    
    return {
        'url_data': dict(url_data),
        'recent_clicks': [dict(click) for click in clicks]
    }

def get_all_urls():
    """Get all URLs from database"""
    db = get_db()
    urls = db.execute(
        'SELECT * FROM urls ORDER BY created_at DESC LIMIT 100'
    ).fetchall()
    db.close()
    
    return [dict(url) for url in urls]

# ==================== WEB ROUTES ====================

@app.route('/')
def index():
    """Home page with URL shortener form"""
    return render_template_string(HOME_TEMPLATE)

@app.route('/shorten', methods=['POST'])
def shorten():
    """Handle URL shortening request"""
    data = request.get_json() if request.is_json else request.form
    
    original_url = data.get('url', '').strip()
    custom_code = data.get('custom', '').strip() or None
    
    # Validate URL
    if not original_url:
        return jsonify({'error': 'URL is required'}), 400
    
    if not original_url.startswith(('http://', 'https://')):
        original_url = 'https://' + original_url
    
    # Shorten URL
    user_ip = request.remote_addr
    short_code, error = shorten_url(original_url, custom_code, user_ip)
    
    if error:
        return jsonify({'error': error}), 400
    
    short_url = request.host_url + short_code
    
    return jsonify({
        'success': True,
        'short_code': short_code,
        'short_url': short_url,
        'original_url': original_url
    })

@app.route('/<short_code>')
def redirect_to_url(short_code):
    """Redirect to original URL"""
    url_data = get_original_url(short_code)
    
    if not url_data:
        return render_template_string(ERROR_TEMPLATE, 
                                     error="URL not found or has been deactivated"), 404
    
    # Record click analytics
    record_click(
        url_data['short_code'],
        request.remote_addr,
        request.headers.get('User-Agent', 'Unknown'),
        request.referrer
    )
    
    return redirect(url_data['original_url'])

@app.route('/stats/<short_code>')
def stats(short_code):
    """Display statistics for a short URL"""
    stats_data = get_url_stats(short_code)
    
    if not stats_data:
        return render_template_string(ERROR_TEMPLATE, 
                                     error="URL not found"), 404
    
    return render_template_string(STATS_TEMPLATE, 
                                 stats=stats_data,
                                 short_code=short_code,
                                 base_url=request.host_url)

@app.route('/dashboard')
def dashboard():
    """Display all shortened URLs"""
    urls = get_all_urls()
    return render_template_string(DASHBOARD_TEMPLATE, 
                                 urls=urls,
                                 base_url=request.host_url)

@app.route('/api/urls')
def api_urls():
    """API endpoint to get all URLs"""
    urls = get_all_urls()
    return jsonify(urls)

# ==================== HTML TEMPLATES ====================

HOME_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>URL Shortener</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 600px;
            width: 100%;
            margin-top: 50px;
        }
        h1 {
            color: #667eea;
            text-align: center;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 600;
        }
        input {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        input:focus {
            outline: none;
            border-color: #667eea;
        }
        button {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s;
        }
        button:hover {
            transform: translateY(-2px);
        }
        .result {
            display: none;
            margin-top: 30px;
            padding: 20px;
            background: #f0f7ff;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }
        .result.show { display: block; }
        .short-url {
            font-size: 20px;
            color: #667eea;
            word-break: break-all;
            margin: 10px 0;
            font-weight: 600;
        }
        .copy-btn {
            background: #4caf50;
            margin-top: 10px;
            padding: 10px;
        }
        .error {
            background: #ffebee;
            color: #c62828;
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 20px;
            display: none;
            border-left: 4px solid #c62828;
        }
        .error.show { display: block; }
        .links {
            text-align: center;
            margin-top: 20px;
        }
        .links a {
            color: #667eea;
            text-decoration: none;
            margin: 0 10px;
            font-weight: 600;
        }
        .links a:hover { text-decoration: underline; }
        .feature {
            background: #f5f5f5;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
        }
        .feature h3 {
            color: #667eea;
            margin-bottom: 10px;
        }
        .feature ul {
            list-style-position: inside;
            color: #666;
        }
        .feature li {
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔗 URL Shortener</h1>
        <p class="subtitle">Shorten your long URLs instantly!</p>
        
        <div class="error" id="error"></div>
        
        <form id="shortenForm">
            <div class="form-group">
                <label>Enter Long URL</label>
                <input type="text" id="url" placeholder="https://example.com/very/long/url" required>
            </div>
            
            <div class="form-group">
                <label>Custom Short Code (Optional)</label>
                <input type="text" id="custom" placeholder="my-link" 
                       pattern="[A-Za-z0-9_-]{3,20}" 
                       title="3-20 characters: letters, numbers, -, _">
            </div>
            
            <button type="submit">✨ Shorten URL</button>
        </form>
        
        <div class="result" id="result">
            <h3>✅ Success!</h3>
            <p>Your shortened URL:</p>
            <div class="short-url" id="shortUrl"></div>
            <button class="copy-btn" onclick="copyUrl()">📋 Copy to Clipboard</button>
            <p style="margin-top: 15px; color: #666;">
                View stats: <a href="#" id="statsLink" target="_blank">Statistics Page</a>
            </p>
        </div>
        
        <div class="links">
            <a href="/dashboard">📊 Dashboard</a>
            <a href="#" onclick="showFeatures(); return false;">ℹ️ Features</a>
        </div>
        
        <div class="feature" id="features" style="display: none;">
            <h3>Features</h3>
            <ul>
                <li>🎯 Custom short codes</li>
                <li>📊 Click analytics</li>
                <li>🔒 SQLite database storage</li>
                <li>🔐 MD5 hashing for code generation</li>
                <li>📈 Real-time statistics</li>
                <li>💾 Persistent data storage</li>
            </ul>
        </div>
    </div>
    
    <script>
        document.getElementById('shortenForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const url = document.getElementById('url').value;
            const custom = document.getElementById('custom').value;
            const errorDiv = document.getElementById('error');
            const resultDiv = document.getElementById('result');
            
            errorDiv.classList.remove('show');
            resultDiv.classList.remove('show');
            
            try {
                const response = await fetch('/shorten', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ url, custom })
                });
                
                const data = await response.json();
                
                if (data.error) {
                    errorDiv.textContent = data.error;
                    errorDiv.classList.add('show');
                } else {
                    document.getElementById('shortUrl').textContent = data.short_url;
                    document.getElementById('statsLink').href = '/stats/' + data.short_code;
                    resultDiv.classList.add('show');
                    document.getElementById('shortenForm').reset();
                }
            } catch (error) {
                errorDiv.textContent = 'An error occurred. Please try again.';
                errorDiv.classList.add('show');
            }
        });
        
        function copyUrl() {
            const url = document.getElementById('shortUrl').textContent;
            navigator.clipboard.writeText(url).then(() => {
                alert('Copied to clipboard!');
            });
        }
        
        function showFeatures() {
            const features = document.getElementById('features');
            features.style.display = features.style.display === 'none' ? 'block' : 'none';
        }
    </script>
</body>
</html>
'''

STATS_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>URL Statistics</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 900px;
            margin: 30px auto;
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }
        h1 {
            color: #667eea;
            margin-bottom: 20px;
        }
        .stat-card {
            background: #f5f5f5;
            padding: 20px;
            border-radius: 10px;
            margin: 15px 0;
        }
        .stat-row {
            display: flex;
            justify-content: space-between;
            margin: 10px 0;
            padding: 10px 0;
            border-bottom: 1px solid #e0e0e0;
        }
        .stat-label {
            font-weight: 600;
            color: #666;
        }
        .stat-value {
            color: #333;
            word-break: break-all;
        }
        .clicks-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        .clicks-table th, .clicks-table td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #e0e0e0;
        }
        .clicks-table th {
            background: #667eea;
            color: white;
        }
        .back-btn {
            display: inline-block;
            padding: 10px 20px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            margin-top: 20px;
        }
        .back-btn:hover {
            background: #5568d3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 URL Statistics</h1>
        
        <div class="stat-card">
            <h2 style="color: #667eea; margin-bottom: 15px;">URL Information</h2>
            <div class="stat-row">
                <span class="stat-label">Short URL:</span>
                <span class="stat-value">{{ base_url }}{{ short_code }}</span>
            </div>
            <div class="stat-row">
                <span class="stat-label">Original URL:</span>
                <span class="stat-value">{{ stats.url_data.original_url }}</span>
            </div>
            <div class="stat-row">
                <span class="stat-label">Created:</span>
                <span class="stat-value">{{ stats.url_data.created_at }}</span>
            </div>
            <div class="stat-row">
                <span class="stat-label">Total Clicks:</span>
                <span class="stat-value">{{ stats.url_data.clicks }}</span>
            </div>
            {% if stats.url_data.last_accessed %}
            <div class="stat-row">
                <span class="stat-label">Last Accessed:</span>
                <span class="stat-value">{{ stats.url_data.last_accessed }}</span>
            </div>
            {% endif %}
        </div>
        
        {% if stats.recent_clicks %}
        <div class="stat-card">
            <h2 style="color: #667eea; margin-bottom: 15px;">Recent Clicks (Last 10)</h2>
            <table class="clicks-table">
                <thead>
                    <tr>
                        <th>Time</th>
                        <th>IP Address</th>
                        <th>Referrer</th>
                    </tr>
                </thead>
                <tbody>
                    {% for click in stats.recent_clicks %}
                    <tr>
                        <td>{{ click.clicked_at }}</td>
                        <td>{{ click.user_ip }}</td>
                        <td>{{ click.referrer or 'Direct' }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        {% endif %}
        
        <a href="/" class="back-btn">← Back to Home</a>
    </div>
</body>
</html>
'''

DASHBOARD_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard - URL Shortener</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 30px auto;
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }
        h1 {
            color: #667eea;
            margin-bottom: 20px;
        }
        .url-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        .url-table th, .url-table td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #e0e0e0;
        }
        .url-table th {
            background: #667eea;
            color: white;
            position: sticky;
            top: 0;
        }
        .url-table tr:hover {
            background: #f5f5f5;
        }
        .short-link {
            color: #667eea;
            text-decoration: none;
            font-weight: 600;
        }
        .short-link:hover {
            text-decoration: underline;
        }
        .stats-link {
            color: #4caf50;
            text-decoration: none;
            font-size: 0.9em;
        }
        .original-url {
            max-width: 300px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        .back-btn {
            display: inline-block;
            padding: 10px 20px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            margin-top: 20px;
        }
        .back-btn:hover {
            background: #5568d3;
        }
        .summary {
            display: flex;
            gap: 20px;
            margin-bottom: 20px;
        }
        .summary-card {
            flex: 1;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        .summary-card h3 {
            font-size: 2em;
            margin-bottom: 5px;
        }
        .summary-card p {
            opacity: 0.9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Dashboard</h1>
        
        <div class="summary">
            <div class="summary-card">
                <h3>{{ urls|length }}</h3>
                <p>Total URLs</p>
            </div>
            <div class="summary-card">
                <h3>{{ urls|sum(attribute='clicks') }}</h3>
                <p>Total Clicks</p>
            </div>
        </div>
        
        {% if urls %}
        <table class="url-table">
            <thead>
                <tr>
                    <th>Short Code</th>
                    <th>Original URL</th>
                    <th>Clicks</th>
                    <th>Created</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {% for url in urls %}
                <tr>
                    <td>
                        <a href="{{ base_url }}{{ url.short_code }}" 
                           class="short-link" 
                           target="_blank">{{ url.short_code }}</a>
                    </td>
                    <td>
                        <div class="original-url" title="{{ url.original_url }}">
                            {{ url.original_url }}
                        </div>
                    </td>
                    <td>{{ url.clicks }}</td>
                    <td>{{ url.created_at }}</td>
                    <td>
                        <a href="/stats/{{ url.short_code }}" class="stats-link">📈 Stats</a>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        {% else %}
        <p style="text-align: center; color: #666; margin: 40px 0;">
            No URLs yet. <a href="/" style="color: #667eea;">Create your first short URL!</a>
        </p>
        {% endif %}
        
        <a href="/" class="back-btn">← Back to Home</a>
    </div>
</body>
</html>
'''

ERROR_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Error - URL Shortener</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 50px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            text-align: center;
            max-width: 500px;
        }
        h1 {
            color: #e74c3c;
            font-size: 4em;
            margin-bottom: 20px;
        }
        p {
            color: #666;
            font-size: 1.2em;
            margin-bottom: 30px;
        }
        .back-btn {
            display: inline-block;
            padding: 12px 30px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
        }
        .back-btn:hover {
            background: #5568d3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>404</h1>
        <p>{{ error }}</p>
        <a href="/" class="back-btn">← Go Home</a>
    </div>
</body>
</html>
'''

# ==================== MAIN ====================

if __name__ == '__main__':
    # Initialize database
    if not os.path.exists(app.config['DATABASE']):
        init_db()
    
    print("\n" + "="*50)
    print("🔗 URL Shortener Server Starting...")
    print("="*50)
    print("\n📍 Access the application at:")
    print("   http://127.0.0.1:5000")
    print("\n💡 Features:")
    print("   • Home page: http://127.0.0.1:5000")
    print("   • Dashboard: http://127.0.0.1:5000/dashboard")
    print("   • API: http://127.0.0.1:5000/api/urls")
    print("\n⚠️  Press CTRL+C to stop the server")
    print("="*50 + "\n")
    
    # Run Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)