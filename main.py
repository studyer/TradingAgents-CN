from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# 导入日志模块
from tradingagents.utils.logging_manager import get_logger
logger = get_logger('default')


# Create a custom config
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "openai"  # Use DeepSeek-compatible
config["backend_url"] = "https://api.deepseek.com/v1"
config["deep_think_llm"] = "deepseek-v4-flash"
config["quick_think_llm"] = "deepseek-v4-flash"
config["max_debate_rounds"] = 1
config["online_tools"] = True

# Initialize with custom config
ta = TradingAgentsGraph(debug=True, config=config)

# forward propagate
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)

# Memorize mistakes and reflect
# ta.reflect_and_remember(1000) # parameter is the position returns
