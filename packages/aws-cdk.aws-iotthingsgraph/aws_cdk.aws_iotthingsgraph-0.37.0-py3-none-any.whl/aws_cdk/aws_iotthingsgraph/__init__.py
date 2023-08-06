import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-iotthingsgraph", "0.37.0", __name__, "aws-iotthingsgraph@0.37.0.jsii.tgz")
class CfnFlowTemplate(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-iotthingsgraph.CfnFlowTemplate"):
    """A CloudFormation ``AWS::IoTThingsGraph::FlowTemplate``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html
    Stability:
        stable
    cloudformationResource:
        AWS::IoTThingsGraph::FlowTemplate
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, definition: typing.Union["DefinitionDocumentProperty", aws_cdk.core.IResolvable], compatible_namespace_version: typing.Optional[jsii.Number]=None) -> None:
        """Create a new ``AWS::IoTThingsGraph::FlowTemplate``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            definition: ``AWS::IoTThingsGraph::FlowTemplate.Definition``.
            compatible_namespace_version: ``AWS::IoTThingsGraph::FlowTemplate.CompatibleNamespaceVersion``.

        Stability:
            stable
        """
        props: CfnFlowTemplateProps = {"definition": definition}

        if compatible_namespace_version is not None:
            props["compatibleNamespaceVersion"] = compatible_namespace_version

        jsii.create(CfnFlowTemplate, self, [scope, id, props])

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
    @jsii.member(jsii_name="definition")
    def definition(self) -> typing.Union["DefinitionDocumentProperty", aws_cdk.core.IResolvable]:
        """``AWS::IoTThingsGraph::FlowTemplate.Definition``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html#cfn-iotthingsgraph-flowtemplate-definition
        Stability:
            stable
        """
        return jsii.get(self, "definition")

    @definition.setter
    def definition(self, value: typing.Union["DefinitionDocumentProperty", aws_cdk.core.IResolvable]):
        return jsii.set(self, "definition", value)

    @property
    @jsii.member(jsii_name="compatibleNamespaceVersion")
    def compatible_namespace_version(self) -> typing.Optional[jsii.Number]:
        """``AWS::IoTThingsGraph::FlowTemplate.CompatibleNamespaceVersion``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html#cfn-iotthingsgraph-flowtemplate-compatiblenamespaceversion
        Stability:
            stable
        """
        return jsii.get(self, "compatibleNamespaceVersion")

    @compatible_namespace_version.setter
    def compatible_namespace_version(self, value: typing.Optional[jsii.Number]):
        return jsii.set(self, "compatibleNamespaceVersion", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-iotthingsgraph.CfnFlowTemplate.DefinitionDocumentProperty", jsii_struct_bases=[])
    class DefinitionDocumentProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotthingsgraph-flowtemplate-definitiondocument.html
        Stability:
            stable
        """
        language: str
        """``CfnFlowTemplate.DefinitionDocumentProperty.Language``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotthingsgraph-flowtemplate-definitiondocument.html#cfn-iotthingsgraph-flowtemplate-definitiondocument-language
        Stability:
            stable
        """

        text: str
        """``CfnFlowTemplate.DefinitionDocumentProperty.Text``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotthingsgraph-flowtemplate-definitiondocument.html#cfn-iotthingsgraph-flowtemplate-definitiondocument-text
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnFlowTemplateProps(jsii.compat.TypedDict, total=False):
    compatibleNamespaceVersion: jsii.Number
    """``AWS::IoTThingsGraph::FlowTemplate.CompatibleNamespaceVersion``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html#cfn-iotthingsgraph-flowtemplate-compatiblenamespaceversion
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-iotthingsgraph.CfnFlowTemplateProps", jsii_struct_bases=[_CfnFlowTemplateProps])
class CfnFlowTemplateProps(_CfnFlowTemplateProps):
    """Properties for defining a ``AWS::IoTThingsGraph::FlowTemplate``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html
    Stability:
        stable
    """
    definition: typing.Union["CfnFlowTemplate.DefinitionDocumentProperty", aws_cdk.core.IResolvable]
    """``AWS::IoTThingsGraph::FlowTemplate.Definition``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html#cfn-iotthingsgraph-flowtemplate-definition
    Stability:
        stable
    """

__all__ = ["CfnFlowTemplate", "CfnFlowTemplateProps", "__jsii_assembly__"]

publication.publish()
