import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_autoscaling_common
import aws_cdk.aws_cloudwatch
import aws_cdk.aws_ec2
import aws_cdk.aws_elasticloadbalancing
import aws_cdk.aws_elasticloadbalancingv2
import aws_cdk.aws_iam
import aws_cdk.aws_sns
import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-autoscaling", "0.36.1", __name__, "aws-autoscaling@0.36.1.jsii.tgz")
@jsii.data_type_optionals(jsii_struct_bases=[])
class _AdjustmentTier(jsii.compat.TypedDict, total=False):
    lowerBound: jsii.Number
    """Lower bound where this scaling tier applies.

    The scaling tier applies if the difference between the metric
    value and its alarm threshold is higher than this value.

    Default:
        -Infinity if this is the first tier, otherwise the upperBound of the previous tier

    Stability:
        experimental
    """
    upperBound: jsii.Number
    """Upper bound where this scaling tier applies.

    The scaling tier applies if the difference between the metric
    value and its alarm threshold is lower than this value.

    Default:
        +Infinity

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.AdjustmentTier", jsii_struct_bases=[_AdjustmentTier])
class AdjustmentTier(_AdjustmentTier):
    """An adjustment.

    Stability:
        experimental
    """
    adjustment: jsii.Number
    """What number to adjust the capacity with.

    The number is interpeted as an added capacity, a new fixed capacity or an
    added percentage depending on the AdjustmentType value of the
    StepScalingPolicy.

    Can be positive or negative.

    Stability:
        experimental
    """

@jsii.enum(jsii_type="@aws-cdk/aws-autoscaling.AdjustmentType")
class AdjustmentType(enum.Enum):
    """How adjustment numbers are interpreted.

    Stability:
        experimental
    """
    CHANGE_IN_CAPACITY = "CHANGE_IN_CAPACITY"
    """Add the adjustment number to the current capacity.

    A positive number increases capacity, a negative number decreases capacity.

    Stability:
        experimental
    """
    PERCENT_CHANGE_IN_CAPACITY = "PERCENT_CHANGE_IN_CAPACITY"
    """Add this percentage of the current capacity to itself.

    The number must be between -100 and 100; a positive number increases
    capacity and a negative number decreases it.

    Stability:
        experimental
    """
    EXACT_CAPACITY = "EXACT_CAPACITY"
    """Make the capacity equal to the exact number given.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.BaseTargetTrackingProps", jsii_struct_bases=[])
class BaseTargetTrackingProps(jsii.compat.TypedDict, total=False):
    """Base interface for target tracking props.

    Contains the attributes that are common to target tracking policies,
    except the ones relating to the metric and to the scalable target.

    This interface is reused by more specific target tracking props objects.

    Stability:
        experimental
    """
    cooldown: aws_cdk.core.Duration
    """Period after a scaling completes before another scaling activity can start.

    Default:
        - The default cooldown configured on the AutoScalingGroup.

    Stability:
        experimental
    """

    disableScaleIn: bool
    """Indicates whether scale in by the target tracking policy is disabled.

    If the value is true, scale in is disabled and the target tracking policy
    won't remove capacity from the autoscaling group. Otherwise, scale in is
    enabled and the target tracking policy can remove capacity from the
    group.

    Default:
        false

    Stability:
        experimental
    """

    estimatedInstanceWarmup: aws_cdk.core.Duration
    """Estimated time until a newly launched instance can send metrics to CloudWatch.

    Default:
        - Same as the cooldown.

    Stability:
        experimental
    """

@jsii.data_type_optionals(jsii_struct_bases=[])
class _BasicLifecycleHookProps(jsii.compat.TypedDict, total=False):
    defaultResult: "DefaultResult"
    """The action the Auto Scaling group takes when the lifecycle hook timeout elapses or if an unexpected failure occurs.

    Default:
        Continue

    Stability:
        experimental
    """
    heartbeatTimeout: aws_cdk.core.Duration
    """Maximum time between calls to RecordLifecycleActionHeartbeat for the hook.

    If the lifecycle hook times out, perform the action in DefaultResult.

    Default:
        - No heartbeat timeout.

    Stability:
        experimental
    """
    lifecycleHookName: str
    """Name of the lifecycle hook.

    Default:
        - Automatically generated name.

    Stability:
        experimental
    """
    notificationMetadata: str
    """Additional data to pass to the lifecycle hook target.

    Default:
        - No metadata.

    Stability:
        experimental
    """
    role: aws_cdk.aws_iam.IRole
    """The role that allows publishing to the notification target.

    Default:
        - A role is automatically created.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.BasicLifecycleHookProps", jsii_struct_bases=[_BasicLifecycleHookProps])
class BasicLifecycleHookProps(_BasicLifecycleHookProps):
    """Basic properties for a lifecycle hook.

    Stability:
        experimental
    """
    lifecycleTransition: "LifecycleTransition"
    """The state of the Amazon EC2 instance to which you want to attach the lifecycle hook.

    Stability:
        experimental
    """

    notificationTarget: "ILifecycleHookTarget"
    """The target of the lifecycle hook.

    Stability:
        experimental
    """

@jsii.data_type_optionals(jsii_struct_bases=[])
class _BasicScheduledActionProps(jsii.compat.TypedDict, total=False):
    desiredCapacity: jsii.Number
    """The new desired capacity.

    At the scheduled time, set the desired capacity to the given capacity.

    At least one of maxCapacity, minCapacity, or desiredCapacity must be supplied.

    Default:
        - No new desired capacity.

    Stability:
        experimental
    """
    endTime: datetime.datetime
    """When this scheduled action expires.

    Default:
        - The rule never expires.

    Stability:
        experimental
    """
    maxCapacity: jsii.Number
    """The new maximum capacity.

    At the scheduled time, set the maximum capacity to the given capacity.

    At least one of maxCapacity, minCapacity, or desiredCapacity must be supplied.

    Default:
        - No new maximum capacity.

    Stability:
        experimental
    """
    minCapacity: jsii.Number
    """The new minimum capacity.

    At the scheduled time, set the minimum capacity to the given capacity.

    At least one of maxCapacity, minCapacity, or desiredCapacity must be supplied.

    Default:
        - No new minimum capacity.

    Stability:
        experimental
    """
    startTime: datetime.datetime
    """When this scheduled action becomes active.

    Default:
        - The rule is activate immediately.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.BasicScheduledActionProps", jsii_struct_bases=[_BasicScheduledActionProps])
class BasicScheduledActionProps(_BasicScheduledActionProps):
    """Properties for a scheduled scaling action.

    Stability:
        experimental
    """
    schedule: "Schedule"
    """When to perform this action.

    Supports cron expressions.

    For more information about cron expressions, see https://en.wikipedia.org/wiki/Cron.

    Stability:
        experimental

    Example::
        0 8 * * ?
    """

@jsii.data_type_optionals(jsii_struct_bases=[])
class _BasicStepScalingPolicyProps(jsii.compat.TypedDict, total=False):
    adjustmentType: "AdjustmentType"
    """How the adjustment numbers inside 'intervals' are interpreted.

    Default:
        ChangeInCapacity

    Stability:
        experimental
    """
    cooldown: aws_cdk.core.Duration
    """Grace period after scaling activity.

    Default:
        Default cooldown period on your AutoScalingGroup

    Stability:
        experimental
    """
    estimatedInstanceWarmup: aws_cdk.core.Duration
    """Estimated time until a newly launched instance can send metrics to CloudWatch.

    Default:
        Same as the cooldown

    Stability:
        experimental
    """
    minAdjustmentMagnitude: jsii.Number
    """Minimum absolute number to adjust capacity with as result of percentage scaling.

    Only when using AdjustmentType = PercentChangeInCapacity, this number controls
    the minimum absolute effect size.

    Default:
        No minimum scaling effect

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.BasicStepScalingPolicyProps", jsii_struct_bases=[_BasicStepScalingPolicyProps])
class BasicStepScalingPolicyProps(_BasicStepScalingPolicyProps):
    """
    Stability:
        experimental
    """
    metric: aws_cdk.aws_cloudwatch.IMetric
    """Metric to scale on.

    Stability:
        experimental
    """

    scalingSteps: typing.List["ScalingInterval"]
    """The intervals for scaling.

    Maps a range of metric values to a particular scaling behavior.

    Stability:
        experimental
    """

@jsii.data_type_optionals(jsii_struct_bases=[BaseTargetTrackingProps])
class _BasicTargetTrackingScalingPolicyProps(BaseTargetTrackingProps, jsii.compat.TypedDict, total=False):
    customMetric: aws_cdk.aws_cloudwatch.IMetric
    """A custom metric for application autoscaling.

    The metric must track utilization. Scaling out will happen if the metric is higher than
    the target value, scaling in will happen in the metric is lower than the target value.

    Exactly one of customMetric or predefinedMetric must be specified.

    Default:
        - No custom metric.

    Stability:
        experimental
    """
    predefinedMetric: "PredefinedMetric"
    """A predefined metric for application autoscaling.

    The metric must track utilization. Scaling out will happen if the metric is higher than
    the target value, scaling in will happen in the metric is lower than the target value.

    Exactly one of customMetric or predefinedMetric must be specified.

    Default:
        - No predefined metric.

    Stability:
        experimental
    """
    resourceLabel: str
    """The resource label associated with the predefined metric.

    Should be supplied if the predefined metric is ALBRequestCountPerTarget, and the
    format should be:

    app///targetgroup//

    Default:
        - No resource label.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.BasicTargetTrackingScalingPolicyProps", jsii_struct_bases=[_BasicTargetTrackingScalingPolicyProps])
class BasicTargetTrackingScalingPolicyProps(_BasicTargetTrackingScalingPolicyProps):
    """Properties for a Target Tracking policy that include the metric but exclude the target.

    Stability:
        experimental
    """
    targetValue: jsii.Number
    """The target value for the metric.

    Stability:
        experimental
    """

class CfnAutoScalingGroup(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-autoscaling.CfnAutoScalingGroup"):
    """A CloudFormation ``AWS::AutoScaling::AutoScalingGroup``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html
    Stability:
        stable
    cloudformationResource:
        AWS::AutoScaling::AutoScalingGroup
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, max_size: str, min_size: str, auto_scaling_group_name: typing.Optional[str]=None, availability_zones: typing.Optional[typing.List[str]]=None, cooldown: typing.Optional[str]=None, desired_capacity: typing.Optional[str]=None, health_check_grace_period: typing.Optional[jsii.Number]=None, health_check_type: typing.Optional[str]=None, instance_id: typing.Optional[str]=None, launch_configuration_name: typing.Optional[str]=None, launch_template: typing.Optional[typing.Union[typing.Optional["LaunchTemplateSpecificationProperty"], typing.Optional[aws_cdk.core.IResolvable]]]=None, lifecycle_hook_specification_list: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "LifecycleHookSpecificationProperty"]]]]]=None, load_balancer_names: typing.Optional[typing.List[str]]=None, metrics_collection: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "MetricsCollectionProperty"]]]]]=None, mixed_instances_policy: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["MixedInstancesPolicyProperty"]]]=None, notification_configurations: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "NotificationConfigurationProperty"]]]]]=None, placement_group: typing.Optional[str]=None, service_linked_role_arn: typing.Optional[str]=None, tags: typing.Optional[typing.List["TagPropertyProperty"]]=None, target_group_arns: typing.Optional[typing.List[str]]=None, termination_policies: typing.Optional[typing.List[str]]=None, vpc_zone_identifier: typing.Optional[typing.List[str]]=None) -> None:
        """Create a new ``AWS::AutoScaling::AutoScalingGroup``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            max_size: ``AWS::AutoScaling::AutoScalingGroup.MaxSize``.
            min_size: ``AWS::AutoScaling::AutoScalingGroup.MinSize``.
            auto_scaling_group_name: ``AWS::AutoScaling::AutoScalingGroup.AutoScalingGroupName``.
            availability_zones: ``AWS::AutoScaling::AutoScalingGroup.AvailabilityZones``.
            cooldown: ``AWS::AutoScaling::AutoScalingGroup.Cooldown``.
            desired_capacity: ``AWS::AutoScaling::AutoScalingGroup.DesiredCapacity``.
            health_check_grace_period: ``AWS::AutoScaling::AutoScalingGroup.HealthCheckGracePeriod``.
            health_check_type: ``AWS::AutoScaling::AutoScalingGroup.HealthCheckType``.
            instance_id: ``AWS::AutoScaling::AutoScalingGroup.InstanceId``.
            launch_configuration_name: ``AWS::AutoScaling::AutoScalingGroup.LaunchConfigurationName``.
            launch_template: ``AWS::AutoScaling::AutoScalingGroup.LaunchTemplate``.
            lifecycle_hook_specification_list: ``AWS::AutoScaling::AutoScalingGroup.LifecycleHookSpecificationList``.
            load_balancer_names: ``AWS::AutoScaling::AutoScalingGroup.LoadBalancerNames``.
            metrics_collection: ``AWS::AutoScaling::AutoScalingGroup.MetricsCollection``.
            mixed_instances_policy: ``AWS::AutoScaling::AutoScalingGroup.MixedInstancesPolicy``.
            notification_configurations: ``AWS::AutoScaling::AutoScalingGroup.NotificationConfigurations``.
            placement_group: ``AWS::AutoScaling::AutoScalingGroup.PlacementGroup``.
            service_linked_role_arn: ``AWS::AutoScaling::AutoScalingGroup.ServiceLinkedRoleARN``.
            tags: ``AWS::AutoScaling::AutoScalingGroup.Tags``.
            target_group_arns: ``AWS::AutoScaling::AutoScalingGroup.TargetGroupARNs``.
            termination_policies: ``AWS::AutoScaling::AutoScalingGroup.TerminationPolicies``.
            vpc_zone_identifier: ``AWS::AutoScaling::AutoScalingGroup.VPCZoneIdentifier``.

        Stability:
            experimental
        """
        props: CfnAutoScalingGroupProps = {"maxSize": max_size, "minSize": min_size}

        if auto_scaling_group_name is not None:
            props["autoScalingGroupName"] = auto_scaling_group_name

        if availability_zones is not None:
            props["availabilityZones"] = availability_zones

        if cooldown is not None:
            props["cooldown"] = cooldown

        if desired_capacity is not None:
            props["desiredCapacity"] = desired_capacity

        if health_check_grace_period is not None:
            props["healthCheckGracePeriod"] = health_check_grace_period

        if health_check_type is not None:
            props["healthCheckType"] = health_check_type

        if instance_id is not None:
            props["instanceId"] = instance_id

        if launch_configuration_name is not None:
            props["launchConfigurationName"] = launch_configuration_name

        if launch_template is not None:
            props["launchTemplate"] = launch_template

        if lifecycle_hook_specification_list is not None:
            props["lifecycleHookSpecificationList"] = lifecycle_hook_specification_list

        if load_balancer_names is not None:
            props["loadBalancerNames"] = load_balancer_names

        if metrics_collection is not None:
            props["metricsCollection"] = metrics_collection

        if mixed_instances_policy is not None:
            props["mixedInstancesPolicy"] = mixed_instances_policy

        if notification_configurations is not None:
            props["notificationConfigurations"] = notification_configurations

        if placement_group is not None:
            props["placementGroup"] = placement_group

        if service_linked_role_arn is not None:
            props["serviceLinkedRoleArn"] = service_linked_role_arn

        if tags is not None:
            props["tags"] = tags

        if target_group_arns is not None:
            props["targetGroupArns"] = target_group_arns

        if termination_policies is not None:
            props["terminationPolicies"] = termination_policies

        if vpc_zone_identifier is not None:
            props["vpcZoneIdentifier"] = vpc_zone_identifier

        jsii.create(CfnAutoScalingGroup, self, [scope, id, props])

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::AutoScaling::AutoScalingGroup.Tags``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-tags
        Stability:
            stable
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="maxSize")
    def max_size(self) -> str:
        """``AWS::AutoScaling::AutoScalingGroup.MaxSize``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-maxsize
        Stability:
            stable
        """
        return jsii.get(self, "maxSize")

    @max_size.setter
    def max_size(self, value: str):
        return jsii.set(self, "maxSize", value)

    @property
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> str:
        """``AWS::AutoScaling::AutoScalingGroup.MinSize``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-minsize
        Stability:
            stable
        """
        return jsii.get(self, "minSize")

    @min_size.setter
    def min_size(self, value: str):
        return jsii.set(self, "minSize", value)

    @property
    @jsii.member(jsii_name="autoScalingGroupName")
    def auto_scaling_group_name(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::AutoScalingGroup.AutoScalingGroupName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-autoscaling-autoscalinggroup-autoscalinggroupname
        Stability:
            stable
        """
        return jsii.get(self, "autoScalingGroupName")

    @auto_scaling_group_name.setter
    def auto_scaling_group_name(self, value: typing.Optional[str]):
        return jsii.set(self, "autoScalingGroupName", value)

    @property
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.Optional[typing.List[str]]:
        """``AWS::AutoScaling::AutoScalingGroup.AvailabilityZones``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-availabilityzones
        Stability:
            stable
        """
        return jsii.get(self, "availabilityZones")

    @availability_zones.setter
    def availability_zones(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "availabilityZones", value)

    @property
    @jsii.member(jsii_name="cooldown")
    def cooldown(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::AutoScalingGroup.Cooldown``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-cooldown
        Stability:
            stable
        """
        return jsii.get(self, "cooldown")

    @cooldown.setter
    def cooldown(self, value: typing.Optional[str]):
        return jsii.set(self, "cooldown", value)

    @property
    @jsii.member(jsii_name="desiredCapacity")
    def desired_capacity(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::AutoScalingGroup.DesiredCapacity``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-desiredcapacity
        Stability:
            stable
        """
        return jsii.get(self, "desiredCapacity")

    @desired_capacity.setter
    def desired_capacity(self, value: typing.Optional[str]):
        return jsii.set(self, "desiredCapacity", value)

    @property
    @jsii.member(jsii_name="healthCheckGracePeriod")
    def health_check_grace_period(self) -> typing.Optional[jsii.Number]:
        """``AWS::AutoScaling::AutoScalingGroup.HealthCheckGracePeriod``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-healthcheckgraceperiod
        Stability:
            stable
        """
        return jsii.get(self, "healthCheckGracePeriod")

    @health_check_grace_period.setter
    def health_check_grace_period(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "healthCheckGracePeriod", value)

    @property
    @jsii.member(jsii_name="healthCheckType")
    def health_check_type(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::AutoScalingGroup.HealthCheckType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-healthchecktype
        Stability:
            stable
        """
        return jsii.get(self, "healthCheckType")

    @health_check_type.setter
    def health_check_type(self, value: typing.Optional[str]):
        return jsii.set(self, "healthCheckType", value)

    @property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::AutoScalingGroup.InstanceId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-instanceid
        Stability:
            stable
        """
        return jsii.get(self, "instanceId")

    @instance_id.setter
    def instance_id(self, value: typing.Optional[str]):
        return jsii.set(self, "instanceId", value)

    @property
    @jsii.member(jsii_name="launchConfigurationName")
    def launch_configuration_name(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::AutoScalingGroup.LaunchConfigurationName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-launchconfigurationname
        Stability:
            stable
        """
        return jsii.get(self, "launchConfigurationName")

    @launch_configuration_name.setter
    def launch_configuration_name(self, value: typing.Optional[str]):
        return jsii.set(self, "launchConfigurationName", value)

    @property
    @jsii.member(jsii_name="launchTemplate")
    def launch_template(self) -> typing.Optional[typing.Union[typing.Optional["LaunchTemplateSpecificationProperty"], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::AutoScaling::AutoScalingGroup.LaunchTemplate``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-launchtemplate
        Stability:
            stable
        """
        return jsii.get(self, "launchTemplate")

    @launch_template.setter
    def launch_template(self, value: typing.Optional[typing.Union[typing.Optional["LaunchTemplateSpecificationProperty"], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "launchTemplate", value)

    @property
    @jsii.member(jsii_name="lifecycleHookSpecificationList")
    def lifecycle_hook_specification_list(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "LifecycleHookSpecificationProperty"]]]]]:
        """``AWS::AutoScaling::AutoScalingGroup.LifecycleHookSpecificationList``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecificationlist
        Stability:
            stable
        """
        return jsii.get(self, "lifecycleHookSpecificationList")

    @lifecycle_hook_specification_list.setter
    def lifecycle_hook_specification_list(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "LifecycleHookSpecificationProperty"]]]]]):
        return jsii.set(self, "lifecycleHookSpecificationList", value)

    @property
    @jsii.member(jsii_name="loadBalancerNames")
    def load_balancer_names(self) -> typing.Optional[typing.List[str]]:
        """``AWS::AutoScaling::AutoScalingGroup.LoadBalancerNames``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-loadbalancernames
        Stability:
            stable
        """
        return jsii.get(self, "loadBalancerNames")

    @load_balancer_names.setter
    def load_balancer_names(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "loadBalancerNames", value)

    @property
    @jsii.member(jsii_name="metricsCollection")
    def metrics_collection(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "MetricsCollectionProperty"]]]]]:
        """``AWS::AutoScaling::AutoScalingGroup.MetricsCollection``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-metricscollection
        Stability:
            stable
        """
        return jsii.get(self, "metricsCollection")

    @metrics_collection.setter
    def metrics_collection(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "MetricsCollectionProperty"]]]]]):
        return jsii.set(self, "metricsCollection", value)

    @property
    @jsii.member(jsii_name="mixedInstancesPolicy")
    def mixed_instances_policy(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["MixedInstancesPolicyProperty"]]]:
        """``AWS::AutoScaling::AutoScalingGroup.MixedInstancesPolicy``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-mixedinstancespolicy
        Stability:
            stable
        """
        return jsii.get(self, "mixedInstancesPolicy")

    @mixed_instances_policy.setter
    def mixed_instances_policy(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["MixedInstancesPolicyProperty"]]]):
        return jsii.set(self, "mixedInstancesPolicy", value)

    @property
    @jsii.member(jsii_name="notificationConfigurations")
    def notification_configurations(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "NotificationConfigurationProperty"]]]]]:
        """``AWS::AutoScaling::AutoScalingGroup.NotificationConfigurations``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-notificationconfigurations
        Stability:
            stable
        """
        return jsii.get(self, "notificationConfigurations")

    @notification_configurations.setter
    def notification_configurations(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "NotificationConfigurationProperty"]]]]]):
        return jsii.set(self, "notificationConfigurations", value)

    @property
    @jsii.member(jsii_name="placementGroup")
    def placement_group(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::AutoScalingGroup.PlacementGroup``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-placementgroup
        Stability:
            stable
        """
        return jsii.get(self, "placementGroup")

    @placement_group.setter
    def placement_group(self, value: typing.Optional[str]):
        return jsii.set(self, "placementGroup", value)

    @property
    @jsii.member(jsii_name="serviceLinkedRoleArn")
    def service_linked_role_arn(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::AutoScalingGroup.ServiceLinkedRoleARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-autoscaling-autoscalinggroup-servicelinkedrolearn
        Stability:
            stable
        """
        return jsii.get(self, "serviceLinkedRoleArn")

    @service_linked_role_arn.setter
    def service_linked_role_arn(self, value: typing.Optional[str]):
        return jsii.set(self, "serviceLinkedRoleArn", value)

    @property
    @jsii.member(jsii_name="targetGroupArns")
    def target_group_arns(self) -> typing.Optional[typing.List[str]]:
        """``AWS::AutoScaling::AutoScalingGroup.TargetGroupARNs``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-targetgrouparns
        Stability:
            stable
        """
        return jsii.get(self, "targetGroupArns")

    @target_group_arns.setter
    def target_group_arns(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "targetGroupArns", value)

    @property
    @jsii.member(jsii_name="terminationPolicies")
    def termination_policies(self) -> typing.Optional[typing.List[str]]:
        """``AWS::AutoScaling::AutoScalingGroup.TerminationPolicies``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-termpolicy
        Stability:
            stable
        """
        return jsii.get(self, "terminationPolicies")

    @termination_policies.setter
    def termination_policies(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "terminationPolicies", value)

    @property
    @jsii.member(jsii_name="vpcZoneIdentifier")
    def vpc_zone_identifier(self) -> typing.Optional[typing.List[str]]:
        """``AWS::AutoScaling::AutoScalingGroup.VPCZoneIdentifier``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-vpczoneidentifier
        Stability:
            stable
        """
        return jsii.get(self, "vpcZoneIdentifier")

    @vpc_zone_identifier.setter
    def vpc_zone_identifier(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "vpcZoneIdentifier", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnAutoScalingGroup.InstancesDistributionProperty", jsii_struct_bases=[])
    class InstancesDistributionProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-as-mixedinstancespolicy-instancesdistribution.html
        Stability:
            stable
        """
        onDemandAllocationStrategy: str
        """``CfnAutoScalingGroup.InstancesDistributionProperty.OnDemandAllocationStrategy``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-as-mixedinstancespolicy-instancesdistribution.html#cfn-autoscaling-autoscalinggroup-instancesdistribution-ondemandallocationstrategy
        Stability:
            stable
        """

        onDemandBaseCapacity: jsii.Number
        """``CfnAutoScalingGroup.InstancesDistributionProperty.OnDemandBaseCapacity``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-as-mixedinstancespolicy-instancesdistribution.html#cfn-autoscaling-autoscalinggroup-instancesdistribution-ondemandbasecapacity
        Stability:
            stable
        """

        onDemandPercentageAboveBaseCapacity: jsii.Number
        """``CfnAutoScalingGroup.InstancesDistributionProperty.OnDemandPercentageAboveBaseCapacity``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-as-mixedinstancespolicy-instancesdistribution.html#cfn-autoscaling-autoscalinggroup-instancesdistribution-ondemandpercentageabovebasecapacity
        Stability:
            stable
        """

        spotAllocationStrategy: str
        """``CfnAutoScalingGroup.InstancesDistributionProperty.SpotAllocationStrategy``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-as-mixedinstancespolicy-instancesdistribution.html#cfn-autoscaling-autoscalinggroup-instancesdistribution-spotallocationstrategy
        Stability:
            stable
        """

        spotInstancePools: jsii.Number
        """``CfnAutoScalingGroup.InstancesDistributionProperty.SpotInstancePools``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-as-mixedinstancespolicy-instancesdistribution.html#cfn-autoscaling-autoscalinggroup-instancesdistribution-spotinstancepools
        Stability:
            stable
        """

        spotMaxPrice: str
        """``CfnAutoScalingGroup.InstancesDistributionProperty.SpotMaxPrice``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-as-mixedinstancespolicy-instancesdistribution.html#cfn-autoscaling-autoscalinggroup-instancesdistribution-spotmaxprice
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnAutoScalingGroup.LaunchTemplateOverridesProperty", jsii_struct_bases=[])
    class LaunchTemplateOverridesProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-as-mixedinstancespolicy-launchtemplateoverrides.html
        Stability:
            stable
        """
        instanceType: str
        """``CfnAutoScalingGroup.LaunchTemplateOverridesProperty.InstanceType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-as-mixedinstancespolicy-launchtemplateoverrides.html#cfn-autoscaling-autoscalinggroup-launchtemplateoverrides-instancetype
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _LaunchTemplateProperty(jsii.compat.TypedDict, total=False):
        overrides: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAutoScalingGroup.LaunchTemplateOverridesProperty"]]]
        """``CfnAutoScalingGroup.LaunchTemplateProperty.Overrides``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-as-mixedinstancespolicy-launchtemplate.html#cfn-as-mixedinstancespolicy-overrides
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnAutoScalingGroup.LaunchTemplateProperty", jsii_struct_bases=[_LaunchTemplateProperty])
    class LaunchTemplateProperty(_LaunchTemplateProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-as-mixedinstancespolicy-launchtemplate.html
        Stability:
            stable
        """
        launchTemplateSpecification: typing.Union["CfnAutoScalingGroup.LaunchTemplateSpecificationProperty", aws_cdk.core.IResolvable]
        """``CfnAutoScalingGroup.LaunchTemplateProperty.LaunchTemplateSpecification``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-as-mixedinstancespolicy-launchtemplate.html#cfn-as-group-launchtemplate
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _LaunchTemplateSpecificationProperty(jsii.compat.TypedDict, total=False):
        launchTemplateId: str
        """``CfnAutoScalingGroup.LaunchTemplateSpecificationProperty.LaunchTemplateId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplatespecification.html#cfn-autoscaling-autoscalinggroup-launchtemplatespecification-launchtemplateid
        Stability:
            stable
        """
        launchTemplateName: str
        """``CfnAutoScalingGroup.LaunchTemplateSpecificationProperty.LaunchTemplateName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplatespecification.html#cfn-autoscaling-autoscalinggroup-launchtemplatespecification-launchtemplatename
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnAutoScalingGroup.LaunchTemplateSpecificationProperty", jsii_struct_bases=[_LaunchTemplateSpecificationProperty])
    class LaunchTemplateSpecificationProperty(_LaunchTemplateSpecificationProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplatespecification.html
        Stability:
            stable
        """
        version: str
        """``CfnAutoScalingGroup.LaunchTemplateSpecificationProperty.Version``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-launchtemplatespecification.html#cfn-autoscaling-autoscalinggroup-launchtemplatespecification-version
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _LifecycleHookSpecificationProperty(jsii.compat.TypedDict, total=False):
        defaultResult: str
        """``CfnAutoScalingGroup.LifecycleHookSpecificationProperty.DefaultResult``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-defaultresult
        Stability:
            stable
        """
        heartbeatTimeout: jsii.Number
        """``CfnAutoScalingGroup.LifecycleHookSpecificationProperty.HeartbeatTimeout``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-heartbeattimeout
        Stability:
            stable
        """
        notificationMetadata: str
        """``CfnAutoScalingGroup.LifecycleHookSpecificationProperty.NotificationMetadata``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-notificationmetadata
        Stability:
            stable
        """
        notificationTargetArn: str
        """``CfnAutoScalingGroup.LifecycleHookSpecificationProperty.NotificationTargetARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-notificationtargetarn
        Stability:
            stable
        """
        roleArn: str
        """``CfnAutoScalingGroup.LifecycleHookSpecificationProperty.RoleARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-rolearn
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnAutoScalingGroup.LifecycleHookSpecificationProperty", jsii_struct_bases=[_LifecycleHookSpecificationProperty])
    class LifecycleHookSpecificationProperty(_LifecycleHookSpecificationProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html
        Stability:
            stable
        """
        lifecycleHookName: str
        """``CfnAutoScalingGroup.LifecycleHookSpecificationProperty.LifecycleHookName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-lifecyclehookname
        Stability:
            stable
        """

        lifecycleTransition: str
        """``CfnAutoScalingGroup.LifecycleHookSpecificationProperty.LifecycleTransition``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-autoscalinggroup-lifecyclehookspecification.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecification-lifecycletransition
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _MetricsCollectionProperty(jsii.compat.TypedDict, total=False):
        metrics: typing.List[str]
        """``CfnAutoScalingGroup.MetricsCollectionProperty.Metrics``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-metricscollection.html#cfn-as-metricscollection-metrics
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnAutoScalingGroup.MetricsCollectionProperty", jsii_struct_bases=[_MetricsCollectionProperty])
    class MetricsCollectionProperty(_MetricsCollectionProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-metricscollection.html
        Stability:
            stable
        """
        granularity: str
        """``CfnAutoScalingGroup.MetricsCollectionProperty.Granularity``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-metricscollection.html#cfn-as-metricscollection-granularity
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _MixedInstancesPolicyProperty(jsii.compat.TypedDict, total=False):
        instancesDistribution: typing.Union[aws_cdk.core.IResolvable, "CfnAutoScalingGroup.InstancesDistributionProperty"]
        """``CfnAutoScalingGroup.MixedInstancesPolicyProperty.InstancesDistribution``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-as-group-mixedinstancespolicy.html#cfn-as-mixedinstancespolicy-instancesdistribution
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnAutoScalingGroup.MixedInstancesPolicyProperty", jsii_struct_bases=[_MixedInstancesPolicyProperty])
    class MixedInstancesPolicyProperty(_MixedInstancesPolicyProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-as-group-mixedinstancespolicy.html
        Stability:
            stable
        """
        launchTemplate: typing.Union[aws_cdk.core.IResolvable, "CfnAutoScalingGroup.LaunchTemplateProperty"]
        """``CfnAutoScalingGroup.MixedInstancesPolicyProperty.LaunchTemplate``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-as-group-mixedinstancespolicy.html#cfn-as-mixedinstancespolicy-launchtemplate
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _NotificationConfigurationProperty(jsii.compat.TypedDict, total=False):
        notificationTypes: typing.List[str]
        """``CfnAutoScalingGroup.NotificationConfigurationProperty.NotificationTypes``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-notificationconfigurations.html#cfn-as-group-notificationconfigurations-notificationtypes
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnAutoScalingGroup.NotificationConfigurationProperty", jsii_struct_bases=[_NotificationConfigurationProperty])
    class NotificationConfigurationProperty(_NotificationConfigurationProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-notificationconfigurations.html
        Stability:
            stable
        """
        topicArn: str
        """``CfnAutoScalingGroup.NotificationConfigurationProperty.TopicARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-notificationconfigurations.html#cfn-autoscaling-autoscalinggroup-notificationconfigurations-topicarn
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnAutoScalingGroup.TagPropertyProperty", jsii_struct_bases=[])
    class TagPropertyProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-tags.html
        Stability:
            stable
        """
        key: str
        """``CfnAutoScalingGroup.TagPropertyProperty.Key``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-tags.html#cfn-as-tags-Key
        Stability:
            stable
        """

        propagateAtLaunch: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnAutoScalingGroup.TagPropertyProperty.PropagateAtLaunch``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-tags.html#cfn-as-tags-PropagateAtLaunch
        Stability:
            stable
        """

        value: str
        """``CfnAutoScalingGroup.TagPropertyProperty.Value``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-tags.html#cfn-as-tags-Value
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnAutoScalingGroupProps(jsii.compat.TypedDict, total=False):
    autoScalingGroupName: str
    """``AWS::AutoScaling::AutoScalingGroup.AutoScalingGroupName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-autoscaling-autoscalinggroup-autoscalinggroupname
    Stability:
        stable
    """
    availabilityZones: typing.List[str]
    """``AWS::AutoScaling::AutoScalingGroup.AvailabilityZones``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-availabilityzones
    Stability:
        stable
    """
    cooldown: str
    """``AWS::AutoScaling::AutoScalingGroup.Cooldown``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-cooldown
    Stability:
        stable
    """
    desiredCapacity: str
    """``AWS::AutoScaling::AutoScalingGroup.DesiredCapacity``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-desiredcapacity
    Stability:
        stable
    """
    healthCheckGracePeriod: jsii.Number
    """``AWS::AutoScaling::AutoScalingGroup.HealthCheckGracePeriod``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-healthcheckgraceperiod
    Stability:
        stable
    """
    healthCheckType: str
    """``AWS::AutoScaling::AutoScalingGroup.HealthCheckType``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-healthchecktype
    Stability:
        stable
    """
    instanceId: str
    """``AWS::AutoScaling::AutoScalingGroup.InstanceId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-instanceid
    Stability:
        stable
    """
    launchConfigurationName: str
    """``AWS::AutoScaling::AutoScalingGroup.LaunchConfigurationName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-launchconfigurationname
    Stability:
        stable
    """
    launchTemplate: typing.Union["CfnAutoScalingGroup.LaunchTemplateSpecificationProperty", aws_cdk.core.IResolvable]
    """``AWS::AutoScaling::AutoScalingGroup.LaunchTemplate``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-launchtemplate
    Stability:
        stable
    """
    lifecycleHookSpecificationList: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAutoScalingGroup.LifecycleHookSpecificationProperty"]]]
    """``AWS::AutoScaling::AutoScalingGroup.LifecycleHookSpecificationList``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-autoscaling-autoscalinggroup-lifecyclehookspecificationlist
    Stability:
        stable
    """
    loadBalancerNames: typing.List[str]
    """``AWS::AutoScaling::AutoScalingGroup.LoadBalancerNames``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-loadbalancernames
    Stability:
        stable
    """
    metricsCollection: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAutoScalingGroup.MetricsCollectionProperty"]]]
    """``AWS::AutoScaling::AutoScalingGroup.MetricsCollection``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-metricscollection
    Stability:
        stable
    """
    mixedInstancesPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnAutoScalingGroup.MixedInstancesPolicyProperty"]
    """``AWS::AutoScaling::AutoScalingGroup.MixedInstancesPolicy``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-mixedinstancespolicy
    Stability:
        stable
    """
    notificationConfigurations: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnAutoScalingGroup.NotificationConfigurationProperty"]]]
    """``AWS::AutoScaling::AutoScalingGroup.NotificationConfigurations``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-notificationconfigurations
    Stability:
        stable
    """
    placementGroup: str
    """``AWS::AutoScaling::AutoScalingGroup.PlacementGroup``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-placementgroup
    Stability:
        stable
    """
    serviceLinkedRoleArn: str
    """``AWS::AutoScaling::AutoScalingGroup.ServiceLinkedRoleARN``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-autoscaling-autoscalinggroup-servicelinkedrolearn
    Stability:
        stable
    """
    tags: typing.List["CfnAutoScalingGroup.TagPropertyProperty"]
    """``AWS::AutoScaling::AutoScalingGroup.Tags``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-tags
    Stability:
        stable
    """
    targetGroupArns: typing.List[str]
    """``AWS::AutoScaling::AutoScalingGroup.TargetGroupARNs``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-targetgrouparns
    Stability:
        stable
    """
    terminationPolicies: typing.List[str]
    """``AWS::AutoScaling::AutoScalingGroup.TerminationPolicies``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-termpolicy
    Stability:
        stable
    """
    vpcZoneIdentifier: typing.List[str]
    """``AWS::AutoScaling::AutoScalingGroup.VPCZoneIdentifier``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-vpczoneidentifier
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnAutoScalingGroupProps", jsii_struct_bases=[_CfnAutoScalingGroupProps])
class CfnAutoScalingGroupProps(_CfnAutoScalingGroupProps):
    """Properties for defining a ``AWS::AutoScaling::AutoScalingGroup``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html
    Stability:
        stable
    """
    maxSize: str
    """``AWS::AutoScaling::AutoScalingGroup.MaxSize``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-maxsize
    Stability:
        stable
    """

    minSize: str
    """``AWS::AutoScaling::AutoScalingGroup.MinSize``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html#cfn-as-group-minsize
    Stability:
        stable
    """

class CfnLaunchConfiguration(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-autoscaling.CfnLaunchConfiguration"):
    """A CloudFormation ``AWS::AutoScaling::LaunchConfiguration``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html
    Stability:
        stable
    cloudformationResource:
        AWS::AutoScaling::LaunchConfiguration
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, image_id: str, instance_type: str, associate_public_ip_address: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, block_device_mappings: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "BlockDeviceMappingProperty"]]]]]=None, classic_link_vpc_id: typing.Optional[str]=None, classic_link_vpc_security_groups: typing.Optional[typing.List[str]]=None, ebs_optimized: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, iam_instance_profile: typing.Optional[str]=None, instance_id: typing.Optional[str]=None, instance_monitoring: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, kernel_id: typing.Optional[str]=None, key_name: typing.Optional[str]=None, launch_configuration_name: typing.Optional[str]=None, placement_tenancy: typing.Optional[str]=None, ram_disk_id: typing.Optional[str]=None, security_groups: typing.Optional[typing.List[str]]=None, spot_price: typing.Optional[str]=None, user_data: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::AutoScaling::LaunchConfiguration``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            image_id: ``AWS::AutoScaling::LaunchConfiguration.ImageId``.
            instance_type: ``AWS::AutoScaling::LaunchConfiguration.InstanceType``.
            associate_public_ip_address: ``AWS::AutoScaling::LaunchConfiguration.AssociatePublicIpAddress``.
            block_device_mappings: ``AWS::AutoScaling::LaunchConfiguration.BlockDeviceMappings``.
            classic_link_vpc_id: ``AWS::AutoScaling::LaunchConfiguration.ClassicLinkVPCId``.
            classic_link_vpc_security_groups: ``AWS::AutoScaling::LaunchConfiguration.ClassicLinkVPCSecurityGroups``.
            ebs_optimized: ``AWS::AutoScaling::LaunchConfiguration.EbsOptimized``.
            iam_instance_profile: ``AWS::AutoScaling::LaunchConfiguration.IamInstanceProfile``.
            instance_id: ``AWS::AutoScaling::LaunchConfiguration.InstanceId``.
            instance_monitoring: ``AWS::AutoScaling::LaunchConfiguration.InstanceMonitoring``.
            kernel_id: ``AWS::AutoScaling::LaunchConfiguration.KernelId``.
            key_name: ``AWS::AutoScaling::LaunchConfiguration.KeyName``.
            launch_configuration_name: ``AWS::AutoScaling::LaunchConfiguration.LaunchConfigurationName``.
            placement_tenancy: ``AWS::AutoScaling::LaunchConfiguration.PlacementTenancy``.
            ram_disk_id: ``AWS::AutoScaling::LaunchConfiguration.RamDiskId``.
            security_groups: ``AWS::AutoScaling::LaunchConfiguration.SecurityGroups``.
            spot_price: ``AWS::AutoScaling::LaunchConfiguration.SpotPrice``.
            user_data: ``AWS::AutoScaling::LaunchConfiguration.UserData``.

        Stability:
            experimental
        """
        props: CfnLaunchConfigurationProps = {"imageId": image_id, "instanceType": instance_type}

        if associate_public_ip_address is not None:
            props["associatePublicIpAddress"] = associate_public_ip_address

        if block_device_mappings is not None:
            props["blockDeviceMappings"] = block_device_mappings

        if classic_link_vpc_id is not None:
            props["classicLinkVpcId"] = classic_link_vpc_id

        if classic_link_vpc_security_groups is not None:
            props["classicLinkVpcSecurityGroups"] = classic_link_vpc_security_groups

        if ebs_optimized is not None:
            props["ebsOptimized"] = ebs_optimized

        if iam_instance_profile is not None:
            props["iamInstanceProfile"] = iam_instance_profile

        if instance_id is not None:
            props["instanceId"] = instance_id

        if instance_monitoring is not None:
            props["instanceMonitoring"] = instance_monitoring

        if kernel_id is not None:
            props["kernelId"] = kernel_id

        if key_name is not None:
            props["keyName"] = key_name

        if launch_configuration_name is not None:
            props["launchConfigurationName"] = launch_configuration_name

        if placement_tenancy is not None:
            props["placementTenancy"] = placement_tenancy

        if ram_disk_id is not None:
            props["ramDiskId"] = ram_disk_id

        if security_groups is not None:
            props["securityGroups"] = security_groups

        if spot_price is not None:
            props["spotPrice"] = spot_price

        if user_data is not None:
            props["userData"] = user_data

        jsii.create(CfnLaunchConfiguration, self, [scope, id, props])

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
    @jsii.member(jsii_name="imageId")
    def image_id(self) -> str:
        """``AWS::AutoScaling::LaunchConfiguration.ImageId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-imageid
        Stability:
            stable
        """
        return jsii.get(self, "imageId")

    @image_id.setter
    def image_id(self, value: str):
        return jsii.set(self, "imageId", value)

    @property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> str:
        """``AWS::AutoScaling::LaunchConfiguration.InstanceType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-instancetype
        Stability:
            stable
        """
        return jsii.get(self, "instanceType")

    @instance_type.setter
    def instance_type(self, value: str):
        return jsii.set(self, "instanceType", value)

    @property
    @jsii.member(jsii_name="associatePublicIpAddress")
    def associate_public_ip_address(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::AutoScaling::LaunchConfiguration.AssociatePublicIpAddress``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cf-as-launchconfig-associatepubip
        Stability:
            stable
        """
        return jsii.get(self, "associatePublicIpAddress")

    @associate_public_ip_address.setter
    def associate_public_ip_address(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "associatePublicIpAddress", value)

    @property
    @jsii.member(jsii_name="blockDeviceMappings")
    def block_device_mappings(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "BlockDeviceMappingProperty"]]]]]:
        """``AWS::AutoScaling::LaunchConfiguration.BlockDeviceMappings``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-blockdevicemappings
        Stability:
            stable
        """
        return jsii.get(self, "blockDeviceMappings")

    @block_device_mappings.setter
    def block_device_mappings(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "BlockDeviceMappingProperty"]]]]]):
        return jsii.set(self, "blockDeviceMappings", value)

    @property
    @jsii.member(jsii_name="classicLinkVpcId")
    def classic_link_vpc_id(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::LaunchConfiguration.ClassicLinkVPCId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-classiclinkvpcid
        Stability:
            stable
        """
        return jsii.get(self, "classicLinkVpcId")

    @classic_link_vpc_id.setter
    def classic_link_vpc_id(self, value: typing.Optional[str]):
        return jsii.set(self, "classicLinkVpcId", value)

    @property
    @jsii.member(jsii_name="classicLinkVpcSecurityGroups")
    def classic_link_vpc_security_groups(self) -> typing.Optional[typing.List[str]]:
        """``AWS::AutoScaling::LaunchConfiguration.ClassicLinkVPCSecurityGroups``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-classiclinkvpcsecuritygroups
        Stability:
            stable
        """
        return jsii.get(self, "classicLinkVpcSecurityGroups")

    @classic_link_vpc_security_groups.setter
    def classic_link_vpc_security_groups(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "classicLinkVpcSecurityGroups", value)

    @property
    @jsii.member(jsii_name="ebsOptimized")
    def ebs_optimized(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::AutoScaling::LaunchConfiguration.EbsOptimized``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-ebsoptimized
        Stability:
            stable
        """
        return jsii.get(self, "ebsOptimized")

    @ebs_optimized.setter
    def ebs_optimized(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "ebsOptimized", value)

    @property
    @jsii.member(jsii_name="iamInstanceProfile")
    def iam_instance_profile(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::LaunchConfiguration.IamInstanceProfile``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-iaminstanceprofile
        Stability:
            stable
        """
        return jsii.get(self, "iamInstanceProfile")

    @iam_instance_profile.setter
    def iam_instance_profile(self, value: typing.Optional[str]):
        return jsii.set(self, "iamInstanceProfile", value)

    @property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::LaunchConfiguration.InstanceId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-instanceid
        Stability:
            stable
        """
        return jsii.get(self, "instanceId")

    @instance_id.setter
    def instance_id(self, value: typing.Optional[str]):
        return jsii.set(self, "instanceId", value)

    @property
    @jsii.member(jsii_name="instanceMonitoring")
    def instance_monitoring(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::AutoScaling::LaunchConfiguration.InstanceMonitoring``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-instancemonitoring
        Stability:
            stable
        """
        return jsii.get(self, "instanceMonitoring")

    @instance_monitoring.setter
    def instance_monitoring(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "instanceMonitoring", value)

    @property
    @jsii.member(jsii_name="kernelId")
    def kernel_id(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::LaunchConfiguration.KernelId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-kernelid
        Stability:
            stable
        """
        return jsii.get(self, "kernelId")

    @kernel_id.setter
    def kernel_id(self, value: typing.Optional[str]):
        return jsii.set(self, "kernelId", value)

    @property
    @jsii.member(jsii_name="keyName")
    def key_name(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::LaunchConfiguration.KeyName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-keyname
        Stability:
            stable
        """
        return jsii.get(self, "keyName")

    @key_name.setter
    def key_name(self, value: typing.Optional[str]):
        return jsii.set(self, "keyName", value)

    @property
    @jsii.member(jsii_name="launchConfigurationName")
    def launch_configuration_name(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::LaunchConfiguration.LaunchConfigurationName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-autoscaling-launchconfig-launchconfigurationname
        Stability:
            stable
        """
        return jsii.get(self, "launchConfigurationName")

    @launch_configuration_name.setter
    def launch_configuration_name(self, value: typing.Optional[str]):
        return jsii.set(self, "launchConfigurationName", value)

    @property
    @jsii.member(jsii_name="placementTenancy")
    def placement_tenancy(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::LaunchConfiguration.PlacementTenancy``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-placementtenancy
        Stability:
            stable
        """
        return jsii.get(self, "placementTenancy")

    @placement_tenancy.setter
    def placement_tenancy(self, value: typing.Optional[str]):
        return jsii.set(self, "placementTenancy", value)

    @property
    @jsii.member(jsii_name="ramDiskId")
    def ram_disk_id(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::LaunchConfiguration.RamDiskId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-ramdiskid
        Stability:
            stable
        """
        return jsii.get(self, "ramDiskId")

    @ram_disk_id.setter
    def ram_disk_id(self, value: typing.Optional[str]):
        return jsii.set(self, "ramDiskId", value)

    @property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.Optional[typing.List[str]]:
        """``AWS::AutoScaling::LaunchConfiguration.SecurityGroups``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-securitygroups
        Stability:
            stable
        """
        return jsii.get(self, "securityGroups")

    @security_groups.setter
    def security_groups(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "securityGroups", value)

    @property
    @jsii.member(jsii_name="spotPrice")
    def spot_price(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::LaunchConfiguration.SpotPrice``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-spotprice
        Stability:
            stable
        """
        return jsii.get(self, "spotPrice")

    @spot_price.setter
    def spot_price(self, value: typing.Optional[str]):
        return jsii.set(self, "spotPrice", value)

    @property
    @jsii.member(jsii_name="userData")
    def user_data(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::LaunchConfiguration.UserData``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-userdata
        Stability:
            stable
        """
        return jsii.get(self, "userData")

    @user_data.setter
    def user_data(self, value: typing.Optional[str]):
        return jsii.set(self, "userData", value)

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _BlockDeviceMappingProperty(jsii.compat.TypedDict, total=False):
        ebs: typing.Union[aws_cdk.core.IResolvable, "CfnLaunchConfiguration.BlockDeviceProperty"]
        """``CfnLaunchConfiguration.BlockDeviceMappingProperty.Ebs``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig-blockdev-mapping.html#cfn-as-launchconfig-blockdev-mapping-ebs
        Stability:
            stable
        """
        noDevice: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnLaunchConfiguration.BlockDeviceMappingProperty.NoDevice``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig-blockdev-mapping.html#cfn-as-launchconfig-blockdev-mapping-nodevice
        Stability:
            stable
        """
        virtualName: str
        """``CfnLaunchConfiguration.BlockDeviceMappingProperty.VirtualName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig-blockdev-mapping.html#cfn-as-launchconfig-blockdev-mapping-virtualname
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnLaunchConfiguration.BlockDeviceMappingProperty", jsii_struct_bases=[_BlockDeviceMappingProperty])
    class BlockDeviceMappingProperty(_BlockDeviceMappingProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig-blockdev-mapping.html
        Stability:
            stable
        """
        deviceName: str
        """``CfnLaunchConfiguration.BlockDeviceMappingProperty.DeviceName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig-blockdev-mapping.html#cfn-as-launchconfig-blockdev-mapping-devicename
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnLaunchConfiguration.BlockDeviceProperty", jsii_struct_bases=[])
    class BlockDeviceProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig-blockdev-template.html
        Stability:
            stable
        """
        deleteOnTermination: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnLaunchConfiguration.BlockDeviceProperty.DeleteOnTermination``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig-blockdev-template.html#cfn-as-launchconfig-blockdev-template-deleteonterm
        Stability:
            stable
        """

        encrypted: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnLaunchConfiguration.BlockDeviceProperty.Encrypted``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig-blockdev-template.html#cfn-as-launchconfig-blockdev-template-encrypted
        Stability:
            stable
        """

        iops: jsii.Number
        """``CfnLaunchConfiguration.BlockDeviceProperty.Iops``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig-blockdev-template.html#cfn-as-launchconfig-blockdev-template-iops
        Stability:
            stable
        """

        snapshotId: str
        """``CfnLaunchConfiguration.BlockDeviceProperty.SnapshotId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig-blockdev-template.html#cfn-as-launchconfig-blockdev-template-snapshotid
        Stability:
            stable
        """

        volumeSize: jsii.Number
        """``CfnLaunchConfiguration.BlockDeviceProperty.VolumeSize``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig-blockdev-template.html#cfn-as-launchconfig-blockdev-template-volumesize
        Stability:
            stable
        """

        volumeType: str
        """``CfnLaunchConfiguration.BlockDeviceProperty.VolumeType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig-blockdev-template.html#cfn-as-launchconfig-blockdev-template-volumetype
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnLaunchConfigurationProps(jsii.compat.TypedDict, total=False):
    associatePublicIpAddress: typing.Union[bool, aws_cdk.core.IResolvable]
    """``AWS::AutoScaling::LaunchConfiguration.AssociatePublicIpAddress``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cf-as-launchconfig-associatepubip
    Stability:
        stable
    """
    blockDeviceMappings: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLaunchConfiguration.BlockDeviceMappingProperty"]]]
    """``AWS::AutoScaling::LaunchConfiguration.BlockDeviceMappings``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-blockdevicemappings
    Stability:
        stable
    """
    classicLinkVpcId: str
    """``AWS::AutoScaling::LaunchConfiguration.ClassicLinkVPCId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-classiclinkvpcid
    Stability:
        stable
    """
    classicLinkVpcSecurityGroups: typing.List[str]
    """``AWS::AutoScaling::LaunchConfiguration.ClassicLinkVPCSecurityGroups``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-classiclinkvpcsecuritygroups
    Stability:
        stable
    """
    ebsOptimized: typing.Union[bool, aws_cdk.core.IResolvable]
    """``AWS::AutoScaling::LaunchConfiguration.EbsOptimized``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-ebsoptimized
    Stability:
        stable
    """
    iamInstanceProfile: str
    """``AWS::AutoScaling::LaunchConfiguration.IamInstanceProfile``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-iaminstanceprofile
    Stability:
        stable
    """
    instanceId: str
    """``AWS::AutoScaling::LaunchConfiguration.InstanceId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-instanceid
    Stability:
        stable
    """
    instanceMonitoring: typing.Union[bool, aws_cdk.core.IResolvable]
    """``AWS::AutoScaling::LaunchConfiguration.InstanceMonitoring``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-instancemonitoring
    Stability:
        stable
    """
    kernelId: str
    """``AWS::AutoScaling::LaunchConfiguration.KernelId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-kernelid
    Stability:
        stable
    """
    keyName: str
    """``AWS::AutoScaling::LaunchConfiguration.KeyName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-keyname
    Stability:
        stable
    """
    launchConfigurationName: str
    """``AWS::AutoScaling::LaunchConfiguration.LaunchConfigurationName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-autoscaling-launchconfig-launchconfigurationname
    Stability:
        stable
    """
    placementTenancy: str
    """``AWS::AutoScaling::LaunchConfiguration.PlacementTenancy``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-placementtenancy
    Stability:
        stable
    """
    ramDiskId: str
    """``AWS::AutoScaling::LaunchConfiguration.RamDiskId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-ramdiskid
    Stability:
        stable
    """
    securityGroups: typing.List[str]
    """``AWS::AutoScaling::LaunchConfiguration.SecurityGroups``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-securitygroups
    Stability:
        stable
    """
    spotPrice: str
    """``AWS::AutoScaling::LaunchConfiguration.SpotPrice``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-spotprice
    Stability:
        stable
    """
    userData: str
    """``AWS::AutoScaling::LaunchConfiguration.UserData``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-userdata
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnLaunchConfigurationProps", jsii_struct_bases=[_CfnLaunchConfigurationProps])
class CfnLaunchConfigurationProps(_CfnLaunchConfigurationProps):
    """Properties for defining a ``AWS::AutoScaling::LaunchConfiguration``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html
    Stability:
        stable
    """
    imageId: str
    """``AWS::AutoScaling::LaunchConfiguration.ImageId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-imageid
    Stability:
        stable
    """

    instanceType: str
    """``AWS::AutoScaling::LaunchConfiguration.InstanceType``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html#cfn-as-launchconfig-instancetype
    Stability:
        stable
    """

class CfnLifecycleHook(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-autoscaling.CfnLifecycleHook"):
    """A CloudFormation ``AWS::AutoScaling::LifecycleHook``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html
    Stability:
        stable
    cloudformationResource:
        AWS::AutoScaling::LifecycleHook
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, auto_scaling_group_name: str, lifecycle_transition: str, default_result: typing.Optional[str]=None, heartbeat_timeout: typing.Optional[jsii.Number]=None, lifecycle_hook_name: typing.Optional[str]=None, notification_metadata: typing.Optional[str]=None, notification_target_arn: typing.Optional[str]=None, role_arn: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::AutoScaling::LifecycleHook``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            auto_scaling_group_name: ``AWS::AutoScaling::LifecycleHook.AutoScalingGroupName``.
            lifecycle_transition: ``AWS::AutoScaling::LifecycleHook.LifecycleTransition``.
            default_result: ``AWS::AutoScaling::LifecycleHook.DefaultResult``.
            heartbeat_timeout: ``AWS::AutoScaling::LifecycleHook.HeartbeatTimeout``.
            lifecycle_hook_name: ``AWS::AutoScaling::LifecycleHook.LifecycleHookName``.
            notification_metadata: ``AWS::AutoScaling::LifecycleHook.NotificationMetadata``.
            notification_target_arn: ``AWS::AutoScaling::LifecycleHook.NotificationTargetARN``.
            role_arn: ``AWS::AutoScaling::LifecycleHook.RoleARN``.

        Stability:
            experimental
        """
        props: CfnLifecycleHookProps = {"autoScalingGroupName": auto_scaling_group_name, "lifecycleTransition": lifecycle_transition}

        if default_result is not None:
            props["defaultResult"] = default_result

        if heartbeat_timeout is not None:
            props["heartbeatTimeout"] = heartbeat_timeout

        if lifecycle_hook_name is not None:
            props["lifecycleHookName"] = lifecycle_hook_name

        if notification_metadata is not None:
            props["notificationMetadata"] = notification_metadata

        if notification_target_arn is not None:
            props["notificationTargetArn"] = notification_target_arn

        if role_arn is not None:
            props["roleArn"] = role_arn

        jsii.create(CfnLifecycleHook, self, [scope, id, props])

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
    @jsii.member(jsii_name="autoScalingGroupName")
    def auto_scaling_group_name(self) -> str:
        """``AWS::AutoScaling::LifecycleHook.AutoScalingGroupName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html#cfn-as-lifecyclehook-autoscalinggroupname
        Stability:
            stable
        """
        return jsii.get(self, "autoScalingGroupName")

    @auto_scaling_group_name.setter
    def auto_scaling_group_name(self, value: str):
        return jsii.set(self, "autoScalingGroupName", value)

    @property
    @jsii.member(jsii_name="lifecycleTransition")
    def lifecycle_transition(self) -> str:
        """``AWS::AutoScaling::LifecycleHook.LifecycleTransition``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html#cfn-as-lifecyclehook-lifecycletransition
        Stability:
            stable
        """
        return jsii.get(self, "lifecycleTransition")

    @lifecycle_transition.setter
    def lifecycle_transition(self, value: str):
        return jsii.set(self, "lifecycleTransition", value)

    @property
    @jsii.member(jsii_name="defaultResult")
    def default_result(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::LifecycleHook.DefaultResult``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html#cfn-as-lifecyclehook-defaultresult
        Stability:
            stable
        """
        return jsii.get(self, "defaultResult")

    @default_result.setter
    def default_result(self, value: typing.Optional[str]):
        return jsii.set(self, "defaultResult", value)

    @property
    @jsii.member(jsii_name="heartbeatTimeout")
    def heartbeat_timeout(self) -> typing.Optional[jsii.Number]:
        """``AWS::AutoScaling::LifecycleHook.HeartbeatTimeout``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html#cfn-as-lifecyclehook-heartbeattimeout
        Stability:
            stable
        """
        return jsii.get(self, "heartbeatTimeout")

    @heartbeat_timeout.setter
    def heartbeat_timeout(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "heartbeatTimeout", value)

    @property
    @jsii.member(jsii_name="lifecycleHookName")
    def lifecycle_hook_name(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::LifecycleHook.LifecycleHookName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html#cfn-autoscaling-lifecyclehook-lifecyclehookname
        Stability:
            stable
        """
        return jsii.get(self, "lifecycleHookName")

    @lifecycle_hook_name.setter
    def lifecycle_hook_name(self, value: typing.Optional[str]):
        return jsii.set(self, "lifecycleHookName", value)

    @property
    @jsii.member(jsii_name="notificationMetadata")
    def notification_metadata(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::LifecycleHook.NotificationMetadata``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html#cfn-as-lifecyclehook-notificationmetadata
        Stability:
            stable
        """
        return jsii.get(self, "notificationMetadata")

    @notification_metadata.setter
    def notification_metadata(self, value: typing.Optional[str]):
        return jsii.set(self, "notificationMetadata", value)

    @property
    @jsii.member(jsii_name="notificationTargetArn")
    def notification_target_arn(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::LifecycleHook.NotificationTargetARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html#cfn-as-lifecyclehook-notificationtargetarn
        Stability:
            stable
        """
        return jsii.get(self, "notificationTargetArn")

    @notification_target_arn.setter
    def notification_target_arn(self, value: typing.Optional[str]):
        return jsii.set(self, "notificationTargetArn", value)

    @property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::LifecycleHook.RoleARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html#cfn-as-lifecyclehook-rolearn
        Stability:
            stable
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter
    def role_arn(self, value: typing.Optional[str]):
        return jsii.set(self, "roleArn", value)


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnLifecycleHookProps(jsii.compat.TypedDict, total=False):
    defaultResult: str
    """``AWS::AutoScaling::LifecycleHook.DefaultResult``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html#cfn-as-lifecyclehook-defaultresult
    Stability:
        stable
    """
    heartbeatTimeout: jsii.Number
    """``AWS::AutoScaling::LifecycleHook.HeartbeatTimeout``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html#cfn-as-lifecyclehook-heartbeattimeout
    Stability:
        stable
    """
    lifecycleHookName: str
    """``AWS::AutoScaling::LifecycleHook.LifecycleHookName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html#cfn-autoscaling-lifecyclehook-lifecyclehookname
    Stability:
        stable
    """
    notificationMetadata: str
    """``AWS::AutoScaling::LifecycleHook.NotificationMetadata``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html#cfn-as-lifecyclehook-notificationmetadata
    Stability:
        stable
    """
    notificationTargetArn: str
    """``AWS::AutoScaling::LifecycleHook.NotificationTargetARN``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html#cfn-as-lifecyclehook-notificationtargetarn
    Stability:
        stable
    """
    roleArn: str
    """``AWS::AutoScaling::LifecycleHook.RoleARN``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html#cfn-as-lifecyclehook-rolearn
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnLifecycleHookProps", jsii_struct_bases=[_CfnLifecycleHookProps])
class CfnLifecycleHookProps(_CfnLifecycleHookProps):
    """Properties for defining a ``AWS::AutoScaling::LifecycleHook``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html
    Stability:
        stable
    """
    autoScalingGroupName: str
    """``AWS::AutoScaling::LifecycleHook.AutoScalingGroupName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html#cfn-as-lifecyclehook-autoscalinggroupname
    Stability:
        stable
    """

    lifecycleTransition: str
    """``AWS::AutoScaling::LifecycleHook.LifecycleTransition``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html#cfn-as-lifecyclehook-lifecycletransition
    Stability:
        stable
    """

class CfnScalingPolicy(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-autoscaling.CfnScalingPolicy"):
    """A CloudFormation ``AWS::AutoScaling::ScalingPolicy``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html
    Stability:
        stable
    cloudformationResource:
        AWS::AutoScaling::ScalingPolicy
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, auto_scaling_group_name: str, adjustment_type: typing.Optional[str]=None, cooldown: typing.Optional[str]=None, estimated_instance_warmup: typing.Optional[jsii.Number]=None, metric_aggregation_type: typing.Optional[str]=None, min_adjustment_magnitude: typing.Optional[jsii.Number]=None, policy_type: typing.Optional[str]=None, scaling_adjustment: typing.Optional[jsii.Number]=None, step_adjustments: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "StepAdjustmentProperty"]]]]]=None, target_tracking_configuration: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["TargetTrackingConfigurationProperty"]]]=None) -> None:
        """Create a new ``AWS::AutoScaling::ScalingPolicy``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            auto_scaling_group_name: ``AWS::AutoScaling::ScalingPolicy.AutoScalingGroupName``.
            adjustment_type: ``AWS::AutoScaling::ScalingPolicy.AdjustmentType``.
            cooldown: ``AWS::AutoScaling::ScalingPolicy.Cooldown``.
            estimated_instance_warmup: ``AWS::AutoScaling::ScalingPolicy.EstimatedInstanceWarmup``.
            metric_aggregation_type: ``AWS::AutoScaling::ScalingPolicy.MetricAggregationType``.
            min_adjustment_magnitude: ``AWS::AutoScaling::ScalingPolicy.MinAdjustmentMagnitude``.
            policy_type: ``AWS::AutoScaling::ScalingPolicy.PolicyType``.
            scaling_adjustment: ``AWS::AutoScaling::ScalingPolicy.ScalingAdjustment``.
            step_adjustments: ``AWS::AutoScaling::ScalingPolicy.StepAdjustments``.
            target_tracking_configuration: ``AWS::AutoScaling::ScalingPolicy.TargetTrackingConfiguration``.

        Stability:
            experimental
        """
        props: CfnScalingPolicyProps = {"autoScalingGroupName": auto_scaling_group_name}

        if adjustment_type is not None:
            props["adjustmentType"] = adjustment_type

        if cooldown is not None:
            props["cooldown"] = cooldown

        if estimated_instance_warmup is not None:
            props["estimatedInstanceWarmup"] = estimated_instance_warmup

        if metric_aggregation_type is not None:
            props["metricAggregationType"] = metric_aggregation_type

        if min_adjustment_magnitude is not None:
            props["minAdjustmentMagnitude"] = min_adjustment_magnitude

        if policy_type is not None:
            props["policyType"] = policy_type

        if scaling_adjustment is not None:
            props["scalingAdjustment"] = scaling_adjustment

        if step_adjustments is not None:
            props["stepAdjustments"] = step_adjustments

        if target_tracking_configuration is not None:
            props["targetTrackingConfiguration"] = target_tracking_configuration

        jsii.create(CfnScalingPolicy, self, [scope, id, props])

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
    @jsii.member(jsii_name="autoScalingGroupName")
    def auto_scaling_group_name(self) -> str:
        """``AWS::AutoScaling::ScalingPolicy.AutoScalingGroupName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html#cfn-as-scalingpolicy-autoscalinggroupname
        Stability:
            stable
        """
        return jsii.get(self, "autoScalingGroupName")

    @auto_scaling_group_name.setter
    def auto_scaling_group_name(self, value: str):
        return jsii.set(self, "autoScalingGroupName", value)

    @property
    @jsii.member(jsii_name="adjustmentType")
    def adjustment_type(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::ScalingPolicy.AdjustmentType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html#cfn-as-scalingpolicy-adjustmenttype
        Stability:
            stable
        """
        return jsii.get(self, "adjustmentType")

    @adjustment_type.setter
    def adjustment_type(self, value: typing.Optional[str]):
        return jsii.set(self, "adjustmentType", value)

    @property
    @jsii.member(jsii_name="cooldown")
    def cooldown(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::ScalingPolicy.Cooldown``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html#cfn-as-scalingpolicy-cooldown
        Stability:
            stable
        """
        return jsii.get(self, "cooldown")

    @cooldown.setter
    def cooldown(self, value: typing.Optional[str]):
        return jsii.set(self, "cooldown", value)

    @property
    @jsii.member(jsii_name="estimatedInstanceWarmup")
    def estimated_instance_warmup(self) -> typing.Optional[jsii.Number]:
        """``AWS::AutoScaling::ScalingPolicy.EstimatedInstanceWarmup``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html#cfn-as-scalingpolicy-estimatedinstancewarmup
        Stability:
            stable
        """
        return jsii.get(self, "estimatedInstanceWarmup")

    @estimated_instance_warmup.setter
    def estimated_instance_warmup(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "estimatedInstanceWarmup", value)

    @property
    @jsii.member(jsii_name="metricAggregationType")
    def metric_aggregation_type(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::ScalingPolicy.MetricAggregationType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html#cfn-as-scalingpolicy-metricaggregationtype
        Stability:
            stable
        """
        return jsii.get(self, "metricAggregationType")

    @metric_aggregation_type.setter
    def metric_aggregation_type(self, value: typing.Optional[str]):
        return jsii.set(self, "metricAggregationType", value)

    @property
    @jsii.member(jsii_name="minAdjustmentMagnitude")
    def min_adjustment_magnitude(self) -> typing.Optional[jsii.Number]:
        """``AWS::AutoScaling::ScalingPolicy.MinAdjustmentMagnitude``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html#cfn-as-scalingpolicy-minadjustmentmagnitude
        Stability:
            stable
        """
        return jsii.get(self, "minAdjustmentMagnitude")

    @min_adjustment_magnitude.setter
    def min_adjustment_magnitude(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "minAdjustmentMagnitude", value)

    @property
    @jsii.member(jsii_name="policyType")
    def policy_type(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::ScalingPolicy.PolicyType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html#cfn-as-scalingpolicy-policytype
        Stability:
            stable
        """
        return jsii.get(self, "policyType")

    @policy_type.setter
    def policy_type(self, value: typing.Optional[str]):
        return jsii.set(self, "policyType", value)

    @property
    @jsii.member(jsii_name="scalingAdjustment")
    def scaling_adjustment(self) -> typing.Optional[jsii.Number]:
        """``AWS::AutoScaling::ScalingPolicy.ScalingAdjustment``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html#cfn-as-scalingpolicy-scalingadjustment
        Stability:
            stable
        """
        return jsii.get(self, "scalingAdjustment")

    @scaling_adjustment.setter
    def scaling_adjustment(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "scalingAdjustment", value)

    @property
    @jsii.member(jsii_name="stepAdjustments")
    def step_adjustments(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "StepAdjustmentProperty"]]]]]:
        """``AWS::AutoScaling::ScalingPolicy.StepAdjustments``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html#cfn-as-scalingpolicy-stepadjustments
        Stability:
            stable
        """
        return jsii.get(self, "stepAdjustments")

    @step_adjustments.setter
    def step_adjustments(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "StepAdjustmentProperty"]]]]]):
        return jsii.set(self, "stepAdjustments", value)

    @property
    @jsii.member(jsii_name="targetTrackingConfiguration")
    def target_tracking_configuration(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["TargetTrackingConfigurationProperty"]]]:
        """``AWS::AutoScaling::ScalingPolicy.TargetTrackingConfiguration``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html#cfn-autoscaling-scalingpolicy-targettrackingconfiguration
        Stability:
            stable
        """
        return jsii.get(self, "targetTrackingConfiguration")

    @target_tracking_configuration.setter
    def target_tracking_configuration(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["TargetTrackingConfigurationProperty"]]]):
        return jsii.set(self, "targetTrackingConfiguration", value)

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _CustomizedMetricSpecificationProperty(jsii.compat.TypedDict, total=False):
        dimensions: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPolicy.MetricDimensionProperty"]]]
        """``CfnScalingPolicy.CustomizedMetricSpecificationProperty.Dimensions``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.html#cfn-autoscaling-scalingpolicy-customizedmetricspecification-dimensions
        Stability:
            stable
        """
        unit: str
        """``CfnScalingPolicy.CustomizedMetricSpecificationProperty.Unit``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.html#cfn-autoscaling-scalingpolicy-customizedmetricspecification-unit
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnScalingPolicy.CustomizedMetricSpecificationProperty", jsii_struct_bases=[_CustomizedMetricSpecificationProperty])
    class CustomizedMetricSpecificationProperty(_CustomizedMetricSpecificationProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.html
        Stability:
            stable
        """
        metricName: str
        """``CfnScalingPolicy.CustomizedMetricSpecificationProperty.MetricName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.html#cfn-autoscaling-scalingpolicy-customizedmetricspecification-metricname
        Stability:
            stable
        """

        namespace: str
        """``CfnScalingPolicy.CustomizedMetricSpecificationProperty.Namespace``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.html#cfn-autoscaling-scalingpolicy-customizedmetricspecification-namespace
        Stability:
            stable
        """

        statistic: str
        """``CfnScalingPolicy.CustomizedMetricSpecificationProperty.Statistic``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.html#cfn-autoscaling-scalingpolicy-customizedmetricspecification-statistic
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnScalingPolicy.MetricDimensionProperty", jsii_struct_bases=[])
    class MetricDimensionProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metricdimension.html
        Stability:
            stable
        """
        name: str
        """``CfnScalingPolicy.MetricDimensionProperty.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metricdimension.html#cfn-autoscaling-scalingpolicy-metricdimension-name
        Stability:
            stable
        """

        value: str
        """``CfnScalingPolicy.MetricDimensionProperty.Value``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-metricdimension.html#cfn-autoscaling-scalingpolicy-metricdimension-value
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _PredefinedMetricSpecificationProperty(jsii.compat.TypedDict, total=False):
        resourceLabel: str
        """``CfnScalingPolicy.PredefinedMetricSpecificationProperty.ResourceLabel``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predefinedmetricspecification.html#cfn-autoscaling-scalingpolicy-predefinedmetricspecification-resourcelabel
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnScalingPolicy.PredefinedMetricSpecificationProperty", jsii_struct_bases=[_PredefinedMetricSpecificationProperty])
    class PredefinedMetricSpecificationProperty(_PredefinedMetricSpecificationProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predefinedmetricspecification.html
        Stability:
            stable
        """
        predefinedMetricType: str
        """``CfnScalingPolicy.PredefinedMetricSpecificationProperty.PredefinedMetricType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predefinedmetricspecification.html#cfn-autoscaling-scalingpolicy-predefinedmetricspecification-predefinedmetrictype
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _StepAdjustmentProperty(jsii.compat.TypedDict, total=False):
        metricIntervalLowerBound: jsii.Number
        """``CfnScalingPolicy.StepAdjustmentProperty.MetricIntervalLowerBound``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-stepadjustments.html#cfn-autoscaling-scalingpolicy-stepadjustment-metricintervallowerbound
        Stability:
            stable
        """
        metricIntervalUpperBound: jsii.Number
        """``CfnScalingPolicy.StepAdjustmentProperty.MetricIntervalUpperBound``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-stepadjustments.html#cfn-autoscaling-scalingpolicy-stepadjustment-metricintervalupperbound
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnScalingPolicy.StepAdjustmentProperty", jsii_struct_bases=[_StepAdjustmentProperty])
    class StepAdjustmentProperty(_StepAdjustmentProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-stepadjustments.html
        Stability:
            stable
        """
        scalingAdjustment: jsii.Number
        """``CfnScalingPolicy.StepAdjustmentProperty.ScalingAdjustment``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-stepadjustments.html#cfn-autoscaling-scalingpolicy-stepadjustment-scalingadjustment
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _TargetTrackingConfigurationProperty(jsii.compat.TypedDict, total=False):
        customizedMetricSpecification: typing.Union[aws_cdk.core.IResolvable, "CfnScalingPolicy.CustomizedMetricSpecificationProperty"]
        """``CfnScalingPolicy.TargetTrackingConfigurationProperty.CustomizedMetricSpecification``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration.html#cfn-autoscaling-scalingpolicy-targettrackingconfiguration-customizedmetricspecification
        Stability:
            stable
        """
        disableScaleIn: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnScalingPolicy.TargetTrackingConfigurationProperty.DisableScaleIn``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration.html#cfn-autoscaling-scalingpolicy-targettrackingconfiguration-disablescalein
        Stability:
            stable
        """
        predefinedMetricSpecification: typing.Union[aws_cdk.core.IResolvable, "CfnScalingPolicy.PredefinedMetricSpecificationProperty"]
        """``CfnScalingPolicy.TargetTrackingConfigurationProperty.PredefinedMetricSpecification``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration.html#cfn-autoscaling-scalingpolicy-targettrackingconfiguration-predefinedmetricspecification
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnScalingPolicy.TargetTrackingConfigurationProperty", jsii_struct_bases=[_TargetTrackingConfigurationProperty])
    class TargetTrackingConfigurationProperty(_TargetTrackingConfigurationProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration.html
        Stability:
            stable
        """
        targetValue: jsii.Number
        """``CfnScalingPolicy.TargetTrackingConfigurationProperty.TargetValue``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration.html#cfn-autoscaling-scalingpolicy-targettrackingconfiguration-targetvalue
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnScalingPolicyProps(jsii.compat.TypedDict, total=False):
    adjustmentType: str
    """``AWS::AutoScaling::ScalingPolicy.AdjustmentType``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html#cfn-as-scalingpolicy-adjustmenttype
    Stability:
        stable
    """
    cooldown: str
    """``AWS::AutoScaling::ScalingPolicy.Cooldown``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html#cfn-as-scalingpolicy-cooldown
    Stability:
        stable
    """
    estimatedInstanceWarmup: jsii.Number
    """``AWS::AutoScaling::ScalingPolicy.EstimatedInstanceWarmup``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html#cfn-as-scalingpolicy-estimatedinstancewarmup
    Stability:
        stable
    """
    metricAggregationType: str
    """``AWS::AutoScaling::ScalingPolicy.MetricAggregationType``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html#cfn-as-scalingpolicy-metricaggregationtype
    Stability:
        stable
    """
    minAdjustmentMagnitude: jsii.Number
    """``AWS::AutoScaling::ScalingPolicy.MinAdjustmentMagnitude``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html#cfn-as-scalingpolicy-minadjustmentmagnitude
    Stability:
        stable
    """
    policyType: str
    """``AWS::AutoScaling::ScalingPolicy.PolicyType``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html#cfn-as-scalingpolicy-policytype
    Stability:
        stable
    """
    scalingAdjustment: jsii.Number
    """``AWS::AutoScaling::ScalingPolicy.ScalingAdjustment``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html#cfn-as-scalingpolicy-scalingadjustment
    Stability:
        stable
    """
    stepAdjustments: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnScalingPolicy.StepAdjustmentProperty"]]]
    """``AWS::AutoScaling::ScalingPolicy.StepAdjustments``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html#cfn-as-scalingpolicy-stepadjustments
    Stability:
        stable
    """
    targetTrackingConfiguration: typing.Union[aws_cdk.core.IResolvable, "CfnScalingPolicy.TargetTrackingConfigurationProperty"]
    """``AWS::AutoScaling::ScalingPolicy.TargetTrackingConfiguration``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html#cfn-autoscaling-scalingpolicy-targettrackingconfiguration
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnScalingPolicyProps", jsii_struct_bases=[_CfnScalingPolicyProps])
class CfnScalingPolicyProps(_CfnScalingPolicyProps):
    """Properties for defining a ``AWS::AutoScaling::ScalingPolicy``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html
    Stability:
        stable
    """
    autoScalingGroupName: str
    """``AWS::AutoScaling::ScalingPolicy.AutoScalingGroupName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html#cfn-as-scalingpolicy-autoscalinggroupname
    Stability:
        stable
    """

class CfnScheduledAction(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-autoscaling.CfnScheduledAction"):
    """A CloudFormation ``AWS::AutoScaling::ScheduledAction``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-scheduledaction.html
    Stability:
        stable
    cloudformationResource:
        AWS::AutoScaling::ScheduledAction
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, auto_scaling_group_name: str, desired_capacity: typing.Optional[jsii.Number]=None, end_time: typing.Optional[str]=None, max_size: typing.Optional[jsii.Number]=None, min_size: typing.Optional[jsii.Number]=None, recurrence: typing.Optional[str]=None, start_time: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::AutoScaling::ScheduledAction``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            auto_scaling_group_name: ``AWS::AutoScaling::ScheduledAction.AutoScalingGroupName``.
            desired_capacity: ``AWS::AutoScaling::ScheduledAction.DesiredCapacity``.
            end_time: ``AWS::AutoScaling::ScheduledAction.EndTime``.
            max_size: ``AWS::AutoScaling::ScheduledAction.MaxSize``.
            min_size: ``AWS::AutoScaling::ScheduledAction.MinSize``.
            recurrence: ``AWS::AutoScaling::ScheduledAction.Recurrence``.
            start_time: ``AWS::AutoScaling::ScheduledAction.StartTime``.

        Stability:
            experimental
        """
        props: CfnScheduledActionProps = {"autoScalingGroupName": auto_scaling_group_name}

        if desired_capacity is not None:
            props["desiredCapacity"] = desired_capacity

        if end_time is not None:
            props["endTime"] = end_time

        if max_size is not None:
            props["maxSize"] = max_size

        if min_size is not None:
            props["minSize"] = min_size

        if recurrence is not None:
            props["recurrence"] = recurrence

        if start_time is not None:
            props["startTime"] = start_time

        jsii.create(CfnScheduledAction, self, [scope, id, props])

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
    @jsii.member(jsii_name="autoScalingGroupName")
    def auto_scaling_group_name(self) -> str:
        """``AWS::AutoScaling::ScheduledAction.AutoScalingGroupName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-scheduledaction.html#cfn-as-scheduledaction-asgname
        Stability:
            stable
        """
        return jsii.get(self, "autoScalingGroupName")

    @auto_scaling_group_name.setter
    def auto_scaling_group_name(self, value: str):
        return jsii.set(self, "autoScalingGroupName", value)

    @property
    @jsii.member(jsii_name="desiredCapacity")
    def desired_capacity(self) -> typing.Optional[jsii.Number]:
        """``AWS::AutoScaling::ScheduledAction.DesiredCapacity``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-scheduledaction.html#cfn-as-scheduledaction-desiredcapacity
        Stability:
            stable
        """
        return jsii.get(self, "desiredCapacity")

    @desired_capacity.setter
    def desired_capacity(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "desiredCapacity", value)

    @property
    @jsii.member(jsii_name="endTime")
    def end_time(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::ScheduledAction.EndTime``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-scheduledaction.html#cfn-as-scheduledaction-endtime
        Stability:
            stable
        """
        return jsii.get(self, "endTime")

    @end_time.setter
    def end_time(self, value: typing.Optional[str]):
        return jsii.set(self, "endTime", value)

    @property
    @jsii.member(jsii_name="maxSize")
    def max_size(self) -> typing.Optional[jsii.Number]:
        """``AWS::AutoScaling::ScheduledAction.MaxSize``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-scheduledaction.html#cfn-as-scheduledaction-maxsize
        Stability:
            stable
        """
        return jsii.get(self, "maxSize")

    @max_size.setter
    def max_size(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "maxSize", value)

    @property
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> typing.Optional[jsii.Number]:
        """``AWS::AutoScaling::ScheduledAction.MinSize``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-scheduledaction.html#cfn-as-scheduledaction-minsize
        Stability:
            stable
        """
        return jsii.get(self, "minSize")

    @min_size.setter
    def min_size(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "minSize", value)

    @property
    @jsii.member(jsii_name="recurrence")
    def recurrence(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::ScheduledAction.Recurrence``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-scheduledaction.html#cfn-as-scheduledaction-recurrence
        Stability:
            stable
        """
        return jsii.get(self, "recurrence")

    @recurrence.setter
    def recurrence(self, value: typing.Optional[str]):
        return jsii.set(self, "recurrence", value)

    @property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> typing.Optional[str]:
        """``AWS::AutoScaling::ScheduledAction.StartTime``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-scheduledaction.html#cfn-as-scheduledaction-starttime
        Stability:
            stable
        """
        return jsii.get(self, "startTime")

    @start_time.setter
    def start_time(self, value: typing.Optional[str]):
        return jsii.set(self, "startTime", value)


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnScheduledActionProps(jsii.compat.TypedDict, total=False):
    desiredCapacity: jsii.Number
    """``AWS::AutoScaling::ScheduledAction.DesiredCapacity``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-scheduledaction.html#cfn-as-scheduledaction-desiredcapacity
    Stability:
        stable
    """
    endTime: str
    """``AWS::AutoScaling::ScheduledAction.EndTime``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-scheduledaction.html#cfn-as-scheduledaction-endtime
    Stability:
        stable
    """
    maxSize: jsii.Number
    """``AWS::AutoScaling::ScheduledAction.MaxSize``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-scheduledaction.html#cfn-as-scheduledaction-maxsize
    Stability:
        stable
    """
    minSize: jsii.Number
    """``AWS::AutoScaling::ScheduledAction.MinSize``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-scheduledaction.html#cfn-as-scheduledaction-minsize
    Stability:
        stable
    """
    recurrence: str
    """``AWS::AutoScaling::ScheduledAction.Recurrence``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-scheduledaction.html#cfn-as-scheduledaction-recurrence
    Stability:
        stable
    """
    startTime: str
    """``AWS::AutoScaling::ScheduledAction.StartTime``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-scheduledaction.html#cfn-as-scheduledaction-starttime
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CfnScheduledActionProps", jsii_struct_bases=[_CfnScheduledActionProps])
class CfnScheduledActionProps(_CfnScheduledActionProps):
    """Properties for defining a ``AWS::AutoScaling::ScheduledAction``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-scheduledaction.html
    Stability:
        stable
    """
    autoScalingGroupName: str
    """``AWS::AutoScaling::ScheduledAction.AutoScalingGroupName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-scheduledaction.html#cfn-as-scheduledaction-asgname
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CommonAutoScalingGroupProps", jsii_struct_bases=[])
class CommonAutoScalingGroupProps(jsii.compat.TypedDict, total=False):
    """Basic properties of an AutoScalingGroup, except the exact machines to run and where they should run.

    Constructs that want to create AutoScalingGroups can inherit
    this interface and specialize the essential parts in various ways.

    Stability:
        experimental
    """
    allowAllOutbound: bool
    """Whether the instances can initiate connections to anywhere by default.

    Default:
        true

    Stability:
        experimental
    """

    associatePublicIpAddress: bool
    """Whether instances in the Auto Scaling Group should have public IP addresses associated with them.

    Default:
        - Use subnet setting.

    Stability:
        experimental
    """

    cooldown: aws_cdk.core.Duration
    """Default scaling cooldown for this AutoScalingGroup.

    Default:
        Duration.minutes(5)

    Stability:
        experimental
    """

    desiredCapacity: jsii.Number
    """Initial amount of instances in the fleet.

    Default:
        1

    Stability:
        experimental
    """

    ignoreUnmodifiedSizeProperties: bool
    """If the ASG has scheduled actions, don't reset unchanged group sizes.

    Only used if the ASG has scheduled actions (which may scale your ASG up
    or down regardless of cdk deployments). If true, the size of the group
    will only be reset if it has been changed in the CDK app. If false, the
    sizes will always be changed back to what they were in the CDK app
    on deployment.

    Default:
        true

    Stability:
        experimental
    """

    keyName: str
    """Name of SSH keypair to grant access to instances.

    Default:
        - No SSH access will be possible.

    Stability:
        experimental
    """

    maxCapacity: jsii.Number
    """Maximum number of instances in the fleet.

    Default:
        desiredCapacity

    Stability:
        experimental
    """

    minCapacity: jsii.Number
    """Minimum number of instances in the fleet.

    Default:
        1

    Stability:
        experimental
    """

    notificationsTopic: aws_cdk.aws_sns.ITopic
    """SNS topic to send notifications about fleet changes.

    Default:
        - No fleet change notifications will be sent.

    Stability:
        experimental
    """

    replacingUpdateMinSuccessfulInstancesPercent: jsii.Number
    """Configuration for replacing updates.

    Only used if updateType == UpdateType.ReplacingUpdate. Specifies how
    many instances must signal success for the update to succeed.

    Default:
        minSuccessfulInstancesPercent

    Stability:
        experimental
    """

    resourceSignalCount: jsii.Number
    """How many ResourceSignal calls CloudFormation expects before the resource is considered created.

    Default:
        1

    Stability:
        experimental
    """

    resourceSignalTimeout: aws_cdk.core.Duration
    """The length of time to wait for the resourceSignalCount.

    The maximum value is 43200 (12 hours).

    Default:
        Duration.minutes(5)

    Stability:
        experimental
    """

    rollingUpdateConfiguration: "RollingUpdateConfiguration"
    """Configuration for rolling updates.

    Only used if updateType == UpdateType.RollingUpdate.

    Default:
        - RollingUpdateConfiguration with defaults.

    Stability:
        experimental
    """

    spotPrice: str
    """The maximum hourly price (in USD) to be paid for any Spot Instance launched to fulfill the request.

    Spot Instances are
    launched when the price you specify exceeds the current Spot market price.

    Default:
        none

    Stability:
        experimental
    """

    updateType: "UpdateType"
    """What to do when an AutoScalingGroup's instance configuration is changed.

    This is applied when any of the settings on the ASG are changed that
    affect how the instances should be created (VPC, instance type, startup
    scripts, etc.). It indicates how the existing instances should be
    replaced with new instances matching the new config. By default, nothing
    is done and only new instances are launched with the new config.

    Default:
        UpdateType.None

    Stability:
        experimental
    """

    vpcSubnets: aws_cdk.aws_ec2.SubnetSelection
    """Where to place instances within the VPC.

    Default:
        - All Private subnets.

    Stability:
        experimental
    """

@jsii.data_type_optionals(jsii_struct_bases=[CommonAutoScalingGroupProps])
class _AutoScalingGroupProps(CommonAutoScalingGroupProps, jsii.compat.TypedDict, total=False):
    role: aws_cdk.aws_iam.IRole
    """An IAM role to associate with the instance profile assigned to this Auto Scaling Group.

    The role must be assumable by the service principal ``ec2.amazonaws.com``:

    Default:
        A role will automatically be created, it can be accessed via the ``role`` property

    Stability:
        experimental

    Example::
           const role = new iam.Role(this, 'MyRole', {
             assumedBy: new iam.ServicePrincipal('ec2.amazonaws.com')
           });
    """
    userData: aws_cdk.aws_ec2.UserData
    """Specific UserData to use.

    The UserData may still be mutated after creation.

    Default:
        - A UserData object appropriate for the MachineImage's
          Operating System is created.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.AutoScalingGroupProps", jsii_struct_bases=[_AutoScalingGroupProps])
class AutoScalingGroupProps(_AutoScalingGroupProps):
    """Properties of a Fleet.

    Stability:
        experimental
    """
    instanceType: aws_cdk.aws_ec2.InstanceType
    """Type of instance to launch.

    Stability:
        experimental
    """

    machineImage: aws_cdk.aws_ec2.IMachineImage
    """AMI to launch.

    Stability:
        experimental
    """

    vpc: aws_cdk.aws_ec2.IVpc
    """VPC to launch these instances in.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CpuUtilizationScalingProps", jsii_struct_bases=[BaseTargetTrackingProps])
class CpuUtilizationScalingProps(BaseTargetTrackingProps, jsii.compat.TypedDict):
    """Properties for enabling scaling based on CPU utilization.

    Stability:
        experimental
    """
    targetUtilizationPercent: jsii.Number
    """Target average CPU utilization across the task.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.CronOptions", jsii_struct_bases=[])
class CronOptions(jsii.compat.TypedDict, total=False):
    """Options to configure a cron expression.

    All fields are strings so you can use complex expresions. Absence of
    a field implies '*' or '?', whichever one is appropriate.

    See:
        http://crontab.org/
    Stability:
        experimental
    """
    day: str
    """The day of the month to run this rule at.

    Default:
        - Every day of the month

    Stability:
        experimental
    """

    hour: str
    """The hour to run this rule at.

    Default:
        - Every hour

    Stability:
        experimental
    """

    minute: str
    """The minute to run this rule at.

    Default:
        - Every minute

    Stability:
        experimental
    """

    month: str
    """The month to run this rule at.

    Default:
        - Every month

    Stability:
        experimental
    """

    weekDay: str
    """The day of the week to run this rule at.

    Default:
        - Any day of the week

    Stability:
        experimental
    """

@jsii.enum(jsii_type="@aws-cdk/aws-autoscaling.DefaultResult")
class DefaultResult(enum.Enum):
    """
    Stability:
        experimental
    """
    CONTINUE = "CONTINUE"
    """
    Stability:
        experimental
    """
    ABANDON = "ABANDON"
    """
    Stability:
        experimental
    """

@jsii.interface(jsii_type="@aws-cdk/aws-autoscaling.IAutoScalingGroup")
class IAutoScalingGroup(aws_cdk.core.IResource, jsii.compat.Protocol):
    """An AutoScalingGroup.

    Stability:
        experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IAutoScalingGroupProxy

    @property
    @jsii.member(jsii_name="autoScalingGroupArn")
    def auto_scaling_group_arn(self) -> str:
        """The arn of the AutoScalingGroup.

        Stability:
            experimental
        attribute:
            true
        """
        ...

    @property
    @jsii.member(jsii_name="autoScalingGroupName")
    def auto_scaling_group_name(self) -> str:
        """The name of the AutoScalingGroup.

        Stability:
            experimental
        attribute:
            true
        """
        ...

    @jsii.member(jsii_name="addLifecycleHook")
    def add_lifecycle_hook(self, id: str, *, lifecycle_transition: "LifecycleTransition", notification_target: "ILifecycleHookTarget", default_result: typing.Optional["DefaultResult"]=None, heartbeat_timeout: typing.Optional[aws_cdk.core.Duration]=None, lifecycle_hook_name: typing.Optional[str]=None, notification_metadata: typing.Optional[str]=None, role: typing.Optional[aws_cdk.aws_iam.IRole]=None) -> "LifecycleHook":
        """Send a message to either an SQS queue or SNS topic when instances launch or terminate.

        Arguments:
            id: -
            props: -
            lifecycle_transition: The state of the Amazon EC2 instance to which you want to attach the lifecycle hook.
            notification_target: The target of the lifecycle hook.
            default_result: The action the Auto Scaling group takes when the lifecycle hook timeout elapses or if an unexpected failure occurs. Default: Continue
            heartbeat_timeout: Maximum time between calls to RecordLifecycleActionHeartbeat for the hook. If the lifecycle hook times out, perform the action in DefaultResult. Default: - No heartbeat timeout.
            lifecycle_hook_name: Name of the lifecycle hook. Default: - Automatically generated name.
            notification_metadata: Additional data to pass to the lifecycle hook target. Default: - No metadata.
            role: The role that allows publishing to the notification target. Default: - A role is automatically created.

        Stability:
            experimental
        """
        ...

    @jsii.member(jsii_name="scaleOnCpuUtilization")
    def scale_on_cpu_utilization(self, id: str, *, target_utilization_percent: jsii.Number, cooldown: typing.Optional[aws_cdk.core.Duration]=None, disable_scale_in: typing.Optional[bool]=None, estimated_instance_warmup: typing.Optional[aws_cdk.core.Duration]=None) -> "TargetTrackingScalingPolicy":
        """Scale out or in to achieve a target CPU utilization.

        Arguments:
            id: -
            props: -
            target_utilization_percent: Target average CPU utilization across the task.
            cooldown: Period after a scaling completes before another scaling activity can start. Default: - The default cooldown configured on the AutoScalingGroup.
            disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the autoscaling group. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the group. Default: false
            estimated_instance_warmup: Estimated time until a newly launched instance can send metrics to CloudWatch. Default: - Same as the cooldown.

        Stability:
            experimental
        """
        ...

    @jsii.member(jsii_name="scaleOnIncomingBytes")
    def scale_on_incoming_bytes(self, id: str, *, target_bytes_per_second: jsii.Number, cooldown: typing.Optional[aws_cdk.core.Duration]=None, disable_scale_in: typing.Optional[bool]=None, estimated_instance_warmup: typing.Optional[aws_cdk.core.Duration]=None) -> "TargetTrackingScalingPolicy":
        """Scale out or in to achieve a target network ingress rate.

        Arguments:
            id: -
            props: -
            target_bytes_per_second: Target average bytes/seconds on each instance.
            cooldown: Period after a scaling completes before another scaling activity can start. Default: - The default cooldown configured on the AutoScalingGroup.
            disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the autoscaling group. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the group. Default: false
            estimated_instance_warmup: Estimated time until a newly launched instance can send metrics to CloudWatch. Default: - Same as the cooldown.

        Stability:
            experimental
        """
        ...

    @jsii.member(jsii_name="scaleOnMetric")
    def scale_on_metric(self, id: str, *, metric: aws_cdk.aws_cloudwatch.IMetric, scaling_steps: typing.List["ScalingInterval"], adjustment_type: typing.Optional["AdjustmentType"]=None, cooldown: typing.Optional[aws_cdk.core.Duration]=None, estimated_instance_warmup: typing.Optional[aws_cdk.core.Duration]=None, min_adjustment_magnitude: typing.Optional[jsii.Number]=None) -> "StepScalingPolicy":
        """Scale out or in, in response to a metric.

        Arguments:
            id: -
            props: -
            metric: Metric to scale on.
            scaling_steps: The intervals for scaling. Maps a range of metric values to a particular scaling behavior.
            adjustment_type: How the adjustment numbers inside 'intervals' are interpreted. Default: ChangeInCapacity
            cooldown: Grace period after scaling activity. Default: Default cooldown period on your AutoScalingGroup
            estimated_instance_warmup: Estimated time until a newly launched instance can send metrics to CloudWatch. Default: Same as the cooldown
            min_adjustment_magnitude: Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect

        Stability:
            experimental
        """
        ...

    @jsii.member(jsii_name="scaleOnOutgoingBytes")
    def scale_on_outgoing_bytes(self, id: str, *, target_bytes_per_second: jsii.Number, cooldown: typing.Optional[aws_cdk.core.Duration]=None, disable_scale_in: typing.Optional[bool]=None, estimated_instance_warmup: typing.Optional[aws_cdk.core.Duration]=None) -> "TargetTrackingScalingPolicy":
        """Scale out or in to achieve a target network egress rate.

        Arguments:
            id: -
            props: -
            target_bytes_per_second: Target average bytes/seconds on each instance.
            cooldown: Period after a scaling completes before another scaling activity can start. Default: - The default cooldown configured on the AutoScalingGroup.
            disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the autoscaling group. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the group. Default: false
            estimated_instance_warmup: Estimated time until a newly launched instance can send metrics to CloudWatch. Default: - Same as the cooldown.

        Stability:
            experimental
        """
        ...

    @jsii.member(jsii_name="scaleOnSchedule")
    def scale_on_schedule(self, id: str, *, schedule: "Schedule", desired_capacity: typing.Optional[jsii.Number]=None, end_time: typing.Optional[datetime.datetime]=None, max_capacity: typing.Optional[jsii.Number]=None, min_capacity: typing.Optional[jsii.Number]=None, start_time: typing.Optional[datetime.datetime]=None) -> "ScheduledAction":
        """Scale out or in based on time.

        Arguments:
            id: -
            props: -
            schedule: When to perform this action. Supports cron expressions. For more information about cron expressions, see https://en.wikipedia.org/wiki/Cron.
            desired_capacity: The new desired capacity. At the scheduled time, set the desired capacity to the given capacity. At least one of maxCapacity, minCapacity, or desiredCapacity must be supplied. Default: - No new desired capacity.
            end_time: When this scheduled action expires. Default: - The rule never expires.
            max_capacity: The new maximum capacity. At the scheduled time, set the maximum capacity to the given capacity. At least one of maxCapacity, minCapacity, or desiredCapacity must be supplied. Default: - No new maximum capacity.
            min_capacity: The new minimum capacity. At the scheduled time, set the minimum capacity to the given capacity. At least one of maxCapacity, minCapacity, or desiredCapacity must be supplied. Default: - No new minimum capacity.
            start_time: When this scheduled action becomes active. Default: - The rule is activate immediately.

        Stability:
            experimental
        """
        ...

    @jsii.member(jsii_name="scaleToTrackMetric")
    def scale_to_track_metric(self, id: str, *, metric: aws_cdk.aws_cloudwatch.IMetric, target_value: jsii.Number, cooldown: typing.Optional[aws_cdk.core.Duration]=None, disable_scale_in: typing.Optional[bool]=None, estimated_instance_warmup: typing.Optional[aws_cdk.core.Duration]=None) -> "TargetTrackingScalingPolicy":
        """Scale out or in in order to keep a metric around a target value.

        Arguments:
            id: -
            props: -
            metric: Metric to track. The metric must represent a utilization, so that if it's higher than the target value, your ASG should scale out, and if it's lower it should scale in.
            target_value: Value to keep the metric around.
            cooldown: Period after a scaling completes before another scaling activity can start. Default: - The default cooldown configured on the AutoScalingGroup.
            disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the autoscaling group. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the group. Default: false
            estimated_instance_warmup: Estimated time until a newly launched instance can send metrics to CloudWatch. Default: - Same as the cooldown.

        Stability:
            experimental
        """
        ...


class _IAutoScalingGroupProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """An AutoScalingGroup.

    Stability:
        experimental
    """
    __jsii_type__ = "@aws-cdk/aws-autoscaling.IAutoScalingGroup"
    @property
    @jsii.member(jsii_name="autoScalingGroupArn")
    def auto_scaling_group_arn(self) -> str:
        """The arn of the AutoScalingGroup.

        Stability:
            experimental
        attribute:
            true
        """
        return jsii.get(self, "autoScalingGroupArn")

    @property
    @jsii.member(jsii_name="autoScalingGroupName")
    def auto_scaling_group_name(self) -> str:
        """The name of the AutoScalingGroup.

        Stability:
            experimental
        attribute:
            true
        """
        return jsii.get(self, "autoScalingGroupName")

    @jsii.member(jsii_name="addLifecycleHook")
    def add_lifecycle_hook(self, id: str, *, lifecycle_transition: "LifecycleTransition", notification_target: "ILifecycleHookTarget", default_result: typing.Optional["DefaultResult"]=None, heartbeat_timeout: typing.Optional[aws_cdk.core.Duration]=None, lifecycle_hook_name: typing.Optional[str]=None, notification_metadata: typing.Optional[str]=None, role: typing.Optional[aws_cdk.aws_iam.IRole]=None) -> "LifecycleHook":
        """Send a message to either an SQS queue or SNS topic when instances launch or terminate.

        Arguments:
            id: -
            props: -
            lifecycle_transition: The state of the Amazon EC2 instance to which you want to attach the lifecycle hook.
            notification_target: The target of the lifecycle hook.
            default_result: The action the Auto Scaling group takes when the lifecycle hook timeout elapses or if an unexpected failure occurs. Default: Continue
            heartbeat_timeout: Maximum time between calls to RecordLifecycleActionHeartbeat for the hook. If the lifecycle hook times out, perform the action in DefaultResult. Default: - No heartbeat timeout.
            lifecycle_hook_name: Name of the lifecycle hook. Default: - Automatically generated name.
            notification_metadata: Additional data to pass to the lifecycle hook target. Default: - No metadata.
            role: The role that allows publishing to the notification target. Default: - A role is automatically created.

        Stability:
            experimental
        """
        props: BasicLifecycleHookProps = {"lifecycleTransition": lifecycle_transition, "notificationTarget": notification_target}

        if default_result is not None:
            props["defaultResult"] = default_result

        if heartbeat_timeout is not None:
            props["heartbeatTimeout"] = heartbeat_timeout

        if lifecycle_hook_name is not None:
            props["lifecycleHookName"] = lifecycle_hook_name

        if notification_metadata is not None:
            props["notificationMetadata"] = notification_metadata

        if role is not None:
            props["role"] = role

        return jsii.invoke(self, "addLifecycleHook", [id, props])

    @jsii.member(jsii_name="scaleOnCpuUtilization")
    def scale_on_cpu_utilization(self, id: str, *, target_utilization_percent: jsii.Number, cooldown: typing.Optional[aws_cdk.core.Duration]=None, disable_scale_in: typing.Optional[bool]=None, estimated_instance_warmup: typing.Optional[aws_cdk.core.Duration]=None) -> "TargetTrackingScalingPolicy":
        """Scale out or in to achieve a target CPU utilization.

        Arguments:
            id: -
            props: -
            target_utilization_percent: Target average CPU utilization across the task.
            cooldown: Period after a scaling completes before another scaling activity can start. Default: - The default cooldown configured on the AutoScalingGroup.
            disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the autoscaling group. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the group. Default: false
            estimated_instance_warmup: Estimated time until a newly launched instance can send metrics to CloudWatch. Default: - Same as the cooldown.

        Stability:
            experimental
        """
        props: CpuUtilizationScalingProps = {"targetUtilizationPercent": target_utilization_percent}

        if cooldown is not None:
            props["cooldown"] = cooldown

        if disable_scale_in is not None:
            props["disableScaleIn"] = disable_scale_in

        if estimated_instance_warmup is not None:
            props["estimatedInstanceWarmup"] = estimated_instance_warmup

        return jsii.invoke(self, "scaleOnCpuUtilization", [id, props])

    @jsii.member(jsii_name="scaleOnIncomingBytes")
    def scale_on_incoming_bytes(self, id: str, *, target_bytes_per_second: jsii.Number, cooldown: typing.Optional[aws_cdk.core.Duration]=None, disable_scale_in: typing.Optional[bool]=None, estimated_instance_warmup: typing.Optional[aws_cdk.core.Duration]=None) -> "TargetTrackingScalingPolicy":
        """Scale out or in to achieve a target network ingress rate.

        Arguments:
            id: -
            props: -
            target_bytes_per_second: Target average bytes/seconds on each instance.
            cooldown: Period after a scaling completes before another scaling activity can start. Default: - The default cooldown configured on the AutoScalingGroup.
            disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the autoscaling group. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the group. Default: false
            estimated_instance_warmup: Estimated time until a newly launched instance can send metrics to CloudWatch. Default: - Same as the cooldown.

        Stability:
            experimental
        """
        props: NetworkUtilizationScalingProps = {"targetBytesPerSecond": target_bytes_per_second}

        if cooldown is not None:
            props["cooldown"] = cooldown

        if disable_scale_in is not None:
            props["disableScaleIn"] = disable_scale_in

        if estimated_instance_warmup is not None:
            props["estimatedInstanceWarmup"] = estimated_instance_warmup

        return jsii.invoke(self, "scaleOnIncomingBytes", [id, props])

    @jsii.member(jsii_name="scaleOnMetric")
    def scale_on_metric(self, id: str, *, metric: aws_cdk.aws_cloudwatch.IMetric, scaling_steps: typing.List["ScalingInterval"], adjustment_type: typing.Optional["AdjustmentType"]=None, cooldown: typing.Optional[aws_cdk.core.Duration]=None, estimated_instance_warmup: typing.Optional[aws_cdk.core.Duration]=None, min_adjustment_magnitude: typing.Optional[jsii.Number]=None) -> "StepScalingPolicy":
        """Scale out or in, in response to a metric.

        Arguments:
            id: -
            props: -
            metric: Metric to scale on.
            scaling_steps: The intervals for scaling. Maps a range of metric values to a particular scaling behavior.
            adjustment_type: How the adjustment numbers inside 'intervals' are interpreted. Default: ChangeInCapacity
            cooldown: Grace period after scaling activity. Default: Default cooldown period on your AutoScalingGroup
            estimated_instance_warmup: Estimated time until a newly launched instance can send metrics to CloudWatch. Default: Same as the cooldown
            min_adjustment_magnitude: Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect

        Stability:
            experimental
        """
        props: BasicStepScalingPolicyProps = {"metric": metric, "scalingSteps": scaling_steps}

        if adjustment_type is not None:
            props["adjustmentType"] = adjustment_type

        if cooldown is not None:
            props["cooldown"] = cooldown

        if estimated_instance_warmup is not None:
            props["estimatedInstanceWarmup"] = estimated_instance_warmup

        if min_adjustment_magnitude is not None:
            props["minAdjustmentMagnitude"] = min_adjustment_magnitude

        return jsii.invoke(self, "scaleOnMetric", [id, props])

    @jsii.member(jsii_name="scaleOnOutgoingBytes")
    def scale_on_outgoing_bytes(self, id: str, *, target_bytes_per_second: jsii.Number, cooldown: typing.Optional[aws_cdk.core.Duration]=None, disable_scale_in: typing.Optional[bool]=None, estimated_instance_warmup: typing.Optional[aws_cdk.core.Duration]=None) -> "TargetTrackingScalingPolicy":
        """Scale out or in to achieve a target network egress rate.

        Arguments:
            id: -
            props: -
            target_bytes_per_second: Target average bytes/seconds on each instance.
            cooldown: Period after a scaling completes before another scaling activity can start. Default: - The default cooldown configured on the AutoScalingGroup.
            disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the autoscaling group. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the group. Default: false
            estimated_instance_warmup: Estimated time until a newly launched instance can send metrics to CloudWatch. Default: - Same as the cooldown.

        Stability:
            experimental
        """
        props: NetworkUtilizationScalingProps = {"targetBytesPerSecond": target_bytes_per_second}

        if cooldown is not None:
            props["cooldown"] = cooldown

        if disable_scale_in is not None:
            props["disableScaleIn"] = disable_scale_in

        if estimated_instance_warmup is not None:
            props["estimatedInstanceWarmup"] = estimated_instance_warmup

        return jsii.invoke(self, "scaleOnOutgoingBytes", [id, props])

    @jsii.member(jsii_name="scaleOnSchedule")
    def scale_on_schedule(self, id: str, *, schedule: "Schedule", desired_capacity: typing.Optional[jsii.Number]=None, end_time: typing.Optional[datetime.datetime]=None, max_capacity: typing.Optional[jsii.Number]=None, min_capacity: typing.Optional[jsii.Number]=None, start_time: typing.Optional[datetime.datetime]=None) -> "ScheduledAction":
        """Scale out or in based on time.

        Arguments:
            id: -
            props: -
            schedule: When to perform this action. Supports cron expressions. For more information about cron expressions, see https://en.wikipedia.org/wiki/Cron.
            desired_capacity: The new desired capacity. At the scheduled time, set the desired capacity to the given capacity. At least one of maxCapacity, minCapacity, or desiredCapacity must be supplied. Default: - No new desired capacity.
            end_time: When this scheduled action expires. Default: - The rule never expires.
            max_capacity: The new maximum capacity. At the scheduled time, set the maximum capacity to the given capacity. At least one of maxCapacity, minCapacity, or desiredCapacity must be supplied. Default: - No new maximum capacity.
            min_capacity: The new minimum capacity. At the scheduled time, set the minimum capacity to the given capacity. At least one of maxCapacity, minCapacity, or desiredCapacity must be supplied. Default: - No new minimum capacity.
            start_time: When this scheduled action becomes active. Default: - The rule is activate immediately.

        Stability:
            experimental
        """
        props: BasicScheduledActionProps = {"schedule": schedule}

        if desired_capacity is not None:
            props["desiredCapacity"] = desired_capacity

        if end_time is not None:
            props["endTime"] = end_time

        if max_capacity is not None:
            props["maxCapacity"] = max_capacity

        if min_capacity is not None:
            props["minCapacity"] = min_capacity

        if start_time is not None:
            props["startTime"] = start_time

        return jsii.invoke(self, "scaleOnSchedule", [id, props])

    @jsii.member(jsii_name="scaleToTrackMetric")
    def scale_to_track_metric(self, id: str, *, metric: aws_cdk.aws_cloudwatch.IMetric, target_value: jsii.Number, cooldown: typing.Optional[aws_cdk.core.Duration]=None, disable_scale_in: typing.Optional[bool]=None, estimated_instance_warmup: typing.Optional[aws_cdk.core.Duration]=None) -> "TargetTrackingScalingPolicy":
        """Scale out or in in order to keep a metric around a target value.

        Arguments:
            id: -
            props: -
            metric: Metric to track. The metric must represent a utilization, so that if it's higher than the target value, your ASG should scale out, and if it's lower it should scale in.
            target_value: Value to keep the metric around.
            cooldown: Period after a scaling completes before another scaling activity can start. Default: - The default cooldown configured on the AutoScalingGroup.
            disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the autoscaling group. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the group. Default: false
            estimated_instance_warmup: Estimated time until a newly launched instance can send metrics to CloudWatch. Default: - Same as the cooldown.

        Stability:
            experimental
        """
        props: MetricTargetTrackingProps = {"metric": metric, "targetValue": target_value}

        if cooldown is not None:
            props["cooldown"] = cooldown

        if disable_scale_in is not None:
            props["disableScaleIn"] = disable_scale_in

        if estimated_instance_warmup is not None:
            props["estimatedInstanceWarmup"] = estimated_instance_warmup

        return jsii.invoke(self, "scaleToTrackMetric", [id, props])


@jsii.implements(aws_cdk.aws_elasticloadbalancing.ILoadBalancerTarget, aws_cdk.aws_ec2.IConnectable, aws_cdk.aws_elasticloadbalancingv2.IApplicationLoadBalancerTarget, aws_cdk.aws_elasticloadbalancingv2.INetworkLoadBalancerTarget, IAutoScalingGroup)
class AutoScalingGroup(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-autoscaling.AutoScalingGroup"):
    """A Fleet represents a managed set of EC2 instances.

    The Fleet models a number of AutoScalingGroups, a launch configuration, a
    security group and an instance role.

    It allows adding arbitrary commands to the startup scripts of the instances
    in the fleet.

    The ASG spans all availability zones.

    Stability:
        experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, instance_type: aws_cdk.aws_ec2.InstanceType, machine_image: aws_cdk.aws_ec2.IMachineImage, vpc: aws_cdk.aws_ec2.IVpc, role: typing.Optional[aws_cdk.aws_iam.IRole]=None, user_data: typing.Optional[aws_cdk.aws_ec2.UserData]=None, allow_all_outbound: typing.Optional[bool]=None, associate_public_ip_address: typing.Optional[bool]=None, cooldown: typing.Optional[aws_cdk.core.Duration]=None, desired_capacity: typing.Optional[jsii.Number]=None, ignore_unmodified_size_properties: typing.Optional[bool]=None, key_name: typing.Optional[str]=None, max_capacity: typing.Optional[jsii.Number]=None, min_capacity: typing.Optional[jsii.Number]=None, notifications_topic: typing.Optional[aws_cdk.aws_sns.ITopic]=None, replacing_update_min_successful_instances_percent: typing.Optional[jsii.Number]=None, resource_signal_count: typing.Optional[jsii.Number]=None, resource_signal_timeout: typing.Optional[aws_cdk.core.Duration]=None, rolling_update_configuration: typing.Optional["RollingUpdateConfiguration"]=None, spot_price: typing.Optional[str]=None, update_type: typing.Optional["UpdateType"]=None, vpc_subnets: typing.Optional[aws_cdk.aws_ec2.SubnetSelection]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            instance_type: Type of instance to launch.
            machine_image: AMI to launch.
            vpc: VPC to launch these instances in.
            role: An IAM role to associate with the instance profile assigned to this Auto Scaling Group. The role must be assumable by the service principal ``ec2.amazonaws.com``: Default: A role will automatically be created, it can be accessed via the ``role`` property
            user_data: Specific UserData to use. The UserData may still be mutated after creation. Default: - A UserData object appropriate for the MachineImage's Operating System is created.
            allow_all_outbound: Whether the instances can initiate connections to anywhere by default. Default: true
            associate_public_ip_address: Whether instances in the Auto Scaling Group should have public IP addresses associated with them. Default: - Use subnet setting.
            cooldown: Default scaling cooldown for this AutoScalingGroup. Default: Duration.minutes(5)
            desired_capacity: Initial amount of instances in the fleet. Default: 1
            ignore_unmodified_size_properties: If the ASG has scheduled actions, don't reset unchanged group sizes. Only used if the ASG has scheduled actions (which may scale your ASG up or down regardless of cdk deployments). If true, the size of the group will only be reset if it has been changed in the CDK app. If false, the sizes will always be changed back to what they were in the CDK app on deployment. Default: true
            key_name: Name of SSH keypair to grant access to instances. Default: - No SSH access will be possible.
            max_capacity: Maximum number of instances in the fleet. Default: desiredCapacity
            min_capacity: Minimum number of instances in the fleet. Default: 1
            notifications_topic: SNS topic to send notifications about fleet changes. Default: - No fleet change notifications will be sent.
            replacing_update_min_successful_instances_percent: Configuration for replacing updates. Only used if updateType == UpdateType.ReplacingUpdate. Specifies how many instances must signal success for the update to succeed. Default: minSuccessfulInstancesPercent
            resource_signal_count: How many ResourceSignal calls CloudFormation expects before the resource is considered created. Default: 1
            resource_signal_timeout: The length of time to wait for the resourceSignalCount. The maximum value is 43200 (12 hours). Default: Duration.minutes(5)
            rolling_update_configuration: Configuration for rolling updates. Only used if updateType == UpdateType.RollingUpdate. Default: - RollingUpdateConfiguration with defaults.
            spot_price: The maximum hourly price (in USD) to be paid for any Spot Instance launched to fulfill the request. Spot Instances are launched when the price you specify exceeds the current Spot market price. Default: none
            update_type: What to do when an AutoScalingGroup's instance configuration is changed. This is applied when any of the settings on the ASG are changed that affect how the instances should be created (VPC, instance type, startup scripts, etc.). It indicates how the existing instances should be replaced with new instances matching the new config. By default, nothing is done and only new instances are launched with the new config. Default: UpdateType.None
            vpc_subnets: Where to place instances within the VPC. Default: - All Private subnets.

        Stability:
            experimental
        """
        props: AutoScalingGroupProps = {"instanceType": instance_type, "machineImage": machine_image, "vpc": vpc}

        if role is not None:
            props["role"] = role

        if user_data is not None:
            props["userData"] = user_data

        if allow_all_outbound is not None:
            props["allowAllOutbound"] = allow_all_outbound

        if associate_public_ip_address is not None:
            props["associatePublicIpAddress"] = associate_public_ip_address

        if cooldown is not None:
            props["cooldown"] = cooldown

        if desired_capacity is not None:
            props["desiredCapacity"] = desired_capacity

        if ignore_unmodified_size_properties is not None:
            props["ignoreUnmodifiedSizeProperties"] = ignore_unmodified_size_properties

        if key_name is not None:
            props["keyName"] = key_name

        if max_capacity is not None:
            props["maxCapacity"] = max_capacity

        if min_capacity is not None:
            props["minCapacity"] = min_capacity

        if notifications_topic is not None:
            props["notificationsTopic"] = notifications_topic

        if replacing_update_min_successful_instances_percent is not None:
            props["replacingUpdateMinSuccessfulInstancesPercent"] = replacing_update_min_successful_instances_percent

        if resource_signal_count is not None:
            props["resourceSignalCount"] = resource_signal_count

        if resource_signal_timeout is not None:
            props["resourceSignalTimeout"] = resource_signal_timeout

        if rolling_update_configuration is not None:
            props["rollingUpdateConfiguration"] = rolling_update_configuration

        if spot_price is not None:
            props["spotPrice"] = spot_price

        if update_type is not None:
            props["updateType"] = update_type

        if vpc_subnets is not None:
            props["vpcSubnets"] = vpc_subnets

        jsii.create(AutoScalingGroup, self, [scope, id, props])

    @jsii.member(jsii_name="fromAutoScalingGroupName")
    @classmethod
    def from_auto_scaling_group_name(cls, scope: aws_cdk.core.Construct, id: str, auto_scaling_group_name: str) -> "IAutoScalingGroup":
        """
        Arguments:
            scope: -
            id: -
            auto_scaling_group_name: -

        Stability:
            experimental
        """
        return jsii.sinvoke(cls, "fromAutoScalingGroupName", [scope, id, auto_scaling_group_name])

    @jsii.member(jsii_name="addLifecycleHook")
    def add_lifecycle_hook(self, id: str, *, lifecycle_transition: "LifecycleTransition", notification_target: "ILifecycleHookTarget", default_result: typing.Optional["DefaultResult"]=None, heartbeat_timeout: typing.Optional[aws_cdk.core.Duration]=None, lifecycle_hook_name: typing.Optional[str]=None, notification_metadata: typing.Optional[str]=None, role: typing.Optional[aws_cdk.aws_iam.IRole]=None) -> "LifecycleHook":
        """Send a message to either an SQS queue or SNS topic when instances launch or terminate.

        Arguments:
            id: -
            props: -
            lifecycle_transition: The state of the Amazon EC2 instance to which you want to attach the lifecycle hook.
            notification_target: The target of the lifecycle hook.
            default_result: The action the Auto Scaling group takes when the lifecycle hook timeout elapses or if an unexpected failure occurs. Default: Continue
            heartbeat_timeout: Maximum time between calls to RecordLifecycleActionHeartbeat for the hook. If the lifecycle hook times out, perform the action in DefaultResult. Default: - No heartbeat timeout.
            lifecycle_hook_name: Name of the lifecycle hook. Default: - Automatically generated name.
            notification_metadata: Additional data to pass to the lifecycle hook target. Default: - No metadata.
            role: The role that allows publishing to the notification target. Default: - A role is automatically created.

        Stability:
            experimental
        """
        props: BasicLifecycleHookProps = {"lifecycleTransition": lifecycle_transition, "notificationTarget": notification_target}

        if default_result is not None:
            props["defaultResult"] = default_result

        if heartbeat_timeout is not None:
            props["heartbeatTimeout"] = heartbeat_timeout

        if lifecycle_hook_name is not None:
            props["lifecycleHookName"] = lifecycle_hook_name

        if notification_metadata is not None:
            props["notificationMetadata"] = notification_metadata

        if role is not None:
            props["role"] = role

        return jsii.invoke(self, "addLifecycleHook", [id, props])

    @jsii.member(jsii_name="addSecurityGroup")
    def add_security_group(self, security_group: aws_cdk.aws_ec2.ISecurityGroup) -> None:
        """Add the security group to all instances via the launch configuration security groups array.

        Arguments:
            security_group: : The security group to add.

        Stability:
            experimental
        """
        return jsii.invoke(self, "addSecurityGroup", [security_group])

    @jsii.member(jsii_name="addToRolePolicy")
    def add_to_role_policy(self, statement: aws_cdk.aws_iam.PolicyStatement) -> None:
        """Adds a statement to the IAM role assumed by instances of this fleet.

        Arguments:
            statement: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "addToRolePolicy", [statement])

    @jsii.member(jsii_name="addUserData")
    def add_user_data(self, *commands: str) -> None:
        """Add command to the startup script of fleet instances. The command must be in the scripting language supported by the fleet's OS (i.e. Linux/Windows).

        Arguments:
            commands: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "addUserData", [*commands])

    @jsii.member(jsii_name="attachToApplicationTargetGroup")
    def attach_to_application_target_group(self, target_group: aws_cdk.aws_elasticloadbalancingv2.ApplicationTargetGroup) -> aws_cdk.aws_elasticloadbalancingv2.LoadBalancerTargetProps:
        """Attach to ELBv2 Application Target Group.

        Arguments:
            target_group: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "attachToApplicationTargetGroup", [target_group])

    @jsii.member(jsii_name="attachToClassicLB")
    def attach_to_classic_lb(self, load_balancer: aws_cdk.aws_elasticloadbalancing.LoadBalancer) -> None:
        """Attach to a classic load balancer.

        Arguments:
            load_balancer: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "attachToClassicLB", [load_balancer])

    @jsii.member(jsii_name="attachToNetworkTargetGroup")
    def attach_to_network_target_group(self, target_group: aws_cdk.aws_elasticloadbalancingv2.NetworkTargetGroup) -> aws_cdk.aws_elasticloadbalancingv2.LoadBalancerTargetProps:
        """Attach to ELBv2 Application Target Group.

        Arguments:
            target_group: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "attachToNetworkTargetGroup", [target_group])

    @jsii.member(jsii_name="scaleOnCpuUtilization")
    def scale_on_cpu_utilization(self, id: str, *, target_utilization_percent: jsii.Number, cooldown: typing.Optional[aws_cdk.core.Duration]=None, disable_scale_in: typing.Optional[bool]=None, estimated_instance_warmup: typing.Optional[aws_cdk.core.Duration]=None) -> "TargetTrackingScalingPolicy":
        """Scale out or in to achieve a target CPU utilization.

        Arguments:
            id: -
            props: -
            target_utilization_percent: Target average CPU utilization across the task.
            cooldown: Period after a scaling completes before another scaling activity can start. Default: - The default cooldown configured on the AutoScalingGroup.
            disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the autoscaling group. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the group. Default: false
            estimated_instance_warmup: Estimated time until a newly launched instance can send metrics to CloudWatch. Default: - Same as the cooldown.

        Stability:
            experimental
        """
        props: CpuUtilizationScalingProps = {"targetUtilizationPercent": target_utilization_percent}

        if cooldown is not None:
            props["cooldown"] = cooldown

        if disable_scale_in is not None:
            props["disableScaleIn"] = disable_scale_in

        if estimated_instance_warmup is not None:
            props["estimatedInstanceWarmup"] = estimated_instance_warmup

        return jsii.invoke(self, "scaleOnCpuUtilization", [id, props])

    @jsii.member(jsii_name="scaleOnIncomingBytes")
    def scale_on_incoming_bytes(self, id: str, *, target_bytes_per_second: jsii.Number, cooldown: typing.Optional[aws_cdk.core.Duration]=None, disable_scale_in: typing.Optional[bool]=None, estimated_instance_warmup: typing.Optional[aws_cdk.core.Duration]=None) -> "TargetTrackingScalingPolicy":
        """Scale out or in to achieve a target network ingress rate.

        Arguments:
            id: -
            props: -
            target_bytes_per_second: Target average bytes/seconds on each instance.
            cooldown: Period after a scaling completes before another scaling activity can start. Default: - The default cooldown configured on the AutoScalingGroup.
            disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the autoscaling group. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the group. Default: false
            estimated_instance_warmup: Estimated time until a newly launched instance can send metrics to CloudWatch. Default: - Same as the cooldown.

        Stability:
            experimental
        """
        props: NetworkUtilizationScalingProps = {"targetBytesPerSecond": target_bytes_per_second}

        if cooldown is not None:
            props["cooldown"] = cooldown

        if disable_scale_in is not None:
            props["disableScaleIn"] = disable_scale_in

        if estimated_instance_warmup is not None:
            props["estimatedInstanceWarmup"] = estimated_instance_warmup

        return jsii.invoke(self, "scaleOnIncomingBytes", [id, props])

    @jsii.member(jsii_name="scaleOnMetric")
    def scale_on_metric(self, id: str, *, metric: aws_cdk.aws_cloudwatch.IMetric, scaling_steps: typing.List["ScalingInterval"], adjustment_type: typing.Optional["AdjustmentType"]=None, cooldown: typing.Optional[aws_cdk.core.Duration]=None, estimated_instance_warmup: typing.Optional[aws_cdk.core.Duration]=None, min_adjustment_magnitude: typing.Optional[jsii.Number]=None) -> "StepScalingPolicy":
        """Scale out or in, in response to a metric.

        Arguments:
            id: -
            props: -
            metric: Metric to scale on.
            scaling_steps: The intervals for scaling. Maps a range of metric values to a particular scaling behavior.
            adjustment_type: How the adjustment numbers inside 'intervals' are interpreted. Default: ChangeInCapacity
            cooldown: Grace period after scaling activity. Default: Default cooldown period on your AutoScalingGroup
            estimated_instance_warmup: Estimated time until a newly launched instance can send metrics to CloudWatch. Default: Same as the cooldown
            min_adjustment_magnitude: Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect

        Stability:
            experimental
        """
        props: BasicStepScalingPolicyProps = {"metric": metric, "scalingSteps": scaling_steps}

        if adjustment_type is not None:
            props["adjustmentType"] = adjustment_type

        if cooldown is not None:
            props["cooldown"] = cooldown

        if estimated_instance_warmup is not None:
            props["estimatedInstanceWarmup"] = estimated_instance_warmup

        if min_adjustment_magnitude is not None:
            props["minAdjustmentMagnitude"] = min_adjustment_magnitude

        return jsii.invoke(self, "scaleOnMetric", [id, props])

    @jsii.member(jsii_name="scaleOnOutgoingBytes")
    def scale_on_outgoing_bytes(self, id: str, *, target_bytes_per_second: jsii.Number, cooldown: typing.Optional[aws_cdk.core.Duration]=None, disable_scale_in: typing.Optional[bool]=None, estimated_instance_warmup: typing.Optional[aws_cdk.core.Duration]=None) -> "TargetTrackingScalingPolicy":
        """Scale out or in to achieve a target network egress rate.

        Arguments:
            id: -
            props: -
            target_bytes_per_second: Target average bytes/seconds on each instance.
            cooldown: Period after a scaling completes before another scaling activity can start. Default: - The default cooldown configured on the AutoScalingGroup.
            disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the autoscaling group. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the group. Default: false
            estimated_instance_warmup: Estimated time until a newly launched instance can send metrics to CloudWatch. Default: - Same as the cooldown.

        Stability:
            experimental
        """
        props: NetworkUtilizationScalingProps = {"targetBytesPerSecond": target_bytes_per_second}

        if cooldown is not None:
            props["cooldown"] = cooldown

        if disable_scale_in is not None:
            props["disableScaleIn"] = disable_scale_in

        if estimated_instance_warmup is not None:
            props["estimatedInstanceWarmup"] = estimated_instance_warmup

        return jsii.invoke(self, "scaleOnOutgoingBytes", [id, props])

    @jsii.member(jsii_name="scaleOnRequestCount")
    def scale_on_request_count(self, id: str, *, target_requests_per_second: jsii.Number, cooldown: typing.Optional[aws_cdk.core.Duration]=None, disable_scale_in: typing.Optional[bool]=None, estimated_instance_warmup: typing.Optional[aws_cdk.core.Duration]=None) -> "TargetTrackingScalingPolicy":
        """Scale out or in to achieve a target request handling rate.

        The AutoScalingGroup must have been attached to an Application Load Balancer
        in order to be able to call this.

        Arguments:
            id: -
            props: -
            target_requests_per_second: Target average requests/seconds on each instance.
            cooldown: Period after a scaling completes before another scaling activity can start. Default: - The default cooldown configured on the AutoScalingGroup.
            disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the autoscaling group. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the group. Default: false
            estimated_instance_warmup: Estimated time until a newly launched instance can send metrics to CloudWatch. Default: - Same as the cooldown.

        Stability:
            experimental
        """
        props: RequestCountScalingProps = {"targetRequestsPerSecond": target_requests_per_second}

        if cooldown is not None:
            props["cooldown"] = cooldown

        if disable_scale_in is not None:
            props["disableScaleIn"] = disable_scale_in

        if estimated_instance_warmup is not None:
            props["estimatedInstanceWarmup"] = estimated_instance_warmup

        return jsii.invoke(self, "scaleOnRequestCount", [id, props])

    @jsii.member(jsii_name="scaleOnSchedule")
    def scale_on_schedule(self, id: str, *, schedule: "Schedule", desired_capacity: typing.Optional[jsii.Number]=None, end_time: typing.Optional[datetime.datetime]=None, max_capacity: typing.Optional[jsii.Number]=None, min_capacity: typing.Optional[jsii.Number]=None, start_time: typing.Optional[datetime.datetime]=None) -> "ScheduledAction":
        """Scale out or in based on time.

        Arguments:
            id: -
            props: -
            schedule: When to perform this action. Supports cron expressions. For more information about cron expressions, see https://en.wikipedia.org/wiki/Cron.
            desired_capacity: The new desired capacity. At the scheduled time, set the desired capacity to the given capacity. At least one of maxCapacity, minCapacity, or desiredCapacity must be supplied. Default: - No new desired capacity.
            end_time: When this scheduled action expires. Default: - The rule never expires.
            max_capacity: The new maximum capacity. At the scheduled time, set the maximum capacity to the given capacity. At least one of maxCapacity, minCapacity, or desiredCapacity must be supplied. Default: - No new maximum capacity.
            min_capacity: The new minimum capacity. At the scheduled time, set the minimum capacity to the given capacity. At least one of maxCapacity, minCapacity, or desiredCapacity must be supplied. Default: - No new minimum capacity.
            start_time: When this scheduled action becomes active. Default: - The rule is activate immediately.

        Stability:
            experimental
        """
        props: BasicScheduledActionProps = {"schedule": schedule}

        if desired_capacity is not None:
            props["desiredCapacity"] = desired_capacity

        if end_time is not None:
            props["endTime"] = end_time

        if max_capacity is not None:
            props["maxCapacity"] = max_capacity

        if min_capacity is not None:
            props["minCapacity"] = min_capacity

        if start_time is not None:
            props["startTime"] = start_time

        return jsii.invoke(self, "scaleOnSchedule", [id, props])

    @jsii.member(jsii_name="scaleToTrackMetric")
    def scale_to_track_metric(self, id: str, *, metric: aws_cdk.aws_cloudwatch.IMetric, target_value: jsii.Number, cooldown: typing.Optional[aws_cdk.core.Duration]=None, disable_scale_in: typing.Optional[bool]=None, estimated_instance_warmup: typing.Optional[aws_cdk.core.Duration]=None) -> "TargetTrackingScalingPolicy":
        """Scale out or in in order to keep a metric around a target value.

        Arguments:
            id: -
            props: -
            metric: Metric to track. The metric must represent a utilization, so that if it's higher than the target value, your ASG should scale out, and if it's lower it should scale in.
            target_value: Value to keep the metric around.
            cooldown: Period after a scaling completes before another scaling activity can start. Default: - The default cooldown configured on the AutoScalingGroup.
            disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the autoscaling group. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the group. Default: false
            estimated_instance_warmup: Estimated time until a newly launched instance can send metrics to CloudWatch. Default: - Same as the cooldown.

        Stability:
            experimental
        """
        props: MetricTargetTrackingProps = {"metric": metric, "targetValue": target_value}

        if cooldown is not None:
            props["cooldown"] = cooldown

        if disable_scale_in is not None:
            props["disableScaleIn"] = disable_scale_in

        if estimated_instance_warmup is not None:
            props["estimatedInstanceWarmup"] = estimated_instance_warmup

        return jsii.invoke(self, "scaleToTrackMetric", [id, props])

    @property
    @jsii.member(jsii_name="autoScalingGroupArn")
    def auto_scaling_group_arn(self) -> str:
        """Arn of the AutoScalingGroup.

        Stability:
            experimental
        """
        return jsii.get(self, "autoScalingGroupArn")

    @property
    @jsii.member(jsii_name="autoScalingGroupName")
    def auto_scaling_group_name(self) -> str:
        """Name of the AutoScalingGroup.

        Stability:
            experimental
        """
        return jsii.get(self, "autoScalingGroupName")

    @property
    @jsii.member(jsii_name="connections")
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        """Allows specify security group connections for instances of this fleet.

        Stability:
            experimental
        """
        return jsii.get(self, "connections")

    @property
    @jsii.member(jsii_name="osType")
    def os_type(self) -> aws_cdk.aws_ec2.OperatingSystemType:
        """The type of OS instances of this fleet are running.

        Stability:
            experimental
        """
        return jsii.get(self, "osType")

    @property
    @jsii.member(jsii_name="role")
    def role(self) -> aws_cdk.aws_iam.IRole:
        """The IAM role assumed by instances of this fleet.

        Stability:
            experimental
        """
        return jsii.get(self, "role")

    @property
    @jsii.member(jsii_name="userData")
    def user_data(self) -> aws_cdk.aws_ec2.UserData:
        """UserData for the instances.

        Stability:
            experimental
        """
        return jsii.get(self, "userData")

    @property
    @jsii.member(jsii_name="albTargetGroup")
    def _alb_target_group(self) -> typing.Optional[aws_cdk.aws_elasticloadbalancingv2.ApplicationTargetGroup]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "albTargetGroup")

    @_alb_target_group.setter
    def _alb_target_group(self, value: typing.Optional[aws_cdk.aws_elasticloadbalancingv2.ApplicationTargetGroup]):
        return jsii.set(self, "albTargetGroup", value)


@jsii.interface(jsii_type="@aws-cdk/aws-autoscaling.ILifecycleHook")
class ILifecycleHook(aws_cdk.core.IResource, jsii.compat.Protocol):
    """A basic lifecycle hook object.

    Stability:
        experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _ILifecycleHookProxy

    @property
    @jsii.member(jsii_name="role")
    def role(self) -> aws_cdk.aws_iam.IRole:
        """The role for the lifecycle hook to execute.

        Stability:
            experimental
        """
        ...


class _ILifecycleHookProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """A basic lifecycle hook object.

    Stability:
        experimental
    """
    __jsii_type__ = "@aws-cdk/aws-autoscaling.ILifecycleHook"
    @property
    @jsii.member(jsii_name="role")
    def role(self) -> aws_cdk.aws_iam.IRole:
        """The role for the lifecycle hook to execute.

        Stability:
            experimental
        """
        return jsii.get(self, "role")


@jsii.interface(jsii_type="@aws-cdk/aws-autoscaling.ILifecycleHookTarget")
class ILifecycleHookTarget(jsii.compat.Protocol):
    """Interface for autoscaling lifecycle hook targets.

    Stability:
        experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _ILifecycleHookTargetProxy

    @jsii.member(jsii_name="bind")
    def bind(self, scope: aws_cdk.core.Construct, lifecycle_hook: "ILifecycleHook") -> "LifecycleHookTargetConfig":
        """Called when this object is used as the target of a lifecycle hook.

        Arguments:
            scope: -
            lifecycle_hook: -

        Stability:
            experimental
        """
        ...


class _ILifecycleHookTargetProxy():
    """Interface for autoscaling lifecycle hook targets.

    Stability:
        experimental
    """
    __jsii_type__ = "@aws-cdk/aws-autoscaling.ILifecycleHookTarget"
    @jsii.member(jsii_name="bind")
    def bind(self, scope: aws_cdk.core.Construct, lifecycle_hook: "ILifecycleHook") -> "LifecycleHookTargetConfig":
        """Called when this object is used as the target of a lifecycle hook.

        Arguments:
            scope: -
            lifecycle_hook: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "bind", [scope, lifecycle_hook])


@jsii.implements(ILifecycleHook)
class LifecycleHook(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-autoscaling.LifecycleHook"):
    """Define a life cycle hook.

    Stability:
        experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, auto_scaling_group: "IAutoScalingGroup", lifecycle_transition: "LifecycleTransition", notification_target: "ILifecycleHookTarget", default_result: typing.Optional["DefaultResult"]=None, heartbeat_timeout: typing.Optional[aws_cdk.core.Duration]=None, lifecycle_hook_name: typing.Optional[str]=None, notification_metadata: typing.Optional[str]=None, role: typing.Optional[aws_cdk.aws_iam.IRole]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            auto_scaling_group: The AutoScalingGroup to add the lifecycle hook to.
            lifecycle_transition: The state of the Amazon EC2 instance to which you want to attach the lifecycle hook.
            notification_target: The target of the lifecycle hook.
            default_result: The action the Auto Scaling group takes when the lifecycle hook timeout elapses or if an unexpected failure occurs. Default: Continue
            heartbeat_timeout: Maximum time between calls to RecordLifecycleActionHeartbeat for the hook. If the lifecycle hook times out, perform the action in DefaultResult. Default: - No heartbeat timeout.
            lifecycle_hook_name: Name of the lifecycle hook. Default: - Automatically generated name.
            notification_metadata: Additional data to pass to the lifecycle hook target. Default: - No metadata.
            role: The role that allows publishing to the notification target. Default: - A role is automatically created.

        Stability:
            experimental
        """
        props: LifecycleHookProps = {"autoScalingGroup": auto_scaling_group, "lifecycleTransition": lifecycle_transition, "notificationTarget": notification_target}

        if default_result is not None:
            props["defaultResult"] = default_result

        if heartbeat_timeout is not None:
            props["heartbeatTimeout"] = heartbeat_timeout

        if lifecycle_hook_name is not None:
            props["lifecycleHookName"] = lifecycle_hook_name

        if notification_metadata is not None:
            props["notificationMetadata"] = notification_metadata

        if role is not None:
            props["role"] = role

        jsii.create(LifecycleHook, self, [scope, id, props])

    @property
    @jsii.member(jsii_name="lifecycleHookName")
    def lifecycle_hook_name(self) -> str:
        """The name of this lifecycle hook.

        Stability:
            experimental
        attribute:
            true
        """
        return jsii.get(self, "lifecycleHookName")

    @property
    @jsii.member(jsii_name="role")
    def role(self) -> aws_cdk.aws_iam.IRole:
        """The role that allows the ASG to publish to the notification target.

        Stability:
            experimental
        """
        return jsii.get(self, "role")


@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.LifecycleHookProps", jsii_struct_bases=[BasicLifecycleHookProps])
class LifecycleHookProps(BasicLifecycleHookProps, jsii.compat.TypedDict):
    """Properties for a Lifecycle hook.

    Stability:
        experimental
    """
    autoScalingGroup: "IAutoScalingGroup"
    """The AutoScalingGroup to add the lifecycle hook to.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.LifecycleHookTargetConfig", jsii_struct_bases=[])
class LifecycleHookTargetConfig(jsii.compat.TypedDict):
    """Properties to add the target to a lifecycle hook.

    Stability:
        experimental
    """
    notificationTargetArn: str
    """The ARN to use as the notification target.

    Stability:
        experimental
    """

@jsii.enum(jsii_type="@aws-cdk/aws-autoscaling.LifecycleTransition")
class LifecycleTransition(enum.Enum):
    """What instance transition to attach the hook to.

    Stability:
        experimental
    """
    INSTANCE_LAUNCHING = "INSTANCE_LAUNCHING"
    """Execute the hook when an instance is about to be added.

    Stability:
        experimental
    """
    INSTANCE_TERMINATING = "INSTANCE_TERMINATING"
    """Execute the hook when an instance is about to be terminated.

    Stability:
        experimental
    """

@jsii.enum(jsii_type="@aws-cdk/aws-autoscaling.MetricAggregationType")
class MetricAggregationType(enum.Enum):
    """How the scaling metric is going to be aggregated.

    Stability:
        experimental
    """
    AVERAGE = "AVERAGE"
    """Average.

    Stability:
        experimental
    """
    MINIMUM = "MINIMUM"
    """Minimum.

    Stability:
        experimental
    """
    MAXIMUM = "MAXIMUM"
    """Maximum.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.MetricTargetTrackingProps", jsii_struct_bases=[BaseTargetTrackingProps])
class MetricTargetTrackingProps(BaseTargetTrackingProps, jsii.compat.TypedDict):
    """Properties for enabling tracking of an arbitrary metric.

    Stability:
        experimental
    """
    metric: aws_cdk.aws_cloudwatch.IMetric
    """Metric to track.

    The metric must represent a utilization, so that if it's higher than the
    target value, your ASG should scale out, and if it's lower it should
    scale in.

    Stability:
        experimental
    """

    targetValue: jsii.Number
    """Value to keep the metric around.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.NetworkUtilizationScalingProps", jsii_struct_bases=[BaseTargetTrackingProps])
class NetworkUtilizationScalingProps(BaseTargetTrackingProps, jsii.compat.TypedDict):
    """Properties for enabling scaling based on network utilization.

    Stability:
        experimental
    """
    targetBytesPerSecond: jsii.Number
    """Target average bytes/seconds on each instance.

    Stability:
        experimental
    """

@jsii.enum(jsii_type="@aws-cdk/aws-autoscaling.PredefinedMetric")
class PredefinedMetric(enum.Enum):
    """One of the predefined autoscaling metrics.

    Stability:
        experimental
    """
    ASG_AVERAGE_CPU_UTILIZATION = "ASG_AVERAGE_CPU_UTILIZATION"
    """Average CPU utilization of the Auto Scaling group.

    Stability:
        experimental
    """
    ASG_AVERAGE_NETWORK_IN = "ASG_AVERAGE_NETWORK_IN"
    """Average number of bytes received on all network interfaces by the Auto Scaling group.

    Stability:
        experimental
    """
    ASG_AVERAGE_NETWORK_OUT = "ASG_AVERAGE_NETWORK_OUT"
    """Average number of bytes sent out on all network interfaces by the Auto Scaling group.

    Stability:
        experimental
    """
    ALB_REQUEST_COUNT_PER_TARGET = "ALB_REQUEST_COUNT_PER_TARGET"
    """Number of requests completed per target in an Application Load Balancer target group.

    Specify the ALB to look at in the ``resourceLabel`` field.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.RequestCountScalingProps", jsii_struct_bases=[BaseTargetTrackingProps])
class RequestCountScalingProps(BaseTargetTrackingProps, jsii.compat.TypedDict):
    """Properties for enabling scaling based on request/second.

    Stability:
        experimental
    """
    targetRequestsPerSecond: jsii.Number
    """Target average requests/seconds on each instance.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.RollingUpdateConfiguration", jsii_struct_bases=[])
class RollingUpdateConfiguration(jsii.compat.TypedDict, total=False):
    """Additional settings when a rolling update is selected.

    Stability:
        experimental
    """
    maxBatchSize: jsii.Number
    """The maximum number of instances that AWS CloudFormation updates at once.

    Default:
        1

    Stability:
        experimental
    """

    minInstancesInService: jsii.Number
    """The minimum number of instances that must be in service before more instances are replaced.

    This number affects the speed of the replacement.

    Default:
        0

    Stability:
        experimental
    """

    minSuccessfulInstancesPercent: jsii.Number
    """The percentage of instances that must signal success for an update to succeed.

    If an instance doesn't send a signal within the time specified in the
    pauseTime property, AWS CloudFormation assumes that the instance wasn't
    updated.

    This number affects the success of the replacement.

    If you specify this property, you must also enable the
    waitOnResourceSignals and pauseTime properties.

    Default:
        100

    Stability:
        experimental
    """

    pauseTime: aws_cdk.core.Duration
    """The pause time after making a change to a batch of instances.

    This is intended to give those instances time to start software applications.

    Specify PauseTime in the ISO8601 duration format (in the format
    PT#H#M#S, where each # is the number of hours, minutes, and seconds,
    respectively). The maximum PauseTime is one hour (PT1H).

    Default:
        Duration.minutes(5) if the waitOnResourceSignals property is true, otherwise 0

    Stability:
        experimental
    """

    suspendProcesses: typing.List["ScalingProcess"]
    """Specifies the Auto Scaling processes to suspend during a stack update.

    Suspending processes prevents Auto Scaling from interfering with a stack
    update.

    Default:
        HealthCheck, ReplaceUnhealthy, AZRebalance, AlarmNotification, ScheduledActions.

    Stability:
        experimental
    """

    waitOnResourceSignals: bool
    """Specifies whether the Auto Scaling group waits on signals from new instances during an update.

    AWS CloudFormation must receive a signal from each new instance within
    the specified PauseTime before continuing the update.

    To have instances wait for an Elastic Load Balancing health check before
    they signal success, add a health-check verification by using the
    cfn-init helper script. For an example, see the verify_instance_health
    command in the Auto Scaling rolling updates sample template.

    Default:
        true if you specified the minSuccessfulInstancesPercent property, false otherwise

    Stability:
        experimental
    """

@jsii.data_type_optionals(jsii_struct_bases=[])
class _ScalingInterval(jsii.compat.TypedDict, total=False):
    lower: jsii.Number
    """The lower bound of the interval.

    The scaling adjustment will be applied if the metric is higher than this value.

    Default:
        Threshold automatically derived from neighbouring intervals

    Stability:
        experimental
    """
    upper: jsii.Number
    """The upper bound of the interval.

    The scaling adjustment will be applied if the metric is lower than this value.

    Default:
        Threshold automatically derived from neighbouring intervals

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.ScalingInterval", jsii_struct_bases=[_ScalingInterval])
class ScalingInterval(_ScalingInterval):
    """A range of metric values in which to apply a certain scaling operation.

    Stability:
        experimental
    """
    change: jsii.Number
    """The capacity adjustment to apply in this interval.

    The number is interpreted differently based on AdjustmentType:

    - ChangeInCapacity: add the adjustment to the current capacity.
      The number can be positive or negative.
    - PercentChangeInCapacity: add or remove the given percentage of the current
      capacity to itself. The number can be in the range [-100..100].
    - ExactCapacity: set the capacity to this number. The number must
      be positive.

    Stability:
        experimental
    """

@jsii.enum(jsii_type="@aws-cdk/aws-autoscaling.ScalingProcess")
class ScalingProcess(enum.Enum):
    """
    Stability:
        experimental
    """
    LAUNCH = "LAUNCH"
    """
    Stability:
        experimental
    """
    TERMINATE = "TERMINATE"
    """
    Stability:
        experimental
    """
    HEALTH_CHECK = "HEALTH_CHECK"
    """
    Stability:
        experimental
    """
    REPLACE_UNHEALTHY = "REPLACE_UNHEALTHY"
    """
    Stability:
        experimental
    """
    AZ_REBALANCE = "AZ_REBALANCE"
    """
    Stability:
        experimental
    """
    ALARM_NOTIFICATION = "ALARM_NOTIFICATION"
    """
    Stability:
        experimental
    """
    SCHEDULED_ACTIONS = "SCHEDULED_ACTIONS"
    """
    Stability:
        experimental
    """
    ADD_TO_LOAD_BALANCER = "ADD_TO_LOAD_BALANCER"
    """
    Stability:
        experimental
    """

class Schedule(metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-autoscaling.Schedule"):
    """Schedule for scheduled scaling actions.

    Stability:
        experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _ScheduleProxy

    def __init__(self) -> None:
        """
        Stability:
            experimental
        """
        jsii.create(Schedule, self, [])

    @jsii.member(jsii_name="cron")
    @classmethod
    def cron(cls, *, day: typing.Optional[str]=None, hour: typing.Optional[str]=None, minute: typing.Optional[str]=None, month: typing.Optional[str]=None, week_day: typing.Optional[str]=None) -> "Schedule":
        """Create a schedule from a set of cron fields.

        Arguments:
            options: -
            day: The day of the month to run this rule at. Default: - Every day of the month
            hour: The hour to run this rule at. Default: - Every hour
            minute: The minute to run this rule at. Default: - Every minute
            month: The month to run this rule at. Default: - Every month
            week_day: The day of the week to run this rule at. Default: - Any day of the week

        Stability:
            experimental
        """
        options: CronOptions = {}

        if day is not None:
            options["day"] = day

        if hour is not None:
            options["hour"] = hour

        if minute is not None:
            options["minute"] = minute

        if month is not None:
            options["month"] = month

        if week_day is not None:
            options["weekDay"] = week_day

        return jsii.sinvoke(cls, "cron", [options])

    @jsii.member(jsii_name="expression")
    @classmethod
    def expression(cls, expression: str) -> "Schedule":
        """Construct a schedule from a literal schedule expression.

        Arguments:
            expression: The expression to use. Must be in a format that AutoScaling will recognize

        See:
            http://crontab.org/
        Stability:
            experimental
        """
        return jsii.sinvoke(cls, "expression", [expression])

    @property
    @jsii.member(jsii_name="expressionString")
    @abc.abstractmethod
    def expression_string(self) -> str:
        """Retrieve the expression for this schedule.

        Stability:
            experimental
        """
        ...


class _ScheduleProxy(Schedule):
    @property
    @jsii.member(jsii_name="expressionString")
    def expression_string(self) -> str:
        """Retrieve the expression for this schedule.

        Stability:
            experimental
        """
        return jsii.get(self, "expressionString")


class ScheduledAction(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-autoscaling.ScheduledAction"):
    """Define a scheduled scaling action.

    Stability:
        experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, auto_scaling_group: "IAutoScalingGroup", schedule: "Schedule", desired_capacity: typing.Optional[jsii.Number]=None, end_time: typing.Optional[datetime.datetime]=None, max_capacity: typing.Optional[jsii.Number]=None, min_capacity: typing.Optional[jsii.Number]=None, start_time: typing.Optional[datetime.datetime]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            auto_scaling_group: The AutoScalingGroup to apply the scheduled actions to.
            schedule: When to perform this action. Supports cron expressions. For more information about cron expressions, see https://en.wikipedia.org/wiki/Cron.
            desired_capacity: The new desired capacity. At the scheduled time, set the desired capacity to the given capacity. At least one of maxCapacity, minCapacity, or desiredCapacity must be supplied. Default: - No new desired capacity.
            end_time: When this scheduled action expires. Default: - The rule never expires.
            max_capacity: The new maximum capacity. At the scheduled time, set the maximum capacity to the given capacity. At least one of maxCapacity, minCapacity, or desiredCapacity must be supplied. Default: - No new maximum capacity.
            min_capacity: The new minimum capacity. At the scheduled time, set the minimum capacity to the given capacity. At least one of maxCapacity, minCapacity, or desiredCapacity must be supplied. Default: - No new minimum capacity.
            start_time: When this scheduled action becomes active. Default: - The rule is activate immediately.

        Stability:
            experimental
        """
        props: ScheduledActionProps = {"autoScalingGroup": auto_scaling_group, "schedule": schedule}

        if desired_capacity is not None:
            props["desiredCapacity"] = desired_capacity

        if end_time is not None:
            props["endTime"] = end_time

        if max_capacity is not None:
            props["maxCapacity"] = max_capacity

        if min_capacity is not None:
            props["minCapacity"] = min_capacity

        if start_time is not None:
            props["startTime"] = start_time

        jsii.create(ScheduledAction, self, [scope, id, props])


@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.ScheduledActionProps", jsii_struct_bases=[BasicScheduledActionProps])
class ScheduledActionProps(BasicScheduledActionProps, jsii.compat.TypedDict):
    """Properties for a scheduled action on an AutoScalingGroup.

    Stability:
        experimental
    """
    autoScalingGroup: "IAutoScalingGroup"
    """The AutoScalingGroup to apply the scheduled actions to.

    Stability:
        experimental
    """

class StepScalingAction(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-autoscaling.StepScalingAction"):
    """Define a step scaling action.

    This kind of scaling policy adjusts the target capacity in configurable
    steps. The size of the step is configurable based on the metric's distance
    to its alarm threshold.

    This Action must be used as the target of a CloudWatch alarm to take effect.

    Stability:
        experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, auto_scaling_group: "IAutoScalingGroup", adjustment_type: typing.Optional["AdjustmentType"]=None, cooldown: typing.Optional[aws_cdk.core.Duration]=None, estimated_instance_warmup: typing.Optional[aws_cdk.core.Duration]=None, metric_aggregation_type: typing.Optional["MetricAggregationType"]=None, min_adjustment_magnitude: typing.Optional[jsii.Number]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            auto_scaling_group: The auto scaling group.
            adjustment_type: How the adjustment numbers are interpreted. Default: ChangeInCapacity
            cooldown: Period after a scaling completes before another scaling activity can start. Default: The default cooldown configured on the AutoScalingGroup
            estimated_instance_warmup: Estimated time until a newly launched instance can send metrics to CloudWatch. Default: Same as the cooldown
            metric_aggregation_type: The aggregation type for the CloudWatch metrics. Default: Average
            min_adjustment_magnitude: Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect

        Stability:
            experimental
        """
        props: StepScalingActionProps = {"autoScalingGroup": auto_scaling_group}

        if adjustment_type is not None:
            props["adjustmentType"] = adjustment_type

        if cooldown is not None:
            props["cooldown"] = cooldown

        if estimated_instance_warmup is not None:
            props["estimatedInstanceWarmup"] = estimated_instance_warmup

        if metric_aggregation_type is not None:
            props["metricAggregationType"] = metric_aggregation_type

        if min_adjustment_magnitude is not None:
            props["minAdjustmentMagnitude"] = min_adjustment_magnitude

        jsii.create(StepScalingAction, self, [scope, id, props])

    @jsii.member(jsii_name="addAdjustment")
    def add_adjustment(self, *, adjustment: jsii.Number, lower_bound: typing.Optional[jsii.Number]=None, upper_bound: typing.Optional[jsii.Number]=None) -> None:
        """Add an adjusment interval to the ScalingAction.

        Arguments:
            adjustment: -
            adjustment: What number to adjust the capacity with. The number is interpeted as an added capacity, a new fixed capacity or an added percentage depending on the AdjustmentType value of the StepScalingPolicy. Can be positive or negative.
            lower_bound: Lower bound where this scaling tier applies. The scaling tier applies if the difference between the metric value and its alarm threshold is higher than this value. Default: -Infinity if this is the first tier, otherwise the upperBound of the previous tier
            upper_bound: Upper bound where this scaling tier applies. The scaling tier applies if the difference between the metric value and its alarm threshold is lower than this value. Default: +Infinity

        Stability:
            experimental
        """
        adjustment: AdjustmentTier = {"adjustment": adjustment}

        if lower_bound is not None:
            adjustment["lowerBound"] = lower_bound

        if upper_bound is not None:
            adjustment["upperBound"] = upper_bound

        return jsii.invoke(self, "addAdjustment", [adjustment])

    @property
    @jsii.member(jsii_name="scalingPolicyArn")
    def scaling_policy_arn(self) -> str:
        """ARN of the scaling policy.

        Stability:
            experimental
        """
        return jsii.get(self, "scalingPolicyArn")


@jsii.data_type_optionals(jsii_struct_bases=[])
class _StepScalingActionProps(jsii.compat.TypedDict, total=False):
    adjustmentType: "AdjustmentType"
    """How the adjustment numbers are interpreted.

    Default:
        ChangeInCapacity

    Stability:
        experimental
    """
    cooldown: aws_cdk.core.Duration
    """Period after a scaling completes before another scaling activity can start.

    Default:
        The default cooldown configured on the AutoScalingGroup

    Stability:
        experimental
    """
    estimatedInstanceWarmup: aws_cdk.core.Duration
    """Estimated time until a newly launched instance can send metrics to CloudWatch.

    Default:
        Same as the cooldown

    Stability:
        experimental
    """
    metricAggregationType: "MetricAggregationType"
    """The aggregation type for the CloudWatch metrics.

    Default:
        Average

    Stability:
        experimental
    """
    minAdjustmentMagnitude: jsii.Number
    """Minimum absolute number to adjust capacity with as result of percentage scaling.

    Only when using AdjustmentType = PercentChangeInCapacity, this number controls
    the minimum absolute effect size.

    Default:
        No minimum scaling effect

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.StepScalingActionProps", jsii_struct_bases=[_StepScalingActionProps])
class StepScalingActionProps(_StepScalingActionProps):
    """Properties for a scaling policy.

    Stability:
        experimental
    """
    autoScalingGroup: "IAutoScalingGroup"
    """The auto scaling group.

    Stability:
        experimental
    """

class StepScalingPolicy(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-autoscaling.StepScalingPolicy"):
    """Define a acaling strategy which scales depending on absolute values of some metric.

    You can specify the scaling behavior for various values of the metric.

    Implemented using one or more CloudWatch alarms and Step Scaling Policies.

    Stability:
        experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, auto_scaling_group: "IAutoScalingGroup", metric: aws_cdk.aws_cloudwatch.IMetric, scaling_steps: typing.List["ScalingInterval"], adjustment_type: typing.Optional["AdjustmentType"]=None, cooldown: typing.Optional[aws_cdk.core.Duration]=None, estimated_instance_warmup: typing.Optional[aws_cdk.core.Duration]=None, min_adjustment_magnitude: typing.Optional[jsii.Number]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            auto_scaling_group: The auto scaling group.
            metric: Metric to scale on.
            scaling_steps: The intervals for scaling. Maps a range of metric values to a particular scaling behavior.
            adjustment_type: How the adjustment numbers inside 'intervals' are interpreted. Default: ChangeInCapacity
            cooldown: Grace period after scaling activity. Default: Default cooldown period on your AutoScalingGroup
            estimated_instance_warmup: Estimated time until a newly launched instance can send metrics to CloudWatch. Default: Same as the cooldown
            min_adjustment_magnitude: Minimum absolute number to adjust capacity with as result of percentage scaling. Only when using AdjustmentType = PercentChangeInCapacity, this number controls the minimum absolute effect size. Default: No minimum scaling effect

        Stability:
            experimental
        """
        props: StepScalingPolicyProps = {"autoScalingGroup": auto_scaling_group, "metric": metric, "scalingSteps": scaling_steps}

        if adjustment_type is not None:
            props["adjustmentType"] = adjustment_type

        if cooldown is not None:
            props["cooldown"] = cooldown

        if estimated_instance_warmup is not None:
            props["estimatedInstanceWarmup"] = estimated_instance_warmup

        if min_adjustment_magnitude is not None:
            props["minAdjustmentMagnitude"] = min_adjustment_magnitude

        jsii.create(StepScalingPolicy, self, [scope, id, props])

    @property
    @jsii.member(jsii_name="lowerAction")
    def lower_action(self) -> typing.Optional["StepScalingAction"]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "lowerAction")

    @property
    @jsii.member(jsii_name="lowerAlarm")
    def lower_alarm(self) -> typing.Optional[aws_cdk.aws_cloudwatch.Alarm]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "lowerAlarm")

    @property
    @jsii.member(jsii_name="upperAction")
    def upper_action(self) -> typing.Optional["StepScalingAction"]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "upperAction")

    @property
    @jsii.member(jsii_name="upperAlarm")
    def upper_alarm(self) -> typing.Optional[aws_cdk.aws_cloudwatch.Alarm]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "upperAlarm")


@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.StepScalingPolicyProps", jsii_struct_bases=[BasicStepScalingPolicyProps])
class StepScalingPolicyProps(BasicStepScalingPolicyProps, jsii.compat.TypedDict):
    """
    Stability:
        experimental
    """
    autoScalingGroup: "IAutoScalingGroup"
    """The auto scaling group.

    Stability:
        experimental
    """

class TargetTrackingScalingPolicy(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-autoscaling.TargetTrackingScalingPolicy"):
    """
    Stability:
        experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, auto_scaling_group: "IAutoScalingGroup", target_value: jsii.Number, custom_metric: typing.Optional[aws_cdk.aws_cloudwatch.IMetric]=None, predefined_metric: typing.Optional["PredefinedMetric"]=None, resource_label: typing.Optional[str]=None, cooldown: typing.Optional[aws_cdk.core.Duration]=None, disable_scale_in: typing.Optional[bool]=None, estimated_instance_warmup: typing.Optional[aws_cdk.core.Duration]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            auto_scaling_group: 
            target_value: The target value for the metric.
            custom_metric: A custom metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No custom metric.
            predefined_metric: A predefined metric for application autoscaling. The metric must track utilization. Scaling out will happen if the metric is higher than the target value, scaling in will happen in the metric is lower than the target value. Exactly one of customMetric or predefinedMetric must be specified. Default: - No predefined metric.
            resource_label: The resource label associated with the predefined metric. Should be supplied if the predefined metric is ALBRequestCountPerTarget, and the format should be: app///targetgroup// Default: - No resource label.
            cooldown: Period after a scaling completes before another scaling activity can start. Default: - The default cooldown configured on the AutoScalingGroup.
            disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the autoscaling group. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the group. Default: false
            estimated_instance_warmup: Estimated time until a newly launched instance can send metrics to CloudWatch. Default: - Same as the cooldown.

        Stability:
            experimental
        """
        props: TargetTrackingScalingPolicyProps = {"autoScalingGroup": auto_scaling_group, "targetValue": target_value}

        if custom_metric is not None:
            props["customMetric"] = custom_metric

        if predefined_metric is not None:
            props["predefinedMetric"] = predefined_metric

        if resource_label is not None:
            props["resourceLabel"] = resource_label

        if cooldown is not None:
            props["cooldown"] = cooldown

        if disable_scale_in is not None:
            props["disableScaleIn"] = disable_scale_in

        if estimated_instance_warmup is not None:
            props["estimatedInstanceWarmup"] = estimated_instance_warmup

        jsii.create(TargetTrackingScalingPolicy, self, [scope, id, props])

    @property
    @jsii.member(jsii_name="scalingPolicyArn")
    def scaling_policy_arn(self) -> str:
        """ARN of the scaling policy.

        Stability:
            experimental
        """
        return jsii.get(self, "scalingPolicyArn")


@jsii.data_type(jsii_type="@aws-cdk/aws-autoscaling.TargetTrackingScalingPolicyProps", jsii_struct_bases=[BasicTargetTrackingScalingPolicyProps])
class TargetTrackingScalingPolicyProps(BasicTargetTrackingScalingPolicyProps, jsii.compat.TypedDict):
    """Properties for a concrete TargetTrackingPolicy.

    Adds the scalingTarget.

    Stability:
        experimental
    """
    autoScalingGroup: "IAutoScalingGroup"
    """
    Stability:
        experimental
    """

@jsii.enum(jsii_type="@aws-cdk/aws-autoscaling.UpdateType")
class UpdateType(enum.Enum):
    """The type of update to perform on instances in this AutoScalingGroup.

    Stability:
        experimental
    """
    NONE = "NONE"
    """Don't do anything.

    Stability:
        experimental
    """
    REPLACING_UPDATE = "REPLACING_UPDATE"
    """Replace the entire AutoScalingGroup.

    Builds a new AutoScalingGroup first, then delete the old one.

    Stability:
        experimental
    """
    ROLLING_UPDATE = "ROLLING_UPDATE"
    """Replace the instances in the AutoScalingGroup.

    Stability:
        experimental
    """

__all__ = ["AdjustmentTier", "AdjustmentType", "AutoScalingGroup", "AutoScalingGroupProps", "BaseTargetTrackingProps", "BasicLifecycleHookProps", "BasicScheduledActionProps", "BasicStepScalingPolicyProps", "BasicTargetTrackingScalingPolicyProps", "CfnAutoScalingGroup", "CfnAutoScalingGroupProps", "CfnLaunchConfiguration", "CfnLaunchConfigurationProps", "CfnLifecycleHook", "CfnLifecycleHookProps", "CfnScalingPolicy", "CfnScalingPolicyProps", "CfnScheduledAction", "CfnScheduledActionProps", "CommonAutoScalingGroupProps", "CpuUtilizationScalingProps", "CronOptions", "DefaultResult", "IAutoScalingGroup", "ILifecycleHook", "ILifecycleHookTarget", "LifecycleHook", "LifecycleHookProps", "LifecycleHookTargetConfig", "LifecycleTransition", "MetricAggregationType", "MetricTargetTrackingProps", "NetworkUtilizationScalingProps", "PredefinedMetric", "RequestCountScalingProps", "RollingUpdateConfiguration", "ScalingInterval", "ScalingProcess", "Schedule", "ScheduledAction", "ScheduledActionProps", "StepScalingAction", "StepScalingActionProps", "StepScalingPolicy", "StepScalingPolicyProps", "TargetTrackingScalingPolicy", "TargetTrackingScalingPolicyProps", "UpdateType", "__jsii_assembly__"]

publication.publish()
