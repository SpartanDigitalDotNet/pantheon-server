@echo off
echo 🧪 Testing Secure Redis Cache with Environment Variables
echo ==================================================

rem Set the Redis password environment variable - CHANGE THIS PASSWORD!
set PANTHEON_REDIS_PASSWORD=YOUR_TEST_PASSWORD_HERE

echo Environment variable set: PANTHEON_REDIS_PASSWORD=***

echo.
echo Running test script...
python test_final_secure.py

echo.
echo Test complete!
pause
