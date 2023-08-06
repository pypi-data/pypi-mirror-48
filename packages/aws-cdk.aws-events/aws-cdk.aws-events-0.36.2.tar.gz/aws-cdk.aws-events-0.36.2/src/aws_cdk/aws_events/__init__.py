import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_iam
import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-events", "0.36.2", __name__, "aws-events@0.36.2.jsii.tgz")
class CfnEventBusPolicy(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events.CfnEventBusPolicy"):
    """A CloudFormation ``AWS::Events::EventBusPolicy``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html
    Stability:
        stable
    cloudformationResource:
        AWS::Events::EventBusPolicy
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, action: str, principal: str, statement_id: str, condition: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ConditionProperty"]]]=None) -> None:
        """Create a new ``AWS::Events::EventBusPolicy``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            action: ``AWS::Events::EventBusPolicy.Action``.
            principal: ``AWS::Events::EventBusPolicy.Principal``.
            statement_id: ``AWS::Events::EventBusPolicy.StatementId``.
            condition: ``AWS::Events::EventBusPolicy.Condition``.

        Stability:
            stable
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
    @jsii.member(jsii_name="action")
    def action(self) -> str:
        """``AWS::Events::EventBusPolicy.Action``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-action
        Stability:
            stable
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
            stable
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
            stable
        """
        return jsii.get(self, "statementId")

    @statement_id.setter
    def statement_id(self, value: str):
        return jsii.set(self, "statementId", value)

    @property
    @jsii.member(jsii_name="condition")
    def condition(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ConditionProperty"]]]:
        """``AWS::Events::EventBusPolicy.Condition``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-condition
        Stability:
            stable
        """
        return jsii.get(self, "condition")

    @condition.setter
    def condition(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ConditionProperty"]]]):
        return jsii.set(self, "condition", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnEventBusPolicy.ConditionProperty", jsii_struct_bases=[])
    class ConditionProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-eventbuspolicy-condition.html
        Stability:
            stable
        """
        key: str
        """``CfnEventBusPolicy.ConditionProperty.Key``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-eventbuspolicy-condition.html#cfn-events-eventbuspolicy-condition-key
        Stability:
            stable
        """

        type: str
        """``CfnEventBusPolicy.ConditionProperty.Type``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-eventbuspolicy-condition.html#cfn-events-eventbuspolicy-condition-type
        Stability:
            stable
        """

        value: str
        """``CfnEventBusPolicy.ConditionProperty.Value``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-eventbuspolicy-condition.html#cfn-events-eventbuspolicy-condition-value
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnEventBusPolicyProps(jsii.compat.TypedDict, total=False):
    condition: typing.Union[aws_cdk.core.IResolvable, "CfnEventBusPolicy.ConditionProperty"]
    """``AWS::Events::EventBusPolicy.Condition``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-condition
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnEventBusPolicyProps", jsii_struct_bases=[_CfnEventBusPolicyProps])
class CfnEventBusPolicyProps(_CfnEventBusPolicyProps):
    """Properties for defining a ``AWS::Events::EventBusPolicy``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html
    Stability:
        stable
    """
    action: str
    """``AWS::Events::EventBusPolicy.Action``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-action
    Stability:
        stable
    """

    principal: str
    """``AWS::Events::EventBusPolicy.Principal``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-principal
    Stability:
        stable
    """

    statementId: str
    """``AWS::Events::EventBusPolicy.StatementId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html#cfn-events-eventbuspolicy-statementid
    Stability:
        stable
    """

class CfnRule(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events.CfnRule"):
    """A CloudFormation ``AWS::Events::Rule``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html
    Stability:
        stable
    cloudformationResource:
        AWS::Events::Rule
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, description: typing.Optional[str]=None, event_pattern: typing.Any=None, name: typing.Optional[str]=None, role_arn: typing.Optional[str]=None, schedule_expression: typing.Optional[str]=None, state: typing.Optional[str]=None, targets: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TargetProperty"]]]]]=None) -> None:
        """Create a new ``AWS::Events::Rule``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            description: ``AWS::Events::Rule.Description``.
            event_pattern: ``AWS::Events::Rule.EventPattern``.
            name: ``AWS::Events::Rule.Name``.
            role_arn: ``AWS::Events::Rule.RoleArn``.
            schedule_expression: ``AWS::Events::Rule.ScheduleExpression``.
            state: ``AWS::Events::Rule.State``.
            targets: ``AWS::Events::Rule.Targets``.

        Stability:
            stable
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
    @jsii.member(jsii_name="eventPattern")
    def event_pattern(self) -> typing.Any:
        """``AWS::Events::Rule.EventPattern``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-eventpattern
        Stability:
            stable
        """
        return jsii.get(self, "eventPattern")

    @event_pattern.setter
    def event_pattern(self, value: typing.Any):
        return jsii.set(self, "eventPattern", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::Events::Rule.Description``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-description
        Stability:
            stable
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::Events::Rule.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-name
        Stability:
            stable
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
            stable
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
            stable
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
            stable
        """
        return jsii.get(self, "state")

    @state.setter
    def state(self, value: typing.Optional[str]):
        return jsii.set(self, "state", value)

    @property
    @jsii.member(jsii_name="targets")
    def targets(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TargetProperty"]]]]]:
        """``AWS::Events::Rule.Targets``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-targets
        Stability:
            stable
        """
        return jsii.get(self, "targets")

    @targets.setter
    def targets(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TargetProperty"]]]]]):
        return jsii.set(self, "targets", value)

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _EcsParametersProperty(jsii.compat.TypedDict, total=False):
        taskCount: jsii.Number
        """``CfnRule.EcsParametersProperty.TaskCount``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html#cfn-events-rule-ecsparameters-taskcount
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.EcsParametersProperty", jsii_struct_bases=[_EcsParametersProperty])
    class EcsParametersProperty(_EcsParametersProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html
        Stability:
            stable
        """
        taskDefinitionArn: str
        """``CfnRule.EcsParametersProperty.TaskDefinitionArn``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-ecsparameters.html#cfn-events-rule-ecsparameters-taskdefinitionarn
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _InputTransformerProperty(jsii.compat.TypedDict, total=False):
        inputPathsMap: typing.Union[aws_cdk.core.IResolvable, typing.Mapping[str,str]]
        """``CfnRule.InputTransformerProperty.InputPathsMap``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-inputtransformer.html#cfn-events-rule-inputtransformer-inputpathsmap
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.InputTransformerProperty", jsii_struct_bases=[_InputTransformerProperty])
    class InputTransformerProperty(_InputTransformerProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-inputtransformer.html
        Stability:
            stable
        """
        inputTemplate: str
        """``CfnRule.InputTransformerProperty.InputTemplate``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-inputtransformer.html#cfn-events-rule-inputtransformer-inputtemplate
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.KinesisParametersProperty", jsii_struct_bases=[])
    class KinesisParametersProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-kinesisparameters.html
        Stability:
            stable
        """
        partitionKeyPath: str
        """``CfnRule.KinesisParametersProperty.PartitionKeyPath``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-kinesisparameters.html#cfn-events-rule-kinesisparameters-partitionkeypath
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.RunCommandParametersProperty", jsii_struct_bases=[])
    class RunCommandParametersProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandparameters.html
        Stability:
            stable
        """
        runCommandTargets: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRule.RunCommandTargetProperty"]]]
        """``CfnRule.RunCommandParametersProperty.RunCommandTargets``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandparameters.html#cfn-events-rule-runcommandparameters-runcommandtargets
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.RunCommandTargetProperty", jsii_struct_bases=[])
    class RunCommandTargetProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandtarget.html
        Stability:
            stable
        """
        key: str
        """``CfnRule.RunCommandTargetProperty.Key``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandtarget.html#cfn-events-rule-runcommandtarget-key
        Stability:
            stable
        """

        values: typing.List[str]
        """``CfnRule.RunCommandTargetProperty.Values``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-runcommandtarget.html#cfn-events-rule-runcommandtarget-values
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.SqsParametersProperty", jsii_struct_bases=[])
    class SqsParametersProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sqsparameters.html
        Stability:
            stable
        """
        messageGroupId: str
        """``CfnRule.SqsParametersProperty.MessageGroupId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-sqsparameters.html#cfn-events-rule-sqsparameters-messagegroupid
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _TargetProperty(jsii.compat.TypedDict, total=False):
        ecsParameters: typing.Union[aws_cdk.core.IResolvable, "CfnRule.EcsParametersProperty"]
        """``CfnRule.TargetProperty.EcsParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-ecsparameters
        Stability:
            stable
        """
        input: str
        """``CfnRule.TargetProperty.Input``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-input
        Stability:
            stable
        """
        inputPath: str
        """``CfnRule.TargetProperty.InputPath``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-inputpath
        Stability:
            stable
        """
        inputTransformer: typing.Union[aws_cdk.core.IResolvable, "CfnRule.InputTransformerProperty"]
        """``CfnRule.TargetProperty.InputTransformer``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-inputtransformer
        Stability:
            stable
        """
        kinesisParameters: typing.Union[aws_cdk.core.IResolvable, "CfnRule.KinesisParametersProperty"]
        """``CfnRule.TargetProperty.KinesisParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-kinesisparameters
        Stability:
            stable
        """
        roleArn: str
        """``CfnRule.TargetProperty.RoleArn``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-rolearn
        Stability:
            stable
        """
        runCommandParameters: typing.Union[aws_cdk.core.IResolvable, "CfnRule.RunCommandParametersProperty"]
        """``CfnRule.TargetProperty.RunCommandParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-runcommandparameters
        Stability:
            stable
        """
        sqsParameters: typing.Union[aws_cdk.core.IResolvable, "CfnRule.SqsParametersProperty"]
        """``CfnRule.TargetProperty.SqsParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-sqsparameters
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRule.TargetProperty", jsii_struct_bases=[_TargetProperty])
    class TargetProperty(_TargetProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html
        Stability:
            stable
        """
        arn: str
        """``CfnRule.TargetProperty.Arn``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-arn
        Stability:
            stable
        """

        id: str
        """``CfnRule.TargetProperty.Id``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-id
        Stability:
            stable
        """


@jsii.data_type(jsii_type="@aws-cdk/aws-events.CfnRuleProps", jsii_struct_bases=[])
class CfnRuleProps(jsii.compat.TypedDict, total=False):
    """Properties for defining a ``AWS::Events::Rule``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html
    Stability:
        stable
    """
    description: str
    """``AWS::Events::Rule.Description``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-description
    Stability:
        stable
    """

    eventPattern: typing.Any
    """``AWS::Events::Rule.EventPattern``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-eventpattern
    Stability:
        stable
    """

    name: str
    """``AWS::Events::Rule.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-name
    Stability:
        stable
    """

    roleArn: str
    """``AWS::Events::Rule.RoleArn``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-rolearn
    Stability:
        stable
    """

    scheduleExpression: str
    """``AWS::Events::Rule.ScheduleExpression``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-scheduleexpression
    Stability:
        stable
    """

    state: str
    """``AWS::Events::Rule.State``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-state
    Stability:
        stable
    """

    targets: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnRule.TargetProperty"]]]
    """``AWS::Events::Rule.Targets``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html#cfn-events-rule-targets
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-events.CronOptions", jsii_struct_bases=[])
class CronOptions(jsii.compat.TypedDict, total=False):
    """Options to configure a cron expression.

    All fields are strings so you can use complex expresions. Absence of
    a field implies '*' or '?', whichever one is appropriate.

    See:
        https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions
    Stability:
        stable
    """
    day: str
    """The day of the month to run this rule at.

    Default:
        - Every day of the month

    Stability:
        stable
    """

    hour: str
    """The hour to run this rule at.

    Default:
        - Every hour

    Stability:
        stable
    """

    minute: str
    """The minute to run this rule at.

    Default:
        - Every minute

    Stability:
        stable
    """

    month: str
    """The month to run this rule at.

    Default:
        - Every month

    Stability:
        stable
    """

    weekDay: str
    """The day of the week to run this rule at.

    Default:
        - Any day of the week

    Stability:
        stable
    """

    year: str
    """The year to run this rule at.

    Default:
        - Every year

    Stability:
        stable
    """

@jsii.implements(aws_cdk.core.IResolvable)
class EventField(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events.EventField"):
    """Represents a field in the event pattern.

    Stability:
        stable
    """
    @jsii.member(jsii_name="fromPath")
    @classmethod
    def from_path(cls, path: str) -> str:
        """Extract a custom JSON path from the event.

        Arguments:
            path: -

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "fromPath", [path])

    @jsii.member(jsii_name="resolve")
    def resolve(self, _ctx: aws_cdk.core.IResolveContext) -> typing.Any:
        """Produce the Token's value at resolution time.

        Arguments:
            _ctx: -

        Stability:
            stable
        """
        return jsii.invoke(self, "resolve", [_ctx])

    @jsii.member(jsii_name="toJSON")
    def to_json(self) -> str:
        """
        Stability:
            stable
        """
        return jsii.invoke(self, "toJSON", [])

    @jsii.member(jsii_name="toString")
    def to_string(self) -> str:
        """Return a string representation of this resolvable object.

        Returns a reversible string representation.

        Stability:
            stable
        """
        return jsii.invoke(self, "toString", [])

    @classproperty
    @jsii.member(jsii_name="account")
    def account(cls) -> str:
        """Extract the account from the event.

        Stability:
            stable
        """
        return jsii.sget(cls, "account")

    @classproperty
    @jsii.member(jsii_name="detailType")
    def detail_type(cls) -> str:
        """Extract the detail type from the event.

        Stability:
            stable
        """
        return jsii.sget(cls, "detailType")

    @classproperty
    @jsii.member(jsii_name="eventId")
    def event_id(cls) -> str:
        """Extract the event ID from the event.

        Stability:
            stable
        """
        return jsii.sget(cls, "eventId")

    @classproperty
    @jsii.member(jsii_name="region")
    def region(cls) -> str:
        """Extract the region from the event.

        Stability:
            stable
        """
        return jsii.sget(cls, "region")

    @classproperty
    @jsii.member(jsii_name="source")
    def source(cls) -> str:
        """Extract the source from the event.

        Stability:
            stable
        """
        return jsii.sget(cls, "source")

    @classproperty
    @jsii.member(jsii_name="time")
    def time(cls) -> str:
        """Extract the time from the event.

        Stability:
            stable
        """
        return jsii.sget(cls, "time")

    @property
    @jsii.member(jsii_name="creationStack")
    def creation_stack(self) -> typing.List[str]:
        """The creation stack of this resolvable which will be appended to errors thrown during resolution.

        If this returns an empty array the stack will not be attached.

        Stability:
            stable
        """
        return jsii.get(self, "creationStack")

    @property
    @jsii.member(jsii_name="displayHint")
    def display_hint(self) -> str:
        """
        Stability:
            stable
        """
        return jsii.get(self, "displayHint")

    @property
    @jsii.member(jsii_name="path")
    def path(self) -> str:
        """
        Stability:
            stable
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
        stable
    """
    account: typing.List[str]
    """The 12-digit number identifying an AWS account.

    Default:
        - No filtering on account

    Stability:
        stable
    """

    detail: typing.Mapping[str,typing.Any]
    """A JSON object, whose content is at the discretion of the service originating the event.

    Default:
        - No filtering on detail

    Stability:
        stable
    """

    detailType: typing.List[str]
    """Identifies, in combination with the source field, the fields and values that appear in the detail field.

    Represents the "detail-type" event field.

    Default:
        - No filtering on detail type

    Stability:
        stable
    """

    id: typing.List[str]
    """A unique value is generated for every event.

    This can be helpful in
    tracing events as they move through rules to targets, and are processed.

    Default:
        - No filtering on id

    Stability:
        stable
    """

    region: typing.List[str]
    """Identifies the AWS region where the event originated.

    Default:
        - No filtering on region

    Stability:
        stable
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
        stable
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
        stable
    """

    time: typing.List[str]
    """The event timestamp, which can be specified by the service originating the event.

    If the event spans a time interval, the service might choose
    to report the start time, so this value can be noticeably before the time
    the event is actually received.

    Default:
        - No filtering on time

    Stability:
        stable
    """

    version: typing.List[str]
    """By default, this is set to 0 (zero) in all events.

    Default:
        - No filtering on version

    Stability:
        stable
    """

@jsii.interface(jsii_type="@aws-cdk/aws-events.IRule")
class IRule(aws_cdk.core.IResource, jsii.compat.Protocol):
    """
    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IRuleProxy

    @property
    @jsii.member(jsii_name="ruleArn")
    def rule_arn(self) -> str:
        """The value of the event rule Amazon Resource Name (ARN), such as arn:aws:events:us-east-2:123456789012:rule/example.

        Stability:
            stable
        attribute:
            true
        """
        ...


class _IRuleProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """
    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-events.IRule"
    @property
    @jsii.member(jsii_name="ruleArn")
    def rule_arn(self) -> str:
        """The value of the event rule Amazon Resource Name (ARN), such as arn:aws:events:us-east-2:123456789012:rule/example.

        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "ruleArn")


@jsii.interface(jsii_type="@aws-cdk/aws-events.IRuleTarget")
class IRuleTarget(jsii.compat.Protocol):
    """An abstract target for EventRules.

    Stability:
        stable
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
            stable
        """
        ...


class _IRuleTargetProxy():
    """An abstract target for EventRules.

    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-events.IRuleTarget"
    @jsii.member(jsii_name="bind")
    def bind(self, rule: "IRule") -> "RuleTargetConfig":
        """Returns the rule target specification. NOTE: Do not use the various ``inputXxx`` options. They can be set in a call to ``addTarget``.

        Arguments:
            rule: The CloudWatch Event Rule that would trigger this target.

        Stability:
            stable
        """
        return jsii.invoke(self, "bind", [rule])


@jsii.data_type(jsii_type="@aws-cdk/aws-events.OnEventOptions", jsii_struct_bases=[])
class OnEventOptions(jsii.compat.TypedDict, total=False):
    """Standard set of options for ``onXxx`` event handlers on construct.

    Stability:
        stable
    """
    description: str
    """A description of the rule's purpose.

    Default:
        - No description

    Stability:
        stable
    """

    eventPattern: "EventPattern"
    """Additional restrictions for the event to route to the specified target.

    The method that generates the rule probably imposes some type of event
    filtering. The filtering implied by what you pass here is added
    on top of that filtering.

    Default:
        - No additional filtering based on an event pattern.

    See:
        http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CloudWatchEventsandEventPatterns.html
    Stability:
        stable
    """

    ruleName: str
    """A name for the rule.

    Default:
        AWS CloudFormation generates a unique physical ID.

    Stability:
        stable
    """

    target: "IRuleTarget"
    """The target to register for the event.

    Default:
        - No target is added to the rule. Use ``addTarget()`` to add a target.

    Stability:
        stable
    """

@jsii.implements(IRule)
class Rule(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events.Rule"):
    """Defines a CloudWatch Event Rule in this stack.

    Stability:
        stable
    resource:
        AWS::Events::Rule
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, description: typing.Optional[str]=None, enabled: typing.Optional[bool]=None, event_pattern: typing.Optional["EventPattern"]=None, rule_name: typing.Optional[str]=None, schedule: typing.Optional["Schedule"]=None, targets: typing.Optional[typing.List["IRuleTarget"]]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            description: A description of the rule's purpose. Default: - No description.
            enabled: Indicates whether the rule is enabled. Default: true
            event_pattern: Describes which events CloudWatch Events routes to the specified target. These routed events are matched events. For more information, see Events and Event Patterns in the Amazon CloudWatch User Guide. Default: - None.
            rule_name: A name for the rule. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the rule name. For more information, see Name Type.
            schedule: The schedule or rate (frequency) that determines when CloudWatch Events runs the rule. For more information, see Schedule Expression Syntax for Rules in the Amazon CloudWatch User Guide. Default: - None.
            targets: Targets to invoke when this rule matches an event. Input will be the full matched event. If you wish to specify custom target input, use ``addTarget(target[, inputOptions])``. Default: - No targets.

        Stability:
            stable
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
    def from_event_rule_arn(cls, scope: aws_cdk.core.Construct, id: str, event_rule_arn: str) -> "IRule":
        """
        Arguments:
            scope: -
            id: -
            event_rule_arn: -

        Stability:
            stable
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
            event_pattern: -
            account: The 12-digit number identifying an AWS account. Default: - No filtering on account
            detail: A JSON object, whose content is at the discretion of the service originating the event. Default: - No filtering on detail
            detail_type: Identifies, in combination with the source field, the fields and values that appear in the detail field. Represents the "detail-type" event field. Default: - No filtering on detail type
            id: A unique value is generated for every event. This can be helpful in tracing events as they move through rules to targets, and are processed. Default: - No filtering on id
            region: Identifies the AWS region where the event originated. Default: - No filtering on region
            resources: This JSON array contains ARNs that identify resources that are involved in the event. Inclusion of these ARNs is at the discretion of the service. For example, Amazon EC2 instance state-changes include Amazon EC2 instance ARNs, Auto Scaling events include ARNs for both instances and Auto Scaling groups, but API calls with AWS CloudTrail do not include resource ARNs. Default: - No filtering on resource
            source: Identifies the service that sourced the event. All events sourced from within AWS begin with "aws." Customer-generated events can have any value here, as long as it doesn't begin with "aws." We recommend the use of Java package-name style reverse domain-name strings. To find the correct value for source for an AWS service, see the table in AWS Service Namespaces. For example, the source value for Amazon CloudFront is aws.cloudfront. Default: - No filtering on source
            time: The event timestamp, which can be specified by the service originating the event. If the event spans a time interval, the service might choose to report the start time, so this value can be noticeably before the time the event is actually received. Default: - No filtering on time
            version: By default, this is set to 0 (zero) in all events. Default: - No filtering on version

        Stability:
            stable
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
            stable
        """
        return jsii.invoke(self, "addTarget", [target])

    @jsii.member(jsii_name="validate")
    def _validate(self) -> typing.List[str]:
        """Validate the current construct.

        This method can be implemented by derived constructs in order to perform
        validation logic. It is called on all constructs before synthesis.

        Stability:
            stable
        """
        return jsii.invoke(self, "validate", [])

    @property
    @jsii.member(jsii_name="ruleArn")
    def rule_arn(self) -> str:
        """The value of the event rule Amazon Resource Name (ARN), such as arn:aws:events:us-east-2:123456789012:rule/example.

        Stability:
            stable
        """
        return jsii.get(self, "ruleArn")


@jsii.data_type(jsii_type="@aws-cdk/aws-events.RuleProps", jsii_struct_bases=[])
class RuleProps(jsii.compat.TypedDict, total=False):
    """
    Stability:
        stable
    """
    description: str
    """A description of the rule's purpose.

    Default:
        - No description.

    Stability:
        stable
    """

    enabled: bool
    """Indicates whether the rule is enabled.

    Default:
        true

    Stability:
        stable
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
        stable
    """

    ruleName: str
    """A name for the rule.

    Default:
        - AWS CloudFormation generates a unique physical ID and uses that ID
          for the rule name. For more information, see Name Type.

    Stability:
        stable
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
        stable
    """

    targets: typing.List["IRuleTarget"]
    """Targets to invoke when this rule matches an event.

    Input will be the full matched event. If you wish to specify custom
    target input, use ``addTarget(target[, inputOptions])``.

    Default:
        - No targets.

    Stability:
        stable
    """

@jsii.data_type_optionals(jsii_struct_bases=[])
class _RuleTargetConfig(jsii.compat.TypedDict, total=False):
    ecsParameters: "CfnRule.EcsParametersProperty"
    """The Amazon ECS task definition and task count to use, if the event target is an Amazon ECS task.

    Stability:
        stable
    """
    input: "RuleTargetInput"
    """What input to send to the event target.

    Default:
        the entire event

    Stability:
        stable
    """
    kinesisParameters: "CfnRule.KinesisParametersProperty"
    """Settings that control shard assignment, when the target is a Kinesis stream.

    If you don't include this parameter, eventId is used as the
    partition key.

    Stability:
        stable
    """
    role: aws_cdk.aws_iam.IRole
    """Role to use to invoke this event target.

    Stability:
        stable
    """
    runCommandParameters: "CfnRule.RunCommandParametersProperty"
    """Parameters used when the rule invokes Amazon EC2 Systems Manager Run Command.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-events.RuleTargetConfig", jsii_struct_bases=[_RuleTargetConfig])
class RuleTargetConfig(_RuleTargetConfig):
    """Properties for an event rule target.

    Stability:
        stable
    """
    arn: str
    """The Amazon Resource Name (ARN) of the target.

    Stability:
        stable
    """

    id: str
    """A unique, user-defined identifier for the target.

    Acceptable values
    include alphanumeric characters, periods (.), hyphens (-), and
    underscores (_).

    Stability:
        stable
    """

class RuleTargetInput(metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-events.RuleTargetInput"):
    """The input to send to the event target.

    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _RuleTargetInputProxy

    def __init__(self) -> None:
        """
        Stability:
            stable
        """
        jsii.create(RuleTargetInput, self, [])

    @jsii.member(jsii_name="fromEventPath")
    @classmethod
    def from_event_path(cls, path: str) -> "RuleTargetInput":
        """Take the event target input from a path in the event JSON.

        Arguments:
            path: -

        Stability:
            stable
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
            stable
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
            stable
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
            stable
        """
        return jsii.sinvoke(cls, "fromText", [text])

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(self, rule: "IRule") -> "RuleTargetInputProperties":
        """Return the input properties for this input object.

        Arguments:
            rule: -

        Stability:
            stable
        """
        ...


class _RuleTargetInputProxy(RuleTargetInput):
    @jsii.member(jsii_name="bind")
    def bind(self, rule: "IRule") -> "RuleTargetInputProperties":
        """Return the input properties for this input object.

        Arguments:
            rule: -

        Stability:
            stable
        """
        return jsii.invoke(self, "bind", [rule])


@jsii.data_type(jsii_type="@aws-cdk/aws-events.RuleTargetInputProperties", jsii_struct_bases=[])
class RuleTargetInputProperties(jsii.compat.TypedDict, total=False):
    """The input properties for an event target.

    Stability:
        stable
    """
    input: str
    """Literal input to the target service (must be valid JSON).

    Stability:
        stable
    """

    inputPath: str
    """JsonPath to take input from the input event.

    Stability:
        stable
    """

    inputPathsMap: typing.Mapping[str,str]
    """Paths map to extract values from event and insert into ``inputTemplate``.

    Stability:
        stable
    """

    inputTemplate: str
    """Input template to insert paths map into.

    Stability:
        stable
    """

class Schedule(metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-events.Schedule"):
    """Schedule for scheduled event rules.

    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _ScheduleProxy

    def __init__(self) -> None:
        """
        Stability:
            stable
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
            week_day: The day of the week to run this rule at. Default: - Any day of the week
            year: The year to run this rule at. Default: - Every year

        Stability:
            stable
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
            stable
        """
        return jsii.sinvoke(cls, "expression", [expression])

    @jsii.member(jsii_name="rate")
    @classmethod
    def rate(cls, duration: aws_cdk.core.Duration) -> "Schedule":
        """Construct a schedule from an interval and a time unit.

        Arguments:
            duration: -

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "rate", [duration])

    @property
    @jsii.member(jsii_name="expressionString")
    @abc.abstractmethod
    def expression_string(self) -> str:
        """Retrieve the expression for this schedule.

        Stability:
            stable
        """
        ...


class _ScheduleProxy(Schedule):
    @property
    @jsii.member(jsii_name="expressionString")
    def expression_string(self) -> str:
        """Retrieve the expression for this schedule.

        Stability:
            stable
        """
        return jsii.get(self, "expressionString")


__all__ = ["CfnEventBusPolicy", "CfnEventBusPolicyProps", "CfnRule", "CfnRuleProps", "CronOptions", "EventField", "EventPattern", "IRule", "IRuleTarget", "OnEventOptions", "Rule", "RuleProps", "RuleTargetConfig", "RuleTargetInput", "RuleTargetInputProperties", "Schedule", "__jsii_assembly__"]

publication.publish()
