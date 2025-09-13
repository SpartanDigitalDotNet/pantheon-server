# Pantheon Server

A FastAPI + Streamlit web server that provides real-time cryptocurrency analysis using the pantheon-legends package with Coinbase market data integration.

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

### 1. Setup Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your Coinbase API credentials (optional)
COINBASE_API_KEY=your_api_key_here
COINBASE_API_SECRET=your_api_secret_here
```

### 3. Run the Services

```bash
# Terminal 1: Start FastAPI backend
uvicorn src.pantheon_server.api.main:app --reload --port 8000

# Terminal 2: Start Streamlit UI
streamlit run src/pantheon_server/ui/main.py --server.port 8501
```

### 4. Access the Application

- **Streamlit UI**: http://localhost:8501
- **FastAPI Docs**: http://localhost:8000/docs
- **Test Panel**: http://localhost:8501 → 🧪 Test Panel

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
