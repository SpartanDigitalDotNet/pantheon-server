# Pantheon Server

A professional cryptocurrency analysis server combining FastAPI backend with Streamlit frontend, powered by the pantheon-legends package and real-time Coinbase market data.

## ✨ What This Does

Transform raw cryptocurrency market data into actionable trading insights using legendary technical analysis methods:

- **📊 Real-time Analysis**: Live market data from Coinbase Advanced Trade API
- **🏛️ Legendary Methods**: Dow Theory, Wyckoff Method, Volume Breakout Scanner  
- **📈 Professional Charts**: TradingView integration with technical indicators
- **🎯 Smart Signals**: Multi-timeframe consensus analysis with confidence scoring
- **💡 Market Overview**: Instant sentiment analysis across 20+ popular crypto pairs
- **🔄 Auto-Refresh**: Live market monitoring with customizable timeframes

## System Requirements

- **Operating System**: Windows 10+, macOS 10.15+, or Linux Ubuntu 18.04+
- **Python**: 3.8 or higher (3.9-3.12 recommended)
- **Memory**: 4GB RAM minimum, 8GB recommended  
- **Network**: Stable internet connection for real-time market data
- **Browser**: Modern web browser (Chrome, Firefox, Safari, Edge)

## Features

- 🏛️ **Pantheon Legends Integration** - Uses published pantheon-legends v0.2.0 package
- 📊 **Real-time Market Data** - Coinbase Advanced Trade API integration
- 🧪 **Interactive Test Panel** - Streamlit UI for testing crypto pairs
- 📈 **TradingView Charts** - Embedded charts with analysis overlays
- 🔗 **Discord-Friendly** - Shareable URLs for community analysis
- ⚡ **Multi-timeframe EMA(9)** - Fakeout detection across timeframes

## Architecture

```
📊 Streamlit UI (Port 8501)
├── 🧪 Test Panel for crypto analysis
├── 📈 TradingView chart integration
├── 🎯 Real-time consensus display
└── 🔗 Discord-shareable analysis pages

🌐 FastAPI Backend (Port 8000)
├── 📡 Scanner alert endpoints
├── 🧠 Pantheon analysis orchestration
├── 📊 Market data aggregation
└── 🔄 Real-time WebSocket updates

💰 Coinbase Service
├── 📈 Real-time price data
├── 🕯️ Historical candle data
├── 📊 Multi-timeframe analysis
└── ⚡ Rate-limited API calls

📦 pantheon-legends v0.2.0
└── 🏛️ Legend engine framework
```

## Quick Start

### Prerequisites

- **Python 3.8+** (tested with Python 3.9-3.12)
- **Git** for cloning the repository
- **Internet connection** for Coinbase API access

### 1. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/SpartanDigital/pantheon-server.git
cd pantheon-server

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Configuration (Optional)

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your Coinbase API credentials (optional for enhanced features)
COINBASE_API_KEY=your_api_key_here
COINBASE_API_SECRET=your_api_secret_here
```

> **Note**: The server works without API credentials using public Coinbase endpoints, but authenticated access provides more features and higher rate limits.

### 3. Start the Application

**Option A: Easy Start (Recommended)**
```bash
# Start both FastAPI backend and Streamlit UI
python run.py dev
```

**Option B: Manual Start**
```bash
# Terminal 1: Start FastAPI backend
python run.py api

# Terminal 2: Start Streamlit UI  
python run.py ui
```

**Option C: Individual Services**
```bash
# FastAPI only
uvicorn src.pantheon_server.api.main:app --reload --port 8000

# Streamlit only
streamlit run src/pantheon_server/ui/streamlit_app.py --server.port 8501
```

### 4. Verify Installation

Once the services are running, verify everything works:

1. **FastAPI Backend**: Visit http://localhost:8000/docs
   - Should show interactive API documentation
   - Test the `/health` endpoint

2. **Streamlit UI**: Visit http://localhost:8501  
   - Should load the Pantheon Server interface
   - Navigate to "Market Overview" and click "🔄 Generate Overview"
   - Check "Crypto Analysis" for individual pair analysis

3. **Test Analysis**: 
   - Select a crypto pair (e.g., BTC-USD)
   - Choose timeframe (e.g., 1h) 
   - Click "🔍 Analyze" to see TradingView charts and analysis results

## Usage

### Test Panel Workflow

1. **Select Crypto Pair**: Choose from popular pairs or enter custom symbol
2. **Configure Analysis**: Set timeframe, candle count, enable multi-timeframe
3. **Simulate Breakouts**: Test "what if" scenarios with price/volume spikes
4. **Run Analysis**: Get real-time Pantheon Legends analysis with EMA(9) fakeout detection
5. **View Results**: Interactive charts, consensus analysis, and trading recommendations

### API Integration

```python
# Send scanner alert to FastAPI endpoint
POST /api/v1/analyze
{
    "scanner_alert": {
        "symbol": "DIMO-USD",
        "price": 0.07948,
        "delta_pct": 1.31,
        "volume_ratio": 3.68,
        "timeframe": "1m"
    },
    "include_ema9": true,
    "trader_profile": "scalper"
}
```

## Development

### Project Structure

```
pantheon-server/
├── src/pantheon_server/
│   ├── api/              # FastAPI backend
│   │   ├── main.py       # FastAPI app
│   │   ├── models.py     # Request/response models
│   │   └── routes.py     # API endpoints
│   ├── services/         # External integrations
│   │   ├── coinbase.py   # Coinbase API service
│   │   └── analyzer.py   # Market analysis orchestration
│   ├── ui/               # Streamlit frontend
│   │   ├── main.py       # Main Streamlit app
│   │   ├── test_panel.py # Interactive test interface
│   │   └── charts.py     # Chart components
│   └── utils/            # Shared utilities
├── tests/                # Test suite
├── requirements.txt      # Python dependencies
└── .env.example         # Environment template
```

### Dependencies

- **pantheon-legends==0.2.0** - Core legend analysis framework
- **fastapi** - Modern web API framework
- **streamlit** - Interactive web UI
- **httpx** - Async HTTP client for Coinbase API
- **plotly** - Interactive charts and visualizations
- **pandas** - Data manipulation and analysis

## Configuration

### Environment Variables

```bash
# Coinbase API (optional - uses public endpoints if not provided)
COINBASE_API_KEY=your_coinbase_api_key
COINBASE_API_SECRET=your_coinbase_api_secret

# Server Configuration
FASTAPI_HOST=0.0.0.0
FASTAPI_PORT=8000
STREAMLIT_PORT=8501

# Analysis Configuration
DEFAULT_CANDLE_COUNT=50
DEFAULT_TIMEFRAME=1m
ENABLE_MULTI_TIMEFRAME=true
```

## Troubleshooting

### Common Issues

**1. Import Errors**
```bash
# Error: ModuleNotFoundError: No module named 'pantheon_server'
# Solution: Ensure you're in the project directory and virtual environment is activated
cd pantheon-server
.venv\Scripts\activate  # Windows
python run.py dev
```

**2. Port Already in Use**
```bash
# Error: Port 8000 or 8501 already in use
# Solution: Kill existing processes or use different ports
# Windows:
netstat -ano | findstr :8000
taskkill /PID <process_id> /F

# Or change ports in .env file
```

**3. Coinbase API Errors**
```bash
# Error: Rate limiting or API access issues
# Solution: 
# 1. Remove API credentials from .env to use public endpoints
# 2. Check API key permissions on Coinbase
# 3. Verify API key format (no extra spaces/characters)
```

**4. Virtual Environment Issues**
```bash
# Error: Package not found or wrong Python version
# Solution: Recreate virtual environment
rm -rf .venv  # or rmdir /s .venv on Windows
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Development Tips

- Use `python run.py dev` for hot-reload development
- Check `http://localhost:8000/docs` for API documentation
- Streamlit auto-refreshes on file changes
- Use Market Overview for quick market sentiment analysis

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

MIT License - see LICENSE file for details

## Related Projects

- **[pantheon-legends](https://github.com/SpartanDigitalDotNet/pantheon-legends)** - Core legend analysis framework
- **[Coinbase Advanced Trade API](https://docs.cloud.coinbase.com/advanced-trade-api/docs/welcome)** - Market data source

---

**Built with the pantheon-legends framework for comprehensive cryptocurrency market analysis** 🏛️📊
