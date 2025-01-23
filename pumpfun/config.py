from solana.rpc.async_api import AsyncClient
from solders.keypair import Keypair #type: ignore
from solana.rpc.commitment import Confirmed

PRIV_KEY = "5NsARpuLhu2eAcH9L62oHgeRTUPvZu91LfN18Xd7VryEQpRc9Ag6RdpRuLMRUVpeST3oPBJgLzoQgwB2JuRUBBWe"
RPC = "https://api.mainnet-beta.solana.com"
UNIT_BUDGET =  100_000
UNIT_PRICE =  1_000_000
client = AsyncClient("https://api.mainnet-beta.solana.com",  commitment=Confirmed)

payer_keypair = Keypair.from_base58_string(PRIV_KEY)
