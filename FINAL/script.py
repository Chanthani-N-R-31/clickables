import os
import glob
import re

html_files = glob.glob('*.html')

style_injection = '''
    <style>
        /* Modern Glassmorphism Navigation Bar */
        .nav-container {
            position: fixed;
            top: 20px;
            left: 20px;
            z-index: 1000;
            display: flex;
            gap: 15px;
            font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        .nav-btn {
            padding: 10px 20px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 8px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            text-decoration: none;
            color: #ffffff;
            display: inline-flex;
            align-items: center;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05), inset 0 1px 0 rgba(255, 255, 255, 0.1);
            background: rgba(255, 255, 255, 0.1);
        }

        .home-btn {
            background: linear-gradient(135deg, rgba(0, 123, 255, 0.85), rgba(0, 86, 179, 0.85));
        }

        .home-btn:hover {
            background: linear-gradient(135deg, rgba(0, 123, 255, 1), rgba(0, 86, 179, 1));
            transform: translateY(-2px);
            box-shadow: 0 8px 15px rgba(0, 123, 255, 0.3);
        }

        .back-btn {
            background: linear-gradient(135deg, rgba(108, 117, 125, 0.85), rgba(90, 98, 104, 0.85));
        }

        .back-btn:hover {
            background: linear-gradient(135deg, rgba(108, 117, 125, 1), rgba(90, 98, 104, 1));
            transform: translateY(-2px);
            box-shadow: 0 8px 15px rgba(108, 117, 125, 0.3);
        }

        .btn-icon {
            margin-right: 8px;
            font-size: 1.2em;
        }

        /* Image Styling */
        img {
            max-width: 100%;
            height: auto;
            border-radius: 12px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.12);
            object-fit: cover;
            display: block;
            margin: 20px auto;
            transition: transform 0.3s ease;
        }

        img:hover {
            transform: scale(1.02);
        }
    </style>
'''

nav_injection = '''
    <div class="nav-container">
        <button onclick="window.history.back()" class="nav-btn back-btn">
            <span class="btn-icon">←</span> Back
        </button>

        <a href="IT.drawio.html" class="nav-btn home-btn">
            <span class="btn-icon">🏠</span> Home
        </a>
    </div>
'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove existing nav-container if it's there
    content = re.sub(r'<div class="nav-container">.*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style>\s*/\*\s*Navigation Bar Styling\s*\*/.*?</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style>\s*/\*\s*Modern Glassmorphism Navigation Bar\s*\*/.*?</style>', '', content, flags=re.DOTALL)

    if '</head>' in content:
        content = content.replace('</head>', style_injection + '\n</head>')
    elif '<body>' in content:
        content = content.replace('<body>', '<head>\n' + style_injection + '\n</head>\n<body>')
        
    content = content.replace('<body>', '<body>\n' + nav_injection)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Processed {len(html_files)} HTML files.")
