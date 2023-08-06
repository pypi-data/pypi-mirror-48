# this file takes optional arguments, arg1 = amount to spend, arg2 = recipient address, arg3 = operation, arg4=OpenField data
# args3+4 are not prompted if ran without args

import base64
import sqlite3
import sys
import time

import socks
from Cryptodome.Hash import SHA
from Cryptodome.Signature import PKCS1_v1_5

import connections
import essentials
import options
from essentials import fee_calculate, address_validate

# TODO: make use of polysign and transaction object.
if __name__ == "__main__":
    config = options.Get()
    config.read()
    ledger_path = config.ledger_path
    hyper_path = config.hyper_path

    key, public_key_readable, private_key_readable, encrypted, unlocked, public_key_b64encoded, address, keyfile = essentials.keys_load_new("wallet.der")

    if encrypted:
        key, private_key_readable = essentials.keys_unlock(private_key_readable)

    print('Number of arguments: %d arguments.' % len(sys.argv))
    print('Argument List: %s' % ', '.join(sys.argv))

    # get balance
    if 'regnet' in config.version:
        debit_mempool = 0
    else:
        # include mempool fees
        mempool = sqlite3.connect('mempool.db')
        mempool.text_factory = str
        m = mempool.cursor()
        m.execute("SELECT count(amount), sum(amount) FROM transactions WHERE address = ?;", (address,))
        result = m.fetchall()[0]
        if result[1] is None:
            debit_mempool = 0
        else:
            debit_mempool = float('%.8f' % (float(result[1]) + float(result[1]) * 0.001 + int(result[0]) * 0.01))
        # include mempool fees

    conn = sqlite3.connect(ledger_path)
    conn.text_factory = str
    c = conn.cursor()

    s = socks.socksocket()
    s.settimeout(10)
    # s.connect(("bismuth.live", 5658))
    if 'regnet' in config.version:
        s.connect(("127.0.0.1", 3030))
    else:
        s.connect(("127.0.0.1", 5658))

    connections.send (s, "balanceget")
    connections.send (s, address)  # change address here to view other people's transactions
    stats_account = connections.receive (s)
    balance = stats_account[0]

    print("Transaction address: %s" % address)
    print("Transaction address balance: %s" % balance)

    try:
        amount_input = sys.argv[1]
    except IndexError:
        amount_input = input("Amount: ")

    try:
        recipient_input = sys.argv[2]
    except IndexError:
        recipient_input = input("Recipient: ")

    if not address_validate(recipient_input):
        print("Wrong recipient address format")
        exit(1)

    try:
        operation_input = sys.argv[3]
    except IndexError:
        operation_input = ""

    try:
        openfield_input = sys.argv[4]
    except IndexError:
        openfield_input = input("Enter openfield data (message): ")

    # hardfork fee display
    fee = fee_calculate(openfield_input)
    print("Fee: %s" % fee)

    confirm = input("Confirm (y/n): ")

    if confirm != 'y':
        print("Transaction cancelled, user confirmation failed")
        exit(1)

    # hardfork fee display
    try:
        float(amount_input)
        is_float = 1
    except ValueError:
        is_float = 0
        exit(1)

    timestamp = '%.2f' % time.time()
    transaction = (str(timestamp), str(address), str(recipient_input), '%.8f' % float(amount_input), str(operation_input), str(openfield_input))  # this is signed
    print(transaction)

    h = SHA.new(str(transaction).encode("utf-8"))
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(h)
    signature_enc = base64.b64encode(signature)
    txid = signature_enc[:56]

    print("Encoded Signature: %s" % signature_enc.decode("utf-8"))
    print("Transaction ID: %s" % txid.decode("utf-8"))

    verifier = PKCS1_v1_5.new(key)

    if verifier.verify(h, signature):
        if float(amount_input) < 0:
            print("Signature OK, but cannot use negative amounts")

        elif float(amount_input) + float(fee) > float(balance):
            print("Mempool: Sending more than owned")

        else:
            tx_submit = (str (timestamp), str (address), str (recipient_input), '%.8f' % float (amount_input), str (signature_enc.decode ("utf-8")), str (public_key_b64encoded.decode("utf-8")), str (operation_input), str (openfield_input))
            connections.send (s, "mpinsert")
            connections.send (s, tx_submit)
            reply = connections.receive (s)
            print ("Client: {}".format (reply))
    else:
        print("Invalid signature")
        # enter transaction end

    s.close()
