import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_cloudwatch
import aws_cdk.aws_iam
import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-logs", "0.37.0", __name__, "aws-logs@0.37.0.jsii.tgz")
class CfnDestination(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-logs.CfnDestination"):
    """A CloudFormation ``AWS::Logs::Destination``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html
    Stability:
        stable
    cloudformationResource:
        AWS::Logs::Destination
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, destination_name: str, destination_policy: str, role_arn: str, target_arn: str) -> None:
        """Create a new ``AWS::Logs::Destination``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            destination_name: ``AWS::Logs::Destination.DestinationName``.
            destination_policy: ``AWS::Logs::Destination.DestinationPolicy``.
            role_arn: ``AWS::Logs::Destination.RoleArn``.
            target_arn: ``AWS::Logs::Destination.TargetArn``.

        Stability:
            stable
        """
        props: CfnDestinationProps = {"destinationName": destination_name, "destinationPolicy": destination_policy, "roleArn": role_arn, "targetArn": target_arn}

        jsii.create(CfnDestination, self, [scope, id, props])

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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="destinationName")
    def destination_name(self) -> str:
        """``AWS::Logs::Destination.DestinationName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-destinationname
        Stability:
            stable
        """
        return jsii.get(self, "destinationName")

    @destination_name.setter
    def destination_name(self, value: str):
        return jsii.set(self, "destinationName", value)

    @property
    @jsii.member(jsii_name="destinationPolicy")
    def destination_policy(self) -> str:
        """``AWS::Logs::Destination.DestinationPolicy``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-destinationpolicy
        Stability:
            stable
        """
        return jsii.get(self, "destinationPolicy")

    @destination_policy.setter
    def destination_policy(self, value: str):
        return jsii.set(self, "destinationPolicy", value)

    @property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> str:
        """``AWS::Logs::Destination.RoleArn``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-rolearn
        Stability:
            stable
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter
    def role_arn(self, value: str):
        return jsii.set(self, "roleArn", value)

    @property
    @jsii.member(jsii_name="targetArn")
    def target_arn(self) -> str:
        """``AWS::Logs::Destination.TargetArn``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-targetarn
        Stability:
            stable
        """
        return jsii.get(self, "targetArn")

    @target_arn.setter
    def target_arn(self, value: str):
        return jsii.set(self, "targetArn", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-logs.CfnDestinationProps", jsii_struct_bases=[])
class CfnDestinationProps(jsii.compat.TypedDict):
    """Properties for defining a ``AWS::Logs::Destination``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html
    Stability:
        stable
    """
    destinationName: str
    """``AWS::Logs::Destination.DestinationName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-destinationname
    Stability:
        stable
    """

    destinationPolicy: str
    """``AWS::Logs::Destination.DestinationPolicy``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-destinationpolicy
    Stability:
        stable
    """

    roleArn: str
    """``AWS::Logs::Destination.RoleArn``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-rolearn
    Stability:
        stable
    """

    targetArn: str
    """``AWS::Logs::Destination.TargetArn``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html#cfn-logs-destination-targetarn
    Stability:
        stable
    """

class CfnLogGroup(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-logs.CfnLogGroup"):
    """A CloudFormation ``AWS::Logs::LogGroup``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html
    Stability:
        stable
    cloudformationResource:
        AWS::Logs::LogGroup
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, log_group_name: typing.Optional[str]=None, retention_in_days: typing.Optional[jsii.Number]=None) -> None:
        """Create a new ``AWS::Logs::LogGroup``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            log_group_name: ``AWS::Logs::LogGroup.LogGroupName``.
            retention_in_days: ``AWS::Logs::LogGroup.RetentionInDays``.

        Stability:
            stable
        """
        props: CfnLogGroupProps = {}

        if log_group_name is not None:
            props["logGroupName"] = log_group_name

        if retention_in_days is not None:
            props["retentionInDays"] = retention_in_days

        jsii.create(CfnLogGroup, self, [scope, id, props])

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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> typing.Optional[str]:
        """``AWS::Logs::LogGroup.LogGroupName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-cwl-loggroup-loggroupname
        Stability:
            stable
        """
        return jsii.get(self, "logGroupName")

    @log_group_name.setter
    def log_group_name(self, value: typing.Optional[str]):
        return jsii.set(self, "logGroupName", value)

    @property
    @jsii.member(jsii_name="retentionInDays")
    def retention_in_days(self) -> typing.Optional[jsii.Number]:
        """``AWS::Logs::LogGroup.RetentionInDays``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-cwl-loggroup-retentionindays
        Stability:
            stable
        """
        return jsii.get(self, "retentionInDays")

    @retention_in_days.setter
    def retention_in_days(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "retentionInDays", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-logs.CfnLogGroupProps", jsii_struct_bases=[])
class CfnLogGroupProps(jsii.compat.TypedDict, total=False):
    """Properties for defining a ``AWS::Logs::LogGroup``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html
    Stability:
        stable
    """
    logGroupName: str
    """``AWS::Logs::LogGroup.LogGroupName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-cwl-loggroup-loggroupname
    Stability:
        stable
    """

    retentionInDays: jsii.Number
    """``AWS::Logs::LogGroup.RetentionInDays``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-cwl-loggroup-retentionindays
    Stability:
        stable
    """

class CfnLogStream(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-logs.CfnLogStream"):
    """A CloudFormation ``AWS::Logs::LogStream``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html
    Stability:
        stable
    cloudformationResource:
        AWS::Logs::LogStream
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, log_group_name: str, log_stream_name: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::Logs::LogStream``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            log_group_name: ``AWS::Logs::LogStream.LogGroupName``.
            log_stream_name: ``AWS::Logs::LogStream.LogStreamName``.

        Stability:
            stable
        """
        props: CfnLogStreamProps = {"logGroupName": log_group_name}

        if log_stream_name is not None:
            props["logStreamName"] = log_stream_name

        jsii.create(CfnLogStream, self, [scope, id, props])

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
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> str:
        """``AWS::Logs::LogStream.LogGroupName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html#cfn-logs-logstream-loggroupname
        Stability:
            stable
        """
        return jsii.get(self, "logGroupName")

    @log_group_name.setter
    def log_group_name(self, value: str):
        return jsii.set(self, "logGroupName", value)

    @property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> typing.Optional[str]:
        """``AWS::Logs::LogStream.LogStreamName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html#cfn-logs-logstream-logstreamname
        Stability:
            stable
        """
        return jsii.get(self, "logStreamName")

    @log_stream_name.setter
    def log_stream_name(self, value: typing.Optional[str]):
        return jsii.set(self, "logStreamName", value)


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnLogStreamProps(jsii.compat.TypedDict, total=False):
    logStreamName: str
    """``AWS::Logs::LogStream.LogStreamName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html#cfn-logs-logstream-logstreamname
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-logs.CfnLogStreamProps", jsii_struct_bases=[_CfnLogStreamProps])
class CfnLogStreamProps(_CfnLogStreamProps):
    """Properties for defining a ``AWS::Logs::LogStream``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html
    Stability:
        stable
    """
    logGroupName: str
    """``AWS::Logs::LogStream.LogGroupName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html#cfn-logs-logstream-loggroupname
    Stability:
        stable
    """

class CfnMetricFilter(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-logs.CfnMetricFilter"):
    """A CloudFormation ``AWS::Logs::MetricFilter``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html
    Stability:
        stable
    cloudformationResource:
        AWS::Logs::MetricFilter
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, filter_pattern: str, log_group_name: str, metric_transformations: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["MetricTransformationProperty", aws_cdk.core.IResolvable]]]) -> None:
        """Create a new ``AWS::Logs::MetricFilter``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            filter_pattern: ``AWS::Logs::MetricFilter.FilterPattern``.
            log_group_name: ``AWS::Logs::MetricFilter.LogGroupName``.
            metric_transformations: ``AWS::Logs::MetricFilter.MetricTransformations``.

        Stability:
            stable
        """
        props: CfnMetricFilterProps = {"filterPattern": filter_pattern, "logGroupName": log_group_name, "metricTransformations": metric_transformations}

        jsii.create(CfnMetricFilter, self, [scope, id, props])

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
    @jsii.member(jsii_name="filterPattern")
    def filter_pattern(self) -> str:
        """``AWS::Logs::MetricFilter.FilterPattern``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html#cfn-cwl-metricfilter-filterpattern
        Stability:
            stable
        """
        return jsii.get(self, "filterPattern")

    @filter_pattern.setter
    def filter_pattern(self, value: str):
        return jsii.set(self, "filterPattern", value)

    @property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> str:
        """``AWS::Logs::MetricFilter.LogGroupName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html#cfn-cwl-metricfilter-loggroupname
        Stability:
            stable
        """
        return jsii.get(self, "logGroupName")

    @log_group_name.setter
    def log_group_name(self, value: str):
        return jsii.set(self, "logGroupName", value)

    @property
    @jsii.member(jsii_name="metricTransformations")
    def metric_transformations(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["MetricTransformationProperty", aws_cdk.core.IResolvable]]]:
        """``AWS::Logs::MetricFilter.MetricTransformations``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html#cfn-cwl-metricfilter-metrictransformations
        Stability:
            stable
        """
        return jsii.get(self, "metricTransformations")

    @metric_transformations.setter
    def metric_transformations(self, value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["MetricTransformationProperty", aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "metricTransformations", value)

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _MetricTransformationProperty(jsii.compat.TypedDict, total=False):
        defaultValue: jsii.Number
        """``CfnMetricFilter.MetricTransformationProperty.DefaultValue``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-cwl-metricfilter-metrictransformation-defaultvalue
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-logs.CfnMetricFilter.MetricTransformationProperty", jsii_struct_bases=[_MetricTransformationProperty])
    class MetricTransformationProperty(_MetricTransformationProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html
        Stability:
            stable
        """
        metricName: str
        """``CfnMetricFilter.MetricTransformationProperty.MetricName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-cwl-metricfilter-metrictransformation-metricname
        Stability:
            stable
        """

        metricNamespace: str
        """``CfnMetricFilter.MetricTransformationProperty.MetricNamespace``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-cwl-metricfilter-metrictransformation-metricnamespace
        Stability:
            stable
        """

        metricValue: str
        """``CfnMetricFilter.MetricTransformationProperty.MetricValue``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-logs-metricfilter-metrictransformation.html#cfn-cwl-metricfilter-metrictransformation-metricvalue
        Stability:
            stable
        """


@jsii.data_type(jsii_type="@aws-cdk/aws-logs.CfnMetricFilterProps", jsii_struct_bases=[])
class CfnMetricFilterProps(jsii.compat.TypedDict):
    """Properties for defining a ``AWS::Logs::MetricFilter``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html
    Stability:
        stable
    """
    filterPattern: str
    """``AWS::Logs::MetricFilter.FilterPattern``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html#cfn-cwl-metricfilter-filterpattern
    Stability:
        stable
    """

    logGroupName: str
    """``AWS::Logs::MetricFilter.LogGroupName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html#cfn-cwl-metricfilter-loggroupname
    Stability:
        stable
    """

    metricTransformations: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnMetricFilter.MetricTransformationProperty", aws_cdk.core.IResolvable]]]
    """``AWS::Logs::MetricFilter.MetricTransformations``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html#cfn-cwl-metricfilter-metrictransformations
    Stability:
        stable
    """

class CfnSubscriptionFilter(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-logs.CfnSubscriptionFilter"):
    """A CloudFormation ``AWS::Logs::SubscriptionFilter``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html
    Stability:
        stable
    cloudformationResource:
        AWS::Logs::SubscriptionFilter
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, destination_arn: str, filter_pattern: str, log_group_name: str, role_arn: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::Logs::SubscriptionFilter``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            destination_arn: ``AWS::Logs::SubscriptionFilter.DestinationArn``.
            filter_pattern: ``AWS::Logs::SubscriptionFilter.FilterPattern``.
            log_group_name: ``AWS::Logs::SubscriptionFilter.LogGroupName``.
            role_arn: ``AWS::Logs::SubscriptionFilter.RoleArn``.

        Stability:
            stable
        """
        props: CfnSubscriptionFilterProps = {"destinationArn": destination_arn, "filterPattern": filter_pattern, "logGroupName": log_group_name}

        if role_arn is not None:
            props["roleArn"] = role_arn

        jsii.create(CfnSubscriptionFilter, self, [scope, id, props])

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
    @jsii.member(jsii_name="destinationArn")
    def destination_arn(self) -> str:
        """``AWS::Logs::SubscriptionFilter.DestinationArn``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-cwl-subscriptionfilter-destinationarn
        Stability:
            stable
        """
        return jsii.get(self, "destinationArn")

    @destination_arn.setter
    def destination_arn(self, value: str):
        return jsii.set(self, "destinationArn", value)

    @property
    @jsii.member(jsii_name="filterPattern")
    def filter_pattern(self) -> str:
        """``AWS::Logs::SubscriptionFilter.FilterPattern``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-cwl-subscriptionfilter-filterpattern
        Stability:
            stable
        """
        return jsii.get(self, "filterPattern")

    @filter_pattern.setter
    def filter_pattern(self, value: str):
        return jsii.set(self, "filterPattern", value)

    @property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> str:
        """``AWS::Logs::SubscriptionFilter.LogGroupName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-cwl-subscriptionfilter-loggroupname
        Stability:
            stable
        """
        return jsii.get(self, "logGroupName")

    @log_group_name.setter
    def log_group_name(self, value: str):
        return jsii.set(self, "logGroupName", value)

    @property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[str]:
        """``AWS::Logs::SubscriptionFilter.RoleArn``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-cwl-subscriptionfilter-rolearn
        Stability:
            stable
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter
    def role_arn(self, value: typing.Optional[str]):
        return jsii.set(self, "roleArn", value)


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnSubscriptionFilterProps(jsii.compat.TypedDict, total=False):
    roleArn: str
    """``AWS::Logs::SubscriptionFilter.RoleArn``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-cwl-subscriptionfilter-rolearn
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-logs.CfnSubscriptionFilterProps", jsii_struct_bases=[_CfnSubscriptionFilterProps])
class CfnSubscriptionFilterProps(_CfnSubscriptionFilterProps):
    """Properties for defining a ``AWS::Logs::SubscriptionFilter``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html
    Stability:
        stable
    """
    destinationArn: str
    """``AWS::Logs::SubscriptionFilter.DestinationArn``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-cwl-subscriptionfilter-destinationarn
    Stability:
        stable
    """

    filterPattern: str
    """``AWS::Logs::SubscriptionFilter.FilterPattern``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-cwl-subscriptionfilter-filterpattern
    Stability:
        stable
    """

    logGroupName: str
    """``AWS::Logs::SubscriptionFilter.LogGroupName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html#cfn-cwl-subscriptionfilter-loggroupname
    Stability:
        stable
    """

@jsii.data_type_optionals(jsii_struct_bases=[])
class _ColumnRestriction(jsii.compat.TypedDict, total=False):
    numberValue: jsii.Number
    """Number value to compare to.

    Exactly one of 'stringValue' and 'numberValue' must be set.

    Stability:
        stable
    """
    stringValue: str
    """String value to compare to.

    Exactly one of 'stringValue' and 'numberValue' must be set.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-logs.ColumnRestriction", jsii_struct_bases=[_ColumnRestriction])
class ColumnRestriction(_ColumnRestriction):
    """
    Stability:
        stable
    """
    comparison: str
    """Comparison operator to use.

    Stability:
        stable
    """

@jsii.data_type_optionals(jsii_struct_bases=[])
class _CrossAccountDestinationProps(jsii.compat.TypedDict, total=False):
    destinationName: str
    """The name of the log destination.

    Default:
        Automatically generated

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-logs.CrossAccountDestinationProps", jsii_struct_bases=[_CrossAccountDestinationProps])
class CrossAccountDestinationProps(_CrossAccountDestinationProps):
    """Properties for a CrossAccountDestination.

    Stability:
        stable
    """
    role: aws_cdk.aws_iam.IRole
    """The role to assume that grants permissions to write to 'target'.

    The role must be assumable by 'logs.{REGION}.amazonaws.com'.

    Stability:
        stable
    """

    targetArn: str
    """The log destination target's ARN.

    Stability:
        stable
    """

class FilterPattern(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-logs.FilterPattern"):
    """A collection of static methods to generate appropriate ILogPatterns.

    Stability:
        stable
    """
    def __init__(self) -> None:
        jsii.create(FilterPattern, self, [])

    @jsii.member(jsii_name="all")
    @classmethod
    def all(cls, *patterns: "JsonPattern") -> "JsonPattern":
        """A JSON log pattern that matches if all given JSON log patterns match.

        Arguments:
            patterns: -

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "all", [*patterns])

    @jsii.member(jsii_name="allEvents")
    @classmethod
    def all_events(cls) -> "IFilterPattern":
        """A log pattern that matches all events.

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "allEvents", [])

    @jsii.member(jsii_name="allTerms")
    @classmethod
    def all_terms(cls, *terms: str) -> "IFilterPattern":
        """A log pattern that matches if all the strings given appear in the event.

        Arguments:
            terms: The words to search for. All terms must match.

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "allTerms", [*terms])

    @jsii.member(jsii_name="any")
    @classmethod
    def any(cls, *patterns: "JsonPattern") -> "JsonPattern":
        """A JSON log pattern that matches if any of the given JSON log patterns match.

        Arguments:
            patterns: -

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "any", [*patterns])

    @jsii.member(jsii_name="anyTerm")
    @classmethod
    def any_term(cls, *terms: str) -> "IFilterPattern":
        """A log pattern that matches if any of the strings given appear in the event.

        Arguments:
            terms: The words to search for. Any terms must match.

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "anyTerm", [*terms])

    @jsii.member(jsii_name="anyTermGroup")
    @classmethod
    def any_term_group(cls, *term_groups: typing.List[str]) -> "IFilterPattern":
        """A log pattern that matches if any of the given term groups matches the event.

        A term group matches an event if all the terms in it appear in the event string.

        Arguments:
            term_groups: A list of term groups to search for. Any one of the clauses must match.

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "anyTermGroup", [*term_groups])

    @jsii.member(jsii_name="booleanValue")
    @classmethod
    def boolean_value(cls, json_field: str, value: bool) -> "JsonPattern":
        """A JSON log pattern that matches if the field exists and equals the boolean value.

        Arguments:
            json_field: Field inside JSON. Example: "$.myField"
            value: The value to match.

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "booleanValue", [json_field, value])

    @jsii.member(jsii_name="exists")
    @classmethod
    def exists(cls, json_field: str) -> "JsonPattern":
        """A JSON log patter that matches if the field exists.

        This is a readable convenience wrapper over 'field = *'

        Arguments:
            json_field: Field inside JSON. Example: "$.myField"

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "exists", [json_field])

    @jsii.member(jsii_name="isNull")
    @classmethod
    def is_null(cls, json_field: str) -> "JsonPattern":
        """A JSON log pattern that matches if the field exists and has the special value 'null'.

        Arguments:
            json_field: Field inside JSON. Example: "$.myField"

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "isNull", [json_field])

    @jsii.member(jsii_name="literal")
    @classmethod
    def literal(cls, log_pattern_string: str) -> "IFilterPattern":
        """Use the given string as log pattern.

        See https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html
        for information on writing log patterns.

        Arguments:
            log_pattern_string: The pattern string to use.

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "literal", [log_pattern_string])

    @jsii.member(jsii_name="notExists")
    @classmethod
    def not_exists(cls, json_field: str) -> "JsonPattern":
        """A JSON log pattern that matches if the field does not exist.

        Arguments:
            json_field: Field inside JSON. Example: "$.myField"

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "notExists", [json_field])

    @jsii.member(jsii_name="numberValue")
    @classmethod
    def number_value(cls, json_field: str, comparison: str, value: jsii.Number) -> "JsonPattern":
        """A JSON log pattern that compares numerical values.

        This pattern only matches if the event is a JSON event, and the indicated field inside
        compares with the value in the indicated way.

        Use '$' to indicate the root of the JSON structure. The comparison operator can only
        compare equality or inequality. The '*' wildcard may appear in the value may at the
        start or at the end.

        For more information, see:

        https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html

        Arguments:
            json_field: Field inside JSON. Example: "$.myField"
            comparison: Comparison to carry out. One of =, !=, <, <=, >, >=.
            value: The numerical value to compare to.

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "numberValue", [json_field, comparison, value])

    @jsii.member(jsii_name="spaceDelimited")
    @classmethod
    def space_delimited(cls, *columns: str) -> "SpaceDelimitedTextPattern":
        """A space delimited log pattern matcher.

        The log event is divided into space-delimited columns (optionally
        enclosed by "" or [] to capture spaces into column values), and names
        are given to each column.

        '...' may be specified once to match any number of columns.

        Afterwards, conditions may be added to individual columns.

        Arguments:
            columns: The columns in the space-delimited log stream.

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "spaceDelimited", [*columns])

    @jsii.member(jsii_name="stringValue")
    @classmethod
    def string_value(cls, json_field: str, comparison: str, value: str) -> "JsonPattern":
        """A JSON log pattern that compares string values.

        This pattern only matches if the event is a JSON event, and the indicated field inside
        compares with the string value.

        Use '$' to indicate the root of the JSON structure. The comparison operator can only
        compare equality or inequality. The '*' wildcard may appear in the value may at the
        start or at the end.

        For more information, see:

        https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html

        Arguments:
            json_field: Field inside JSON. Example: "$.myField"
            comparison: Comparison to carry out. Either = or !=.
            value: The string value to compare to. May use '*' as wildcard at start or end of string.

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "stringValue", [json_field, comparison, value])


@jsii.interface(jsii_type="@aws-cdk/aws-logs.IFilterPattern")
class IFilterPattern(jsii.compat.Protocol):
    """Interface for objects that can render themselves to log patterns.

    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IFilterPatternProxy

    @property
    @jsii.member(jsii_name="logPatternString")
    def log_pattern_string(self) -> str:
        """
        Stability:
            stable
        """
        ...


class _IFilterPatternProxy():
    """Interface for objects that can render themselves to log patterns.

    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-logs.IFilterPattern"
    @property
    @jsii.member(jsii_name="logPatternString")
    def log_pattern_string(self) -> str:
        """
        Stability:
            stable
        """
        return jsii.get(self, "logPatternString")


@jsii.interface(jsii_type="@aws-cdk/aws-logs.ILogGroup")
class ILogGroup(aws_cdk.core.IResource, jsii.compat.Protocol):
    """
    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _ILogGroupProxy

    @property
    @jsii.member(jsii_name="logGroupArn")
    def log_group_arn(self) -> str:
        """The ARN of this log group.

        Stability:
            stable
        attribute:
            true
        """
        ...

    @property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> str:
        """The name of this log group.

        Stability:
            stable
        attribute:
            true
        """
        ...

    @jsii.member(jsii_name="addMetricFilter")
    def add_metric_filter(self, id: str, *, filter_pattern: "IFilterPattern", metric_name: str, metric_namespace: str, default_value: typing.Optional[jsii.Number]=None, metric_value: typing.Optional[str]=None) -> "MetricFilter":
        """Create a new Metric Filter on this Log Group.

        Arguments:
            id: Unique identifier for the construct in its parent.
            props: Properties for creating the MetricFilter.
            filter_pattern: Pattern to search for log events.
            metric_name: The name of the metric to emit.
            metric_namespace: The namespace of the metric to emit.
            default_value: The value to emit if the pattern does not match a particular event. Default: No metric emitted.
            metric_value: The value to emit for the metric. Can either be a literal number (typically "1"), or the name of a field in the structure to take the value from the matched event. If you are using a field value, the field value must have been matched using the pattern. If you want to specify a field from a matched JSON structure, use '$.fieldName', and make sure the field is in the pattern (if only as '$.fieldName = *'). If you want to specify a field from a matched space-delimited structure, use '$fieldName'. Default: "1"

        Stability:
            stable
        """
        ...

    @jsii.member(jsii_name="addStream")
    def add_stream(self, id: str, *, log_stream_name: typing.Optional[str]=None) -> "LogStream":
        """Create a new Log Stream for this Log Group.

        Arguments:
            id: Unique identifier for the construct in its parent.
            props: Properties for creating the LogStream.
            log_stream_name: The name of the log stream to create. The name must be unique within the log group. Default: Automatically generated

        Stability:
            stable
        """
        ...

    @jsii.member(jsii_name="addSubscriptionFilter")
    def add_subscription_filter(self, id: str, *, destination: "ILogSubscriptionDestination", filter_pattern: "IFilterPattern") -> "SubscriptionFilter":
        """Create a new Subscription Filter on this Log Group.

        Arguments:
            id: Unique identifier for the construct in its parent.
            props: Properties for creating the SubscriptionFilter.
            destination: The destination to send the filtered events to. For example, a Kinesis stream or a Lambda function.
            filter_pattern: Log events matching this pattern will be sent to the destination.

        Stability:
            stable
        """
        ...

    @jsii.member(jsii_name="extractMetric")
    def extract_metric(self, json_field: str, metric_namespace: str, metric_name: str) -> aws_cdk.aws_cloudwatch.Metric:
        """Extract a metric from structured log events in the LogGroup.

        Creates a MetricFilter on this LogGroup that will extract the value
        of the indicated JSON field in all records where it occurs.

        The metric will be available in CloudWatch Metrics under the
        indicated namespace and name.

        Arguments:
            json_field: JSON field to extract (example: '$.myfield').
            metric_namespace: Namespace to emit the metric under.
            metric_name: Name to emit the metric under.

        Returns:
            A Metric object representing the extracted metric

        Stability:
            stable
        """
        ...

    @jsii.member(jsii_name="grant")
    def grant(self, grantee: aws_cdk.aws_iam.IGrantable, *actions: str) -> aws_cdk.aws_iam.Grant:
        """Give the indicated permissions on this log group and all streams.

        Arguments:
            grantee: -
            actions: -

        Stability:
            stable
        """
        ...

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Give permissions to write to create and write to streams in this log group.

        Arguments:
            grantee: -

        Stability:
            stable
        """
        ...


class _ILogGroupProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """
    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-logs.ILogGroup"
    @property
    @jsii.member(jsii_name="logGroupArn")
    def log_group_arn(self) -> str:
        """The ARN of this log group.

        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "logGroupArn")

    @property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> str:
        """The name of this log group.

        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "logGroupName")

    @jsii.member(jsii_name="addMetricFilter")
    def add_metric_filter(self, id: str, *, filter_pattern: "IFilterPattern", metric_name: str, metric_namespace: str, default_value: typing.Optional[jsii.Number]=None, metric_value: typing.Optional[str]=None) -> "MetricFilter":
        """Create a new Metric Filter on this Log Group.

        Arguments:
            id: Unique identifier for the construct in its parent.
            props: Properties for creating the MetricFilter.
            filter_pattern: Pattern to search for log events.
            metric_name: The name of the metric to emit.
            metric_namespace: The namespace of the metric to emit.
            default_value: The value to emit if the pattern does not match a particular event. Default: No metric emitted.
            metric_value: The value to emit for the metric. Can either be a literal number (typically "1"), or the name of a field in the structure to take the value from the matched event. If you are using a field value, the field value must have been matched using the pattern. If you want to specify a field from a matched JSON structure, use '$.fieldName', and make sure the field is in the pattern (if only as '$.fieldName = *'). If you want to specify a field from a matched space-delimited structure, use '$fieldName'. Default: "1"

        Stability:
            stable
        """
        props: MetricFilterOptions = {"filterPattern": filter_pattern, "metricName": metric_name, "metricNamespace": metric_namespace}

        if default_value is not None:
            props["defaultValue"] = default_value

        if metric_value is not None:
            props["metricValue"] = metric_value

        return jsii.invoke(self, "addMetricFilter", [id, props])

    @jsii.member(jsii_name="addStream")
    def add_stream(self, id: str, *, log_stream_name: typing.Optional[str]=None) -> "LogStream":
        """Create a new Log Stream for this Log Group.

        Arguments:
            id: Unique identifier for the construct in its parent.
            props: Properties for creating the LogStream.
            log_stream_name: The name of the log stream to create. The name must be unique within the log group. Default: Automatically generated

        Stability:
            stable
        """
        props: StreamOptions = {}

        if log_stream_name is not None:
            props["logStreamName"] = log_stream_name

        return jsii.invoke(self, "addStream", [id, props])

    @jsii.member(jsii_name="addSubscriptionFilter")
    def add_subscription_filter(self, id: str, *, destination: "ILogSubscriptionDestination", filter_pattern: "IFilterPattern") -> "SubscriptionFilter":
        """Create a new Subscription Filter on this Log Group.

        Arguments:
            id: Unique identifier for the construct in its parent.
            props: Properties for creating the SubscriptionFilter.
            destination: The destination to send the filtered events to. For example, a Kinesis stream or a Lambda function.
            filter_pattern: Log events matching this pattern will be sent to the destination.

        Stability:
            stable
        """
        props: SubscriptionFilterOptions = {"destination": destination, "filterPattern": filter_pattern}

        return jsii.invoke(self, "addSubscriptionFilter", [id, props])

    @jsii.member(jsii_name="extractMetric")
    def extract_metric(self, json_field: str, metric_namespace: str, metric_name: str) -> aws_cdk.aws_cloudwatch.Metric:
        """Extract a metric from structured log events in the LogGroup.

        Creates a MetricFilter on this LogGroup that will extract the value
        of the indicated JSON field in all records where it occurs.

        The metric will be available in CloudWatch Metrics under the
        indicated namespace and name.

        Arguments:
            json_field: JSON field to extract (example: '$.myfield').
            metric_namespace: Namespace to emit the metric under.
            metric_name: Name to emit the metric under.

        Returns:
            A Metric object representing the extracted metric

        Stability:
            stable
        """
        return jsii.invoke(self, "extractMetric", [json_field, metric_namespace, metric_name])

    @jsii.member(jsii_name="grant")
    def grant(self, grantee: aws_cdk.aws_iam.IGrantable, *actions: str) -> aws_cdk.aws_iam.Grant:
        """Give the indicated permissions on this log group and all streams.

        Arguments:
            grantee: -
            actions: -

        Stability:
            stable
        """
        return jsii.invoke(self, "grant", [grantee, *actions])

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Give permissions to write to create and write to streams in this log group.

        Arguments:
            grantee: -

        Stability:
            stable
        """
        return jsii.invoke(self, "grantWrite", [grantee])


@jsii.interface(jsii_type="@aws-cdk/aws-logs.ILogStream")
class ILogStream(aws_cdk.core.IResource, jsii.compat.Protocol):
    """
    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _ILogStreamProxy

    @property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> str:
        """The name of this log stream.

        Stability:
            stable
        attribute:
            true
        """
        ...


class _ILogStreamProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """
    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-logs.ILogStream"
    @property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> str:
        """The name of this log stream.

        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "logStreamName")


@jsii.interface(jsii_type="@aws-cdk/aws-logs.ILogSubscriptionDestination")
class ILogSubscriptionDestination(jsii.compat.Protocol):
    """Interface for classes that can be the destination of a log Subscription.

    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _ILogSubscriptionDestinationProxy

    @jsii.member(jsii_name="bind")
    def bind(self, scope: aws_cdk.core.Construct, source_log_group: "ILogGroup") -> "LogSubscriptionDestinationConfig":
        """Return the properties required to send subscription events to this destination.

        If necessary, the destination can use the properties of the SubscriptionFilter
        object itself to configure its permissions to allow the subscription to write
        to it.

        The destination may reconfigure its own permissions in response to this
        function call.

        Arguments:
            scope: -
            source_log_group: -

        Stability:
            stable
        """
        ...


class _ILogSubscriptionDestinationProxy():
    """Interface for classes that can be the destination of a log Subscription.

    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-logs.ILogSubscriptionDestination"
    @jsii.member(jsii_name="bind")
    def bind(self, scope: aws_cdk.core.Construct, source_log_group: "ILogGroup") -> "LogSubscriptionDestinationConfig":
        """Return the properties required to send subscription events to this destination.

        If necessary, the destination can use the properties of the SubscriptionFilter
        object itself to configure its permissions to allow the subscription to write
        to it.

        The destination may reconfigure its own permissions in response to this
        function call.

        Arguments:
            scope: -
            source_log_group: -

        Stability:
            stable
        """
        return jsii.invoke(self, "bind", [scope, source_log_group])


@jsii.implements(ILogSubscriptionDestination)
class CrossAccountDestination(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-logs.CrossAccountDestination"):
    """A new CloudWatch Logs Destination for use in cross-account scenarios.

    CrossAccountDestinations are used to subscribe a Kinesis stream in a
    different account to a CloudWatch Subscription.

    Consumers will hardly ever need to use this class. Instead, directly
    subscribe a Kinesis stream using the integration class in the
    ``@aws-cdk/aws-logs-destinations`` package; if necessary, a
    ``CrossAccountDestination`` will be created automatically.

    Stability:
        stable
    resource:
        AWS::Logs::Destination
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, role: aws_cdk.aws_iam.IRole, target_arn: str, destination_name: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            role: The role to assume that grants permissions to write to 'target'. The role must be assumable by 'logs.{REGION}.amazonaws.com'.
            target_arn: The log destination target's ARN.
            destination_name: The name of the log destination. Default: Automatically generated

        Stability:
            stable
        """
        props: CrossAccountDestinationProps = {"role": role, "targetArn": target_arn}

        if destination_name is not None:
            props["destinationName"] = destination_name

        jsii.create(CrossAccountDestination, self, [scope, id, props])

    @jsii.member(jsii_name="addToPolicy")
    def add_to_policy(self, statement: aws_cdk.aws_iam.PolicyStatement) -> None:
        """
        Arguments:
            statement: -

        Stability:
            stable
        """
        return jsii.invoke(self, "addToPolicy", [statement])

    @jsii.member(jsii_name="bind")
    def bind(self, _scope: aws_cdk.core.Construct, _source_log_group: "ILogGroup") -> "LogSubscriptionDestinationConfig":
        """Return the properties required to send subscription events to this destination.

        If necessary, the destination can use the properties of the SubscriptionFilter
        object itself to configure its permissions to allow the subscription to write
        to it.

        The destination may reconfigure its own permissions in response to this
        function call.

        Arguments:
            _scope: -
            _source_log_group: -

        Stability:
            stable
        """
        return jsii.invoke(self, "bind", [_scope, _source_log_group])

    @property
    @jsii.member(jsii_name="destinationArn")
    def destination_arn(self) -> str:
        """The ARN of this CrossAccountDestination object.

        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "destinationArn")

    @property
    @jsii.member(jsii_name="destinationName")
    def destination_name(self) -> str:
        """The name of this CrossAccountDestination object.

        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "destinationName")

    @property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> aws_cdk.aws_iam.PolicyDocument:
        """Policy object of this CrossAccountDestination object.

        Stability:
            stable
        """
        return jsii.get(self, "policyDocument")


@jsii.implements(IFilterPattern)
class JsonPattern(metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-logs.JsonPattern"):
    """Base class for patterns that only match JSON log events.

    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _JsonPatternProxy

    def __init__(self, json_pattern_string: str) -> None:
        """
        Arguments:
            json_pattern_string: -

        Stability:
            stable
        """
        jsii.create(JsonPattern, self, [json_pattern_string])

    @property
    @jsii.member(jsii_name="jsonPatternString")
    def json_pattern_string(self) -> str:
        """
        Stability:
            stable
        """
        return jsii.get(self, "jsonPatternString")

    @property
    @jsii.member(jsii_name="logPatternString")
    def log_pattern_string(self) -> str:
        """
        Stability:
            stable
        """
        return jsii.get(self, "logPatternString")


class _JsonPatternProxy(JsonPattern):
    pass

@jsii.implements(ILogGroup)
class LogGroup(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-logs.LogGroup"):
    """Define a CloudWatch Log Group.

    Stability:
        stable
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, log_group_name: typing.Optional[str]=None, removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy]=None, retention: typing.Optional["RetentionDays"]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            log_group_name: Name of the log group. Default: Automatically generated
            removal_policy: Determine the removal policy of this log group. Normally you want to retain the log group so you can diagnose issues from logs even after a deployment that no longer includes the log group. In that case, use the normal date-based retention policy to age out your logs. Default: RemovalPolicy.Retain
            retention: How long, in days, the log contents will be retained. To retain all logs, set this value to Infinity. Default: RetentionDays.TwoYears

        Stability:
            stable
        """
        props: LogGroupProps = {}

        if log_group_name is not None:
            props["logGroupName"] = log_group_name

        if removal_policy is not None:
            props["removalPolicy"] = removal_policy

        if retention is not None:
            props["retention"] = retention

        jsii.create(LogGroup, self, [scope, id, props])

    @jsii.member(jsii_name="fromLogGroupArn")
    @classmethod
    def from_log_group_arn(cls, scope: aws_cdk.core.Construct, id: str, log_group_arn: str) -> "ILogGroup":
        """Import an existing LogGroup.

        Arguments:
            scope: -
            id: -
            log_group_arn: -

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "fromLogGroupArn", [scope, id, log_group_arn])

    @jsii.member(jsii_name="addMetricFilter")
    def add_metric_filter(self, id: str, *, filter_pattern: "IFilterPattern", metric_name: str, metric_namespace: str, default_value: typing.Optional[jsii.Number]=None, metric_value: typing.Optional[str]=None) -> "MetricFilter":
        """Create a new Metric Filter on this Log Group.

        Arguments:
            id: Unique identifier for the construct in its parent.
            props: Properties for creating the MetricFilter.
            filter_pattern: Pattern to search for log events.
            metric_name: The name of the metric to emit.
            metric_namespace: The namespace of the metric to emit.
            default_value: The value to emit if the pattern does not match a particular event. Default: No metric emitted.
            metric_value: The value to emit for the metric. Can either be a literal number (typically "1"), or the name of a field in the structure to take the value from the matched event. If you are using a field value, the field value must have been matched using the pattern. If you want to specify a field from a matched JSON structure, use '$.fieldName', and make sure the field is in the pattern (if only as '$.fieldName = *'). If you want to specify a field from a matched space-delimited structure, use '$fieldName'. Default: "1"

        Stability:
            stable
        """
        props: MetricFilterOptions = {"filterPattern": filter_pattern, "metricName": metric_name, "metricNamespace": metric_namespace}

        if default_value is not None:
            props["defaultValue"] = default_value

        if metric_value is not None:
            props["metricValue"] = metric_value

        return jsii.invoke(self, "addMetricFilter", [id, props])

    @jsii.member(jsii_name="addStream")
    def add_stream(self, id: str, *, log_stream_name: typing.Optional[str]=None) -> "LogStream":
        """Create a new Log Stream for this Log Group.

        Arguments:
            id: Unique identifier for the construct in its parent.
            props: Properties for creating the LogStream.
            log_stream_name: The name of the log stream to create. The name must be unique within the log group. Default: Automatically generated

        Stability:
            stable
        """
        props: StreamOptions = {}

        if log_stream_name is not None:
            props["logStreamName"] = log_stream_name

        return jsii.invoke(self, "addStream", [id, props])

    @jsii.member(jsii_name="addSubscriptionFilter")
    def add_subscription_filter(self, id: str, *, destination: "ILogSubscriptionDestination", filter_pattern: "IFilterPattern") -> "SubscriptionFilter":
        """Create a new Subscription Filter on this Log Group.

        Arguments:
            id: Unique identifier for the construct in its parent.
            props: Properties for creating the SubscriptionFilter.
            destination: The destination to send the filtered events to. For example, a Kinesis stream or a Lambda function.
            filter_pattern: Log events matching this pattern will be sent to the destination.

        Stability:
            stable
        """
        props: SubscriptionFilterOptions = {"destination": destination, "filterPattern": filter_pattern}

        return jsii.invoke(self, "addSubscriptionFilter", [id, props])

    @jsii.member(jsii_name="extractMetric")
    def extract_metric(self, json_field: str, metric_namespace: str, metric_name: str) -> aws_cdk.aws_cloudwatch.Metric:
        """Extract a metric from structured log events in the LogGroup.

        Creates a MetricFilter on this LogGroup that will extract the value
        of the indicated JSON field in all records where it occurs.

        The metric will be available in CloudWatch Metrics under the
        indicated namespace and name.

        Arguments:
            json_field: JSON field to extract (example: '$.myfield').
            metric_namespace: Namespace to emit the metric under.
            metric_name: Name to emit the metric under.

        Returns:
            A Metric object representing the extracted metric

        Stability:
            stable
        """
        return jsii.invoke(self, "extractMetric", [json_field, metric_namespace, metric_name])

    @jsii.member(jsii_name="grant")
    def grant(self, grantee: aws_cdk.aws_iam.IGrantable, *actions: str) -> aws_cdk.aws_iam.Grant:
        """Give the indicated permissions on this log group and all streams.

        Arguments:
            grantee: -
            actions: -

        Stability:
            stable
        """
        return jsii.invoke(self, "grant", [grantee, *actions])

    @jsii.member(jsii_name="grantWrite")
    def grant_write(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Give permissions to write to create and write to streams in this log group.

        Arguments:
            grantee: -

        Stability:
            stable
        """
        return jsii.invoke(self, "grantWrite", [grantee])

    @property
    @jsii.member(jsii_name="logGroupArn")
    def log_group_arn(self) -> str:
        """The ARN of this log group.

        Stability:
            stable
        """
        return jsii.get(self, "logGroupArn")

    @property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> str:
        """The name of this log group.

        Stability:
            stable
        """
        return jsii.get(self, "logGroupName")


@jsii.data_type(jsii_type="@aws-cdk/aws-logs.LogGroupProps", jsii_struct_bases=[])
class LogGroupProps(jsii.compat.TypedDict, total=False):
    """Properties for a LogGroup.

    Stability:
        stable
    """
    logGroupName: str
    """Name of the log group.

    Default:
        Automatically generated

    Stability:
        stable
    """

    removalPolicy: aws_cdk.core.RemovalPolicy
    """Determine the removal policy of this log group.

    Normally you want to retain the log group so you can diagnose issues
    from logs even after a deployment that no longer includes the log group.
    In that case, use the normal date-based retention policy to age out your
    logs.

    Default:
        RemovalPolicy.Retain

    Stability:
        stable
    """

    retention: "RetentionDays"
    """How long, in days, the log contents will be retained.

    To retain all logs, set this value to Infinity.

    Default:
        RetentionDays.TwoYears

    Stability:
        stable
    """

@jsii.implements(ILogStream)
class LogStream(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-logs.LogStream"):
    """Define a Log Stream in a Log Group.

    Stability:
        stable
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, log_group: "ILogGroup", log_stream_name: typing.Optional[str]=None, removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            log_group: The log group to create a log stream for.
            log_stream_name: The name of the log stream to create. The name must be unique within the log group. Default: Automatically generated
            removal_policy: Determine what happens when the log stream resource is removed from the app. Normally you want to retain the log stream so you can diagnose issues from logs even after a deployment that no longer includes the log stream. The date-based retention policy of your log group will age out the logs after a certain time. Default: RemovalPolicy.Retain

        Stability:
            stable
        """
        props: LogStreamProps = {"logGroup": log_group}

        if log_stream_name is not None:
            props["logStreamName"] = log_stream_name

        if removal_policy is not None:
            props["removalPolicy"] = removal_policy

        jsii.create(LogStream, self, [scope, id, props])

    @jsii.member(jsii_name="fromLogStreamName")
    @classmethod
    def from_log_stream_name(cls, scope: aws_cdk.core.Construct, id: str, log_stream_name: str) -> "ILogStream":
        """Import an existing LogGroup.

        Arguments:
            scope: -
            id: -
            log_stream_name: -

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "fromLogStreamName", [scope, id, log_stream_name])

    @property
    @jsii.member(jsii_name="logStreamName")
    def log_stream_name(self) -> str:
        """The name of this log stream.

        Stability:
            stable
        """
        return jsii.get(self, "logStreamName")


@jsii.data_type_optionals(jsii_struct_bases=[])
class _LogStreamProps(jsii.compat.TypedDict, total=False):
    logStreamName: str
    """The name of the log stream to create.

    The name must be unique within the log group.

    Default:
        Automatically generated

    Stability:
        stable
    """
    removalPolicy: aws_cdk.core.RemovalPolicy
    """Determine what happens when the log stream resource is removed from the app.

    Normally you want to retain the log stream so you can diagnose issues from
    logs even after a deployment that no longer includes the log stream.

    The date-based retention policy of your log group will age out the logs
    after a certain time.

    Default:
        RemovalPolicy.Retain

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-logs.LogStreamProps", jsii_struct_bases=[_LogStreamProps])
class LogStreamProps(_LogStreamProps):
    """Properties for a LogStream.

    Stability:
        stable
    """
    logGroup: "ILogGroup"
    """The log group to create a log stream for.

    Stability:
        stable
    """

@jsii.data_type_optionals(jsii_struct_bases=[])
class _LogSubscriptionDestinationConfig(jsii.compat.TypedDict, total=False):
    role: aws_cdk.aws_iam.IRole
    """The role to assume to write log events to the destination.

    Default:
        No role assumed

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-logs.LogSubscriptionDestinationConfig", jsii_struct_bases=[_LogSubscriptionDestinationConfig])
class LogSubscriptionDestinationConfig(_LogSubscriptionDestinationConfig):
    """Properties returned by a Subscription destination.

    Stability:
        stable
    """
    arn: str
    """The ARN of the subscription's destination.

    Stability:
        stable
    """

class MetricFilter(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-logs.MetricFilter"):
    """A filter that extracts information from CloudWatch Logs and emits to CloudWatch Metrics.

    Stability:
        stable
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, log_group: "ILogGroup", filter_pattern: "IFilterPattern", metric_name: str, metric_namespace: str, default_value: typing.Optional[jsii.Number]=None, metric_value: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            log_group: The log group to create the filter on.
            filter_pattern: Pattern to search for log events.
            metric_name: The name of the metric to emit.
            metric_namespace: The namespace of the metric to emit.
            default_value: The value to emit if the pattern does not match a particular event. Default: No metric emitted.
            metric_value: The value to emit for the metric. Can either be a literal number (typically "1"), or the name of a field in the structure to take the value from the matched event. If you are using a field value, the field value must have been matched using the pattern. If you want to specify a field from a matched JSON structure, use '$.fieldName', and make sure the field is in the pattern (if only as '$.fieldName = *'). If you want to specify a field from a matched space-delimited structure, use '$fieldName'. Default: "1"

        Stability:
            stable
        """
        props: MetricFilterProps = {"logGroup": log_group, "filterPattern": filter_pattern, "metricName": metric_name, "metricNamespace": metric_namespace}

        if default_value is not None:
            props["defaultValue"] = default_value

        if metric_value is not None:
            props["metricValue"] = metric_value

        jsii.create(MetricFilter, self, [scope, id, props])


@jsii.data_type_optionals(jsii_struct_bases=[])
class _MetricFilterOptions(jsii.compat.TypedDict, total=False):
    defaultValue: jsii.Number
    """The value to emit if the pattern does not match a particular event.

    Default:
        No metric emitted.

    Stability:
        stable
    """
    metricValue: str
    """The value to emit for the metric.

    Can either be a literal number (typically "1"), or the name of a field in the structure
    to take the value from the matched event. If you are using a field value, the field
    value must have been matched using the pattern.

    If you want to specify a field from a matched JSON structure, use '$.fieldName',
    and make sure the field is in the pattern (if only as '$.fieldName = *').

    If you want to specify a field from a matched space-delimited structure,
    use '$fieldName'.

    Default:
        "1"

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-logs.MetricFilterOptions", jsii_struct_bases=[_MetricFilterOptions])
class MetricFilterOptions(_MetricFilterOptions):
    """Properties for a MetricFilter created from a LogGroup.

    Stability:
        stable
    """
    filterPattern: "IFilterPattern"
    """Pattern to search for log events.

    Stability:
        stable
    """

    metricName: str
    """The name of the metric to emit.

    Stability:
        stable
    """

    metricNamespace: str
    """The namespace of the metric to emit.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-logs.MetricFilterProps", jsii_struct_bases=[MetricFilterOptions])
class MetricFilterProps(MetricFilterOptions, jsii.compat.TypedDict):
    """Properties for a MetricFilter.

    Stability:
        stable
    """
    logGroup: "ILogGroup"
    """The log group to create the filter on.

    Stability:
        stable
    """

@jsii.enum(jsii_type="@aws-cdk/aws-logs.RetentionDays")
class RetentionDays(enum.Enum):
    """How long, in days, the log contents will be retained.

    Stability:
        stable
    """
    ONE_DAY = "ONE_DAY"
    """1 day.

    Stability:
        stable
    """
    THREE_DAYS = "THREE_DAYS"
    """3 days.

    Stability:
        stable
    """
    FIVE_DAYS = "FIVE_DAYS"
    """5 days.

    Stability:
        stable
    """
    ONE_WEEK = "ONE_WEEK"
    """1 week.

    Stability:
        stable
    """
    TWO_WEEKS = "TWO_WEEKS"
    """2 weeks.

    Stability:
        stable
    """
    ONE_MONTH = "ONE_MONTH"
    """1 month.

    Stability:
        stable
    """
    TWO_MONTHS = "TWO_MONTHS"
    """2 months.

    Stability:
        stable
    """
    THREE_MONTHS = "THREE_MONTHS"
    """3 months.

    Stability:
        stable
    """
    FOUR_MONTHS = "FOUR_MONTHS"
    """4 months.

    Stability:
        stable
    """
    FIVE_MONTHS = "FIVE_MONTHS"
    """5 months.

    Stability:
        stable
    """
    SIX_MONTHS = "SIX_MONTHS"
    """6 months.

    Stability:
        stable
    """
    ONE_YEAR = "ONE_YEAR"
    """1 year.

    Stability:
        stable
    """
    THIRTEEN_MONTHS = "THIRTEEN_MONTHS"
    """13 months.

    Stability:
        stable
    """
    EIGHTEEN_MONTHS = "EIGHTEEN_MONTHS"
    """18 months.

    Stability:
        stable
    """
    TWO_YEARS = "TWO_YEARS"
    """2 years.

    Stability:
        stable
    """
    FIVE_YEARS = "FIVE_YEARS"
    """5 years.

    Stability:
        stable
    """
    TEN_YEARS = "TEN_YEARS"
    """10 years.

    Stability:
        stable
    """

@jsii.implements(IFilterPattern)
class SpaceDelimitedTextPattern(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-logs.SpaceDelimitedTextPattern"):
    """Space delimited text pattern.

    Stability:
        stable
    """
    def __init__(self, columns: typing.List[str], restrictions: typing.Mapping[str,typing.List["ColumnRestriction"]]) -> None:
        """
        Arguments:
            columns: -
            restrictions: -

        Stability:
            stable
        """
        jsii.create(SpaceDelimitedTextPattern, self, [columns, restrictions])

    @jsii.member(jsii_name="construct")
    @classmethod
    def construct(cls, columns: typing.List[str]) -> "SpaceDelimitedTextPattern":
        """Construct a new instance of a space delimited text pattern.

        Since this class must be public, we can't rely on the user only creating it through
        the ``LogPattern.spaceDelimited()`` factory function. We must therefore validate the
        argument in the constructor. Since we're returning a copy on every mutation, and we
        don't want to re-validate the same things on every construction, we provide a limited
        set of mutator functions and only validate the new data every time.

        Arguments:
            columns: -

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "construct", [columns])

    @jsii.member(jsii_name="whereNumber")
    def where_number(self, column_name: str, comparison: str, value: jsii.Number) -> "SpaceDelimitedTextPattern":
        """Restrict where the pattern applies.

        Arguments:
            column_name: -
            comparison: -
            value: -

        Stability:
            stable
        """
        return jsii.invoke(self, "whereNumber", [column_name, comparison, value])

    @jsii.member(jsii_name="whereString")
    def where_string(self, column_name: str, comparison: str, value: str) -> "SpaceDelimitedTextPattern":
        """Restrict where the pattern applies.

        Arguments:
            column_name: -
            comparison: -
            value: -

        Stability:
            stable
        """
        return jsii.invoke(self, "whereString", [column_name, comparison, value])

    @property
    @jsii.member(jsii_name="logPatternString")
    def log_pattern_string(self) -> str:
        """
        Stability:
            stable
        """
        return jsii.get(self, "logPatternString")


@jsii.data_type(jsii_type="@aws-cdk/aws-logs.StreamOptions", jsii_struct_bases=[])
class StreamOptions(jsii.compat.TypedDict, total=False):
    """Properties for a new LogStream created from a LogGroup.

    Stability:
        stable
    """
    logStreamName: str
    """The name of the log stream to create.

    The name must be unique within the log group.

    Default:
        Automatically generated

    Stability:
        stable
    """

class SubscriptionFilter(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-logs.SubscriptionFilter"):
    """A new Subscription on a CloudWatch log group.

    Stability:
        stable
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, log_group: "ILogGroup", destination: "ILogSubscriptionDestination", filter_pattern: "IFilterPattern") -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            log_group: The log group to create the subscription on.
            destination: The destination to send the filtered events to. For example, a Kinesis stream or a Lambda function.
            filter_pattern: Log events matching this pattern will be sent to the destination.

        Stability:
            stable
        """
        props: SubscriptionFilterProps = {"logGroup": log_group, "destination": destination, "filterPattern": filter_pattern}

        jsii.create(SubscriptionFilter, self, [scope, id, props])


@jsii.data_type(jsii_type="@aws-cdk/aws-logs.SubscriptionFilterOptions", jsii_struct_bases=[])
class SubscriptionFilterOptions(jsii.compat.TypedDict):
    """Properties for a new SubscriptionFilter created from a LogGroup.

    Stability:
        stable
    """
    destination: "ILogSubscriptionDestination"
    """The destination to send the filtered events to.

    For example, a Kinesis stream or a Lambda function.

    Stability:
        stable
    """

    filterPattern: "IFilterPattern"
    """Log events matching this pattern will be sent to the destination.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-logs.SubscriptionFilterProps", jsii_struct_bases=[SubscriptionFilterOptions])
class SubscriptionFilterProps(SubscriptionFilterOptions, jsii.compat.TypedDict):
    """Properties for a SubscriptionFilter.

    Stability:
        stable
    """
    logGroup: "ILogGroup"
    """The log group to create the subscription on.

    Stability:
        stable
    """

__all__ = ["CfnDestination", "CfnDestinationProps", "CfnLogGroup", "CfnLogGroupProps", "CfnLogStream", "CfnLogStreamProps", "CfnMetricFilter", "CfnMetricFilterProps", "CfnSubscriptionFilter", "CfnSubscriptionFilterProps", "ColumnRestriction", "CrossAccountDestination", "CrossAccountDestinationProps", "FilterPattern", "IFilterPattern", "ILogGroup", "ILogStream", "ILogSubscriptionDestination", "JsonPattern", "LogGroup", "LogGroupProps", "LogStream", "LogStreamProps", "LogSubscriptionDestinationConfig", "MetricFilter", "MetricFilterOptions", "MetricFilterProps", "RetentionDays", "SpaceDelimitedTextPattern", "StreamOptions", "SubscriptionFilter", "SubscriptionFilterOptions", "SubscriptionFilterProps", "__jsii_assembly__"]

publication.publish()
