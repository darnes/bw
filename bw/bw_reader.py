import logging
from contextlib import closing

from bluetooth import BluetoothSocket, RFCOMM
from thinkgear import ThinkGearProtocol


_log = logging.getLogger(__name__)


class ReadableBluetoothSocket(BluetoothSocket):
    """
    Minor change to allow read method for BluetoothSocket, so it could be passed to ThinkGearProtocol.
    """
    def read(self, n):
        return self.recv(n)


class BWReader(object):
    """Encapsulates bluetooth connection and thinkgear functionality.

    >>> from thinkgear import ThinkGearAttentionData
    >>> bw = BWReader(device)
    >>> for d in bw.get_packets():
    ...     if isinstance(d, ThinkGearAttentionData) and d.value == 100:
    ...         print "You win!"
    ...         break

    """
    def __init__(self, address='00:13:EF:00:4F:F2', port=3):
        self._address = address
        self._port = port
        self._socket = None
        self._tg = None

    def connect(self):
        _log.debug('connecting')
        self._socket = ReadableBluetoothSocket(RFCOMM)
        self._socket.connect((self._address, self._port))
        self._tg = ThinkGearProtocol(self._socket)

    def get_packets(self):
        if not self._socket:
            self.connect()

        with closing(self):
            for data_packet in self._tg.get_packets():
                for d in data_packet:
                    yield d

    def close(self):
        _log.debug('closing socket')
        if self._socket:
            self._socket.close()
            self._socket = None
