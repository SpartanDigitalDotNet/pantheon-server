@echo off
echo Running Complete Redis Cache Test Suite
echo ==========================================

rem Set the Redis password environment variable
set PANTHEON_REDIS_PASSWORD=SuperSecure123!

echo Environment configured for testing
echo.

rem Run the comprehensive test suite
python test_redis_complete.py

echo.
echo Test suite completed!
pause
