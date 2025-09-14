@echo off
echo 🔒 Starting Pantheon Server with Secure Configuration
echo ==================================================

REM Set Redis password environment variable
set PANTHEON_REDIS_PASSWORD=pantheon_server**!

echo ✅ Environment variable set: PANTHEON_REDIS_PASSWORD
echo 🔒 Password configured from environment variable

echo 🚀 Starting Pantheon Server...
"C:\Dev\repo\Pantheon\pantheon-server\.venv\Scripts\python.exe" run.py dev
