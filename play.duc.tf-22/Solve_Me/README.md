#### Challenge:

Aight warm up time. All you gotta do is call the solve function. You can do it!

Goal: Call the solve function! [SolveMe.sol](./SolveMe.sol ":ignore")

---

#### Solution:

- invoking the mentioned function on [web3 blockchain](https://docs.moonbeam.network/builders/build/eth-api/libraries/web3py/#interact-with-contract) will show us the flag

```python
import solcx
from web3.middleware import geth_poa_middleware
from web3 import Web3
import requests

solcx.install_solc(version='0.8.9')
solcx.set_solc_version('0.8.9')

temp_file = solcx.compile_files('SolveMe.sol')

abi = temp_file['SolveMe.sol:SolveMe']['abi']
bytecode = temp_file['SolveMe.sol:SolveMe']['bin']

rpc_enpoint = "https://blockchain-solveme-0c2898c03d6584b0-eth.2022.ductf.dev"
account_from = {
    'private_key': '0x9dda7e7b51f424ed5944829e0feaaf539f945eb785e2a16cf077f0be114286bf',
    'address': '0xfF018e26B3A0073E6D780be838Cc59BFa9f73e2B',
}
contract_address = '0x6C3900d9FcBf5F0B7beD98057FEA558D7e44faB6'

web3 = Web3(Web3.HTTPProvider(rpc_enpoint))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)
Incrementer = web3.eth.contract(address=contract_address, abi=abi)

isSolved = Incrementer.functions.isSolved().call()
if not isSolved:
    increment_tx = Incrementer.functions.solveChallenge().buildTransaction(
        {
            'from': account_from['address'],
            'nonce': web3.eth.get_transaction_count(account_from['address']),
            "gasPrice": web3.eth.gas_price,
        }
    )

    tx_create = web3.eth.account.sign_transaction(
        increment_tx, account_from['private_key'])

    tx_hash = web3.eth.send_raw_transaction(tx_create.rawTransaction)
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    print(f'Tx successful with hash: { tx_receipt.transactionHash.hex() }')


isSolved = Incrementer.functions.isSolved().call()
if isSolved:
    print(requests.get("https://blockchain-solveme-0c2898c03d6584b0.2022.ductf.dev/challenge/solve").json()['flag'])
```

---

<details><summary>FLAG:</summary>

```
DUCTF{muM_1_did_a_blonkchain!}
```

</details>
<br/>
