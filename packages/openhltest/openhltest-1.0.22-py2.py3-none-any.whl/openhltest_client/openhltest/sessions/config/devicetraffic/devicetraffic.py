from openhltest_client.base import Base


class DeviceTraffic(Base):
	"""This is a collection of nodes that the server uses to generate 1..n traffic-streams.
	The source and destinations of the device traffic group can only come from the device-groups list or its children.

	This class supports iterators and encapsulates 0..n instances of the openhltest:sessions/config/device-traffic resource.
	"""
	YANG_NAME = 'device-traffic'
	YANG_KEYWORD = 'list'
	YANG_KEY = 'name'
	YANG_PROPERTY_MAP = {"Name": "name", "MeshType": "mesh-type", "Sources": "sources", "BiDirectional": "bi-directional", "Encapsulation": "encapsulation", "Destinations": "destinations"}
	YANG_ACTIONS = []

	def __init__(self, parent):
		super(DeviceTraffic, self).__init__(parent)

	@property
	def Frames(self):
		"""List of user defined frames.
		Frames that are generated as part of the traffic-streams will overwrite any user defined frame leafs
		that are part of the learned info due to the endpoint-type.

		Get an instance of the Frames class.

		Returns:
			obj(openhltest_client.openhltest.sessions.config.devicetraffic.frames.frames.Frames)
		"""
		from openhltest_client.openhltest.sessions.config.devicetraffic.frames.frames import Frames
		return Frames(self)

	@property
	def FrameLength(self):
		"""TBD

		Get an instance of the FrameLength class.

		Returns:
			obj(openhltest_client.openhltest.sessions.config.devicetraffic.framelength.framelength.FrameLength)
		"""
		from openhltest_client.openhltest.sessions.config.devicetraffic.framelength.framelength import FrameLength
		return FrameLength(self)._read()

	@property
	def FrameRate(self):
		"""TBD

		Get an instance of the FrameRate class.

		Returns:
			obj(openhltest_client.openhltest.sessions.config.devicetraffic.framerate.framerate.FrameRate)
		"""
		from openhltest_client.openhltest.sessions.config.devicetraffic.framerate.framerate import FrameRate
		return FrameRate(self)._read()

	@property
	def Name(self):
		"""The unique name of a traffic group

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
	def Encapsulation(self):
		"""The encapsulation determines the following:
		What frames will be generated.
		What the traffic-streams name will be.

		Getter Returns:
			ETHERNET | VLAN | IPV4 | IPV6

		Setter Allows:
			ETHERNET | VLAN | IPV4 | IPV6

		Setter Raises:
			ValueError
			InvalidValueError
		"""
		return self._get_value('encapsulation')

	@property
	def Sources(self):
		"""A list of device source endpoint references.

		Getter Returns:
			list(OpenHLTest.Sessions.Config.DeviceGroups.Name)

		Setter Allows:
			obj(OpenHLTest.Sessions.Config.DeviceGroups) | list(OpenHLTest.Sessions.Config.DeviceGroups.Name)

		Setter Raises:
			ValueError
			InvalidValueError
		"""
		return self._get_value('sources')

	@property
	def Destinations(self):
		"""A list of device destination endpoint references.

		Getter Returns:
			list(OpenHLTest.Sessions.Config.DeviceGroups.Name)

		Setter Allows:
			obj(OpenHLTest.Sessions.Config.DeviceGroups) | list(OpenHLTest.Sessions.Config.DeviceGroups.Name)

		Setter Raises:
			ValueError
			InvalidValueError
		"""
		return self._get_value('destinations')

	@property
	def BiDirectional(self):
		"""If true then traffic-streams objects will be generated from destination DEVICES to source DEVICES.

		Getter Returns:
			boolean

		Setter Allows:
			boolean

		Setter Raises:
			ValueError
			InvalidValueError
		"""
		return self._get_value('bi-directional')

	@property
	def MeshType(self):
		"""If true then generated-traffic-streams objects will be generated from every destination DEVICES to every source DEVICES.

		Getter Returns:
			ONE_TO_ONE | FULL_MESHED

		Setter Allows:
			ONE_TO_ONE | FULL_MESHED

		Setter Raises:
			ValueError
			InvalidValueError
		"""
		return self._get_value('mesh-type')

	def read(self, Name=None):
		"""Get `device-traffic` resource(s). Returns all `device-traffic` resources from the server if no input parameters are specified.

		"""
		return self._read(Name)

	def create(self, Name, Encapsulation=None, Sources=None, Destinations=None, BiDirectional=None, MeshType=None):
		"""Create an instance of the `device-traffic` resource

		Args:
			Name (string): The unique name of a traffic group
			Encapsulation (enumeration): The encapsulation determines the following:What frames will be generated.What the traffic-streams name will be.
			Sources (union[leafref]): A list of device source endpoint references.
			Destinations (union[leafref]): A list of device destination endpoint references.
			BiDirectional (boolean): If true then traffic-streams objects will be generated from destination DEVICES to source DEVICES.
			MeshType (enumeration): If true then generated-traffic-streams objects will be generated from every destination DEVICES to every source DEVICES.
		"""
		return self._create(locals())

	def delete(self):
		"""Delete all the encapsulated instances of the retrieved `device-traffic` resource

		"""
		return self._delete()

	def update(self, Encapsulation=None, Sources=None, Destinations=None, BiDirectional=None, MeshType=None):
		"""Update the current instance of the `device-traffic` resource

		Args:
			Encapsulation (enumeration): The encapsulation determines the following:What frames will be generated.What the traffic-streams name will be.
			Sources (union[leafref]): A list of device source endpoint references.
			Destinations (union[leafref]): A list of device destination endpoint references.
			BiDirectional (boolean): If true then traffic-streams objects will be generated from destination DEVICES to source DEVICES.
			MeshType (enumeration): If true then generated-traffic-streams objects will be generated from every destination DEVICES to every source DEVICES.
		"""
		return self._update(locals())

