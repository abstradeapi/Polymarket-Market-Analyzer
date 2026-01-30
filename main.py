from py_clob_client.client import ClobClient, OrderArgs
from py_clob_client.clob_types import MarketOrderArgs, OrderType
from py_clob_client.order_builder.constants import BUY, SELL
import os
import json
import requests
from datetime import datetime, timezone
import re
from typing import Dict, Optional, Tuple, List
import time
import pytz
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from web3 import Web3
from eth_account import Account
from eth_abi import encode
import statistics
from functools import wraps
from py_clob_client.clob_types import OpenOrderParams
import requests
import re
import json
from datetime import datetime, timedelta
import pytz
from typing import List, Dict, Optional
from typing import Any
import websocket
import json
import threading
import time
from dotenv import load_dotenv
from eth_utils import to_checksum_address, keccak
from eth_abi import encode
from decimal import Decimal
import os
from py_builder_relayer_client.client import RelayClient
from py_builder_relayer_client.models import OperationType, SafeTransaction
from py_builder_signing_sdk.config import BuilderConfig, BuilderApiKeyCreds
from py_clob_client.clob_types import OrderArgs, PostOrdersArgs, OrderType
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
import pandas as pd
from scipy.ndimage import gaussian_filter





HOST = "https://clob.polymarket.com"
CHAIN_ID = 137
POLYMARKET_PROXY_ADDRESS = ''

CTF_ADDRESS = to_checksum_address("")
USDC_ADDRESS = to_checksum_address("")
RELAYER_URL = "https://relayer-v2.polymarket.com"
CHAIN_ID = 137
PARENT_COLLECTION_ID = "0x0000000000000000000000000000000000000000000000000000000000000000"



.....


