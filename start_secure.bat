@echo off
echo 🔒 Starting Pantheon Server with Secure Configuration
echo ==================================================

REM Set Redis password environment variable - CHANGE THIS PASSWORD!
set PANTHEON_REDIS_PASSWORD=YOUR_SECURE_PASSWORD_HERE

echo ✅ Environment variable set: PANTHEON_REDIS_PASSWORD
echo 🔒 Password configured from environment variable

echo 🚀 Starting Pantheon Server...
"C:\Dev\repo\Pantheon\pantheon-server\.venv\Scripts\python.exe" run.py dev
