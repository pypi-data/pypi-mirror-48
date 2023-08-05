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


class V1ConfigMapNodeConfigSource(object):
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
        'kubelet_config_key': 'str',
        'name': 'str',
        'namespace': 'str',
        'resource_version': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'kubelet_config_key': 'kubeletConfigKey',
        'name': 'name',
        'namespace': 'namespace',
        'resource_version': 'resourceVersion',
        'uid': 'uid'
    }

    def __init__(self, kubelet_config_key=None, name=None, namespace=None, resource_version=None, uid=None):
        """
        V1ConfigMapNodeConfigSource - a model defined in Swagger
        """

        self._kubelet_config_key = None
        self._name = None
        self._namespace = None
        self._resource_version = None
        self._uid = None
        self.discriminator = None

        self.kubelet_config_key = kubelet_config_key
        self.name = name
        self.namespace = namespace
        if resource_version is not None:
          self.resource_version = resource_version
        if uid is not None:
          self.uid = uid

    @property
    def kubelet_config_key(self):
        """
        Gets the kubelet_config_key of this V1ConfigMapNodeConfigSource.
        KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases.

        :return: The kubelet_config_key of this V1ConfigMapNodeConfigSource.
        :rtype: str
        """
        return self._kubelet_config_key

    @kubelet_config_key.setter
    def kubelet_config_key(self, kubelet_config_key):
        """
        Sets the kubelet_config_key of this V1ConfigMapNodeConfigSource.
        KubeletConfigKey declares which key of the referenced ConfigMap corresponds to the KubeletConfiguration structure This field is required in all cases.

        :param kubelet_config_key: The kubelet_config_key of this V1ConfigMapNodeConfigSource.
        :type: str
        """
        if kubelet_config_key is None:
            raise ValueError("Invalid value for `kubelet_config_key`, must not be `None`")

        self._kubelet_config_key = kubelet_config_key

    @property
    def name(self):
        """
        Gets the name of this V1ConfigMapNodeConfigSource.
        Name is the metadata.name of the referenced ConfigMap. This field is required in all cases.

        :return: The name of this V1ConfigMapNodeConfigSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1ConfigMapNodeConfigSource.
        Name is the metadata.name of the referenced ConfigMap. This field is required in all cases.

        :param name: The name of this V1ConfigMapNodeConfigSource.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def namespace(self):
        """
        Gets the namespace of this V1ConfigMapNodeConfigSource.
        Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases.

        :return: The namespace of this V1ConfigMapNodeConfigSource.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this V1ConfigMapNodeConfigSource.
        Namespace is the metadata.namespace of the referenced ConfigMap. This field is required in all cases.

        :param namespace: The namespace of this V1ConfigMapNodeConfigSource.
        :type: str
        """
        if namespace is None:
            raise ValueError("Invalid value for `namespace`, must not be `None`")

        self._namespace = namespace

    @property
    def resource_version(self):
        """
        Gets the resource_version of this V1ConfigMapNodeConfigSource.
        ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.

        :return: The resource_version of this V1ConfigMapNodeConfigSource.
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        """
        Sets the resource_version of this V1ConfigMapNodeConfigSource.
        ResourceVersion is the metadata.ResourceVersion of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.

        :param resource_version: The resource_version of this V1ConfigMapNodeConfigSource.
        :type: str
        """

        self._resource_version = resource_version

    @property
    def uid(self):
        """
        Gets the uid of this V1ConfigMapNodeConfigSource.
        UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.

        :return: The uid of this V1ConfigMapNodeConfigSource.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this V1ConfigMapNodeConfigSource.
        UID is the metadata.UID of the referenced ConfigMap. This field is forbidden in Node.Spec, and required in Node.Status.

        :param uid: The uid of this V1ConfigMapNodeConfigSource.
        :type: str
        """

        self._uid = uid

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
        if not isinstance(other, V1ConfigMapNodeConfigSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
