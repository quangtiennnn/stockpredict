from tti.indicators import *
from StockData import StockData

SHEET_NAME = "stockpredict"


class StockAnalysis:
    def __init__(self, input_data: StockData):
        self.df = input_data
        self.point = self.get_point()

    def get_point(self):
        """BOLLINGER BAND"""
        BB_indicator = BollingerBands(input_data=self.df)
        """FIBONACCI RETRACEMENT"""
        FIBO_indicator = FibonacciRetracement(input_data=self.df)
        """MOVING AVERAGE CONVERGENCE DIVERGENCE"""
        MACD_indicator = MovingAverageConvergenceDivergence(input_data=self.df)
        """RELATIVE STRENGTH INDEX"""
        RSI_indicator = RelativeStrengthIndex(input_data=self.df)
        """ICHIMOKU CLOUD"""
        IC_indicator = IchimokuCloud(input_data=self.df)
        """WILLIAM'S R"""
        WR_indicator = WilliamsR(input_data=self.df)
        """ON BALANCE VOLUME"""
        OBV_indicator = OnBalanceVolume(input_data=self.df)
        output = {
            SHEET_NAME: {
                "bb": BB_indicator.getTiSignal()[1],
                "fibo": FIBO_indicator.getTiSignal()[1],
                "macd": MACD_indicator.getTiSignal()[1],
                "rsi": RSI_indicator.getTiSignal()[1],
                "ic": IC_indicator.getTiSignal()[1],
                "wr": WR_indicator.getTiSignal()[1],
                "obv": OBV_indicator.getTiSignal()[1],
            }
        }
        return output