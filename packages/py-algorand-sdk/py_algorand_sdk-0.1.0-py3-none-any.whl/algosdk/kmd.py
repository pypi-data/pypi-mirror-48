from urllib.request import Request, urlopen
from urllib import parse
import urllib.error
import json
import base64
from . import encoding
from . import error
from . import transaction
from . import responses
from . import constants


class kmdClient:
    """
    Client class for kmd. Handles all kmd requests.

    Args:
        kmdToken (str): kmd API token
        kmdAddress (str): kmd address

    Attributes:
        kmdToken (str)
        kmdAddress (str)
    """
    def __init__(self, kmdToken, kmdAddress):
        self.kmdToken = kmdToken
        self.kmdAddress = kmdAddress

    def kmdRequest(self, method, requrl, params=None, data=None):
        """
        Execute a given request.

        Args:
            method (str): request method
            requrl (str): url for the request
            params (dict, optional): parameters for the request
            data (dict, optional): data in the body of the request

        Returns:
            dict: loaded from json response body
        """
        if requrl in constants.noAuth:
            header = {}
        else:
            header = {
                constants.kmdAuthHeader: self.kmdToken
                }
        if requrl not in constants.unversionedPaths:
            requrl = constants.apiVersionPathPrefix + requrl
        if params:
            requrl = requrl + "?" + parse.urlencode(params)
        if data:
            data = json.dumps(data, indent=2)
            data = bytearray(data, "ascii")
        req = Request(
            self.kmdAddress+requrl, headers=header,
            method=method, data=data)
        resp = None
        try:
            resp = urlopen(req)
        except urllib.error.HTTPError as e:
            e = e.read().decode("ascii")
            try:
                raise error.KmdHTTPError(json.loads(e)["message"])
            except:
                raise error.KmdHTTPError(e)
        return json.loads(resp.read().decode("ascii"))

    def getVersion(self):
        """
        Get kmd versions.

        Returns:
            str[]: list of versions
        """
        req = "/versions"
        return self.kmdRequest("GET", req)["versions"]

    def listWallets(self):
        """
        List all wallets hosted on node.

        Returns:
            WalletResponse[]: list of objects containing wallet information
        """
        req = "/wallets"
        result = self.kmdRequest("GET", req)
        if result:
            return [responses.WalletResponse(w) for w in result["wallets"]]
        return []

    def createWallet(self, name, pswd, driver_name="sqlite",
                     master_deriv_key=None):
        """
        Create a new wallet.

        Args:
            name (str): wallet name
            pswd (str): wallet password
            driver_name (str, optional): name of the driver
            master_deriv_key (str, optional): if recovering a wallet, include

        Returns:
            WalletResponse: object containing wallet information
        """
        req = "/wallet"
        query = {
            "wallet_driver_name": driver_name,
            "wallet_name": name,
            "wallet_password": pswd
            }
        if master_deriv_key:
            query["master_derivation_key"] = master_deriv_key
        result = self.kmdRequest("POST", req, data=query)["wallet"]
        return responses.WalletResponse(result)

    def getWallet(self, handle):
        """
        Get wallet information.

        Args:
            handle (str): wallet handle token

        Returns:
            WalletHandleResponse: object containing wallet handle information
                and wallet information
        """
        req = "/wallet/info"
        query = {"wallet_handle_token": handle}
        result = self.kmdRequest("POST", req, data=query)
        return responses.WalletHandleResponse(result)

    def initWalletHandle(self, id, password):
        """
        Initialize a handle for the wallet.

        Args:
            id (str): wallet ID
            password (str): wallet password

        Returns:
            str: wallet handle token
        """
        req = "/wallet/init"
        query = {
            "wallet_id": id,
            "wallet_password": password
            }
        return self.kmdRequest("POST", req, data=query)["wallet_handle_token"]

    def releaseWalletHandle(self, handle):
        """
        Deactivate the handle for the wallet.

        Args:
        handle (str): wallet handle token

        Returns:
            bool: True if the handle has been deactivated
        """
        req = "/wallet/release"
        query = {"wallet_handle_token": handle}
        result = self.kmdRequest("POST", req, data=query)
        return result == {}

    def renewWalletHandle(self, handle):
        """
        Renew the wallet handle.

        Args:
            handle (str): wallet handle token

        Returns:
            WalletHandleResponse: object containing wallet handle information
                and wallet information
        """
        req = "/wallet/renew"
        query = {
            "wallet_handle_token": handle
            }
        result = self.kmdRequest("POST", req, data=query)
        return responses.WalletHandleResponse(result)

    def renameWallet(self, id, password, new_name):
        """
        Rename the wallet.

        Args:
            id (str): wallet ID
            password (str): wallet password
            new_name (str): new name for the wallet

        Returns:
            WalletResponse: object containing wallet information
        """
        req = "/wallet/rename"
        query = {
            "wallet_id": id,
            "wallet_password": password,
            "wallet_name": new_name
            }
        result = self.kmdRequest("POST", req, data=query)["wallet"]
        return responses.WalletResponse(result)

    def exportMasterDerivationKey(self, handle, password):
        """
        Get the wallet's master derivation key.

        Args:
            handle (str): wallet handle token
            password (str): wallet password

        Returns:
            str: master derivation key
        """
        req = "/master-key/export"
        query = {
            "wallet_handle_token": handle,
            "wallet_password": password
            }
        result = self.kmdRequest("POST", req, data=query)
        return result["master_derivation_key"]

    def importKey(self, handle, private_key):
        """
        Import an account into a wallet.

        Args:
            handle (str): wallet handle token
            private_key (str): private key of account to be imported

        Returns:
            str: base32 address of the account
        """
        req = "/key/import"
        query = {
            "wallet_handle_token": handle,
            "private_key": private_key
            }
        return self.kmdRequest("POST", req, data=query)["address"]

    def exportKey(self, handle, password, address):
        """
        Return an account private key.

        Args:
            handle (str): wallet handle token
            password (str): wallet password
            address (str): base32 address of the account

        Returns:
            str: private key
        """
        req = "/key/export"
        query = {
            "wallet_handle_token": handle,
            "wallet_password": password,
            "address": address
            }
        return self.kmdRequest("POST", req, data=query)["private_key"]

    def generateKey(self, handle, display_mnemonic=True):
        """
        Generate a key in the wallet.

        Args:
            handle (str): wallet handle token
            display_mnemonic (bool, optional): whether or not the mnemonic
                should be displayed

        Returns:
            str: base32 address of the generated account
        """
        req = "/key"
        query = {
            "wallet_handle_token": handle
            }
        return self.kmdRequest("POST", req, data=query)["address"]

    def deleteKey(self, handle, password, address):
        """
        Delete a key in the wallet.

        Args:
            handle (str): wallet handle token
            password (str): wallet password
            address (str): base32 address of account to be deleted

        Returns:
            bool: True if the account has been deleted
        """
        req = "/key"
        query = {
            "wallet_handle_token": handle,
            "wallet_password": password,
            "address": address
            }
        result = self.kmdRequest("DELETE", req, data=query)
        return result == {}

    def listKeys(self, handle):
        """
        List all keys in the wallet.

        Args:
            handle (str): wallet handle token

        Returns:
            str[]: list of base32 addresses in the wallet
        """
        req = "/key/list"
        query = {
            "wallet_handle_token": handle
            }

        result = self.kmdRequest("POST", req, data=query)
        if result:
            return result["addresses"]
        return []

    def signTransaction(self, handle, password, txn):
        """
        Sign a transaction.

        Args:
            handle (str): wallet handle token
            password (str): wallet password
            txn (Transaction): transaction to be signed

        Returns:
            SignedTransaction: signed transaction with signature of sender
        """
        # transaction is a Transaction object
        txn = encoding.msgpack_encode(txn)
        req = "/transaction/sign"
        query = {
            "wallet_handle_token": handle,
            "wallet_password": password,
            "transaction": txn
            }
        result = self.kmdRequest("POST", req, data=query)["signed_transaction"]
        return encoding.msgpack_decode(result)

    def listMultisig(self, handle):
        """
        List all multisig accounts in the wallet.

        Args:
            handle (str): wallet handle token

        Returns:
            str[]: list of base32 multisig account addresses
        """
        req = "/multisig/list"
        query = {
            "wallet_handle_token": handle
            }
        result = self.kmdRequest("POST", req, data=query)
        if result == {}:
            return []
        return result["addresses"]

    def importMultisig(self, handle, multisig):
        """
        Import a multisig account into the wallet.

        Args:
            handle (str): wallet handle token
            multisig (Multisig): multisig account to be imported

        Returns:
            str: base32 address of the imported multisig account
        """
        req = "/multisig/import"
        query = {
            "wallet_handle_token": handle,
            "multisig_version": multisig.version,
            "threshold": multisig.threshold,
            "pks": [base64.b64encode(s.public_key).decode()
                    for s in multisig.subsigs]
            }
        return self.kmdRequest("POST", req, data=query)["address"]

    def exportMultisig(self, handle, address):
        """
        Export a multisig account.

        Args:
            handle (str): wallet token handle
            address (str): base32 address of the multisig account

        Returns:
            Multisig: multisig object corresponding to the address
        """
        req = "/multisig/export"
        query = {
            "wallet_handle_token": handle,
            "address": address
            }
        result = self.kmdRequest("POST", req, data=query)
        pks = result["pks"]
        pks = [encoding.encodeAddress(base64.b64decode(p)) for p in pks]
        msig = transaction.Multisig(result["multisig_version"],
                                    result["threshold"], pks)
        return msig

    def deleteMultisig(self, handle, password, address):
        """
        Delete a multisig account.

        Args:
            handle (str): wallet handle token
            password (str): wallet password
            address (str): base32 address of the multisig account to delete

        Returns:
            bool: True if the multisig account has been deleted
        """
        req = "/multisig"
        query = {
            "wallet_handle_token": handle,
            "wallet_password": password,
            "address": address
            }
        result = self.kmdRequest("DELETE", req, data=query)
        return result == {}

    def signMultisigTransaction(self, handle, password, public_key, preStx):
        """
        Sign a multisig transaction for the given public key.

        Args:
            handle (str): wallet handle token
            password (str): wallet password
            public_key (str): base32 address that is signing the transaction
            preStx (SignedTransaction): object containing unsigned or
                partially signed multisig

        Returns:
            SignedTransaction: signed transaction with multisig containing
                public_key's signature
        """
        partial = preStx.multisig.json_dictify()
        txn = encoding.msgpack_encode(preStx.transaction)
        public_key = base64.b64encode(encoding.decodeAddress(public_key))
        public_key = public_key.decode()
        req = "/multisig/sign"
        query = {
            "wallet_handle_token": handle,
            "wallet_password": password,
            "transaction": txn,
            "public_key": public_key,
            "partial_multisig": partial
            }
        result = self.kmdRequest("POST", req, data=query)["multisig"]
        msig = encoding.msgpack_decode(result)
        preStx.multisig = msig
        return preStx

if __name__ == "__main__":
    pass
