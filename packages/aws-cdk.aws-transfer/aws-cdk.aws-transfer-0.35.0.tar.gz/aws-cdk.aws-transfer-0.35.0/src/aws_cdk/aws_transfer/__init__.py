import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.cdk
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-transfer", "0.35.0", __name__, "aws-transfer@0.35.0.jsii.tgz")
class CfnServer(aws_cdk.cdk.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-transfer.CfnServer"):
    """A CloudFormation ``AWS::Transfer::Server``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html
    Stability:
        experimental
    cloudformationResource:
        AWS::Transfer::Server
    """
    def __init__(self, scope: aws_cdk.cdk.Construct, id: str, *, endpoint_details: typing.Optional[typing.Union[typing.Optional["EndpointDetailsProperty"], typing.Optional[aws_cdk.cdk.IResolvable]]]=None, endpoint_type: typing.Optional[str]=None, identity_provider_details: typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional["IdentityProviderDetailsProperty"]]]=None, identity_provider_type: typing.Optional[str]=None, logging_role: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.cdk.CfnTag]]=None) -> None:
        """Create a new ``AWS::Transfer::Server``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            endpointDetails: ``AWS::Transfer::Server.EndpointDetails``.
            endpointType: ``AWS::Transfer::Server.EndpointType``.
            identityProviderDetails: ``AWS::Transfer::Server.IdentityProviderDetails``.
            identityProviderType: ``AWS::Transfer::Server.IdentityProviderType``.
            loggingRole: ``AWS::Transfer::Server.LoggingRole``.
            tags: ``AWS::Transfer::Server.Tags``.

        Stability:
            experimental
        """
        props: CfnServerProps = {}

        if endpoint_details is not None:
            props["endpointDetails"] = endpoint_details

        if endpoint_type is not None:
            props["endpointType"] = endpoint_type

        if identity_provider_details is not None:
            props["identityProviderDetails"] = identity_provider_details

        if identity_provider_type is not None:
            props["identityProviderType"] = identity_provider_type

        if logging_role is not None:
            props["loggingRole"] = logging_role

        if tags is not None:
            props["tags"] = tags

        jsii.create(CfnServer, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrServerId")
    def attr_server_id(self) -> str:
        """
        Stability:
            experimental
        cloudformationAttribute:
            ServerId
        """
        return jsii.get(self, "attrServerId")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.cdk.TagManager:
        """``AWS::Transfer::Server.Tags``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-tags
        Stability:
            experimental
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="endpointDetails")
    def endpoint_details(self) -> typing.Optional[typing.Union[typing.Optional["EndpointDetailsProperty"], typing.Optional[aws_cdk.cdk.IResolvable]]]:
        """``AWS::Transfer::Server.EndpointDetails``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-endpointdetails
        Stability:
            experimental
        """
        return jsii.get(self, "endpointDetails")

    @endpoint_details.setter
    def endpoint_details(self, value: typing.Optional[typing.Union[typing.Optional["EndpointDetailsProperty"], typing.Optional[aws_cdk.cdk.IResolvable]]]):
        return jsii.set(self, "endpointDetails", value)

    @property
    @jsii.member(jsii_name="endpointType")
    def endpoint_type(self) -> typing.Optional[str]:
        """``AWS::Transfer::Server.EndpointType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-endpointtype
        Stability:
            experimental
        """
        return jsii.get(self, "endpointType")

    @endpoint_type.setter
    def endpoint_type(self, value: typing.Optional[str]):
        return jsii.set(self, "endpointType", value)

    @property
    @jsii.member(jsii_name="identityProviderDetails")
    def identity_provider_details(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional["IdentityProviderDetailsProperty"]]]:
        """``AWS::Transfer::Server.IdentityProviderDetails``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-identityproviderdetails
        Stability:
            experimental
        """
        return jsii.get(self, "identityProviderDetails")

    @identity_provider_details.setter
    def identity_provider_details(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional["IdentityProviderDetailsProperty"]]]):
        return jsii.set(self, "identityProviderDetails", value)

    @property
    @jsii.member(jsii_name="identityProviderType")
    def identity_provider_type(self) -> typing.Optional[str]:
        """``AWS::Transfer::Server.IdentityProviderType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-identityprovidertype
        Stability:
            experimental
        """
        return jsii.get(self, "identityProviderType")

    @identity_provider_type.setter
    def identity_provider_type(self, value: typing.Optional[str]):
        return jsii.set(self, "identityProviderType", value)

    @property
    @jsii.member(jsii_name="loggingRole")
    def logging_role(self) -> typing.Optional[str]:
        """``AWS::Transfer::Server.LoggingRole``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-loggingrole
        Stability:
            experimental
        """
        return jsii.get(self, "loggingRole")

    @logging_role.setter
    def logging_role(self, value: typing.Optional[str]):
        return jsii.set(self, "loggingRole", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-transfer.CfnServer.EndpointDetailsProperty", jsii_struct_bases=[])
    class EndpointDetailsProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html
        Stability:
            experimental
        """
        vpcEndpointId: str
        """``CfnServer.EndpointDetailsProperty.VpcEndpointId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-vpcendpointid
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-transfer.CfnServer.IdentityProviderDetailsProperty", jsii_struct_bases=[])
    class IdentityProviderDetailsProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html
        Stability:
            experimental
        """
        invocationRole: str
        """``CfnServer.IdentityProviderDetailsProperty.InvocationRole``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html#cfn-transfer-server-identityproviderdetails-invocationrole
        Stability:
            experimental
        """

        url: str
        """``CfnServer.IdentityProviderDetailsProperty.Url``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html#cfn-transfer-server-identityproviderdetails-url
        Stability:
            experimental
        """


@jsii.data_type(jsii_type="@aws-cdk/aws-transfer.CfnServerProps", jsii_struct_bases=[])
class CfnServerProps(jsii.compat.TypedDict, total=False):
    """Properties for defining a ``AWS::Transfer::Server``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html
    Stability:
        experimental
    """
    endpointDetails: typing.Union["CfnServer.EndpointDetailsProperty", aws_cdk.cdk.IResolvable]
    """``AWS::Transfer::Server.EndpointDetails``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-endpointdetails
    Stability:
        experimental
    """

    endpointType: str
    """``AWS::Transfer::Server.EndpointType``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-endpointtype
    Stability:
        experimental
    """

    identityProviderDetails: typing.Union[aws_cdk.cdk.IResolvable, "CfnServer.IdentityProviderDetailsProperty"]
    """``AWS::Transfer::Server.IdentityProviderDetails``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-identityproviderdetails
    Stability:
        experimental
    """

    identityProviderType: str
    """``AWS::Transfer::Server.IdentityProviderType``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-identityprovidertype
    Stability:
        experimental
    """

    loggingRole: str
    """``AWS::Transfer::Server.LoggingRole``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-loggingrole
    Stability:
        experimental
    """

    tags: typing.List[aws_cdk.cdk.CfnTag]
    """``AWS::Transfer::Server.Tags``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-tags
    Stability:
        experimental
    """

class CfnUser(aws_cdk.cdk.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-transfer.CfnUser"):
    """A CloudFormation ``AWS::Transfer::User``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html
    Stability:
        experimental
    cloudformationResource:
        AWS::Transfer::User
    """
    def __init__(self, scope: aws_cdk.cdk.Construct, id: str, *, role: str, server_id: str, user_name: str, home_directory: typing.Optional[str]=None, policy: typing.Optional[str]=None, ssh_public_keys: typing.Optional[typing.List[str]]=None, tags: typing.Optional[typing.List[aws_cdk.cdk.CfnTag]]=None) -> None:
        """Create a new ``AWS::Transfer::User``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            role: ``AWS::Transfer::User.Role``.
            serverId: ``AWS::Transfer::User.ServerId``.
            userName: ``AWS::Transfer::User.UserName``.
            homeDirectory: ``AWS::Transfer::User.HomeDirectory``.
            policy: ``AWS::Transfer::User.Policy``.
            sshPublicKeys: ``AWS::Transfer::User.SshPublicKeys``.
            tags: ``AWS::Transfer::User.Tags``.

        Stability:
            experimental
        """
        props: CfnUserProps = {"role": role, "serverId": server_id, "userName": user_name}

        if home_directory is not None:
            props["homeDirectory"] = home_directory

        if policy is not None:
            props["policy"] = policy

        if ssh_public_keys is not None:
            props["sshPublicKeys"] = ssh_public_keys

        if tags is not None:
            props["tags"] = tags

        jsii.create(CfnUser, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrServerId")
    def attr_server_id(self) -> str:
        """
        Stability:
            experimental
        cloudformationAttribute:
            ServerId
        """
        return jsii.get(self, "attrServerId")

    @property
    @jsii.member(jsii_name="attrUserName")
    def attr_user_name(self) -> str:
        """
        Stability:
            experimental
        cloudformationAttribute:
            UserName
        """
        return jsii.get(self, "attrUserName")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.cdk.TagManager:
        """``AWS::Transfer::User.Tags``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-tags
        Stability:
            experimental
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="role")
    def role(self) -> str:
        """``AWS::Transfer::User.Role``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-role
        Stability:
            experimental
        """
        return jsii.get(self, "role")

    @role.setter
    def role(self, value: str):
        return jsii.set(self, "role", value)

    @property
    @jsii.member(jsii_name="serverId")
    def server_id(self) -> str:
        """``AWS::Transfer::User.ServerId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-serverid
        Stability:
            experimental
        """
        return jsii.get(self, "serverId")

    @server_id.setter
    def server_id(self, value: str):
        return jsii.set(self, "serverId", value)

    @property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> str:
        """``AWS::Transfer::User.UserName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-username
        Stability:
            experimental
        """
        return jsii.get(self, "userName")

    @user_name.setter
    def user_name(self, value: str):
        return jsii.set(self, "userName", value)

    @property
    @jsii.member(jsii_name="homeDirectory")
    def home_directory(self) -> typing.Optional[str]:
        """``AWS::Transfer::User.HomeDirectory``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectory
        Stability:
            experimental
        """
        return jsii.get(self, "homeDirectory")

    @home_directory.setter
    def home_directory(self, value: typing.Optional[str]):
        return jsii.set(self, "homeDirectory", value)

    @property
    @jsii.member(jsii_name="policy")
    def policy(self) -> typing.Optional[str]:
        """``AWS::Transfer::User.Policy``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-policy
        Stability:
            experimental
        """
        return jsii.get(self, "policy")

    @policy.setter
    def policy(self, value: typing.Optional[str]):
        return jsii.set(self, "policy", value)

    @property
    @jsii.member(jsii_name="sshPublicKeys")
    def ssh_public_keys(self) -> typing.Optional[typing.List[str]]:
        """``AWS::Transfer::User.SshPublicKeys``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-sshpublickeys
        Stability:
            experimental
        """
        return jsii.get(self, "sshPublicKeys")

    @ssh_public_keys.setter
    def ssh_public_keys(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "sshPublicKeys", value)


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnUserProps(jsii.compat.TypedDict, total=False):
    homeDirectory: str
    """``AWS::Transfer::User.HomeDirectory``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectory
    Stability:
        experimental
    """
    policy: str
    """``AWS::Transfer::User.Policy``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-policy
    Stability:
        experimental
    """
    sshPublicKeys: typing.List[str]
    """``AWS::Transfer::User.SshPublicKeys``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-sshpublickeys
    Stability:
        experimental
    """
    tags: typing.List[aws_cdk.cdk.CfnTag]
    """``AWS::Transfer::User.Tags``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-tags
    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-transfer.CfnUserProps", jsii_struct_bases=[_CfnUserProps])
class CfnUserProps(_CfnUserProps):
    """Properties for defining a ``AWS::Transfer::User``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html
    Stability:
        experimental
    """
    role: str
    """``AWS::Transfer::User.Role``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-role
    Stability:
        experimental
    """

    serverId: str
    """``AWS::Transfer::User.ServerId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-serverid
    Stability:
        experimental
    """

    userName: str
    """``AWS::Transfer::User.UserName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-username
    Stability:
        experimental
    """

__all__ = ["CfnServer", "CfnServerProps", "CfnUser", "CfnUserProps", "__jsii_assembly__"]

publication.publish()
