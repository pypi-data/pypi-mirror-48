# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.14.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1alpha1VolumeError(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'message': 'str',
        'time': 'datetime'
    }

    attribute_map = {
        'message': 'message',
        'time': 'time'
    }

    def __init__(self, message=None, time=None):
        """
        V1alpha1VolumeError - a model defined in Swagger
        """

        self._message = None
        self._time = None
        self.discriminator = None

        if message is not None:
          self.message = message
        if time is not None:
          self.time = time

    @property
    def message(self):
        """
        Gets the message of this V1alpha1VolumeError.
        String detailing the error encountered during Attach or Detach operation. This string maybe logged, so it should not contain sensitive information.

        :return: The message of this V1alpha1VolumeError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this V1alpha1VolumeError.
        String detailing the error encountered during Attach or Detach operation. This string maybe logged, so it should not contain sensitive information.

        :param message: The message of this V1alpha1VolumeError.
        :type: str
        """

        self._message = message

    @property
    def time(self):
        """
        Gets the time of this V1alpha1VolumeError.
        Time the error was encountered.

        :return: The time of this V1alpha1VolumeError.
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this V1alpha1VolumeError.
        Time the error was encountered.

        :param time: The time of this V1alpha1VolumeError.
        :type: datetime
        """

        self._time = time

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1alpha1VolumeError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
