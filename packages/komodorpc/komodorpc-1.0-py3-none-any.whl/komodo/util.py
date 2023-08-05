import rpc_util.rpc as rpc


def createmultisig(number_required=1, keys=['']):
    '''
    The createmultisig method creates a multi-signature address with
    n signature(s) of m key(s) required.
    :param number_required: (numeric, required)	the number of required
        signatures out of the n key(s) or address(es)
    :param keys: [string, required]	a list of keys (string) which are
        addresses or hex-encoded public keys
    :return: JSON string containing:
        "address" (string) the value of the new multisig address
        "redeemScript" (string)	the string value of the hex-encoded
            redemption script
    '''
    key_list = "[";
    for addr in keys:
        key_list += "\"" + str(addr) + "\","
    if (len(keys) > 0):
        key_list = key_list[:-1]
    key_list += "]";
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "createmultisig", ' \
                '"params": [' + str(number_required) +\
                    ', ' + str(key_list) + '] }'
    return rpc.rpc_request(data)


def decodeccopret(scriptPubKey=''):
    '''
    The decodeccopret method decodes the OP RETURN data from
    a CC transaction to output the EVALCODE and function id of
    the method that produced the transaction.
    :param scriptPubKey: (string) the hex-string format scriptPubKey
        of the type : nulldata in the vout of a transaction produced
        by a CC module
    :return: JSON string containing:
        result (string) whether the call succeeded
        OpRets (json) a json containing the keys EVALCODE and function id
        eval_code (hexadecimal number) the EVALCODE of the method that
            produced the transaction.
        function (string) the function id of the method that produced the
            transaction.
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "decodeccopret", ' \
                '"params": ["' + scriptPubKey + '"] }'
    return rpc.rpc_request(data)


def estimatefee(num_blocks=0):
    '''
    The estimatefee method estimates the approximate fee per kilobyte.
    The method is needed for a transaction to begin confirmation within
    nblocks blocks. The value -1.0 is returned if not enough transactions
    and blocks have been observed to make an estimate.
    :param num_blocks: (numeric) the number of blocks within which
        the fee should be tested
    :return: number (JSON string) the estimated fee
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "estimatefee", ' \
                '"params": [' + str(num_blocks) + '] }'
    return rpc.rpc_request(data)


def estimatepriority(num_blocks=0):
    '''
    The estimatepriority method estimates the approximate priority of
    a zero-fee transaction, when it needs to begin confirmation within
    nblocks blocks. The value -1.0 is returned if not enough transactions
    and blocks have been observed to make an estimate
    :param num_blocks: (numeric) a statement indicating within how many
        blocks the transaction should be confirmed
    :return: number	(numeric) the estimated priority
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "estimatepriority", ' \
                '"params": [' + str(num_blocks) + '] }'
    return rpc.rpc_request(data)


def invalidateblock(block_hash=''):
    '''
    The invalidateblock method permanently marks a block as invalid,
    as if it violated a consensus rule.
    :param block_hash: (string, required) the hash of the block to
        mark as invalid
    :return: JSON string
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "invalidateblock", ' \
                '"params": ["' + str(block_hash) + '"] }'
    return rpc.rpc_request(data)


def reconsiderblock(block_hash=''):
    '''
    The reconsiderblock method removes invalidity status of a block
    and its descendants, reconsidering them for activation.
    :param block_hash: (string, required) the hash of the block
        to reconsider
    :return: JSON string
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "reconsiderblock", ' \
                '"params": ["' + str(block_hash) + '"] }'
    return rpc.rpc_request(data)


def txnotarizedconfirmed(tx_id=''):
    '''
    The txnotarizedconfirmed method returns information about
        a transaction's state of confirmation.
    :param tx_id: (string, required) the transaction id
    :return: "result" (JSON string) whether the transaction is
        confirmed, for dPoW-based chains;
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "txnotarizedconfirmed", ' \
                '"params": ["' + str(tx_id) + '"] }'
    return rpc.rpc_request(data)


def validateaddress(address=''):
    '''
    The validateaddress method returns information about the given address.
    :param address: (string, required) the address to validate
    :return: JSON string containing:
        "isvalid" (boolean) indicates whether the address is valid.
            If it is not, this is the only property returned.
        "address" (string) the address validated
        "scriptPubKey" (string) the hex encoded scriptPubKey generated by
            the address
        "ismine" (boolean) indicates whether the address is yours
        "isscript" (boolean) whether the key is a script
        "pubkey" (string) the hex value of the raw public key
        "iscompressed" (boolean) whether the address is compressed
        "account" (string) DEPRECATED the account associated with the
            address; "" is the default account
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "validateaddress", ' \
                '"params": ["' + str(address) + '"] }'
    return rpc.rpc_request(data)


def verifymessage(address='', signature='', message=''):
    '''
    The verifymessage method verifies a signed message.
    :param address: (string, required) the address to use for
        the signature
    :param signature: (string, required) the signature provided
        by the signer in base 64 encoding
    :param message: (string, required)	the message that was signed
    :return: true/false	(JSON string) indicates whether the signature
        is verified
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "verifymessage", ' \
                '"params": ["' + str(address) + '", "' + str(signature) +\
                    '", "' + str(message) + '"] }'
    return rpc.rpc_request(data)


def z_validateaddress(address=''):
    '''
    The z_validateaddress method returns information about
    the given z address.
    :param address: "zaddr"	(string, required) the z address
        to validate
    :return: JSON string containing:
        "isvalid" (boolean) indicates whether the address is valid;
            if not, this is the only property returned
        "address" (string) the z address validated
        "ismine" (boolean) indicates if the address is yours or not
        "payingkey" (string) the hex value of the paying key, a_pk
        "transmissionkey" (string) the hex value of the transmission
            key, pk_enc
    '''
    data = '{'+rpc.get_request_metadata()+', ' \
                '"method": "z_validateaddress", ' \
                '"params": ["' + str(address) + '"] }'
    return rpc.rpc_request(data)

