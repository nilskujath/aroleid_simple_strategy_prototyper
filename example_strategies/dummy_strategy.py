from aroleid_simple_strategy_prototyper import Backtester
import pandas as pd
import logging

logging.getLogger("aroleid_simple_strategy_prototyper").setLevel(logging.DEBUG)


class DummyStrategy(Backtester):
    def add_indicators(self) -> None:
        pass

    def strategy(self, row: pd.Series) -> None:
        pass


if __name__ == "__main__":
    backtester = DummyStrategy()
    backtester.load_historical_market_data(
        path_to_dbcsv="./csv_port/glbx-mdp3-20241202-20241205.ohlcv-1s.csv",
        symbol="MNQZ4",
    )
