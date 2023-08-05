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


class V1beta1ResourceRule(object):
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
        'api_groups': 'list[str]',
        'resource_names': 'list[str]',
        'resources': 'list[str]',
        'verbs': 'list[str]'
    }

    attribute_map = {
        'api_groups': 'apiGroups',
        'resource_names': 'resourceNames',
        'resources': 'resources',
        'verbs': 'verbs'
    }

    def __init__(self, api_groups=None, resource_names=None, resources=None, verbs=None):
        """
        V1beta1ResourceRule - a model defined in Swagger
        """

        self._api_groups = None
        self._resource_names = None
        self._resources = None
        self._verbs = None
        self.discriminator = None

        if api_groups is not None:
          self.api_groups = api_groups
        if resource_names is not None:
          self.resource_names = resource_names
        if resources is not None:
          self.resources = resources
        self.verbs = verbs

    @property
    def api_groups(self):
        """
        Gets the api_groups of this V1beta1ResourceRule.
        APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.  \"*\" means all.

        :return: The api_groups of this V1beta1ResourceRule.
        :rtype: list[str]
        """
        return self._api_groups

    @api_groups.setter
    def api_groups(self, api_groups):
        """
        Sets the api_groups of this V1beta1ResourceRule.
        APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.  \"*\" means all.

        :param api_groups: The api_groups of this V1beta1ResourceRule.
        :type: list[str]
        """

        self._api_groups = api_groups

    @property
    def resource_names(self):
        """
        Gets the resource_names of this V1beta1ResourceRule.
        ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.  \"*\" means all.

        :return: The resource_names of this V1beta1ResourceRule.
        :rtype: list[str]
        """
        return self._resource_names

    @resource_names.setter
    def resource_names(self, resource_names):
        """
        Sets the resource_names of this V1beta1ResourceRule.
        ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.  \"*\" means all.

        :param resource_names: The resource_names of this V1beta1ResourceRule.
        :type: list[str]
        """

        self._resource_names = resource_names

    @property
    def resources(self):
        """
        Gets the resources of this V1beta1ResourceRule.
        Resources is a list of resources this rule applies to.  \"*\" means all in the specified apiGroups.  \"*/foo\" represents the subresource 'foo' for all resources in the specified apiGroups.

        :return: The resources of this V1beta1ResourceRule.
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this V1beta1ResourceRule.
        Resources is a list of resources this rule applies to.  \"*\" means all in the specified apiGroups.  \"*/foo\" represents the subresource 'foo' for all resources in the specified apiGroups.

        :param resources: The resources of this V1beta1ResourceRule.
        :type: list[str]
        """

        self._resources = resources

    @property
    def verbs(self):
        """
        Gets the verbs of this V1beta1ResourceRule.
        Verb is a list of kubernetes resource API verbs, like: get, list, watch, create, update, delete, proxy.  \"*\" means all.

        :return: The verbs of this V1beta1ResourceRule.
        :rtype: list[str]
        """
        return self._verbs

    @verbs.setter
    def verbs(self, verbs):
        """
        Sets the verbs of this V1beta1ResourceRule.
        Verb is a list of kubernetes resource API verbs, like: get, list, watch, create, update, delete, proxy.  \"*\" means all.

        :param verbs: The verbs of this V1beta1ResourceRule.
        :type: list[str]
        """
        if verbs is None:
            raise ValueError("Invalid value for `verbs`, must not be `None`")

        self._verbs = verbs

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
        if not isinstance(other, V1beta1ResourceRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
