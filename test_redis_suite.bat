@echo off
echo Running Complete Redis Cache Test Suite
echo ==========================================

rem Set the Redis password environment variable - CHANGE THIS PASSWORD!
set PANTHEON_REDIS_PASSWORD=YOUR_TEST_PASSWORD_HERE

echo Environment configured for testing
echo.

rem Run the comprehensive test suite
python test_redis_complete.py

echo.
echo Test suite completed!
pause
