@echo off
echo 🧪 Testing Secure Redis Cache with Environment Variables
echo ==================================================

rem Set the Redis password environment variable
set PANTHEON_REDIS_PASSWORD=SuperSecure123!

echo Environment variable set: PANTHEON_REDIS_PASSWORD=***

echo.
echo Running test script...
python test_final_secure.py

echo.
echo Test complete!
pause
