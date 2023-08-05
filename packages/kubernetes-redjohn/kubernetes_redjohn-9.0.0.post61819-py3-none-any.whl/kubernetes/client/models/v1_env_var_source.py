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


class V1EnvVarSource(object):
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
        'config_map_key_ref': 'V1ConfigMapKeySelector',
        'field_ref': 'V1ObjectFieldSelector',
        'resource_field_ref': 'V1ResourceFieldSelector',
        'secret_key_ref': 'V1SecretKeySelector'
    }

    attribute_map = {
        'config_map_key_ref': 'configMapKeyRef',
        'field_ref': 'fieldRef',
        'resource_field_ref': 'resourceFieldRef',
        'secret_key_ref': 'secretKeyRef'
    }

    def __init__(self, config_map_key_ref=None, field_ref=None, resource_field_ref=None, secret_key_ref=None):
        """
        V1EnvVarSource - a model defined in Swagger
        """

        self._config_map_key_ref = None
        self._field_ref = None
        self._resource_field_ref = None
        self._secret_key_ref = None
        self.discriminator = None

        if config_map_key_ref is not None:
          self.config_map_key_ref = config_map_key_ref
        if field_ref is not None:
          self.field_ref = field_ref
        if resource_field_ref is not None:
          self.resource_field_ref = resource_field_ref
        if secret_key_ref is not None:
          self.secret_key_ref = secret_key_ref

    @property
    def config_map_key_ref(self):
        """
        Gets the config_map_key_ref of this V1EnvVarSource.
        Selects a key of a ConfigMap.

        :return: The config_map_key_ref of this V1EnvVarSource.
        :rtype: V1ConfigMapKeySelector
        """
        return self._config_map_key_ref

    @config_map_key_ref.setter
    def config_map_key_ref(self, config_map_key_ref):
        """
        Sets the config_map_key_ref of this V1EnvVarSource.
        Selects a key of a ConfigMap.

        :param config_map_key_ref: The config_map_key_ref of this V1EnvVarSource.
        :type: V1ConfigMapKeySelector
        """

        self._config_map_key_ref = config_map_key_ref

    @property
    def field_ref(self):
        """
        Gets the field_ref of this V1EnvVarSource.
        Selects a field of the pod: supports metadata.name, metadata.namespace, metadata.labels, metadata.annotations, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP.

        :return: The field_ref of this V1EnvVarSource.
        :rtype: V1ObjectFieldSelector
        """
        return self._field_ref

    @field_ref.setter
    def field_ref(self, field_ref):
        """
        Sets the field_ref of this V1EnvVarSource.
        Selects a field of the pod: supports metadata.name, metadata.namespace, metadata.labels, metadata.annotations, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP.

        :param field_ref: The field_ref of this V1EnvVarSource.
        :type: V1ObjectFieldSelector
        """

        self._field_ref = field_ref

    @property
    def resource_field_ref(self):
        """
        Gets the resource_field_ref of this V1EnvVarSource.
        Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.

        :return: The resource_field_ref of this V1EnvVarSource.
        :rtype: V1ResourceFieldSelector
        """
        return self._resource_field_ref

    @resource_field_ref.setter
    def resource_field_ref(self, resource_field_ref):
        """
        Sets the resource_field_ref of this V1EnvVarSource.
        Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.

        :param resource_field_ref: The resource_field_ref of this V1EnvVarSource.
        :type: V1ResourceFieldSelector
        """

        self._resource_field_ref = resource_field_ref

    @property
    def secret_key_ref(self):
        """
        Gets the secret_key_ref of this V1EnvVarSource.
        Selects a key of a secret in the pod's namespace

        :return: The secret_key_ref of this V1EnvVarSource.
        :rtype: V1SecretKeySelector
        """
        return self._secret_key_ref

    @secret_key_ref.setter
    def secret_key_ref(self, secret_key_ref):
        """
        Sets the secret_key_ref of this V1EnvVarSource.
        Selects a key of a secret in the pod's namespace

        :param secret_key_ref: The secret_key_ref of this V1EnvVarSource.
        :type: V1SecretKeySelector
        """

        self._secret_key_ref = secret_key_ref

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
        if not isinstance(other, V1EnvVarSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
