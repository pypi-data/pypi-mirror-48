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
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-kms", "0.37.0", __name__, "aws-kms@0.37.0.jsii.tgz")
@jsii.data_type(jsii_type="@aws-cdk/aws-kms.AliasAttributes", jsii_struct_bases=[])
class AliasAttributes(jsii.compat.TypedDict):
    """
    Stability:
        stable
    """
    aliasName: str
    """
    Stability:
        stable
    """

    aliasTargetKey: "IKey"
    """
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-kms.AliasProps", jsii_struct_bases=[])
class AliasProps(jsii.compat.TypedDict):
    """Construction properties for a KMS Key Alias object.

    Stability:
        stable
    """
    aliasName: str
    """The name of the alias.

    The name must start with alias followed by a
    forward slash, such as alias/. You can't specify aliases that begin with
    alias/AWS. These aliases are reserved.

    Stability:
        stable
    """

    targetKey: "IKey"
    """The ID of the key for which you are creating the alias.

    Specify the key's
    globally unique identifier or Amazon Resource Name (ARN). You can't
    specify another alias.

    Stability:
        stable
    """

class CfnAlias(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-kms.CfnAlias"):
    """A CloudFormation ``AWS::KMS::Alias``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.html
    Stability:
        stable
    cloudformationResource:
        AWS::KMS::Alias
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, alias_name: str, target_key_id: str) -> None:
        """Create a new ``AWS::KMS::Alias``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            alias_name: ``AWS::KMS::Alias.AliasName``.
            target_key_id: ``AWS::KMS::Alias.TargetKeyId``.

        Stability:
            stable
        """
        props: CfnAliasProps = {"aliasName": alias_name, "targetKeyId": target_key_id}

        jsii.create(CfnAlias, self, [scope, id, props])

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
    @jsii.member(jsii_name="aliasName")
    def alias_name(self) -> str:
        """``AWS::KMS::Alias.AliasName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.html#cfn-kms-alias-aliasname
        Stability:
            stable
        """
        return jsii.get(self, "aliasName")

    @alias_name.setter
    def alias_name(self, value: str):
        return jsii.set(self, "aliasName", value)

    @property
    @jsii.member(jsii_name="targetKeyId")
    def target_key_id(self) -> str:
        """``AWS::KMS::Alias.TargetKeyId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.html#cfn-kms-alias-targetkeyid
        Stability:
            stable
        """
        return jsii.get(self, "targetKeyId")

    @target_key_id.setter
    def target_key_id(self, value: str):
        return jsii.set(self, "targetKeyId", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-kms.CfnAliasProps", jsii_struct_bases=[])
class CfnAliasProps(jsii.compat.TypedDict):
    """Properties for defining a ``AWS::KMS::Alias``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.html
    Stability:
        stable
    """
    aliasName: str
    """``AWS::KMS::Alias.AliasName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.html#cfn-kms-alias-aliasname
    Stability:
        stable
    """

    targetKeyId: str
    """``AWS::KMS::Alias.TargetKeyId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-alias.html#cfn-kms-alias-targetkeyid
    Stability:
        stable
    """

class CfnKey(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-kms.CfnKey"):
    """A CloudFormation ``AWS::KMS::Key``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html
    Stability:
        stable
    cloudformationResource:
        AWS::KMS::Key
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, key_policy: typing.Any, description: typing.Optional[str]=None, enabled: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, enable_key_rotation: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, key_usage: typing.Optional[str]=None, pending_window_in_days: typing.Optional[jsii.Number]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::KMS::Key``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            key_policy: ``AWS::KMS::Key.KeyPolicy``.
            description: ``AWS::KMS::Key.Description``.
            enabled: ``AWS::KMS::Key.Enabled``.
            enable_key_rotation: ``AWS::KMS::Key.EnableKeyRotation``.
            key_usage: ``AWS::KMS::Key.KeyUsage``.
            pending_window_in_days: ``AWS::KMS::Key.PendingWindowInDays``.
            tags: ``AWS::KMS::Key.Tags``.

        Stability:
            stable
        """
        props: CfnKeyProps = {"keyPolicy": key_policy}

        if description is not None:
            props["description"] = description

        if enabled is not None:
            props["enabled"] = enabled

        if enable_key_rotation is not None:
            props["enableKeyRotation"] = enable_key_rotation

        if key_usage is not None:
            props["keyUsage"] = key_usage

        if pending_window_in_days is not None:
            props["pendingWindowInDays"] = pending_window_in_days

        if tags is not None:
            props["tags"] = tags

        jsii.create(CfnKey, self, [scope, id, props])

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
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        """``AWS::KMS::Key.Tags``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-tags
        Stability:
            stable
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="keyPolicy")
    def key_policy(self) -> typing.Any:
        """``AWS::KMS::Key.KeyPolicy``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keypolicy
        Stability:
            stable
        """
        return jsii.get(self, "keyPolicy")

    @key_policy.setter
    def key_policy(self, value: typing.Any):
        return jsii.set(self, "keyPolicy", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::KMS::Key.Description``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-description
        Stability:
            stable
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::KMS::Key.Enabled``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-enabled
        Stability:
            stable
        """
        return jsii.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "enabled", value)

    @property
    @jsii.member(jsii_name="enableKeyRotation")
    def enable_key_rotation(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::KMS::Key.EnableKeyRotation``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-enablekeyrotation
        Stability:
            stable
        """
        return jsii.get(self, "enableKeyRotation")

    @enable_key_rotation.setter
    def enable_key_rotation(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "enableKeyRotation", value)

    @property
    @jsii.member(jsii_name="keyUsage")
    def key_usage(self) -> typing.Optional[str]:
        """``AWS::KMS::Key.KeyUsage``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keyusage
        Stability:
            stable
        """
        return jsii.get(self, "keyUsage")

    @key_usage.setter
    def key_usage(self, value: typing.Optional[str]):
        return jsii.set(self, "keyUsage", value)

    @property
    @jsii.member(jsii_name="pendingWindowInDays")
    def pending_window_in_days(self) -> typing.Optional[jsii.Number]:
        """``AWS::KMS::Key.PendingWindowInDays``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-pendingwindowindays
        Stability:
            stable
        """
        return jsii.get(self, "pendingWindowInDays")

    @pending_window_in_days.setter
    def pending_window_in_days(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "pendingWindowInDays", value)


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnKeyProps(jsii.compat.TypedDict, total=False):
    description: str
    """``AWS::KMS::Key.Description``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-description
    Stability:
        stable
    """
    enabled: typing.Union[bool, aws_cdk.core.IResolvable]
    """``AWS::KMS::Key.Enabled``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-enabled
    Stability:
        stable
    """
    enableKeyRotation: typing.Union[bool, aws_cdk.core.IResolvable]
    """``AWS::KMS::Key.EnableKeyRotation``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-enablekeyrotation
    Stability:
        stable
    """
    keyUsage: str
    """``AWS::KMS::Key.KeyUsage``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keyusage
    Stability:
        stable
    """
    pendingWindowInDays: jsii.Number
    """``AWS::KMS::Key.PendingWindowInDays``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-pendingwindowindays
    Stability:
        stable
    """
    tags: typing.List[aws_cdk.core.CfnTag]
    """``AWS::KMS::Key.Tags``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-tags
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-kms.CfnKeyProps", jsii_struct_bases=[_CfnKeyProps])
class CfnKeyProps(_CfnKeyProps):
    """Properties for defining a ``AWS::KMS::Key``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html
    Stability:
        stable
    """
    keyPolicy: typing.Any
    """``AWS::KMS::Key.KeyPolicy``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kms-key.html#cfn-kms-key-keypolicy
    Stability:
        stable
    """

@jsii.interface(jsii_type="@aws-cdk/aws-kms.IAlias")
class IAlias(aws_cdk.core.IResource, jsii.compat.Protocol):
    """A KMS Key alias.

    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IAliasProxy

    @property
    @jsii.member(jsii_name="aliasName")
    def alias_name(self) -> str:
        """The name of the alias.

        Stability:
            stable
        attribute:
            true
        """
        ...

    @property
    @jsii.member(jsii_name="aliasTargetKey")
    def alias_target_key(self) -> "IKey":
        """The Key to which the Alias refers.

        Stability:
            stable
        attribute:
            true
        """
        ...


class _IAliasProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """A KMS Key alias.

    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-kms.IAlias"
    @property
    @jsii.member(jsii_name="aliasName")
    def alias_name(self) -> str:
        """The name of the alias.

        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "aliasName")

    @property
    @jsii.member(jsii_name="aliasTargetKey")
    def alias_target_key(self) -> "IKey":
        """The Key to which the Alias refers.

        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "aliasTargetKey")


@jsii.implements(IAlias)
class Alias(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-kms.Alias"):
    """Defines a display name for a customer master key (CMK) in AWS Key Management Service (AWS KMS).

    Using an alias to refer to a key can help you simplify key
    management. For example, when rotating keys, you can just update the alias
    mapping instead of tracking and changing key IDs. For more information, see
    Working with Aliases in the AWS Key Management Service Developer Guide.

    You can also add an alias for a key by calling ``key.addAlias(alias)``.

    Stability:
        stable
    resource:
        AWS::KMS::Alias
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, alias_name: str, target_key: "IKey") -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            alias_name: The name of the alias. The name must start with alias followed by a forward slash, such as alias/. You can't specify aliases that begin with alias/AWS. These aliases are reserved.
            target_key: The ID of the key for which you are creating the alias. Specify the key's globally unique identifier or Amazon Resource Name (ARN). You can't specify another alias.

        Stability:
            stable
        """
        props: AliasProps = {"aliasName": alias_name, "targetKey": target_key}

        jsii.create(Alias, self, [scope, id, props])

    @jsii.member(jsii_name="fromAliasAttributes")
    @classmethod
    def from_alias_attributes(cls, scope: aws_cdk.core.Construct, id: str, *, alias_name: str, alias_target_key: "IKey") -> "IAlias":
        """
        Arguments:
            scope: -
            id: -
            attrs: -
            alias_name: 
            alias_target_key: 

        Stability:
            stable
        """
        attrs: AliasAttributes = {"aliasName": alias_name, "aliasTargetKey": alias_target_key}

        return jsii.sinvoke(cls, "fromAliasAttributes", [scope, id, attrs])

    @property
    @jsii.member(jsii_name="aliasName")
    def alias_name(self) -> str:
        """The name of the alias.

        Stability:
            stable
        """
        return jsii.get(self, "aliasName")

    @property
    @jsii.member(jsii_name="aliasTargetKey")
    def alias_target_key(self) -> "IKey":
        """The Key to which the Alias refers.

        Stability:
            stable
        """
        return jsii.get(self, "aliasTargetKey")


@jsii.interface(jsii_type="@aws-cdk/aws-kms.IKey")
class IKey(aws_cdk.core.IResource, jsii.compat.Protocol):
    """A KMS Key, either managed by this CDK app, or imported.

    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IKeyProxy

    @property
    @jsii.member(jsii_name="keyArn")
    def key_arn(self) -> str:
        """The ARN of the key.

        Stability:
            stable
        attribute:
            true
        """
        ...

    @jsii.member(jsii_name="addAlias")
    def add_alias(self, alias: str) -> "Alias":
        """Defines a new alias for the key.

        Arguments:
            alias: -

        Stability:
            stable
        """
        ...

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(self, statement: aws_cdk.aws_iam.PolicyStatement, allow_no_op: typing.Optional[bool]=None) -> None:
        """Adds a statement to the KMS key resource policy.

        Arguments:
            statement: The policy statement to add.
            allow_no_op: If this is set to ``false`` and there is no policy defined (i.e. external key), the operation will fail. Otherwise, it will no-op.

        Stability:
            stable
        """
        ...

    @jsii.member(jsii_name="grant")
    def grant(self, grantee: aws_cdk.aws_iam.IGrantable, *actions: str) -> aws_cdk.aws_iam.Grant:
        """Grant the indicated permissions on this key to the given principal.

        Arguments:
            grantee: -
            actions: -

        Stability:
            stable
        """
        ...

    @jsii.member(jsii_name="grantDecrypt")
    def grant_decrypt(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant decryption permisisons using this key to the given principal.

        Arguments:
            grantee: -

        Stability:
            stable
        """
        ...

    @jsii.member(jsii_name="grantEncrypt")
    def grant_encrypt(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant encryption permisisons using this key to the given principal.

        Arguments:
            grantee: -

        Stability:
            stable
        """
        ...

    @jsii.member(jsii_name="grantEncryptDecrypt")
    def grant_encrypt_decrypt(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant encryption and decryption permisisons using this key to the given principal.

        Arguments:
            grantee: -

        Stability:
            stable
        """
        ...


class _IKeyProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """A KMS Key, either managed by this CDK app, or imported.

    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-kms.IKey"
    @property
    @jsii.member(jsii_name="keyArn")
    def key_arn(self) -> str:
        """The ARN of the key.

        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "keyArn")

    @jsii.member(jsii_name="addAlias")
    def add_alias(self, alias: str) -> "Alias":
        """Defines a new alias for the key.

        Arguments:
            alias: -

        Stability:
            stable
        """
        return jsii.invoke(self, "addAlias", [alias])

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(self, statement: aws_cdk.aws_iam.PolicyStatement, allow_no_op: typing.Optional[bool]=None) -> None:
        """Adds a statement to the KMS key resource policy.

        Arguments:
            statement: The policy statement to add.
            allow_no_op: If this is set to ``false`` and there is no policy defined (i.e. external key), the operation will fail. Otherwise, it will no-op.

        Stability:
            stable
        """
        return jsii.invoke(self, "addToResourcePolicy", [statement, allow_no_op])

    @jsii.member(jsii_name="grant")
    def grant(self, grantee: aws_cdk.aws_iam.IGrantable, *actions: str) -> aws_cdk.aws_iam.Grant:
        """Grant the indicated permissions on this key to the given principal.

        Arguments:
            grantee: -
            actions: -

        Stability:
            stable
        """
        return jsii.invoke(self, "grant", [grantee, *actions])

    @jsii.member(jsii_name="grantDecrypt")
    def grant_decrypt(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant decryption permisisons using this key to the given principal.

        Arguments:
            grantee: -

        Stability:
            stable
        """
        return jsii.invoke(self, "grantDecrypt", [grantee])

    @jsii.member(jsii_name="grantEncrypt")
    def grant_encrypt(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant encryption permisisons using this key to the given principal.

        Arguments:
            grantee: -

        Stability:
            stable
        """
        return jsii.invoke(self, "grantEncrypt", [grantee])

    @jsii.member(jsii_name="grantEncryptDecrypt")
    def grant_encrypt_decrypt(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant encryption and decryption permisisons using this key to the given principal.

        Arguments:
            grantee: -

        Stability:
            stable
        """
        return jsii.invoke(self, "grantEncryptDecrypt", [grantee])


@jsii.implements(IKey)
class Key(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-kms.Key"):
    """Defines a KMS key.

    Stability:
        stable
    resource:
        AWS::KMS::Key
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, description: typing.Optional[str]=None, enabled: typing.Optional[bool]=None, enable_key_rotation: typing.Optional[bool]=None, policy: typing.Optional[aws_cdk.aws_iam.PolicyDocument]=None, removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            description: A description of the key. Use a description that helps your users decide whether the key is appropriate for a particular task. Default: - No description.
            enabled: Indicates whether the key is available for use. Default: - Key is enabled.
            enable_key_rotation: Indicates whether AWS KMS rotates the key. Default: false
            policy: Custom policy document to attach to the KMS key. Default: - A policy document with permissions for the account root to administer the key will be created.
            removal_policy: Whether the encryption key should be retained when it is removed from the Stack. This is useful when one wants to retain access to data that was encrypted with a key that is being retired. Default: RemovalPolicy.Retain

        Stability:
            stable
        """
        props: KeyProps = {}

        if description is not None:
            props["description"] = description

        if enabled is not None:
            props["enabled"] = enabled

        if enable_key_rotation is not None:
            props["enableKeyRotation"] = enable_key_rotation

        if policy is not None:
            props["policy"] = policy

        if removal_policy is not None:
            props["removalPolicy"] = removal_policy

        jsii.create(Key, self, [scope, id, props])

    @jsii.member(jsii_name="fromKeyArn")
    @classmethod
    def from_key_arn(cls, scope: aws_cdk.core.Construct, id: str, key_arn: str) -> "IKey":
        """Import an externally defined KMS Key using its ARN.

        Arguments:
            scope: the construct that will "own" the imported key.
            id: the id of the imported key in the construct tree.
            key_arn: the ARN of an existing KMS key.

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "fromKeyArn", [scope, id, key_arn])

    @jsii.member(jsii_name="addAlias")
    def add_alias(self, alias: str) -> "Alias":
        """Defines a new alias for the key.

        Arguments:
            alias: -

        Stability:
            stable
        """
        return jsii.invoke(self, "addAlias", [alias])

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(self, statement: aws_cdk.aws_iam.PolicyStatement, allow_no_op: typing.Optional[bool]=None) -> None:
        """Adds a statement to the KMS key resource policy.

        Arguments:
            statement: The policy statement to add.
            allow_no_op: If this is set to ``false`` and there is no policy defined (i.e. external key), the operation will fail. Otherwise, it will no-op.

        Stability:
            stable
        """
        return jsii.invoke(self, "addToResourcePolicy", [statement, allow_no_op])

    @jsii.member(jsii_name="grant")
    def grant(self, grantee: aws_cdk.aws_iam.IGrantable, *actions: str) -> aws_cdk.aws_iam.Grant:
        """Grant the indicated permissions on this key to the given principal.

        This modifies both the principal's policy as well as the resource policy,
        since the default CloudFormation setup for KMS keys is that the policy
        must not be empty and so default grants won't work.

        Arguments:
            grantee: -
            actions: -

        Stability:
            stable
        """
        return jsii.invoke(self, "grant", [grantee, *actions])

    @jsii.member(jsii_name="grantDecrypt")
    def grant_decrypt(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant decryption permisisons using this key to the given principal.

        Arguments:
            grantee: -

        Stability:
            stable
        """
        return jsii.invoke(self, "grantDecrypt", [grantee])

    @jsii.member(jsii_name="grantEncrypt")
    def grant_encrypt(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant encryption permisisons using this key to the given principal.

        Arguments:
            grantee: -

        Stability:
            stable
        """
        return jsii.invoke(self, "grantEncrypt", [grantee])

    @jsii.member(jsii_name="grantEncryptDecrypt")
    def grant_encrypt_decrypt(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant encryption and decryption permisisons using this key to the given principal.

        Arguments:
            grantee: -

        Stability:
            stable
        """
        return jsii.invoke(self, "grantEncryptDecrypt", [grantee])

    @property
    @jsii.member(jsii_name="keyArn")
    def key_arn(self) -> str:
        """The ARN of the key.

        Stability:
            stable
        """
        return jsii.get(self, "keyArn")

    @property
    @jsii.member(jsii_name="policy")
    def _policy(self) -> typing.Optional[aws_cdk.aws_iam.PolicyDocument]:
        """Optional policy document that represents the resource policy of this key.

        If specified, addToResourcePolicy can be used to edit this policy.
        Otherwise this method will no-op.

        Stability:
            stable
        """
        return jsii.get(self, "policy")


@jsii.data_type(jsii_type="@aws-cdk/aws-kms.KeyProps", jsii_struct_bases=[])
class KeyProps(jsii.compat.TypedDict, total=False):
    """Construction properties for a KMS Key object.

    Stability:
        stable
    """
    description: str
    """A description of the key.

    Use a description that helps your users decide
    whether the key is appropriate for a particular task.

    Default:
        - No description.

    Stability:
        stable
    """

    enabled: bool
    """Indicates whether the key is available for use.

    Default:
        - Key is enabled.

    Stability:
        stable
    """

    enableKeyRotation: bool
    """Indicates whether AWS KMS rotates the key.

    Default:
        false

    Stability:
        stable
    """

    policy: aws_cdk.aws_iam.PolicyDocument
    """Custom policy document to attach to the KMS key.

    Default:
        - A policy document with permissions for the account root to
          administer the key will be created.

    Stability:
        stable
    """

    removalPolicy: aws_cdk.core.RemovalPolicy
    """Whether the encryption key should be retained when it is removed from the Stack.

    This is useful when one wants to
    retain access to data that was encrypted with a key that is being retired.

    Default:
        RemovalPolicy.Retain

    Stability:
        stable
    """

class ViaServicePrincipal(aws_cdk.aws_iam.PrincipalBase, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-kms.ViaServicePrincipal"):
    """A principal to allow access to a key if it's being used through another AWS service.

    Stability:
        stable
    """
    def __init__(self, service_name: str, base_principal: typing.Optional[aws_cdk.aws_iam.IPrincipal]=None) -> None:
        """
        Arguments:
            service_name: -
            base_principal: -

        Stability:
            stable
        """
        jsii.create(ViaServicePrincipal, self, [service_name, base_principal])

    @property
    @jsii.member(jsii_name="policyFragment")
    def policy_fragment(self) -> aws_cdk.aws_iam.PrincipalPolicyFragment:
        """Return the policy fragment that identifies this principal in a Policy.

        Stability:
            stable
        """
        return jsii.get(self, "policyFragment")


__all__ = ["Alias", "AliasAttributes", "AliasProps", "CfnAlias", "CfnAliasProps", "CfnKey", "CfnKeyProps", "IAlias", "IKey", "Key", "KeyProps", "ViaServicePrincipal", "__jsii_assembly__"]

publication.publish()
