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


class V1DeploymentStrategy(object):
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
        'rolling_update': 'V1RollingUpdateDeployment',
        'type': 'str'
    }

    attribute_map = {
        'rolling_update': 'rollingUpdate',
        'type': 'type'
    }

    def __init__(self, rolling_update=None, type=None):
        """
        V1DeploymentStrategy - a model defined in Swagger
        """

        self._rolling_update = None
        self._type = None
        self.discriminator = None

        if rolling_update is not None:
          self.rolling_update = rolling_update
        if type is not None:
          self.type = type

    @property
    def rolling_update(self):
        """
        Gets the rolling_update of this V1DeploymentStrategy.
        Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.

        :return: The rolling_update of this V1DeploymentStrategy.
        :rtype: V1RollingUpdateDeployment
        """
        return self._rolling_update

    @rolling_update.setter
    def rolling_update(self, rolling_update):
        """
        Sets the rolling_update of this V1DeploymentStrategy.
        Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.

        :param rolling_update: The rolling_update of this V1DeploymentStrategy.
        :type: V1RollingUpdateDeployment
        """

        self._rolling_update = rolling_update

    @property
    def type(self):
        """
        Gets the type of this V1DeploymentStrategy.
        Type of deployment. Can be \"Recreate\" or \"RollingUpdate\". Default is RollingUpdate.

        :return: The type of this V1DeploymentStrategy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1DeploymentStrategy.
        Type of deployment. Can be \"Recreate\" or \"RollingUpdate\". Default is RollingUpdate.

        :param type: The type of this V1DeploymentStrategy.
        :type: str
        """

        self._type = type

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
        if not isinstance(other, V1DeploymentStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
