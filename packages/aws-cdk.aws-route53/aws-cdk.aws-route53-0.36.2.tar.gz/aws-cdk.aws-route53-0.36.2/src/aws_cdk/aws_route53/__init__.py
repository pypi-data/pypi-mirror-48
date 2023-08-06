import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_ec2
import aws_cdk.aws_logs
import aws_cdk.core
import aws_cdk.cx_api
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-route53", "0.36.2", __name__, "aws-route53@0.36.2.jsii.tgz")
@jsii.data_type(jsii_type="@aws-cdk/aws-route53.AliasRecordTargetConfig", jsii_struct_bases=[])
class AliasRecordTargetConfig(jsii.compat.TypedDict):
    """Represents the properties of an alias target destination.

    Stability:
        stable
    """
    dnsName: str
    """DNS name of the target.

    Stability:
        stable
    """

    hostedZoneId: str
    """Hosted zone ID of the target.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-route53.CaaRecordValue", jsii_struct_bases=[])
class CaaRecordValue(jsii.compat.TypedDict):
    """Properties for a CAA record value.

    Stability:
        stable
    """
    flag: jsii.Number
    """The flag.

    Stability:
        stable
    """

    tag: "CaaTag"
    """The tag.

    Stability:
        stable
    """

    value: str
    """The value associated with the tag.

    Stability:
        stable
    """

@jsii.enum(jsii_type="@aws-cdk/aws-route53.CaaTag")
class CaaTag(enum.Enum):
    """The CAA tag.

    Stability:
        stable
    """
    ISSUE = "ISSUE"
    """Explicity authorizes a single certificate authority to issue a certificate (any type) for the hostname.

    Stability:
        stable
    """
    ISSUEWILD = "ISSUEWILD"
    """Explicity authorizes a single certificate authority to issue a wildcard certificate (and only wildcard) for the hostname.

    Stability:
        stable
    """
    IODEF = "IODEF"
    """Specifies a URL to which a certificate authority may report policy violations.

    Stability:
        stable
    """

class CfnHealthCheck(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53.CfnHealthCheck"):
    """A CloudFormation ``AWS::Route53::HealthCheck``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html
    Stability:
        stable
    cloudformationResource:
        AWS::Route53::HealthCheck
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, health_check_config: typing.Union["HealthCheckConfigProperty", aws_cdk.core.IResolvable], health_check_tags: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "HealthCheckTagProperty"]]]]]=None) -> None:
        """Create a new ``AWS::Route53::HealthCheck``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            health_check_config: ``AWS::Route53::HealthCheck.HealthCheckConfig``.
            health_check_tags: ``AWS::Route53::HealthCheck.HealthCheckTags``.

        Stability:
            stable
        """
        props: CfnHealthCheckProps = {"healthCheckConfig": health_check_config}

        if health_check_tags is not None:
            props["healthCheckTags"] = health_check_tags

        jsii.create(CfnHealthCheck, self, [scope, id, props])

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
    @jsii.member(jsii_name="healthCheckConfig")
    def health_check_config(self) -> typing.Union["HealthCheckConfigProperty", aws_cdk.core.IResolvable]:
        """``AWS::Route53::HealthCheck.HealthCheckConfig``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#cfn-route53-healthcheck-healthcheckconfig
        Stability:
            stable
        """
        return jsii.get(self, "healthCheckConfig")

    @health_check_config.setter
    def health_check_config(self, value: typing.Union["HealthCheckConfigProperty", aws_cdk.core.IResolvable]):
        return jsii.set(self, "healthCheckConfig", value)

    @property
    @jsii.member(jsii_name="healthCheckTags")
    def health_check_tags(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "HealthCheckTagProperty"]]]]]:
        """``AWS::Route53::HealthCheck.HealthCheckTags``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#cfn-route53-healthcheck-healthchecktags
        Stability:
            stable
        """
        return jsii.get(self, "healthCheckTags")

    @health_check_tags.setter
    def health_check_tags(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "HealthCheckTagProperty"]]]]]):
        return jsii.set(self, "healthCheckTags", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-route53.CfnHealthCheck.AlarmIdentifierProperty", jsii_struct_bases=[])
    class AlarmIdentifierProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html
        Stability:
            stable
        """
        name: str
        """``CfnHealthCheck.AlarmIdentifierProperty.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html#cfn-route53-healthcheck-alarmidentifier-name
        Stability:
            stable
        """

        region: str
        """``CfnHealthCheck.AlarmIdentifierProperty.Region``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html#cfn-route53-healthcheck-alarmidentifier-region
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _HealthCheckConfigProperty(jsii.compat.TypedDict, total=False):
        alarmIdentifier: typing.Union[aws_cdk.core.IResolvable, "CfnHealthCheck.AlarmIdentifierProperty"]
        """``CfnHealthCheck.HealthCheckConfigProperty.AlarmIdentifier``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-alarmidentifier
        Stability:
            stable
        """
        childHealthChecks: typing.List[str]
        """``CfnHealthCheck.HealthCheckConfigProperty.ChildHealthChecks``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-childhealthchecks
        Stability:
            stable
        """
        enableSni: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnHealthCheck.HealthCheckConfigProperty.EnableSNI``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-enablesni
        Stability:
            stable
        """
        failureThreshold: jsii.Number
        """``CfnHealthCheck.HealthCheckConfigProperty.FailureThreshold``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-failurethreshold
        Stability:
            stable
        """
        fullyQualifiedDomainName: str
        """``CfnHealthCheck.HealthCheckConfigProperty.FullyQualifiedDomainName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-fullyqualifieddomainname
        Stability:
            stable
        """
        healthThreshold: jsii.Number
        """``CfnHealthCheck.HealthCheckConfigProperty.HealthThreshold``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-healththreshold
        Stability:
            stable
        """
        insufficientDataHealthStatus: str
        """``CfnHealthCheck.HealthCheckConfigProperty.InsufficientDataHealthStatus``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-insufficientdatahealthstatus
        Stability:
            stable
        """
        inverted: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnHealthCheck.HealthCheckConfigProperty.Inverted``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-inverted
        Stability:
            stable
        """
        ipAddress: str
        """``CfnHealthCheck.HealthCheckConfigProperty.IPAddress``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-ipaddress
        Stability:
            stable
        """
        measureLatency: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnHealthCheck.HealthCheckConfigProperty.MeasureLatency``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-measurelatency
        Stability:
            stable
        """
        port: jsii.Number
        """``CfnHealthCheck.HealthCheckConfigProperty.Port``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-port
        Stability:
            stable
        """
        regions: typing.List[str]
        """``CfnHealthCheck.HealthCheckConfigProperty.Regions``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-regions
        Stability:
            stable
        """
        requestInterval: jsii.Number
        """``CfnHealthCheck.HealthCheckConfigProperty.RequestInterval``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-requestinterval
        Stability:
            stable
        """
        resourcePath: str
        """``CfnHealthCheck.HealthCheckConfigProperty.ResourcePath``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-resourcepath
        Stability:
            stable
        """
        searchString: str
        """``CfnHealthCheck.HealthCheckConfigProperty.SearchString``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-searchstring
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-route53.CfnHealthCheck.HealthCheckConfigProperty", jsii_struct_bases=[_HealthCheckConfigProperty])
    class HealthCheckConfigProperty(_HealthCheckConfigProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html
        Stability:
            stable
        """
        type: str
        """``CfnHealthCheck.HealthCheckConfigProperty.Type``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-type
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-route53.CfnHealthCheck.HealthCheckTagProperty", jsii_struct_bases=[])
    class HealthCheckTagProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthchecktag.html
        Stability:
            stable
        """
        key: str
        """``CfnHealthCheck.HealthCheckTagProperty.Key``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthchecktag.html#cfn-route53-healthchecktags-key
        Stability:
            stable
        """

        value: str
        """``CfnHealthCheck.HealthCheckTagProperty.Value``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthchecktag.html#cfn-route53-healthchecktags-value
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnHealthCheckProps(jsii.compat.TypedDict, total=False):
    healthCheckTags: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnHealthCheck.HealthCheckTagProperty"]]]
    """``AWS::Route53::HealthCheck.HealthCheckTags``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#cfn-route53-healthcheck-healthchecktags
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-route53.CfnHealthCheckProps", jsii_struct_bases=[_CfnHealthCheckProps])
class CfnHealthCheckProps(_CfnHealthCheckProps):
    """Properties for defining a ``AWS::Route53::HealthCheck``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html
    Stability:
        stable
    """
    healthCheckConfig: typing.Union["CfnHealthCheck.HealthCheckConfigProperty", aws_cdk.core.IResolvable]
    """``AWS::Route53::HealthCheck.HealthCheckConfig``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#cfn-route53-healthcheck-healthcheckconfig
    Stability:
        stable
    """

class CfnHostedZone(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53.CfnHostedZone"):
    """A CloudFormation ``AWS::Route53::HostedZone``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html
    Stability:
        stable
    cloudformationResource:
        AWS::Route53::HostedZone
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, name: str, hosted_zone_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["HostedZoneConfigProperty"]]]=None, hosted_zone_tags: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "HostedZoneTagProperty"]]]]]=None, query_logging_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["QueryLoggingConfigProperty"]]]=None, vpcs: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union["VPCProperty", aws_cdk.core.IResolvable]]]]]=None) -> None:
        """Create a new ``AWS::Route53::HostedZone``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            name: ``AWS::Route53::HostedZone.Name``.
            hosted_zone_config: ``AWS::Route53::HostedZone.HostedZoneConfig``.
            hosted_zone_tags: ``AWS::Route53::HostedZone.HostedZoneTags``.
            query_logging_config: ``AWS::Route53::HostedZone.QueryLoggingConfig``.
            vpcs: ``AWS::Route53::HostedZone.VPCs``.

        Stability:
            stable
        """
        props: CfnHostedZoneProps = {"name": name}

        if hosted_zone_config is not None:
            props["hostedZoneConfig"] = hosted_zone_config

        if hosted_zone_tags is not None:
            props["hostedZoneTags"] = hosted_zone_tags

        if query_logging_config is not None:
            props["queryLoggingConfig"] = query_logging_config

        if vpcs is not None:
            props["vpcs"] = vpcs

        jsii.create(CfnHostedZone, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrNameServers")
    def attr_name_servers(self) -> typing.List[str]:
        """
        Stability:
            stable
        cloudformationAttribute:
            NameServers
        """
        return jsii.get(self, "attrNameServers")

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
        """``AWS::Route53::HostedZone.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-name
        Stability:
            stable
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="hostedZoneConfig")
    def hosted_zone_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["HostedZoneConfigProperty"]]]:
        """``AWS::Route53::HostedZone.HostedZoneConfig``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-hostedzoneconfig
        Stability:
            stable
        """
        return jsii.get(self, "hostedZoneConfig")

    @hosted_zone_config.setter
    def hosted_zone_config(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["HostedZoneConfigProperty"]]]):
        return jsii.set(self, "hostedZoneConfig", value)

    @property
    @jsii.member(jsii_name="hostedZoneTags")
    def hosted_zone_tags(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "HostedZoneTagProperty"]]]]]:
        """``AWS::Route53::HostedZone.HostedZoneTags``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-hostedzonetags
        Stability:
            stable
        """
        return jsii.get(self, "hostedZoneTags")

    @hosted_zone_tags.setter
    def hosted_zone_tags(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "HostedZoneTagProperty"]]]]]):
        return jsii.set(self, "hostedZoneTags", value)

    @property
    @jsii.member(jsii_name="queryLoggingConfig")
    def query_logging_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["QueryLoggingConfigProperty"]]]:
        """``AWS::Route53::HostedZone.QueryLoggingConfig``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-queryloggingconfig
        Stability:
            stable
        """
        return jsii.get(self, "queryLoggingConfig")

    @query_logging_config.setter
    def query_logging_config(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["QueryLoggingConfigProperty"]]]):
        return jsii.set(self, "queryLoggingConfig", value)

    @property
    @jsii.member(jsii_name="vpcs")
    def vpcs(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union["VPCProperty", aws_cdk.core.IResolvable]]]]]:
        """``AWS::Route53::HostedZone.VPCs``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-vpcs
        Stability:
            stable
        """
        return jsii.get(self, "vpcs")

    @vpcs.setter
    def vpcs(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union["VPCProperty", aws_cdk.core.IResolvable]]]]]):
        return jsii.set(self, "vpcs", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-route53.CfnHostedZone.HostedZoneConfigProperty", jsii_struct_bases=[])
    class HostedZoneConfigProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzoneconfig.html
        Stability:
            stable
        """
        comment: str
        """``CfnHostedZone.HostedZoneConfigProperty.Comment``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzoneconfig.html#cfn-route53-hostedzone-hostedzoneconfig-comment
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-route53.CfnHostedZone.HostedZoneTagProperty", jsii_struct_bases=[])
    class HostedZoneTagProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzonetags.html
        Stability:
            stable
        """
        key: str
        """``CfnHostedZone.HostedZoneTagProperty.Key``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzonetags.html#cfn-route53-hostedzonetags-key
        Stability:
            stable
        """

        value: str
        """``CfnHostedZone.HostedZoneTagProperty.Value``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzonetags.html#cfn-route53-hostedzonetags-value
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-route53.CfnHostedZone.QueryLoggingConfigProperty", jsii_struct_bases=[])
    class QueryLoggingConfigProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-queryloggingconfig.html
        Stability:
            stable
        """
        cloudWatchLogsLogGroupArn: str
        """``CfnHostedZone.QueryLoggingConfigProperty.CloudWatchLogsLogGroupArn``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-queryloggingconfig.html#cfn-route53-hostedzone-queryloggingconfig-cloudwatchlogsloggrouparn
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-route53.CfnHostedZone.VPCProperty", jsii_struct_bases=[])
    class VPCProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone-hostedzonevpcs.html
        Stability:
            stable
        """
        vpcId: str
        """``CfnHostedZone.VPCProperty.VPCId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone-hostedzonevpcs.html#cfn-route53-hostedzone-hostedzonevpcs-vpcid
        Stability:
            stable
        """

        vpcRegion: str
        """``CfnHostedZone.VPCProperty.VPCRegion``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone-hostedzonevpcs.html#cfn-route53-hostedzone-hostedzonevpcs-vpcregion
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnHostedZoneProps(jsii.compat.TypedDict, total=False):
    hostedZoneConfig: typing.Union[aws_cdk.core.IResolvable, "CfnHostedZone.HostedZoneConfigProperty"]
    """``AWS::Route53::HostedZone.HostedZoneConfig``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-hostedzoneconfig
    Stability:
        stable
    """
    hostedZoneTags: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnHostedZone.HostedZoneTagProperty"]]]
    """``AWS::Route53::HostedZone.HostedZoneTags``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-hostedzonetags
    Stability:
        stable
    """
    queryLoggingConfig: typing.Union[aws_cdk.core.IResolvable, "CfnHostedZone.QueryLoggingConfigProperty"]
    """``AWS::Route53::HostedZone.QueryLoggingConfig``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-queryloggingconfig
    Stability:
        stable
    """
    vpcs: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnHostedZone.VPCProperty", aws_cdk.core.IResolvable]]]
    """``AWS::Route53::HostedZone.VPCs``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-vpcs
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-route53.CfnHostedZoneProps", jsii_struct_bases=[_CfnHostedZoneProps])
class CfnHostedZoneProps(_CfnHostedZoneProps):
    """Properties for defining a ``AWS::Route53::HostedZone``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html
    Stability:
        stable
    """
    name: str
    """``AWS::Route53::HostedZone.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-name
    Stability:
        stable
    """

class CfnRecordSet(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53.CfnRecordSet"):
    """A CloudFormation ``AWS::Route53::RecordSet``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html
    Stability:
        stable
    cloudformationResource:
        AWS::Route53::RecordSet
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, name: str, type: str, alias_target: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AliasTargetProperty"]]]=None, comment: typing.Optional[str]=None, failover: typing.Optional[str]=None, geo_location: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["GeoLocationProperty"]]]=None, health_check_id: typing.Optional[str]=None, hosted_zone_id: typing.Optional[str]=None, hosted_zone_name: typing.Optional[str]=None, multi_value_answer: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, region: typing.Optional[str]=None, resource_records: typing.Optional[typing.List[str]]=None, set_identifier: typing.Optional[str]=None, ttl: typing.Optional[str]=None, weight: typing.Optional[jsii.Number]=None) -> None:
        """Create a new ``AWS::Route53::RecordSet``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            name: ``AWS::Route53::RecordSet.Name``.
            type: ``AWS::Route53::RecordSet.Type``.
            alias_target: ``AWS::Route53::RecordSet.AliasTarget``.
            comment: ``AWS::Route53::RecordSet.Comment``.
            failover: ``AWS::Route53::RecordSet.Failover``.
            geo_location: ``AWS::Route53::RecordSet.GeoLocation``.
            health_check_id: ``AWS::Route53::RecordSet.HealthCheckId``.
            hosted_zone_id: ``AWS::Route53::RecordSet.HostedZoneId``.
            hosted_zone_name: ``AWS::Route53::RecordSet.HostedZoneName``.
            multi_value_answer: ``AWS::Route53::RecordSet.MultiValueAnswer``.
            region: ``AWS::Route53::RecordSet.Region``.
            resource_records: ``AWS::Route53::RecordSet.ResourceRecords``.
            set_identifier: ``AWS::Route53::RecordSet.SetIdentifier``.
            ttl: ``AWS::Route53::RecordSet.TTL``.
            weight: ``AWS::Route53::RecordSet.Weight``.

        Stability:
            stable
        """
        props: CfnRecordSetProps = {"name": name, "type": type}

        if alias_target is not None:
            props["aliasTarget"] = alias_target

        if comment is not None:
            props["comment"] = comment

        if failover is not None:
            props["failover"] = failover

        if geo_location is not None:
            props["geoLocation"] = geo_location

        if health_check_id is not None:
            props["healthCheckId"] = health_check_id

        if hosted_zone_id is not None:
            props["hostedZoneId"] = hosted_zone_id

        if hosted_zone_name is not None:
            props["hostedZoneName"] = hosted_zone_name

        if multi_value_answer is not None:
            props["multiValueAnswer"] = multi_value_answer

        if region is not None:
            props["region"] = region

        if resource_records is not None:
            props["resourceRecords"] = resource_records

        if set_identifier is not None:
            props["setIdentifier"] = set_identifier

        if ttl is not None:
            props["ttl"] = ttl

        if weight is not None:
            props["weight"] = weight

        jsii.create(CfnRecordSet, self, [scope, id, props])

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
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::Route53::RecordSet.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-name
        Stability:
            stable
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="type")
    def type(self) -> str:
        """``AWS::Route53::RecordSet.Type``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-type
        Stability:
            stable
        """
        return jsii.get(self, "type")

    @type.setter
    def type(self, value: str):
        return jsii.set(self, "type", value)

    @property
    @jsii.member(jsii_name="aliasTarget")
    def alias_target(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AliasTargetProperty"]]]:
        """``AWS::Route53::RecordSet.AliasTarget``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-aliastarget
        Stability:
            stable
        """
        return jsii.get(self, "aliasTarget")

    @alias_target.setter
    def alias_target(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AliasTargetProperty"]]]):
        return jsii.set(self, "aliasTarget", value)

    @property
    @jsii.member(jsii_name="comment")
    def comment(self) -> typing.Optional[str]:
        """``AWS::Route53::RecordSet.Comment``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-comment
        Stability:
            stable
        """
        return jsii.get(self, "comment")

    @comment.setter
    def comment(self, value: typing.Optional[str]):
        return jsii.set(self, "comment", value)

    @property
    @jsii.member(jsii_name="failover")
    def failover(self) -> typing.Optional[str]:
        """``AWS::Route53::RecordSet.Failover``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-failover
        Stability:
            stable
        """
        return jsii.get(self, "failover")

    @failover.setter
    def failover(self, value: typing.Optional[str]):
        return jsii.set(self, "failover", value)

    @property
    @jsii.member(jsii_name="geoLocation")
    def geo_location(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["GeoLocationProperty"]]]:
        """``AWS::Route53::RecordSet.GeoLocation``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-geolocation
        Stability:
            stable
        """
        return jsii.get(self, "geoLocation")

    @geo_location.setter
    def geo_location(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["GeoLocationProperty"]]]):
        return jsii.set(self, "geoLocation", value)

    @property
    @jsii.member(jsii_name="healthCheckId")
    def health_check_id(self) -> typing.Optional[str]:
        """``AWS::Route53::RecordSet.HealthCheckId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-healthcheckid
        Stability:
            stable
        """
        return jsii.get(self, "healthCheckId")

    @health_check_id.setter
    def health_check_id(self, value: typing.Optional[str]):
        return jsii.set(self, "healthCheckId", value)

    @property
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> typing.Optional[str]:
        """``AWS::Route53::RecordSet.HostedZoneId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-hostedzoneid
        Stability:
            stable
        """
        return jsii.get(self, "hostedZoneId")

    @hosted_zone_id.setter
    def hosted_zone_id(self, value: typing.Optional[str]):
        return jsii.set(self, "hostedZoneId", value)

    @property
    @jsii.member(jsii_name="hostedZoneName")
    def hosted_zone_name(self) -> typing.Optional[str]:
        """``AWS::Route53::RecordSet.HostedZoneName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-hostedzonename
        Stability:
            stable
        """
        return jsii.get(self, "hostedZoneName")

    @hosted_zone_name.setter
    def hosted_zone_name(self, value: typing.Optional[str]):
        return jsii.set(self, "hostedZoneName", value)

    @property
    @jsii.member(jsii_name="multiValueAnswer")
    def multi_value_answer(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::Route53::RecordSet.MultiValueAnswer``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-multivalueanswer
        Stability:
            stable
        """
        return jsii.get(self, "multiValueAnswer")

    @multi_value_answer.setter
    def multi_value_answer(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "multiValueAnswer", value)

    @property
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[str]:
        """``AWS::Route53::RecordSet.Region``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-region
        Stability:
            stable
        """
        return jsii.get(self, "region")

    @region.setter
    def region(self, value: typing.Optional[str]):
        return jsii.set(self, "region", value)

    @property
    @jsii.member(jsii_name="resourceRecords")
    def resource_records(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Route53::RecordSet.ResourceRecords``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-resourcerecords
        Stability:
            stable
        """
        return jsii.get(self, "resourceRecords")

    @resource_records.setter
    def resource_records(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "resourceRecords", value)

    @property
    @jsii.member(jsii_name="setIdentifier")
    def set_identifier(self) -> typing.Optional[str]:
        """``AWS::Route53::RecordSet.SetIdentifier``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-setidentifier
        Stability:
            stable
        """
        return jsii.get(self, "setIdentifier")

    @set_identifier.setter
    def set_identifier(self, value: typing.Optional[str]):
        return jsii.set(self, "setIdentifier", value)

    @property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> typing.Optional[str]:
        """``AWS::Route53::RecordSet.TTL``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-ttl
        Stability:
            stable
        """
        return jsii.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: typing.Optional[str]):
        return jsii.set(self, "ttl", value)

    @property
    @jsii.member(jsii_name="weight")
    def weight(self) -> typing.Optional[jsii.Number]:
        """``AWS::Route53::RecordSet.Weight``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-weight
        Stability:
            stable
        """
        return jsii.get(self, "weight")

    @weight.setter
    def weight(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "weight", value)

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _AliasTargetProperty(jsii.compat.TypedDict, total=False):
        evaluateTargetHealth: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnRecordSet.AliasTargetProperty.EvaluateTargetHealth``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-evaluatetargethealth
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-route53.CfnRecordSet.AliasTargetProperty", jsii_struct_bases=[_AliasTargetProperty])
    class AliasTargetProperty(_AliasTargetProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html
        Stability:
            stable
        """
        dnsName: str
        """``CfnRecordSet.AliasTargetProperty.DNSName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-dnshostname
        Stability:
            stable
        """

        hostedZoneId: str
        """``CfnRecordSet.AliasTargetProperty.HostedZoneId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-hostedzoneid
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-route53.CfnRecordSet.GeoLocationProperty", jsii_struct_bases=[])
    class GeoLocationProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html
        Stability:
            stable
        """
        continentCode: str
        """``CfnRecordSet.GeoLocationProperty.ContinentCode``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordset-geolocation-continentcode
        Stability:
            stable
        """

        countryCode: str
        """``CfnRecordSet.GeoLocationProperty.CountryCode``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordset-geolocation-countrycode
        Stability:
            stable
        """

        subdivisionCode: str
        """``CfnRecordSet.GeoLocationProperty.SubdivisionCode``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordset-geolocation-subdivisioncode
        Stability:
            stable
        """


class CfnRecordSetGroup(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53.CfnRecordSetGroup"):
    """A CloudFormation ``AWS::Route53::RecordSetGroup``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html
    Stability:
        stable
    cloudformationResource:
        AWS::Route53::RecordSetGroup
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, comment: typing.Optional[str]=None, hosted_zone_id: typing.Optional[str]=None, hosted_zone_name: typing.Optional[str]=None, record_sets: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "RecordSetProperty"]]]]]=None) -> None:
        """Create a new ``AWS::Route53::RecordSetGroup``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            comment: ``AWS::Route53::RecordSetGroup.Comment``.
            hosted_zone_id: ``AWS::Route53::RecordSetGroup.HostedZoneId``.
            hosted_zone_name: ``AWS::Route53::RecordSetGroup.HostedZoneName``.
            record_sets: ``AWS::Route53::RecordSetGroup.RecordSets``.

        Stability:
            stable
        """
        props: CfnRecordSetGroupProps = {}

        if comment is not None:
            props["comment"] = comment

        if hosted_zone_id is not None:
            props["hostedZoneId"] = hosted_zone_id

        if hosted_zone_name is not None:
            props["hostedZoneName"] = hosted_zone_name

        if record_sets is not None:
            props["recordSets"] = record_sets

        jsii.create(CfnRecordSetGroup, self, [scope, id, props])

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
    @jsii.member(jsii_name="comment")
    def comment(self) -> typing.Optional[str]:
        """``AWS::Route53::RecordSetGroup.Comment``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-comment
        Stability:
            stable
        """
        return jsii.get(self, "comment")

    @comment.setter
    def comment(self, value: typing.Optional[str]):
        return jsii.set(self, "comment", value)

    @property
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> typing.Optional[str]:
        """``AWS::Route53::RecordSetGroup.HostedZoneId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-hostedzoneid
        Stability:
            stable
        """
        return jsii.get(self, "hostedZoneId")

    @hosted_zone_id.setter
    def hosted_zone_id(self, value: typing.Optional[str]):
        return jsii.set(self, "hostedZoneId", value)

    @property
    @jsii.member(jsii_name="hostedZoneName")
    def hosted_zone_name(self) -> typing.Optional[str]:
        """``AWS::Route53::RecordSetGroup.HostedZoneName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-hostedzonename
        Stability:
            stable
        """
        return jsii.get(self, "hostedZoneName")

    @hosted_zone_name.setter
    def hosted_zone_name(self, value: typing.Optional[str]):
        return jsii.set(self, "hostedZoneName", value)

    @property
    @jsii.member(jsii_name="recordSets")
    def record_sets(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "RecordSetProperty"]]]]]:
        """``AWS::Route53::RecordSetGroup.RecordSets``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-recordsets
        Stability:
            stable
        """
        return jsii.get(self, "recordSets")

    @record_sets.setter
    def record_sets(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "RecordSetProperty"]]]]]):
        return jsii.set(self, "recordSets", value)

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _AliasTargetProperty(jsii.compat.TypedDict, total=False):
        evaluateTargetHealth: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnRecordSetGroup.AliasTargetProperty.EvaluateTargetHealth``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-evaluatetargethealth
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-route53.CfnRecordSetGroup.AliasTargetProperty", jsii_struct_bases=[_AliasTargetProperty])
    class AliasTargetProperty(_AliasTargetProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html
        Stability:
            stable
        """
        dnsName: str
        """``CfnRecordSetGroup.AliasTargetProperty.DNSName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-dnshostname
        Stability:
            stable
        """

        hostedZoneId: str
        """``CfnRecordSetGroup.AliasTargetProperty.HostedZoneId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-aliastarget.html#cfn-route53-aliastarget-hostedzoneid
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-route53.CfnRecordSetGroup.GeoLocationProperty", jsii_struct_bases=[])
    class GeoLocationProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html
        Stability:
            stable
        """
        continentCode: str
        """``CfnRecordSetGroup.GeoLocationProperty.ContinentCode``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordsetgroup-geolocation-continentcode
        Stability:
            stable
        """

        countryCode: str
        """``CfnRecordSetGroup.GeoLocationProperty.CountryCode``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordset-geolocation-countrycode
        Stability:
            stable
        """

        subdivisionCode: str
        """``CfnRecordSetGroup.GeoLocationProperty.SubdivisionCode``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordset-geolocation-subdivisioncode
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _RecordSetProperty(jsii.compat.TypedDict, total=False):
        aliasTarget: typing.Union[aws_cdk.core.IResolvable, "CfnRecordSetGroup.AliasTargetProperty"]
        """``CfnRecordSetGroup.RecordSetProperty.AliasTarget``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-aliastarget
        Stability:
            stable
        """
        comment: str
        """``CfnRecordSetGroup.RecordSetProperty.Comment``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-comment
        Stability:
            stable
        """
        failover: str
        """``CfnRecordSetGroup.RecordSetProperty.Failover``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-failover
        Stability:
            stable
        """
        geoLocation: typing.Union[aws_cdk.core.IResolvable, "CfnRecordSetGroup.GeoLocationProperty"]
        """``CfnRecordSetGroup.RecordSetProperty.GeoLocation``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-geolocation
        Stability:
            stable
        """
        healthCheckId: str
        """``CfnRecordSetGroup.RecordSetProperty.HealthCheckId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-healthcheckid
        Stability:
            stable
        """
        hostedZoneId: str
        """``CfnRecordSetGroup.RecordSetProperty.HostedZoneId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-hostedzoneid
        Stability:
            stable
        """
        hostedZoneName: str
        """``CfnRecordSetGroup.RecordSetProperty.HostedZoneName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-hostedzonename
        Stability:
            stable
        """
        multiValueAnswer: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnRecordSetGroup.RecordSetProperty.MultiValueAnswer``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-multivalueanswer
        Stability:
            stable
        """
        region: str
        """``CfnRecordSetGroup.RecordSetProperty.Region``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-region
        Stability:
            stable
        """
        resourceRecords: typing.List[str]
        """``CfnRecordSetGroup.RecordSetProperty.ResourceRecords``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-resourcerecords
        Stability:
            stable
        """
        setIdentifier: str
        """``CfnRecordSetGroup.RecordSetProperty.SetIdentifier``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-setidentifier
        Stability:
            stable
        """
        ttl: str
        """``CfnRecordSetGroup.RecordSetProperty.TTL``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-ttl
        Stability:
            stable
        """
        weight: jsii.Number
        """``CfnRecordSetGroup.RecordSetProperty.Weight``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-weight
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-route53.CfnRecordSetGroup.RecordSetProperty", jsii_struct_bases=[_RecordSetProperty])
    class RecordSetProperty(_RecordSetProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html
        Stability:
            stable
        """
        name: str
        """``CfnRecordSetGroup.RecordSetProperty.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-name
        Stability:
            stable
        """

        type: str
        """``CfnRecordSetGroup.RecordSetProperty.Type``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-type
        Stability:
            stable
        """


@jsii.data_type(jsii_type="@aws-cdk/aws-route53.CfnRecordSetGroupProps", jsii_struct_bases=[])
class CfnRecordSetGroupProps(jsii.compat.TypedDict, total=False):
    """Properties for defining a ``AWS::Route53::RecordSetGroup``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html
    Stability:
        stable
    """
    comment: str
    """``AWS::Route53::RecordSetGroup.Comment``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-comment
    Stability:
        stable
    """

    hostedZoneId: str
    """``AWS::Route53::RecordSetGroup.HostedZoneId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-hostedzoneid
    Stability:
        stable
    """

    hostedZoneName: str
    """``AWS::Route53::RecordSetGroup.HostedZoneName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-hostedzonename
    Stability:
        stable
    """

    recordSets: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRecordSetGroup.RecordSetProperty"]]]
    """``AWS::Route53::RecordSetGroup.RecordSets``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-recordsets
    Stability:
        stable
    """

@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnRecordSetProps(jsii.compat.TypedDict, total=False):
    aliasTarget: typing.Union[aws_cdk.core.IResolvable, "CfnRecordSet.AliasTargetProperty"]
    """``AWS::Route53::RecordSet.AliasTarget``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-aliastarget
    Stability:
        stable
    """
    comment: str
    """``AWS::Route53::RecordSet.Comment``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-comment
    Stability:
        stable
    """
    failover: str
    """``AWS::Route53::RecordSet.Failover``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-failover
    Stability:
        stable
    """
    geoLocation: typing.Union[aws_cdk.core.IResolvable, "CfnRecordSet.GeoLocationProperty"]
    """``AWS::Route53::RecordSet.GeoLocation``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-geolocation
    Stability:
        stable
    """
    healthCheckId: str
    """``AWS::Route53::RecordSet.HealthCheckId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-healthcheckid
    Stability:
        stable
    """
    hostedZoneId: str
    """``AWS::Route53::RecordSet.HostedZoneId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-hostedzoneid
    Stability:
        stable
    """
    hostedZoneName: str
    """``AWS::Route53::RecordSet.HostedZoneName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-hostedzonename
    Stability:
        stable
    """
    multiValueAnswer: typing.Union[bool, aws_cdk.core.IResolvable]
    """``AWS::Route53::RecordSet.MultiValueAnswer``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-multivalueanswer
    Stability:
        stable
    """
    region: str
    """``AWS::Route53::RecordSet.Region``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-region
    Stability:
        stable
    """
    resourceRecords: typing.List[str]
    """``AWS::Route53::RecordSet.ResourceRecords``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-resourcerecords
    Stability:
        stable
    """
    setIdentifier: str
    """``AWS::Route53::RecordSet.SetIdentifier``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-setidentifier
    Stability:
        stable
    """
    ttl: str
    """``AWS::Route53::RecordSet.TTL``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-ttl
    Stability:
        stable
    """
    weight: jsii.Number
    """``AWS::Route53::RecordSet.Weight``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-weight
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-route53.CfnRecordSetProps", jsii_struct_bases=[_CfnRecordSetProps])
class CfnRecordSetProps(_CfnRecordSetProps):
    """Properties for defining a ``AWS::Route53::RecordSet``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html
    Stability:
        stable
    """
    name: str
    """``AWS::Route53::RecordSet.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-name
    Stability:
        stable
    """

    type: str
    """``AWS::Route53::RecordSet.Type``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-type
    Stability:
        stable
    """

@jsii.data_type_optionals(jsii_struct_bases=[])
class _CommonHostedZoneProps(jsii.compat.TypedDict, total=False):
    comment: str
    """Any comments that you want to include about the hosted zone.

    Default:
        none

    Stability:
        stable
    """
    queryLogsLogGroupArn: str
    """The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to.

    Default:
        disabled

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-route53.CommonHostedZoneProps", jsii_struct_bases=[_CommonHostedZoneProps])
class CommonHostedZoneProps(_CommonHostedZoneProps):
    """
    Stability:
        stable
    """
    zoneName: str
    """The name of the domain.

    For resource record types that include a domain
    name, specify a fully qualified domain name.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-route53.HostedZoneAttributes", jsii_struct_bases=[])
class HostedZoneAttributes(jsii.compat.TypedDict):
    """Reference to a hosted zone.

    Stability:
        stable
    """
    hostedZoneId: str
    """Identifier of the hosted zone.

    Stability:
        stable
    """

    zoneName: str
    """Name of the hosted zone.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-route53.HostedZoneProps", jsii_struct_bases=[CommonHostedZoneProps])
class HostedZoneProps(CommonHostedZoneProps, jsii.compat.TypedDict, total=False):
    """Properties of a new hosted zone.

    Stability:
        stable
    """
    vpcs: typing.List[aws_cdk.aws_ec2.IVpc]
    """A VPC that you want to associate with this hosted zone.

    When you specify
    this property, a private hosted zone will be created.

    You can associate additional VPCs to this private zone using ``addVpc(vpc)``.

    Default:
        public (no VPCs associated)

    Stability:
        stable
    """

@jsii.data_type_optionals(jsii_struct_bases=[])
class _HostedZoneProviderProps(jsii.compat.TypedDict, total=False):
    privateZone: bool
    """Is this a private zone.

    Stability:
        stable
    """
    vpcId: str
    """If this is a private zone which VPC is assocaitated.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-route53.HostedZoneProviderProps", jsii_struct_bases=[_HostedZoneProviderProps])
class HostedZoneProviderProps(_HostedZoneProviderProps):
    """Zone properties for looking up the Hosted Zone.

    Stability:
        stable
    """
    domainName: str
    """The zone domain e.g. example.com.

    Stability:
        stable
    """

@jsii.interface(jsii_type="@aws-cdk/aws-route53.IAliasRecordTarget")
class IAliasRecordTarget(jsii.compat.Protocol):
    """Classes that are valid alias record targets, like CloudFront distributions and load balancers, should implement this interface.

    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IAliasRecordTargetProxy

    @jsii.member(jsii_name="bind")
    def bind(self, record: "IRecordSet") -> "AliasRecordTargetConfig":
        """Return hosted zone ID and DNS name, usable for Route53 alias targets.

        Arguments:
            record: -

        Stability:
            stable
        """
        ...


class _IAliasRecordTargetProxy():
    """Classes that are valid alias record targets, like CloudFront distributions and load balancers, should implement this interface.

    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-route53.IAliasRecordTarget"
    @jsii.member(jsii_name="bind")
    def bind(self, record: "IRecordSet") -> "AliasRecordTargetConfig":
        """Return hosted zone ID and DNS name, usable for Route53 alias targets.

        Arguments:
            record: -

        Stability:
            stable
        """
        return jsii.invoke(self, "bind", [record])


@jsii.interface(jsii_type="@aws-cdk/aws-route53.IHostedZone")
class IHostedZone(aws_cdk.core.IResource, jsii.compat.Protocol):
    """Imported or created hosted zone.

    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IHostedZoneProxy

    @property
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> str:
        """ID of this hosted zone, such as "Z23ABC4XYZL05B".

        Stability:
            stable
        attribute:
            true
        """
        ...

    @property
    @jsii.member(jsii_name="zoneName")
    def zone_name(self) -> str:
        """FQDN of this hosted zone.

        Stability:
            stable
        """
        ...

    @property
    @jsii.member(jsii_name="hostedZoneNameServers")
    def hosted_zone_name_servers(self) -> typing.Optional[typing.List[str]]:
        """Returns the set of name servers for the specific hosted zone. For example: ns1.example.com.

        This attribute will be undefined for private hosted zones or hosted zones imported from another stack.

        Stability:
            stable
        attribute:
            true
        """
        ...


class _IHostedZoneProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """Imported or created hosted zone.

    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-route53.IHostedZone"
    @property
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> str:
        """ID of this hosted zone, such as "Z23ABC4XYZL05B".

        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "hostedZoneId")

    @property
    @jsii.member(jsii_name="zoneName")
    def zone_name(self) -> str:
        """FQDN of this hosted zone.

        Stability:
            stable
        """
        return jsii.get(self, "zoneName")

    @property
    @jsii.member(jsii_name="hostedZoneNameServers")
    def hosted_zone_name_servers(self) -> typing.Optional[typing.List[str]]:
        """Returns the set of name servers for the specific hosted zone. For example: ns1.example.com.

        This attribute will be undefined for private hosted zones or hosted zones imported from another stack.

        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "hostedZoneNameServers")


@jsii.implements(IHostedZone)
class HostedZone(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53.HostedZone"):
    """
    Stability:
        stable
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, vpcs: typing.Optional[typing.List[aws_cdk.aws_ec2.IVpc]]=None, zone_name: str, comment: typing.Optional[str]=None, query_logs_log_group_arn: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            vpcs: A VPC that you want to associate with this hosted zone. When you specify this property, a private hosted zone will be created. You can associate additional VPCs to this private zone using ``addVpc(vpc)``. Default: public (no VPCs associated)
            zone_name: The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name.
            comment: Any comments that you want to include about the hosted zone. Default: none
            query_logs_log_group_arn: The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to. Default: disabled

        Stability:
            stable
        """
        props: HostedZoneProps = {"zoneName": zone_name}

        if vpcs is not None:
            props["vpcs"] = vpcs

        if comment is not None:
            props["comment"] = comment

        if query_logs_log_group_arn is not None:
            props["queryLogsLogGroupArn"] = query_logs_log_group_arn

        jsii.create(HostedZone, self, [scope, id, props])

    @jsii.member(jsii_name="fromHostedZoneAttributes")
    @classmethod
    def from_hosted_zone_attributes(cls, scope: aws_cdk.core.Construct, id: str, *, hosted_zone_id: str, zone_name: str) -> "IHostedZone":
        """Imports a hosted zone from another stack.

        Arguments:
            scope: -
            id: -
            attrs: -
            hosted_zone_id: Identifier of the hosted zone.
            zone_name: Name of the hosted zone.

        Stability:
            stable
        """
        attrs: HostedZoneAttributes = {"hostedZoneId": hosted_zone_id, "zoneName": zone_name}

        return jsii.sinvoke(cls, "fromHostedZoneAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="fromHostedZoneId")
    @classmethod
    def from_hosted_zone_id(cls, scope: aws_cdk.core.Construct, id: str, hosted_zone_id: str) -> "IHostedZone":
        """
        Arguments:
            scope: -
            id: -
            hosted_zone_id: -

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "fromHostedZoneId", [scope, id, hosted_zone_id])

    @jsii.member(jsii_name="fromLookup")
    @classmethod
    def from_lookup(cls, scope: aws_cdk.core.Construct, id: str, *, domain_name: str, private_zone: typing.Optional[bool]=None, vpc_id: typing.Optional[str]=None) -> "IHostedZone":
        """Lookup a hosted zone in the current account/region based on query parameters.

        Arguments:
            scope: -
            id: -
            query: -
            domain_name: The zone domain e.g. example.com.
            private_zone: Is this a private zone.
            vpc_id: If this is a private zone which VPC is assocaitated.

        Stability:
            stable
        """
        query: HostedZoneProviderProps = {"domainName": domain_name}

        if private_zone is not None:
            query["privateZone"] = private_zone

        if vpc_id is not None:
            query["vpcId"] = vpc_id

        return jsii.sinvoke(cls, "fromLookup", [scope, id, query])

    @jsii.member(jsii_name="addVpc")
    def add_vpc(self, vpc: aws_cdk.aws_ec2.IVpc) -> None:
        """Add another VPC to this private hosted zone.

        Arguments:
            vpc: the other VPC to add.

        Stability:
            stable
        """
        return jsii.invoke(self, "addVpc", [vpc])

    @property
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> str:
        """ID of this hosted zone, such as "Z23ABC4XYZL05B".

        Stability:
            stable
        """
        return jsii.get(self, "hostedZoneId")

    @property
    @jsii.member(jsii_name="vpcs")
    def _vpcs(self) -> typing.List["CfnHostedZone.VPCProperty"]:
        """VPCs to which this hosted zone will be added.

        Stability:
            stable
        """
        return jsii.get(self, "vpcs")

    @property
    @jsii.member(jsii_name="zoneName")
    def zone_name(self) -> str:
        """FQDN of this hosted zone.

        Stability:
            stable
        """
        return jsii.get(self, "zoneName")

    @property
    @jsii.member(jsii_name="hostedZoneNameServers")
    def hosted_zone_name_servers(self) -> typing.Optional[typing.List[str]]:
        """Returns the set of name servers for the specific hosted zone. For example: ns1.example.com.

        This attribute will be undefined for private hosted zones or hosted zones imported from another stack.

        Stability:
            stable
        """
        return jsii.get(self, "hostedZoneNameServers")


@jsii.interface(jsii_type="@aws-cdk/aws-route53.IPrivateHostedZone")
class IPrivateHostedZone(IHostedZone, jsii.compat.Protocol):
    """
    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IPrivateHostedZoneProxy

    pass

class _IPrivateHostedZoneProxy(jsii.proxy_for(IHostedZone)):
    """
    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-route53.IPrivateHostedZone"
    pass

@jsii.interface(jsii_type="@aws-cdk/aws-route53.IPublicHostedZone")
class IPublicHostedZone(IHostedZone, jsii.compat.Protocol):
    """
    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IPublicHostedZoneProxy

    pass

class _IPublicHostedZoneProxy(jsii.proxy_for(IHostedZone)):
    """
    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-route53.IPublicHostedZone"
    pass

@jsii.interface(jsii_type="@aws-cdk/aws-route53.IRecordSet")
class IRecordSet(aws_cdk.core.IResource, jsii.compat.Protocol):
    """A record set.

    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IRecordSetProxy

    @property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> str:
        """The domain name of the record.

        Stability:
            stable
        """
        ...


class _IRecordSetProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """A record set.

    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-route53.IRecordSet"
    @property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> str:
        """The domain name of the record.

        Stability:
            stable
        """
        return jsii.get(self, "domainName")


@jsii.data_type(jsii_type="@aws-cdk/aws-route53.MxRecordValue", jsii_struct_bases=[])
class MxRecordValue(jsii.compat.TypedDict):
    """Properties for a MX record value.

    Stability:
        stable
    """
    hostName: str
    """The mail server host name.

    Stability:
        stable
    """

    priority: jsii.Number
    """The priority.

    Stability:
        stable
    """

@jsii.implements(IPrivateHostedZone)
class PrivateHostedZone(HostedZone, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53.PrivateHostedZone"):
    """Create a Route53 private hosted zone for use in one or more VPCs.

    Note that ``enableDnsHostnames`` and ``enableDnsSupport`` must have been enabled
    for the VPC you're configuring for private hosted zones.

    Stability:
        stable
    resource:
        AWS::Route53::HostedZone
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, vpc: aws_cdk.aws_ec2.IVpc, zone_name: str, comment: typing.Optional[str]=None, query_logs_log_group_arn: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            vpc: A VPC that you want to associate with this hosted zone. Private hosted zones must be associated with at least one VPC. You can associated additional VPCs using ``addVpc(vpc)``.
            zone_name: The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name.
            comment: Any comments that you want to include about the hosted zone. Default: none
            query_logs_log_group_arn: The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to. Default: disabled

        Stability:
            stable
        """
        props: PrivateHostedZoneProps = {"vpc": vpc, "zoneName": zone_name}

        if comment is not None:
            props["comment"] = comment

        if query_logs_log_group_arn is not None:
            props["queryLogsLogGroupArn"] = query_logs_log_group_arn

        jsii.create(PrivateHostedZone, self, [scope, id, props])

    @jsii.member(jsii_name="fromPrivateHostedZoneId")
    @classmethod
    def from_private_hosted_zone_id(cls, scope: aws_cdk.core.Construct, id: str, private_hosted_zone_id: str) -> "IPrivateHostedZone":
        """
        Arguments:
            scope: -
            id: -
            private_hosted_zone_id: -

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "fromPrivateHostedZoneId", [scope, id, private_hosted_zone_id])


@jsii.data_type(jsii_type="@aws-cdk/aws-route53.PrivateHostedZoneProps", jsii_struct_bases=[CommonHostedZoneProps])
class PrivateHostedZoneProps(CommonHostedZoneProps, jsii.compat.TypedDict):
    """
    Stability:
        stable
    """
    vpc: aws_cdk.aws_ec2.IVpc
    """A VPC that you want to associate with this hosted zone.

    Private hosted zones must be associated with at least one VPC. You can
    associated additional VPCs using ``addVpc(vpc)``.

    Stability:
        stable
    """

@jsii.implements(IPublicHostedZone)
class PublicHostedZone(HostedZone, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53.PublicHostedZone"):
    """Create a Route53 public hosted zone.

    Stability:
        stable
    resource:
        AWS::Route53::HostedZone
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, caa_amazon: typing.Optional[bool]=None, zone_name: str, comment: typing.Optional[str]=None, query_logs_log_group_arn: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            caa_amazon: Whether to create a CAA record to restrict certificate authorities allowed to issue certificates for this domain to Amazon only. Default: false
            zone_name: The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name.
            comment: Any comments that you want to include about the hosted zone. Default: none
            query_logs_log_group_arn: The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to. Default: disabled

        Stability:
            stable
        """
        props: PublicHostedZoneProps = {"zoneName": zone_name}

        if caa_amazon is not None:
            props["caaAmazon"] = caa_amazon

        if comment is not None:
            props["comment"] = comment

        if query_logs_log_group_arn is not None:
            props["queryLogsLogGroupArn"] = query_logs_log_group_arn

        jsii.create(PublicHostedZone, self, [scope, id, props])

    @jsii.member(jsii_name="fromPublicHostedZoneId")
    @classmethod
    def from_public_hosted_zone_id(cls, scope: aws_cdk.core.Construct, id: str, public_hosted_zone_id: str) -> "IPublicHostedZone":
        """
        Arguments:
            scope: -
            id: -
            public_hosted_zone_id: -

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "fromPublicHostedZoneId", [scope, id, public_hosted_zone_id])

    @jsii.member(jsii_name="addDelegation")
    def add_delegation(self, delegate: "IPublicHostedZone", *, comment: typing.Optional[str]=None, ttl: typing.Optional[aws_cdk.core.Duration]=None) -> None:
        """Adds a delegation from this zone to a designated zone.

        Arguments:
            delegate: the zone being delegated to.
            opts: options for creating the DNS record, if any.
            comment: A comment to add on the DNS record created to incorporate the delegation. Default: none
            ttl: The TTL (Time To Live) of the DNS delegation record in DNS caches. Default: 172800

        Stability:
            stable
        """
        opts: ZoneDelegationOptions = {}

        if comment is not None:
            opts["comment"] = comment

        if ttl is not None:
            opts["ttl"] = ttl

        return jsii.invoke(self, "addDelegation", [delegate, opts])

    @jsii.member(jsii_name="addVpc")
    def add_vpc(self, _vpc: aws_cdk.aws_ec2.IVpc) -> None:
        """Add another VPC to this private hosted zone.

        Arguments:
            _vpc: -

        Stability:
            stable
        """
        return jsii.invoke(self, "addVpc", [_vpc])


@jsii.data_type(jsii_type="@aws-cdk/aws-route53.PublicHostedZoneProps", jsii_struct_bases=[CommonHostedZoneProps])
class PublicHostedZoneProps(CommonHostedZoneProps, jsii.compat.TypedDict, total=False):
    """Construction properties for a PublicHostedZone.

    Stability:
        stable
    """
    caaAmazon: bool
    """Whether to create a CAA record to restrict certificate authorities allowed to issue certificates for this domain to Amazon only.

    Default:
        false

    Stability:
        stable
    """

@jsii.implements(IRecordSet)
class RecordSet(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53.RecordSet"):
    """A record set.

    Stability:
        stable
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, record_type: "RecordType", target: "RecordTarget", zone: "IHostedZone", comment: typing.Optional[str]=None, record_name: typing.Optional[str]=None, ttl: typing.Optional[aws_cdk.core.Duration]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            record_type: The record type.
            target: The target for this record, either ``RecordTarget.fromValues()`` or ``RecordTarget.fromAlias()``.
            zone: The hosted zone in which to define the new record.
            comment: A comment to add on the record. Default: no comment
            record_name: The domain name for this record. Default: zone root
            ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)

        Stability:
            stable
        """
        props: RecordSetProps = {"recordType": record_type, "target": target, "zone": zone}

        if comment is not None:
            props["comment"] = comment

        if record_name is not None:
            props["recordName"] = record_name

        if ttl is not None:
            props["ttl"] = ttl

        jsii.create(RecordSet, self, [scope, id, props])

    @property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> str:
        """The domain name of the record.

        Stability:
            stable
        """
        return jsii.get(self, "domainName")


class ARecord(RecordSet, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53.ARecord"):
    """A DNS A record.

    Stability:
        stable
    resource:
        AWS::Route53::RecordSet
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, target: "RecordTarget", zone: "IHostedZone", comment: typing.Optional[str]=None, record_name: typing.Optional[str]=None, ttl: typing.Optional[aws_cdk.core.Duration]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            target: The target.
            zone: The hosted zone in which to define the new record.
            comment: A comment to add on the record. Default: no comment
            record_name: The domain name for this record. Default: zone root
            ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)

        Stability:
            stable
        """
        props: ARecordProps = {"target": target, "zone": zone}

        if comment is not None:
            props["comment"] = comment

        if record_name is not None:
            props["recordName"] = record_name

        if ttl is not None:
            props["ttl"] = ttl

        jsii.create(ARecord, self, [scope, id, props])


class AaaaRecord(RecordSet, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53.AaaaRecord"):
    """A DNS AAAA record.

    Stability:
        stable
    resource:
        AWS::Route53::RecordSet
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, target: "AddressRecordTarget", zone: "IHostedZone", comment: typing.Optional[str]=None, record_name: typing.Optional[str]=None, ttl: typing.Optional[aws_cdk.core.Duration]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            target: The target.
            zone: The hosted zone in which to define the new record.
            comment: A comment to add on the record. Default: no comment
            record_name: The domain name for this record. Default: zone root
            ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)

        Stability:
            stable
        """
        props: AaaaRecordProps = {"target": target, "zone": zone}

        if comment is not None:
            props["comment"] = comment

        if record_name is not None:
            props["recordName"] = record_name

        if ttl is not None:
            props["ttl"] = ttl

        jsii.create(AaaaRecord, self, [scope, id, props])


class CaaRecord(RecordSet, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53.CaaRecord"):
    """A DNS CAA record.

    Stability:
        stable
    resource:
        AWS::Route53::RecordSet
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, values: typing.List["CaaRecordValue"], zone: "IHostedZone", comment: typing.Optional[str]=None, record_name: typing.Optional[str]=None, ttl: typing.Optional[aws_cdk.core.Duration]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            values: The values.
            zone: The hosted zone in which to define the new record.
            comment: A comment to add on the record. Default: no comment
            record_name: The domain name for this record. Default: zone root
            ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)

        Stability:
            stable
        """
        props: CaaRecordProps = {"values": values, "zone": zone}

        if comment is not None:
            props["comment"] = comment

        if record_name is not None:
            props["recordName"] = record_name

        if ttl is not None:
            props["ttl"] = ttl

        jsii.create(CaaRecord, self, [scope, id, props])


class CaaAmazonRecord(CaaRecord, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53.CaaAmazonRecord"):
    """A DNS Amazon CAA record.

    A CAA record to restrict certificate authorities allowed
    to issue certificates for a domain to Amazon only.

    Stability:
        stable
    resource:
        AWS::Route53::RecordSet
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, zone: "IHostedZone", comment: typing.Optional[str]=None, record_name: typing.Optional[str]=None, ttl: typing.Optional[aws_cdk.core.Duration]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            zone: The hosted zone in which to define the new record.
            comment: A comment to add on the record. Default: no comment
            record_name: The domain name for this record. Default: zone root
            ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)

        Stability:
            stable
        """
        props: CaaAmazonRecordProps = {"zone": zone}

        if comment is not None:
            props["comment"] = comment

        if record_name is not None:
            props["recordName"] = record_name

        if ttl is not None:
            props["ttl"] = ttl

        jsii.create(CaaAmazonRecord, self, [scope, id, props])


class CnameRecord(RecordSet, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53.CnameRecord"):
    """A DNS CNAME record.

    Stability:
        stable
    resource:
        AWS::Route53::RecordSet
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, domain_name: str, zone: "IHostedZone", comment: typing.Optional[str]=None, record_name: typing.Optional[str]=None, ttl: typing.Optional[aws_cdk.core.Duration]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            domain_name: The domain name.
            zone: The hosted zone in which to define the new record.
            comment: A comment to add on the record. Default: no comment
            record_name: The domain name for this record. Default: zone root
            ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)

        Stability:
            stable
        """
        props: CnameRecordProps = {"domainName": domain_name, "zone": zone}

        if comment is not None:
            props["comment"] = comment

        if record_name is not None:
            props["recordName"] = record_name

        if ttl is not None:
            props["ttl"] = ttl

        jsii.create(CnameRecord, self, [scope, id, props])


class MxRecord(RecordSet, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53.MxRecord"):
    """A DNS MX record.

    Stability:
        stable
    resource:
        AWS::Route53::RecordSet
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, values: typing.List["MxRecordValue"], zone: "IHostedZone", comment: typing.Optional[str]=None, record_name: typing.Optional[str]=None, ttl: typing.Optional[aws_cdk.core.Duration]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            values: The values.
            zone: The hosted zone in which to define the new record.
            comment: A comment to add on the record. Default: no comment
            record_name: The domain name for this record. Default: zone root
            ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)

        Stability:
            stable
        """
        props: MxRecordProps = {"values": values, "zone": zone}

        if comment is not None:
            props["comment"] = comment

        if record_name is not None:
            props["recordName"] = record_name

        if ttl is not None:
            props["ttl"] = ttl

        jsii.create(MxRecord, self, [scope, id, props])


@jsii.data_type_optionals(jsii_struct_bases=[])
class _RecordSetOptions(jsii.compat.TypedDict, total=False):
    comment: str
    """A comment to add on the record.

    Default:
        no comment

    Stability:
        stable
    """
    recordName: str
    """The domain name for this record.

    Default:
        zone root

    Stability:
        stable
    """
    ttl: aws_cdk.core.Duration
    """The resource record cache time to live (TTL).

    Default:
        Duration.minutes(30)

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-route53.RecordSetOptions", jsii_struct_bases=[_RecordSetOptions])
class RecordSetOptions(_RecordSetOptions):
    """Options for a RecordSet.

    Stability:
        stable
    """
    zone: "IHostedZone"
    """The hosted zone in which to define the new record.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-route53.ARecordProps", jsii_struct_bases=[RecordSetOptions])
class ARecordProps(RecordSetOptions, jsii.compat.TypedDict):
    """Construction properties for a ARecord.

    Stability:
        stable
    """
    target: "RecordTarget"
    """The target.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-route53.AaaaRecordProps", jsii_struct_bases=[RecordSetOptions])
class AaaaRecordProps(RecordSetOptions, jsii.compat.TypedDict):
    """Construction properties for a AaaaRecord.

    Stability:
        stable
    """
    target: "AddressRecordTarget"
    """The target.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-route53.CaaAmazonRecordProps", jsii_struct_bases=[RecordSetOptions])
class CaaAmazonRecordProps(RecordSetOptions, jsii.compat.TypedDict):
    """Construction properties for a CaaAmazonRecord.

    Stability:
        stable
    """
    pass

@jsii.data_type(jsii_type="@aws-cdk/aws-route53.CaaRecordProps", jsii_struct_bases=[RecordSetOptions])
class CaaRecordProps(RecordSetOptions, jsii.compat.TypedDict):
    """Construction properties for a CaaRecord.

    Stability:
        stable
    """
    values: typing.List["CaaRecordValue"]
    """The values.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-route53.CnameRecordProps", jsii_struct_bases=[RecordSetOptions])
class CnameRecordProps(RecordSetOptions, jsii.compat.TypedDict):
    """Construction properties for a CnameRecord.

    Stability:
        stable
    """
    domainName: str
    """The domain name.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-route53.MxRecordProps", jsii_struct_bases=[RecordSetOptions])
class MxRecordProps(RecordSetOptions, jsii.compat.TypedDict):
    """Construction properties for a MxRecord.

    Stability:
        stable
    """
    values: typing.List["MxRecordValue"]
    """The values.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-route53.RecordSetProps", jsii_struct_bases=[RecordSetOptions])
class RecordSetProps(RecordSetOptions, jsii.compat.TypedDict):
    """Construction properties for a RecordSet.

    Stability:
        stable
    """
    recordType: "RecordType"
    """The record type.

    Stability:
        stable
    """

    target: "RecordTarget"
    """The target for this record, either ``RecordTarget.fromValues()`` or ``RecordTarget.fromAlias()``.

    Stability:
        stable
    """

class RecordTarget(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53.RecordTarget"):
    """Type union for a record that accepts multiple types of target.

    Stability:
        stable
    """
    def __init__(self, values: typing.Optional[typing.List[str]]=None, alias_target: typing.Optional["IAliasRecordTarget"]=None) -> None:
        """
        Arguments:
            values: -
            alias_target: -

        Stability:
            stable
        """
        jsii.create(RecordTarget, self, [values, alias_target])

    @jsii.member(jsii_name="fromAlias")
    @classmethod
    def from_alias(cls, alias_target: "IAliasRecordTarget") -> "RecordTarget":
        """Use an alias as target.

        Arguments:
            alias_target: -

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "fromAlias", [alias_target])

    @jsii.member(jsii_name="fromIpAddresses")
    @classmethod
    def from_ip_addresses(cls, *ip_addresses: str) -> "RecordTarget":
        """Use ip adresses as target.

        Arguments:
            ip_addresses: -

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "fromIpAddresses", [*ip_addresses])

    @jsii.member(jsii_name="fromValues")
    @classmethod
    def from_values(cls, *values: str) -> "RecordTarget":
        """Use string values as target.

        Arguments:
            values: -

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "fromValues", [*values])

    @property
    @jsii.member(jsii_name="aliasTarget")
    def alias_target(self) -> typing.Optional["IAliasRecordTarget"]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "aliasTarget")

    @property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.Optional[typing.List[str]]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "values")


class AddressRecordTarget(RecordTarget, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53.AddressRecordTarget"):
    """
    Deprecated:
        Use RecordTarget

    Stability:
        deprecated
    """
    def __init__(self, values: typing.Optional[typing.List[str]]=None, alias_target: typing.Optional["IAliasRecordTarget"]=None) -> None:
        """
        Arguments:
            values: -
            alias_target: -

        Stability:
            stable
        """
        jsii.create(AddressRecordTarget, self, [values, alias_target])


@jsii.enum(jsii_type="@aws-cdk/aws-route53.RecordType")
class RecordType(enum.Enum):
    """The record type.

    Stability:
        stable
    """
    A = "A"
    """
    Stability:
        stable
    """
    AAAA = "AAAA"
    """
    Stability:
        stable
    """
    CAA = "CAA"
    """
    Stability:
        stable
    """
    CNAME = "CNAME"
    """
    Stability:
        stable
    """
    MX = "MX"
    """
    Stability:
        stable
    """
    NAPTR = "NAPTR"
    """
    Stability:
        stable
    """
    NS = "NS"
    """
    Stability:
        stable
    """
    PTR = "PTR"
    """
    Stability:
        stable
    """
    SOA = "SOA"
    """
    Stability:
        stable
    """
    SPF = "SPF"
    """
    Stability:
        stable
    """
    SRV = "SRV"
    """
    Stability:
        stable
    """
    TXT = "TXT"
    """
    Stability:
        stable
    """

class SrvRecord(RecordSet, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53.SrvRecord"):
    """A DNS SRV record.

    Stability:
        stable
    resource:
        AWS::Route53::RecordSet
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, values: typing.List["SrvRecordValue"], zone: "IHostedZone", comment: typing.Optional[str]=None, record_name: typing.Optional[str]=None, ttl: typing.Optional[aws_cdk.core.Duration]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            values: The values.
            zone: The hosted zone in which to define the new record.
            comment: A comment to add on the record. Default: no comment
            record_name: The domain name for this record. Default: zone root
            ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)

        Stability:
            stable
        """
        props: SrvRecordProps = {"values": values, "zone": zone}

        if comment is not None:
            props["comment"] = comment

        if record_name is not None:
            props["recordName"] = record_name

        if ttl is not None:
            props["ttl"] = ttl

        jsii.create(SrvRecord, self, [scope, id, props])


@jsii.data_type(jsii_type="@aws-cdk/aws-route53.SrvRecordProps", jsii_struct_bases=[RecordSetOptions])
class SrvRecordProps(RecordSetOptions, jsii.compat.TypedDict):
    """Construction properties for a SrvRecord.

    Stability:
        stable
    """
    values: typing.List["SrvRecordValue"]
    """The values.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-route53.SrvRecordValue", jsii_struct_bases=[])
class SrvRecordValue(jsii.compat.TypedDict):
    """Properties for a SRV record value.

    Stability:
        stable
    """
    hostName: str
    """The server host name.

    Stability:
        stable
    """

    port: jsii.Number
    """The port.

    Stability:
        stable
    """

    priority: jsii.Number
    """The priority.

    Stability:
        stable
    """

    weight: jsii.Number
    """The weight.

    Stability:
        stable
    """

class TxtRecord(RecordSet, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53.TxtRecord"):
    """A DNS TXT record.

    Stability:
        stable
    resource:
        AWS::Route53::RecordSet
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, values: typing.List[str], zone: "IHostedZone", comment: typing.Optional[str]=None, record_name: typing.Optional[str]=None, ttl: typing.Optional[aws_cdk.core.Duration]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            values: The text values.
            zone: The hosted zone in which to define the new record.
            comment: A comment to add on the record. Default: no comment
            record_name: The domain name for this record. Default: zone root
            ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)

        Stability:
            stable
        """
        props: TxtRecordProps = {"values": values, "zone": zone}

        if comment is not None:
            props["comment"] = comment

        if record_name is not None:
            props["recordName"] = record_name

        if ttl is not None:
            props["ttl"] = ttl

        jsii.create(TxtRecord, self, [scope, id, props])


@jsii.data_type(jsii_type="@aws-cdk/aws-route53.TxtRecordProps", jsii_struct_bases=[RecordSetOptions])
class TxtRecordProps(RecordSetOptions, jsii.compat.TypedDict):
    """Construction properties for a TxtRecord.

    Stability:
        stable
    """
    values: typing.List[str]
    """The text values.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-route53.ZoneDelegationOptions", jsii_struct_bases=[])
class ZoneDelegationOptions(jsii.compat.TypedDict, total=False):
    """Options available when creating a delegation relationship from one PublicHostedZone to another.

    Stability:
        stable
    """
    comment: str
    """A comment to add on the DNS record created to incorporate the delegation.

    Default:
        none

    Stability:
        stable
    """

    ttl: aws_cdk.core.Duration
    """The TTL (Time To Live) of the DNS delegation record in DNS caches.

    Default:
        172800

    Stability:
        stable
    """

class ZoneDelegationRecord(RecordSet, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53.ZoneDelegationRecord"):
    """A record to delegate further lookups to a different set of name servers.

    Stability:
        stable
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, name_servers: typing.List[str], zone: "IHostedZone", comment: typing.Optional[str]=None, record_name: typing.Optional[str]=None, ttl: typing.Optional[aws_cdk.core.Duration]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            name_servers: The name servers to report in the delegation records.
            zone: The hosted zone in which to define the new record.
            comment: A comment to add on the record. Default: no comment
            record_name: The domain name for this record. Default: zone root
            ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)

        Stability:
            stable
        """
        props: ZoneDelegationRecordProps = {"nameServers": name_servers, "zone": zone}

        if comment is not None:
            props["comment"] = comment

        if record_name is not None:
            props["recordName"] = record_name

        if ttl is not None:
            props["ttl"] = ttl

        jsii.create(ZoneDelegationRecord, self, [scope, id, props])


@jsii.data_type(jsii_type="@aws-cdk/aws-route53.ZoneDelegationRecordProps", jsii_struct_bases=[RecordSetOptions])
class ZoneDelegationRecordProps(RecordSetOptions, jsii.compat.TypedDict):
    """Construction properties for a ZoneDelegationRecord.

    Stability:
        stable
    """
    nameServers: typing.List[str]
    """The name servers to report in the delegation records.

    Stability:
        stable
    """

__all__ = ["ARecord", "ARecordProps", "AaaaRecord", "AaaaRecordProps", "AddressRecordTarget", "AliasRecordTargetConfig", "CaaAmazonRecord", "CaaAmazonRecordProps", "CaaRecord", "CaaRecordProps", "CaaRecordValue", "CaaTag", "CfnHealthCheck", "CfnHealthCheckProps", "CfnHostedZone", "CfnHostedZoneProps", "CfnRecordSet", "CfnRecordSetGroup", "CfnRecordSetGroupProps", "CfnRecordSetProps", "CnameRecord", "CnameRecordProps", "CommonHostedZoneProps", "HostedZone", "HostedZoneAttributes", "HostedZoneProps", "HostedZoneProviderProps", "IAliasRecordTarget", "IHostedZone", "IPrivateHostedZone", "IPublicHostedZone", "IRecordSet", "MxRecord", "MxRecordProps", "MxRecordValue", "PrivateHostedZone", "PrivateHostedZoneProps", "PublicHostedZone", "PublicHostedZoneProps", "RecordSet", "RecordSetOptions", "RecordSetProps", "RecordTarget", "RecordType", "SrvRecord", "SrvRecordProps", "SrvRecordValue", "TxtRecord", "TxtRecordProps", "ZoneDelegationOptions", "ZoneDelegationRecord", "ZoneDelegationRecordProps", "__jsii_assembly__"]

publication.publish()
