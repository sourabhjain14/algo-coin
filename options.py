from utils import config
from enums import TradingType, ExchangeType


@config
class ExchangeConfig:
    type = ExchangeType, ExchangeType.GDAX


@config
class BacktestConfig:
    file = str


@config
class RiskConfig:
    pass


@config
class ExecutionConfig:
    pass


@config
class TradingEngineConfig:
    type = TradingType, TradingType.SANDBOX
    verbose = bool, True
    exchange_options = ExchangeConfig, ExchangeConfig()
    backtest_options = BacktestConfig, BacktestConfig()
    risk_options = RiskConfig, RiskConfig()
    execution_options = ExecutionConfig, ExecutionConfig()
