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


class V1RBDVolumeSource(object):
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
        'fs_type': 'str',
        'image': 'str',
        'keyring': 'str',
        'monitors': 'list[str]',
        'pool': 'str',
        'read_only': 'bool',
        'secret_ref': 'V1LocalObjectReference',
        'user': 'str'
    }

    attribute_map = {
        'fs_type': 'fsType',
        'image': 'image',
        'keyring': 'keyring',
        'monitors': 'monitors',
        'pool': 'pool',
        'read_only': 'readOnly',
        'secret_ref': 'secretRef',
        'user': 'user'
    }

    def __init__(self, fs_type=None, image=None, keyring=None, monitors=None, pool=None, read_only=None, secret_ref=None, user=None):
        """
        V1RBDVolumeSource - a model defined in Swagger
        """

        self._fs_type = None
        self._image = None
        self._keyring = None
        self._monitors = None
        self._pool = None
        self._read_only = None
        self._secret_ref = None
        self._user = None
        self.discriminator = None

        if fs_type is not None:
          self.fs_type = fs_type
        self.image = image
        if keyring is not None:
          self.keyring = keyring
        self.monitors = monitors
        if pool is not None:
          self.pool = pool
        if read_only is not None:
          self.read_only = read_only
        if secret_ref is not None:
          self.secret_ref = secret_ref
        if user is not None:
          self.user = user

    @property
    def fs_type(self):
        """
        Gets the fs_type of this V1RBDVolumeSource.
        Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd

        :return: The fs_type of this V1RBDVolumeSource.
        :rtype: str
        """
        return self._fs_type

    @fs_type.setter
    def fs_type(self, fs_type):
        """
        Sets the fs_type of this V1RBDVolumeSource.
        Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: \"ext4\", \"xfs\", \"ntfs\". Implicitly inferred to be \"ext4\" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd

        :param fs_type: The fs_type of this V1RBDVolumeSource.
        :type: str
        """

        self._fs_type = fs_type

    @property
    def image(self):
        """
        Gets the image of this V1RBDVolumeSource.
        The rados image name. More info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :return: The image of this V1RBDVolumeSource.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this V1RBDVolumeSource.
        The rados image name. More info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :param image: The image of this V1RBDVolumeSource.
        :type: str
        """
        if image is None:
            raise ValueError("Invalid value for `image`, must not be `None`")

        self._image = image

    @property
    def keyring(self):
        """
        Gets the keyring of this V1RBDVolumeSource.
        Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :return: The keyring of this V1RBDVolumeSource.
        :rtype: str
        """
        return self._keyring

    @keyring.setter
    def keyring(self, keyring):
        """
        Sets the keyring of this V1RBDVolumeSource.
        Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :param keyring: The keyring of this V1RBDVolumeSource.
        :type: str
        """

        self._keyring = keyring

    @property
    def monitors(self):
        """
        Gets the monitors of this V1RBDVolumeSource.
        A collection of Ceph monitors. More info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :return: The monitors of this V1RBDVolumeSource.
        :rtype: list[str]
        """
        return self._monitors

    @monitors.setter
    def monitors(self, monitors):
        """
        Sets the monitors of this V1RBDVolumeSource.
        A collection of Ceph monitors. More info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :param monitors: The monitors of this V1RBDVolumeSource.
        :type: list[str]
        """
        if monitors is None:
            raise ValueError("Invalid value for `monitors`, must not be `None`")

        self._monitors = monitors

    @property
    def pool(self):
        """
        Gets the pool of this V1RBDVolumeSource.
        The rados pool name. Default is rbd. More info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :return: The pool of this V1RBDVolumeSource.
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """
        Sets the pool of this V1RBDVolumeSource.
        The rados pool name. Default is rbd. More info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :param pool: The pool of this V1RBDVolumeSource.
        :type: str
        """

        self._pool = pool

    @property
    def read_only(self):
        """
        Gets the read_only of this V1RBDVolumeSource.
        ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :return: The read_only of this V1RBDVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this V1RBDVolumeSource.
        ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :param read_only: The read_only of this V1RBDVolumeSource.
        :type: bool
        """

        self._read_only = read_only

    @property
    def secret_ref(self):
        """
        Gets the secret_ref of this V1RBDVolumeSource.
        SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :return: The secret_ref of this V1RBDVolumeSource.
        :rtype: V1LocalObjectReference
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """
        Sets the secret_ref of this V1RBDVolumeSource.
        SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :param secret_ref: The secret_ref of this V1RBDVolumeSource.
        :type: V1LocalObjectReference
        """

        self._secret_ref = secret_ref

    @property
    def user(self):
        """
        Gets the user of this V1RBDVolumeSource.
        The rados user name. Default is admin. More info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :return: The user of this V1RBDVolumeSource.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this V1RBDVolumeSource.
        The rados user name. Default is admin. More info: https://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it

        :param user: The user of this V1RBDVolumeSource.
        :type: str
        """

        self._user = user

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
        if not isinstance(other, V1RBDVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
