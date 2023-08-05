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


class V2beta1PodsMetricSource(object):
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
        'metric_name': 'str',
        'selector': 'V1LabelSelector',
        'target_average_value': 'str'
    }

    attribute_map = {
        'metric_name': 'metricName',
        'selector': 'selector',
        'target_average_value': 'targetAverageValue'
    }

    def __init__(self, metric_name=None, selector=None, target_average_value=None):
        """
        V2beta1PodsMetricSource - a model defined in Swagger
        """

        self._metric_name = None
        self._selector = None
        self._target_average_value = None
        self.discriminator = None

        self.metric_name = metric_name
        if selector is not None:
          self.selector = selector
        self.target_average_value = target_average_value

    @property
    def metric_name(self):
        """
        Gets the metric_name of this V2beta1PodsMetricSource.
        metricName is the name of the metric in question

        :return: The metric_name of this V2beta1PodsMetricSource.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """
        Sets the metric_name of this V2beta1PodsMetricSource.
        metricName is the name of the metric in question

        :param metric_name: The metric_name of this V2beta1PodsMetricSource.
        :type: str
        """
        if metric_name is None:
            raise ValueError("Invalid value for `metric_name`, must not be `None`")

        self._metric_name = metric_name

    @property
    def selector(self):
        """
        Gets the selector of this V2beta1PodsMetricSource.
        selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping When unset, just the metricName will be used to gather metrics.

        :return: The selector of this V2beta1PodsMetricSource.
        :rtype: V1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this V2beta1PodsMetricSource.
        selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping When unset, just the metricName will be used to gather metrics.

        :param selector: The selector of this V2beta1PodsMetricSource.
        :type: V1LabelSelector
        """

        self._selector = selector

    @property
    def target_average_value(self):
        """
        Gets the target_average_value of this V2beta1PodsMetricSource.
        targetAverageValue is the target value of the average of the metric across all relevant pods (as a quantity)

        :return: The target_average_value of this V2beta1PodsMetricSource.
        :rtype: str
        """
        return self._target_average_value

    @target_average_value.setter
    def target_average_value(self, target_average_value):
        """
        Sets the target_average_value of this V2beta1PodsMetricSource.
        targetAverageValue is the target value of the average of the metric across all relevant pods (as a quantity)

        :param target_average_value: The target_average_value of this V2beta1PodsMetricSource.
        :type: str
        """
        if target_average_value is None:
            raise ValueError("Invalid value for `target_average_value`, must not be `None`")

        self._target_average_value = target_average_value

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
        if not isinstance(other, V2beta1PodsMetricSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
