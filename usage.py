import json
import time
from polyz_functions import (
    get_market_details_by_slug,
    market_analyzer,
    market_insight_dashboard,
    price_evolution_with_fill,
    trade_analytics,
    plot_gradient_scatter_analytics,
    plot_advanced_gradient_scatter,
    plot_outcome_gradient_analytics,
    plot_advanced_distribution_gradients,
    plot_trader_strategy_analysis,
    plot_trader_timing_analysis,
)

def main():
    # Define market slug
    MARKET_SLUG = "bitcoin-up-or-down-january-30-3am-et"

    # Fetch market details
    market = get_market_details_by_slug(MARKET_SLUG)

    # General market analytics and dashboards
    market_analyzer(MARKET_SLUG)
    market_insight_dashboard(MARKET_SLUG)

    # Price evolution and trading analytics
    price_evolution_with_fill(MARKET_SLUG)
    trade_analytics(MARKET_SLUG)

    # Visualization and analytics plots
    plot_gradient_scatter_analytics(MARKET_SLUG)
    plot_advanced_gradient_scatter(MARKET_SLUG)
    plot_outcome_gradient_analytics(MARKET_SLUG)
    plot_advanced_distribution_gradients(MARKET_SLUG)

    # Trader-specific analysis
    market_slug = "bitcoin-up-or-down-january-29-8am-et"
    user_address = "0x6031b6eed1c97e853c6e0f03ad3ce3529351f96d"

    plot_trader_strategy_analysis(market_slug, user_address)
    plot_trader_timing_analysis(market_slug, user_address)




if __name__ == "__main__":
    main()