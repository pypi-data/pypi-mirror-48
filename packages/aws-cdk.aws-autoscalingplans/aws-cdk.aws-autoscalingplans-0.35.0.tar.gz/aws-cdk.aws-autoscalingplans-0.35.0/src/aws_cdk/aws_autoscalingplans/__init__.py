import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.cdk
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-autoscalingplans", "0.35.0", __name__, "aws-autoscalingplans@0.35.0.jsii.tgz")
class CfnScalingPlan(aws_cdk.cdk.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlan"):
    """A CloudFormation ``AWS::AutoScalingPlans::ScalingPlan``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html
    Stability:
        experimental
    cloudformationResource:
        AWS::AutoScalingPlans::ScalingPlan
    """
    def __init__(self, scope: aws_cdk.cdk.Construct, id: str, *, application_source: typing.Union["ApplicationSourceProperty", aws_cdk.cdk.IResolvable], scaling_instructions: typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "ScalingInstructionProperty"]]]) -> None:
        """Create a new ``AWS::AutoScalingPlans::ScalingPlan``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            applicationSource: ``AWS::AutoScalingPlans::ScalingPlan.ApplicationSource``.
            scalingInstructions: ``AWS::AutoScalingPlans::ScalingPlan.ScalingInstructions``.

        Stability:
            experimental
        """
        props: CfnScalingPlanProps = {"applicationSource": application_source, "scalingInstructions": scaling_instructions}

        jsii.create(CfnScalingPlan, self, [scope, id, props])

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(self, props: typing.Mapping[str,typing.Any]) -> typing.Mapping[str,typing.Any]:
        """
        Arguments:
            props: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "renderProperties", [props])

    @classproperty
    @jsii.member(jsii_name="cfnResourceTypeName")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class.

        Stability:
            experimental
        """
        return jsii.sget(cls, "cfnResourceTypeName")

    @property
    @jsii.member(jsii_name="attrScalingPlanName")
    def attr_scaling_plan_name(self) -> str:
        """
        Stability:
            experimental
        cloudformationAttribute:
            ScalingPlanName
        """
        return jsii.get(self, "attrScalingPlanName")

    @property
    @jsii.member(jsii_name="attrScalingPlanVersion")
    def attr_scaling_plan_version(self) -> str:
        """
        Stability:
            experimental
        cloudformationAttribute:
            ScalingPlanVersion
        """
        return jsii.get(self, "attrScalingPlanVersion")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="applicationSource")
    def application_source(self) -> typing.Union["ApplicationSourceProperty", aws_cdk.cdk.IResolvable]:
        """``AWS::AutoScalingPlans::ScalingPlan.ApplicationSource``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html#cfn-autoscalingplans-scalingplan-applicationsource
        Stability:
            experimental
        """
        return jsii.get(self, "applicationSource")

    @application_source.setter
    def application_source(self, value: typing.Union["ApplicationSourceProperty", aws_cdk.cdk.IResolvable]):
        return jsii.set(self, "applicationSource", value)

    @property
    @jsii.member(jsii_name="scalingInstructions")
    def scaling_instructions(self) -> typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "ScalingInstructionProperty"]]]:
        """``AWS::AutoScalingPlans::ScalingPlan.ScalingInstructions``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html#cfn-autoscalingplans-scalingplan-scalinginstructions
        Stability:
            experimental
        """
        return jsii.get(self, "scalingInstructions")

    @scaling_instructions.setter
    def scaling_instructions(self, value: typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "ScalingInstructionProperty"]]]):
        return jsii.set(self, "scalingInstructions", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlan.ApplicationSourceProperty", jsii_struct_bases=[])
    class ApplicationSourceProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-applicationsource.html
        Stability:
            experimental
        """
        cloudFormationStackArn: str
        """``CfnScalingPlan.ApplicationSourceProperty.CloudFormationStackARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-applicationsource.html#cfn-autoscalingplans-scalingplan-applicationsource-cloudformationstackarn
        Stability:
            experimental
        """

        tagFilters: typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "CfnScalingPlan.TagFilterProperty"]]]
        """``CfnScalingPlan.ApplicationSourceProperty.TagFilters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-applicationsource.html#cfn-autoscalingplans-scalingplan-applicationsource-tagfilters
        Stability:
            experimental
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _CustomizedLoadMetricSpecificationProperty(jsii.compat.TypedDict, total=False):
        dimensions: typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "CfnScalingPlan.MetricDimensionProperty"]]]
        """``CfnScalingPlan.CustomizedLoadMetricSpecificationProperty.Dimensions``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedloadmetricspecification-dimensions
        Stability:
            experimental
        """
        unit: str
        """``CfnScalingPlan.CustomizedLoadMetricSpecificationProperty.Unit``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedloadmetricspecification-unit
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlan.CustomizedLoadMetricSpecificationProperty", jsii_struct_bases=[_CustomizedLoadMetricSpecificationProperty])
    class CustomizedLoadMetricSpecificationProperty(_CustomizedLoadMetricSpecificationProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedloadmetricspecification.html
        Stability:
            experimental
        """
        metricName: str
        """``CfnScalingPlan.CustomizedLoadMetricSpecificationProperty.MetricName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedloadmetricspecification-metricname
        Stability:
            experimental
        """

        namespace: str
        """``CfnScalingPlan.CustomizedLoadMetricSpecificationProperty.Namespace``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedloadmetricspecification-namespace
        Stability:
            experimental
        """

        statistic: str
        """``CfnScalingPlan.CustomizedLoadMetricSpecificationProperty.Statistic``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedloadmetricspecification-statistic
        Stability:
            experimental
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _CustomizedScalingMetricSpecificationProperty(jsii.compat.TypedDict, total=False):
        dimensions: typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "CfnScalingPlan.MetricDimensionProperty"]]]
        """``CfnScalingPlan.CustomizedScalingMetricSpecificationProperty.Dimensions``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedscalingmetricspecification-dimensions
        Stability:
            experimental
        """
        unit: str
        """``CfnScalingPlan.CustomizedScalingMetricSpecificationProperty.Unit``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedscalingmetricspecification-unit
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlan.CustomizedScalingMetricSpecificationProperty", jsii_struct_bases=[_CustomizedScalingMetricSpecificationProperty])
    class CustomizedScalingMetricSpecificationProperty(_CustomizedScalingMetricSpecificationProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html
        Stability:
            experimental
        """
        metricName: str
        """``CfnScalingPlan.CustomizedScalingMetricSpecificationProperty.MetricName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedscalingmetricspecification-metricname
        Stability:
            experimental
        """

        namespace: str
        """``CfnScalingPlan.CustomizedScalingMetricSpecificationProperty.Namespace``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedscalingmetricspecification-namespace
        Stability:
            experimental
        """

        statistic: str
        """``CfnScalingPlan.CustomizedScalingMetricSpecificationProperty.Statistic``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-customizedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-customizedscalingmetricspecification-statistic
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlan.MetricDimensionProperty", jsii_struct_bases=[])
    class MetricDimensionProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-metricdimension.html
        Stability:
            experimental
        """
        name: str
        """``CfnScalingPlan.MetricDimensionProperty.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-metricdimension.html#cfn-autoscalingplans-scalingplan-metricdimension-name
        Stability:
            experimental
        """

        value: str
        """``CfnScalingPlan.MetricDimensionProperty.Value``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-metricdimension.html#cfn-autoscalingplans-scalingplan-metricdimension-value
        Stability:
            experimental
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _PredefinedLoadMetricSpecificationProperty(jsii.compat.TypedDict, total=False):
        resourceLabel: str
        """``CfnScalingPlan.PredefinedLoadMetricSpecificationProperty.ResourceLabel``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-predefinedloadmetricspecification-resourcelabel
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlan.PredefinedLoadMetricSpecificationProperty", jsii_struct_bases=[_PredefinedLoadMetricSpecificationProperty])
    class PredefinedLoadMetricSpecificationProperty(_PredefinedLoadMetricSpecificationProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedloadmetricspecification.html
        Stability:
            experimental
        """
        predefinedLoadMetricType: str
        """``CfnScalingPlan.PredefinedLoadMetricSpecificationProperty.PredefinedLoadMetricType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedloadmetricspecification.html#cfn-autoscalingplans-scalingplan-predefinedloadmetricspecification-predefinedloadmetrictype
        Stability:
            experimental
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _PredefinedScalingMetricSpecificationProperty(jsii.compat.TypedDict, total=False):
        resourceLabel: str
        """``CfnScalingPlan.PredefinedScalingMetricSpecificationProperty.ResourceLabel``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-predefinedscalingmetricspecification-resourcelabel
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlan.PredefinedScalingMetricSpecificationProperty", jsii_struct_bases=[_PredefinedScalingMetricSpecificationProperty])
    class PredefinedScalingMetricSpecificationProperty(_PredefinedScalingMetricSpecificationProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedscalingmetricspecification.html
        Stability:
            experimental
        """
        predefinedScalingMetricType: str
        """``CfnScalingPlan.PredefinedScalingMetricSpecificationProperty.PredefinedScalingMetricType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-predefinedscalingmetricspecification.html#cfn-autoscalingplans-scalingplan-predefinedscalingmetricspecification-predefinedscalingmetrictype
        Stability:
            experimental
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _ScalingInstructionProperty(jsii.compat.TypedDict, total=False):
        customizedLoadMetricSpecification: typing.Union[aws_cdk.cdk.IResolvable, "CfnScalingPlan.CustomizedLoadMetricSpecificationProperty"]
        """``CfnScalingPlan.ScalingInstructionProperty.CustomizedLoadMetricSpecification``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-customizedloadmetricspecification
        Stability:
            experimental
        """
        disableDynamicScaling: typing.Union[bool, aws_cdk.cdk.IResolvable]
        """``CfnScalingPlan.ScalingInstructionProperty.DisableDynamicScaling``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-disabledynamicscaling
        Stability:
            experimental
        """
        predefinedLoadMetricSpecification: typing.Union[aws_cdk.cdk.IResolvable, "CfnScalingPlan.PredefinedLoadMetricSpecificationProperty"]
        """``CfnScalingPlan.ScalingInstructionProperty.PredefinedLoadMetricSpecification``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-predefinedloadmetricspecification
        Stability:
            experimental
        """
        predictiveScalingMaxCapacityBehavior: str
        """``CfnScalingPlan.ScalingInstructionProperty.PredictiveScalingMaxCapacityBehavior``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-predictivescalingmaxcapacitybehavior
        Stability:
            experimental
        """
        predictiveScalingMaxCapacityBuffer: jsii.Number
        """``CfnScalingPlan.ScalingInstructionProperty.PredictiveScalingMaxCapacityBuffer``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-predictivescalingmaxcapacitybuffer
        Stability:
            experimental
        """
        predictiveScalingMode: str
        """``CfnScalingPlan.ScalingInstructionProperty.PredictiveScalingMode``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-predictivescalingmode
        Stability:
            experimental
        """
        scalingPolicyUpdateBehavior: str
        """``CfnScalingPlan.ScalingInstructionProperty.ScalingPolicyUpdateBehavior``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-scalingpolicyupdatebehavior
        Stability:
            experimental
        """
        scheduledActionBufferTime: jsii.Number
        """``CfnScalingPlan.ScalingInstructionProperty.ScheduledActionBufferTime``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-scheduledactionbuffertime
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlan.ScalingInstructionProperty", jsii_struct_bases=[_ScalingInstructionProperty])
    class ScalingInstructionProperty(_ScalingInstructionProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html
        Stability:
            experimental
        """
        maxCapacity: jsii.Number
        """``CfnScalingPlan.ScalingInstructionProperty.MaxCapacity``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-maxcapacity
        Stability:
            experimental
        """

        minCapacity: jsii.Number
        """``CfnScalingPlan.ScalingInstructionProperty.MinCapacity``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-mincapacity
        Stability:
            experimental
        """

        resourceId: str
        """``CfnScalingPlan.ScalingInstructionProperty.ResourceId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-resourceid
        Stability:
            experimental
        """

        scalableDimension: str
        """``CfnScalingPlan.ScalingInstructionProperty.ScalableDimension``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-scalabledimension
        Stability:
            experimental
        """

        serviceNamespace: str
        """``CfnScalingPlan.ScalingInstructionProperty.ServiceNamespace``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-servicenamespace
        Stability:
            experimental
        """

        targetTrackingConfigurations: typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "CfnScalingPlan.TargetTrackingConfigurationProperty"]]]
        """``CfnScalingPlan.ScalingInstructionProperty.TargetTrackingConfigurations``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-scalinginstruction.html#cfn-autoscalingplans-scalingplan-scalinginstruction-targettrackingconfigurations
        Stability:
            experimental
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _TagFilterProperty(jsii.compat.TypedDict, total=False):
        values: typing.List[str]
        """``CfnScalingPlan.TagFilterProperty.Values``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-tagfilter.html#cfn-autoscalingplans-scalingplan-tagfilter-values
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlan.TagFilterProperty", jsii_struct_bases=[_TagFilterProperty])
    class TagFilterProperty(_TagFilterProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-tagfilter.html
        Stability:
            experimental
        """
        key: str
        """``CfnScalingPlan.TagFilterProperty.Key``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-tagfilter.html#cfn-autoscalingplans-scalingplan-tagfilter-key
        Stability:
            experimental
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _TargetTrackingConfigurationProperty(jsii.compat.TypedDict, total=False):
        customizedScalingMetricSpecification: typing.Union[aws_cdk.cdk.IResolvable, "CfnScalingPlan.CustomizedScalingMetricSpecificationProperty"]
        """``CfnScalingPlan.TargetTrackingConfigurationProperty.CustomizedScalingMetricSpecification``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-customizedscalingmetricspecification
        Stability:
            experimental
        """
        disableScaleIn: typing.Union[bool, aws_cdk.cdk.IResolvable]
        """``CfnScalingPlan.TargetTrackingConfigurationProperty.DisableScaleIn``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-disablescalein
        Stability:
            experimental
        """
        estimatedInstanceWarmup: jsii.Number
        """``CfnScalingPlan.TargetTrackingConfigurationProperty.EstimatedInstanceWarmup``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-estimatedinstancewarmup
        Stability:
            experimental
        """
        predefinedScalingMetricSpecification: typing.Union[aws_cdk.cdk.IResolvable, "CfnScalingPlan.PredefinedScalingMetricSpecificationProperty"]
        """``CfnScalingPlan.TargetTrackingConfigurationProperty.PredefinedScalingMetricSpecification``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-predefinedscalingmetricspecification
        Stability:
            experimental
        """
        scaleInCooldown: jsii.Number
        """``CfnScalingPlan.TargetTrackingConfigurationProperty.ScaleInCooldown``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-scaleincooldown
        Stability:
            experimental
        """
        scaleOutCooldown: jsii.Number
        """``CfnScalingPlan.TargetTrackingConfigurationProperty.ScaleOutCooldown``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-scaleoutcooldown
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlan.TargetTrackingConfigurationProperty", jsii_struct_bases=[_TargetTrackingConfigurationProperty])
    class TargetTrackingConfigurationProperty(_TargetTrackingConfigurationProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html
        Stability:
            experimental
        """
        targetValue: jsii.Number
        """``CfnScalingPlan.TargetTrackingConfigurationProperty.TargetValue``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscalingplans-scalingplan-targettrackingconfiguration.html#cfn-autoscalingplans-scalingplan-targettrackingconfiguration-targetvalue
        Stability:
            experimental
        """


@jsii.data_type(jsii_type="@aws-cdk/aws-autoscalingplans.CfnScalingPlanProps", jsii_struct_bases=[])
class CfnScalingPlanProps(jsii.compat.TypedDict):
    """Properties for defining a ``AWS::AutoScalingPlans::ScalingPlan``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html
    Stability:
        experimental
    """
    applicationSource: typing.Union["CfnScalingPlan.ApplicationSourceProperty", aws_cdk.cdk.IResolvable]
    """``AWS::AutoScalingPlans::ScalingPlan.ApplicationSource``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html#cfn-autoscalingplans-scalingplan-applicationsource
    Stability:
        experimental
    """

    scalingInstructions: typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "CfnScalingPlan.ScalingInstructionProperty"]]]
    """``AWS::AutoScalingPlans::ScalingPlan.ScalingInstructions``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html#cfn-autoscalingplans-scalingplan-scalinginstructions
    Stability:
        experimental
    """

__all__ = ["CfnScalingPlan", "CfnScalingPlanProps", "__jsii_assembly__"]

publication.publish()
