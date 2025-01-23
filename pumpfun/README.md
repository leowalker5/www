import nest_asyncio
import asyncio
import time
from base58 import b58decode, b58encode
from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solders.transaction import Transaction
from solders.message import Message
from solders.instruction import Instruction
from solders.system_program import CreateAccountParams, create_account, TransferParams, transfer
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Confirmed

nest_asyncio.apply()
from pumpfun import pump_fun
coin = '8pbcncFt7Zp2QX5zm5T76Rx1v2RZH4gHnqwBLdjZpump'

asyncio.run(pump_fun.sell(coin,100,10))#(代币地址，卖出百分比没用多少都是清仓，滑点)
asyncio.run(pump_fun.buy(coin,0.01,10))#(代币地址，购买sol数量，滑点)