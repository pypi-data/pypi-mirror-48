import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-sam", "0.36.2", __name__, "aws-sam@0.36.2.jsii.tgz")
class CfnApi(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-sam.CfnApi"):
    """A CloudFormation ``AWS::Serverless::Api``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
    Stability:
        stable
    cloudformationResource:
        AWS::Serverless::Api
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, stage_name: str, auth: typing.Optional[typing.Union[typing.Optional["AuthProperty"], typing.Optional[aws_cdk.core.IResolvable]]]=None, binary_media_types: typing.Optional[typing.List[str]]=None, cache_cluster_enabled: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, cache_cluster_size: typing.Optional[str]=None, cors: typing.Optional[str]=None, definition_body: typing.Any=None, definition_uri: typing.Optional[typing.Union[typing.Optional[str], typing.Optional[aws_cdk.core.IResolvable], typing.Optional["S3LocationProperty"]]]=None, endpoint_configuration: typing.Optional[str]=None, method_settings: typing.Any=None, name: typing.Optional[str]=None, tracing_enabled: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, variables: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,str]]]]=None) -> None:
        """Create a new ``AWS::Serverless::Api``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            stage_name: ``AWS::Serverless::Api.StageName``.
            auth: ``AWS::Serverless::Api.Auth``.
            binary_media_types: ``AWS::Serverless::Api.BinaryMediaTypes``.
            cache_cluster_enabled: ``AWS::Serverless::Api.CacheClusterEnabled``.
            cache_cluster_size: ``AWS::Serverless::Api.CacheClusterSize``.
            cors: ``AWS::Serverless::Api.Cors``.
            definition_body: ``AWS::Serverless::Api.DefinitionBody``.
            definition_uri: ``AWS::Serverless::Api.DefinitionUri``.
            endpoint_configuration: ``AWS::Serverless::Api.EndpointConfiguration``.
            method_settings: ``AWS::Serverless::Api.MethodSettings``.
            name: ``AWS::Serverless::Api.Name``.
            tracing_enabled: ``AWS::Serverless::Api.TracingEnabled``.
            variables: ``AWS::Serverless::Api.Variables``.

        Stability:
            stable
        """
        props: CfnApiProps = {"stageName": stage_name}

        if auth is not None:
            props["auth"] = auth

        if binary_media_types is not None:
            props["binaryMediaTypes"] = binary_media_types

        if cache_cluster_enabled is not None:
            props["cacheClusterEnabled"] = cache_cluster_enabled

        if cache_cluster_size is not None:
            props["cacheClusterSize"] = cache_cluster_size

        if cors is not None:
            props["cors"] = cors

        if definition_body is not None:
            props["definitionBody"] = definition_body

        if definition_uri is not None:
            props["definitionUri"] = definition_uri

        if endpoint_configuration is not None:
            props["endpointConfiguration"] = endpoint_configuration

        if method_settings is not None:
            props["methodSettings"] = method_settings

        if name is not None:
            props["name"] = name

        if tracing_enabled is not None:
            props["tracingEnabled"] = tracing_enabled

        if variables is not None:
            props["variables"] = variables

        jsii.create(CfnApi, self, [scope, id, props])

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

    @classproperty
    @jsii.member(jsii_name="REQUIRED_TRANSFORM")
    def REQUIRED_TRANSFORM(cls) -> str:
        """The ``Transform`` a template must use in order to use this resource.

        Stability:
            stable
        """
        return jsii.sget(cls, "REQUIRED_TRANSFORM")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="definitionBody")
    def definition_body(self) -> typing.Any:
        """``AWS::Serverless::Api.DefinitionBody``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
        Stability:
            stable
        """
        return jsii.get(self, "definitionBody")

    @definition_body.setter
    def definition_body(self, value: typing.Any):
        return jsii.set(self, "definitionBody", value)

    @property
    @jsii.member(jsii_name="methodSettings")
    def method_settings(self) -> typing.Any:
        """``AWS::Serverless::Api.MethodSettings``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
        Stability:
            stable
        """
        return jsii.get(self, "methodSettings")

    @method_settings.setter
    def method_settings(self, value: typing.Any):
        return jsii.set(self, "methodSettings", value)

    @property
    @jsii.member(jsii_name="stageName")
    def stage_name(self) -> str:
        """``AWS::Serverless::Api.StageName``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
        Stability:
            stable
        """
        return jsii.get(self, "stageName")

    @stage_name.setter
    def stage_name(self, value: str):
        return jsii.set(self, "stageName", value)

    @property
    @jsii.member(jsii_name="auth")
    def auth(self) -> typing.Optional[typing.Union[typing.Optional["AuthProperty"], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::Serverless::Api.Auth``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
        Stability:
            stable
        """
        return jsii.get(self, "auth")

    @auth.setter
    def auth(self, value: typing.Optional[typing.Union[typing.Optional["AuthProperty"], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "auth", value)

    @property
    @jsii.member(jsii_name="binaryMediaTypes")
    def binary_media_types(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Serverless::Api.BinaryMediaTypes``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
        Stability:
            stable
        """
        return jsii.get(self, "binaryMediaTypes")

    @binary_media_types.setter
    def binary_media_types(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "binaryMediaTypes", value)

    @property
    @jsii.member(jsii_name="cacheClusterEnabled")
    def cache_cluster_enabled(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::Serverless::Api.CacheClusterEnabled``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
        Stability:
            stable
        """
        return jsii.get(self, "cacheClusterEnabled")

    @cache_cluster_enabled.setter
    def cache_cluster_enabled(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "cacheClusterEnabled", value)

    @property
    @jsii.member(jsii_name="cacheClusterSize")
    def cache_cluster_size(self) -> typing.Optional[str]:
        """``AWS::Serverless::Api.CacheClusterSize``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
        Stability:
            stable
        """
        return jsii.get(self, "cacheClusterSize")

    @cache_cluster_size.setter
    def cache_cluster_size(self, value: typing.Optional[str]):
        return jsii.set(self, "cacheClusterSize", value)

    @property
    @jsii.member(jsii_name="cors")
    def cors(self) -> typing.Optional[str]:
        """``AWS::Serverless::Api.Cors``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
        Stability:
            stable
        """
        return jsii.get(self, "cors")

    @cors.setter
    def cors(self, value: typing.Optional[str]):
        return jsii.set(self, "cors", value)

    @property
    @jsii.member(jsii_name="definitionUri")
    def definition_uri(self) -> typing.Optional[typing.Union[typing.Optional[str], typing.Optional[aws_cdk.core.IResolvable], typing.Optional["S3LocationProperty"]]]:
        """``AWS::Serverless::Api.DefinitionUri``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
        Stability:
            stable
        """
        return jsii.get(self, "definitionUri")

    @definition_uri.setter
    def definition_uri(self, value: typing.Optional[typing.Union[typing.Optional[str], typing.Optional[aws_cdk.core.IResolvable], typing.Optional["S3LocationProperty"]]]):
        return jsii.set(self, "definitionUri", value)

    @property
    @jsii.member(jsii_name="endpointConfiguration")
    def endpoint_configuration(self) -> typing.Optional[str]:
        """``AWS::Serverless::Api.EndpointConfiguration``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
        Stability:
            stable
        """
        return jsii.get(self, "endpointConfiguration")

    @endpoint_configuration.setter
    def endpoint_configuration(self, value: typing.Optional[str]):
        return jsii.set(self, "endpointConfiguration", value)

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::Serverless::Api.Name``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
        Stability:
            stable
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="tracingEnabled")
    def tracing_enabled(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::Serverless::Api.TracingEnabled``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
        Stability:
            stable
        """
        return jsii.get(self, "tracingEnabled")

    @tracing_enabled.setter
    def tracing_enabled(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "tracingEnabled", value)

    @property
    @jsii.member(jsii_name="variables")
    def variables(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,str]]]]:
        """``AWS::Serverless::Api.Variables``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
        Stability:
            stable
        """
        return jsii.get(self, "variables")

    @variables.setter
    def variables(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,str]]]]):
        return jsii.set(self, "variables", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnApi.AuthProperty", jsii_struct_bases=[])
    class AuthProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#api-auth-object
        Stability:
            stable
        """
        authorizers: typing.Any
        """``CfnApi.AuthProperty.Authorizers``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#api-auth-object
        Stability:
            stable
        """

        defaultAuthorizer: str
        """``CfnApi.AuthProperty.DefaultAuthorizer``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#api-auth-object
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnApi.S3LocationProperty", jsii_struct_bases=[])
    class S3LocationProperty(jsii.compat.TypedDict):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#s3-location-object
        Stability:
            stable
        """
        bucket: str
        """``CfnApi.S3LocationProperty.Bucket``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """

        key: str
        """``CfnApi.S3LocationProperty.Key``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """

        version: jsii.Number
        """``CfnApi.S3LocationProperty.Version``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnApiProps(jsii.compat.TypedDict, total=False):
    auth: typing.Union["CfnApi.AuthProperty", aws_cdk.core.IResolvable]
    """``AWS::Serverless::Api.Auth``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
    Stability:
        stable
    """
    binaryMediaTypes: typing.List[str]
    """``AWS::Serverless::Api.BinaryMediaTypes``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
    Stability:
        stable
    """
    cacheClusterEnabled: typing.Union[bool, aws_cdk.core.IResolvable]
    """``AWS::Serverless::Api.CacheClusterEnabled``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
    Stability:
        stable
    """
    cacheClusterSize: str
    """``AWS::Serverless::Api.CacheClusterSize``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
    Stability:
        stable
    """
    cors: str
    """``AWS::Serverless::Api.Cors``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
    Stability:
        stable
    """
    definitionBody: typing.Any
    """``AWS::Serverless::Api.DefinitionBody``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
    Stability:
        stable
    """
    definitionUri: typing.Union[str, aws_cdk.core.IResolvable, "CfnApi.S3LocationProperty"]
    """``AWS::Serverless::Api.DefinitionUri``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
    Stability:
        stable
    """
    endpointConfiguration: str
    """``AWS::Serverless::Api.EndpointConfiguration``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
    Stability:
        stable
    """
    methodSettings: typing.Any
    """``AWS::Serverless::Api.MethodSettings``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
    Stability:
        stable
    """
    name: str
    """``AWS::Serverless::Api.Name``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
    Stability:
        stable
    """
    tracingEnabled: typing.Union[bool, aws_cdk.core.IResolvable]
    """``AWS::Serverless::Api.TracingEnabled``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
    Stability:
        stable
    """
    variables: typing.Union[aws_cdk.core.IResolvable, typing.Mapping[str,str]]
    """``AWS::Serverless::Api.Variables``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnApiProps", jsii_struct_bases=[_CfnApiProps])
class CfnApiProps(_CfnApiProps):
    """Properties for defining a ``AWS::Serverless::Api``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
    Stability:
        stable
    """
    stageName: str
    """``AWS::Serverless::Api.StageName``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi
    Stability:
        stable
    """

class CfnApplication(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-sam.CfnApplication"):
    """A CloudFormation ``AWS::Serverless::Application``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapplication
    Stability:
        stable
    cloudformationResource:
        AWS::Serverless::Application
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, location: typing.Union[str, aws_cdk.core.IResolvable, "ApplicationLocationProperty"], notification_arns: typing.Optional[typing.List[str]]=None, parameters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,str]]]]=None, tags: typing.Optional[typing.Mapping[str,str]]=None, timeout_in_minutes: typing.Optional[jsii.Number]=None) -> None:
        """Create a new ``AWS::Serverless::Application``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            location: ``AWS::Serverless::Application.Location``.
            notification_arns: ``AWS::Serverless::Application.NotificationArns``.
            parameters: ``AWS::Serverless::Application.Parameters``.
            tags: ``AWS::Serverless::Application.Tags``.
            timeout_in_minutes: ``AWS::Serverless::Application.TimeoutInMinutes``.

        Stability:
            stable
        """
        props: CfnApplicationProps = {"location": location}

        if notification_arns is not None:
            props["notificationArns"] = notification_arns

        if parameters is not None:
            props["parameters"] = parameters

        if tags is not None:
            props["tags"] = tags

        if timeout_in_minutes is not None:
            props["timeoutInMinutes"] = timeout_in_minutes

        jsii.create(CfnApplication, self, [scope, id, props])

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

    @classproperty
    @jsii.member(jsii_name="REQUIRED_TRANSFORM")
    def REQUIRED_TRANSFORM(cls) -> str:
        """The ``Transform`` a template must use in order to use this resource.

        Stability:
            stable
        """
        return jsii.sget(cls, "REQUIRED_TRANSFORM")

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
        """``AWS::Serverless::Application.Tags``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapplication
        Stability:
            stable
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="location")
    def location(self) -> typing.Union[str, aws_cdk.core.IResolvable, "ApplicationLocationProperty"]:
        """``AWS::Serverless::Application.Location``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapplication
        Stability:
            stable
        """
        return jsii.get(self, "location")

    @location.setter
    def location(self, value: typing.Union[str, aws_cdk.core.IResolvable, "ApplicationLocationProperty"]):
        return jsii.set(self, "location", value)

    @property
    @jsii.member(jsii_name="notificationArns")
    def notification_arns(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Serverless::Application.NotificationArns``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapplication
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
        """``AWS::Serverless::Application.Parameters``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapplication
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
        """``AWS::Serverless::Application.TimeoutInMinutes``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapplication
        Stability:
            stable
        """
        return jsii.get(self, "timeoutInMinutes")

    @timeout_in_minutes.setter
    def timeout_in_minutes(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "timeoutInMinutes", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnApplication.ApplicationLocationProperty", jsii_struct_bases=[])
    class ApplicationLocationProperty(jsii.compat.TypedDict):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapplication
        Stability:
            stable
        """
        applicationId: str
        """``CfnApplication.ApplicationLocationProperty.ApplicationId``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapplication
        Stability:
            stable
        """

        semanticVersion: str
        """``CfnApplication.ApplicationLocationProperty.SemanticVersion``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapplication
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnApplicationProps(jsii.compat.TypedDict, total=False):
    notificationArns: typing.List[str]
    """``AWS::Serverless::Application.NotificationArns``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapplication
    Stability:
        stable
    """
    parameters: typing.Union[aws_cdk.core.IResolvable, typing.Mapping[str,str]]
    """``AWS::Serverless::Application.Parameters``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapplication
    Stability:
        stable
    """
    tags: typing.Mapping[str,str]
    """``AWS::Serverless::Application.Tags``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapplication
    Stability:
        stable
    """
    timeoutInMinutes: jsii.Number
    """``AWS::Serverless::Application.TimeoutInMinutes``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapplication
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnApplicationProps", jsii_struct_bases=[_CfnApplicationProps])
class CfnApplicationProps(_CfnApplicationProps):
    """Properties for defining a ``AWS::Serverless::Application``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapplication
    Stability:
        stable
    """
    location: typing.Union[str, aws_cdk.core.IResolvable, "CfnApplication.ApplicationLocationProperty"]
    """``AWS::Serverless::Application.Location``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapplication
    Stability:
        stable
    """

class CfnFunction(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-sam.CfnFunction"):
    """A CloudFormation ``AWS::Serverless::Function``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    cloudformationResource:
        AWS::Serverless::Function
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, code_uri: typing.Union[str, aws_cdk.core.IResolvable, "S3LocationProperty"], handler: str, runtime: str, auto_publish_alias: typing.Optional[str]=None, dead_letter_queue: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["DeadLetterQueueProperty"]]]=None, deployment_preference: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["DeploymentPreferenceProperty"]]]=None, description: typing.Optional[str]=None, environment: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["FunctionEnvironmentProperty"]]]=None, events: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,typing.Union[aws_cdk.core.IResolvable, "EventSourceProperty"]]]]]=None, function_name: typing.Optional[str]=None, kms_key_arn: typing.Optional[str]=None, layers: typing.Optional[typing.List[str]]=None, memory_size: typing.Optional[jsii.Number]=None, permissions_boundary: typing.Optional[str]=None, policies: typing.Optional[typing.Union[typing.Optional[str], typing.Optional[aws_cdk.core.IResolvable], typing.Optional["IAMPolicyDocumentProperty"], typing.Optional[typing.List[typing.Union[str, aws_cdk.core.IResolvable, "IAMPolicyDocumentProperty", "SAMPolicyTemplateProperty"]]]]]=None, reserved_concurrent_executions: typing.Optional[jsii.Number]=None, role: typing.Optional[str]=None, tags: typing.Optional[typing.Mapping[str,str]]=None, timeout: typing.Optional[jsii.Number]=None, tracing: typing.Optional[str]=None, vpc_config: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["VpcConfigProperty"]]]=None) -> None:
        """Create a new ``AWS::Serverless::Function``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            code_uri: ``AWS::Serverless::Function.CodeUri``.
            handler: ``AWS::Serverless::Function.Handler``.
            runtime: ``AWS::Serverless::Function.Runtime``.
            auto_publish_alias: ``AWS::Serverless::Function.AutoPublishAlias``.
            dead_letter_queue: ``AWS::Serverless::Function.DeadLetterQueue``.
            deployment_preference: ``AWS::Serverless::Function.DeploymentPreference``.
            description: ``AWS::Serverless::Function.Description``.
            environment: ``AWS::Serverless::Function.Environment``.
            events: ``AWS::Serverless::Function.Events``.
            function_name: ``AWS::Serverless::Function.FunctionName``.
            kms_key_arn: ``AWS::Serverless::Function.KmsKeyArn``.
            layers: ``AWS::Serverless::Function.Layers``.
            memory_size: ``AWS::Serverless::Function.MemorySize``.
            permissions_boundary: ``AWS::Serverless::Function.PermissionsBoundary``.
            policies: ``AWS::Serverless::Function.Policies``.
            reserved_concurrent_executions: ``AWS::Serverless::Function.ReservedConcurrentExecutions``.
            role: ``AWS::Serverless::Function.Role``.
            tags: ``AWS::Serverless::Function.Tags``.
            timeout: ``AWS::Serverless::Function.Timeout``.
            tracing: ``AWS::Serverless::Function.Tracing``.
            vpc_config: ``AWS::Serverless::Function.VpcConfig``.

        Stability:
            stable
        """
        props: CfnFunctionProps = {"codeUri": code_uri, "handler": handler, "runtime": runtime}

        if auto_publish_alias is not None:
            props["autoPublishAlias"] = auto_publish_alias

        if dead_letter_queue is not None:
            props["deadLetterQueue"] = dead_letter_queue

        if deployment_preference is not None:
            props["deploymentPreference"] = deployment_preference

        if description is not None:
            props["description"] = description

        if environment is not None:
            props["environment"] = environment

        if events is not None:
            props["events"] = events

        if function_name is not None:
            props["functionName"] = function_name

        if kms_key_arn is not None:
            props["kmsKeyArn"] = kms_key_arn

        if layers is not None:
            props["layers"] = layers

        if memory_size is not None:
            props["memorySize"] = memory_size

        if permissions_boundary is not None:
            props["permissionsBoundary"] = permissions_boundary

        if policies is not None:
            props["policies"] = policies

        if reserved_concurrent_executions is not None:
            props["reservedConcurrentExecutions"] = reserved_concurrent_executions

        if role is not None:
            props["role"] = role

        if tags is not None:
            props["tags"] = tags

        if timeout is not None:
            props["timeout"] = timeout

        if tracing is not None:
            props["tracing"] = tracing

        if vpc_config is not None:
            props["vpcConfig"] = vpc_config

        jsii.create(CfnFunction, self, [scope, id, props])

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

    @classproperty
    @jsii.member(jsii_name="REQUIRED_TRANSFORM")
    def REQUIRED_TRANSFORM(cls) -> str:
        """The ``Transform`` a template must use in order to use this resource.

        Stability:
            stable
        """
        return jsii.sget(cls, "REQUIRED_TRANSFORM")

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
        """``AWS::Serverless::Function.Tags``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="codeUri")
    def code_uri(self) -> typing.Union[str, aws_cdk.core.IResolvable, "S3LocationProperty"]:
        """``AWS::Serverless::Function.CodeUri``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """
        return jsii.get(self, "codeUri")

    @code_uri.setter
    def code_uri(self, value: typing.Union[str, aws_cdk.core.IResolvable, "S3LocationProperty"]):
        return jsii.set(self, "codeUri", value)

    @property
    @jsii.member(jsii_name="handler")
    def handler(self) -> str:
        """``AWS::Serverless::Function.Handler``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """
        return jsii.get(self, "handler")

    @handler.setter
    def handler(self, value: str):
        return jsii.set(self, "handler", value)

    @property
    @jsii.member(jsii_name="runtime")
    def runtime(self) -> str:
        """``AWS::Serverless::Function.Runtime``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """
        return jsii.get(self, "runtime")

    @runtime.setter
    def runtime(self, value: str):
        return jsii.set(self, "runtime", value)

    @property
    @jsii.member(jsii_name="autoPublishAlias")
    def auto_publish_alias(self) -> typing.Optional[str]:
        """``AWS::Serverless::Function.AutoPublishAlias``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """
        return jsii.get(self, "autoPublishAlias")

    @auto_publish_alias.setter
    def auto_publish_alias(self, value: typing.Optional[str]):
        return jsii.set(self, "autoPublishAlias", value)

    @property
    @jsii.member(jsii_name="deadLetterQueue")
    def dead_letter_queue(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["DeadLetterQueueProperty"]]]:
        """``AWS::Serverless::Function.DeadLetterQueue``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """
        return jsii.get(self, "deadLetterQueue")

    @dead_letter_queue.setter
    def dead_letter_queue(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["DeadLetterQueueProperty"]]]):
        return jsii.set(self, "deadLetterQueue", value)

    @property
    @jsii.member(jsii_name="deploymentPreference")
    def deployment_preference(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["DeploymentPreferenceProperty"]]]:
        """``AWS::Serverless::Function.DeploymentPreference``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#deploymentpreference-object
        Stability:
            stable
        """
        return jsii.get(self, "deploymentPreference")

    @deployment_preference.setter
    def deployment_preference(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["DeploymentPreferenceProperty"]]]):
        return jsii.set(self, "deploymentPreference", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::Serverless::Function.Description``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="environment")
    def environment(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["FunctionEnvironmentProperty"]]]:
        """``AWS::Serverless::Function.Environment``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """
        return jsii.get(self, "environment")

    @environment.setter
    def environment(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["FunctionEnvironmentProperty"]]]):
        return jsii.set(self, "environment", value)

    @property
    @jsii.member(jsii_name="events")
    def events(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,typing.Union[aws_cdk.core.IResolvable, "EventSourceProperty"]]]]]:
        """``AWS::Serverless::Function.Events``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """
        return jsii.get(self, "events")

    @events.setter
    def events(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.Mapping[str,typing.Union[aws_cdk.core.IResolvable, "EventSourceProperty"]]]]]):
        return jsii.set(self, "events", value)

    @property
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> typing.Optional[str]:
        """``AWS::Serverless::Function.FunctionName``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """
        return jsii.get(self, "functionName")

    @function_name.setter
    def function_name(self, value: typing.Optional[str]):
        return jsii.set(self, "functionName", value)

    @property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[str]:
        """``AWS::Serverless::Function.KmsKeyArn``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """
        return jsii.get(self, "kmsKeyArn")

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[str]):
        return jsii.set(self, "kmsKeyArn", value)

    @property
    @jsii.member(jsii_name="layers")
    def layers(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Serverless::Function.Layers``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """
        return jsii.get(self, "layers")

    @layers.setter
    def layers(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "layers", value)

    @property
    @jsii.member(jsii_name="memorySize")
    def memory_size(self) -> typing.Optional[jsii.Number]:
        """``AWS::Serverless::Function.MemorySize``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """
        return jsii.get(self, "memorySize")

    @memory_size.setter
    def memory_size(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "memorySize", value)

    @property
    @jsii.member(jsii_name="permissionsBoundary")
    def permissions_boundary(self) -> typing.Optional[str]:
        """``AWS::Serverless::Function.PermissionsBoundary``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """
        return jsii.get(self, "permissionsBoundary")

    @permissions_boundary.setter
    def permissions_boundary(self, value: typing.Optional[str]):
        return jsii.set(self, "permissionsBoundary", value)

    @property
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.Optional[typing.Union[typing.Optional[str], typing.Optional[aws_cdk.core.IResolvable], typing.Optional["IAMPolicyDocumentProperty"], typing.Optional[typing.List[typing.Union[str, aws_cdk.core.IResolvable, "IAMPolicyDocumentProperty", "SAMPolicyTemplateProperty"]]]]]:
        """``AWS::Serverless::Function.Policies``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """
        return jsii.get(self, "policies")

    @policies.setter
    def policies(self, value: typing.Optional[typing.Union[typing.Optional[str], typing.Optional[aws_cdk.core.IResolvable], typing.Optional["IAMPolicyDocumentProperty"], typing.Optional[typing.List[typing.Union[str, aws_cdk.core.IResolvable, "IAMPolicyDocumentProperty", "SAMPolicyTemplateProperty"]]]]]):
        return jsii.set(self, "policies", value)

    @property
    @jsii.member(jsii_name="reservedConcurrentExecutions")
    def reserved_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        """``AWS::Serverless::Function.ReservedConcurrentExecutions``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """
        return jsii.get(self, "reservedConcurrentExecutions")

    @reserved_concurrent_executions.setter
    def reserved_concurrent_executions(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "reservedConcurrentExecutions", value)

    @property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[str]:
        """``AWS::Serverless::Function.Role``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """
        return jsii.get(self, "role")

    @role.setter
    def role(self, value: typing.Optional[str]):
        return jsii.set(self, "role", value)

    @property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> typing.Optional[jsii.Number]:
        """``AWS::Serverless::Function.Timeout``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """
        return jsii.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "timeout", value)

    @property
    @jsii.member(jsii_name="tracing")
    def tracing(self) -> typing.Optional[str]:
        """``AWS::Serverless::Function.Tracing``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """
        return jsii.get(self, "tracing")

    @tracing.setter
    def tracing(self, value: typing.Optional[str]):
        return jsii.set(self, "tracing", value)

    @property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["VpcConfigProperty"]]]:
        """``AWS::Serverless::Function.VpcConfig``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """
        return jsii.get(self, "vpcConfig")

    @vpc_config.setter
    def vpc_config(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["VpcConfigProperty"]]]):
        return jsii.set(self, "vpcConfig", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.AlexaSkillEventProperty", jsii_struct_bases=[])
    class AlexaSkillEventProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#alexaskill
        Stability:
            stable
        """
        variables: typing.Union[aws_cdk.core.IResolvable, typing.Mapping[str,str]]
        """``CfnFunction.AlexaSkillEventProperty.Variables``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#alexaskill
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _ApiEventProperty(jsii.compat.TypedDict, total=False):
        restApiId: str
        """``CfnFunction.ApiEventProperty.RestApiId``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#api
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.ApiEventProperty", jsii_struct_bases=[_ApiEventProperty])
    class ApiEventProperty(_ApiEventProperty):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#api
        Stability:
            stable
        """
        method: str
        """``CfnFunction.ApiEventProperty.Method``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#api
        Stability:
            stable
        """

        path: str
        """``CfnFunction.ApiEventProperty.Path``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#api
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.BucketSAMPTProperty", jsii_struct_bases=[])
    class BucketSAMPTProperty(jsii.compat.TypedDict):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """
        bucketName: str
        """``CfnFunction.BucketSAMPTProperty.BucketName``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _CloudWatchEventEventProperty(jsii.compat.TypedDict, total=False):
        input: str
        """``CfnFunction.CloudWatchEventEventProperty.Input``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#cloudwatchevent
        Stability:
            stable
        """
        inputPath: str
        """``CfnFunction.CloudWatchEventEventProperty.InputPath``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#cloudwatchevent
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.CloudWatchEventEventProperty", jsii_struct_bases=[_CloudWatchEventEventProperty])
    class CloudWatchEventEventProperty(_CloudWatchEventEventProperty):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#cloudwatchevent
        Stability:
            stable
        """
        pattern: typing.Any
        """``CfnFunction.CloudWatchEventEventProperty.Pattern``.

        See:
            http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/CloudWatchEventsandEventPatterns.html
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.CollectionSAMPTProperty", jsii_struct_bases=[])
    class CollectionSAMPTProperty(jsii.compat.TypedDict):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """
        collectionId: str
        """``CfnFunction.CollectionSAMPTProperty.CollectionId``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.DeadLetterQueueProperty", jsii_struct_bases=[])
    class DeadLetterQueueProperty(jsii.compat.TypedDict):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#deadletterqueue-object
        Stability:
            stable
        """
        targetArn: str
        """``CfnFunction.DeadLetterQueueProperty.TargetArn``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """

        type: str
        """``CfnFunction.DeadLetterQueueProperty.Type``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _DeploymentPreferenceProperty(jsii.compat.TypedDict, total=False):
        alarms: typing.List[str]
        """``CfnFunction.DeploymentPreferenceProperty.Alarms``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#deploymentpreference-object
        Stability:
            stable
        """
        hooks: typing.List[str]
        """``CfnFunction.DeploymentPreferenceProperty.Hooks``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#deploymentpreference-object
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.DeploymentPreferenceProperty", jsii_struct_bases=[_DeploymentPreferenceProperty])
    class DeploymentPreferenceProperty(_DeploymentPreferenceProperty):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/safe_lambda_deployments.rst
        Stability:
            stable
        """
        enabled: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnFunction.DeploymentPreferenceProperty.Enabled``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#deploymentpreference-object
        Stability:
            stable
        """

        type: str
        """``CfnFunction.DeploymentPreferenceProperty.Type``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#deploymentpreference-object
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.DomainSAMPTProperty", jsii_struct_bases=[])
    class DomainSAMPTProperty(jsii.compat.TypedDict):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """
        domainName: str
        """``CfnFunction.DomainSAMPTProperty.DomainName``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _DynamoDBEventProperty(jsii.compat.TypedDict, total=False):
        batchSize: jsii.Number
        """``CfnFunction.DynamoDBEventProperty.BatchSize``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#dynamodb
        Stability:
            stable
        """
        enabled: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnFunction.DynamoDBEventProperty.Enabled``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#dynamodb
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.DynamoDBEventProperty", jsii_struct_bases=[_DynamoDBEventProperty])
    class DynamoDBEventProperty(_DynamoDBEventProperty):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#dynamodb
        Stability:
            stable
        """
        startingPosition: str
        """``CfnFunction.DynamoDBEventProperty.StartingPosition``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#dynamodb
        Stability:
            stable
        """

        stream: str
        """``CfnFunction.DynamoDBEventProperty.Stream``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#dynamodb
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.EmptySAMPTProperty", jsii_struct_bases=[])
    class EmptySAMPTProperty(jsii.compat.TypedDict):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """
        pass

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.EventSourceProperty", jsii_struct_bases=[])
    class EventSourceProperty(jsii.compat.TypedDict):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#event-source-object
        Stability:
            stable
        """
        properties: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.AlexaSkillEventProperty", "CfnFunction.ApiEventProperty", "CfnFunction.CloudWatchEventEventProperty", "CfnFunction.DynamoDBEventProperty", "CfnFunction.S3EventProperty", "CfnFunction.SNSEventProperty", "CfnFunction.SQSEventProperty", "CfnFunction.KinesisEventProperty", "CfnFunction.ScheduleEventProperty", "CfnFunction.IoTRuleEventProperty"]
        """``CfnFunction.EventSourceProperty.Properties``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#event-source-types
        Stability:
            stable
        """

        type: str
        """``CfnFunction.EventSourceProperty.Type``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#event-source-object
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.FunctionEnvironmentProperty", jsii_struct_bases=[])
    class FunctionEnvironmentProperty(jsii.compat.TypedDict):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#environment-object
        Stability:
            stable
        """
        variables: typing.Union[aws_cdk.core.IResolvable, typing.Mapping[str,str]]
        """``CfnFunction.FunctionEnvironmentProperty.Variables``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#environment-object
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.FunctionSAMPTProperty", jsii_struct_bases=[])
    class FunctionSAMPTProperty(jsii.compat.TypedDict):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """
        functionName: str
        """``CfnFunction.FunctionSAMPTProperty.FunctionName``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

    @jsii.interface(jsii_type="@aws-cdk/aws-sam.CfnFunction.IAMPolicyDocumentProperty")
    class IAMPolicyDocumentProperty(jsii.compat.Protocol):
        """
        See:
            http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html
        Stability:
            stable
        """
        @staticmethod
        def __jsii_proxy_class__():
            return _IAMPolicyDocumentPropertyProxy

        @property
        @jsii.member(jsii_name="statement")
        def statement(self) -> typing.Any:
            """``CfnFunction.IAMPolicyDocumentProperty.Statement``.

            See:
                http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html
            Stability:
                stable
            """
            ...


    class _IAMPolicyDocumentPropertyProxy():
        """
        See:
            http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html
        Stability:
            stable
        """
        __jsii_type__ = "@aws-cdk/aws-sam.CfnFunction.IAMPolicyDocumentProperty"
        @property
        @jsii.member(jsii_name="statement")
        def statement(self) -> typing.Any:
            """``CfnFunction.IAMPolicyDocumentProperty.Statement``.

            See:
                http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html
            Stability:
                stable
            """
            return jsii.get(self, "statement")


    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.IdentitySAMPTProperty", jsii_struct_bases=[])
    class IdentitySAMPTProperty(jsii.compat.TypedDict):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """
        identityName: str
        """``CfnFunction.IdentitySAMPTProperty.IdentityName``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _IoTRuleEventProperty(jsii.compat.TypedDict, total=False):
        awsIotSqlVersion: str
        """``CfnFunction.IoTRuleEventProperty.AwsIotSqlVersion``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#iotrule
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.IoTRuleEventProperty", jsii_struct_bases=[_IoTRuleEventProperty])
    class IoTRuleEventProperty(_IoTRuleEventProperty):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#iotrule
        Stability:
            stable
        """
        sql: str
        """``CfnFunction.IoTRuleEventProperty.Sql``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#iotrule
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.KeySAMPTProperty", jsii_struct_bases=[])
    class KeySAMPTProperty(jsii.compat.TypedDict):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """
        keyId: str
        """``CfnFunction.KeySAMPTProperty.KeyId``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _KinesisEventProperty(jsii.compat.TypedDict, total=False):
        batchSize: jsii.Number
        """``CfnFunction.KinesisEventProperty.BatchSize``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#kinesis
        Stability:
            stable
        """
        enabled: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnFunction.KinesisEventProperty.Enabled``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#kinesis
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.KinesisEventProperty", jsii_struct_bases=[_KinesisEventProperty])
    class KinesisEventProperty(_KinesisEventProperty):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#kinesis
        Stability:
            stable
        """
        startingPosition: str
        """``CfnFunction.KinesisEventProperty.StartingPosition``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#kinesis
        Stability:
            stable
        """

        stream: str
        """``CfnFunction.KinesisEventProperty.Stream``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#kinesis
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.LogGroupSAMPTProperty", jsii_struct_bases=[])
    class LogGroupSAMPTProperty(jsii.compat.TypedDict):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """
        logGroupName: str
        """``CfnFunction.LogGroupSAMPTProperty.LogGroupName``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.QueueSAMPTProperty", jsii_struct_bases=[])
    class QueueSAMPTProperty(jsii.compat.TypedDict):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """
        queueName: str
        """``CfnFunction.QueueSAMPTProperty.QueueName``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _S3EventProperty(jsii.compat.TypedDict, total=False):
        filter: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.S3NotificationFilterProperty"]
        """``CfnFunction.S3EventProperty.Filter``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#s3
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.S3EventProperty", jsii_struct_bases=[_S3EventProperty])
    class S3EventProperty(_S3EventProperty):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#s3
        Stability:
            stable
        """
        bucket: str
        """``CfnFunction.S3EventProperty.Bucket``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#s3
        Stability:
            stable
        """

        events: typing.Union[str, aws_cdk.core.IResolvable, typing.List[str]]
        """``CfnFunction.S3EventProperty.Events``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#s3
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _S3LocationProperty(jsii.compat.TypedDict, total=False):
        version: jsii.Number
        """``CfnFunction.S3LocationProperty.Version``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.S3LocationProperty", jsii_struct_bases=[_S3LocationProperty])
    class S3LocationProperty(_S3LocationProperty):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#s3-location-object
        Stability:
            stable
        """
        bucket: str
        """``CfnFunction.S3LocationProperty.Bucket``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """

        key: str
        """``CfnFunction.S3LocationProperty.Key``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.S3NotificationFilterProperty", jsii_struct_bases=[])
    class S3NotificationFilterProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfiguration-config-filter.html
        Stability:
            stable
        """
        s3Key: str
        """``CfnFunction.S3NotificationFilterProperty.S3Key``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-notificationconfiguration-config-filter.html
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.SAMPolicyTemplateProperty", jsii_struct_bases=[])
    class SAMPolicyTemplateProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """
        amiDescribePolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.EmptySAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.AMIDescribePolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        cloudFormationDescribeStacksPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.EmptySAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.CloudFormationDescribeStacksPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        cloudWatchPutMetricPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.EmptySAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.CloudWatchPutMetricPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        dynamoDbCrudPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.TableSAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.DynamoDBCrudPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        dynamoDbReadPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.TableSAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.DynamoDBReadPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        dynamoDbStreamReadPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.TableStreamSAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.DynamoDBStreamReadPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        ec2DescribePolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.EmptySAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.EC2DescribePolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        elasticsearchHttpPostPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.DomainSAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.ElasticsearchHttpPostPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        filterLogEventsPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.LogGroupSAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.FilterLogEventsPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        kinesisCrudPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.StreamSAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.KinesisCrudPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        kinesisStreamReadPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.StreamSAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.KinesisStreamReadPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        kmsDecryptPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.KeySAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.KMSDecryptPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        lambdaInvokePolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.FunctionSAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.LambdaInvokePolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        rekognitionDetectOnlyPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.EmptySAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.RekognitionDetectOnlyPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        rekognitionLabelsPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.EmptySAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.RekognitionLabelsPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        rekognitionNoDataAccessPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.CollectionSAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.RekognitionNoDataAccessPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        rekognitionReadPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.CollectionSAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.RekognitionReadPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        rekognitionWriteOnlyAccessPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.CollectionSAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.RekognitionWriteOnlyAccessPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        s3CrudPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.BucketSAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.S3CrudPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        s3ReadPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.BucketSAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.S3ReadPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        sesBulkTemplatedCrudPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.IdentitySAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.SESBulkTemplatedCrudPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        sesCrudPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.IdentitySAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.SESCrudPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        sesEmailTemplateCrudPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.EmptySAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.SESEmailTemplateCrudPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        sesSendBouncePolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.IdentitySAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.SESSendBouncePolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        snsCrudPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.TopicSAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.SNSCrudPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        snsPublishMessagePolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.TopicSAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.SNSPublishMessagePolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        sqsPollerPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.QueueSAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.SQSPollerPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        sqsSendMessagePolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.QueueSAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.SQSSendMessagePolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        stepFunctionsExecutionPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.StateMachineSAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.StepFunctionsExecutionPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        vpcAccessPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.EmptySAMPTProperty"]
        """``CfnFunction.SAMPolicyTemplateProperty.VPCAccessPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.SNSEventProperty", jsii_struct_bases=[])
    class SNSEventProperty(jsii.compat.TypedDict):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#sns
        Stability:
            stable
        """
        topic: str
        """``CfnFunction.SNSEventProperty.Topic``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#sns
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _SQSEventProperty(jsii.compat.TypedDict, total=False):
        batchSize: jsii.Number
        """``CfnFunction.SQSEventProperty.BatchSize``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#sqs
        Stability:
            stable
        """
        enabled: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnFunction.SQSEventProperty.Enabled``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#sqs
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.SQSEventProperty", jsii_struct_bases=[_SQSEventProperty])
    class SQSEventProperty(_SQSEventProperty):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#sqs
        Stability:
            stable
        """
        queue: str
        """``CfnFunction.SQSEventProperty.Queue``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#sqs
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _ScheduleEventProperty(jsii.compat.TypedDict, total=False):
        input: str
        """``CfnFunction.ScheduleEventProperty.Input``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#schedule
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.ScheduleEventProperty", jsii_struct_bases=[_ScheduleEventProperty])
    class ScheduleEventProperty(_ScheduleEventProperty):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#schedule
        Stability:
            stable
        """
        schedule: str
        """``CfnFunction.ScheduleEventProperty.Schedule``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#schedule
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.StateMachineSAMPTProperty", jsii_struct_bases=[])
    class StateMachineSAMPTProperty(jsii.compat.TypedDict):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """
        stateMachineName: str
        """``CfnFunction.StateMachineSAMPTProperty.StateMachineName``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.StreamSAMPTProperty", jsii_struct_bases=[])
    class StreamSAMPTProperty(jsii.compat.TypedDict):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """
        streamName: str
        """``CfnFunction.StreamSAMPTProperty.StreamName``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.TableSAMPTProperty", jsii_struct_bases=[])
    class TableSAMPTProperty(jsii.compat.TypedDict):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """
        tableName: str
        """``CfnFunction.TableSAMPTProperty.TableName``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.TableStreamSAMPTProperty", jsii_struct_bases=[])
    class TableStreamSAMPTProperty(jsii.compat.TypedDict):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """
        streamName: str
        """``CfnFunction.TableStreamSAMPTProperty.StreamName``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

        tableName: str
        """``CfnFunction.TableStreamSAMPTProperty.TableName``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.TopicSAMPTProperty", jsii_struct_bases=[])
    class TopicSAMPTProperty(jsii.compat.TypedDict):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """
        topicName: str
        """``CfnFunction.TopicSAMPTProperty.TopicName``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/docs/policy_templates.rst
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunction.VpcConfigProperty", jsii_struct_bases=[])
    class VpcConfigProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html
        Stability:
            stable
        """
        securityGroupIds: typing.List[str]
        """``CfnFunction.VpcConfigProperty.SecurityGroupIds``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html
        Stability:
            stable
        """

        subnetIds: typing.List[str]
        """``CfnFunction.VpcConfigProperty.SubnetIds``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnFunctionProps(jsii.compat.TypedDict, total=False):
    autoPublishAlias: str
    """``AWS::Serverless::Function.AutoPublishAlias``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """
    deadLetterQueue: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.DeadLetterQueueProperty"]
    """``AWS::Serverless::Function.DeadLetterQueue``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """
    deploymentPreference: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.DeploymentPreferenceProperty"]
    """``AWS::Serverless::Function.DeploymentPreference``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#deploymentpreference-object
    Stability:
        stable
    """
    description: str
    """``AWS::Serverless::Function.Description``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """
    environment: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.FunctionEnvironmentProperty"]
    """``AWS::Serverless::Function.Environment``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """
    events: typing.Union[aws_cdk.core.IResolvable, typing.Mapping[str,typing.Union[aws_cdk.core.IResolvable, "CfnFunction.EventSourceProperty"]]]
    """``AWS::Serverless::Function.Events``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """
    functionName: str
    """``AWS::Serverless::Function.FunctionName``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """
    kmsKeyArn: str
    """``AWS::Serverless::Function.KmsKeyArn``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """
    layers: typing.List[str]
    """``AWS::Serverless::Function.Layers``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """
    memorySize: jsii.Number
    """``AWS::Serverless::Function.MemorySize``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """
    permissionsBoundary: str
    """``AWS::Serverless::Function.PermissionsBoundary``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """
    policies: typing.Union[str, aws_cdk.core.IResolvable, "CfnFunction.IAMPolicyDocumentProperty", typing.List[typing.Union[str, aws_cdk.core.IResolvable, "CfnFunction.IAMPolicyDocumentProperty", "CfnFunction.SAMPolicyTemplateProperty"]]]
    """``AWS::Serverless::Function.Policies``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """
    reservedConcurrentExecutions: jsii.Number
    """``AWS::Serverless::Function.ReservedConcurrentExecutions``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """
    role: str
    """``AWS::Serverless::Function.Role``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """
    tags: typing.Mapping[str,str]
    """``AWS::Serverless::Function.Tags``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """
    timeout: jsii.Number
    """``AWS::Serverless::Function.Timeout``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """
    tracing: str
    """``AWS::Serverless::Function.Tracing``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """
    vpcConfig: typing.Union[aws_cdk.core.IResolvable, "CfnFunction.VpcConfigProperty"]
    """``AWS::Serverless::Function.VpcConfig``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnFunctionProps", jsii_struct_bases=[_CfnFunctionProps])
class CfnFunctionProps(_CfnFunctionProps):
    """Properties for defining a ``AWS::Serverless::Function``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """
    codeUri: typing.Union[str, aws_cdk.core.IResolvable, "CfnFunction.S3LocationProperty"]
    """``AWS::Serverless::Function.CodeUri``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """

    handler: str
    """``AWS::Serverless::Function.Handler``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """

    runtime: str
    """``AWS::Serverless::Function.Runtime``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Stability:
        stable
    """

class CfnLayerVersion(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-sam.CfnLayerVersion"):
    """A CloudFormation ``AWS::Serverless::LayerVersion``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesslayerversion
    Stability:
        stable
    cloudformationResource:
        AWS::Serverless::LayerVersion
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, compatible_runtimes: typing.Optional[typing.List[str]]=None, content_uri: typing.Optional[str]=None, description: typing.Optional[str]=None, layer_name: typing.Optional[str]=None, license_info: typing.Optional[str]=None, retention_policy: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::Serverless::LayerVersion``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            compatible_runtimes: ``AWS::Serverless::LayerVersion.CompatibleRuntimes``.
            content_uri: ``AWS::Serverless::LayerVersion.ContentUri``.
            description: ``AWS::Serverless::LayerVersion.Description``.
            layer_name: ``AWS::Serverless::LayerVersion.LayerName``.
            license_info: ``AWS::Serverless::LayerVersion.LicenseInfo``.
            retention_policy: ``AWS::Serverless::LayerVersion.RetentionPolicy``.

        Stability:
            stable
        """
        props: CfnLayerVersionProps = {}

        if compatible_runtimes is not None:
            props["compatibleRuntimes"] = compatible_runtimes

        if content_uri is not None:
            props["contentUri"] = content_uri

        if description is not None:
            props["description"] = description

        if layer_name is not None:
            props["layerName"] = layer_name

        if license_info is not None:
            props["licenseInfo"] = license_info

        if retention_policy is not None:
            props["retentionPolicy"] = retention_policy

        jsii.create(CfnLayerVersion, self, [scope, id, props])

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

    @classproperty
    @jsii.member(jsii_name="REQUIRED_TRANSFORM")
    def REQUIRED_TRANSFORM(cls) -> str:
        """The ``Transform`` a template must use in order to use this resource.

        Stability:
            stable
        """
        return jsii.sget(cls, "REQUIRED_TRANSFORM")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="compatibleRuntimes")
    def compatible_runtimes(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Serverless::LayerVersion.CompatibleRuntimes``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesslayerversion
        Stability:
            stable
        """
        return jsii.get(self, "compatibleRuntimes")

    @compatible_runtimes.setter
    def compatible_runtimes(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "compatibleRuntimes", value)

    @property
    @jsii.member(jsii_name="contentUri")
    def content_uri(self) -> typing.Optional[str]:
        """``AWS::Serverless::LayerVersion.ContentUri``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesslayerversion
        Stability:
            stable
        """
        return jsii.get(self, "contentUri")

    @content_uri.setter
    def content_uri(self, value: typing.Optional[str]):
        return jsii.set(self, "contentUri", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::Serverless::LayerVersion.Description``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesslayerversion
        Stability:
            stable
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="layerName")
    def layer_name(self) -> typing.Optional[str]:
        """``AWS::Serverless::LayerVersion.LayerName``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesslayerversion
        Stability:
            stable
        """
        return jsii.get(self, "layerName")

    @layer_name.setter
    def layer_name(self, value: typing.Optional[str]):
        return jsii.set(self, "layerName", value)

    @property
    @jsii.member(jsii_name="licenseInfo")
    def license_info(self) -> typing.Optional[str]:
        """``AWS::Serverless::LayerVersion.LicenseInfo``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesslayerversion
        Stability:
            stable
        """
        return jsii.get(self, "licenseInfo")

    @license_info.setter
    def license_info(self, value: typing.Optional[str]):
        return jsii.set(self, "licenseInfo", value)

    @property
    @jsii.member(jsii_name="retentionPolicy")
    def retention_policy(self) -> typing.Optional[str]:
        """``AWS::Serverless::LayerVersion.RetentionPolicy``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesslayerversion
        Stability:
            stable
        """
        return jsii.get(self, "retentionPolicy")

    @retention_policy.setter
    def retention_policy(self, value: typing.Optional[str]):
        return jsii.set(self, "retentionPolicy", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnLayerVersionProps", jsii_struct_bases=[])
class CfnLayerVersionProps(jsii.compat.TypedDict, total=False):
    """Properties for defining a ``AWS::Serverless::LayerVersion``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesslayerversion
    Stability:
        stable
    """
    compatibleRuntimes: typing.List[str]
    """``AWS::Serverless::LayerVersion.CompatibleRuntimes``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesslayerversion
    Stability:
        stable
    """

    contentUri: str
    """``AWS::Serverless::LayerVersion.ContentUri``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesslayerversion
    Stability:
        stable
    """

    description: str
    """``AWS::Serverless::LayerVersion.Description``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesslayerversion
    Stability:
        stable
    """

    layerName: str
    """``AWS::Serverless::LayerVersion.LayerName``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesslayerversion
    Stability:
        stable
    """

    licenseInfo: str
    """``AWS::Serverless::LayerVersion.LicenseInfo``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesslayerversion
    Stability:
        stable
    """

    retentionPolicy: str
    """``AWS::Serverless::LayerVersion.RetentionPolicy``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesslayerversion
    Stability:
        stable
    """

class CfnSimpleTable(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-sam.CfnSimpleTable"):
    """A CloudFormation ``AWS::Serverless::SimpleTable``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesssimpletable
    Stability:
        stable
    cloudformationResource:
        AWS::Serverless::SimpleTable
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, primary_key: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["PrimaryKeyProperty"]]]=None, provisioned_throughput: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ProvisionedThroughputProperty"]]]=None, sse_specification: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["SSESpecificationProperty"]]]=None, table_name: typing.Optional[str]=None, tags: typing.Optional[typing.Mapping[str,str]]=None) -> None:
        """Create a new ``AWS::Serverless::SimpleTable``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            primary_key: ``AWS::Serverless::SimpleTable.PrimaryKey``.
            provisioned_throughput: ``AWS::Serverless::SimpleTable.ProvisionedThroughput``.
            sse_specification: ``AWS::Serverless::SimpleTable.SSESpecification``.
            table_name: ``AWS::Serverless::SimpleTable.TableName``.
            tags: ``AWS::Serverless::SimpleTable.Tags``.

        Stability:
            stable
        """
        props: CfnSimpleTableProps = {}

        if primary_key is not None:
            props["primaryKey"] = primary_key

        if provisioned_throughput is not None:
            props["provisionedThroughput"] = provisioned_throughput

        if sse_specification is not None:
            props["sseSpecification"] = sse_specification

        if table_name is not None:
            props["tableName"] = table_name

        if tags is not None:
            props["tags"] = tags

        jsii.create(CfnSimpleTable, self, [scope, id, props])

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

    @classproperty
    @jsii.member(jsii_name="REQUIRED_TRANSFORM")
    def REQUIRED_TRANSFORM(cls) -> str:
        """The ``Transform`` a template must use in order to use this resource.

        Stability:
            stable
        """
        return jsii.sget(cls, "REQUIRED_TRANSFORM")

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
        """``AWS::Serverless::SimpleTable.Tags``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesssimpletable
        Stability:
            stable
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="primaryKey")
    def primary_key(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["PrimaryKeyProperty"]]]:
        """``AWS::Serverless::SimpleTable.PrimaryKey``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#primary-key-object
        Stability:
            stable
        """
        return jsii.get(self, "primaryKey")

    @primary_key.setter
    def primary_key(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["PrimaryKeyProperty"]]]):
        return jsii.set(self, "primaryKey", value)

    @property
    @jsii.member(jsii_name="provisionedThroughput")
    def provisioned_throughput(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ProvisionedThroughputProperty"]]]:
        """``AWS::Serverless::SimpleTable.ProvisionedThroughput``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html
        Stability:
            stable
        """
        return jsii.get(self, "provisionedThroughput")

    @provisioned_throughput.setter
    def provisioned_throughput(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ProvisionedThroughputProperty"]]]):
        return jsii.set(self, "provisionedThroughput", value)

    @property
    @jsii.member(jsii_name="sseSpecification")
    def sse_specification(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["SSESpecificationProperty"]]]:
        """``AWS::Serverless::SimpleTable.SSESpecification``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesssimpletable
        Stability:
            stable
        """
        return jsii.get(self, "sseSpecification")

    @sse_specification.setter
    def sse_specification(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["SSESpecificationProperty"]]]):
        return jsii.set(self, "sseSpecification", value)

    @property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> typing.Optional[str]:
        """``AWS::Serverless::SimpleTable.TableName``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesssimpletable
        Stability:
            stable
        """
        return jsii.get(self, "tableName")

    @table_name.setter
    def table_name(self, value: typing.Optional[str]):
        return jsii.set(self, "tableName", value)

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _PrimaryKeyProperty(jsii.compat.TypedDict, total=False):
        name: str
        """``CfnSimpleTable.PrimaryKeyProperty.Name``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#primary-key-object
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnSimpleTable.PrimaryKeyProperty", jsii_struct_bases=[_PrimaryKeyProperty])
    class PrimaryKeyProperty(_PrimaryKeyProperty):
        """
        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#primary-key-object
        Stability:
            stable
        """
        type: str
        """``CfnSimpleTable.PrimaryKeyProperty.Type``.

        See:
            https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#primary-key-object
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _ProvisionedThroughputProperty(jsii.compat.TypedDict, total=False):
        readCapacityUnits: jsii.Number
        """``CfnSimpleTable.ProvisionedThroughputProperty.ReadCapacityUnits``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnSimpleTable.ProvisionedThroughputProperty", jsii_struct_bases=[_ProvisionedThroughputProperty])
    class ProvisionedThroughputProperty(_ProvisionedThroughputProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html
        Stability:
            stable
        """
        writeCapacityUnits: jsii.Number
        """``CfnSimpleTable.ProvisionedThroughputProperty.WriteCapacityUnits``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnSimpleTable.SSESpecificationProperty", jsii_struct_bases=[])
    class SSESpecificationProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html
        Stability:
            stable
        """
        sseEnabled: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnSimpleTable.SSESpecificationProperty.SSEEnabled``.

        See:
            https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html
        Stability:
            stable
        """


@jsii.data_type(jsii_type="@aws-cdk/aws-sam.CfnSimpleTableProps", jsii_struct_bases=[])
class CfnSimpleTableProps(jsii.compat.TypedDict, total=False):
    """Properties for defining a ``AWS::Serverless::SimpleTable``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesssimpletable
    Stability:
        stable
    """
    primaryKey: typing.Union[aws_cdk.core.IResolvable, "CfnSimpleTable.PrimaryKeyProperty"]
    """``AWS::Serverless::SimpleTable.PrimaryKey``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#primary-key-object
    Stability:
        stable
    """

    provisionedThroughput: typing.Union[aws_cdk.core.IResolvable, "CfnSimpleTable.ProvisionedThroughputProperty"]
    """``AWS::Serverless::SimpleTable.ProvisionedThroughput``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html
    Stability:
        stable
    """

    sseSpecification: typing.Union[aws_cdk.core.IResolvable, "CfnSimpleTable.SSESpecificationProperty"]
    """``AWS::Serverless::SimpleTable.SSESpecification``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesssimpletable
    Stability:
        stable
    """

    tableName: str
    """``AWS::Serverless::SimpleTable.TableName``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesssimpletable
    Stability:
        stable
    """

    tags: typing.Mapping[str,str]
    """``AWS::Serverless::SimpleTable.Tags``.

    See:
        https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesssimpletable
    Stability:
        stable
    """

__all__ = ["CfnApi", "CfnApiProps", "CfnApplication", "CfnApplicationProps", "CfnFunction", "CfnFunctionProps", "CfnLayerVersion", "CfnLayerVersionProps", "CfnSimpleTable", "CfnSimpleTableProps", "__jsii_assembly__"]

publication.publish()
