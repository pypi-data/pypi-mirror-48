import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_ec2
import aws_cdk.aws_elasticloadbalancingv2
import aws_cdk.aws_route53
import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-servicediscovery", "0.37.0", __name__, "aws-servicediscovery@0.37.0.jsii.tgz")
@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.BaseInstanceProps", jsii_struct_bases=[])
class BaseInstanceProps(jsii.compat.TypedDict, total=False):
    """Used when the resource that's associated with the service instance is accessible using values other than an IP address or a domain name (CNAME), i.e. for non-ip-instances.

    Stability:
        stable
    """
    customAttributes: typing.Mapping[str,str]
    """Custom attributes of the instance.

    Default:
        none

    Stability:
        stable
    """

    instanceId: str
    """The id of the instance resource.

    Default:
        Automatically generated name

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.AliasTargetInstanceProps", jsii_struct_bases=[BaseInstanceProps])
class AliasTargetInstanceProps(BaseInstanceProps, jsii.compat.TypedDict):
    """
    Stability:
        stable
    """
    dnsName: str
    """DNS name of the target.

    Stability:
        stable
    """

    service: "IService"
    """The Cloudmap service this resource is registered to.

    Stability:
        stable
    """

@jsii.data_type_optionals(jsii_struct_bases=[])
class _BaseNamespaceProps(jsii.compat.TypedDict, total=False):
    description: str
    """A description of the Namespace.

    Default:
        none

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.BaseNamespaceProps", jsii_struct_bases=[_BaseNamespaceProps])
class BaseNamespaceProps(_BaseNamespaceProps):
    """
    Stability:
        stable
    """
    name: str
    """A name for the Namespace.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.BaseServiceProps", jsii_struct_bases=[])
class BaseServiceProps(jsii.compat.TypedDict, total=False):
    """Basic props needed to create a service in a given namespace.

    Used by HttpNamespace.createService

    Stability:
        stable
    """
    customHealthCheck: "HealthCheckCustomConfig"
    """Structure containing failure threshold for a custom health checker. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. See: https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html.

    Default:
        none

    Stability:
        stable
    """

    description: str
    """A description of the service.

    Default:
        none

    Stability:
        stable
    """

    healthCheck: "HealthCheckConfig"
    """Settings for an optional health check.

    If you specify health check settings, AWS Cloud Map associates the health
    check with the records that you specify in DnsConfig. Only one of healthCheckConfig or healthCheckCustomConfig can
    be specified. Not valid for PrivateDnsNamespaces. If you use healthCheck, you can only register IP instances to
    this service.

    Default:
        none

    Stability:
        stable
    """

    name: str
    """A name for the Service.

    Default:
        CloudFormation-generated name

    Stability:
        stable
    """

class CfnHttpNamespace(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-servicediscovery.CfnHttpNamespace"):
    """A CloudFormation ``AWS::ServiceDiscovery::HttpNamespace``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html
    Stability:
        stable
    cloudformationResource:
        AWS::ServiceDiscovery::HttpNamespace
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, name: str, description: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::ServiceDiscovery::HttpNamespace``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            name: ``AWS::ServiceDiscovery::HttpNamespace.Name``.
            description: ``AWS::ServiceDiscovery::HttpNamespace.Description``.

        Stability:
            stable
        """
        props: CfnHttpNamespaceProps = {"name": name}

        if description is not None:
            props["description"] = description

        jsii.create(CfnHttpNamespace, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        Arguments:
            props: -

        Stability:
            stable
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class.

        Stability:
            stable
        """
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> str:
        """
        Stability:
            stable
        cloudformationAttribute:
            Arn
        """
        return jsii.get(self, "attrArn")

    @property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> str:
        """
        Stability:
            stable
        cloudformationAttribute:
            Id
        """
        return jsii.get(self, "attrId")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::ServiceDiscovery::HttpNamespace.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html#cfn-servicediscovery-httpnamespace-name
        Stability:
            stable
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::ServiceDiscovery::HttpNamespace.Description``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html#cfn-servicediscovery-httpnamespace-description
        Stability:
            stable
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnHttpNamespaceProps(jsii.compat.TypedDict, total=False):
    description: str
    """``AWS::ServiceDiscovery::HttpNamespace.Description``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html#cfn-servicediscovery-httpnamespace-description
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.CfnHttpNamespaceProps", jsii_struct_bases=[_CfnHttpNamespaceProps])
class CfnHttpNamespaceProps(_CfnHttpNamespaceProps):
    """Properties for defining a ``AWS::ServiceDiscovery::HttpNamespace``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html
    Stability:
        stable
    """
    name: str
    """``AWS::ServiceDiscovery::HttpNamespace.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html#cfn-servicediscovery-httpnamespace-name
    Stability:
        stable
    """

class CfnInstance(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-servicediscovery.CfnInstance"):
    """A CloudFormation ``AWS::ServiceDiscovery::Instance``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html
    Stability:
        stable
    cloudformationResource:
        AWS::ServiceDiscovery::Instance
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, instance_attributes: typing.Any, service_id: str, instance_id: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::ServiceDiscovery::Instance``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            instance_attributes: ``AWS::ServiceDiscovery::Instance.InstanceAttributes``.
            service_id: ``AWS::ServiceDiscovery::Instance.ServiceId``.
            instance_id: ``AWS::ServiceDiscovery::Instance.InstanceId``.

        Stability:
            stable
        """
        props: CfnInstanceProps = {"instanceAttributes": instance_attributes, "serviceId": service_id}

        if instance_id is not None:
            props["instanceId"] = instance_id

        jsii.create(CfnInstance, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        Arguments:
            props: -

        Stability:
            stable
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class.

        Stability:
            stable
        """
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="instanceAttributes")
    def instance_attributes(self) -> typing.Any:
        """``AWS::ServiceDiscovery::Instance.InstanceAttributes``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html#cfn-servicediscovery-instance-instanceattributes
        Stability:
            stable
        """
        return jsii.get(self, "instanceAttributes")

    @instance_attributes.setter
    def instance_attributes(self, value: typing.Any):
        return jsii.set(self, "instanceAttributes", value)

    @property
    @jsii.member(jsii_name="serviceId")
    def service_id(self) -> str:
        """``AWS::ServiceDiscovery::Instance.ServiceId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html#cfn-servicediscovery-instance-serviceid
        Stability:
            stable
        """
        return jsii.get(self, "serviceId")

    @service_id.setter
    def service_id(self, value: str):
        return jsii.set(self, "serviceId", value)

    @property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> typing.Optional[str]:
        """``AWS::ServiceDiscovery::Instance.InstanceId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html#cfn-servicediscovery-instance-instanceid
        Stability:
            stable
        """
        return jsii.get(self, "instanceId")

    @instance_id.setter
    def instance_id(self, value: typing.Optional[str]):
        return jsii.set(self, "instanceId", value)


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnInstanceProps(jsii.compat.TypedDict, total=False):
    instanceId: str
    """``AWS::ServiceDiscovery::Instance.InstanceId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html#cfn-servicediscovery-instance-instanceid
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.CfnInstanceProps", jsii_struct_bases=[_CfnInstanceProps])
class CfnInstanceProps(_CfnInstanceProps):
    """Properties for defining a ``AWS::ServiceDiscovery::Instance``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html
    Stability:
        stable
    """
    instanceAttributes: typing.Any
    """``AWS::ServiceDiscovery::Instance.InstanceAttributes``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html#cfn-servicediscovery-instance-instanceattributes
    Stability:
        stable
    """

    serviceId: str
    """``AWS::ServiceDiscovery::Instance.ServiceId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html#cfn-servicediscovery-instance-serviceid
    Stability:
        stable
    """

class CfnPrivateDnsNamespace(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-servicediscovery.CfnPrivateDnsNamespace"):
    """A CloudFormation ``AWS::ServiceDiscovery::PrivateDnsNamespace``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html
    Stability:
        stable
    cloudformationResource:
        AWS::ServiceDiscovery::PrivateDnsNamespace
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, name: str, vpc: str, description: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::ServiceDiscovery::PrivateDnsNamespace``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            name: ``AWS::ServiceDiscovery::PrivateDnsNamespace.Name``.
            vpc: ``AWS::ServiceDiscovery::PrivateDnsNamespace.Vpc``.
            description: ``AWS::ServiceDiscovery::PrivateDnsNamespace.Description``.

        Stability:
            stable
        """
        props: CfnPrivateDnsNamespaceProps = {"name": name, "vpc": vpc}

        if description is not None:
            props["description"] = description

        jsii.create(CfnPrivateDnsNamespace, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        Arguments:
            props: -

        Stability:
            stable
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class.

        Stability:
            stable
        """
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> str:
        """
        Stability:
            stable
        cloudformationAttribute:
            Arn
        """
        return jsii.get(self, "attrArn")

    @property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> str:
        """
        Stability:
            stable
        cloudformationAttribute:
            Id
        """
        return jsii.get(self, "attrId")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::ServiceDiscovery::PrivateDnsNamespace.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-name
        Stability:
            stable
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> str:
        """``AWS::ServiceDiscovery::PrivateDnsNamespace.Vpc``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-vpc
        Stability:
            stable
        """
        return jsii.get(self, "vpc")

    @vpc.setter
    def vpc(self, value: str):
        return jsii.set(self, "vpc", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::ServiceDiscovery::PrivateDnsNamespace.Description``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-description
        Stability:
            stable
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnPrivateDnsNamespaceProps(jsii.compat.TypedDict, total=False):
    description: str
    """``AWS::ServiceDiscovery::PrivateDnsNamespace.Description``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-description
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.CfnPrivateDnsNamespaceProps", jsii_struct_bases=[_CfnPrivateDnsNamespaceProps])
class CfnPrivateDnsNamespaceProps(_CfnPrivateDnsNamespaceProps):
    """Properties for defining a ``AWS::ServiceDiscovery::PrivateDnsNamespace``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html
    Stability:
        stable
    """
    name: str
    """``AWS::ServiceDiscovery::PrivateDnsNamespace.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-name
    Stability:
        stable
    """

    vpc: str
    """``AWS::ServiceDiscovery::PrivateDnsNamespace.Vpc``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html#cfn-servicediscovery-privatednsnamespace-vpc
    Stability:
        stable
    """

class CfnPublicDnsNamespace(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-servicediscovery.CfnPublicDnsNamespace"):
    """A CloudFormation ``AWS::ServiceDiscovery::PublicDnsNamespace``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html
    Stability:
        stable
    cloudformationResource:
        AWS::ServiceDiscovery::PublicDnsNamespace
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, name: str, description: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::ServiceDiscovery::PublicDnsNamespace``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            name: ``AWS::ServiceDiscovery::PublicDnsNamespace.Name``.
            description: ``AWS::ServiceDiscovery::PublicDnsNamespace.Description``.

        Stability:
            stable
        """
        props: CfnPublicDnsNamespaceProps = {"name": name}

        if description is not None:
            props["description"] = description

        jsii.create(CfnPublicDnsNamespace, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        Arguments:
            props: -

        Stability:
            stable
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class.

        Stability:
            stable
        """
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> str:
        """
        Stability:
            stable
        cloudformationAttribute:
            Arn
        """
        return jsii.get(self, "attrArn")

    @property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> str:
        """
        Stability:
            stable
        cloudformationAttribute:
            Id
        """
        return jsii.get(self, "attrId")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::ServiceDiscovery::PublicDnsNamespace.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html#cfn-servicediscovery-publicdnsnamespace-name
        Stability:
            stable
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::ServiceDiscovery::PublicDnsNamespace.Description``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html#cfn-servicediscovery-publicdnsnamespace-description
        Stability:
            stable
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnPublicDnsNamespaceProps(jsii.compat.TypedDict, total=False):
    description: str
    """``AWS::ServiceDiscovery::PublicDnsNamespace.Description``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html#cfn-servicediscovery-publicdnsnamespace-description
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.CfnPublicDnsNamespaceProps", jsii_struct_bases=[_CfnPublicDnsNamespaceProps])
class CfnPublicDnsNamespaceProps(_CfnPublicDnsNamespaceProps):
    """Properties for defining a ``AWS::ServiceDiscovery::PublicDnsNamespace``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html
    Stability:
        stable
    """
    name: str
    """``AWS::ServiceDiscovery::PublicDnsNamespace.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html#cfn-servicediscovery-publicdnsnamespace-name
    Stability:
        stable
    """

class CfnService(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-servicediscovery.CfnService"):
    """A CloudFormation ``AWS::ServiceDiscovery::Service``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html
    Stability:
        stable
    cloudformationResource:
        AWS::ServiceDiscovery::Service
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, description: typing.Optional[str]=None, dns_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["DnsConfigProperty"]]]=None, health_check_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["HealthCheckConfigProperty"]]]=None, health_check_custom_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["HealthCheckCustomConfigProperty"]]]=None, name: typing.Optional[str]=None, namespace_id: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::ServiceDiscovery::Service``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            description: ``AWS::ServiceDiscovery::Service.Description``.
            dns_config: ``AWS::ServiceDiscovery::Service.DnsConfig``.
            health_check_config: ``AWS::ServiceDiscovery::Service.HealthCheckConfig``.
            health_check_custom_config: ``AWS::ServiceDiscovery::Service.HealthCheckCustomConfig``.
            name: ``AWS::ServiceDiscovery::Service.Name``.
            namespace_id: ``AWS::ServiceDiscovery::Service.NamespaceId``.

        Stability:
            stable
        """
        props: CfnServiceProps = {}

        if description is not None:
            props["description"] = description

        if dns_config is not None:
            props["dnsConfig"] = dns_config

        if health_check_config is not None:
            props["healthCheckConfig"] = health_check_config

        if health_check_custom_config is not None:
            props["healthCheckCustomConfig"] = health_check_custom_config

        if name is not None:
            props["name"] = name

        if namespace_id is not None:
            props["namespaceId"] = namespace_id

        jsii.create(CfnService, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        Arguments:
            props: -

        Stability:
            stable
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class.

        Stability:
            stable
        """
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")

    @property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> str:
        """
        Stability:
            stable
        cloudformationAttribute:
            Arn
        """
        return jsii.get(self, "attrArn")

    @property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> str:
        """
        Stability:
            stable
        cloudformationAttribute:
            Id
        """
        return jsii.get(self, "attrId")

    @property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> str:
        """
        Stability:
            stable
        cloudformationAttribute:
            Name
        """
        return jsii.get(self, "attrName")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::ServiceDiscovery::Service.Description``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-description
        Stability:
            stable
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="dnsConfig")
    def dns_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["DnsConfigProperty"]]]:
        """``AWS::ServiceDiscovery::Service.DnsConfig``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-dnsconfig
        Stability:
            stable
        """
        return jsii.get(self, "dnsConfig")

    @dns_config.setter
    def dns_config(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["DnsConfigProperty"]]]):
        return jsii.set(self, "dnsConfig", value)

    @property
    @jsii.member(jsii_name="healthCheckConfig")
    def health_check_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["HealthCheckConfigProperty"]]]:
        """``AWS::ServiceDiscovery::Service.HealthCheckConfig``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-healthcheckconfig
        Stability:
            stable
        """
        return jsii.get(self, "healthCheckConfig")

    @health_check_config.setter
    def health_check_config(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["HealthCheckConfigProperty"]]]):
        return jsii.set(self, "healthCheckConfig", value)

    @property
    @jsii.member(jsii_name="healthCheckCustomConfig")
    def health_check_custom_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["HealthCheckCustomConfigProperty"]]]:
        """``AWS::ServiceDiscovery::Service.HealthCheckCustomConfig``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-healthcheckcustomconfig
        Stability:
            stable
        """
        return jsii.get(self, "healthCheckCustomConfig")

    @health_check_custom_config.setter
    def health_check_custom_config(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["HealthCheckCustomConfigProperty"]]]):
        return jsii.set(self, "healthCheckCustomConfig", value)

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::ServiceDiscovery::Service.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-name
        Stability:
            stable
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> typing.Optional[str]:
        """``AWS::ServiceDiscovery::Service.NamespaceId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-namespaceid
        Stability:
            stable
        """
        return jsii.get(self, "namespaceId")

    @namespace_id.setter
    def namespace_id(self, value: typing.Optional[str]):
        return jsii.set(self, "namespaceId", value)

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _DnsConfigProperty(jsii.compat.TypedDict, total=False):
        namespaceId: str
        """``CfnService.DnsConfigProperty.NamespaceId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsconfig.html#cfn-servicediscovery-service-dnsconfig-namespaceid
        Stability:
            stable
        """
        routingPolicy: str
        """``CfnService.DnsConfigProperty.RoutingPolicy``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsconfig.html#cfn-servicediscovery-service-dnsconfig-routingpolicy
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.CfnService.DnsConfigProperty", jsii_struct_bases=[_DnsConfigProperty])
    class DnsConfigProperty(_DnsConfigProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsconfig.html
        Stability:
            stable
        """
        dnsRecords: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnService.DnsRecordProperty"]]]
        """``CfnService.DnsConfigProperty.DnsRecords``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsconfig.html#cfn-servicediscovery-service-dnsconfig-dnsrecords
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.CfnService.DnsRecordProperty", jsii_struct_bases=[])
    class DnsRecordProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsrecord.html
        Stability:
            stable
        """
        ttl: jsii.Number
        """``CfnService.DnsRecordProperty.TTL``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsrecord.html#cfn-servicediscovery-service-dnsrecord-ttl
        Stability:
            stable
        """

        type: str
        """``CfnService.DnsRecordProperty.Type``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-dnsrecord.html#cfn-servicediscovery-service-dnsrecord-type
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _HealthCheckConfigProperty(jsii.compat.TypedDict, total=False):
        failureThreshold: jsii.Number
        """``CfnService.HealthCheckConfigProperty.FailureThreshold``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckconfig.html#cfn-servicediscovery-service-healthcheckconfig-failurethreshold
        Stability:
            stable
        """
        resourcePath: str
        """``CfnService.HealthCheckConfigProperty.ResourcePath``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckconfig.html#cfn-servicediscovery-service-healthcheckconfig-resourcepath
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.CfnService.HealthCheckConfigProperty", jsii_struct_bases=[_HealthCheckConfigProperty])
    class HealthCheckConfigProperty(_HealthCheckConfigProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckconfig.html
        Stability:
            stable
        """
        type: str
        """``CfnService.HealthCheckConfigProperty.Type``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckconfig.html#cfn-servicediscovery-service-healthcheckconfig-type
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.CfnService.HealthCheckCustomConfigProperty", jsii_struct_bases=[])
    class HealthCheckCustomConfigProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckcustomconfig.html
        Stability:
            stable
        """
        failureThreshold: jsii.Number
        """``CfnService.HealthCheckCustomConfigProperty.FailureThreshold``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-servicediscovery-service-healthcheckcustomconfig.html#cfn-servicediscovery-service-healthcheckcustomconfig-failurethreshold
        Stability:
            stable
        """


@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.CfnServiceProps", jsii_struct_bases=[])
class CfnServiceProps(jsii.compat.TypedDict, total=False):
    """Properties for defining a ``AWS::ServiceDiscovery::Service``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html
    Stability:
        stable
    """
    description: str
    """``AWS::ServiceDiscovery::Service.Description``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-description
    Stability:
        stable
    """

    dnsConfig: typing.Union[aws_cdk.core.IResolvable, "CfnService.DnsConfigProperty"]
    """``AWS::ServiceDiscovery::Service.DnsConfig``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-dnsconfig
    Stability:
        stable
    """

    healthCheckConfig: typing.Union[aws_cdk.core.IResolvable, "CfnService.HealthCheckConfigProperty"]
    """``AWS::ServiceDiscovery::Service.HealthCheckConfig``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-healthcheckconfig
    Stability:
        stable
    """

    healthCheckCustomConfig: typing.Union[aws_cdk.core.IResolvable, "CfnService.HealthCheckCustomConfigProperty"]
    """``AWS::ServiceDiscovery::Service.HealthCheckCustomConfig``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-healthcheckcustomconfig
    Stability:
        stable
    """

    name: str
    """``AWS::ServiceDiscovery::Service.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-name
    Stability:
        stable
    """

    namespaceId: str
    """``AWS::ServiceDiscovery::Service.NamespaceId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html#cfn-servicediscovery-service-namespaceid
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.CnameInstanceBaseProps", jsii_struct_bases=[BaseInstanceProps])
class CnameInstanceBaseProps(BaseInstanceProps, jsii.compat.TypedDict):
    """
    Stability:
        stable
    """
    instanceCname: str
    """If the service configuration includes a CNAME record, the domain name that you want Route 53 to return in response to DNS queries, for example, example.com. This value is required if the service specified by ServiceId includes settings for an CNAME record.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.CnameInstanceProps", jsii_struct_bases=[CnameInstanceBaseProps])
class CnameInstanceProps(CnameInstanceBaseProps, jsii.compat.TypedDict):
    """
    Stability:
        stable
    """
    service: "IService"
    """The Cloudmap service this resource is registered to.

    Stability:
        stable
    """

@jsii.enum(jsii_type="@aws-cdk/aws-servicediscovery.DnsRecordType")
class DnsRecordType(enum.Enum):
    """
    Stability:
        stable
    """
    A = "A"
    """An A record.

    Stability:
        stable
    """
    AAAA = "AAAA"
    """An AAAA record.

    Stability:
        stable
    """
    A_AAAA = "A_AAAA"
    """Both an A and AAAA record.

    Stability:
        stable
    """
    SRV = "SRV"
    """A Srv record.

    Stability:
        stable
    """
    CNAME = "CNAME"
    """A CNAME record.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.DnsServiceProps", jsii_struct_bases=[BaseServiceProps])
class DnsServiceProps(BaseServiceProps, jsii.compat.TypedDict, total=False):
    """Service props needed to create a service in a given namespace.

    Used by createService() for PrivateDnsNamespace and
    PublicDnsNamespace

    Stability:
        stable
    """
    dnsRecordType: "DnsRecordType"
    """The DNS type of the record that you want AWS Cloud Map to create.

    Supported record types
    include A, AAAA, A and AAAA (A_AAAA), CNAME, and SRV.

    Default:
        A

    Stability:
        stable
    """

    dnsTtl: aws_cdk.core.Duration
    """The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record.

    Default:
        Duration.minutes(1)

    Stability:
        stable
    """

    loadBalancer: bool
    """Whether or not this service will have an Elastic LoadBalancer registered to it as an AliasTargetInstance.

    Setting this to ``true`` correctly configures the ``routingPolicy``
    and performs some additional validation.

    Default:
        false

    Stability:
        stable
    """

    routingPolicy: "RoutingPolicy"
    """The routing policy that you want to apply to all DNS records that AWS Cloud Map creates when you register an instance and specify this service.

    Default:
        WEIGHTED for CNAME records and when loadBalancer is true, MULTIVALUE otherwise

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.HealthCheckConfig", jsii_struct_bases=[])
class HealthCheckConfig(jsii.compat.TypedDict, total=False):
    """Settings for an optional Amazon Route 53 health check.

    If you specify settings for a health check, AWS Cloud Map
    associates the health check with all the records that you specify in DnsConfig. Only valid with a PublicDnsNamespace.

    Stability:
        stable
    """
    failureThreshold: jsii.Number
    """The number of consecutive health checks that an endpoint must pass or fail for Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa.

    Default:
        1

    Stability:
        stable
    """

    resourcePath: str
    """The path that you want Route 53 to request when performing health checks.

    Do not use when health check type is TCP.

    Default:
        '/'

    Stability:
        stable
    """

    type: "HealthCheckType"
    """The type of health check that you want to create, which indicates how Route 53 determines whether an endpoint is healthy.

    Cannot be modified once created. Supported values are HTTP, HTTPS, and TCP.

    Default:
        HTTP

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.HealthCheckCustomConfig", jsii_struct_bases=[])
class HealthCheckCustomConfig(jsii.compat.TypedDict, total=False):
    """Specifies information about an optional custom health check.

    Stability:
        stable
    """
    failureThreshold: jsii.Number
    """The number of 30-second intervals that you want Cloud Map to wait after receiving an UpdateInstanceCustomHealthStatus request before it changes the health status of a service instance.

    Default:
        1

    Stability:
        stable
    """

@jsii.enum(jsii_type="@aws-cdk/aws-servicediscovery.HealthCheckType")
class HealthCheckType(enum.Enum):
    """
    Stability:
        stable
    """
    HTTP = "HTTP"
    """Route 53 tries to establish a TCP connection.

    If successful, Route 53 submits an HTTP request and waits for an HTTP
    status code of 200 or greater and less than 400.

    Stability:
        stable
    """
    HTTPS = "HTTPS"
    """Route 53 tries to establish a TCP connection.

    If successful, Route 53 submits an HTTPS request and waits for an
    HTTP status code of 200 or greater and less than 400.  If you specify HTTPS for the value of Type, the endpoint
    must support TLS v1.0 or later.

    Stability:
        stable
    """
    TCP = "TCP"
    """Route 53 tries to establish a TCP connection. If you specify TCP for Type, don't specify a value for ResourcePath.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.HttpNamespaceAttributes", jsii_struct_bases=[])
class HttpNamespaceAttributes(jsii.compat.TypedDict):
    """
    Stability:
        stable
    """
    namespaceArn: str
    """Namespace ARN for the Namespace.

    Stability:
        stable
    """

    namespaceId: str
    """Namespace Id for the Namespace.

    Stability:
        stable
    """

    namespaceName: str
    """A name for the Namespace.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.HttpNamespaceProps", jsii_struct_bases=[BaseNamespaceProps])
class HttpNamespaceProps(BaseNamespaceProps, jsii.compat.TypedDict):
    """
    Stability:
        stable
    """
    pass

@jsii.interface(jsii_type="@aws-cdk/aws-servicediscovery.IInstance")
class IInstance(aws_cdk.core.IResource, jsii.compat.Protocol):
    """
    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IInstanceProxy

    @property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> str:
        """The id of the instance resource.

        Stability:
            stable
        attribute:
            true
        """
        ...

    @property
    @jsii.member(jsii_name="service")
    def service(self) -> "IService":
        """The Cloudmap service this resource is registered to.

        Stability:
            stable
        """
        ...


class _IInstanceProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """
    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-servicediscovery.IInstance"
    @property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> str:
        """The id of the instance resource.

        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "instanceId")

    @property
    @jsii.member(jsii_name="service")
    def service(self) -> "IService":
        """The Cloudmap service this resource is registered to.

        Stability:
            stable
        """
        return jsii.get(self, "service")


@jsii.interface(jsii_type="@aws-cdk/aws-servicediscovery.INamespace")
class INamespace(aws_cdk.core.IResource, jsii.compat.Protocol):
    """
    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _INamespaceProxy

    @property
    @jsii.member(jsii_name="namespaceArn")
    def namespace_arn(self) -> str:
        """Namespace ARN for the Namespace.

        Stability:
            stable
        attribute:
            true
        """
        ...

    @property
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> str:
        """Namespace Id for the Namespace.

        Stability:
            stable
        attribute:
            true
        """
        ...

    @property
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> str:
        """A name for the Namespace.

        Stability:
            stable
        attribute:
            true
        """
        ...

    @property
    @jsii.member(jsii_name="type")
    def type(self) -> "NamespaceType":
        """Type of Namespace.

        Stability:
            stable
        """
        ...


class _INamespaceProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """
    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-servicediscovery.INamespace"
    @property
    @jsii.member(jsii_name="namespaceArn")
    def namespace_arn(self) -> str:
        """Namespace ARN for the Namespace.

        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "namespaceArn")

    @property
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> str:
        """Namespace Id for the Namespace.

        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "namespaceId")

    @property
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> str:
        """A name for the Namespace.

        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "namespaceName")

    @property
    @jsii.member(jsii_name="type")
    def type(self) -> "NamespaceType":
        """Type of Namespace.

        Stability:
            stable
        """
        return jsii.get(self, "type")


@jsii.interface(jsii_type="@aws-cdk/aws-servicediscovery.IHttpNamespace")
class IHttpNamespace(INamespace, jsii.compat.Protocol):
    """
    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IHttpNamespaceProxy

    pass

class _IHttpNamespaceProxy(jsii.proxy_for(INamespace)):
    """
    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-servicediscovery.IHttpNamespace"
    pass

@jsii.implements(IHttpNamespace)
class HttpNamespace(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-servicediscovery.HttpNamespace"):
    """Define an HTTP Namespace.

    Stability:
        stable
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, name: str, description: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            name: A name for the Namespace.
            description: A description of the Namespace. Default: none

        Stability:
            stable
        """
        props: HttpNamespaceProps = {"name": name}

        if description is not None:
            props["description"] = description

        jsii.create(HttpNamespace, self, [scope, id, props])

    @jsii.member(jsii_name="fromHttpNamespaceAttributes")
    @classmethod
    def from_http_namespace_attributes(cls, scope: aws_cdk.core.Construct, id: str, *, namespace_arn: str, namespace_id: str, namespace_name: str) -> "IHttpNamespace":
        """
        Arguments:
            scope: -
            id: -
            attrs: -
            namespace_arn: Namespace ARN for the Namespace.
            namespace_id: Namespace Id for the Namespace.
            namespace_name: A name for the Namespace.

        Stability:
            stable
        """
        attrs: HttpNamespaceAttributes = {"namespaceArn": namespace_arn, "namespaceId": namespace_id, "namespaceName": namespace_name}

        return jsii.sinvoke(cls, "fromHttpNamespaceAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="createService")
    def create_service(self, id: str, *, custom_health_check: typing.Optional["HealthCheckCustomConfig"]=None, description: typing.Optional[str]=None, health_check: typing.Optional["HealthCheckConfig"]=None, name: typing.Optional[str]=None) -> "Service":
        """Creates a service within the namespace.

        Arguments:
            id: -
            props: -
            custom_health_check: Structure containing failure threshold for a custom health checker. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. See: https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html. Default: none
            description: A description of the service. Default: none
            health_check: Settings for an optional health check. If you specify health check settings, AWS Cloud Map associates the health check with the records that you specify in DnsConfig. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. Not valid for PrivateDnsNamespaces. If you use healthCheck, you can only register IP instances to this service. Default: none
            name: A name for the Service. Default: CloudFormation-generated name

        Stability:
            stable
        """
        props: BaseServiceProps = {}

        if custom_health_check is not None:
            props["customHealthCheck"] = custom_health_check

        if description is not None:
            props["description"] = description

        if health_check is not None:
            props["healthCheck"] = health_check

        if name is not None:
            props["name"] = name

        return jsii.invoke(self, "createService", [id, props])

    @property
    @jsii.member(jsii_name="httpNamespaceArn")
    def http_namespace_arn(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "httpNamespaceArn")

    @property
    @jsii.member(jsii_name="httpNamespaceId")
    def http_namespace_id(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "httpNamespaceId")

    @property
    @jsii.member(jsii_name="httpNamespaceName")
    def http_namespace_name(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "httpNamespaceName")

    @property
    @jsii.member(jsii_name="namespaceArn")
    def namespace_arn(self) -> str:
        """Namespace Arn for the namespace.

        Stability:
            stable
        """
        return jsii.get(self, "namespaceArn")

    @property
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> str:
        """Namespace Id for the namespace.

        Stability:
            stable
        """
        return jsii.get(self, "namespaceId")

    @property
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> str:
        """A name for the namespace.

        Stability:
            stable
        """
        return jsii.get(self, "namespaceName")

    @property
    @jsii.member(jsii_name="type")
    def type(self) -> "NamespaceType":
        """Type of the namespace.

        Stability:
            stable
        """
        return jsii.get(self, "type")


@jsii.interface(jsii_type="@aws-cdk/aws-servicediscovery.IPrivateDnsNamespace")
class IPrivateDnsNamespace(INamespace, jsii.compat.Protocol):
    """
    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IPrivateDnsNamespaceProxy

    pass

class _IPrivateDnsNamespaceProxy(jsii.proxy_for(INamespace)):
    """
    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-servicediscovery.IPrivateDnsNamespace"
    pass

@jsii.interface(jsii_type="@aws-cdk/aws-servicediscovery.IPublicDnsNamespace")
class IPublicDnsNamespace(INamespace, jsii.compat.Protocol):
    """
    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IPublicDnsNamespaceProxy

    pass

class _IPublicDnsNamespaceProxy(jsii.proxy_for(INamespace)):
    """
    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-servicediscovery.IPublicDnsNamespace"
    pass

@jsii.interface(jsii_type="@aws-cdk/aws-servicediscovery.IService")
class IService(aws_cdk.core.IResource, jsii.compat.Protocol):
    """
    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IServiceProxy

    @property
    @jsii.member(jsii_name="dnsRecordType")
    def dns_record_type(self) -> "DnsRecordType":
        """The DnsRecordType used by the service.

        Stability:
            stable
        """
        ...

    @property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> "INamespace":
        """The namespace for the Cloudmap Service.

        Stability:
            stable
        """
        ...

    @property
    @jsii.member(jsii_name="routingPolicy")
    def routing_policy(self) -> "RoutingPolicy":
        """The Routing Policy used by the service.

        Stability:
            stable
        """
        ...

    @property
    @jsii.member(jsii_name="serviceArn")
    def service_arn(self) -> str:
        """The Arn of the namespace that you want to use for DNS configuration.

        Stability:
            stable
        attribute:
            true
        """
        ...

    @property
    @jsii.member(jsii_name="serviceId")
    def service_id(self) -> str:
        """The ID of the namespace that you want to use for DNS configuration.

        Stability:
            stable
        attribute:
            true
        """
        ...

    @property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> str:
        """A name for the Cloudmap Service.

        Stability:
            stable
        attribute:
            true
        """
        ...


class _IServiceProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """
    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-servicediscovery.IService"
    @property
    @jsii.member(jsii_name="dnsRecordType")
    def dns_record_type(self) -> "DnsRecordType":
        """The DnsRecordType used by the service.

        Stability:
            stable
        """
        return jsii.get(self, "dnsRecordType")

    @property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> "INamespace":
        """The namespace for the Cloudmap Service.

        Stability:
            stable
        """
        return jsii.get(self, "namespace")

    @property
    @jsii.member(jsii_name="routingPolicy")
    def routing_policy(self) -> "RoutingPolicy":
        """The Routing Policy used by the service.

        Stability:
            stable
        """
        return jsii.get(self, "routingPolicy")

    @property
    @jsii.member(jsii_name="serviceArn")
    def service_arn(self) -> str:
        """The Arn of the namespace that you want to use for DNS configuration.

        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "serviceArn")

    @property
    @jsii.member(jsii_name="serviceId")
    def service_id(self) -> str:
        """The ID of the namespace that you want to use for DNS configuration.

        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "serviceId")

    @property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> str:
        """A name for the Cloudmap Service.

        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "serviceName")


@jsii.implements(IInstance)
class InstanceBase(aws_cdk.core.Resource, metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-servicediscovery.InstanceBase"):
    """
    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _InstanceBaseProxy

    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, physical_name: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time

        Stability:
            stable
        """
        props: aws_cdk.core.ResourceProps = {}

        if physical_name is not None:
            props["physicalName"] = physical_name

        jsii.create(InstanceBase, self, [scope, id, props])

    @jsii.member(jsii_name="uniqueInstanceId")
    def _unique_instance_id(self) -> str:
        """Generate a unique instance Id that is safe to pass to CloudMap.

        Stability:
            stable
        """
        return jsii.invoke(self, "uniqueInstanceId", [])

    @property
    @jsii.member(jsii_name="instanceId")
    @abc.abstractmethod
    def instance_id(self) -> str:
        """The Id of the instance.

        Stability:
            stable
        """
        ...

    @property
    @jsii.member(jsii_name="service")
    @abc.abstractmethod
    def service(self) -> "IService":
        """The Cloudmap service to which the instance is registered.

        Stability:
            stable
        """
        ...


class _InstanceBaseProxy(InstanceBase, jsii.proxy_for(aws_cdk.core.Resource)):
    @property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> str:
        """The Id of the instance.

        Stability:
            stable
        """
        return jsii.get(self, "instanceId")

    @property
    @jsii.member(jsii_name="service")
    def service(self) -> "IService":
        """The Cloudmap service to which the instance is registered.

        Stability:
            stable
        """
        return jsii.get(self, "service")


class AliasTargetInstance(InstanceBase, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-servicediscovery.AliasTargetInstance"):
    """Instance that uses Route 53 Alias record type.

    Currently, the only resource types supported are Elastic Load
    Balancers.

    Stability:
        stable
    resource:
        AWS::ServiceDiscovery::Instance
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, dns_name: str, service: "IService", custom_attributes: typing.Optional[typing.Mapping[str,str]]=None, instance_id: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            dns_name: DNS name of the target.
            service: The Cloudmap service this resource is registered to.
            custom_attributes: Custom attributes of the instance. Default: none
            instance_id: The id of the instance resource. Default: Automatically generated name

        Stability:
            stable
        """
        props: AliasTargetInstanceProps = {"dnsName": dns_name, "service": service}

        if custom_attributes is not None:
            props["customAttributes"] = custom_attributes

        if instance_id is not None:
            props["instanceId"] = instance_id

        jsii.create(AliasTargetInstance, self, [scope, id, props])

    @property
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> str:
        """The Route53 DNS name of the alias target.

        Stability:
            stable
        """
        return jsii.get(self, "dnsName")

    @property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> str:
        """The Id of the instance.

        Stability:
            stable
        """
        return jsii.get(self, "instanceId")

    @property
    @jsii.member(jsii_name="service")
    def service(self) -> "IService":
        """The Cloudmap service to which the instance is registered.

        Stability:
            stable
        """
        return jsii.get(self, "service")


class CnameInstance(InstanceBase, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-servicediscovery.CnameInstance"):
    """Instance that is accessible using a domain name (CNAME).

    Stability:
        stable
    resource:
        AWS::ServiceDiscovery::Instance
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, service: "IService", instance_cname: str, custom_attributes: typing.Optional[typing.Mapping[str,str]]=None, instance_id: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            service: The Cloudmap service this resource is registered to.
            instance_cname: If the service configuration includes a CNAME record, the domain name that you want Route 53 to return in response to DNS queries, for example, example.com. This value is required if the service specified by ServiceId includes settings for an CNAME record.
            custom_attributes: Custom attributes of the instance. Default: none
            instance_id: The id of the instance resource. Default: Automatically generated name

        Stability:
            stable
        """
        props: CnameInstanceProps = {"service": service, "instanceCname": instance_cname}

        if custom_attributes is not None:
            props["customAttributes"] = custom_attributes

        if instance_id is not None:
            props["instanceId"] = instance_id

        jsii.create(CnameInstance, self, [scope, id, props])

    @property
    @jsii.member(jsii_name="cname")
    def cname(self) -> str:
        """The domain name returned by DNS queries for the instance.

        Stability:
            stable
        """
        return jsii.get(self, "cname")

    @property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> str:
        """The Id of the instance.

        Stability:
            stable
        """
        return jsii.get(self, "instanceId")

    @property
    @jsii.member(jsii_name="service")
    def service(self) -> "IService":
        """The Cloudmap service to which the instance is registered.

        Stability:
            stable
        """
        return jsii.get(self, "service")


class IpInstance(InstanceBase, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-servicediscovery.IpInstance"):
    """Instance that is accessible using an IP address.

    Stability:
        stable
    resource:
        AWS::ServiceDiscovery::Instance
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, service: "IService", ipv4: typing.Optional[str]=None, ipv6: typing.Optional[str]=None, port: typing.Optional[jsii.Number]=None, custom_attributes: typing.Optional[typing.Mapping[str,str]]=None, instance_id: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            service: The Cloudmap service this resource is registered to.
            ipv4: If the service that you specify contains a template for an A record, the IPv4 address that you want AWS Cloud Map to use for the value of the A record. Default: none
            ipv6: If the service that you specify contains a template for an AAAA record, the IPv6 address that you want AWS Cloud Map to use for the value of the AAAA record. Default: none
            port: The port on the endpoint that you want AWS Cloud Map to perform health checks on. This value is also used for the port value in an SRV record if the service that you specify includes an SRV record. You can also specify a default port that is applied to all instances in the Service configuration. Default: 80
            custom_attributes: Custom attributes of the instance. Default: none
            instance_id: The id of the instance resource. Default: Automatically generated name

        Stability:
            stable
        """
        props: IpInstanceProps = {"service": service}

        if ipv4 is not None:
            props["ipv4"] = ipv4

        if ipv6 is not None:
            props["ipv6"] = ipv6

        if port is not None:
            props["port"] = port

        if custom_attributes is not None:
            props["customAttributes"] = custom_attributes

        if instance_id is not None:
            props["instanceId"] = instance_id

        jsii.create(IpInstance, self, [scope, id, props])

    @property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> str:
        """The Id of the instance.

        Stability:
            stable
        """
        return jsii.get(self, "instanceId")

    @property
    @jsii.member(jsii_name="ipv4")
    def ipv4(self) -> str:
        """The Ipv4 address of the instance, or blank string if none available.

        Stability:
            stable
        """
        return jsii.get(self, "ipv4")

    @property
    @jsii.member(jsii_name="ipv6")
    def ipv6(self) -> str:
        """The Ipv6 address of the instance, or blank string if none available.

        Stability:
            stable
        """
        return jsii.get(self, "ipv6")

    @property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        """The exposed port of the instance.

        Stability:
            stable
        """
        return jsii.get(self, "port")

    @property
    @jsii.member(jsii_name="service")
    def service(self) -> "IService":
        """The Cloudmap service to which the instance is registered.

        Stability:
            stable
        """
        return jsii.get(self, "service")


@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.IpInstanceBaseProps", jsii_struct_bases=[BaseInstanceProps])
class IpInstanceBaseProps(BaseInstanceProps, jsii.compat.TypedDict, total=False):
    """
    Stability:
        stable
    """
    ipv4: str
    """If the service that you specify contains a template for an A record, the IPv4 address that you want AWS Cloud Map to use for the value of the A record.

    Default:
        none

    Stability:
        stable
    """

    ipv6: str
    """If the service that you specify contains a template for an AAAA record, the IPv6 address that you want AWS Cloud Map to use for the value of the AAAA record.

    Default:
        none

    Stability:
        stable
    """

    port: jsii.Number
    """The port on the endpoint that you want AWS Cloud Map to perform health checks on.

    This value is also used for
    the port value in an SRV record if the service that you specify includes an SRV record. You can also specify a
    default port that is applied to all instances in the Service configuration.

    Default:
        80

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.IpInstanceProps", jsii_struct_bases=[IpInstanceBaseProps])
class IpInstanceProps(IpInstanceBaseProps, jsii.compat.TypedDict):
    """
    Stability:
        stable
    """
    service: "IService"
    """The Cloudmap service this resource is registered to.

    Stability:
        stable
    """

@jsii.enum(jsii_type="@aws-cdk/aws-servicediscovery.NamespaceType")
class NamespaceType(enum.Enum):
    """
    Stability:
        stable
    """
    HTTP = "HTTP"
    """Choose this option if you want your application to use only API calls to discover registered instances.

    Stability:
        stable
    """
    DNS_PRIVATE = "DNS_PRIVATE"
    """Choose this option if you want your application to be able to discover instances using either API calls or using DNS queries in a VPC.

    Stability:
        stable
    """
    DNS_PUBLIC = "DNS_PUBLIC"
    """Choose this option if you want your application to be able to discover instances using either API calls or using public DNS queries.

    You aren't required to use both methods.

    Stability:
        stable
    """

class NonIpInstance(InstanceBase, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-servicediscovery.NonIpInstance"):
    """Instance accessible using values other than an IP address or a domain name (CNAME). Specify the other values in Custom attributes.

    Stability:
        stable
    resource:
        AWS::ServiceDiscovery::Instance
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, service: "IService", custom_attributes: typing.Optional[typing.Mapping[str,str]]=None, instance_id: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            service: The Cloudmap service this resource is registered to.
            custom_attributes: Custom attributes of the instance. Default: none
            instance_id: The id of the instance resource. Default: Automatically generated name

        Stability:
            stable
        """
        props: NonIpInstanceProps = {"service": service}

        if custom_attributes is not None:
            props["customAttributes"] = custom_attributes

        if instance_id is not None:
            props["instanceId"] = instance_id

        jsii.create(NonIpInstance, self, [scope, id, props])

    @property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> str:
        """The Id of the instance.

        Stability:
            stable
        """
        return jsii.get(self, "instanceId")

    @property
    @jsii.member(jsii_name="service")
    def service(self) -> "IService":
        """The Cloudmap service to which the instance is registered.

        Stability:
            stable
        """
        return jsii.get(self, "service")


@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.NonIpInstanceBaseProps", jsii_struct_bases=[BaseInstanceProps])
class NonIpInstanceBaseProps(BaseInstanceProps, jsii.compat.TypedDict):
    """
    Stability:
        stable
    """
    pass

@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.NonIpInstanceProps", jsii_struct_bases=[NonIpInstanceBaseProps])
class NonIpInstanceProps(NonIpInstanceBaseProps, jsii.compat.TypedDict):
    """
    Stability:
        stable
    """
    service: "IService"
    """The Cloudmap service this resource is registered to.

    Stability:
        stable
    """

@jsii.implements(IPrivateDnsNamespace)
class PrivateDnsNamespace(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-servicediscovery.PrivateDnsNamespace"):
    """Define a Service Discovery HTTP Namespace.

    Stability:
        stable
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, vpc: aws_cdk.aws_ec2.IVpc, name: str, description: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            vpc: The Amazon VPC that you want to associate the namespace with.
            name: A name for the Namespace.
            description: A description of the Namespace. Default: none

        Stability:
            stable
        """
        props: PrivateDnsNamespaceProps = {"vpc": vpc, "name": name}

        if description is not None:
            props["description"] = description

        jsii.create(PrivateDnsNamespace, self, [scope, id, props])

    @jsii.member(jsii_name="fromPrivateDnsNamespaceAttributes")
    @classmethod
    def from_private_dns_namespace_attributes(cls, scope: aws_cdk.core.Construct, id: str, *, namespace_arn: str, namespace_id: str, namespace_name: str) -> "IPrivateDnsNamespace":
        """
        Arguments:
            scope: -
            id: -
            attrs: -
            namespace_arn: Namespace ARN for the Namespace.
            namespace_id: Namespace Id for the Namespace.
            namespace_name: A name for the Namespace.

        Stability:
            stable
        """
        attrs: PrivateDnsNamespaceAttributes = {"namespaceArn": namespace_arn, "namespaceId": namespace_id, "namespaceName": namespace_name}

        return jsii.sinvoke(cls, "fromPrivateDnsNamespaceAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="createService")
    def create_service(self, id: str, *, dns_record_type: typing.Optional["DnsRecordType"]=None, dns_ttl: typing.Optional[aws_cdk.core.Duration]=None, load_balancer: typing.Optional[bool]=None, routing_policy: typing.Optional["RoutingPolicy"]=None, custom_health_check: typing.Optional["HealthCheckCustomConfig"]=None, description: typing.Optional[str]=None, health_check: typing.Optional["HealthCheckConfig"]=None, name: typing.Optional[str]=None) -> "Service":
        """Creates a service within the namespace.

        Arguments:
            id: -
            props: -
            dns_record_type: The DNS type of the record that you want AWS Cloud Map to create. Supported record types include A, AAAA, A and AAAA (A_AAAA), CNAME, and SRV. Default: A
            dns_ttl: The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record. Default: Duration.minutes(1)
            load_balancer: Whether or not this service will have an Elastic LoadBalancer registered to it as an AliasTargetInstance. Setting this to ``true`` correctly configures the ``routingPolicy`` and performs some additional validation. Default: false
            routing_policy: The routing policy that you want to apply to all DNS records that AWS Cloud Map creates when you register an instance and specify this service. Default: WEIGHTED for CNAME records and when loadBalancer is true, MULTIVALUE otherwise
            custom_health_check: Structure containing failure threshold for a custom health checker. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. See: https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html. Default: none
            description: A description of the service. Default: none
            health_check: Settings for an optional health check. If you specify health check settings, AWS Cloud Map associates the health check with the records that you specify in DnsConfig. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. Not valid for PrivateDnsNamespaces. If you use healthCheck, you can only register IP instances to this service. Default: none
            name: A name for the Service. Default: CloudFormation-generated name

        Stability:
            stable
        """
        props: DnsServiceProps = {}

        if dns_record_type is not None:
            props["dnsRecordType"] = dns_record_type

        if dns_ttl is not None:
            props["dnsTtl"] = dns_ttl

        if load_balancer is not None:
            props["loadBalancer"] = load_balancer

        if routing_policy is not None:
            props["routingPolicy"] = routing_policy

        if custom_health_check is not None:
            props["customHealthCheck"] = custom_health_check

        if description is not None:
            props["description"] = description

        if health_check is not None:
            props["healthCheck"] = health_check

        if name is not None:
            props["name"] = name

        return jsii.invoke(self, "createService", [id, props])

    @property
    @jsii.member(jsii_name="namespaceArn")
    def namespace_arn(self) -> str:
        """Namespace Arn of the namespace.

        Stability:
            stable
        """
        return jsii.get(self, "namespaceArn")

    @property
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> str:
        """Namespace Id of the PrivateDnsNamespace.

        Stability:
            stable
        """
        return jsii.get(self, "namespaceId")

    @property
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> str:
        """The name of the PrivateDnsNamespace.

        Stability:
            stable
        """
        return jsii.get(self, "namespaceName")

    @property
    @jsii.member(jsii_name="privateDnsNamespaceArn")
    def private_dns_namespace_arn(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "privateDnsNamespaceArn")

    @property
    @jsii.member(jsii_name="privateDnsNamespaceId")
    def private_dns_namespace_id(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "privateDnsNamespaceId")

    @property
    @jsii.member(jsii_name="privateDnsNamespaceName")
    def private_dns_namespace_name(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "privateDnsNamespaceName")

    @property
    @jsii.member(jsii_name="type")
    def type(self) -> "NamespaceType":
        """Type of the namespace.

        Stability:
            stable
        """
        return jsii.get(self, "type")


@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.PrivateDnsNamespaceAttributes", jsii_struct_bases=[])
class PrivateDnsNamespaceAttributes(jsii.compat.TypedDict):
    """
    Stability:
        stable
    """
    namespaceArn: str
    """Namespace ARN for the Namespace.

    Stability:
        stable
    """

    namespaceId: str
    """Namespace Id for the Namespace.

    Stability:
        stable
    """

    namespaceName: str
    """A name for the Namespace.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.PrivateDnsNamespaceProps", jsii_struct_bases=[BaseNamespaceProps])
class PrivateDnsNamespaceProps(BaseNamespaceProps, jsii.compat.TypedDict):
    """
    Stability:
        stable
    """
    vpc: aws_cdk.aws_ec2.IVpc
    """The Amazon VPC that you want to associate the namespace with.

    Stability:
        stable
    """

@jsii.implements(IPublicDnsNamespace)
class PublicDnsNamespace(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-servicediscovery.PublicDnsNamespace"):
    """Define a Public DNS Namespace.

    Stability:
        stable
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, name: str, description: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            name: A name for the Namespace.
            description: A description of the Namespace. Default: none

        Stability:
            stable
        """
        props: PublicDnsNamespaceProps = {"name": name}

        if description is not None:
            props["description"] = description

        jsii.create(PublicDnsNamespace, self, [scope, id, props])

    @jsii.member(jsii_name="fromPublicDnsNamespaceAttributes")
    @classmethod
    def from_public_dns_namespace_attributes(cls, scope: aws_cdk.core.Construct, id: str, *, namespace_arn: str, namespace_id: str, namespace_name: str) -> "IPublicDnsNamespace":
        """
        Arguments:
            scope: -
            id: -
            attrs: -
            namespace_arn: Namespace ARN for the Namespace.
            namespace_id: Namespace Id for the Namespace.
            namespace_name: A name for the Namespace.

        Stability:
            stable
        """
        attrs: PublicDnsNamespaceAttributes = {"namespaceArn": namespace_arn, "namespaceId": namespace_id, "namespaceName": namespace_name}

        return jsii.sinvoke(cls, "fromPublicDnsNamespaceAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="createService")
    def create_service(self, id: str, *, dns_record_type: typing.Optional["DnsRecordType"]=None, dns_ttl: typing.Optional[aws_cdk.core.Duration]=None, load_balancer: typing.Optional[bool]=None, routing_policy: typing.Optional["RoutingPolicy"]=None, custom_health_check: typing.Optional["HealthCheckCustomConfig"]=None, description: typing.Optional[str]=None, health_check: typing.Optional["HealthCheckConfig"]=None, name: typing.Optional[str]=None) -> "Service":
        """Creates a service within the namespace.

        Arguments:
            id: -
            props: -
            dns_record_type: The DNS type of the record that you want AWS Cloud Map to create. Supported record types include A, AAAA, A and AAAA (A_AAAA), CNAME, and SRV. Default: A
            dns_ttl: The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record. Default: Duration.minutes(1)
            load_balancer: Whether or not this service will have an Elastic LoadBalancer registered to it as an AliasTargetInstance. Setting this to ``true`` correctly configures the ``routingPolicy`` and performs some additional validation. Default: false
            routing_policy: The routing policy that you want to apply to all DNS records that AWS Cloud Map creates when you register an instance and specify this service. Default: WEIGHTED for CNAME records and when loadBalancer is true, MULTIVALUE otherwise
            custom_health_check: Structure containing failure threshold for a custom health checker. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. See: https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html. Default: none
            description: A description of the service. Default: none
            health_check: Settings for an optional health check. If you specify health check settings, AWS Cloud Map associates the health check with the records that you specify in DnsConfig. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. Not valid for PrivateDnsNamespaces. If you use healthCheck, you can only register IP instances to this service. Default: none
            name: A name for the Service. Default: CloudFormation-generated name

        Stability:
            stable
        """
        props: DnsServiceProps = {}

        if dns_record_type is not None:
            props["dnsRecordType"] = dns_record_type

        if dns_ttl is not None:
            props["dnsTtl"] = dns_ttl

        if load_balancer is not None:
            props["loadBalancer"] = load_balancer

        if routing_policy is not None:
            props["routingPolicy"] = routing_policy

        if custom_health_check is not None:
            props["customHealthCheck"] = custom_health_check

        if description is not None:
            props["description"] = description

        if health_check is not None:
            props["healthCheck"] = health_check

        if name is not None:
            props["name"] = name

        return jsii.invoke(self, "createService", [id, props])

    @property
    @jsii.member(jsii_name="namespaceArn")
    def namespace_arn(self) -> str:
        """Namespace Arn for the namespace.

        Stability:
            stable
        """
        return jsii.get(self, "namespaceArn")

    @property
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> str:
        """Namespace Id for the namespace.

        Stability:
            stable
        """
        return jsii.get(self, "namespaceId")

    @property
    @jsii.member(jsii_name="namespaceName")
    def namespace_name(self) -> str:
        """A name for the namespace.

        Stability:
            stable
        """
        return jsii.get(self, "namespaceName")

    @property
    @jsii.member(jsii_name="publicDnsNamespaceArn")
    def public_dns_namespace_arn(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "publicDnsNamespaceArn")

    @property
    @jsii.member(jsii_name="publicDnsNamespaceId")
    def public_dns_namespace_id(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "publicDnsNamespaceId")

    @property
    @jsii.member(jsii_name="publicDnsNamespaceName")
    def public_dns_namespace_name(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "publicDnsNamespaceName")

    @property
    @jsii.member(jsii_name="type")
    def type(self) -> "NamespaceType":
        """Type of the namespace.

        Stability:
            stable
        """
        return jsii.get(self, "type")


@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.PublicDnsNamespaceAttributes", jsii_struct_bases=[])
class PublicDnsNamespaceAttributes(jsii.compat.TypedDict):
    """
    Stability:
        stable
    """
    namespaceArn: str
    """Namespace ARN for the Namespace.

    Stability:
        stable
    """

    namespaceId: str
    """Namespace Id for the Namespace.

    Stability:
        stable
    """

    namespaceName: str
    """A name for the Namespace.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.PublicDnsNamespaceProps", jsii_struct_bases=[BaseNamespaceProps])
class PublicDnsNamespaceProps(BaseNamespaceProps, jsii.compat.TypedDict):
    """
    Stability:
        stable
    """
    pass

@jsii.enum(jsii_type="@aws-cdk/aws-servicediscovery.RoutingPolicy")
class RoutingPolicy(enum.Enum):
    """
    Stability:
        stable
    """
    WEIGHTED = "WEIGHTED"
    """Route 53 returns the applicable value from one randomly selected instance from among the instances that you registered using the same service.

    Stability:
        stable
    """
    MULTIVALUE = "MULTIVALUE"
    """If you define a health check for the service and the health check is healthy, Route 53 returns the applicable value for up to eight instances.

    Stability:
        stable
    """

@jsii.implements(IService)
class Service(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-servicediscovery.Service"):
    """Define a CloudMap Service.

    Stability:
        stable
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, namespace: "INamespace", dns_record_type: typing.Optional["DnsRecordType"]=None, dns_ttl: typing.Optional[aws_cdk.core.Duration]=None, load_balancer: typing.Optional[bool]=None, routing_policy: typing.Optional["RoutingPolicy"]=None, custom_health_check: typing.Optional["HealthCheckCustomConfig"]=None, description: typing.Optional[str]=None, health_check: typing.Optional["HealthCheckConfig"]=None, name: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            namespace: The ID of the namespace that you want to use for DNS configuration.
            dns_record_type: The DNS type of the record that you want AWS Cloud Map to create. Supported record types include A, AAAA, A and AAAA (A_AAAA), CNAME, and SRV. Default: A
            dns_ttl: The amount of time, in seconds, that you want DNS resolvers to cache the settings for this record. Default: Duration.minutes(1)
            load_balancer: Whether or not this service will have an Elastic LoadBalancer registered to it as an AliasTargetInstance. Setting this to ``true`` correctly configures the ``routingPolicy`` and performs some additional validation. Default: false
            routing_policy: The routing policy that you want to apply to all DNS records that AWS Cloud Map creates when you register an instance and specify this service. Default: WEIGHTED for CNAME records and when loadBalancer is true, MULTIVALUE otherwise
            custom_health_check: Structure containing failure threshold for a custom health checker. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. See: https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html. Default: none
            description: A description of the service. Default: none
            health_check: Settings for an optional health check. If you specify health check settings, AWS Cloud Map associates the health check with the records that you specify in DnsConfig. Only one of healthCheckConfig or healthCheckCustomConfig can be specified. Not valid for PrivateDnsNamespaces. If you use healthCheck, you can only register IP instances to this service. Default: none
            name: A name for the Service. Default: CloudFormation-generated name

        Stability:
            stable
        """
        props: ServiceProps = {"namespace": namespace}

        if dns_record_type is not None:
            props["dnsRecordType"] = dns_record_type

        if dns_ttl is not None:
            props["dnsTtl"] = dns_ttl

        if load_balancer is not None:
            props["loadBalancer"] = load_balancer

        if routing_policy is not None:
            props["routingPolicy"] = routing_policy

        if custom_health_check is not None:
            props["customHealthCheck"] = custom_health_check

        if description is not None:
            props["description"] = description

        if health_check is not None:
            props["healthCheck"] = health_check

        if name is not None:
            props["name"] = name

        jsii.create(Service, self, [scope, id, props])

    @jsii.member(jsii_name="fromServiceAttributes")
    @classmethod
    def from_service_attributes(cls, scope: aws_cdk.core.Construct, id: str, *, dns_record_type: "DnsRecordType", routing_policy: "RoutingPolicy", service_arn: str, service_id: str, service_name: str) -> "IService":
        """
        Arguments:
            scope: -
            id: -
            attrs: -
            dns_record_type: 
            routing_policy: 
            service_arn: 
            service_id: 
            service_name: 

        Stability:
            stable
        """
        attrs: ServiceAttributes = {"dnsRecordType": dns_record_type, "routingPolicy": routing_policy, "serviceArn": service_arn, "serviceId": service_id, "serviceName": service_name}

        return jsii.sinvoke(cls, "fromServiceAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="registerCnameInstance")
    def register_cname_instance(self, id: str, *, instance_cname: str, custom_attributes: typing.Optional[typing.Mapping[str,str]]=None, instance_id: typing.Optional[str]=None) -> "IInstance":
        """Registers a resource that is accessible using a CNAME.

        Arguments:
            id: -
            props: -
            instance_cname: If the service configuration includes a CNAME record, the domain name that you want Route 53 to return in response to DNS queries, for example, example.com. This value is required if the service specified by ServiceId includes settings for an CNAME record.
            custom_attributes: Custom attributes of the instance. Default: none
            instance_id: The id of the instance resource. Default: Automatically generated name

        Stability:
            stable
        """
        props: CnameInstanceBaseProps = {"instanceCname": instance_cname}

        if custom_attributes is not None:
            props["customAttributes"] = custom_attributes

        if instance_id is not None:
            props["instanceId"] = instance_id

        return jsii.invoke(self, "registerCnameInstance", [id, props])

    @jsii.member(jsii_name="registerIpInstance")
    def register_ip_instance(self, id: str, *, ipv4: typing.Optional[str]=None, ipv6: typing.Optional[str]=None, port: typing.Optional[jsii.Number]=None, custom_attributes: typing.Optional[typing.Mapping[str,str]]=None, instance_id: typing.Optional[str]=None) -> "IInstance":
        """Registers a resource that is accessible using an IP address.

        Arguments:
            id: -
            props: -
            ipv4: If the service that you specify contains a template for an A record, the IPv4 address that you want AWS Cloud Map to use for the value of the A record. Default: none
            ipv6: If the service that you specify contains a template for an AAAA record, the IPv6 address that you want AWS Cloud Map to use for the value of the AAAA record. Default: none
            port: The port on the endpoint that you want AWS Cloud Map to perform health checks on. This value is also used for the port value in an SRV record if the service that you specify includes an SRV record. You can also specify a default port that is applied to all instances in the Service configuration. Default: 80
            custom_attributes: Custom attributes of the instance. Default: none
            instance_id: The id of the instance resource. Default: Automatically generated name

        Stability:
            stable
        """
        props: IpInstanceBaseProps = {}

        if ipv4 is not None:
            props["ipv4"] = ipv4

        if ipv6 is not None:
            props["ipv6"] = ipv6

        if port is not None:
            props["port"] = port

        if custom_attributes is not None:
            props["customAttributes"] = custom_attributes

        if instance_id is not None:
            props["instanceId"] = instance_id

        return jsii.invoke(self, "registerIpInstance", [id, props])

    @jsii.member(jsii_name="registerLoadBalancer")
    def register_load_balancer(self, id: str, load_balancer: aws_cdk.aws_elasticloadbalancingv2.ILoadBalancerV2, custom_attributes: typing.Optional[typing.Mapping[str,str]]=None) -> "IInstance":
        """Registers an ELB as a new instance with unique name instanceId in this service.

        Arguments:
            id: -
            load_balancer: -
            custom_attributes: -

        Stability:
            stable
        """
        return jsii.invoke(self, "registerLoadBalancer", [id, load_balancer, custom_attributes])

    @jsii.member(jsii_name="registerNonIpInstance")
    def register_non_ip_instance(self, id: str, *, custom_attributes: typing.Optional[typing.Mapping[str,str]]=None, instance_id: typing.Optional[str]=None) -> "IInstance":
        """Registers a resource that is accessible using values other than an IP address or a domain name (CNAME).

        Arguments:
            id: -
            props: -
            custom_attributes: Custom attributes of the instance. Default: none
            instance_id: The id of the instance resource. Default: Automatically generated name

        Stability:
            stable
        """
        props: NonIpInstanceBaseProps = {}

        if custom_attributes is not None:
            props["customAttributes"] = custom_attributes

        if instance_id is not None:
            props["instanceId"] = instance_id

        return jsii.invoke(self, "registerNonIpInstance", [id, props])

    @property
    @jsii.member(jsii_name="dnsRecordType")
    def dns_record_type(self) -> "DnsRecordType":
        """The DnsRecordType used by the service.

        Stability:
            stable
        """
        return jsii.get(self, "dnsRecordType")

    @property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> "INamespace":
        """The namespace for the Cloudmap Service.

        Stability:
            stable
        """
        return jsii.get(self, "namespace")

    @property
    @jsii.member(jsii_name="routingPolicy")
    def routing_policy(self) -> "RoutingPolicy":
        """The Routing Policy used by the service.

        Stability:
            stable
        """
        return jsii.get(self, "routingPolicy")

    @property
    @jsii.member(jsii_name="serviceArn")
    def service_arn(self) -> str:
        """The Arn of the namespace that you want to use for DNS configuration.

        Stability:
            stable
        """
        return jsii.get(self, "serviceArn")

    @property
    @jsii.member(jsii_name="serviceId")
    def service_id(self) -> str:
        """The ID of the namespace that you want to use for DNS configuration.

        Stability:
            stable
        """
        return jsii.get(self, "serviceId")

    @property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> str:
        """A name for the Cloudmap Service.

        Stability:
            stable
        """
        return jsii.get(self, "serviceName")


@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.ServiceAttributes", jsii_struct_bases=[])
class ServiceAttributes(jsii.compat.TypedDict):
    """
    Stability:
        stable
    """
    dnsRecordType: "DnsRecordType"
    """
    Stability:
        stable
    """

    routingPolicy: "RoutingPolicy"
    """
    Stability:
        stable
    """

    serviceArn: str
    """
    Stability:
        stable
    """

    serviceId: str
    """
    Stability:
        stable
    """

    serviceName: str
    """
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-servicediscovery.ServiceProps", jsii_struct_bases=[DnsServiceProps])
class ServiceProps(DnsServiceProps, jsii.compat.TypedDict):
    """
    Stability:
        stable
    """
    namespace: "INamespace"
    """The ID of the namespace that you want to use for DNS configuration.

    Stability:
        stable
    """

__all__ = ["AliasTargetInstance", "AliasTargetInstanceProps", "BaseInstanceProps", "BaseNamespaceProps", "BaseServiceProps", "CfnHttpNamespace", "CfnHttpNamespaceProps", "CfnInstance", "CfnInstanceProps", "CfnPrivateDnsNamespace", "CfnPrivateDnsNamespaceProps", "CfnPublicDnsNamespace", "CfnPublicDnsNamespaceProps", "CfnService", "CfnServiceProps", "CnameInstance", "CnameInstanceBaseProps", "CnameInstanceProps", "DnsRecordType", "DnsServiceProps", "HealthCheckConfig", "HealthCheckCustomConfig", "HealthCheckType", "HttpNamespace", "HttpNamespaceAttributes", "HttpNamespaceProps", "IHttpNamespace", "IInstance", "INamespace", "IPrivateDnsNamespace", "IPublicDnsNamespace", "IService", "InstanceBase", "IpInstance", "IpInstanceBaseProps", "IpInstanceProps", "NamespaceType", "NonIpInstance", "NonIpInstanceBaseProps", "NonIpInstanceProps", "PrivateDnsNamespace", "PrivateDnsNamespaceAttributes", "PrivateDnsNamespaceProps", "PublicDnsNamespace", "PublicDnsNamespaceAttributes", "PublicDnsNamespaceProps", "RoutingPolicy", "Service", "ServiceAttributes", "ServiceProps", "__jsii_assembly__"]

publication.publish()
