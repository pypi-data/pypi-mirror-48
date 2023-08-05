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


class V1Handler(object):
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
        '_exec': 'V1ExecAction',
        'http_get': 'V1HTTPGetAction',
        'tcp_socket': 'V1TCPSocketAction'
    }

    attribute_map = {
        '_exec': 'exec',
        'http_get': 'httpGet',
        'tcp_socket': 'tcpSocket'
    }

    def __init__(self, _exec=None, http_get=None, tcp_socket=None):
        """
        V1Handler - a model defined in Swagger
        """

        self.__exec = None
        self._http_get = None
        self._tcp_socket = None
        self.discriminator = None

        if _exec is not None:
          self._exec = _exec
        if http_get is not None:
          self.http_get = http_get
        if tcp_socket is not None:
          self.tcp_socket = tcp_socket

    @property
    def _exec(self):
        """
        Gets the _exec of this V1Handler.
        One and only one of the following should be specified. Exec specifies the action to take.

        :return: The _exec of this V1Handler.
        :rtype: V1ExecAction
        """
        return self.__exec

    @_exec.setter
    def _exec(self, _exec):
        """
        Sets the _exec of this V1Handler.
        One and only one of the following should be specified. Exec specifies the action to take.

        :param _exec: The _exec of this V1Handler.
        :type: V1ExecAction
        """

        self.__exec = _exec

    @property
    def http_get(self):
        """
        Gets the http_get of this V1Handler.
        HTTPGet specifies the http request to perform.

        :return: The http_get of this V1Handler.
        :rtype: V1HTTPGetAction
        """
        return self._http_get

    @http_get.setter
    def http_get(self, http_get):
        """
        Sets the http_get of this V1Handler.
        HTTPGet specifies the http request to perform.

        :param http_get: The http_get of this V1Handler.
        :type: V1HTTPGetAction
        """

        self._http_get = http_get

    @property
    def tcp_socket(self):
        """
        Gets the tcp_socket of this V1Handler.
        TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported

        :return: The tcp_socket of this V1Handler.
        :rtype: V1TCPSocketAction
        """
        return self._tcp_socket

    @tcp_socket.setter
    def tcp_socket(self, tcp_socket):
        """
        Sets the tcp_socket of this V1Handler.
        TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported

        :param tcp_socket: The tcp_socket of this V1Handler.
        :type: V1TCPSocketAction
        """

        self._tcp_socket = tcp_socket

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
        if not isinstance(other, V1Handler):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
