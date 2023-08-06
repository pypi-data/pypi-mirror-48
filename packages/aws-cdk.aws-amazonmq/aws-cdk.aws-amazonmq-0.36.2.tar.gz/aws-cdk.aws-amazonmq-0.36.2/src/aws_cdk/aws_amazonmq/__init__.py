import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-amazonmq", "0.36.2", __name__, "aws-amazonmq@0.36.2.jsii.tgz")
class CfnBroker(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-amazonmq.CfnBroker"):
    """A CloudFormation ``AWS::AmazonMQ::Broker``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html
    Stability:
        stable
    cloudformationResource:
        AWS::AmazonMQ::Broker
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, auto_minor_version_upgrade: typing.Union[bool, aws_cdk.core.IResolvable], broker_name: str, deployment_mode: str, engine_type: str, engine_version: str, host_instance_type: str, publicly_accessible: typing.Union[bool, aws_cdk.core.IResolvable], users: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "UserProperty"]]], configuration: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ConfigurationIdProperty"]]]=None, logs: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["LogListProperty"]]]=None, maintenance_window_start_time: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["MaintenanceWindowProperty"]]]=None, security_groups: typing.Optional[typing.List[str]]=None, subnet_ids: typing.Optional[typing.List[str]]=None, tags: typing.Optional[typing.List["TagsEntryProperty"]]=None) -> None:
        """Create a new ``AWS::AmazonMQ::Broker``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            auto_minor_version_upgrade: ``AWS::AmazonMQ::Broker.AutoMinorVersionUpgrade``.
            broker_name: ``AWS::AmazonMQ::Broker.BrokerName``.
            deployment_mode: ``AWS::AmazonMQ::Broker.DeploymentMode``.
            engine_type: ``AWS::AmazonMQ::Broker.EngineType``.
            engine_version: ``AWS::AmazonMQ::Broker.EngineVersion``.
            host_instance_type: ``AWS::AmazonMQ::Broker.HostInstanceType``.
            publicly_accessible: ``AWS::AmazonMQ::Broker.PubliclyAccessible``.
            users: ``AWS::AmazonMQ::Broker.Users``.
            configuration: ``AWS::AmazonMQ::Broker.Configuration``.
            logs: ``AWS::AmazonMQ::Broker.Logs``.
            maintenance_window_start_time: ``AWS::AmazonMQ::Broker.MaintenanceWindowStartTime``.
            security_groups: ``AWS::AmazonMQ::Broker.SecurityGroups``.
            subnet_ids: ``AWS::AmazonMQ::Broker.SubnetIds``.
            tags: ``AWS::AmazonMQ::Broker.Tags``.

        Stability:
            stable
        """
        props: CfnBrokerProps = {"autoMinorVersionUpgrade": auto_minor_version_upgrade, "brokerName": broker_name, "deploymentMode": deployment_mode, "engineType": engine_type, "engineVersion": engine_version, "hostInstanceType": host_instance_type, "publiclyAccessible": publicly_accessible, "users": users}

        if configuration is not None:
            props["configuration"] = configuration

        if logs is not None:
            props["logs"] = logs

        if maintenance_window_start_time is not None:
            props["maintenanceWindowStartTime"] = maintenance_window_start_time

        if security_groups is not None:
            props["securityGroups"] = security_groups

        if subnet_ids is not None:
            props["subnetIds"] = subnet_ids

        if tags is not None:
            props["tags"] = tags

        jsii.create(CfnBroker, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrAmqpEndpoints")
    def attr_amqp_endpoints(self) -> typing.List[str]:
        """
        Stability:
            stable
        cloudformationAttribute:
            AmqpEndpoints
        """
        return jsii.get(self, "attrAmqpEndpoints")

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
    @jsii.member(jsii_name="attrConfigurationId")
    def attr_configuration_id(self) -> str:
        """
        Stability:
            stable
        cloudformationAttribute:
            ConfigurationId
        """
        return jsii.get(self, "attrConfigurationId")

    @property
    @jsii.member(jsii_name="attrConfigurationRevision")
    def attr_configuration_revision(self) -> jsii.Number:
        """
        Stability:
            stable
        cloudformationAttribute:
            ConfigurationRevision
        """
        return jsii.get(self, "attrConfigurationRevision")

    @property
    @jsii.member(jsii_name="attrIpAddresses")
    def attr_ip_addresses(self) -> typing.List[str]:
        """
        Stability:
            stable
        cloudformationAttribute:
            IpAddresses
        """
        return jsii.get(self, "attrIpAddresses")

    @property
    @jsii.member(jsii_name="attrMqttEndpoints")
    def attr_mqtt_endpoints(self) -> typing.List[str]:
        """
        Stability:
            stable
        cloudformationAttribute:
            MqttEndpoints
        """
        return jsii.get(self, "attrMqttEndpoints")

    @property
    @jsii.member(jsii_name="attrOpenWireEndpoints")
    def attr_open_wire_endpoints(self) -> typing.List[str]:
        """
        Stability:
            stable
        cloudformationAttribute:
            OpenWireEndpoints
        """
        return jsii.get(self, "attrOpenWireEndpoints")

    @property
    @jsii.member(jsii_name="attrStompEndpoints")
    def attr_stomp_endpoints(self) -> typing.List[str]:
        """
        Stability:
            stable
        cloudformationAttribute:
            StompEndpoints
        """
        return jsii.get(self, "attrStompEndpoints")

    @property
    @jsii.member(jsii_name="attrWssEndpoints")
    def attr_wss_endpoints(self) -> typing.List[str]:
        """
        Stability:
            stable
        cloudformationAttribute:
            WssEndpoints
        """
        return jsii.get(self, "attrWssEndpoints")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::AmazonMQ::Broker.Tags``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-tags
        Stability:
            stable
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::AmazonMQ::Broker.AutoMinorVersionUpgrade``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-autominorversionupgrade
        Stability:
            stable
        """
        return jsii.get(self, "autoMinorVersionUpgrade")

    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(self, value: typing.Union[bool, aws_cdk.core.IResolvable]):
        return jsii.set(self, "autoMinorVersionUpgrade", value)

    @property
    @jsii.member(jsii_name="brokerName")
    def broker_name(self) -> str:
        """``AWS::AmazonMQ::Broker.BrokerName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-brokername
        Stability:
            stable
        """
        return jsii.get(self, "brokerName")

    @broker_name.setter
    def broker_name(self, value: str):
        return jsii.set(self, "brokerName", value)

    @property
    @jsii.member(jsii_name="deploymentMode")
    def deployment_mode(self) -> str:
        """``AWS::AmazonMQ::Broker.DeploymentMode``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-deploymentmode
        Stability:
            stable
        """
        return jsii.get(self, "deploymentMode")

    @deployment_mode.setter
    def deployment_mode(self, value: str):
        return jsii.set(self, "deploymentMode", value)

    @property
    @jsii.member(jsii_name="engineType")
    def engine_type(self) -> str:
        """``AWS::AmazonMQ::Broker.EngineType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-enginetype
        Stability:
            stable
        """
        return jsii.get(self, "engineType")

    @engine_type.setter
    def engine_type(self, value: str):
        return jsii.set(self, "engineType", value)

    @property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> str:
        """``AWS::AmazonMQ::Broker.EngineVersion``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-engineversion
        Stability:
            stable
        """
        return jsii.get(self, "engineVersion")

    @engine_version.setter
    def engine_version(self, value: str):
        return jsii.set(self, "engineVersion", value)

    @property
    @jsii.member(jsii_name="hostInstanceType")
    def host_instance_type(self) -> str:
        """``AWS::AmazonMQ::Broker.HostInstanceType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-hostinstancetype
        Stability:
            stable
        """
        return jsii.get(self, "hostInstanceType")

    @host_instance_type.setter
    def host_instance_type(self, value: str):
        return jsii.set(self, "hostInstanceType", value)

    @property
    @jsii.member(jsii_name="publiclyAccessible")
    def publicly_accessible(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::AmazonMQ::Broker.PubliclyAccessible``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-publiclyaccessible
        Stability:
            stable
        """
        return jsii.get(self, "publiclyAccessible")

    @publicly_accessible.setter
    def publicly_accessible(self, value: typing.Union[bool, aws_cdk.core.IResolvable]):
        return jsii.set(self, "publiclyAccessible", value)

    @property
    @jsii.member(jsii_name="users")
    def users(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "UserProperty"]]]:
        """``AWS::AmazonMQ::Broker.Users``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-users
        Stability:
            stable
        """
        return jsii.get(self, "users")

    @users.setter
    def users(self, value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "UserProperty"]]]):
        return jsii.set(self, "users", value)

    @property
    @jsii.member(jsii_name="configuration")
    def configuration(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ConfigurationIdProperty"]]]:
        """``AWS::AmazonMQ::Broker.Configuration``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-configuration
        Stability:
            stable
        """
        return jsii.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ConfigurationIdProperty"]]]):
        return jsii.set(self, "configuration", value)

    @property
    @jsii.member(jsii_name="logs")
    def logs(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["LogListProperty"]]]:
        """``AWS::AmazonMQ::Broker.Logs``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-logs
        Stability:
            stable
        """
        return jsii.get(self, "logs")

    @logs.setter
    def logs(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["LogListProperty"]]]):
        return jsii.set(self, "logs", value)

    @property
    @jsii.member(jsii_name="maintenanceWindowStartTime")
    def maintenance_window_start_time(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["MaintenanceWindowProperty"]]]:
        """``AWS::AmazonMQ::Broker.MaintenanceWindowStartTime``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-maintenancewindowstarttime
        Stability:
            stable
        """
        return jsii.get(self, "maintenanceWindowStartTime")

    @maintenance_window_start_time.setter
    def maintenance_window_start_time(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["MaintenanceWindowProperty"]]]):
        return jsii.set(self, "maintenanceWindowStartTime", value)

    @property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.Optional[typing.List[str]]:
        """``AWS::AmazonMQ::Broker.SecurityGroups``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-securitygroups
        Stability:
            stable
        """
        return jsii.get(self, "securityGroups")

    @security_groups.setter
    def security_groups(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "securityGroups", value)

    @property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.Optional[typing.List[str]]:
        """``AWS::AmazonMQ::Broker.SubnetIds``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-subnetids
        Stability:
            stable
        """
        return jsii.get(self, "subnetIds")

    @subnet_ids.setter
    def subnet_ids(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "subnetIds", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-amazonmq.CfnBroker.ConfigurationIdProperty", jsii_struct_bases=[])
    class ConfigurationIdProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-configurationid.html
        Stability:
            stable
        """
        id: str
        """``CfnBroker.ConfigurationIdProperty.Id``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-configurationid.html#cfn-amazonmq-broker-configurationid-id
        Stability:
            stable
        """

        revision: jsii.Number
        """``CfnBroker.ConfigurationIdProperty.Revision``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-configurationid.html#cfn-amazonmq-broker-configurationid-revision
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-amazonmq.CfnBroker.LogListProperty", jsii_struct_bases=[])
    class LogListProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-loglist.html
        Stability:
            stable
        """
        audit: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnBroker.LogListProperty.Audit``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-loglist.html#cfn-amazonmq-broker-loglist-audit
        Stability:
            stable
        """

        general: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnBroker.LogListProperty.General``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-loglist.html#cfn-amazonmq-broker-loglist-general
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-amazonmq.CfnBroker.MaintenanceWindowProperty", jsii_struct_bases=[])
    class MaintenanceWindowProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-maintenancewindow.html
        Stability:
            stable
        """
        dayOfWeek: str
        """``CfnBroker.MaintenanceWindowProperty.DayOfWeek``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-maintenancewindow.html#cfn-amazonmq-broker-maintenancewindow-dayofweek
        Stability:
            stable
        """

        timeOfDay: str
        """``CfnBroker.MaintenanceWindowProperty.TimeOfDay``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-maintenancewindow.html#cfn-amazonmq-broker-maintenancewindow-timeofday
        Stability:
            stable
        """

        timeZone: str
        """``CfnBroker.MaintenanceWindowProperty.TimeZone``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-maintenancewindow.html#cfn-amazonmq-broker-maintenancewindow-timezone
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-amazonmq.CfnBroker.TagsEntryProperty", jsii_struct_bases=[])
    class TagsEntryProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-tagsentry.html
        Stability:
            stable
        """
        key: str
        """``CfnBroker.TagsEntryProperty.Key``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-tagsentry.html#cfn-amazonmq-broker-tagsentry-key
        Stability:
            stable
        """

        value: str
        """``CfnBroker.TagsEntryProperty.Value``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-tagsentry.html#cfn-amazonmq-broker-tagsentry-value
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _UserProperty(jsii.compat.TypedDict, total=False):
        consoleAccess: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnBroker.UserProperty.ConsoleAccess``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-user.html#cfn-amazonmq-broker-user-consoleaccess
        Stability:
            stable
        """
        groups: typing.List[str]
        """``CfnBroker.UserProperty.Groups``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-user.html#cfn-amazonmq-broker-user-groups
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-amazonmq.CfnBroker.UserProperty", jsii_struct_bases=[_UserProperty])
    class UserProperty(_UserProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-user.html
        Stability:
            stable
        """
        password: str
        """``CfnBroker.UserProperty.Password``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-user.html#cfn-amazonmq-broker-user-password
        Stability:
            stable
        """

        username: str
        """``CfnBroker.UserProperty.Username``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-user.html#cfn-amazonmq-broker-user-username
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnBrokerProps(jsii.compat.TypedDict, total=False):
    configuration: typing.Union[aws_cdk.core.IResolvable, "CfnBroker.ConfigurationIdProperty"]
    """``AWS::AmazonMQ::Broker.Configuration``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-configuration
    Stability:
        stable
    """
    logs: typing.Union[aws_cdk.core.IResolvable, "CfnBroker.LogListProperty"]
    """``AWS::AmazonMQ::Broker.Logs``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-logs
    Stability:
        stable
    """
    maintenanceWindowStartTime: typing.Union[aws_cdk.core.IResolvable, "CfnBroker.MaintenanceWindowProperty"]
    """``AWS::AmazonMQ::Broker.MaintenanceWindowStartTime``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-maintenancewindowstarttime
    Stability:
        stable
    """
    securityGroups: typing.List[str]
    """``AWS::AmazonMQ::Broker.SecurityGroups``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-securitygroups
    Stability:
        stable
    """
    subnetIds: typing.List[str]
    """``AWS::AmazonMQ::Broker.SubnetIds``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-subnetids
    Stability:
        stable
    """
    tags: typing.List["CfnBroker.TagsEntryProperty"]
    """``AWS::AmazonMQ::Broker.Tags``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-tags
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-amazonmq.CfnBrokerProps", jsii_struct_bases=[_CfnBrokerProps])
class CfnBrokerProps(_CfnBrokerProps):
    """Properties for defining a ``AWS::AmazonMQ::Broker``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html
    Stability:
        stable
    """
    autoMinorVersionUpgrade: typing.Union[bool, aws_cdk.core.IResolvable]
    """``AWS::AmazonMQ::Broker.AutoMinorVersionUpgrade``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-autominorversionupgrade
    Stability:
        stable
    """

    brokerName: str
    """``AWS::AmazonMQ::Broker.BrokerName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-brokername
    Stability:
        stable
    """

    deploymentMode: str
    """``AWS::AmazonMQ::Broker.DeploymentMode``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-deploymentmode
    Stability:
        stable
    """

    engineType: str
    """``AWS::AmazonMQ::Broker.EngineType``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-enginetype
    Stability:
        stable
    """

    engineVersion: str
    """``AWS::AmazonMQ::Broker.EngineVersion``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-engineversion
    Stability:
        stable
    """

    hostInstanceType: str
    """``AWS::AmazonMQ::Broker.HostInstanceType``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-hostinstancetype
    Stability:
        stable
    """

    publiclyAccessible: typing.Union[bool, aws_cdk.core.IResolvable]
    """``AWS::AmazonMQ::Broker.PubliclyAccessible``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-publiclyaccessible
    Stability:
        stable
    """

    users: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnBroker.UserProperty"]]]
    """``AWS::AmazonMQ::Broker.Users``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html#cfn-amazonmq-broker-users
    Stability:
        stable
    """

class CfnConfiguration(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-amazonmq.CfnConfiguration"):
    """A CloudFormation ``AWS::AmazonMQ::Configuration``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html
    Stability:
        stable
    cloudformationResource:
        AWS::AmazonMQ::Configuration
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, data: str, engine_type: str, engine_version: str, name: str, description: typing.Optional[str]=None, tags: typing.Optional[typing.List["TagsEntryProperty"]]=None) -> None:
        """Create a new ``AWS::AmazonMQ::Configuration``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            data: ``AWS::AmazonMQ::Configuration.Data``.
            engine_type: ``AWS::AmazonMQ::Configuration.EngineType``.
            engine_version: ``AWS::AmazonMQ::Configuration.EngineVersion``.
            name: ``AWS::AmazonMQ::Configuration.Name``.
            description: ``AWS::AmazonMQ::Configuration.Description``.
            tags: ``AWS::AmazonMQ::Configuration.Tags``.

        Stability:
            stable
        """
        props: CfnConfigurationProps = {"data": data, "engineType": engine_type, "engineVersion": engine_version, "name": name}

        if description is not None:
            props["description"] = description

        if tags is not None:
            props["tags"] = tags

        jsii.create(CfnConfiguration, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrRevision")
    def attr_revision(self) -> jsii.Number:
        """
        Stability:
            stable
        cloudformationAttribute:
            Revision
        """
        return jsii.get(self, "attrRevision")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::AmazonMQ::Configuration.Tags``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-tags
        Stability:
            stable
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="data")
    def data(self) -> str:
        """``AWS::AmazonMQ::Configuration.Data``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-data
        Stability:
            stable
        """
        return jsii.get(self, "data")

    @data.setter
    def data(self, value: str):
        return jsii.set(self, "data", value)

    @property
    @jsii.member(jsii_name="engineType")
    def engine_type(self) -> str:
        """``AWS::AmazonMQ::Configuration.EngineType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-enginetype
        Stability:
            stable
        """
        return jsii.get(self, "engineType")

    @engine_type.setter
    def engine_type(self, value: str):
        return jsii.set(self, "engineType", value)

    @property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> str:
        """``AWS::AmazonMQ::Configuration.EngineVersion``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-engineversion
        Stability:
            stable
        """
        return jsii.get(self, "engineVersion")

    @engine_version.setter
    def engine_version(self, value: str):
        return jsii.set(self, "engineVersion", value)

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::AmazonMQ::Configuration.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-name
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
        """``AWS::AmazonMQ::Configuration.Description``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-description
        Stability:
            stable
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-amazonmq.CfnConfiguration.TagsEntryProperty", jsii_struct_bases=[])
    class TagsEntryProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configuration-tagsentry.html
        Stability:
            stable
        """
        key: str
        """``CfnConfiguration.TagsEntryProperty.Key``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configuration-tagsentry.html#cfn-amazonmq-configuration-tagsentry-key
        Stability:
            stable
        """

        value: str
        """``CfnConfiguration.TagsEntryProperty.Value``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configuration-tagsentry.html#cfn-amazonmq-configuration-tagsentry-value
        Stability:
            stable
        """


class CfnConfigurationAssociation(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-amazonmq.CfnConfigurationAssociation"):
    """A CloudFormation ``AWS::AmazonMQ::ConfigurationAssociation``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configurationassociation.html
    Stability:
        stable
    cloudformationResource:
        AWS::AmazonMQ::ConfigurationAssociation
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, broker: str, configuration: typing.Union[aws_cdk.core.IResolvable, "ConfigurationIdProperty"]) -> None:
        """Create a new ``AWS::AmazonMQ::ConfigurationAssociation``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            broker: ``AWS::AmazonMQ::ConfigurationAssociation.Broker``.
            configuration: ``AWS::AmazonMQ::ConfigurationAssociation.Configuration``.

        Stability:
            stable
        """
        props: CfnConfigurationAssociationProps = {"broker": broker, "configuration": configuration}

        jsii.create(CfnConfigurationAssociation, self, [scope, id, props])

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
    @jsii.member(jsii_name="broker")
    def broker(self) -> str:
        """``AWS::AmazonMQ::ConfigurationAssociation.Broker``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configurationassociation.html#cfn-amazonmq-configurationassociation-broker
        Stability:
            stable
        """
        return jsii.get(self, "broker")

    @broker.setter
    def broker(self, value: str):
        return jsii.set(self, "broker", value)

    @property
    @jsii.member(jsii_name="configuration")
    def configuration(self) -> typing.Union[aws_cdk.core.IResolvable, "ConfigurationIdProperty"]:
        """``AWS::AmazonMQ::ConfigurationAssociation.Configuration``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configurationassociation.html#cfn-amazonmq-configurationassociation-configuration
        Stability:
            stable
        """
        return jsii.get(self, "configuration")

    @configuration.setter
    def configuration(self, value: typing.Union[aws_cdk.core.IResolvable, "ConfigurationIdProperty"]):
        return jsii.set(self, "configuration", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-amazonmq.CfnConfigurationAssociation.ConfigurationIdProperty", jsii_struct_bases=[])
    class ConfigurationIdProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configurationassociation-configurationid.html
        Stability:
            stable
        """
        id: str
        """``CfnConfigurationAssociation.ConfigurationIdProperty.Id``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configurationassociation-configurationid.html#cfn-amazonmq-configurationassociation-configurationid-id
        Stability:
            stable
        """

        revision: jsii.Number
        """``CfnConfigurationAssociation.ConfigurationIdProperty.Revision``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-configurationassociation-configurationid.html#cfn-amazonmq-configurationassociation-configurationid-revision
        Stability:
            stable
        """


@jsii.data_type(jsii_type="@aws-cdk/aws-amazonmq.CfnConfigurationAssociationProps", jsii_struct_bases=[])
class CfnConfigurationAssociationProps(jsii.compat.TypedDict):
    """Properties for defining a ``AWS::AmazonMQ::ConfigurationAssociation``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configurationassociation.html
    Stability:
        stable
    """
    broker: str
    """``AWS::AmazonMQ::ConfigurationAssociation.Broker``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configurationassociation.html#cfn-amazonmq-configurationassociation-broker
    Stability:
        stable
    """

    configuration: typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationAssociation.ConfigurationIdProperty"]
    """``AWS::AmazonMQ::ConfigurationAssociation.Configuration``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configurationassociation.html#cfn-amazonmq-configurationassociation-configuration
    Stability:
        stable
    """

@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnConfigurationProps(jsii.compat.TypedDict, total=False):
    description: str
    """``AWS::AmazonMQ::Configuration.Description``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-description
    Stability:
        stable
    """
    tags: typing.List["CfnConfiguration.TagsEntryProperty"]
    """``AWS::AmazonMQ::Configuration.Tags``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-tags
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-amazonmq.CfnConfigurationProps", jsii_struct_bases=[_CfnConfigurationProps])
class CfnConfigurationProps(_CfnConfigurationProps):
    """Properties for defining a ``AWS::AmazonMQ::Configuration``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html
    Stability:
        stable
    """
    data: str
    """``AWS::AmazonMQ::Configuration.Data``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-data
    Stability:
        stable
    """

    engineType: str
    """``AWS::AmazonMQ::Configuration.EngineType``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-enginetype
    Stability:
        stable
    """

    engineVersion: str
    """``AWS::AmazonMQ::Configuration.EngineVersion``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-engineversion
    Stability:
        stable
    """

    name: str
    """``AWS::AmazonMQ::Configuration.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html#cfn-amazonmq-configuration-name
    Stability:
        stable
    """

__all__ = ["CfnBroker", "CfnBrokerProps", "CfnConfiguration", "CfnConfigurationAssociation", "CfnConfigurationAssociationProps", "CfnConfigurationProps", "__jsii_assembly__"]

publication.publish()
