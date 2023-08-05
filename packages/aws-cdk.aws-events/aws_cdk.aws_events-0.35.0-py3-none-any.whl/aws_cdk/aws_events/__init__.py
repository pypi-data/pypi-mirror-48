import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_iam
import aws_cdk.cdk
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-events", "0.35.0", __name__, "aws-events@0.35.0.jsii.tgz")
class CfnEventBusPolicy(aws_cdk.cdk.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events.CfnEventBusPolicy"):
    """A CloudFormation ``AWS::Events::EventBusPolicy``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html
    Stability:
        experimental
    cloudformationResource:
        AWS::Events::EventBusPolicy
    """
    def __init__(self, scope: aws_cdk.cdk.Construct, id: str, *, action: str, principal: str, statement_id: str, condition: typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional["ConditionProperty"]]]=None) -> None:
        """Create a new ``AWS::Events::EventBusPolicy``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            action: ``AWS::Events::EventBusPolicy.Action``.
            principal: ``AWS::Events::EventBusPolicy.Principal``.
            statementId: ``AWS::Events::EventBusPolicy.StatementId``.
            condition: ``AWS::Events::EventBusPolicy.Condition``.

        Stability:
            experimental
        """
        props: CfnEventBusPolicyProps = {"action": action, "principal": principal, "statementId": statement_id}

        if condition is not None:
            props["condition"] = condition

        jsii.create(CfnEventBusPolicy, self, [scope, id, props])

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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="action")
    def action(self) -> str:
        """``AWS::Events::EventBusPolicy.Action``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-action
        Stability:
            experimental
        """
        return jsii.get(self, "action")

    @action.setter
    def action(self, value: str):
        return jsii.set(self, "action", value)

    @property
    @jsii.member(jsii_name="principal")
    def principal(self) -> str:
        """``AWS::Events::EventBusPolicy.Principal``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-principal
        Stability:
            experimental
        """
        return jsii.get(self, "principal")

    @principal.setter
    def principal(self, value: str):
        return jsii.set(self, "principal", value)

    @property
    @jsii.member(jsii_name="statementId")
    def statement_id(self) -> str:
        """``AWS::Events::EventBusPolicy.StatementId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-statementid
        Stability:
            experimental
        """
        return jsii.get(self, "statementId")

    @statement_id.setter
    def statement_id(self, value: str):
        return jsii.set(self, "statementId", value)

    @property
    @jsii.member(jsii_name="condition")
    def condition(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional["ConditionProperty"]]]:
        """``AWS::Events::EventBusPolicy.Condition``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-condition
        Stability:
            experimental
        """
        return jsii.get(self, "condition")

    @condition.setter
    def condition(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional["ConditionProperty"]]]):
        return jsii.set(self, "condition", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnEventBusPolicy.ConditionProperty", jsii_struct_bases=[])
    class ConditionProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-eventbuspolicy-condition.html
        Stability:
            experimental
        """
        key: str
        """``CfnEventBusPolicy.ConditionProperty.Key``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-eventbuspolicy-condition.html#cfn-events-eventbuspolicy-condition-key
        Stability:
            experimental
        """

        type: str
        """``CfnEventBusPolicy.ConditionProperty.Type``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-eventbuspolicy-condition.html#cfn-events-eventbuspolicy-condition-type
        Stability:
            experimental
        """

        value: str
        """``CfnEventBusPolicy.ConditionProperty.Value``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-eventbuspolicy-condition.html#cfn-events-eventbuspolicy-condition-value
        Stability:
            experimental
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnEventBusPolicyProps(jsii.compat.TypedDict, total=False):
    condition: typing.Union[aws_cdk.cdk.IResolvable, "CfnEventBusPolicy.ConditionProperty"]
    """``AWS::Events::EventBusPolicy.Condition``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-condition
    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnEventBusPolicyProps", jsii_struct_bases=[_CfnEventBusPolicyProps])
class CfnEventBusPolicyProps(_CfnEventBusPolicyProps):
    """Properties for defining a ``AWS::Events::EventBusPolicy``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html
    Stability:
        experimental
    """
    action: str
    """``AWS::Events::EventBusPolicy.Action``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-action
    Stability:
        experimental
    """

    principal: str
    """``AWS::Events::EventBusPolicy.Principal``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-principal
    Stability:
        experimental
    """

    statementId: str
    """``AWS::Events::EventBusPolicy.StatementId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-statementid
    Stability:
        experimental
    """

class CfnRule(aws_cdk.cdk.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events.CfnRule"):
    """A CloudFormation ``AWS::Events::Rule``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html
    Stability:
        experimental
    cloudformationResource:
        AWS::Events::Rule
    """
    def __init__(self, scope: aws_cdk.cdk.Construct, id: str, *, description: typing.Optional[str]=None, event_pattern: typing.Optional[typing.Union[typing.Optional[typing.Mapping[typing.Any, typing.Any]], typing.Optional[aws_cdk.cdk.IResolvable]]]=None, name: typing.Optional[str]=None, role_arn: typing.Optional[str]=None, schedule_expression: typing.Optional[str]=None, state: typing.Optional[str]=None, targets: typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.cdk.IResolvable, "TargetProperty"]]]]]=None) -> None:
        """Create a new ``AWS::Events::Rule``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            description: ``AWS::Events::Rule.Description``.
            eventPattern: ``AWS::Events::Rule.EventPattern``.
            name: ``AWS::Events::Rule.Name``.
            roleArn: ``AWS::Events::Rule.RoleArn``.
            scheduleExpression: ``AWS::Events::Rule.ScheduleExpression``.
            state: ``AWS::Events::Rule.State``.
            targets: ``AWS::Events::Rule.Targets``.

        Stability:
            experimental
        """
        props: CfnRuleProps = {}

        if description is not None:
            props["description"] = description

        if event_pattern is not None:
            props["eventPattern"] = event_pattern

        if name is not None:
            props["name"] = name

        if role_arn is not None:
            props["roleArn"] = role_arn

        if schedule_expression is not None:
            props["scheduleExpression"] = schedule_expression

        if state is not None:
            props["state"] = state

        if targets is not None:
            props["targets"] = targets

        jsii.create(CfnRule, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> str:
        """
        Stability:
            experimental
        cloudformationAttribute:
            Arn
        """
        return jsii.get(self, "attrArn")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::Events::Rule.Description``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-description
        Stability:
            experimental
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="eventPattern")
    def event_pattern(self) -> typing.Optional[typing.Union[typing.Optional[typing.Mapping[typing.Any, typing.Any]], typing.Optional[aws_cdk.cdk.IResolvable]]]:
        """``AWS::Events::Rule.EventPattern``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-eventpattern
        Stability:
            experimental
        """
        return jsii.get(self, "eventPattern")

    @event_pattern.setter
    def event_pattern(self, value: typing.Optional[typing.Union[typing.Optional[typing.Mapping[typing.Any, typing.Any]], typing.Optional[aws_cdk.cdk.IResolvable]]]):
        return jsii.set(self, "eventPattern", value)

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::Events::Rule.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-name
        Stability:
            experimental
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[str]:
        """``AWS::Events::Rule.RoleArn``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-rolearn
        Stability:
            experimental
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter
    def role_arn(self, value: typing.Optional[str]):
        return jsii.set(self, "roleArn", value)

    @property
    @jsii.member(jsii_name="scheduleExpression")
    def schedule_expression(self) -> typing.Optional[str]:
        """``AWS::Events::Rule.ScheduleExpression``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-scheduleexpression
        Stability:
            experimental
        """
        return jsii.get(self, "scheduleExpression")

    @schedule_expression.setter
    def schedule_expression(self, value: typing.Optional[str]):
        return jsii.set(self, "scheduleExpression", value)

    @property
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[str]:
        """``AWS::Events::Rule.State``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-state
        Stability:
            experimental
        """
        return jsii.get(self, "state")

    @state.setter
    def state(self, value: typing.Optional[str]):
        return jsii.set(self, "state", value)

    @property
    @jsii.member(jsii_name="targets")
    def targets(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.cdk.IResolvable, "TargetProperty"]]]]]:
        """``AWS::Events::Rule.Targets``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-targets
        Stability:
            experimental
        """
        return jsii.get(self, "targets")

    @targets.setter
    def targets(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.cdk.IResolvable, "TargetProperty"]]]]]):
        return jsii.set(self, "targets", value)

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _EcsParametersProperty(jsii.compat.TypedDict, total=False):
        taskCount: jsii.Number
        """``CfnRule.EcsParametersProperty.TaskCount``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html#cfn-events-rule-ecsparameters-taskcount
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.EcsParametersProperty", jsii_struct_bases=[_EcsParametersProperty])
    class EcsParametersProperty(_EcsParametersProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html
        Stability:
            experimental
        """
        taskDefinitionArn: str
        """``CfnRule.EcsParametersProperty.TaskDefinitionArn``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html#cfn-events-rule-ecsparameters-taskdefinitionarn
        Stability:
            experimental
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _InputTransformerProperty(jsii.compat.TypedDict, total=False):
        inputPathsMap: typing.Union[aws_cdk.cdk.IResolvable, typing.Mapping[str,str]]
        """``CfnRule.InputTransformerProperty.InputPathsMap``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-inputtransformer.html#cfn-events-rule-inputtransformer-inputpathsmap
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.InputTransformerProperty", jsii_struct_bases=[_InputTransformerProperty])
    class InputTransformerProperty(_InputTransformerProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-inputtransformer.html
        Stability:
            experimental
        """
        inputTemplate: str
        """``CfnRule.InputTransformerProperty.InputTemplate``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-inputtransformer.html#cfn-events-rule-inputtransformer-inputtemplate
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.KinesisParametersProperty", jsii_struct_bases=[])
    class KinesisParametersProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-kinesisparameters.html
        Stability:
            experimental
        """
        partitionKeyPath: str
        """``CfnRule.KinesisParametersProperty.PartitionKeyPath``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-kinesisparameters.html#cfn-events-rule-kinesisparameters-partitionkeypath
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.RunCommandParametersProperty", jsii_struct_bases=[])
    class RunCommandParametersProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandparameters.html
        Stability:
            experimental
        """
        runCommandTargets: typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "CfnRule.RunCommandTargetProperty"]]]
        """``CfnRule.RunCommandParametersProperty.RunCommandTargets``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandparameters.html#cfn-events-rule-runcommandparameters-runcommandtargets
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.RunCommandTargetProperty", jsii_struct_bases=[])
    class RunCommandTargetProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandtarget.html
        Stability:
            experimental
        """
        key: str
        """``CfnRule.RunCommandTargetProperty.Key``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandtarget.html#cfn-events-rule-runcommandtarget-key
        Stability:
            experimental
        """

        values: typing.List[str]
        """``CfnRule.RunCommandTargetProperty.Values``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandtarget.html#cfn-events-rule-runcommandtarget-values
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.SqsParametersProperty", jsii_struct_bases=[])
    class SqsParametersProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sqsparameters.html
        Stability:
            experimental
        """
        messageGroupId: str
        """``CfnRule.SqsParametersProperty.MessageGroupId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sqsparameters.html#cfn-events-rule-sqsparameters-messagegroupid
        Stability:
            experimental
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _TargetProperty(jsii.compat.TypedDict, total=False):
        ecsParameters: typing.Union[aws_cdk.cdk.IResolvable, "CfnRule.EcsParametersProperty"]
        """``CfnRule.TargetProperty.EcsParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-ecsparameters
        Stability:
            experimental
        """
        input: str
        """``CfnRule.TargetProperty.Input``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-input
        Stability:
            experimental
        """
        inputPath: str
        """``CfnRule.TargetProperty.InputPath``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-inputpath
        Stability:
            experimental
        """
        inputTransformer: typing.Union[aws_cdk.cdk.IResolvable, "CfnRule.InputTransformerProperty"]
        """``CfnRule.TargetProperty.InputTransformer``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-inputtransformer
        Stability:
            experimental
        """
        kinesisParameters: typing.Union[aws_cdk.cdk.IResolvable, "CfnRule.KinesisParametersProperty"]
        """``CfnRule.TargetProperty.KinesisParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-kinesisparameters
        Stability:
            experimental
        """
        roleArn: str
        """``CfnRule.TargetProperty.RoleArn``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-rolearn
        Stability:
            experimental
        """
        runCommandParameters: typing.Union[aws_cdk.cdk.IResolvable, "CfnRule.RunCommandParametersProperty"]
        """``CfnRule.TargetProperty.RunCommandParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-runcommandparameters
        Stability:
            experimental
        """
        sqsParameters: typing.Union[aws_cdk.cdk.IResolvable, "CfnRule.SqsParametersProperty"]
        """``CfnRule.TargetProperty.SqsParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-sqsparameters
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.TargetProperty", jsii_struct_bases=[_TargetProperty])
    class TargetProperty(_TargetProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html
        Stability:
            experimental
        """
        arn: str
        """``CfnRule.TargetProperty.Arn``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-arn
        Stability:
            experimental
        """

        id: str
        """``CfnRule.TargetProperty.Id``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-id
        Stability:
            experimental
        """


@jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRuleProps", jsii_struct_bases=[])
class CfnRuleProps(jsii.compat.TypedDict, total=False):
    """Properties for defining a ``AWS::Events::Rule``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html
    Stability:
        experimental
    """
    description: str
    """``AWS::Events::Rule.Description``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-description
    Stability:
        experimental
    """

    eventPattern: typing.Union[typing.Mapping[typing.Any, typing.Any], aws_cdk.cdk.IResolvable]
    """``AWS::Events::Rule.EventPattern``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-eventpattern
    Stability:
        experimental
    """

    name: str
    """``AWS::Events::Rule.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-name
    Stability:
        experimental
    """

    roleArn: str
    """``AWS::Events::Rule.RoleArn``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-rolearn
    Stability:
        experimental
    """

    scheduleExpression: str
    """``AWS::Events::Rule.ScheduleExpression``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-scheduleexpression
    Stability:
        experimental
    """

    state: str
    """``AWS::Events::Rule.State``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-state
    Stability:
        experimental
    """

    targets: typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "CfnRule.TargetProperty"]]]
    """``AWS::Events::Rule.Targets``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-targets
    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-events.CronOptions", jsii_struct_bases=[])
class CronOptions(jsii.compat.TypedDict, total=False):
    """Options to configure a cron expression.

    All fields are strings so you can use complex expresions. Absence of
    a field implies '*' or '?', whichever one is appropriate.

    See:
        https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions
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

    year: str
    """The year to run this rule at.

    Default:
        - Every year

    Stability:
        experimental
    """

@jsii.implements(aws_cdk.cdk.IResolvable)
class EventField(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events.EventField"):
    """Represents a field in the event pattern.

    Stability:
        experimental
    """
    @jsii.member(jsii_name="fromPath")
    @classmethod
    def from_path(cls, path: str) -> str:
        """Extract a custom JSON path from the event.

        Arguments:
            path: -

        Stability:
            experimental
        """
        return jsii.sinvoke(cls, "fromPath", [path])

    @jsii.member(jsii_name="resolve")
    def resolve(self, _ctx: aws_cdk.cdk.IResolveContext) -> typing.Any:
        """Produce the Token's value at resolution time.

        Arguments:
            _ctx: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "resolve", [_ctx])

    @jsii.member(jsii_name="toJSON")
    def to_json(self) -> str:
        """
        Stability:
            experimental
        """
        return jsii.invoke(self, "toJSON", [])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> str:
        """Return a string representation of this resolvable object.

        Returns a reversible string representation.

        Stability:
            experimental
        """
        return jsii.invoke(self, "toString", [])

    @classproperty
    @jsii.member(jsii_name="account")
    def account(cls) -> str:
        """Extract the account from the event.

        Stability:
            experimental
        """
        return jsii.sget(cls, "account")

    @classproperty
    @jsii.member(jsii_name="detailType")
    def detail_type(cls) -> str:
        """Extract the detail type from the event.

        Stability:
            experimental
        """
        return jsii.sget(cls, "detailType")

    @classproperty
    @jsii.member(jsii_name="eventId")
    def event_id(cls) -> str:
        """Extract the event ID from the event.

        Stability:
            experimental
        """
        return jsii.sget(cls, "eventId")

    @classproperty
    @jsii.member(jsii_name="region")
    def region(cls) -> str:
        """Extract the region from the event.

        Stability:
            experimental
        """
        return jsii.sget(cls, "region")

    @classproperty
    @jsii.member(jsii_name="source")
    def source(cls) -> str:
        """Extract the source from the event.

        Stability:
            experimental
        """
        return jsii.sget(cls, "source")

    @classproperty
    @jsii.member(jsii_name="time")
    def time(cls) -> str:
        """Extract the time from the event.

        Stability:
            experimental
        """
        return jsii.sget(cls, "time")

    @property
    @jsii.member(jsii_name="creationStack")
    def creation_stack(self) -> typing.List[str]:
        """The creation stack of this resolvable which will be appended to errors thrown during resolution.

        If this returns an empty array or ``undefined`` the stack will not be
        attached.

        Stability:
            experimental
        """
        return jsii.get(self, "creationStack")

    @property
    @jsii.member(jsii_name="displayHint")
    def display_hint(self) -> str:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "displayHint")

    @property
    @jsii.member(jsii_name="path")
    def path(self) -> str:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "path")


@jsii.data_type(jsii_type="@aws-cdk/aws-events.EventPattern", jsii_struct_bases=[])
class EventPattern(jsii.compat.TypedDict, total=False):
    """Events in Amazon CloudWatch Events are represented as JSON objects. For more information about JSON objects, see RFC 7159.

    Rules use event patterns to select events and route them to targets. A
    pattern either matches an event or it doesn't. Event patterns are represented
    as JSON objects with a structure that is similar to that of events, for
    example:

    It is important to remember the following about event pattern matching:

    - For a pattern to match an event, the event must contain all the field names
      listed in the pattern. The field names must appear in the event with the
      same nesting structure.
    - Other fields of the event not mentioned in the pattern are ignored;
      effectively, there is a ``"*": "*"`` wildcard for fields not mentioned.
    - The matching is exact (character-by-character), without case-folding or any
      other string normalization.
    - The values being matched follow JSON rules: Strings enclosed in quotes,
      numbers, and the unquoted keywords true, false, and null.
    - Number matching is at the string representation level. For example, 300,
      300.0, and 3.0e2 are not considered equal.

    See:
        https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html
    Stability:
        experimental
    """
    account: typing.List[str]
    """The 12-digit number identifying an AWS account.

    Default:
        - No filtering on account

    Stability:
        experimental
    """

    detail: typing.Mapping[str,typing.Any]
    """A JSON object, whose content is at the discretion of the service originating the event.

    Default:
        - No filtering on detail

    Stability:
        experimental
    """

    detailType: typing.List[str]
    """Identifies, in combination with the source field, the fields and values that appear in the detail field.

    Represents the "detail-type" event field.

    Default:
        - No filtering on detail type

    Stability:
        experimental
    """

    id: typing.List[str]
    """A unique value is generated for every event.

    This can be helpful in
    tracing events as they move through rules to targets, and are processed.

    Default:
        - No filtering on id

    Stability:
        experimental
    """

    region: typing.List[str]
    """Identifies the AWS region where the event originated.

    Default:
        - No filtering on region

    Stability:
        experimental
    """

    resources: typing.List[str]
    """This JSON array contains ARNs that identify resources that are involved in the event.

    Inclusion of these ARNs is at the discretion of the
    service.

    For example, Amazon EC2 instance state-changes include Amazon EC2
    instance ARNs, Auto Scaling events include ARNs for both instances and
    Auto Scaling groups, but API calls with AWS CloudTrail do not include
    resource ARNs.

    Default:
        - No filtering on resource

    Stability:
        experimental
    """

    source: typing.List[str]
    """Identifies the service that sourced the event.

    All events sourced from
    within AWS begin with "aws." Customer-generated events can have any value
    here, as long as it doesn't begin with "aws." We recommend the use of
    Java package-name style reverse domain-name strings.

    To find the correct value for source for an AWS service, see the table in
    AWS Service Namespaces. For example, the source value for Amazon
    CloudFront is aws.cloudfront.

    Default:
        - No filtering on source

    See:
        http://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#genref-aws-service-namespaces
    Stability:
        experimental
    """

    time: typing.List[str]
    """The event timestamp, which can be specified by the service originating the event.

    If the event spans a time interval, the service might choose
    to report the start time, so this value can be noticeably before the time
    the event is actually received.

    Default:
        - No filtering on time

    Stability:
        experimental
    """

    version: typing.List[str]
    """By default, this is set to 0 (zero) in all events.

    Default:
        - No filtering on version

    Stability:
        experimental
    """

@jsii.interface(jsii_type="@aws-cdk/aws-events.IRule")
class IRule(aws_cdk.cdk.IResource, jsii.compat.Protocol):
    """
    Stability:
        experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IRuleProxy

    @property
    @jsii.member(jsii_name="ruleArn")
    def rule_arn(self) -> str:
        """The value of the event rule Amazon Resource Name (ARN), such as arn:aws:events:us-east-2:123456789012:rule/example.

        Stability:
            experimental
        attribute:
            true
        """
        ...


class _IRuleProxy(jsii.proxy_for(aws_cdk.cdk.IResource)):
    """
    Stability:
        experimental
    """
    __jsii_type__ = "@aws-cdk/aws-events.IRule"
    @property
    @jsii.member(jsii_name="ruleArn")
    def rule_arn(self) -> str:
        """The value of the event rule Amazon Resource Name (ARN), such as arn:aws:events:us-east-2:123456789012:rule/example.

        Stability:
            experimental
        attribute:
            true
        """
        return jsii.get(self, "ruleArn")


@jsii.interface(jsii_type="@aws-cdk/aws-events.IRuleTarget")
class IRuleTarget(jsii.compat.Protocol):
    """An abstract target for EventRules.

    Stability:
        experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IRuleTargetProxy

    @jsii.member(jsii_name="bind")
    def bind(self, rule: "IRule") -> "RuleTargetConfig":
        """Returns the rule target specification. NOTE: Do not use the various ``inputXxx`` options. They can be set in a call to ``addTarget``.

        Arguments:
            rule: The CloudWatch Event Rule that would trigger this target.

        Stability:
            experimental
        """
        ...


class _IRuleTargetProxy():
    """An abstract target for EventRules.

    Stability:
        experimental
    """
    __jsii_type__ = "@aws-cdk/aws-events.IRuleTarget"
    @jsii.member(jsii_name="bind")
    def bind(self, rule: "IRule") -> "RuleTargetConfig":
        """Returns the rule target specification. NOTE: Do not use the various ``inputXxx`` options. They can be set in a call to ``addTarget``.

        Arguments:
            rule: The CloudWatch Event Rule that would trigger this target.

        Stability:
            experimental
        """
        return jsii.invoke(self, "bind", [rule])


@jsii.data_type_optionals(jsii_struct_bases=[])
class _OnEventOptions(jsii.compat.TypedDict, total=False):
    description: str
    """A description of the rule's purpose.

    Stability:
        experimental
    """
    eventPattern: "EventPattern"
    """Additional restrictions for the event to route to the specified target.

    The method that generates the rule probably imposes some type of event
    filtering. The filtering implied by what you pass here is added
    on top of that filtering.

    See:
        http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CloudWatchEventsandEventPatterns.html
    Stability:
        experimental
    """
    ruleName: str
    """A name for the rule.

    Default:
        AWS CloudFormation generates a unique physical ID.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-events.OnEventOptions", jsii_struct_bases=[_OnEventOptions])
class OnEventOptions(_OnEventOptions):
    """Standard set of options for ``onXxx`` event handlers on construct.

    Stability:
        experimental
    """
    target: "IRuleTarget"
    """The target to register for the event.

    Stability:
        experimental
    """

@jsii.implements(IRule)
class Rule(aws_cdk.cdk.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events.Rule"):
    """Defines a CloudWatch Event Rule in this stack.

    Stability:
        experimental
    resource:
        AWS::Events::Rule
    """
    def __init__(self, scope: aws_cdk.cdk.Construct, id: str, *, description: typing.Optional[str]=None, enabled: typing.Optional[bool]=None, event_pattern: typing.Optional["EventPattern"]=None, rule_name: typing.Optional[str]=None, schedule: typing.Optional["Schedule"]=None, targets: typing.Optional[typing.List["IRuleTarget"]]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            description: A description of the rule's purpose. Default: - No description.
            enabled: Indicates whether the rule is enabled. Default: true
            eventPattern: Describes which events CloudWatch Events routes to the specified target. These routed events are matched events. For more information, see Events and Event Patterns in the Amazon CloudWatch User Guide. Default: - None.
            ruleName: A name for the rule. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the rule name. For more information, see Name Type.
            schedule: The schedule or rate (frequency) that determines when CloudWatch Events runs the rule. For more information, see Schedule Expression Syntax for Rules in the Amazon CloudWatch User Guide. Default: - None.
            targets: Targets to invoke when this rule matches an event. Input will be the full matched event. If you wish to specify custom target input, use ``addTarget(target[, inputOptions])``. Default: - No targets.

        Stability:
            experimental
        """
        props: RuleProps = {}

        if description is not None:
            props["description"] = description

        if enabled is not None:
            props["enabled"] = enabled

        if event_pattern is not None:
            props["eventPattern"] = event_pattern

        if rule_name is not None:
            props["ruleName"] = rule_name

        if schedule is not None:
            props["schedule"] = schedule

        if targets is not None:
            props["targets"] = targets

        jsii.create(Rule, self, [scope, id, props])

    @jsii.member(jsii_name="fromEventRuleArn")
    @classmethod
    def from_event_rule_arn(cls, scope: aws_cdk.cdk.Construct, id: str, event_rule_arn: str) -> "IRule":
        """
        Arguments:
            scope: -
            id: -
            eventRuleArn: -

        Stability:
            experimental
        """
        return jsii.sinvoke(cls, "fromEventRuleArn", [scope, id, event_rule_arn])

    @jsii.member(jsii_name="addEventPattern")
    def add_event_pattern(self, *, account: typing.Optional[typing.List[str]]=None, detail: typing.Optional[typing.Mapping[str,typing.Any]]=None, detail_type: typing.Optional[typing.List[str]]=None, id: typing.Optional[typing.List[str]]=None, region: typing.Optional[typing.List[str]]=None, resources: typing.Optional[typing.List[str]]=None, source: typing.Optional[typing.List[str]]=None, time: typing.Optional[typing.List[str]]=None, version: typing.Optional[typing.List[str]]=None) -> None:
        """Adds an event pattern filter to this rule.

        If a pattern was already specified,
        these values are merged into the existing pattern.

        For example, if the rule already contains the pattern::

           {
             "resources": [ "r1" ],
             "detail": {
               "hello": [ 1 ]
             }
           }

        And ``addEventPattern`` is called with the pattern::

           {
             "resources": [ "r2" ],
             "detail": {
               "foo": [ "bar" ]
             }
           }

        The resulting event pattern will be::

           {
             "resources": [ "r1", "r2" ],
             "detail": {
               "hello": [ 1 ],
               "foo": [ "bar" ]
             }
           }

        Arguments:
            eventPattern: -
            account: The 12-digit number identifying an AWS account. Default: - No filtering on account
            detail: A JSON object, whose content is at the discretion of the service originating the event. Default: - No filtering on detail
            detailType: Identifies, in combination with the source field, the fields and values that appear in the detail field. Represents the "detail-type" event field. Default: - No filtering on detail type
            id: A unique value is generated for every event. This can be helpful in tracing events as they move through rules to targets, and are processed. Default: - No filtering on id
            region: Identifies the AWS region where the event originated. Default: - No filtering on region
            resources: This JSON array contains ARNs that identify resources that are involved in the event. Inclusion of these ARNs is at the discretion of the service. For example, Amazon EC2 instance state-changes include Amazon EC2 instance ARNs, Auto Scaling events include ARNs for both instances and Auto Scaling groups, but API calls with AWS CloudTrail do not include resource ARNs. Default: - No filtering on resource
            source: Identifies the service that sourced the event. All events sourced from within AWS begin with "aws." Customer-generated events can have any value here, as long as it doesn't begin with "aws." We recommend the use of Java package-name style reverse domain-name strings. To find the correct value for source for an AWS service, see the table in AWS Service Namespaces. For example, the source value for Amazon CloudFront is aws.cloudfront. Default: - No filtering on source
            time: The event timestamp, which can be specified by the service originating the event. If the event spans a time interval, the service might choose to report the start time, so this value can be noticeably before the time the event is actually received. Default: - No filtering on time
            version: By default, this is set to 0 (zero) in all events. Default: - No filtering on version

        Stability:
            experimental
        """
        event_pattern: EventPattern = {}

        if account is not None:
            event_pattern["account"] = account

        if detail is not None:
            event_pattern["detail"] = detail

        if detail_type is not None:
            event_pattern["detailType"] = detail_type

        if id is not None:
            event_pattern["id"] = id

        if region is not None:
            event_pattern["region"] = region

        if resources is not None:
            event_pattern["resources"] = resources

        if source is not None:
            event_pattern["source"] = source

        if time is not None:
            event_pattern["time"] = time

        if version is not None:
            event_pattern["version"] = version

        return jsii.invoke(self, "addEventPattern", [event_pattern])

    @jsii.member(jsii_name="addTarget")
    def add_target(self, target: typing.Optional["IRuleTarget"]=None) -> None:
        """Adds a target to the rule. The abstract class RuleTarget can be extended to define new targets.

        No-op if target is undefined.

        Arguments:
            target: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "addTarget", [target])

    @jsii.member(jsii_name="validate")
    def _validate(self) -> typing.List[str]:
        """Validate the current construct.

        This method can be implemented by derived constructs in order to perform
        validation logic. It is called on all constructs before synthesis.

        Stability:
            experimental
        """
        return jsii.invoke(self, "validate", [])

    @property
    @jsii.member(jsii_name="ruleArn")
    def rule_arn(self) -> str:
        """The value of the event rule Amazon Resource Name (ARN), such as arn:aws:events:us-east-2:123456789012:rule/example.

        Stability:
            experimental
        """
        return jsii.get(self, "ruleArn")


@jsii.data_type(jsii_type="@aws-cdk/aws-events.RuleProps", jsii_struct_bases=[])
class RuleProps(jsii.compat.TypedDict, total=False):
    """
    Stability:
        experimental
    """
    description: str
    """A description of the rule's purpose.

    Default:
        - No description.

    Stability:
        experimental
    """

    enabled: bool
    """Indicates whether the rule is enabled.

    Default:
        true

    Stability:
        experimental
    """

    eventPattern: "EventPattern"
    """Describes which events CloudWatch Events routes to the specified target. These routed events are matched events. For more information, see Events and Event Patterns in the Amazon CloudWatch User Guide.

    Default:
        - None.

    See:
        http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CloudWatchEventsandEventPatterns.html
        
        You must specify this property (either via props or via
        ``addEventPattern``), the ``scheduleExpression`` property, or both. The
        method ``addEventPattern`` can be used to add filter values to the event
        pattern.
    Stability:
        experimental
    """

    ruleName: str
    """A name for the rule.

    Default:
        - AWS CloudFormation generates a unique physical ID and uses that ID
          for the rule name. For more information, see Name Type.

    Stability:
        experimental
    """

    schedule: "Schedule"
    """The schedule or rate (frequency) that determines when CloudWatch Events runs the rule.

    For more information, see Schedule Expression Syntax for
    Rules in the Amazon CloudWatch User Guide.

    Default:
        - None.

    See:
        http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html
        
        You must specify this property, the ``eventPattern`` property, or both.
    Stability:
        experimental
    """

    targets: typing.List["IRuleTarget"]
    """Targets to invoke when this rule matches an event.

    Input will be the full matched event. If you wish to specify custom
    target input, use ``addTarget(target[, inputOptions])``.

    Default:
        - No targets.

    Stability:
        experimental
    """

@jsii.data_type_optionals(jsii_struct_bases=[])
class _RuleTargetConfig(jsii.compat.TypedDict, total=False):
    ecsParameters: "CfnRule.EcsParametersProperty"
    """The Amazon ECS task definition and task count to use, if the event target is an Amazon ECS task.

    Stability:
        experimental
    """
    input: "RuleTargetInput"
    """What input to send to the event target.

    Default:
        the entire event

    Stability:
        experimental
    """
    kinesisParameters: "CfnRule.KinesisParametersProperty"
    """Settings that control shard assignment, when the target is a Kinesis stream.

    If you don't include this parameter, eventId is used as the
    partition key.

    Stability:
        experimental
    """
    role: aws_cdk.aws_iam.IRole
    """Role to use to invoke this event target.

    Stability:
        experimental
    """
    runCommandParameters: "CfnRule.RunCommandParametersProperty"
    """Parameters used when the rule invokes Amazon EC2 Systems Manager Run Command.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-events.RuleTargetConfig", jsii_struct_bases=[_RuleTargetConfig])
class RuleTargetConfig(_RuleTargetConfig):
    """Properties for an event rule target.

    Stability:
        experimental
    """
    arn: str
    """The Amazon Resource Name (ARN) of the target.

    Stability:
        experimental
    """

    id: str
    """A unique, user-defined identifier for the target.

    Acceptable values
    include alphanumeric characters, periods (.), hyphens (-), and
    underscores (_).

    Stability:
        experimental
    """

class RuleTargetInput(metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-events.RuleTargetInput"):
    """The input to send to the event target.

    Stability:
        experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _RuleTargetInputProxy

    def __init__(self) -> None:
        """
        Stability:
            experimental
        """
        jsii.create(RuleTargetInput, self, [])

    @jsii.member(jsii_name="fromEventPath")
    @classmethod
    def from_event_path(cls, path: str) -> "RuleTargetInput":
        """Take the event target input from a path in the event JSON.

        Arguments:
            path: -

        Stability:
            experimental
        """
        return jsii.sinvoke(cls, "fromEventPath", [path])

    @jsii.member(jsii_name="fromMultilineText")
    @classmethod
    def from_multiline_text(cls, text: str) -> "RuleTargetInput":
        """Pass text to the event target, splitting on newlines.

        This is only useful when passing to a target that does not
        take a single argument.

        May contain strings returned by EventField.from() to substitute in parts
        of the matched event.

        Arguments:
            text: -

        Stability:
            experimental
        """
        return jsii.sinvoke(cls, "fromMultilineText", [text])

    @jsii.member(jsii_name="fromObject")
    @classmethod
    def from_object(cls, obj: typing.Any) -> "RuleTargetInput":
        """Pass a JSON object to the event target.

        May contain strings returned by EventField.from() to substitute in parts of the
        matched event.

        Arguments:
            obj: -

        Stability:
            experimental
        """
        return jsii.sinvoke(cls, "fromObject", [obj])

    @jsii.member(jsii_name="fromText")
    @classmethod
    def from_text(cls, text: str) -> "RuleTargetInput":
        """Pass text to the event target.

        May contain strings returned by EventField.from() to substitute in parts of the
        matched event.

        Arguments:
            text: -

        Stability:
            experimental
        """
        return jsii.sinvoke(cls, "fromText", [text])

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(self, rule: "IRule") -> "RuleTargetInputProperties":
        """Return the input properties for this input object.

        Arguments:
            rule: -

        Stability:
            experimental
        """
        ...


class _RuleTargetInputProxy(RuleTargetInput):
    @jsii.member(jsii_name="bind")
    def bind(self, rule: "IRule") -> "RuleTargetInputProperties":
        """Return the input properties for this input object.

        Arguments:
            rule: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "bind", [rule])


@jsii.data_type(jsii_type="@aws-cdk/aws-events.RuleTargetInputProperties", jsii_struct_bases=[])
class RuleTargetInputProperties(jsii.compat.TypedDict, total=False):
    """The input properties for an event target.

    Stability:
        experimental
    """
    input: str
    """Literal input to the target service (must be valid JSON).

    Stability:
        experimental
    """

    inputPath: str
    """JsonPath to take input from the input event.

    Stability:
        experimental
    """

    inputPathsMap: typing.Mapping[str,str]
    """Paths map to extract values from event and insert into ``inputTemplate``.

    Stability:
        experimental
    """

    inputTemplate: str
    """Input template to insert paths map into.

    Stability:
        experimental
    """

class Schedule(metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-events.Schedule"):
    """Schedule for scheduled event rules.

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
    def cron(cls, *, day: typing.Optional[str]=None, hour: typing.Optional[str]=None, minute: typing.Optional[str]=None, month: typing.Optional[str]=None, week_day: typing.Optional[str]=None, year: typing.Optional[str]=None) -> "Schedule":
        """Create a schedule from a set of cron fields.

        Arguments:
            options: -
            day: The day of the month to run this rule at. Default: - Every day of the month
            hour: The hour to run this rule at. Default: - Every hour
            minute: The minute to run this rule at. Default: - Every minute
            month: The month to run this rule at. Default: - Every month
            weekDay: The day of the week to run this rule at. Default: - Any day of the week
            year: The year to run this rule at. Default: - Every year

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

        if year is not None:
            options["year"] = year

        return jsii.sinvoke(cls, "cron", [options])

    @jsii.member(jsii_name="expression")
    @classmethod
    def expression(cls, expression: str) -> "Schedule":
        """Construct a schedule from a literal schedule expression.

        Arguments:
            expression: The expression to use. Must be in a format that Cloudwatch Events will recognize

        Stability:
            experimental
        """
        return jsii.sinvoke(cls, "expression", [expression])

    @jsii.member(jsii_name="rate")
    @classmethod
    def rate(cls, interval: jsii.Number, unit: "TimeUnit") -> "Schedule":
        """Construct a schedule from an interval and a time unit.

        Arguments:
            interval: -
            unit: -

        Stability:
            experimental
        """
        return jsii.sinvoke(cls, "rate", [interval, unit])

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


@jsii.enum(jsii_type="@aws-cdk/aws-events.TimeUnit")
class TimeUnit(enum.Enum):
    """What unit to interpret the rate in.

    Stability:
        experimental
    """
    Minute = "Minute"
    """The rate is in minutes.

    Stability:
        experimental
    """
    Hour = "Hour"
    """The rate is in hours.

    Stability:
        experimental
    """
    Day = "Day"
    """The rate is in days.

    Stability:
        experimental
    """

__all__ = ["CfnEventBusPolicy", "CfnEventBusPolicyProps", "CfnRule", "CfnRuleProps", "CronOptions", "EventField", "EventPattern", "IRule", "IRuleTarget", "OnEventOptions", "Rule", "RuleProps", "RuleTargetConfig", "RuleTargetInput", "RuleTargetInputProperties", "Schedule", "TimeUnit", "__jsii_assembly__"]

publication.publish()
