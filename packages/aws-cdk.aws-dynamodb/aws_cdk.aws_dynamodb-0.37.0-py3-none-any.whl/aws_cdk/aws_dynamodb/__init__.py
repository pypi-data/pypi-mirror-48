import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_applicationautoscaling
import aws_cdk.aws_iam
import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-dynamodb", "0.37.0", __name__, "aws-dynamodb@0.37.0.jsii.tgz")
@jsii.data_type(jsii_type="@aws-cdk/aws-dynamodb.Attribute", jsii_struct_bases=[])
class Attribute(jsii.compat.TypedDict):
    """
    Stability:
        stable
    """
    name: str
    """The name of an attribute.

    Stability:
        stable
    """

    type: "AttributeType"
    """The data type of an attribute.

    Stability:
        stable
    """

@jsii.enum(jsii_type="@aws-cdk/aws-dynamodb.AttributeType")
class AttributeType(enum.Enum):
    """
    Stability:
        stable
    """
    BINARY = "BINARY"
    """
    Stability:
        stable
    """
    NUMBER = "NUMBER"
    """
    Stability:
        stable
    """
    STRING = "STRING"
    """
    Stability:
        stable
    """

@jsii.enum(jsii_type="@aws-cdk/aws-dynamodb.BillingMode")
class BillingMode(enum.Enum):
    """DyanmoDB's Read/Write capacity modes.

    Stability:
        stable
    """
    PAY_PER_REQUEST = "PAY_PER_REQUEST"
    """Pay only for what you use.

    You don't configure Read/Write capacity units.

    Stability:
        stable
    """
    PROVISIONED = "PROVISIONED"
    """Explicitly specified Read/Write capacity units.

    Stability:
        stable
    """

class CfnTable(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-dynamodb.CfnTable"):
    """A CloudFormation ``AWS::DynamoDB::Table``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html
    Stability:
        stable
    cloudformationResource:
        AWS::DynamoDB::Table
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, key_schema: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["KeySchemaProperty", aws_cdk.core.IResolvable]]], attribute_definitions: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "AttributeDefinitionProperty"]]]]]=None, billing_mode: typing.Optional[str]=None, global_secondary_indexes: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "GlobalSecondaryIndexProperty"]]]]]=None, local_secondary_indexes: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "LocalSecondaryIndexProperty"]]]]]=None, point_in_time_recovery_specification: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["PointInTimeRecoverySpecificationProperty"]]]=None, provisioned_throughput: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ProvisionedThroughputProperty"]]]=None, sse_specification: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["SSESpecificationProperty"]]]=None, stream_specification: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["StreamSpecificationProperty"]]]=None, table_name: typing.Optional[str]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None, time_to_live_specification: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["TimeToLiveSpecificationProperty"]]]=None) -> None:
        """Create a new ``AWS::DynamoDB::Table``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            key_schema: ``AWS::DynamoDB::Table.KeySchema``.
            attribute_definitions: ``AWS::DynamoDB::Table.AttributeDefinitions``.
            billing_mode: ``AWS::DynamoDB::Table.BillingMode``.
            global_secondary_indexes: ``AWS::DynamoDB::Table.GlobalSecondaryIndexes``.
            local_secondary_indexes: ``AWS::DynamoDB::Table.LocalSecondaryIndexes``.
            point_in_time_recovery_specification: ``AWS::DynamoDB::Table.PointInTimeRecoverySpecification``.
            provisioned_throughput: ``AWS::DynamoDB::Table.ProvisionedThroughput``.
            sse_specification: ``AWS::DynamoDB::Table.SSESpecification``.
            stream_specification: ``AWS::DynamoDB::Table.StreamSpecification``.
            table_name: ``AWS::DynamoDB::Table.TableName``.
            tags: ``AWS::DynamoDB::Table.Tags``.
            time_to_live_specification: ``AWS::DynamoDB::Table.TimeToLiveSpecification``.

        Stability:
            stable
        """
        props: CfnTableProps = {"keySchema": key_schema}

        if attribute_definitions is not None:
            props["attributeDefinitions"] = attribute_definitions

        if billing_mode is not None:
            props["billingMode"] = billing_mode

        if global_secondary_indexes is not None:
            props["globalSecondaryIndexes"] = global_secondary_indexes

        if local_secondary_indexes is not None:
            props["localSecondaryIndexes"] = local_secondary_indexes

        if point_in_time_recovery_specification is not None:
            props["pointInTimeRecoverySpecification"] = point_in_time_recovery_specification

        if provisioned_throughput is not None:
            props["provisionedThroughput"] = provisioned_throughput

        if sse_specification is not None:
            props["sseSpecification"] = sse_specification

        if stream_specification is not None:
            props["streamSpecification"] = stream_specification

        if table_name is not None:
            props["tableName"] = table_name

        if tags is not None:
            props["tags"] = tags

        if time_to_live_specification is not None:
            props["timeToLiveSpecification"] = time_to_live_specification

        jsii.create(CfnTable, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrStreamArn")
    def attr_stream_arn(self) -> str:
        """
        Stability:
            stable
        cloudformationAttribute:
            StreamArn
        """
        return jsii.get(self, "attrStreamArn")

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
        """``AWS::DynamoDB::Table.Tags``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tags
        Stability:
            stable
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="keySchema")
    def key_schema(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["KeySchemaProperty", aws_cdk.core.IResolvable]]]:
        """``AWS::DynamoDB::Table.KeySchema``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-keyschema
        Stability:
            stable
        """
        return jsii.get(self, "keySchema")

    @key_schema.setter
    def key_schema(self, value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["KeySchemaProperty", aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "keySchema", value)

    @property
    @jsii.member(jsii_name="attributeDefinitions")
    def attribute_definitions(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "AttributeDefinitionProperty"]]]]]:
        """``AWS::DynamoDB::Table.AttributeDefinitions``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-attributedef
        Stability:
            stable
        """
        return jsii.get(self, "attributeDefinitions")

    @attribute_definitions.setter
    def attribute_definitions(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "AttributeDefinitionProperty"]]]]]):
        return jsii.set(self, "attributeDefinitions", value)

    @property
    @jsii.member(jsii_name="billingMode")
    def billing_mode(self) -> typing.Optional[str]:
        """``AWS::DynamoDB::Table.BillingMode``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-billingmode
        Stability:
            stable
        """
        return jsii.get(self, "billingMode")

    @billing_mode.setter
    def billing_mode(self, value: typing.Optional[str]):
        return jsii.set(self, "billingMode", value)

    @property
    @jsii.member(jsii_name="globalSecondaryIndexes")
    def global_secondary_indexes(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "GlobalSecondaryIndexProperty"]]]]]:
        """``AWS::DynamoDB::Table.GlobalSecondaryIndexes``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-gsi
        Stability:
            stable
        """
        return jsii.get(self, "globalSecondaryIndexes")

    @global_secondary_indexes.setter
    def global_secondary_indexes(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "GlobalSecondaryIndexProperty"]]]]]):
        return jsii.set(self, "globalSecondaryIndexes", value)

    @property
    @jsii.member(jsii_name="localSecondaryIndexes")
    def local_secondary_indexes(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "LocalSecondaryIndexProperty"]]]]]:
        """``AWS::DynamoDB::Table.LocalSecondaryIndexes``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-lsi
        Stability:
            stable
        """
        return jsii.get(self, "localSecondaryIndexes")

    @local_secondary_indexes.setter
    def local_secondary_indexes(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "LocalSecondaryIndexProperty"]]]]]):
        return jsii.set(self, "localSecondaryIndexes", value)

    @property
    @jsii.member(jsii_name="pointInTimeRecoverySpecification")
    def point_in_time_recovery_specification(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["PointInTimeRecoverySpecificationProperty"]]]:
        """``AWS::DynamoDB::Table.PointInTimeRecoverySpecification``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-pointintimerecoveryspecification
        Stability:
            stable
        """
        return jsii.get(self, "pointInTimeRecoverySpecification")

    @point_in_time_recovery_specification.setter
    def point_in_time_recovery_specification(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["PointInTimeRecoverySpecificationProperty"]]]):
        return jsii.set(self, "pointInTimeRecoverySpecification", value)

    @property
    @jsii.member(jsii_name="provisionedThroughput")
    def provisioned_throughput(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ProvisionedThroughputProperty"]]]:
        """``AWS::DynamoDB::Table.ProvisionedThroughput``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-provisionedthroughput
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
        """``AWS::DynamoDB::Table.SSESpecification``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-ssespecification
        Stability:
            stable
        """
        return jsii.get(self, "sseSpecification")

    @sse_specification.setter
    def sse_specification(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["SSESpecificationProperty"]]]):
        return jsii.set(self, "sseSpecification", value)

    @property
    @jsii.member(jsii_name="streamSpecification")
    def stream_specification(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["StreamSpecificationProperty"]]]:
        """``AWS::DynamoDB::Table.StreamSpecification``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-streamspecification
        Stability:
            stable
        """
        return jsii.get(self, "streamSpecification")

    @stream_specification.setter
    def stream_specification(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["StreamSpecificationProperty"]]]):
        return jsii.set(self, "streamSpecification", value)

    @property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> typing.Optional[str]:
        """``AWS::DynamoDB::Table.TableName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tablename
        Stability:
            stable
        """
        return jsii.get(self, "tableName")

    @table_name.setter
    def table_name(self, value: typing.Optional[str]):
        return jsii.set(self, "tableName", value)

    @property
    @jsii.member(jsii_name="timeToLiveSpecification")
    def time_to_live_specification(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["TimeToLiveSpecificationProperty"]]]:
        """``AWS::DynamoDB::Table.TimeToLiveSpecification``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-timetolivespecification
        Stability:
            stable
        """
        return jsii.get(self, "timeToLiveSpecification")

    @time_to_live_specification.setter
    def time_to_live_specification(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["TimeToLiveSpecificationProperty"]]]):
        return jsii.set(self, "timeToLiveSpecification", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-dynamodb.CfnTable.AttributeDefinitionProperty", jsii_struct_bases=[])
    class AttributeDefinitionProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-attributedef.html
        Stability:
            stable
        """
        attributeName: str
        """``CfnTable.AttributeDefinitionProperty.AttributeName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-attributedef.html#cfn-dynamodb-attributedef-attributename
        Stability:
            stable
        """

        attributeType: str
        """``CfnTable.AttributeDefinitionProperty.AttributeType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-attributedef.html#cfn-dynamodb-attributedef-attributename-attributetype
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _GlobalSecondaryIndexProperty(jsii.compat.TypedDict, total=False):
        provisionedThroughput: typing.Union[aws_cdk.core.IResolvable, "CfnTable.ProvisionedThroughputProperty"]
        """``CfnTable.GlobalSecondaryIndexProperty.ProvisionedThroughput``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-provisionedthroughput
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-dynamodb.CfnTable.GlobalSecondaryIndexProperty", jsii_struct_bases=[_GlobalSecondaryIndexProperty])
    class GlobalSecondaryIndexProperty(_GlobalSecondaryIndexProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html
        Stability:
            stable
        """
        indexName: str
        """``CfnTable.GlobalSecondaryIndexProperty.IndexName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-indexname
        Stability:
            stable
        """

        keySchema: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnTable.KeySchemaProperty", aws_cdk.core.IResolvable]]]
        """``CfnTable.GlobalSecondaryIndexProperty.KeySchema``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-keyschema
        Stability:
            stable
        """

        projection: typing.Union[aws_cdk.core.IResolvable, "CfnTable.ProjectionProperty"]
        """``CfnTable.GlobalSecondaryIndexProperty.Projection``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-gsi.html#cfn-dynamodb-gsi-projection
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-dynamodb.CfnTable.KeySchemaProperty", jsii_struct_bases=[])
    class KeySchemaProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-keyschema.html
        Stability:
            stable
        """
        attributeName: str
        """``CfnTable.KeySchemaProperty.AttributeName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-keyschema.html#aws-properties-dynamodb-keyschema-attributename
        Stability:
            stable
        """

        keyType: str
        """``CfnTable.KeySchemaProperty.KeyType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-keyschema.html#aws-properties-dynamodb-keyschema-keytype
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-dynamodb.CfnTable.LocalSecondaryIndexProperty", jsii_struct_bases=[])
    class LocalSecondaryIndexProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html
        Stability:
            stable
        """
        indexName: str
        """``CfnTable.LocalSecondaryIndexProperty.IndexName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html#cfn-dynamodb-lsi-indexname
        Stability:
            stable
        """

        keySchema: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnTable.KeySchemaProperty", aws_cdk.core.IResolvable]]]
        """``CfnTable.LocalSecondaryIndexProperty.KeySchema``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html#cfn-dynamodb-lsi-keyschema
        Stability:
            stable
        """

        projection: typing.Union[aws_cdk.core.IResolvable, "CfnTable.ProjectionProperty"]
        """``CfnTable.LocalSecondaryIndexProperty.Projection``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-lsi.html#cfn-dynamodb-lsi-projection
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-dynamodb.CfnTable.PointInTimeRecoverySpecificationProperty", jsii_struct_bases=[])
    class PointInTimeRecoverySpecificationProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-pointintimerecoveryspecification.html
        Stability:
            stable
        """
        pointInTimeRecoveryEnabled: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnTable.PointInTimeRecoverySpecificationProperty.PointInTimeRecoveryEnabled``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-pointintimerecoveryspecification.html#cfn-dynamodb-table-pointintimerecoveryspecification-pointintimerecoveryenabled
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-dynamodb.CfnTable.ProjectionProperty", jsii_struct_bases=[])
    class ProjectionProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-projectionobject.html
        Stability:
            stable
        """
        nonKeyAttributes: typing.List[str]
        """``CfnTable.ProjectionProperty.NonKeyAttributes``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-projectionobject.html#cfn-dynamodb-projectionobj-nonkeyatt
        Stability:
            stable
        """

        projectionType: str
        """``CfnTable.ProjectionProperty.ProjectionType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-projectionobject.html#cfn-dynamodb-projectionobj-projtype
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-dynamodb.CfnTable.ProvisionedThroughputProperty", jsii_struct_bases=[])
    class ProvisionedThroughputProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html
        Stability:
            stable
        """
        readCapacityUnits: jsii.Number
        """``CfnTable.ProvisionedThroughputProperty.ReadCapacityUnits``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html#cfn-dynamodb-provisionedthroughput-readcapacityunits
        Stability:
            stable
        """

        writeCapacityUnits: jsii.Number
        """``CfnTable.ProvisionedThroughputProperty.WriteCapacityUnits``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-provisionedthroughput.html#cfn-dynamodb-provisionedthroughput-writecapacityunits
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-dynamodb.CfnTable.SSESpecificationProperty", jsii_struct_bases=[])
    class SSESpecificationProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html
        Stability:
            stable
        """
        sseEnabled: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnTable.SSESpecificationProperty.SSEEnabled``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-ssespecification.html#cfn-dynamodb-table-ssespecification-sseenabled
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-dynamodb.CfnTable.StreamSpecificationProperty", jsii_struct_bases=[])
    class StreamSpecificationProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-streamspecification.html
        Stability:
            stable
        """
        streamViewType: str
        """``CfnTable.StreamSpecificationProperty.StreamViewType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-streamspecification.html#cfn-dynamodb-streamspecification-streamviewtype
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-dynamodb.CfnTable.TimeToLiveSpecificationProperty", jsii_struct_bases=[])
    class TimeToLiveSpecificationProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-timetolivespecification.html
        Stability:
            stable
        """
        attributeName: str
        """``CfnTable.TimeToLiveSpecificationProperty.AttributeName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-timetolivespecification.html#cfn-dynamodb-timetolivespecification-attributename
        Stability:
            stable
        """

        enabled: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnTable.TimeToLiveSpecificationProperty.Enabled``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-timetolivespecification.html#cfn-dynamodb-timetolivespecification-enabled
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnTableProps(jsii.compat.TypedDict, total=False):
    attributeDefinitions: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTable.AttributeDefinitionProperty"]]]
    """``AWS::DynamoDB::Table.AttributeDefinitions``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-attributedef
    Stability:
        stable
    """
    billingMode: str
    """``AWS::DynamoDB::Table.BillingMode``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-billingmode
    Stability:
        stable
    """
    globalSecondaryIndexes: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTable.GlobalSecondaryIndexProperty"]]]
    """``AWS::DynamoDB::Table.GlobalSecondaryIndexes``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-gsi
    Stability:
        stable
    """
    localSecondaryIndexes: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnTable.LocalSecondaryIndexProperty"]]]
    """``AWS::DynamoDB::Table.LocalSecondaryIndexes``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-lsi
    Stability:
        stable
    """
    pointInTimeRecoverySpecification: typing.Union[aws_cdk.core.IResolvable, "CfnTable.PointInTimeRecoverySpecificationProperty"]
    """``AWS::DynamoDB::Table.PointInTimeRecoverySpecification``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-pointintimerecoveryspecification
    Stability:
        stable
    """
    provisionedThroughput: typing.Union[aws_cdk.core.IResolvable, "CfnTable.ProvisionedThroughputProperty"]
    """``AWS::DynamoDB::Table.ProvisionedThroughput``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-provisionedthroughput
    Stability:
        stable
    """
    sseSpecification: typing.Union[aws_cdk.core.IResolvable, "CfnTable.SSESpecificationProperty"]
    """``AWS::DynamoDB::Table.SSESpecification``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-ssespecification
    Stability:
        stable
    """
    streamSpecification: typing.Union[aws_cdk.core.IResolvable, "CfnTable.StreamSpecificationProperty"]
    """``AWS::DynamoDB::Table.StreamSpecification``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-streamspecification
    Stability:
        stable
    """
    tableName: str
    """``AWS::DynamoDB::Table.TableName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tablename
    Stability:
        stable
    """
    tags: typing.List[aws_cdk.core.CfnTag]
    """``AWS::DynamoDB::Table.Tags``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-tags
    Stability:
        stable
    """
    timeToLiveSpecification: typing.Union[aws_cdk.core.IResolvable, "CfnTable.TimeToLiveSpecificationProperty"]
    """``AWS::DynamoDB::Table.TimeToLiveSpecification``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-timetolivespecification
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-dynamodb.CfnTableProps", jsii_struct_bases=[_CfnTableProps])
class CfnTableProps(_CfnTableProps):
    """Properties for defining a ``AWS::DynamoDB::Table``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html
    Stability:
        stable
    """
    keySchema: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnTable.KeySchemaProperty", aws_cdk.core.IResolvable]]]
    """``AWS::DynamoDB::Table.KeySchema``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html#cfn-dynamodb-table-keyschema
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-dynamodb.EnableScalingProps", jsii_struct_bases=[])
class EnableScalingProps(jsii.compat.TypedDict):
    """Properties for enabling DynamoDB capacity scaling.

    Stability:
        stable
    """
    maxCapacity: jsii.Number
    """Maximum capacity to scale to.

    Stability:
        stable
    """

    minCapacity: jsii.Number
    """Minimum capacity to scale to.

    Stability:
        stable
    """

@jsii.interface(jsii_type="@aws-cdk/aws-dynamodb.IScalableTableAttribute")
class IScalableTableAttribute(jsii.compat.Protocol):
    """Interface for scalable attributes.

    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IScalableTableAttributeProxy

    @jsii.member(jsii_name="scaleOnSchedule")
    def scale_on_schedule(self, id: str, *, schedule: aws_cdk.aws_applicationautoscaling.Schedule, end_time: typing.Optional[datetime.datetime]=None, max_capacity: typing.Optional[jsii.Number]=None, min_capacity: typing.Optional[jsii.Number]=None, start_time: typing.Optional[datetime.datetime]=None) -> None:
        """Add scheduled scaling for this scaling attribute.

        Arguments:
            id: -
            actions: -
            schedule: When to perform this action.
            end_time: When this scheduled action expires. Default: The rule never expires.
            max_capacity: The new maximum capacity. During the scheduled time, the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new maximum capacity
            min_capacity: The new minimum capacity. During the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new minimum capacity
            start_time: When this scheduled action becomes active. Default: The rule is activate immediately

        Stability:
            stable
        """
        ...

    @jsii.member(jsii_name="scaleOnUtilization")
    def scale_on_utilization(self, *, target_utilization_percent: jsii.Number, disable_scale_in: typing.Optional[bool]=None, policy_name: typing.Optional[str]=None, scale_in_cooldown: typing.Optional[aws_cdk.core.Duration]=None, scale_out_cooldown: typing.Optional[aws_cdk.core.Duration]=None) -> None:
        """Scale out or in to keep utilization at a given level.

        Arguments:
            props: -
            target_utilization_percent: Target utilization percentage for the attribute.
            disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
            policy_name: A name for the scaling policy. Default: - Automatically generated name.
            scale_in_cooldown: Period after a scale in activity completes before another scale in activity can start. Default: - No scale in cooldown.
            scale_out_cooldown: Period after a scale out activity completes before another scale out activity can start. Default: - No scale out cooldown.

        Stability:
            stable
        """
        ...


class _IScalableTableAttributeProxy():
    """Interface for scalable attributes.

    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-dynamodb.IScalableTableAttribute"
    @jsii.member(jsii_name="scaleOnSchedule")
    def scale_on_schedule(self, id: str, *, schedule: aws_cdk.aws_applicationautoscaling.Schedule, end_time: typing.Optional[datetime.datetime]=None, max_capacity: typing.Optional[jsii.Number]=None, min_capacity: typing.Optional[jsii.Number]=None, start_time: typing.Optional[datetime.datetime]=None) -> None:
        """Add scheduled scaling for this scaling attribute.

        Arguments:
            id: -
            actions: -
            schedule: When to perform this action.
            end_time: When this scheduled action expires. Default: The rule never expires.
            max_capacity: The new maximum capacity. During the scheduled time, the current capacity is above the maximum capacity, Application Auto Scaling scales in to the maximum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new maximum capacity
            min_capacity: The new minimum capacity. During the scheduled time, if the current capacity is below the minimum capacity, Application Auto Scaling scales out to the minimum capacity. At least one of maxCapacity and minCapacity must be supplied. Default: No new minimum capacity
            start_time: When this scheduled action becomes active. Default: The rule is activate immediately

        Stability:
            stable
        """
        actions: aws_cdk.aws_applicationautoscaling.ScalingSchedule = {"schedule": schedule}

        if end_time is not None:
            actions["endTime"] = end_time

        if max_capacity is not None:
            actions["maxCapacity"] = max_capacity

        if min_capacity is not None:
            actions["minCapacity"] = min_capacity

        if start_time is not None:
            actions["startTime"] = start_time

        return jsii.invoke(self, "scaleOnSchedule", [id, actions])

    @jsii.member(jsii_name="scaleOnUtilization")
    def scale_on_utilization(self, *, target_utilization_percent: jsii.Number, disable_scale_in: typing.Optional[bool]=None, policy_name: typing.Optional[str]=None, scale_in_cooldown: typing.Optional[aws_cdk.core.Duration]=None, scale_out_cooldown: typing.Optional[aws_cdk.core.Duration]=None) -> None:
        """Scale out or in to keep utilization at a given level.

        Arguments:
            props: -
            target_utilization_percent: Target utilization percentage for the attribute.
            disable_scale_in: Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won't remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. Default: false
            policy_name: A name for the scaling policy. Default: - Automatically generated name.
            scale_in_cooldown: Period after a scale in activity completes before another scale in activity can start. Default: - No scale in cooldown.
            scale_out_cooldown: Period after a scale out activity completes before another scale out activity can start. Default: - No scale out cooldown.

        Stability:
            stable
        """
        props: UtilizationScalingProps = {"targetUtilizationPercent": target_utilization_percent}

        if disable_scale_in is not None:
            props["disableScaleIn"] = disable_scale_in

        if policy_name is not None:
            props["policyName"] = policy_name

        if scale_in_cooldown is not None:
            props["scaleInCooldown"] = scale_in_cooldown

        if scale_out_cooldown is not None:
            props["scaleOutCooldown"] = scale_out_cooldown

        return jsii.invoke(self, "scaleOnUtilization", [props])


@jsii.enum(jsii_type="@aws-cdk/aws-dynamodb.ProjectionType")
class ProjectionType(enum.Enum):
    """
    Stability:
        stable
    """
    KEYS_ONLY = "KEYS_ONLY"
    """
    Stability:
        stable
    """
    INCLUDE = "INCLUDE"
    """
    Stability:
        stable
    """
    ALL = "ALL"
    """
    Stability:
        stable
    """

@jsii.data_type_optionals(jsii_struct_bases=[])
class _SecondaryIndexProps(jsii.compat.TypedDict, total=False):
    nonKeyAttributes: typing.List[str]
    """The non-key attributes that are projected into the secondary index.

    Default:
        undefined

    Stability:
        stable
    """
    projectionType: "ProjectionType"
    """The set of attributes that are projected into the secondary index.

    Default:
        ALL

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-dynamodb.SecondaryIndexProps", jsii_struct_bases=[_SecondaryIndexProps])
class SecondaryIndexProps(_SecondaryIndexProps):
    """
    Stability:
        stable
    """
    indexName: str
    """The name of the secondary index.

    Stability:
        stable
    """

@jsii.data_type_optionals(jsii_struct_bases=[SecondaryIndexProps])
class _GlobalSecondaryIndexProps(SecondaryIndexProps, jsii.compat.TypedDict, total=False):
    readCapacity: jsii.Number
    """The read capacity for the global secondary index.

    Can only be provided if table billingMode is Provisioned or undefined.

    Default:
        5

    Stability:
        stable
    """
    sortKey: "Attribute"
    """The attribute of a sort key for the global secondary index.

    Default:
        undefined

    Stability:
        stable
    """
    writeCapacity: jsii.Number
    """The write capacity for the global secondary index.

    Can only be provided if table billingMode is Provisioned or undefined.

    Default:
        5

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-dynamodb.GlobalSecondaryIndexProps", jsii_struct_bases=[_GlobalSecondaryIndexProps])
class GlobalSecondaryIndexProps(_GlobalSecondaryIndexProps):
    """
    Stability:
        stable
    """
    partitionKey: "Attribute"
    """The attribute of a partition key for the global secondary index.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-dynamodb.LocalSecondaryIndexProps", jsii_struct_bases=[SecondaryIndexProps])
class LocalSecondaryIndexProps(SecondaryIndexProps, jsii.compat.TypedDict):
    """
    Stability:
        stable
    """
    sortKey: "Attribute"
    """The attribute of a sort key for the local secondary index.

    Stability:
        stable
    """

@jsii.enum(jsii_type="@aws-cdk/aws-dynamodb.StreamViewType")
class StreamViewType(enum.Enum):
    """When an item in the table is modified, StreamViewType determines what information is written to the stream for this table.

    Valid values for StreamViewType are:

    Stability:
        stable
    enum:
        true
    link:
        https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_StreamSpecification.html
    """
    NEW_IMAGE = "NEW_IMAGE"
    """The entire item, as it appears after it was modified, is written to the stream.

    Stability:
        stable
    """
    OLD_IMAGE = "OLD_IMAGE"
    """The entire item, as it appeared before it was modified, is written to the stream.

    Stability:
        stable
    """
    NEW_AND_OLD_IMAGES = "NEW_AND_OLD_IMAGES"
    """Both the new and the old item images of the item are written to the stream.

    Stability:
        stable
    """
    KEYS_ONLY = "KEYS_ONLY"
    """Only the key attributes of the modified item are written to the stream.

    Stability:
        stable
    """

class Table(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-dynamodb.Table"):
    """Provides a DynamoDB table.

    Stability:
        stable
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, table_name: typing.Optional[str]=None, partition_key: "Attribute", billing_mode: typing.Optional["BillingMode"]=None, point_in_time_recovery: typing.Optional[bool]=None, read_capacity: typing.Optional[jsii.Number]=None, removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy]=None, server_side_encryption: typing.Optional[bool]=None, sort_key: typing.Optional["Attribute"]=None, stream: typing.Optional["StreamViewType"]=None, time_to_live_attribute: typing.Optional[str]=None, write_capacity: typing.Optional[jsii.Number]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            table_name: Enforces a particular physical table name. Default: 
            partition_key: Partition key attribute definition.
            billing_mode: Specify how you are charged for read and write throughput and how you manage capacity. Default: Provisioned
            point_in_time_recovery: Whether point-in-time recovery is enabled. Default: - point-in-time recovery is disabled
            read_capacity: The read capacity for the table. Careful if you add Global Secondary Indexes, as those will share the table's provisioned throughput. Can only be provided if billingMode is Provisioned. Default: 5
            removal_policy: The removal policy to apply to the DynamoDB Table. Default: RemovalPolicy.RETAIN
            server_side_encryption: Whether server-side encryption with an AWS managed customer master key is enabled. Default: - server-side encryption is enabled with an AWS owned customer master key
            sort_key: Table sort key attribute definition. Default: no sort key
            stream: When an item in the table is modified, StreamViewType determines what information is written to the stream for this table. Valid values for StreamViewType are: Default: undefined, streams are disabled
            time_to_live_attribute: The name of TTL attribute. Default: - TTL is disabled
            write_capacity: The write capacity for the table. Careful if you add Global Secondary Indexes, as those will share the table's provisioned throughput. Can only be provided if billingMode is Provisioned. Default: 5

        Stability:
            stable
        """
        props: TableProps = {"partitionKey": partition_key}

        if table_name is not None:
            props["tableName"] = table_name

        if billing_mode is not None:
            props["billingMode"] = billing_mode

        if point_in_time_recovery is not None:
            props["pointInTimeRecovery"] = point_in_time_recovery

        if read_capacity is not None:
            props["readCapacity"] = read_capacity

        if removal_policy is not None:
            props["removalPolicy"] = removal_policy

        if server_side_encryption is not None:
            props["serverSideEncryption"] = server_side_encryption

        if sort_key is not None:
            props["sortKey"] = sort_key

        if stream is not None:
            props["stream"] = stream

        if time_to_live_attribute is not None:
            props["timeToLiveAttribute"] = time_to_live_attribute

        if write_capacity is not None:
            props["writeCapacity"] = write_capacity

        jsii.create(Table, self, [scope, id, props])

    @jsii.member(jsii_name="grantListStreams")
    @classmethod
    def grant_list_streams(cls, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Permits an IAM Principal to list all DynamoDB Streams.

        Arguments:
            grantee: The principal (no-op if undefined).

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "grantListStreams", [grantee])

    @jsii.member(jsii_name="addGlobalSecondaryIndex")
    def add_global_secondary_index(self, *, partition_key: "Attribute", read_capacity: typing.Optional[jsii.Number]=None, sort_key: typing.Optional["Attribute"]=None, write_capacity: typing.Optional[jsii.Number]=None, index_name: str, non_key_attributes: typing.Optional[typing.List[str]]=None, projection_type: typing.Optional["ProjectionType"]=None) -> None:
        """Add a global secondary index of table.

        Arguments:
            props: the property of global secondary index.
            partition_key: The attribute of a partition key for the global secondary index.
            read_capacity: The read capacity for the global secondary index. Can only be provided if table billingMode is Provisioned or undefined. Default: 5
            sort_key: The attribute of a sort key for the global secondary index. Default: undefined
            write_capacity: The write capacity for the global secondary index. Can only be provided if table billingMode is Provisioned or undefined. Default: 5
            index_name: The name of the secondary index.
            non_key_attributes: The non-key attributes that are projected into the secondary index. Default: undefined
            projection_type: The set of attributes that are projected into the secondary index. Default: ALL

        Stability:
            stable
        """
        props: GlobalSecondaryIndexProps = {"partitionKey": partition_key, "indexName": index_name}

        if read_capacity is not None:
            props["readCapacity"] = read_capacity

        if sort_key is not None:
            props["sortKey"] = sort_key

        if write_capacity is not None:
            props["writeCapacity"] = write_capacity

        if non_key_attributes is not None:
            props["nonKeyAttributes"] = non_key_attributes

        if projection_type is not None:
            props["projectionType"] = projection_type

        return jsii.invoke(self, "addGlobalSecondaryIndex", [props])

    @jsii.member(jsii_name="addLocalSecondaryIndex")
    def add_local_secondary_index(self, *, sort_key: "Attribute", index_name: str, non_key_attributes: typing.Optional[typing.List[str]]=None, projection_type: typing.Optional["ProjectionType"]=None) -> None:
        """Add a local secondary index of table.

        Arguments:
            props: the property of local secondary index.
            sort_key: The attribute of a sort key for the local secondary index.
            index_name: The name of the secondary index.
            non_key_attributes: The non-key attributes that are projected into the secondary index. Default: undefined
            projection_type: The set of attributes that are projected into the secondary index. Default: ALL

        Stability:
            stable
        """
        props: LocalSecondaryIndexProps = {"sortKey": sort_key, "indexName": index_name}

        if non_key_attributes is not None:
            props["nonKeyAttributes"] = non_key_attributes

        if projection_type is not None:
            props["projectionType"] = projection_type

        return jsii.invoke(self, "addLocalSecondaryIndex", [props])

    @jsii.member(jsii_name="autoScaleGlobalSecondaryIndexReadCapacity")
    def auto_scale_global_secondary_index_read_capacity(self, index_name: str, *, max_capacity: jsii.Number, min_capacity: jsii.Number) -> "IScalableTableAttribute":
        """Enable read capacity scaling for the given GSI.

        Arguments:
            index_name: -
            props: -
            max_capacity: Maximum capacity to scale to.
            min_capacity: Minimum capacity to scale to.

        Returns:
            An object to configure additional AutoScaling settings for this attribute

        Stability:
            stable
        """
        props: EnableScalingProps = {"maxCapacity": max_capacity, "minCapacity": min_capacity}

        return jsii.invoke(self, "autoScaleGlobalSecondaryIndexReadCapacity", [index_name, props])

    @jsii.member(jsii_name="autoScaleGlobalSecondaryIndexWriteCapacity")
    def auto_scale_global_secondary_index_write_capacity(self, index_name: str, *, max_capacity: jsii.Number, min_capacity: jsii.Number) -> "IScalableTableAttribute":
        """Enable write capacity scaling for the given GSI.

        Arguments:
            index_name: -
            props: -
            max_capacity: Maximum capacity to scale to.
            min_capacity: Minimum capacity to scale to.

        Returns:
            An object to configure additional AutoScaling settings for this attribute

        Stability:
            stable
        """
        props: EnableScalingProps = {"maxCapacity": max_capacity, "minCapacity": min_capacity}

        return jsii.invoke(self, "autoScaleGlobalSecondaryIndexWriteCapacity", [index_name, props])

    @jsii.member(jsii_name="autoScaleReadCapacity")
    def auto_scale_read_capacity(self, *, max_capacity: jsii.Number, min_capacity: jsii.Number) -> "IScalableTableAttribute":
        """Enable read capacity scaling for this table.

        Arguments:
            props: -
            max_capacity: Maximum capacity to scale to.
            min_capacity: Minimum capacity to scale to.

        Returns:
            An object to configure additional AutoScaling settings

        Stability:
            stable
        """
        props: EnableScalingProps = {"maxCapacity": max_capacity, "minCapacity": min_capacity}

        return jsii.invoke(self, "autoScaleReadCapacity", [props])

    @jsii.member(jsii_name="autoScaleWriteCapacity")
    def auto_scale_write_capacity(self, *, max_capacity: jsii.Number, min_capacity: jsii.Number) -> "IScalableTableAttribute":
        """Enable write capacity scaling for this table.

        Arguments:
            props: -
            max_capacity: Maximum capacity to scale to.
            min_capacity: Minimum capacity to scale to.

        Returns:
            An object to configure additional AutoScaling settings for this attribute

        Stability:
            stable
        """
        props: EnableScalingProps = {"maxCapacity": max_capacity, "minCapacity": min_capacity}

        return jsii.invoke(self, "autoScaleWriteCapacity", [props])

    @jsii.member(jsii_name="grant")
    def grant(self, grantee: aws_cdk.aws_iam.IGrantable, *actions: str) -> aws_cdk.aws_iam.Grant:
        """Adds an IAM policy statement associated with this table to an IAM principal's policy.

        Arguments:
            grantee: The principal (no-op if undefined).
            actions: The set of actions to allow (i.e. "dynamodb:PutItem", "dynamodb:GetItem", ...).

        Stability:
            stable
        """
        return jsii.invoke(self, "grant", [grantee, *actions])

    @jsii.member(jsii_name="grantFullAccess")
    def grant_full_access(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Permits all DynamoDB operations ("dynamodb:*") to an IAM principal.

        Arguments:
            grantee: The principal to grant access to.

        Stability:
            stable
        """
        return jsii.invoke(self, "grantFullAccess", [grantee])

    @jsii.member(jsii_name="grantReadData")
    def grant_read_data(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Permits an IAM principal all data read operations from this table: BatchGetItem, GetRecords, GetShardIterator, Query, GetItem, Scan.

        Arguments:
            grantee: The principal to grant access to.

        Stability:
            stable
        """
        return jsii.invoke(self, "grantReadData", [grantee])

    @jsii.member(jsii_name="grantReadWriteData")
    def grant_read_write_data(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Permits an IAM principal to all data read/write operations to this table. BatchGetItem, GetRecords, GetShardIterator, Query, GetItem, Scan, BatchWriteItem, PutItem, UpdateItem, DeleteItem.

        Arguments:
            grantee: The principal to grant access to.

        Stability:
            stable
        """
        return jsii.invoke(self, "grantReadWriteData", [grantee])

    @jsii.member(jsii_name="grantStream")
    def grant_stream(self, grantee: aws_cdk.aws_iam.IGrantable, *actions: str) -> aws_cdk.aws_iam.Grant:
        """Adds an IAM policy statement associated with this table's stream to an IAM principal's policy.

        Arguments:
            grantee: The principal (no-op if undefined).
            actions: The set of actions to allow (i.e. "dynamodb:DescribeStream", "dynamodb:GetRecords", ...).

        Stability:
            stable
        """
        return jsii.invoke(self, "grantStream", [grantee, *actions])

    @jsii.member(jsii_name="grantStreamRead")
    def grant_stream_read(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Permis an IAM principal all stream data read operations for this table's stream: DescribeStream, GetRecords, GetShardIterator, ListStreams.

        Arguments:
            grantee: The principal to grant access to.

        Stability:
            stable
        """
        return jsii.invoke(self, "grantStreamRead", [grantee])

    @jsii.member(jsii_name="grantWriteData")
    def grant_write_data(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Permits an IAM principal all data write operations to this table: BatchWriteItem, PutItem, UpdateItem, DeleteItem.

        Arguments:
            grantee: The principal to grant access to.

        Stability:
            stable
        """
        return jsii.invoke(self, "grantWriteData", [grantee])

    @jsii.member(jsii_name="validate")
    def _validate(self) -> typing.List[str]:
        """Validate the table construct.

        Returns:
            an array of validation error message

        Stability:
            stable
        """
        return jsii.invoke(self, "validate", [])

    @property
    @jsii.member(jsii_name="tableArn")
    def table_arn(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "tableArn")

    @property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "tableName")

    @property
    @jsii.member(jsii_name="tableStreamArn")
    def table_stream_arn(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "tableStreamArn")


@jsii.data_type_optionals(jsii_struct_bases=[])
class _TableOptions(jsii.compat.TypedDict, total=False):
    billingMode: "BillingMode"
    """Specify how you are charged for read and write throughput and how you manage capacity.

    Default:
        Provisioned

    Stability:
        stable
    """
    pointInTimeRecovery: bool
    """Whether point-in-time recovery is enabled.

    Default:
        - point-in-time recovery is disabled

    Stability:
        stable
    """
    readCapacity: jsii.Number
    """The read capacity for the table.

    Careful if you add Global Secondary Indexes, as
    those will share the table's provisioned throughput.

    Can only be provided if billingMode is Provisioned.

    Default:
        5

    Stability:
        stable
    """
    removalPolicy: aws_cdk.core.RemovalPolicy
    """The removal policy to apply to the DynamoDB Table.

    Default:
        RemovalPolicy.RETAIN

    Stability:
        stable
    """
    serverSideEncryption: bool
    """Whether server-side encryption with an AWS managed customer master key is enabled.

    Default:
        - server-side encryption is enabled with an AWS owned customer master key

    Stability:
        stable
    """
    sortKey: "Attribute"
    """Table sort key attribute definition.

    Default:
        no sort key

    Stability:
        stable
    """
    stream: "StreamViewType"
    """When an item in the table is modified, StreamViewType determines what information is written to the stream for this table.

    Valid values for StreamViewType are:

    Default:
        undefined, streams are disabled

    Stability:
        stable
    """
    timeToLiveAttribute: str
    """The name of TTL attribute.

    Default:
        - TTL is disabled

    Stability:
        stable
    """
    writeCapacity: jsii.Number
    """The write capacity for the table.

    Careful if you add Global Secondary Indexes, as
    those will share the table's provisioned throughput.

    Can only be provided if billingMode is Provisioned.

    Default:
        5

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-dynamodb.TableOptions", jsii_struct_bases=[_TableOptions])
class TableOptions(_TableOptions):
    """
    Stability:
        stable
    """
    partitionKey: "Attribute"
    """Partition key attribute definition.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-dynamodb.TableProps", jsii_struct_bases=[TableOptions])
class TableProps(TableOptions, jsii.compat.TypedDict, total=False):
    """
    Stability:
        stable
    """
    tableName: str
    """Enforces a particular physical table name.

    Default:
        
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-dynamodb.UtilizationScalingProps", jsii_struct_bases=[aws_cdk.aws_applicationautoscaling.BaseTargetTrackingProps])
class UtilizationScalingProps(aws_cdk.aws_applicationautoscaling.BaseTargetTrackingProps, jsii.compat.TypedDict):
    """Properties for enabling DynamoDB utilization tracking.

    Stability:
        stable
    """
    targetUtilizationPercent: jsii.Number
    """Target utilization percentage for the attribute.

    Stability:
        stable
    """

__all__ = ["Attribute", "AttributeType", "BillingMode", "CfnTable", "CfnTableProps", "EnableScalingProps", "GlobalSecondaryIndexProps", "IScalableTableAttribute", "LocalSecondaryIndexProps", "ProjectionType", "SecondaryIndexProps", "StreamViewType", "Table", "TableOptions", "TableProps", "UtilizationScalingProps", "__jsii_assembly__"]

publication.publish()
