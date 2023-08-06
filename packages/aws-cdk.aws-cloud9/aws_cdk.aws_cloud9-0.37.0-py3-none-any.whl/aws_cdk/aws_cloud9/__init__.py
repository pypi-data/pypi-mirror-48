import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-cloud9", "0.37.0", __name__, "aws-cloud9@0.37.0.jsii.tgz")
class CfnEnvironmentEC2(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-cloud9.CfnEnvironmentEC2"):
    """A CloudFormation ``AWS::Cloud9::EnvironmentEC2``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html
    Stability:
        stable
    cloudformationResource:
        AWS::Cloud9::EnvironmentEC2
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, instance_type: str, automatic_stop_time_minutes: typing.Optional[jsii.Number]=None, description: typing.Optional[str]=None, name: typing.Optional[str]=None, owner_arn: typing.Optional[str]=None, repositories: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union["RepositoryProperty", aws_cdk.core.IResolvable]]]]]=None, subnet_id: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::Cloud9::EnvironmentEC2``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            instance_type: ``AWS::Cloud9::EnvironmentEC2.InstanceType``.
            automatic_stop_time_minutes: ``AWS::Cloud9::EnvironmentEC2.AutomaticStopTimeMinutes``.
            description: ``AWS::Cloud9::EnvironmentEC2.Description``.
            name: ``AWS::Cloud9::EnvironmentEC2.Name``.
            owner_arn: ``AWS::Cloud9::EnvironmentEC2.OwnerArn``.
            repositories: ``AWS::Cloud9::EnvironmentEC2.Repositories``.
            subnet_id: ``AWS::Cloud9::EnvironmentEC2.SubnetId``.

        Stability:
            stable
        """
        props: CfnEnvironmentEC2Props = {"instanceType": instance_type}

        if automatic_stop_time_minutes is not None:
            props["automaticStopTimeMinutes"] = automatic_stop_time_minutes

        if description is not None:
            props["description"] = description

        if name is not None:
            props["name"] = name

        if owner_arn is not None:
            props["ownerArn"] = owner_arn

        if repositories is not None:
            props["repositories"] = repositories

        if subnet_id is not None:
            props["subnetId"] = subnet_id

        jsii.create(CfnEnvironmentEC2, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> str:
        """
        Stability:
            stable
        cloudformationAttribute:
            Name
        """
        return jsii.get(self, "attrName")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> str:
        """``AWS::Cloud9::EnvironmentEC2.InstanceType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-instancetype
        Stability:
            stable
        """
        return jsii.get(self, "instanceType")

    @instance_type.setter
    def instance_type(self, value: str):
        return jsii.set(self, "instanceType", value)

    @property
    @jsii.member(jsii_name="automaticStopTimeMinutes")
    def automatic_stop_time_minutes(self) -> typing.Optional[jsii.Number]:
        """``AWS::Cloud9::EnvironmentEC2.AutomaticStopTimeMinutes``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-automaticstoptimeminutes
        Stability:
            stable
        """
        return jsii.get(self, "automaticStopTimeMinutes")

    @automatic_stop_time_minutes.setter
    def automatic_stop_time_minutes(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "automaticStopTimeMinutes", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::Cloud9::EnvironmentEC2.Description``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-description
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
        """``AWS::Cloud9::EnvironmentEC2.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-name
        Stability:
            stable
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="ownerArn")
    def owner_arn(self) -> typing.Optional[str]:
        """``AWS::Cloud9::EnvironmentEC2.OwnerArn``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-ownerarn
        Stability:
            stable
        """
        return jsii.get(self, "ownerArn")

    @owner_arn.setter
    def owner_arn(self, value: typing.Optional[str]):
        return jsii.set(self, "ownerArn", value)

    @property
    @jsii.member(jsii_name="repositories")
    def repositories(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union["RepositoryProperty", aws_cdk.core.IResolvable]]]]]:
        """``AWS::Cloud9::EnvironmentEC2.Repositories``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-repositories
        Stability:
            stable
        """
        return jsii.get(self, "repositories")

    @repositories.setter
    def repositories(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union["RepositoryProperty", aws_cdk.core.IResolvable]]]]]):
        return jsii.set(self, "repositories", value)

    @property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> typing.Optional[str]:
        """``AWS::Cloud9::EnvironmentEC2.SubnetId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-subnetid
        Stability:
            stable
        """
        return jsii.get(self, "subnetId")

    @subnet_id.setter
    def subnet_id(self, value: typing.Optional[str]):
        return jsii.set(self, "subnetId", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-cloud9.CfnEnvironmentEC2.RepositoryProperty", jsii_struct_bases=[])
    class RepositoryProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloud9-environmentec2-repository.html
        Stability:
            stable
        """
        pathComponent: str
        """``CfnEnvironmentEC2.RepositoryProperty.PathComponent``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloud9-environmentec2-repository.html#cfn-cloud9-environmentec2-repository-pathcomponent
        Stability:
            stable
        """

        repositoryUrl: str
        """``CfnEnvironmentEC2.RepositoryProperty.RepositoryUrl``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloud9-environmentec2-repository.html#cfn-cloud9-environmentec2-repository-repositoryurl
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnEnvironmentEC2Props(jsii.compat.TypedDict, total=False):
    automaticStopTimeMinutes: jsii.Number
    """``AWS::Cloud9::EnvironmentEC2.AutomaticStopTimeMinutes``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-automaticstoptimeminutes
    Stability:
        stable
    """
    description: str
    """``AWS::Cloud9::EnvironmentEC2.Description``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-description
    Stability:
        stable
    """
    name: str
    """``AWS::Cloud9::EnvironmentEC2.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-name
    Stability:
        stable
    """
    ownerArn: str
    """``AWS::Cloud9::EnvironmentEC2.OwnerArn``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-ownerarn
    Stability:
        stable
    """
    repositories: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnEnvironmentEC2.RepositoryProperty", aws_cdk.core.IResolvable]]]
    """``AWS::Cloud9::EnvironmentEC2.Repositories``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-repositories
    Stability:
        stable
    """
    subnetId: str
    """``AWS::Cloud9::EnvironmentEC2.SubnetId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-subnetid
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-cloud9.CfnEnvironmentEC2Props", jsii_struct_bases=[_CfnEnvironmentEC2Props])
class CfnEnvironmentEC2Props(_CfnEnvironmentEC2Props):
    """Properties for defining a ``AWS::Cloud9::EnvironmentEC2``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html
    Stability:
        stable
    """
    instanceType: str
    """``AWS::Cloud9::EnvironmentEC2.InstanceType``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloud9-environmentec2.html#cfn-cloud9-environmentec2-instancetype
    Stability:
        stable
    """

__all__ = ["CfnEnvironmentEC2", "CfnEnvironmentEC2Props", "__jsii_assembly__"]

publication.publish()
