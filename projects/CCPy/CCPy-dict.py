
# CPP Version (major, minor)
CCP_version = (2,1)

# Table of Command Codes
cmd = {
        # non-optionall commands
        'CONNECT':0x01,
        'GET_CCP_VERSION': 0x1B,
        'EXCHANGE_ID': 0x17, 
        'SET_MTA': 0x02, 
        'DNLOAD': 0x03, 
        'UPLOAD': 0x04, 
        'GET_DAQ_SIZE': 0x14, 
        'SET_DAQ_PTR': 0x15, 
        'WRITE_DAQ': 0x16, 
        'START_STOP': 0x06, 
        'DISCONNECT': 0x07, 
        # Optional commands
        'SELECT_CAL_PAGE': 0x11, 
        'GET_SEED': 0x12,  
        'UNLOCK': 0x13, 
        'DNLOAD_6': 0x23, 
        'SHORT_UP': 0x0F, 
        'SET_S_STATUS': 0x0C,
        'GET_S_STATUS': 0x0D,
        'BUILD_CHKSUM': 0x0E,
        'CLEAR_MEMORY': 0x10,
        'PROGRAM': 0x18, 
        'PROGRAM_6': 0x22, 
        'MOVE': 0x19,
        'TEST': 0x05,
        'GET_ACTIVE_CAL_PAGE': 0x09,
        'START_STOP_ALL': 0x08,
        'DIAG_SERVICE': 0x20,
        'ACTION_SERVICE': 0x21
        }

# Table of Command Return Codes

# Category | Description                         | Action        | Retries
# -----------------------------------------------------------------------------
# timeout  |  no handshake message               | retry         |  2
# C0       | warning                             | -             | -
# C1       | spurious (comm error, busy, ...)    | wait (ACK or timeout) | 2
# C2       | resolvable (temp. power loss, ...)  | reinitialize  | 1
# C3       | unresolvable (setup, overload, ...) | terminate     | -        

cmd_rc = {
        'ACK': 0x00, # Acknowledge / no error
        'DAQ_PROCESSOR_OVERLOAD': 0x01,     # C0
        'COMMAND_PROCESSOR_BUSY': 0x10,     # C1 NONE (wait until ACK or timeout)
        'DAQ_PROCESSOR_BUSY': 0x11,         # C1 NONE (wait until ACK or timeout)
        'INTERNAL_TIMOUT': 0x12,            # C1 NONE (wait until ACK or timeout)
        'KEY_REQUEST': 0x18,                # C1 NONE (embedded seed&key)
        'SESSION_STATUS_REQUEST': 0x19      # C1 NONE (embedded SET_S_STATUS)
        'COLD_START_REQUEST': 0x20,         # C2 COLD STAR
        'CAL_DATA_INIT_REQUEST': 0x21,      # C2 cal. data initialization
        'DAQ_LIST_INIT_REQUEST': 0x22,      # C2 DAQ list initialization
        'CODE_UPDATE_REQUEST': 0x23,        # C2 (COLD START)
        'UNKNOWN_COMMAND': 0x30,            # C3 (FAULT)
        'COMMAND_SYNTAX': 0x31,             # C3 FAULT
        'PARAMETERS_OUT_OF_RANGE': 0x32,    # C3 FAULT
        'ACCESS_DENIED': 0x33,              # C3 FAULT
        'OVERLOAD': 0x34,                   # C3 FAULT
        'ACCESS_LOCKED': 0x35,              # C3 FAULT
        'RESOURCE_FUNCTION_NOT_AVAILABLE': 0x36,    # C3 FAULT
        }

# If errors occur asynchroneously to protocol commands, the CCP slave device may
# also directly invoke appropriate error handling by sending error codes as
# Event Messages (Packet ID 0xFE).

