@echo off
echo 🧪 Simple Redis Test
echo ===================

rem Set the Redis password environment variable - CHANGE THIS PASSWORD!
set PANTHEON_REDIS_PASSWORD=YOUR_TEST_PASSWORD_HERE

python test_simple.py
