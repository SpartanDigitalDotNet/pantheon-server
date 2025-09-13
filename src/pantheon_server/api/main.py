"""
Pantheon Server API

This module provides the main FastAPI application for the Pantheon Server,
exposing REST endpoints for cryptocurrency analysis and market data.
"""

import os
from datetime import datetime
from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from legends import LegendType, Pantheon
from pydantic import BaseModel
from dotenv import load_dotenv

from ..services import CoinbaseService, PantheonMarketAnalyzer

# Load environment variables
load_dotenv()

# Initialize services
coinbase_service = CoinbaseService()
market_analyzer = PantheonMarketAnalyzer(coinbase_service)

app = FastAPI(
    title="Pantheon Server",
    description="Cryptocurrency analysis server using Pantheon Legends framework",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic models for request/response
class AnalysisRequest(BaseModel):
    product_id: str
    legend_type: LegendType = LegendType.TRADITIONAL
    timeframes: Optional[List[str]] = ["5m", "15m", "1h"]
    max_candles: int = 200


class ScanRequest(BaseModel):
    product_ids: List[str]
    legend_type: LegendType = LegendType.SCANNER
    timeframe: str = "5m"
    max_candles: int = 100


@app.get("/")
async def root() -> Dict[str, str]:
    """Root endpoint returning basic server information"""
    try:
        return {
            "service": "Pantheon Server",
            "version": "0.1.0",
            "description": "Cryptocurrency analysis using Pantheon Legends",
            "timestamp": datetime.utcnow().isoformat(),
            "docs": "/docs",
            "endpoints": {
                "health": "/health",
                "engines": "/engines",
                "products": "/products",
                "analyze": "/analyze",
                "scan": "/scan",
                "ema9": "/ema9/{product_id}",
                "overview": "/overview"
            }
        }
    except Exception as e:
        return {"error": str(e), "type": type(e).__name__}


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "pantheon-server",
        "pantheon_legends": "connected",
        "coinbase_api": "available"
    }


@app.get("/test")
async def test_endpoint() -> Dict[str, str]:
    """Simple test endpoint for debugging"""
    return {"message": "Server is working!", "status": "ok"}


@app.get("/engines")
async def list_engines() -> Dict[str, List[str]]:
    """List available analysis engines"""
    try:
        pantheon = Pantheon.create_default()
        engines = pantheon.available_engines
        return {
            "available_engines": list(engines),
            "timestamp": datetime.utcnow().isoformat(),
            "descriptions": {
                "traditional": "Classic technical analysis with traditional indicators",
                "scanner": "Advanced scanning engine for pattern detection"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving engines: {str(e)}")


@app.get("/products")
async def get_products() -> Dict:
    """Get available cryptocurrency trading pairs"""
    try:
        products = await coinbase_service.get_products()
        popular_pairs = coinbase_service.get_popular_crypto_pairs()
        
        return {
            "total_products": len(products),
            "popular_pairs": popular_pairs,
            "all_products": [p.get("id") for p in products if p.get("id")],
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching products: {str(e)}")


@app.post("/analyze")
async def analyze_crypto(request: AnalysisRequest) -> Dict:
    """Analyze a cryptocurrency pair using specified engine and timeframes"""
    try:
        result = await market_analyzer.analyze_crypto_pair(
            product_id=request.product_id,
            engine_type=request.engine_type,
            timeframes=request.timeframes,
            max_candles=request.max_candles
        )
        
        return {
            "success": True,
            "request": request.dict(),
            "results": result,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


@app.post("/scan")
async def scan_multiple_pairs(request: ScanRequest) -> Dict:
    """Scan multiple cryptocurrency pairs for trading opportunities"""
    try:
        results = await market_analyzer.scan_multiple_pairs(
            product_ids=request.product_ids,
            engine_type=request.engine_type,
            timeframe=request.timeframe,
            max_candles=request.max_candles
        )
        
        # Count successful vs failed scans
        successful = sum(1 for r in results.values() if "error" not in r)
        failed = len(results) - successful
        
        return {
            "success": True,
            "request": request.dict(),
            "summary": {
                "total_pairs": len(request.product_ids),
                "successful_scans": successful,
                "failed_scans": failed,
                "success_rate": (successful / len(request.product_ids)) * 100
            },
            "results": results,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Scan failed: {str(e)}")


@app.get("/ema9/{product_id}")
async def ema9_fakeout_analysis(product_id: str, max_candles: int = 200) -> Dict:
    """Run EMA(9) fakeout analysis on a specific cryptocurrency pair"""
    try:
        signals = await market_analyzer.get_ema9_fakeout_signals(
            product_id=product_id,
            max_candles=max_candles
        )
        
        return {
            "success": True,
            "product_id": product_id,
            "strategy": "EMA(9) Multi-timeframe Fakeout Detection",
            "signals": signals,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"EMA(9) analysis failed: {str(e)}")


@app.get("/overview")
async def market_overview(
    popular_only: bool = True,
    legend_type: LegendType = LegendType.TRADITIONAL
) -> Dict:
    """Get a comprehensive market overview across multiple cryptocurrency pairs"""
    try:
        overview = await market_analyzer.get_market_overview(
            popular_pairs_only=popular_only,
            legend_type=legend_type
        )
        
        return {
            "success": True,
            "overview": overview,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Market overview failed: {str(e)}")


@app.get("/ticker/{product_id}")
async def get_ticker(product_id: str) -> Dict:
    """Get current ticker information for a cryptocurrency pair"""
    try:
        ticker = await coinbase_service.get_product_ticker(product_id)
        
        return {
            "success": True,
            "product_id": product_id,
            "ticker": ticker,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ticker fetch failed: {str(e)}")


@app.get("/candles/{product_id}")
async def get_candles(
    product_id: str,
    timeframe: str = "300",
    max_candles: int = 100
) -> Dict:
    """Get historical candle data for a cryptocurrency pair"""
    try:
        df = await coinbase_service.get_product_candles(
            product_id=product_id,
            timeframe=timeframe,
            max_candles=max_candles
        )
        
        # Convert DataFrame to JSON-serializable format
        candles_data = []
        for timestamp, row in df.iterrows():
            candles_data.append({
                "timestamp": timestamp.isoformat(),
                "open": float(row['open']),
                "high": float(row['high']),
                "low": float(row['low']),
                "close": float(row['close']),
                "volume": float(row['volume'])
            })
        
        return {
            "success": True,
            "product_id": product_id,
            "timeframe": timeframe,
            "candle_count": len(candles_data),
            "candles": candles_data,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Candles fetch failed: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    
    # Load environment variables
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    reload = os.getenv("RELOAD", "true").lower() == "true"
    
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=reload
    )
