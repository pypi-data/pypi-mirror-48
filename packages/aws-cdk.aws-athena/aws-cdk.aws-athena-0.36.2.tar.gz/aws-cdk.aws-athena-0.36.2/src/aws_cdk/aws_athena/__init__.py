import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-athena", "0.36.2", __name__, "aws-athena@0.36.2.jsii.tgz")
class CfnNamedQuery(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-athena.CfnNamedQuery"):
    """A CloudFormation ``AWS::Athena::NamedQuery``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html
    Stability:
        stable
    cloudformationResource:
        AWS::Athena::NamedQuery
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, database: str, query_string: str, description: typing.Optional[str]=None, name: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::Athena::NamedQuery``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            database: ``AWS::Athena::NamedQuery.Database``.
            query_string: ``AWS::Athena::NamedQuery.QueryString``.
            description: ``AWS::Athena::NamedQuery.Description``.
            name: ``AWS::Athena::NamedQuery.Name``.

        Stability:
            stable
        """
        props: CfnNamedQueryProps = {"database": database, "queryString": query_string}

        if description is not None:
            props["description"] = description

        if name is not None:
            props["name"] = name

        jsii.create(CfnNamedQuery, self, [scope, id, props])

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
    @jsii.member(jsii_name="database")
    def database(self) -> str:
        """``AWS::Athena::NamedQuery.Database``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-database
        Stability:
            stable
        """
        return jsii.get(self, "database")

    @database.setter
    def database(self, value: str):
        return jsii.set(self, "database", value)

    @property
    @jsii.member(jsii_name="queryString")
    def query_string(self) -> str:
        """``AWS::Athena::NamedQuery.QueryString``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-querystring
        Stability:
            stable
        """
        return jsii.get(self, "queryString")

    @query_string.setter
    def query_string(self, value: str):
        return jsii.set(self, "queryString", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::Athena::NamedQuery.Description``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-description
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
        """``AWS::Athena::NamedQuery.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-name
        Stability:
            stable
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        return jsii.set(self, "name", value)


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnNamedQueryProps(jsii.compat.TypedDict, total=False):
    description: str
    """``AWS::Athena::NamedQuery.Description``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-description
    Stability:
        stable
    """
    name: str
    """``AWS::Athena::NamedQuery.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-name
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-athena.CfnNamedQueryProps", jsii_struct_bases=[_CfnNamedQueryProps])
class CfnNamedQueryProps(_CfnNamedQueryProps):
    """Properties for defining a ``AWS::Athena::NamedQuery``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html
    Stability:
        stable
    """
    database: str
    """``AWS::Athena::NamedQuery.Database``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-database
    Stability:
        stable
    """

    queryString: str
    """``AWS::Athena::NamedQuery.QueryString``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html#cfn-athena-namedquery-querystring
    Stability:
        stable
    """

__all__ = ["CfnNamedQuery", "CfnNamedQueryProps", "__jsii_assembly__"]

publication.publish()
