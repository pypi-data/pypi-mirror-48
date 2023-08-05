from openhltest_client.base import Base


class EthernetType(Base):
	"""Ethernet type.
	Common values are 88B5 86DD 0800
	"""
	YANG_NAME = 'ethernet-type'
	YANG_KEYWORD = 'container'
	YANG_KEY = None
	YANG_PROPERTY_MAP = {"Count": "count", "PatternType": "pattern-type", "PatternFormat": "pattern-format", "Single": "single", "ValueList": "value-list", "StatisticTracking": "statistic-tracking"}
	YANG_ACTIONS = []

	def __init__(self, parent):
		super(EthernetType, self).__init__(parent)

	@property
	def Increment(self):
		"""The values that make up the increment pattern

		Get an instance of the Increment class.

		Returns:
			obj(openhltest_client.openhltest.sessions.config.porttraffic.frames.ethernet.ethernettype.increment.increment.Increment)
		"""
		from openhltest_client.openhltest.sessions.config.porttraffic.frames.ethernet.ethernettype.increment.increment import Increment
		return Increment(self)._read()

	@property
	def Decrement(self):
		"""TBD

		Get an instance of the Decrement class.

		Returns:
			obj(openhltest_client.openhltest.sessions.config.porttraffic.frames.ethernet.ethernettype.decrement.decrement.Decrement)
		"""
		from openhltest_client.openhltest.sessions.config.porttraffic.frames.ethernet.ethernettype.decrement.decrement import Decrement
		return Decrement(self)._read()

	@property
	def Random(self):
		"""The repeatable random pattern.

		Get an instance of the Random class.

		Returns:
			obj(openhltest_client.openhltest.sessions.config.porttraffic.frames.ethernet.ethernettype.random.random.Random)
		"""
		from openhltest_client.openhltest.sessions.config.porttraffic.frames.ethernet.ethernettype.random.random import Random
		return Random(self)._read()

	@property
	def PatternType(self):
		"""The selected pattern from the possible pattern types.

		Getter Returns:
			SINGLE | INCREMENT | DECREMENT | RANDOM | VALUE_LIST

		Setter Allows:
			SINGLE | INCREMENT | DECREMENT | RANDOM | VALUE_LIST

		Setter Raises:
			ValueError
			InvalidValueError
		"""
		return self._get_value('pattern-type')

	@property
	def PatternFormat(self):
		"""The format of the pattern.
		This will almost always be a regular expression.
		It is used to determine the validity of the values being set in the child leaf nodes of the pattern.

		Getter Returns:
			string
		"""
		return self._get_value('pattern-format')

	@property
	def Single(self):
		"""The value of the single pattern

		Getter Returns:
			string

		Setter Allows:
			string

		Setter Raises:
			ValueError
			InvalidValueError
		"""
		return self._get_value('single')

	@property
	def ValueList(self):
		"""The value list pattern takes a list of values that will be repeated if they do not meet or exceed the count

		Getter Returns:
			string

		Setter Allows:
			string

		Setter Raises:
			ValueError
			InvalidValueError
		"""
		return self._get_value('value-list')

	@property
	def Count(self):
		"""The count of the pattern

		Getter Returns:
			int32

		Setter Allows:
			int32

		Setter Raises:
			ValueError
			InvalidValueError
		"""
		return self._get_value('count')

	@property
	def StatisticTracking(self):
		"""Flag to identify the parent pattern container as a candidate for statistic tracking

		Getter Returns:
			boolean

		Setter Allows:
			boolean

		Setter Raises:
			ValueError
			InvalidValueError
		"""
		return self._get_value('statistic-tracking')

	def update(self, PatternType=None, PatternFormat=None, Single=None, ValueList=None, Count=None, StatisticTracking=None):
		"""Update the current instance of the `ethernet-type` resource

		Args:
			PatternType (enumeration): The selected pattern from the possible pattern types.
			PatternFormat (string): The format of the pattern.This will almost always be a regular expression.It is used to determine the validity of the values being set in the child leaf nodes of the pattern.
			Single (string): The value of the single pattern
			ValueList (string): The value list pattern takes a list of values that will be repeated if they do not meet or exceed the count
			Count (int32): The count of the pattern
			StatisticTracking (boolean): Flag to identify the parent pattern container as a candidate for statistic tracking
		"""
		return self._update(locals())

