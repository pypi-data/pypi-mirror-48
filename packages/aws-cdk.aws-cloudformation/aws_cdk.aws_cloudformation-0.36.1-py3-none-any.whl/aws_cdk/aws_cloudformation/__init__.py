import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_iam
import aws_cdk.aws_lambda
import aws_cdk.aws_sns
import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-cloudformation", "0.36.1", __name__, "aws-cloudformation@0.36.1.jsii.tgz")
class CfnCustomResource(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cloudformation.CfnCustomResource"):
    """A CloudFormation ``AWS::CloudFormation::CustomResource``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html
    Stability:
        stable
    cloudformationResource:
        AWS::CloudFormation::CustomResource
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, service_token: str) -> None:
        """Create a new ``AWS::CloudFormation::CustomResource``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            service_token: ``AWS::CloudFormation::CustomResource.ServiceToken``.

        Stability:
            experimental
        """
        props: CfnCustomResourceProps = {"serviceToken": service_token}

        jsii.create(CfnCustomResource, self, [scope, id, props])

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
    @jsii.member(jsii_name="serviceToken")
    def service_token(self) -> str:
        """``AWS::CloudFormation::CustomResource.ServiceToken``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html#cfn-customresource-servicetoken
        Stability:
            stable
        """
        return jsii.get(self, "serviceToken")

    @service_token.setter
    def service_token(self, value: str):
        return jsii.set(self, "serviceToken", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-cloudformation.CfnCustomResourceProps", jsii_struct_bases=[])
class CfnCustomResourceProps(jsii.compat.TypedDict):
    """Properties for defining a ``AWS::CloudFormation::CustomResource``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html
    Stability:
        stable
    """
    serviceToken: str
    """``AWS::CloudFormation::CustomResource.ServiceToken``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html#cfn-customresource-servicetoken
    Stability:
        stable
    """

class CfnMacro(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cloudformation.CfnMacro"):
    """A CloudFormation ``AWS::CloudFormation::Macro``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html
    Stability:
        stable
    cloudformationResource:
        AWS::CloudFormation::Macro
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, function_name: str, name: str, description: typing.Optional[str]=None, log_group_name: typing.Optional[str]=None, log_role_arn: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::CloudFormation::Macro``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            function_name: ``AWS::CloudFormation::Macro.FunctionName``.
            name: ``AWS::CloudFormation::Macro.Name``.
            description: ``AWS::CloudFormation::Macro.Description``.
            log_group_name: ``AWS::CloudFormation::Macro.LogGroupName``.
            log_role_arn: ``AWS::CloudFormation::Macro.LogRoleARN``.

        Stability:
            experimental
        """
        props: CfnMacroProps = {"functionName": function_name, "name": name}

        if description is not None:
            props["description"] = description

        if log_group_name is not None:
            props["logGroupName"] = log_group_name

        if log_role_arn is not None:
            props["logRoleArn"] = log_role_arn

        jsii.create(CfnMacro, self, [scope, id, props])

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
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> str:
        """``AWS::CloudFormation::Macro.FunctionName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-functionname
        Stability:
            stable
        """
        return jsii.get(self, "functionName")

    @function_name.setter
    def function_name(self, value: str):
        return jsii.set(self, "functionName", value)

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::CloudFormation::Macro.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-name
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
        """``AWS::CloudFormation::Macro.Description``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-description
        Stability:
            stable
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="logGroupName")
    def log_group_name(self) -> typing.Optional[str]:
        """``AWS::CloudFormation::Macro.LogGroupName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-loggroupname
        Stability:
            stable
        """
        return jsii.get(self, "logGroupName")

    @log_group_name.setter
    def log_group_name(self, value: typing.Optional[str]):
        return jsii.set(self, "logGroupName", value)

    @property
    @jsii.member(jsii_name="logRoleArn")
    def log_role_arn(self) -> typing.Optional[str]:
        """``AWS::CloudFormation::Macro.LogRoleARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-logrolearn
        Stability:
            stable
        """
        return jsii.get(self, "logRoleArn")

    @log_role_arn.setter
    def log_role_arn(self, value: typing.Optional[str]):
        return jsii.set(self, "logRoleArn", value)


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnMacroProps(jsii.compat.TypedDict, total=False):
    description: str
    """``AWS::CloudFormation::Macro.Description``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-description
    Stability:
        stable
    """
    logGroupName: str
    """``AWS::CloudFormation::Macro.LogGroupName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-loggroupname
    Stability:
        stable
    """
    logRoleArn: str
    """``AWS::CloudFormation::Macro.LogRoleARN``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-logrolearn
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-cloudformation.CfnMacroProps", jsii_struct_bases=[_CfnMacroProps])
class CfnMacroProps(_CfnMacroProps):
    """Properties for defining a ``AWS::CloudFormation::Macro``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html
    Stability:
        stable
    """
    functionName: str
    """``AWS::CloudFormation::Macro.FunctionName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-functionname
    Stability:
        stable
    """

    name: str
    """``AWS::CloudFormation::Macro.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html#cfn-cloudformation-macro-name
    Stability:
        stable
    """

class CfnStack(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cloudformation.CfnStack"):
    """A CloudFormation ``AWS::CloudFormation::Stack``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html
    Stability:
        stable
    cloudformationResource:
        AWS::CloudFormation::Stack
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, template_url: str, notification_arns: typing.Optional[typing.List[str]]=None, parameters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,str]]]]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None, timeout_in_minutes: typing.Optional[jsii.Number]=None) -> None:
        """Create a new ``AWS::CloudFormation::Stack``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            template_url: ``AWS::CloudFormation::Stack.TemplateURL``.
            notification_arns: ``AWS::CloudFormation::Stack.NotificationARNs``.
            parameters: ``AWS::CloudFormation::Stack.Parameters``.
            tags: ``AWS::CloudFormation::Stack.Tags``.
            timeout_in_minutes: ``AWS::CloudFormation::Stack.TimeoutInMinutes``.

        Stability:
            experimental
        """
        props: CfnStackProps = {"templateUrl": template_url}

        if notification_arns is not None:
            props["notificationArns"] = notification_arns

        if parameters is not None:
            props["parameters"] = parameters

        if tags is not None:
            props["tags"] = tags

        if timeout_in_minutes is not None:
            props["timeoutInMinutes"] = timeout_in_minutes

        jsii.create(CfnStack, self, [scope, id, props])

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
        """``AWS::CloudFormation::Stack.Tags``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-tags
        Stability:
            stable
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="templateUrl")
    def template_url(self) -> str:
        """``AWS::CloudFormation::Stack.TemplateURL``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-templateurl
        Stability:
            stable
        """
        return jsii.get(self, "templateUrl")

    @template_url.setter
    def template_url(self, value: str):
        return jsii.set(self, "templateUrl", value)

    @property
    @jsii.member(jsii_name="notificationArns")
    def notification_arns(self) -> typing.Optional[typing.List[str]]:
        """``AWS::CloudFormation::Stack.NotificationARNs``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-notificationarns
        Stability:
            stable
        """
        return jsii.get(self, "notificationArns")

    @notification_arns.setter
    def notification_arns(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "notificationArns", value)

    @property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,str]]]]:
        """``AWS::CloudFormation::Stack.Parameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-parameters
        Stability:
            stable
        """
        return jsii.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,str]]]]):
        return jsii.set(self, "parameters", value)

    @property
    @jsii.member(jsii_name="timeoutInMinutes")
    def timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        """``AWS::CloudFormation::Stack.TimeoutInMinutes``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-timeoutinminutes
        Stability:
            stable
        """
        return jsii.get(self, "timeoutInMinutes")

    @timeout_in_minutes.setter
    def timeout_in_minutes(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "timeoutInMinutes", value)


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnStackProps(jsii.compat.TypedDict, total=False):
    notificationArns: typing.List[str]
    """``AWS::CloudFormation::Stack.NotificationARNs``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-notificationarns
    Stability:
        stable
    """
    parameters: typing.Union[aws_cdk.core.IResolvable, typing.Mapping[str,str]]
    """``AWS::CloudFormation::Stack.Parameters``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-parameters
    Stability:
        stable
    """
    tags: typing.List[aws_cdk.core.CfnTag]
    """``AWS::CloudFormation::Stack.Tags``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-tags
    Stability:
        stable
    """
    timeoutInMinutes: jsii.Number
    """``AWS::CloudFormation::Stack.TimeoutInMinutes``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-timeoutinminutes
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-cloudformation.CfnStackProps", jsii_struct_bases=[_CfnStackProps])
class CfnStackProps(_CfnStackProps):
    """Properties for defining a ``AWS::CloudFormation::Stack``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html
    Stability:
        stable
    """
    templateUrl: str
    """``AWS::CloudFormation::Stack.TemplateURL``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html#cfn-cloudformation-stack-templateurl
    Stability:
        stable
    """

class CfnWaitCondition(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cloudformation.CfnWaitCondition"):
    """A CloudFormation ``AWS::CloudFormation::WaitCondition``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html
    Stability:
        stable
    cloudformationResource:
        AWS::CloudFormation::WaitCondition
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, count: typing.Optional[jsii.Number]=None, handle: typing.Optional[str]=None, timeout: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::CloudFormation::WaitCondition``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            count: ``AWS::CloudFormation::WaitCondition.Count``.
            handle: ``AWS::CloudFormation::WaitCondition.Handle``.
            timeout: ``AWS::CloudFormation::WaitCondition.Timeout``.

        Stability:
            experimental
        """
        props: CfnWaitConditionProps = {}

        if count is not None:
            props["count"] = count

        if handle is not None:
            props["handle"] = handle

        if timeout is not None:
            props["timeout"] = timeout

        jsii.create(CfnWaitCondition, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrData")
    def attr_data(self) -> aws_cdk.core.IResolvable:
        """
        Stability:
            stable
        cloudformationAttribute:
            Data
        """
        return jsii.get(self, "attrData")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="count")
    def count(self) -> typing.Optional[jsii.Number]:
        """``AWS::CloudFormation::WaitCondition.Count``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-count
        Stability:
            stable
        """
        return jsii.get(self, "count")

    @count.setter
    def count(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "count", value)

    @property
    @jsii.member(jsii_name="handle")
    def handle(self) -> typing.Optional[str]:
        """``AWS::CloudFormation::WaitCondition.Handle``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-handle
        Stability:
            stable
        """
        return jsii.get(self, "handle")

    @handle.setter
    def handle(self, value: typing.Optional[str]):
        return jsii.set(self, "handle", value)

    @property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> typing.Optional[str]:
        """``AWS::CloudFormation::WaitCondition.Timeout``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-timeout
        Stability:
            stable
        """
        return jsii.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: typing.Optional[str]):
        return jsii.set(self, "timeout", value)


class CfnWaitConditionHandle(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cloudformation.CfnWaitConditionHandle"):
    """A CloudFormation ``AWS::CloudFormation::WaitConditionHandle``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitconditionhandle.html
    Stability:
        stable
    cloudformationResource:
        AWS::CloudFormation::WaitConditionHandle
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str) -> None:
        """Create a new ``AWS::CloudFormation::WaitConditionHandle``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.

        Stability:
            experimental
        """
        jsii.create(CfnWaitConditionHandle, self, [scope, id])

    @classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> str:
        """The CloudFormation resource type name for this resource class.

        Stability:
            stable
        """
        return jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME")


@jsii.data_type(jsii_type="@aws-cdk/aws-cloudformation.CfnWaitConditionProps", jsii_struct_bases=[])
class CfnWaitConditionProps(jsii.compat.TypedDict, total=False):
    """Properties for defining a ``AWS::CloudFormation::WaitCondition``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html
    Stability:
        stable
    """
    count: jsii.Number
    """``AWS::CloudFormation::WaitCondition.Count``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-count
    Stability:
        stable
    """

    handle: str
    """``AWS::CloudFormation::WaitCondition.Handle``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-handle
    Stability:
        stable
    """

    timeout: str
    """``AWS::CloudFormation::WaitCondition.Timeout``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html#cfn-waitcondition-timeout
    Stability:
        stable
    """

@jsii.enum(jsii_type="@aws-cdk/aws-cloudformation.CloudFormationCapabilities")
class CloudFormationCapabilities(enum.Enum):
    """Capabilities that affect whether CloudFormation is allowed to change IAM resources.

    Stability:
        experimental
    """
    NONE = "NONE"
    """No IAM Capabilities.

    Pass this capability if you wish to block the creation IAM resources.

    Stability:
        experimental
    link:
        https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities
    """
    ANONYMOUS_IAM = "ANONYMOUS_IAM"
    """Capability to create anonymous IAM resources.

    Pass this capability if you're only creating anonymous resources.

    Stability:
        experimental
    link:
        https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities
    """
    NAMED_IAM = "NAMED_IAM"
    """Capability to create named IAM resources.

    Pass this capability if you're creating IAM resources that have physical
    names.

    ``CloudFormationCapabilities.NamedIAM`` implies ``CloudFormationCapabilities.IAM``; you don't have to pass both.

    Stability:
        experimental
    link:
        https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities
    """
    AUTO_EXPAND = "AUTO_EXPAND"
    """Capability to run CloudFormation macros.

    Pass this capability if your template includes macros, for example AWS::Include or AWS::Serverless.

    Stability:
        experimental
    link:
        https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStack.html
    """

class CustomResource(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cloudformation.CustomResource"):
    """Custom resource that is implemented using a Lambda.

    As a custom resource author, you should be publishing a subclass of this class
    that hides the choice of provider, and accepts a strongly-typed properties
    object with the properties your provider accepts.

    Stability:
        experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, provider: "CustomResourceProvider", properties: typing.Optional[typing.Mapping[str,typing.Any]]=None, removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy]=None, resource_type: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            provider: The provider which implements the custom resource.
            properties: Properties to pass to the Lambda. Default: - No properties.
            removal_policy: The policy to apply when this resource is removed from the application. Default: cdk.RemovalPolicy.Destroy
            resource_type: For custom resources, you can specify AWS::CloudFormation::CustomResource (the default) as the resource type, or you can specify your own resource type name. For example, you can use "Custom::MyCustomResourceTypeName". Custom resource type names must begin with "Custom::" and can include alphanumeric characters and the following characters: _@-. You can specify a custom resource type name up to a maximum length of 60 characters. You cannot change the type during an update. Using your own resource type names helps you quickly differentiate the types of custom resources in your stack. For example, if you had two custom resources that conduct two different ping tests, you could name their type as Custom::PingTester to make them easily identifiable as ping testers (instead of using AWS::CloudFormation::CustomResource). Default: - AWS::CloudFormation::CustomResource

        Stability:
            experimental
        """
        props: CustomResourceProps = {"provider": provider}

        if properties is not None:
            props["properties"] = properties

        if removal_policy is not None:
            props["removalPolicy"] = removal_policy

        if resource_type is not None:
            props["resourceType"] = resource_type

        jsii.create(CustomResource, self, [scope, id, props])

    @jsii.member(jsii_name="getAtt")
    def get_att(self, attribute_name: str) -> aws_cdk.core.IResolvable:
        """
        Arguments:
            attribute_name: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "getAtt", [attribute_name])


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CustomResourceProps(jsii.compat.TypedDict, total=False):
    properties: typing.Mapping[str,typing.Any]
    """Properties to pass to the Lambda.

    Default:
        - No properties.

    Stability:
        experimental
    """
    removalPolicy: aws_cdk.core.RemovalPolicy
    """The policy to apply when this resource is removed from the application.

    Default:
        cdk.RemovalPolicy.Destroy

    Stability:
        experimental
    """
    resourceType: str
    """For custom resources, you can specify AWS::CloudFormation::CustomResource (the default) as the resource type, or you can specify your own resource type name.

    For example, you can use "Custom::MyCustomResourceTypeName".

    Custom resource type names must begin with "Custom::" and can include
    alphanumeric characters and the following characters: _@-. You can specify
    a custom resource type name up to a maximum length of 60 characters. You
    cannot change the type during an update.

    Using your own resource type names helps you quickly differentiate the
    types of custom resources in your stack. For example, if you had two custom
    resources that conduct two different ping tests, you could name their type
    as Custom::PingTester to make them easily identifiable as ping testers
    (instead of using AWS::CloudFormation::CustomResource).

    Default:
        - AWS::CloudFormation::CustomResource

    See:
        https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html#aws-cfn-resource-type-name
    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-cloudformation.CustomResourceProps", jsii_struct_bases=[_CustomResourceProps])
class CustomResourceProps(_CustomResourceProps):
    """Properties to provide a Lambda-backed custom resource.

    Stability:
        experimental
    """
    provider: "CustomResourceProvider"
    """The provider which implements the custom resource.

    Stability:
        experimental

    Example::
        CustomResourceProvider.topic(myTopic)
    """

class CustomResourceProvider(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cloudformation.CustomResourceProvider"):
    """
    Stability:
        experimental
    """
    @jsii.member(jsii_name="lambda")
    @classmethod
    def lambda_(cls, handler: aws_cdk.aws_lambda.IFunction) -> "CustomResourceProvider":
        """The Lambda provider that implements this custom resource.

        We recommend using a lambda.SingletonFunction for this.

        Arguments:
            handler: -

        Stability:
            experimental
        """
        return jsii.sinvoke(cls, "lambda", [handler])

    @jsii.member(jsii_name="topic")
    @classmethod
    def topic(cls, topic: aws_cdk.aws_sns.ITopic) -> "CustomResourceProvider":
        """The SNS Topic for the provider that implements this custom resource.

        Arguments:
            topic: -

        Stability:
            experimental
        """
        return jsii.sinvoke(cls, "topic", [topic])

    @property
    @jsii.member(jsii_name="serviceToken")
    def service_token(self) -> str:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "serviceToken")


__all__ = ["CfnCustomResource", "CfnCustomResourceProps", "CfnMacro", "CfnMacroProps", "CfnStack", "CfnStackProps", "CfnWaitCondition", "CfnWaitConditionHandle", "CfnWaitConditionProps", "CloudFormationCapabilities", "CustomResource", "CustomResourceProps", "CustomResourceProvider", "__jsii_assembly__"]

publication.publish()
