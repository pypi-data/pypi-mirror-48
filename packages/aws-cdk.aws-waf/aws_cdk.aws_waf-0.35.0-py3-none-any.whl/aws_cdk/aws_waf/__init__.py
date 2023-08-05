import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.cdk
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-waf", "0.35.0", __name__, "aws-waf@0.35.0.jsii.tgz")
class CfnByteMatchSet(aws_cdk.cdk.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-waf.CfnByteMatchSet"):
    """A CloudFormation ``AWS::WAF::ByteMatchSet``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html
    Stability:
        experimental
    cloudformationResource:
        AWS::WAF::ByteMatchSet
    """
    def __init__(self, scope: aws_cdk.cdk.Construct, id: str, *, name: str, byte_match_tuples: typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional[typing.List[typing.Union["ByteMatchTupleProperty", aws_cdk.cdk.IResolvable]]]]]=None) -> None:
        """Create a new ``AWS::WAF::ByteMatchSet``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            name: ``AWS::WAF::ByteMatchSet.Name``.
            byteMatchTuples: ``AWS::WAF::ByteMatchSet.ByteMatchTuples``.

        Stability:
            experimental
        """
        props: CfnByteMatchSetProps = {"name": name}

        if byte_match_tuples is not None:
            props["byteMatchTuples"] = byte_match_tuples

        jsii.create(CfnByteMatchSet, self, [scope, id, props])

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
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::WAF::ByteMatchSet.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html#cfn-waf-bytematchset-name
        Stability:
            experimental
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="byteMatchTuples")
    def byte_match_tuples(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional[typing.List[typing.Union["ByteMatchTupleProperty", aws_cdk.cdk.IResolvable]]]]]:
        """``AWS::WAF::ByteMatchSet.ByteMatchTuples``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html#cfn-waf-bytematchset-bytematchtuples
        Stability:
            experimental
        """
        return jsii.get(self, "byteMatchTuples")

    @byte_match_tuples.setter
    def byte_match_tuples(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional[typing.List[typing.Union["ByteMatchTupleProperty", aws_cdk.cdk.IResolvable]]]]]):
        return jsii.set(self, "byteMatchTuples", value)

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _ByteMatchTupleProperty(jsii.compat.TypedDict, total=False):
        targetString: str
        """``CfnByteMatchSet.ByteMatchTupleProperty.TargetString``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-targetstring
        Stability:
            experimental
        """
        targetStringBase64: str
        """``CfnByteMatchSet.ByteMatchTupleProperty.TargetStringBase64``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-targetstringbase64
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-waf.CfnByteMatchSet.ByteMatchTupleProperty", jsii_struct_bases=[_ByteMatchTupleProperty])
    class ByteMatchTupleProperty(_ByteMatchTupleProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html
        Stability:
            experimental
        """
        fieldToMatch: typing.Union[aws_cdk.cdk.IResolvable, "CfnByteMatchSet.FieldToMatchProperty"]
        """``CfnByteMatchSet.ByteMatchTupleProperty.FieldToMatch``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-fieldtomatch
        Stability:
            experimental
        """

        positionalConstraint: str
        """``CfnByteMatchSet.ByteMatchTupleProperty.PositionalConstraint``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-positionalconstraint
        Stability:
            experimental
        """

        textTransformation: str
        """``CfnByteMatchSet.ByteMatchTupleProperty.TextTransformation``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples.html#cfn-waf-bytematchset-bytematchtuples-texttransformation
        Stability:
            experimental
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _FieldToMatchProperty(jsii.compat.TypedDict, total=False):
        data: str
        """``CfnByteMatchSet.FieldToMatchProperty.Data``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html#cfn-waf-bytematchset-bytematchtuples-fieldtomatch-data
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-waf.CfnByteMatchSet.FieldToMatchProperty", jsii_struct_bases=[_FieldToMatchProperty])
    class FieldToMatchProperty(_FieldToMatchProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html
        Stability:
            experimental
        """
        type: str
        """``CfnByteMatchSet.FieldToMatchProperty.Type``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html#cfn-waf-bytematchset-bytematchtuples-fieldtomatch-type
        Stability:
            experimental
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnByteMatchSetProps(jsii.compat.TypedDict, total=False):
    byteMatchTuples: typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union["CfnByteMatchSet.ByteMatchTupleProperty", aws_cdk.cdk.IResolvable]]]
    """``AWS::WAF::ByteMatchSet.ByteMatchTuples``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html#cfn-waf-bytematchset-bytematchtuples
    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-waf.CfnByteMatchSetProps", jsii_struct_bases=[_CfnByteMatchSetProps])
class CfnByteMatchSetProps(_CfnByteMatchSetProps):
    """Properties for defining a ``AWS::WAF::ByteMatchSet``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html
    Stability:
        experimental
    """
    name: str
    """``AWS::WAF::ByteMatchSet.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html#cfn-waf-bytematchset-name
    Stability:
        experimental
    """

class CfnIPSet(aws_cdk.cdk.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-waf.CfnIPSet"):
    """A CloudFormation ``AWS::WAF::IPSet``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html
    Stability:
        experimental
    cloudformationResource:
        AWS::WAF::IPSet
    """
    def __init__(self, scope: aws_cdk.cdk.Construct, id: str, *, name: str, ip_set_descriptors: typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.cdk.IResolvable, "IPSetDescriptorProperty"]]]]]=None) -> None:
        """Create a new ``AWS::WAF::IPSet``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            name: ``AWS::WAF::IPSet.Name``.
            ipSetDescriptors: ``AWS::WAF::IPSet.IPSetDescriptors``.

        Stability:
            experimental
        """
        props: CfnIPSetProps = {"name": name}

        if ip_set_descriptors is not None:
            props["ipSetDescriptors"] = ip_set_descriptors

        jsii.create(CfnIPSet, self, [scope, id, props])

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
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::WAF::IPSet.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html#cfn-waf-ipset-name
        Stability:
            experimental
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="ipSetDescriptors")
    def ip_set_descriptors(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.cdk.IResolvable, "IPSetDescriptorProperty"]]]]]:
        """``AWS::WAF::IPSet.IPSetDescriptors``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html#cfn-waf-ipset-ipsetdescriptors
        Stability:
            experimental
        """
        return jsii.get(self, "ipSetDescriptors")

    @ip_set_descriptors.setter
    def ip_set_descriptors(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.cdk.IResolvable, "IPSetDescriptorProperty"]]]]]):
        return jsii.set(self, "ipSetDescriptors", value)

    @jsii.interface(jsii_type="@aws-cdk/aws-waf.CfnIPSet.IPSetDescriptorProperty")
    class IPSetDescriptorProperty(jsii.compat.Protocol):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html
        Stability:
            experimental
        """
        @staticmethod
        def __jsii_proxy_class__():
            return _IPSetDescriptorPropertyProxy

        @property
        @jsii.member(jsii_name="type")
        def type(self) -> str:
            """``CfnIPSet.IPSetDescriptorProperty.Type``.

            See:
                http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html#cfn-waf-ipset-ipsetdescriptors-type
            Stability:
                experimental
            """
            ...

        @property
        @jsii.member(jsii_name="value")
        def value(self) -> str:
            """``CfnIPSet.IPSetDescriptorProperty.Value``.

            See:
                http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html#cfn-waf-ipset-ipsetdescriptors-value
            Stability:
                experimental
            """
            ...


    class _IPSetDescriptorPropertyProxy():
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html
        Stability:
            experimental
        """
        __jsii_type__ = "@aws-cdk/aws-waf.CfnIPSet.IPSetDescriptorProperty"
        @property
        @jsii.member(jsii_name="type")
        def type(self) -> str:
            """``CfnIPSet.IPSetDescriptorProperty.Type``.

            See:
                http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html#cfn-waf-ipset-ipsetdescriptors-type
            Stability:
                experimental
            """
            return jsii.get(self, "type")

        @property
        @jsii.member(jsii_name="value")
        def value(self) -> str:
            """``CfnIPSet.IPSetDescriptorProperty.Value``.

            See:
                http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-ipset-ipsetdescriptors.html#cfn-waf-ipset-ipsetdescriptors-value
            Stability:
                experimental
            """
            return jsii.get(self, "value")



@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnIPSetProps(jsii.compat.TypedDict, total=False):
    ipSetDescriptors: typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "CfnIPSet.IPSetDescriptorProperty"]]]
    """``AWS::WAF::IPSet.IPSetDescriptors``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html#cfn-waf-ipset-ipsetdescriptors
    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-waf.CfnIPSetProps", jsii_struct_bases=[_CfnIPSetProps])
class CfnIPSetProps(_CfnIPSetProps):
    """Properties for defining a ``AWS::WAF::IPSet``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html
    Stability:
        experimental
    """
    name: str
    """``AWS::WAF::IPSet.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html#cfn-waf-ipset-name
    Stability:
        experimental
    """

class CfnRule(aws_cdk.cdk.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-waf.CfnRule"):
    """A CloudFormation ``AWS::WAF::Rule``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html
    Stability:
        experimental
    cloudformationResource:
        AWS::WAF::Rule
    """
    def __init__(self, scope: aws_cdk.cdk.Construct, id: str, *, metric_name: str, name: str, predicates: typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.cdk.IResolvable, "PredicateProperty"]]]]]=None) -> None:
        """Create a new ``AWS::WAF::Rule``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            metricName: ``AWS::WAF::Rule.MetricName``.
            name: ``AWS::WAF::Rule.Name``.
            predicates: ``AWS::WAF::Rule.Predicates``.

        Stability:
            experimental
        """
        props: CfnRuleProps = {"metricName": metric_name, "name": name}

        if predicates is not None:
            props["predicates"] = predicates

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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> str:
        """``AWS::WAF::Rule.MetricName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-metricname
        Stability:
            experimental
        """
        return jsii.get(self, "metricName")

    @metric_name.setter
    def metric_name(self, value: str):
        return jsii.set(self, "metricName", value)

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::WAF::Rule.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-name
        Stability:
            experimental
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="predicates")
    def predicates(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.cdk.IResolvable, "PredicateProperty"]]]]]:
        """``AWS::WAF::Rule.Predicates``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-predicates
        Stability:
            experimental
        """
        return jsii.get(self, "predicates")

    @predicates.setter
    def predicates(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.cdk.IResolvable, "PredicateProperty"]]]]]):
        return jsii.set(self, "predicates", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-waf.CfnRule.PredicateProperty", jsii_struct_bases=[])
    class PredicateProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-rule-predicates.html
        Stability:
            experimental
        """
        dataId: str
        """``CfnRule.PredicateProperty.DataId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-rule-predicates.html#cfn-waf-rule-predicates-dataid
        Stability:
            experimental
        """

        negated: typing.Union[bool, aws_cdk.cdk.IResolvable]
        """``CfnRule.PredicateProperty.Negated``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-rule-predicates.html#cfn-waf-rule-predicates-negated
        Stability:
            experimental
        """

        type: str
        """``CfnRule.PredicateProperty.Type``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-rule-predicates.html#cfn-waf-rule-predicates-type
        Stability:
            experimental
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnRuleProps(jsii.compat.TypedDict, total=False):
    predicates: typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "CfnRule.PredicateProperty"]]]
    """``AWS::WAF::Rule.Predicates``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-predicates
    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-waf.CfnRuleProps", jsii_struct_bases=[_CfnRuleProps])
class CfnRuleProps(_CfnRuleProps):
    """Properties for defining a ``AWS::WAF::Rule``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html
    Stability:
        experimental
    """
    metricName: str
    """``AWS::WAF::Rule.MetricName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-metricname
    Stability:
        experimental
    """

    name: str
    """``AWS::WAF::Rule.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html#cfn-waf-rule-name
    Stability:
        experimental
    """

class CfnSizeConstraintSet(aws_cdk.cdk.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-waf.CfnSizeConstraintSet"):
    """A CloudFormation ``AWS::WAF::SizeConstraintSet``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html
    Stability:
        experimental
    cloudformationResource:
        AWS::WAF::SizeConstraintSet
    """
    def __init__(self, scope: aws_cdk.cdk.Construct, id: str, *, name: str, size_constraints: typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "SizeConstraintProperty"]]]) -> None:
        """Create a new ``AWS::WAF::SizeConstraintSet``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            name: ``AWS::WAF::SizeConstraintSet.Name``.
            sizeConstraints: ``AWS::WAF::SizeConstraintSet.SizeConstraints``.

        Stability:
            experimental
        """
        props: CfnSizeConstraintSetProps = {"name": name, "sizeConstraints": size_constraints}

        jsii.create(CfnSizeConstraintSet, self, [scope, id, props])

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
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::WAF::SizeConstraintSet.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html#cfn-waf-sizeconstraintset-name
        Stability:
            experimental
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="sizeConstraints")
    def size_constraints(self) -> typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "SizeConstraintProperty"]]]:
        """``AWS::WAF::SizeConstraintSet.SizeConstraints``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html#cfn-waf-sizeconstraintset-sizeconstraints
        Stability:
            experimental
        """
        return jsii.get(self, "sizeConstraints")

    @size_constraints.setter
    def size_constraints(self, value: typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "SizeConstraintProperty"]]]):
        return jsii.set(self, "sizeConstraints", value)

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _FieldToMatchProperty(jsii.compat.TypedDict, total=False):
        data: str
        """``CfnSizeConstraintSet.FieldToMatchProperty.Data``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint-fieldtomatch.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch-data
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-waf.CfnSizeConstraintSet.FieldToMatchProperty", jsii_struct_bases=[_FieldToMatchProperty])
    class FieldToMatchProperty(_FieldToMatchProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint-fieldtomatch.html
        Stability:
            experimental
        """
        type: str
        """``CfnSizeConstraintSet.FieldToMatchProperty.Type``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint-fieldtomatch.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch-type
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-waf.CfnSizeConstraintSet.SizeConstraintProperty", jsii_struct_bases=[])
    class SizeConstraintProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html
        Stability:
            experimental
        """
        comparisonOperator: str
        """``CfnSizeConstraintSet.SizeConstraintProperty.ComparisonOperator``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-comparisonoperator
        Stability:
            experimental
        """

        fieldToMatch: typing.Union[aws_cdk.cdk.IResolvable, "CfnSizeConstraintSet.FieldToMatchProperty"]
        """``CfnSizeConstraintSet.SizeConstraintProperty.FieldToMatch``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch
        Stability:
            experimental
        """

        size: jsii.Number
        """``CfnSizeConstraintSet.SizeConstraintProperty.Size``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-size
        Stability:
            experimental
        """

        textTransformation: str
        """``CfnSizeConstraintSet.SizeConstraintProperty.TextTransformation``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sizeconstraintset-sizeconstraint.html#cfn-waf-sizeconstraintset-sizeconstraint-texttransformation
        Stability:
            experimental
        """


@jsii.data_type(jsii_type="@aws-cdk/aws-waf.CfnSizeConstraintSetProps", jsii_struct_bases=[])
class CfnSizeConstraintSetProps(jsii.compat.TypedDict):
    """Properties for defining a ``AWS::WAF::SizeConstraintSet``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html
    Stability:
        experimental
    """
    name: str
    """``AWS::WAF::SizeConstraintSet.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html#cfn-waf-sizeconstraintset-name
    Stability:
        experimental
    """

    sizeConstraints: typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "CfnSizeConstraintSet.SizeConstraintProperty"]]]
    """``AWS::WAF::SizeConstraintSet.SizeConstraints``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html#cfn-waf-sizeconstraintset-sizeconstraints
    Stability:
        experimental
    """

class CfnSqlInjectionMatchSet(aws_cdk.cdk.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-waf.CfnSqlInjectionMatchSet"):
    """A CloudFormation ``AWS::WAF::SqlInjectionMatchSet``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html
    Stability:
        experimental
    cloudformationResource:
        AWS::WAF::SqlInjectionMatchSet
    """
    def __init__(self, scope: aws_cdk.cdk.Construct, id: str, *, name: str, sql_injection_match_tuples: typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.cdk.IResolvable, "SqlInjectionMatchTupleProperty"]]]]]=None) -> None:
        """Create a new ``AWS::WAF::SqlInjectionMatchSet``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            name: ``AWS::WAF::SqlInjectionMatchSet.Name``.
            sqlInjectionMatchTuples: ``AWS::WAF::SqlInjectionMatchSet.SqlInjectionMatchTuples``.

        Stability:
            experimental
        """
        props: CfnSqlInjectionMatchSetProps = {"name": name}

        if sql_injection_match_tuples is not None:
            props["sqlInjectionMatchTuples"] = sql_injection_match_tuples

        jsii.create(CfnSqlInjectionMatchSet, self, [scope, id, props])

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
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::WAF::SqlInjectionMatchSet.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html#cfn-waf-sqlinjectionmatchset-name
        Stability:
            experimental
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="sqlInjectionMatchTuples")
    def sql_injection_match_tuples(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.cdk.IResolvable, "SqlInjectionMatchTupleProperty"]]]]]:
        """``AWS::WAF::SqlInjectionMatchSet.SqlInjectionMatchTuples``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html#cfn-waf-sqlinjectionmatchset-sqlinjectionmatchtuples
        Stability:
            experimental
        """
        return jsii.get(self, "sqlInjectionMatchTuples")

    @sql_injection_match_tuples.setter
    def sql_injection_match_tuples(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.cdk.IResolvable, "SqlInjectionMatchTupleProperty"]]]]]):
        return jsii.set(self, "sqlInjectionMatchTuples", value)

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _FieldToMatchProperty(jsii.compat.TypedDict, total=False):
        data: str
        """``CfnSqlInjectionMatchSet.FieldToMatchProperty.Data``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch-data
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-waf.CfnSqlInjectionMatchSet.FieldToMatchProperty", jsii_struct_bases=[_FieldToMatchProperty])
    class FieldToMatchProperty(_FieldToMatchProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html
        Stability:
            experimental
        """
        type: str
        """``CfnSqlInjectionMatchSet.FieldToMatchProperty.Type``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-bytematchset-bytematchtuples-fieldtomatch.html#cfn-waf-sizeconstraintset-sizeconstraint-fieldtomatch-type
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-waf.CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty", jsii_struct_bases=[])
    class SqlInjectionMatchTupleProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sqlinjectionmatchset-sqlinjectionmatchtuples.html
        Stability:
            experimental
        """
        fieldToMatch: typing.Union[aws_cdk.cdk.IResolvable, "CfnSqlInjectionMatchSet.FieldToMatchProperty"]
        """``CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty.FieldToMatch``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sqlinjectionmatchset-sqlinjectionmatchtuples.html#cfn-waf-sqlinjectionmatchset-sqlinjectionmatchtuples-fieldtomatch
        Stability:
            experimental
        """

        textTransformation: str
        """``CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty.TextTransformation``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-sqlinjectionmatchset-sqlinjectionmatchtuples.html#cfn-waf-sqlinjectionmatchset-sqlinjectionmatchtuples-texttransformation
        Stability:
            experimental
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnSqlInjectionMatchSetProps(jsii.compat.TypedDict, total=False):
    sqlInjectionMatchTuples: typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "CfnSqlInjectionMatchSet.SqlInjectionMatchTupleProperty"]]]
    """``AWS::WAF::SqlInjectionMatchSet.SqlInjectionMatchTuples``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html#cfn-waf-sqlinjectionmatchset-sqlinjectionmatchtuples
    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-waf.CfnSqlInjectionMatchSetProps", jsii_struct_bases=[_CfnSqlInjectionMatchSetProps])
class CfnSqlInjectionMatchSetProps(_CfnSqlInjectionMatchSetProps):
    """Properties for defining a ``AWS::WAF::SqlInjectionMatchSet``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html
    Stability:
        experimental
    """
    name: str
    """``AWS::WAF::SqlInjectionMatchSet.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html#cfn-waf-sqlinjectionmatchset-name
    Stability:
        experimental
    """

class CfnWebACL(aws_cdk.cdk.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-waf.CfnWebACL"):
    """A CloudFormation ``AWS::WAF::WebACL``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html
    Stability:
        experimental
    cloudformationResource:
        AWS::WAF::WebACL
    """
    def __init__(self, scope: aws_cdk.cdk.Construct, id: str, *, default_action: typing.Union[aws_cdk.cdk.IResolvable, "WafActionProperty"], metric_name: str, name: str, rules: typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.cdk.IResolvable, "ActivatedRuleProperty"]]]]]=None) -> None:
        """Create a new ``AWS::WAF::WebACL``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            defaultAction: ``AWS::WAF::WebACL.DefaultAction``.
            metricName: ``AWS::WAF::WebACL.MetricName``.
            name: ``AWS::WAF::WebACL.Name``.
            rules: ``AWS::WAF::WebACL.Rules``.

        Stability:
            experimental
        """
        props: CfnWebACLProps = {"defaultAction": default_action, "metricName": metric_name, "name": name}

        if rules is not None:
            props["rules"] = rules

        jsii.create(CfnWebACL, self, [scope, id, props])

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
    @jsii.member(jsii_name="defaultAction")
    def default_action(self) -> typing.Union[aws_cdk.cdk.IResolvable, "WafActionProperty"]:
        """``AWS::WAF::WebACL.DefaultAction``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-defaultaction
        Stability:
            experimental
        """
        return jsii.get(self, "defaultAction")

    @default_action.setter
    def default_action(self, value: typing.Union[aws_cdk.cdk.IResolvable, "WafActionProperty"]):
        return jsii.set(self, "defaultAction", value)

    @property
    @jsii.member(jsii_name="metricName")
    def metric_name(self) -> str:
        """``AWS::WAF::WebACL.MetricName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-metricname
        Stability:
            experimental
        """
        return jsii.get(self, "metricName")

    @metric_name.setter
    def metric_name(self, value: str):
        return jsii.set(self, "metricName", value)

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::WAF::WebACL.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-name
        Stability:
            experimental
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="rules")
    def rules(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.cdk.IResolvable, "ActivatedRuleProperty"]]]]]:
        """``AWS::WAF::WebACL.Rules``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-rules
        Stability:
            experimental
        """
        return jsii.get(self, "rules")

    @rules.setter
    def rules(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.cdk.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.cdk.IResolvable, "ActivatedRuleProperty"]]]]]):
        return jsii.set(self, "rules", value)

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _ActivatedRuleProperty(jsii.compat.TypedDict, total=False):
        action: typing.Union[aws_cdk.cdk.IResolvable, "CfnWebACL.WafActionProperty"]
        """``CfnWebACL.ActivatedRuleProperty.Action``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-rules.html#cfn-waf-webacl-rules-action
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-waf.CfnWebACL.ActivatedRuleProperty", jsii_struct_bases=[_ActivatedRuleProperty])
    class ActivatedRuleProperty(_ActivatedRuleProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-rules.html
        Stability:
            experimental
        """
        priority: jsii.Number
        """``CfnWebACL.ActivatedRuleProperty.Priority``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-rules.html#cfn-waf-webacl-rules-priority
        Stability:
            experimental
        """

        ruleId: str
        """``CfnWebACL.ActivatedRuleProperty.RuleId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-rules.html#cfn-waf-webacl-rules-ruleid
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-waf.CfnWebACL.WafActionProperty", jsii_struct_bases=[])
    class WafActionProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-action.html
        Stability:
            experimental
        """
        type: str
        """``CfnWebACL.WafActionProperty.Type``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-webacl-action.html#cfn-waf-webacl-action-type
        Stability:
            experimental
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnWebACLProps(jsii.compat.TypedDict, total=False):
    rules: typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "CfnWebACL.ActivatedRuleProperty"]]]
    """``AWS::WAF::WebACL.Rules``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-rules
    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-waf.CfnWebACLProps", jsii_struct_bases=[_CfnWebACLProps])
class CfnWebACLProps(_CfnWebACLProps):
    """Properties for defining a ``AWS::WAF::WebACL``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html
    Stability:
        experimental
    """
    defaultAction: typing.Union[aws_cdk.cdk.IResolvable, "CfnWebACL.WafActionProperty"]
    """``AWS::WAF::WebACL.DefaultAction``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-defaultaction
    Stability:
        experimental
    """

    metricName: str
    """``AWS::WAF::WebACL.MetricName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-metricname
    Stability:
        experimental
    """

    name: str
    """``AWS::WAF::WebACL.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html#cfn-waf-webacl-name
    Stability:
        experimental
    """

class CfnXssMatchSet(aws_cdk.cdk.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-waf.CfnXssMatchSet"):
    """A CloudFormation ``AWS::WAF::XssMatchSet``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html
    Stability:
        experimental
    cloudformationResource:
        AWS::WAF::XssMatchSet
    """
    def __init__(self, scope: aws_cdk.cdk.Construct, id: str, *, name: str, xss_match_tuples: typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "XssMatchTupleProperty"]]]) -> None:
        """Create a new ``AWS::WAF::XssMatchSet``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            name: ``AWS::WAF::XssMatchSet.Name``.
            xssMatchTuples: ``AWS::WAF::XssMatchSet.XssMatchTuples``.

        Stability:
            experimental
        """
        props: CfnXssMatchSetProps = {"name": name, "xssMatchTuples": xss_match_tuples}

        jsii.create(CfnXssMatchSet, self, [scope, id, props])

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
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """``AWS::WAF::XssMatchSet.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html#cfn-waf-xssmatchset-name
        Stability:
            experimental
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: str):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="xssMatchTuples")
    def xss_match_tuples(self) -> typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "XssMatchTupleProperty"]]]:
        """``AWS::WAF::XssMatchSet.XssMatchTuples``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html#cfn-waf-xssmatchset-xssmatchtuples
        Stability:
            experimental
        """
        return jsii.get(self, "xssMatchTuples")

    @xss_match_tuples.setter
    def xss_match_tuples(self, value: typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "XssMatchTupleProperty"]]]):
        return jsii.set(self, "xssMatchTuples", value)

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _FieldToMatchProperty(jsii.compat.TypedDict, total=False):
        data: str
        """``CfnXssMatchSet.FieldToMatchProperty.Data``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple-fieldtomatch.html#cfn-waf-xssmatchset-xssmatchtuple-fieldtomatch-data
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-waf.CfnXssMatchSet.FieldToMatchProperty", jsii_struct_bases=[_FieldToMatchProperty])
    class FieldToMatchProperty(_FieldToMatchProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple-fieldtomatch.html
        Stability:
            experimental
        """
        type: str
        """``CfnXssMatchSet.FieldToMatchProperty.Type``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple-fieldtomatch.html#cfn-waf-xssmatchset-xssmatchtuple-fieldtomatch-type
        Stability:
            experimental
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-waf.CfnXssMatchSet.XssMatchTupleProperty", jsii_struct_bases=[])
    class XssMatchTupleProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple.html
        Stability:
            experimental
        """
        fieldToMatch: typing.Union[aws_cdk.cdk.IResolvable, "CfnXssMatchSet.FieldToMatchProperty"]
        """``CfnXssMatchSet.XssMatchTupleProperty.FieldToMatch``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple.html#cfn-waf-xssmatchset-xssmatchtuple-fieldtomatch
        Stability:
            experimental
        """

        textTransformation: str
        """``CfnXssMatchSet.XssMatchTupleProperty.TextTransformation``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waf-xssmatchset-xssmatchtuple.html#cfn-waf-xssmatchset-xssmatchtuple-texttransformation
        Stability:
            experimental
        """


@jsii.data_type(jsii_type="@aws-cdk/aws-waf.CfnXssMatchSetProps", jsii_struct_bases=[])
class CfnXssMatchSetProps(jsii.compat.TypedDict):
    """Properties for defining a ``AWS::WAF::XssMatchSet``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html
    Stability:
        experimental
    """
    name: str
    """``AWS::WAF::XssMatchSet.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html#cfn-waf-xssmatchset-name
    Stability:
        experimental
    """

    xssMatchTuples: typing.Union[aws_cdk.cdk.IResolvable, typing.List[typing.Union[aws_cdk.cdk.IResolvable, "CfnXssMatchSet.XssMatchTupleProperty"]]]
    """``AWS::WAF::XssMatchSet.XssMatchTuples``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html#cfn-waf-xssmatchset-xssmatchtuples
    Stability:
        experimental
    """

__all__ = ["CfnByteMatchSet", "CfnByteMatchSetProps", "CfnIPSet", "CfnIPSetProps", "CfnRule", "CfnRuleProps", "CfnSizeConstraintSet", "CfnSizeConstraintSetProps", "CfnSqlInjectionMatchSet", "CfnSqlInjectionMatchSetProps", "CfnWebACL", "CfnWebACLProps", "CfnXssMatchSet", "CfnXssMatchSetProps", "__jsii_assembly__"]

publication.publish()
