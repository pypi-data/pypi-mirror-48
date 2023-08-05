from openhltest_client.base import Base


class Bfdv4Statistics(Base):
	"""TBD

	This class supports iterators and encapsulates 0..n instances of the openhltest:sessions/statistics/bfdv4-statistics resource.
	"""
	YANG_NAME = 'bfdv4-statistics'
	YANG_KEYWORD = 'list'
	YANG_KEY = 'device-name'
	YANG_PROPERTY_MAP = {"PortName": "port-name", "DeviceName": "device-name", "RxCount": "rx-count", "TxCount": "tx-count"}
	YANG_ACTIONS = []

	def __init__(self, parent):
		super(Bfdv4Statistics, self).__init__(parent)

	@property
	def DeviceName(self):
		"""Device Name

		Getter Returns:
			string
		"""
		return self._get_value('device-name')

	@property
	def PortName(self):
		"""An abstract test port name

		Getter Returns:
			string
		"""
		return self._get_value('port-name')

	@property
	def TxCount(self):
		"""Number of BFD packets sent on this router.

		Getter Returns:
			uint64
		"""
		return self._get_value('tx-count')

	@property
	def RxCount(self):
		"""Number of BFD packets received on this router.

		Getter Returns:
			uint64
		"""
		return self._get_value('rx-count')

	def read(self, DeviceName=None):
		"""Get `bfdv4-statistics` resource(s). Returns all `bfdv4-statistics` resources from the server if no input parameters are specified.

		"""
		return self._read(DeviceName)

