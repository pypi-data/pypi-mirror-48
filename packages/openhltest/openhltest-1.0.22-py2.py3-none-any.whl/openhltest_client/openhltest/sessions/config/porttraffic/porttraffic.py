from openhltest_client.base import Base


class PortTraffic(Base):
	"""A list of traffic streams where each traffic stream
	has a single transmit port as its source and a list of user defined frames.

	This class supports iterators and encapsulates 0..n instances of the openhltest:sessions/config/port-traffic resource.
	"""
	YANG_NAME = 'port-traffic'
	YANG_KEYWORD = 'list'
	YANG_KEY = 'name'
	YANG_PROPERTY_MAP = {"Source": "source", "Name": "name", "Destinations": "destinations"}
	YANG_ACTIONS = []

	def __init__(self, parent):
		super(PortTraffic, self).__init__(parent)

	@property
	def Frames(self):
		"""List of user defined frames.
		The order of frames in the list will be the order of frames on the wire

		Get an instance of the Frames class.

		Returns:
			obj(openhltest_client.openhltest.sessions.config.porttraffic.frames.frames.Frames)
		"""
		from openhltest_client.openhltest.sessions.config.porttraffic.frames.frames import Frames
		return Frames(self)

	@property
	def FrameLength(self):
		"""TBD

		Get an instance of the FrameLength class.

		Returns:
			obj(openhltest_client.openhltest.sessions.config.porttraffic.framelength.framelength.FrameLength)
		"""
		from openhltest_client.openhltest.sessions.config.porttraffic.framelength.framelength import FrameLength
		return FrameLength(self)._read()

	@property
	def FrameRate(self):
		"""TBD

		Get an instance of the FrameRate class.

		Returns:
			obj(openhltest_client.openhltest.sessions.config.porttraffic.framerate.framerate.FrameRate)
		"""
		from openhltest_client.openhltest.sessions.config.porttraffic.framerate.framerate import FrameRate
		return FrameRate(self)._read()

	@property
	def Name(self):
		"""The unique name of this traffic stream

		Getter Returns:
			string

		Setter Allows:
			string

		Setter Raises:
			ValueError
			InvalidValueError
		"""
		return self._get_value('name')

	@property
	def Source(self):
		"""The transmit port of this traffic stream

		Getter Returns:
			leafref

		Setter Allows:
			leafref

		Setter Raises:
			ValueError
			InvalidValueError
		"""
		return self._get_value('source')

	@property
	def Destinations(self):
		"""The intended receive ports for this traffic stream.
		Any empty list means that any port can receive these frames.
		For a non-empty list, any frame received by a port that is not in the list will be counted as stray.

		Getter Returns:
			list(OpenHLTest.Sessions.Config.Ports.Name)

		Setter Allows:
			obj(OpenHLTest.Sessions.Config.Ports) | list(OpenHLTest.Sessions.Config.Ports.Name)

		Setter Raises:
			ValueError
			InvalidValueError
		"""
		return self._get_value('destinations')

	def read(self, Name=None):
		"""Get `port-traffic` resource(s). Returns all `port-traffic` resources from the server if no input parameters are specified.

		"""
		return self._read(Name)

	def create(self, Name, Source=None, Destinations=None):
		"""Create an instance of the `port-traffic` resource

		Args:
			Name (string): The unique name of this traffic stream
			Source (leafref): The transmit port of this traffic stream
			Destinations (leafref): The intended receive ports for this traffic stream.Any empty list means that any port can receive these frames.For a non-empty list, any frame received by a port that is not in the list will be counted as stray.
		"""
		return self._create(locals())

	def delete(self):
		"""Delete all the encapsulated instances of the retrieved `port-traffic` resource

		"""
		return self._delete()

	def update(self, Source=None, Destinations=None):
		"""Update the current instance of the `port-traffic` resource

		Args:
			Source (leafref): The transmit port of this traffic stream
			Destinations (leafref): The intended receive ports for this traffic stream.Any empty list means that any port can receive these frames.For a non-empty list, any frame received by a port that is not in the list will be counted as stray.
		"""
		return self._update(locals())

