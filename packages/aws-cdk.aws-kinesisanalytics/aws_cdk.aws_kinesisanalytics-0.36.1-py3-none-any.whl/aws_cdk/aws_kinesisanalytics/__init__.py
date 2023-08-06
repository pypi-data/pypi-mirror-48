import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-kinesisanalytics", "0.36.1", __name__, "aws-kinesisanalytics@0.36.1.jsii.tgz")
class CfnApplication(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication"):
    """A CloudFormation ``AWS::KinesisAnalytics::Application``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html
    Stability:
        stable
    cloudformationResource:
        AWS::KinesisAnalytics::Application
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, inputs: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["InputProperty", aws_cdk.core.IResolvable]]], application_code: typing.Optional[str]=None, application_description: typing.Optional[str]=None, application_name: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::KinesisAnalytics::Application``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            inputs: ``AWS::KinesisAnalytics::Application.Inputs``.
            application_code: ``AWS::KinesisAnalytics::Application.ApplicationCode``.
            application_description: ``AWS::KinesisAnalytics::Application.ApplicationDescription``.
            application_name: ``AWS::KinesisAnalytics::Application.ApplicationName``.

        Stability:
            experimental
        """
        props: CfnApplicationProps = {"inputs": inputs}

        if application_code is not None:
            props["applicationCode"] = application_code

        if application_description is not None:
            props["applicationDescription"] = application_description

        if application_name is not None:
            props["applicationName"] = application_name

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

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="inputs")
    def inputs(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["InputProperty", aws_cdk.core.IResolvable]]]:
        """``AWS::KinesisAnalytics::Application.Inputs``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-inputs
        Stability:
            stable
        """
        return jsii.get(self, "inputs")

    @inputs.setter
    def inputs(self, value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["InputProperty", aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "inputs", value)

    @property
    @jsii.member(jsii_name="applicationCode")
    def application_code(self) -> typing.Optional[str]:
        """``AWS::KinesisAnalytics::Application.ApplicationCode``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationcode
        Stability:
            stable
        """
        return jsii.get(self, "applicationCode")

    @application_code.setter
    def application_code(self, value: typing.Optional[str]):
        return jsii.set(self, "applicationCode", value)

    @property
    @jsii.member(jsii_name="applicationDescription")
    def application_description(self) -> typing.Optional[str]:
        """``AWS::KinesisAnalytics::Application.ApplicationDescription``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationdescription
        Stability:
            stable
        """
        return jsii.get(self, "applicationDescription")

    @application_description.setter
    def application_description(self, value: typing.Optional[str]):
        return jsii.set(self, "applicationDescription", value)

    @property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> typing.Optional[str]:
        """``AWS::KinesisAnalytics::Application.ApplicationName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationname
        Stability:
            stable
        """
        return jsii.get(self, "applicationName")

    @application_name.setter
    def application_name(self, value: typing.Optional[str]):
        return jsii.set(self, "applicationName", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.CSVMappingParametersProperty", jsii_struct_bases=[])
    class CSVMappingParametersProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-csvmappingparameters.html
        Stability:
            stable
        """
        recordColumnDelimiter: str
        """``CfnApplication.CSVMappingParametersProperty.RecordColumnDelimiter``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-csvmappingparameters.html#cfn-kinesisanalytics-application-csvmappingparameters-recordcolumndelimiter
        Stability:
            stable
        """

        recordRowDelimiter: str
        """``CfnApplication.CSVMappingParametersProperty.RecordRowDelimiter``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-csvmappingparameters.html#cfn-kinesisanalytics-application-csvmappingparameters-recordrowdelimiter
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.InputLambdaProcessorProperty", jsii_struct_bases=[])
    class InputLambdaProcessorProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html
        Stability:
            stable
        """
        resourceArn: str
        """``CfnApplication.InputLambdaProcessorProperty.ResourceARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html#cfn-kinesisanalytics-application-inputlambdaprocessor-resourcearn
        Stability:
            stable
        """

        roleArn: str
        """``CfnApplication.InputLambdaProcessorProperty.RoleARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputlambdaprocessor.html#cfn-kinesisanalytics-application-inputlambdaprocessor-rolearn
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.InputParallelismProperty", jsii_struct_bases=[])
    class InputParallelismProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputparallelism.html
        Stability:
            stable
        """
        count: jsii.Number
        """``CfnApplication.InputParallelismProperty.Count``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputparallelism.html#cfn-kinesisanalytics-application-inputparallelism-count
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.InputProcessingConfigurationProperty", jsii_struct_bases=[])
    class InputProcessingConfigurationProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputprocessingconfiguration.html
        Stability:
            stable
        """
        inputLambdaProcessor: typing.Union[aws_cdk.core.IResolvable, "CfnApplication.InputLambdaProcessorProperty"]
        """``CfnApplication.InputProcessingConfigurationProperty.InputLambdaProcessor``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputprocessingconfiguration.html#cfn-kinesisanalytics-application-inputprocessingconfiguration-inputlambdaprocessor
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _InputProperty(jsii.compat.TypedDict, total=False):
        inputParallelism: typing.Union[aws_cdk.core.IResolvable, "CfnApplication.InputParallelismProperty"]
        """``CfnApplication.InputProperty.InputParallelism``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-inputparallelism
        Stability:
            stable
        """
        inputProcessingConfiguration: typing.Union[aws_cdk.core.IResolvable, "CfnApplication.InputProcessingConfigurationProperty"]
        """``CfnApplication.InputProperty.InputProcessingConfiguration``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-inputprocessingconfiguration
        Stability:
            stable
        """
        kinesisFirehoseInput: typing.Union[aws_cdk.core.IResolvable, "CfnApplication.KinesisFirehoseInputProperty"]
        """``CfnApplication.InputProperty.KinesisFirehoseInput``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-kinesisfirehoseinput
        Stability:
            stable
        """
        kinesisStreamsInput: typing.Union[aws_cdk.core.IResolvable, "CfnApplication.KinesisStreamsInputProperty"]
        """``CfnApplication.InputProperty.KinesisStreamsInput``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-kinesisstreamsinput
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.InputProperty", jsii_struct_bases=[_InputProperty])
    class InputProperty(_InputProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html
        Stability:
            stable
        """
        inputSchema: typing.Union[aws_cdk.core.IResolvable, "CfnApplication.InputSchemaProperty"]
        """``CfnApplication.InputProperty.InputSchema``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-inputschema
        Stability:
            stable
        """

        namePrefix: str
        """``CfnApplication.InputProperty.NamePrefix``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-input.html#cfn-kinesisanalytics-application-input-nameprefix
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _InputSchemaProperty(jsii.compat.TypedDict, total=False):
        recordEncoding: str
        """``CfnApplication.InputSchemaProperty.RecordEncoding``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html#cfn-kinesisanalytics-application-inputschema-recordencoding
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.InputSchemaProperty", jsii_struct_bases=[_InputSchemaProperty])
    class InputSchemaProperty(_InputSchemaProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html
        Stability:
            stable
        """
        recordColumns: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnApplication.RecordColumnProperty"]]]
        """``CfnApplication.InputSchemaProperty.RecordColumns``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html#cfn-kinesisanalytics-application-inputschema-recordcolumns
        Stability:
            stable
        """

        recordFormat: typing.Union[aws_cdk.core.IResolvable, "CfnApplication.RecordFormatProperty"]
        """``CfnApplication.InputSchemaProperty.RecordFormat``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-inputschema.html#cfn-kinesisanalytics-application-inputschema-recordformat
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.JSONMappingParametersProperty", jsii_struct_bases=[])
    class JSONMappingParametersProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-jsonmappingparameters.html
        Stability:
            stable
        """
        recordRowPath: str
        """``CfnApplication.JSONMappingParametersProperty.RecordRowPath``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-jsonmappingparameters.html#cfn-kinesisanalytics-application-jsonmappingparameters-recordrowpath
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.KinesisFirehoseInputProperty", jsii_struct_bases=[])
    class KinesisFirehoseInputProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisfirehoseinput.html
        Stability:
            stable
        """
        resourceArn: str
        """``CfnApplication.KinesisFirehoseInputProperty.ResourceARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisfirehoseinput.html#cfn-kinesisanalytics-application-kinesisfirehoseinput-resourcearn
        Stability:
            stable
        """

        roleArn: str
        """``CfnApplication.KinesisFirehoseInputProperty.RoleARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisfirehoseinput.html#cfn-kinesisanalytics-application-kinesisfirehoseinput-rolearn
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.KinesisStreamsInputProperty", jsii_struct_bases=[])
    class KinesisStreamsInputProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisstreamsinput.html
        Stability:
            stable
        """
        resourceArn: str
        """``CfnApplication.KinesisStreamsInputProperty.ResourceARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisstreamsinput.html#cfn-kinesisanalytics-application-kinesisstreamsinput-resourcearn
        Stability:
            stable
        """

        roleArn: str
        """``CfnApplication.KinesisStreamsInputProperty.RoleARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-kinesisstreamsinput.html#cfn-kinesisanalytics-application-kinesisstreamsinput-rolearn
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.MappingParametersProperty", jsii_struct_bases=[])
    class MappingParametersProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-mappingparameters.html
        Stability:
            stable
        """
        csvMappingParameters: typing.Union[aws_cdk.core.IResolvable, "CfnApplication.CSVMappingParametersProperty"]
        """``CfnApplication.MappingParametersProperty.CSVMappingParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-mappingparameters.html#cfn-kinesisanalytics-application-mappingparameters-csvmappingparameters
        Stability:
            stable
        """

        jsonMappingParameters: typing.Union[aws_cdk.core.IResolvable, "CfnApplication.JSONMappingParametersProperty"]
        """``CfnApplication.MappingParametersProperty.JSONMappingParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-mappingparameters.html#cfn-kinesisanalytics-application-mappingparameters-jsonmappingparameters
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _RecordColumnProperty(jsii.compat.TypedDict, total=False):
        mapping: str
        """``CfnApplication.RecordColumnProperty.Mapping``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html#cfn-kinesisanalytics-application-recordcolumn-mapping
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.RecordColumnProperty", jsii_struct_bases=[_RecordColumnProperty])
    class RecordColumnProperty(_RecordColumnProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html
        Stability:
            stable
        """
        name: str
        """``CfnApplication.RecordColumnProperty.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html#cfn-kinesisanalytics-application-recordcolumn-name
        Stability:
            stable
        """

        sqlType: str
        """``CfnApplication.RecordColumnProperty.SqlType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordcolumn.html#cfn-kinesisanalytics-application-recordcolumn-sqltype
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _RecordFormatProperty(jsii.compat.TypedDict, total=False):
        mappingParameters: typing.Union[aws_cdk.core.IResolvable, "CfnApplication.MappingParametersProperty"]
        """``CfnApplication.RecordFormatProperty.MappingParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordformat.html#cfn-kinesisanalytics-application-recordformat-mappingparameters
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplication.RecordFormatProperty", jsii_struct_bases=[_RecordFormatProperty])
    class RecordFormatProperty(_RecordFormatProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordformat.html
        Stability:
            stable
        """
        recordFormatType: str
        """``CfnApplication.RecordFormatProperty.RecordFormatType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-application-recordformat.html#cfn-kinesisanalytics-application-recordformat-recordformattype
        Stability:
            stable
        """


class CfnApplicationCloudWatchLoggingOptionV2(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationCloudWatchLoggingOptionV2"):
    """A CloudFormation ``AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html
    Stability:
        stable
    cloudformationResource:
        AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, application_name: str, cloud_watch_logging_option: typing.Union[aws_cdk.core.IResolvable, "CloudWatchLoggingOptionProperty"]) -> None:
        """Create a new ``AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            application_name: ``AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption.ApplicationName``.
            cloud_watch_logging_option: ``AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption.CloudWatchLoggingOption``.

        Stability:
            experimental
        """
        props: CfnApplicationCloudWatchLoggingOptionV2Props = {"applicationName": application_name, "cloudWatchLoggingOption": cloud_watch_logging_option}

        jsii.create(CfnApplicationCloudWatchLoggingOptionV2, self, [scope, id, props])

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
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> str:
        """``AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption.ApplicationName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-applicationname
        Stability:
            stable
        """
        return jsii.get(self, "applicationName")

    @application_name.setter
    def application_name(self, value: str):
        return jsii.set(self, "applicationName", value)

    @property
    @jsii.member(jsii_name="cloudWatchLoggingOption")
    def cloud_watch_logging_option(self) -> typing.Union[aws_cdk.core.IResolvable, "CloudWatchLoggingOptionProperty"]:
        """``AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption.CloudWatchLoggingOption``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption
        Stability:
            stable
        """
        return jsii.get(self, "cloudWatchLoggingOption")

    @cloud_watch_logging_option.setter
    def cloud_watch_logging_option(self, value: typing.Union[aws_cdk.core.IResolvable, "CloudWatchLoggingOptionProperty"]):
        return jsii.set(self, "cloudWatchLoggingOption", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationCloudWatchLoggingOptionV2.CloudWatchLoggingOptionProperty", jsii_struct_bases=[])
    class CloudWatchLoggingOptionProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption.html
        Stability:
            stable
        """
        logStreamArn: str
        """``CfnApplicationCloudWatchLoggingOptionV2.CloudWatchLoggingOptionProperty.LogStreamARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption-logstreamarn
        Stability:
            stable
        """


@jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationCloudWatchLoggingOptionV2Props", jsii_struct_bases=[])
class CfnApplicationCloudWatchLoggingOptionV2Props(jsii.compat.TypedDict):
    """Properties for defining a ``AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html
    Stability:
        stable
    """
    applicationName: str
    """``AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption.ApplicationName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-applicationname
    Stability:
        stable
    """

    cloudWatchLoggingOption: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationCloudWatchLoggingOptionV2.CloudWatchLoggingOptionProperty"]
    """``AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption.CloudWatchLoggingOption``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html#cfn-kinesisanalyticsv2-applicationcloudwatchloggingoption-cloudwatchloggingoption
    Stability:
        stable
    """

class CfnApplicationOutput(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutput"):
    """A CloudFormation ``AWS::KinesisAnalytics::ApplicationOutput``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html
    Stability:
        stable
    cloudformationResource:
        AWS::KinesisAnalytics::ApplicationOutput
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, application_name: str, output: typing.Union[aws_cdk.core.IResolvable, "OutputProperty"]) -> None:
        """Create a new ``AWS::KinesisAnalytics::ApplicationOutput``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            application_name: ``AWS::KinesisAnalytics::ApplicationOutput.ApplicationName``.
            output: ``AWS::KinesisAnalytics::ApplicationOutput.Output``.

        Stability:
            experimental
        """
        props: CfnApplicationOutputProps = {"applicationName": application_name, "output": output}

        jsii.create(CfnApplicationOutput, self, [scope, id, props])

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
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> str:
        """``AWS::KinesisAnalytics::ApplicationOutput.ApplicationName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html#cfn-kinesisanalytics-applicationoutput-applicationname
        Stability:
            stable
        """
        return jsii.get(self, "applicationName")

    @application_name.setter
    def application_name(self, value: str):
        return jsii.set(self, "applicationName", value)

    @property
    @jsii.member(jsii_name="output")
    def output(self) -> typing.Union[aws_cdk.core.IResolvable, "OutputProperty"]:
        """``AWS::KinesisAnalytics::ApplicationOutput.Output``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html#cfn-kinesisanalytics-applicationoutput-output
        Stability:
            stable
        """
        return jsii.get(self, "output")

    @output.setter
    def output(self, value: typing.Union[aws_cdk.core.IResolvable, "OutputProperty"]):
        return jsii.set(self, "output", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutput.DestinationSchemaProperty", jsii_struct_bases=[])
    class DestinationSchemaProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-destinationschema.html
        Stability:
            stable
        """
        recordFormatType: str
        """``CfnApplicationOutput.DestinationSchemaProperty.RecordFormatType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-destinationschema.html#cfn-kinesisanalytics-applicationoutput-destinationschema-recordformattype
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutput.KinesisFirehoseOutputProperty", jsii_struct_bases=[])
    class KinesisFirehoseOutputProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput.html
        Stability:
            stable
        """
        resourceArn: str
        """``CfnApplicationOutput.KinesisFirehoseOutputProperty.ResourceARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput.html#cfn-kinesisanalytics-applicationoutput-kinesisfirehoseoutput-resourcearn
        Stability:
            stable
        """

        roleArn: str
        """``CfnApplicationOutput.KinesisFirehoseOutputProperty.RoleARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisfirehoseoutput.html#cfn-kinesisanalytics-applicationoutput-kinesisfirehoseoutput-rolearn
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutput.KinesisStreamsOutputProperty", jsii_struct_bases=[])
    class KinesisStreamsOutputProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput.html
        Stability:
            stable
        """
        resourceArn: str
        """``CfnApplicationOutput.KinesisStreamsOutputProperty.ResourceARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput.html#cfn-kinesisanalytics-applicationoutput-kinesisstreamsoutput-resourcearn
        Stability:
            stable
        """

        roleArn: str
        """``CfnApplicationOutput.KinesisStreamsOutputProperty.RoleARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-kinesisstreamsoutput.html#cfn-kinesisanalytics-applicationoutput-kinesisstreamsoutput-rolearn
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutput.LambdaOutputProperty", jsii_struct_bases=[])
    class LambdaOutputProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-lambdaoutput.html
        Stability:
            stable
        """
        resourceArn: str
        """``CfnApplicationOutput.LambdaOutputProperty.ResourceARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-lambdaoutput.html#cfn-kinesisanalytics-applicationoutput-lambdaoutput-resourcearn
        Stability:
            stable
        """

        roleArn: str
        """``CfnApplicationOutput.LambdaOutputProperty.RoleARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-lambdaoutput.html#cfn-kinesisanalytics-applicationoutput-lambdaoutput-rolearn
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _OutputProperty(jsii.compat.TypedDict, total=False):
        kinesisFirehoseOutput: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationOutput.KinesisFirehoseOutputProperty"]
        """``CfnApplicationOutput.OutputProperty.KinesisFirehoseOutput``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-kinesisfirehoseoutput
        Stability:
            stable
        """
        kinesisStreamsOutput: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationOutput.KinesisStreamsOutputProperty"]
        """``CfnApplicationOutput.OutputProperty.KinesisStreamsOutput``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-kinesisstreamsoutput
        Stability:
            stable
        """
        lambdaOutput: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationOutput.LambdaOutputProperty"]
        """``CfnApplicationOutput.OutputProperty.LambdaOutput``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-lambdaoutput
        Stability:
            stable
        """
        name: str
        """``CfnApplicationOutput.OutputProperty.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-name
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutput.OutputProperty", jsii_struct_bases=[_OutputProperty])
    class OutputProperty(_OutputProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html
        Stability:
            stable
        """
        destinationSchema: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationOutput.DestinationSchemaProperty"]
        """``CfnApplicationOutput.OutputProperty.DestinationSchema``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationoutput-output.html#cfn-kinesisanalytics-applicationoutput-output-destinationschema
        Stability:
            stable
        """


@jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutputProps", jsii_struct_bases=[])
class CfnApplicationOutputProps(jsii.compat.TypedDict):
    """Properties for defining a ``AWS::KinesisAnalytics::ApplicationOutput``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html
    Stability:
        stable
    """
    applicationName: str
    """``AWS::KinesisAnalytics::ApplicationOutput.ApplicationName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html#cfn-kinesisanalytics-applicationoutput-applicationname
    Stability:
        stable
    """

    output: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationOutput.OutputProperty"]
    """``AWS::KinesisAnalytics::ApplicationOutput.Output``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html#cfn-kinesisanalytics-applicationoutput-output
    Stability:
        stable
    """

class CfnApplicationOutputV2(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutputV2"):
    """A CloudFormation ``AWS::KinesisAnalyticsV2::ApplicationOutput``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html
    Stability:
        stable
    cloudformationResource:
        AWS::KinesisAnalyticsV2::ApplicationOutput
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, application_name: str, output: typing.Union[aws_cdk.core.IResolvable, "OutputProperty"]) -> None:
        """Create a new ``AWS::KinesisAnalyticsV2::ApplicationOutput``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            application_name: ``AWS::KinesisAnalyticsV2::ApplicationOutput.ApplicationName``.
            output: ``AWS::KinesisAnalyticsV2::ApplicationOutput.Output``.

        Stability:
            experimental
        """
        props: CfnApplicationOutputV2Props = {"applicationName": application_name, "output": output}

        jsii.create(CfnApplicationOutputV2, self, [scope, id, props])

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
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> str:
        """``AWS::KinesisAnalyticsV2::ApplicationOutput.ApplicationName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html#cfn-kinesisanalyticsv2-applicationoutput-applicationname
        Stability:
            stable
        """
        return jsii.get(self, "applicationName")

    @application_name.setter
    def application_name(self, value: str):
        return jsii.set(self, "applicationName", value)

    @property
    @jsii.member(jsii_name="output")
    def output(self) -> typing.Union[aws_cdk.core.IResolvable, "OutputProperty"]:
        """``AWS::KinesisAnalyticsV2::ApplicationOutput.Output``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html#cfn-kinesisanalyticsv2-applicationoutput-output
        Stability:
            stable
        """
        return jsii.get(self, "output")

    @output.setter
    def output(self, value: typing.Union[aws_cdk.core.IResolvable, "OutputProperty"]):
        return jsii.set(self, "output", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutputV2.DestinationSchemaProperty", jsii_struct_bases=[])
    class DestinationSchemaProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-destinationschema.html
        Stability:
            stable
        """
        recordFormatType: str
        """``CfnApplicationOutputV2.DestinationSchemaProperty.RecordFormatType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-destinationschema.html#cfn-kinesisanalyticsv2-applicationoutput-destinationschema-recordformattype
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutputV2.KinesisFirehoseOutputProperty", jsii_struct_bases=[])
    class KinesisFirehoseOutputProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisfirehoseoutput.html
        Stability:
            stable
        """
        resourceArn: str
        """``CfnApplicationOutputV2.KinesisFirehoseOutputProperty.ResourceARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisfirehoseoutput.html#cfn-kinesisanalyticsv2-applicationoutput-kinesisfirehoseoutput-resourcearn
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutputV2.KinesisStreamsOutputProperty", jsii_struct_bases=[])
    class KinesisStreamsOutputProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput.html
        Stability:
            stable
        """
        resourceArn: str
        """``CfnApplicationOutputV2.KinesisStreamsOutputProperty.ResourceARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput.html#cfn-kinesisanalyticsv2-applicationoutput-kinesisstreamsoutput-resourcearn
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutputV2.LambdaOutputProperty", jsii_struct_bases=[])
    class LambdaOutputProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-lambdaoutput.html
        Stability:
            stable
        """
        resourceArn: str
        """``CfnApplicationOutputV2.LambdaOutputProperty.ResourceARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-lambdaoutput.html#cfn-kinesisanalyticsv2-applicationoutput-lambdaoutput-resourcearn
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _OutputProperty(jsii.compat.TypedDict, total=False):
        kinesisFirehoseOutput: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationOutputV2.KinesisFirehoseOutputProperty"]
        """``CfnApplicationOutputV2.OutputProperty.KinesisFirehoseOutput``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-kinesisfirehoseoutput
        Stability:
            stable
        """
        kinesisStreamsOutput: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationOutputV2.KinesisStreamsOutputProperty"]
        """``CfnApplicationOutputV2.OutputProperty.KinesisStreamsOutput``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-kinesisstreamsoutput
        Stability:
            stable
        """
        lambdaOutput: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationOutputV2.LambdaOutputProperty"]
        """``CfnApplicationOutputV2.OutputProperty.LambdaOutput``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-lambdaoutput
        Stability:
            stable
        """
        name: str
        """``CfnApplicationOutputV2.OutputProperty.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-name
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutputV2.OutputProperty", jsii_struct_bases=[_OutputProperty])
    class OutputProperty(_OutputProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html
        Stability:
            stable
        """
        destinationSchema: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationOutputV2.DestinationSchemaProperty"]
        """``CfnApplicationOutputV2.OutputProperty.DestinationSchema``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationoutput-output.html#cfn-kinesisanalyticsv2-applicationoutput-output-destinationschema
        Stability:
            stable
        """


@jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationOutputV2Props", jsii_struct_bases=[])
class CfnApplicationOutputV2Props(jsii.compat.TypedDict):
    """Properties for defining a ``AWS::KinesisAnalyticsV2::ApplicationOutput``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html
    Stability:
        stable
    """
    applicationName: str
    """``AWS::KinesisAnalyticsV2::ApplicationOutput.ApplicationName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html#cfn-kinesisanalyticsv2-applicationoutput-applicationname
    Stability:
        stable
    """

    output: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationOutputV2.OutputProperty"]
    """``AWS::KinesisAnalyticsV2::ApplicationOutput.Output``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html#cfn-kinesisanalyticsv2-applicationoutput-output
    Stability:
        stable
    """

@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnApplicationProps(jsii.compat.TypedDict, total=False):
    applicationCode: str
    """``AWS::KinesisAnalytics::Application.ApplicationCode``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationcode
    Stability:
        stable
    """
    applicationDescription: str
    """``AWS::KinesisAnalytics::Application.ApplicationDescription``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationdescription
    Stability:
        stable
    """
    applicationName: str
    """``AWS::KinesisAnalytics::Application.ApplicationName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-applicationname
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationProps", jsii_struct_bases=[_CfnApplicationProps])
class CfnApplicationProps(_CfnApplicationProps):
    """Properties for defining a ``AWS::KinesisAnalytics::Application``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html
    Stability:
        stable
    """
    inputs: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnApplication.InputProperty", aws_cdk.core.IResolvable]]]
    """``AWS::KinesisAnalytics::Application.Inputs``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html#cfn-kinesisanalytics-application-inputs
    Stability:
        stable
    """

class CfnApplicationReferenceDataSource(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSource"):
    """A CloudFormation ``AWS::KinesisAnalytics::ApplicationReferenceDataSource``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html
    Stability:
        stable
    cloudformationResource:
        AWS::KinesisAnalytics::ApplicationReferenceDataSource
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, application_name: str, reference_data_source: typing.Union[aws_cdk.core.IResolvable, "ReferenceDataSourceProperty"]) -> None:
        """Create a new ``AWS::KinesisAnalytics::ApplicationReferenceDataSource``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            application_name: ``AWS::KinesisAnalytics::ApplicationReferenceDataSource.ApplicationName``.
            reference_data_source: ``AWS::KinesisAnalytics::ApplicationReferenceDataSource.ReferenceDataSource``.

        Stability:
            experimental
        """
        props: CfnApplicationReferenceDataSourceProps = {"applicationName": application_name, "referenceDataSource": reference_data_source}

        jsii.create(CfnApplicationReferenceDataSource, self, [scope, id, props])

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
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> str:
        """``AWS::KinesisAnalytics::ApplicationReferenceDataSource.ApplicationName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-applicationname
        Stability:
            stable
        """
        return jsii.get(self, "applicationName")

    @application_name.setter
    def application_name(self, value: str):
        return jsii.set(self, "applicationName", value)

    @property
    @jsii.member(jsii_name="referenceDataSource")
    def reference_data_source(self) -> typing.Union[aws_cdk.core.IResolvable, "ReferenceDataSourceProperty"]:
        """``AWS::KinesisAnalytics::ApplicationReferenceDataSource.ReferenceDataSource``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource
        Stability:
            stable
        """
        return jsii.get(self, "referenceDataSource")

    @reference_data_source.setter
    def reference_data_source(self, value: typing.Union[aws_cdk.core.IResolvable, "ReferenceDataSourceProperty"]):
        return jsii.set(self, "referenceDataSource", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSource.CSVMappingParametersProperty", jsii_struct_bases=[])
    class CSVMappingParametersProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters.html
        Stability:
            stable
        """
        recordColumnDelimiter: str
        """``CfnApplicationReferenceDataSource.CSVMappingParametersProperty.RecordColumnDelimiter``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-csvmappingparameters-recordcolumndelimiter
        Stability:
            stable
        """

        recordRowDelimiter: str
        """``CfnApplicationReferenceDataSource.CSVMappingParametersProperty.RecordRowDelimiter``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-csvmappingparameters-recordrowdelimiter
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSource.JSONMappingParametersProperty", jsii_struct_bases=[])
    class JSONMappingParametersProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-jsonmappingparameters.html
        Stability:
            stable
        """
        recordRowPath: str
        """``CfnApplicationReferenceDataSource.JSONMappingParametersProperty.RecordRowPath``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-jsonmappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-jsonmappingparameters-recordrowpath
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSource.MappingParametersProperty", jsii_struct_bases=[])
    class MappingParametersProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-mappingparameters.html
        Stability:
            stable
        """
        csvMappingParameters: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationReferenceDataSource.CSVMappingParametersProperty"]
        """``CfnApplicationReferenceDataSource.MappingParametersProperty.CSVMappingParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-mappingparameters-csvmappingparameters
        Stability:
            stable
        """

        jsonMappingParameters: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationReferenceDataSource.JSONMappingParametersProperty"]
        """``CfnApplicationReferenceDataSource.MappingParametersProperty.JSONMappingParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalytics-applicationreferencedatasource-mappingparameters-jsonmappingparameters
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _RecordColumnProperty(jsii.compat.TypedDict, total=False):
        mapping: str
        """``CfnApplicationReferenceDataSource.RecordColumnProperty.Mapping``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-mapping
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSource.RecordColumnProperty", jsii_struct_bases=[_RecordColumnProperty])
    class RecordColumnProperty(_RecordColumnProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html
        Stability:
            stable
        """
        name: str
        """``CfnApplicationReferenceDataSource.RecordColumnProperty.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-name
        Stability:
            stable
        """

        sqlType: str
        """``CfnApplicationReferenceDataSource.RecordColumnProperty.SqlType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalytics-applicationreferencedatasource-recordcolumn-sqltype
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _RecordFormatProperty(jsii.compat.TypedDict, total=False):
        mappingParameters: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationReferenceDataSource.MappingParametersProperty"]
        """``CfnApplicationReferenceDataSource.RecordFormatProperty.MappingParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordformat.html#cfn-kinesisanalytics-applicationreferencedatasource-recordformat-mappingparameters
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSource.RecordFormatProperty", jsii_struct_bases=[_RecordFormatProperty])
    class RecordFormatProperty(_RecordFormatProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordformat.html
        Stability:
            stable
        """
        recordFormatType: str
        """``CfnApplicationReferenceDataSource.RecordFormatProperty.RecordFormatType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-recordformat.html#cfn-kinesisanalytics-applicationreferencedatasource-recordformat-recordformattype
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _ReferenceDataSourceProperty(jsii.compat.TypedDict, total=False):
        s3ReferenceDataSource: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty"]
        """``CfnApplicationReferenceDataSource.ReferenceDataSourceProperty.S3ReferenceDataSource``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource-s3referencedatasource
        Stability:
            stable
        """
        tableName: str
        """``CfnApplicationReferenceDataSource.ReferenceDataSourceProperty.TableName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource-tablename
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSource.ReferenceDataSourceProperty", jsii_struct_bases=[_ReferenceDataSourceProperty])
    class ReferenceDataSourceProperty(_ReferenceDataSourceProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html
        Stability:
            stable
        """
        referenceSchema: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationReferenceDataSource.ReferenceSchemaProperty"]
        """``CfnApplicationReferenceDataSource.ReferenceDataSourceProperty.ReferenceSchema``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource-referenceschema
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _ReferenceSchemaProperty(jsii.compat.TypedDict, total=False):
        recordEncoding: str
        """``CfnApplicationReferenceDataSource.ReferenceSchemaProperty.RecordEncoding``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordencoding
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSource.ReferenceSchemaProperty", jsii_struct_bases=[_ReferenceSchemaProperty])
    class ReferenceSchemaProperty(_ReferenceSchemaProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html
        Stability:
            stable
        """
        recordColumns: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnApplicationReferenceDataSource.RecordColumnProperty"]]]
        """``CfnApplicationReferenceDataSource.ReferenceSchemaProperty.RecordColumns``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordcolumns
        Stability:
            stable
        """

        recordFormat: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationReferenceDataSource.RecordFormatProperty"]
        """``CfnApplicationReferenceDataSource.ReferenceSchemaProperty.RecordFormat``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalytics-applicationreferencedatasource-referenceschema-recordformat
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty", jsii_struct_bases=[])
    class S3ReferenceDataSourceProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html
        Stability:
            stable
        """
        bucketArn: str
        """``CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty.BucketARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-s3referencedatasource-bucketarn
        Stability:
            stable
        """

        fileKey: str
        """``CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty.FileKey``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-s3referencedatasource-filekey
        Stability:
            stable
        """

        referenceRoleArn: str
        """``CfnApplicationReferenceDataSource.S3ReferenceDataSourceProperty.ReferenceRoleARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalytics-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-s3referencedatasource-referencerolearn
        Stability:
            stable
        """


@jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceProps", jsii_struct_bases=[])
class CfnApplicationReferenceDataSourceProps(jsii.compat.TypedDict):
    """Properties for defining a ``AWS::KinesisAnalytics::ApplicationReferenceDataSource``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html
    Stability:
        stable
    """
    applicationName: str
    """``AWS::KinesisAnalytics::ApplicationReferenceDataSource.ApplicationName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-applicationname
    Stability:
        stable
    """

    referenceDataSource: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationReferenceDataSource.ReferenceDataSourceProperty"]
    """``AWS::KinesisAnalytics::ApplicationReferenceDataSource.ReferenceDataSource``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html#cfn-kinesisanalytics-applicationreferencedatasource-referencedatasource
    Stability:
        stable
    """

class CfnApplicationReferenceDataSourceV2(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceV2"):
    """A CloudFormation ``AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html
    Stability:
        stable
    cloudformationResource:
        AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, application_name: str, reference_data_source: typing.Union[aws_cdk.core.IResolvable, "ReferenceDataSourceProperty"]) -> None:
        """Create a new ``AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            application_name: ``AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.ApplicationName``.
            reference_data_source: ``AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.ReferenceDataSource``.

        Stability:
            experimental
        """
        props: CfnApplicationReferenceDataSourceV2Props = {"applicationName": application_name, "referenceDataSource": reference_data_source}

        jsii.create(CfnApplicationReferenceDataSourceV2, self, [scope, id, props])

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
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> str:
        """``AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.ApplicationName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-applicationname
        Stability:
            stable
        """
        return jsii.get(self, "applicationName")

    @application_name.setter
    def application_name(self, value: str):
        return jsii.set(self, "applicationName", value)

    @property
    @jsii.member(jsii_name="referenceDataSource")
    def reference_data_source(self) -> typing.Union[aws_cdk.core.IResolvable, "ReferenceDataSourceProperty"]:
        """``AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.ReferenceDataSource``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource
        Stability:
            stable
        """
        return jsii.get(self, "referenceDataSource")

    @reference_data_source.setter
    def reference_data_source(self, value: typing.Union[aws_cdk.core.IResolvable, "ReferenceDataSourceProperty"]):
        return jsii.set(self, "referenceDataSource", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceV2.CSVMappingParametersProperty", jsii_struct_bases=[])
    class CSVMappingParametersProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters.html
        Stability:
            stable
        """
        recordColumnDelimiter: str
        """``CfnApplicationReferenceDataSourceV2.CSVMappingParametersProperty.RecordColumnDelimiter``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters-recordcolumndelimiter
        Stability:
            stable
        """

        recordRowDelimiter: str
        """``CfnApplicationReferenceDataSourceV2.CSVMappingParametersProperty.RecordRowDelimiter``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-csvmappingparameters-recordrowdelimiter
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceV2.JSONMappingParametersProperty", jsii_struct_bases=[])
    class JSONMappingParametersProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters.html
        Stability:
            stable
        """
        recordRowPath: str
        """``CfnApplicationReferenceDataSourceV2.JSONMappingParametersProperty.RecordRowPath``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-jsonmappingparameters-recordrowpath
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceV2.MappingParametersProperty", jsii_struct_bases=[])
    class MappingParametersProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html
        Stability:
            stable
        """
        csvMappingParameters: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationReferenceDataSourceV2.CSVMappingParametersProperty"]
        """``CfnApplicationReferenceDataSourceV2.MappingParametersProperty.CSVMappingParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters-csvmappingparameters
        Stability:
            stable
        """

        jsonMappingParameters: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationReferenceDataSourceV2.JSONMappingParametersProperty"]
        """``CfnApplicationReferenceDataSourceV2.MappingParametersProperty.JSONMappingParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-mappingparameters-jsonmappingparameters
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _RecordColumnProperty(jsii.compat.TypedDict, total=False):
        mapping: str
        """``CfnApplicationReferenceDataSourceV2.RecordColumnProperty.Mapping``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-mapping
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceV2.RecordColumnProperty", jsii_struct_bases=[_RecordColumnProperty])
    class RecordColumnProperty(_RecordColumnProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html
        Stability:
            stable
        """
        name: str
        """``CfnApplicationReferenceDataSourceV2.RecordColumnProperty.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-name
        Stability:
            stable
        """

        sqlType: str
        """``CfnApplicationReferenceDataSourceV2.RecordColumnProperty.SqlType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordcolumn-sqltype
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _RecordFormatProperty(jsii.compat.TypedDict, total=False):
        mappingParameters: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationReferenceDataSourceV2.MappingParametersProperty"]
        """``CfnApplicationReferenceDataSourceV2.RecordFormatProperty.MappingParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordformat.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordformat-mappingparameters
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceV2.RecordFormatProperty", jsii_struct_bases=[_RecordFormatProperty])
    class RecordFormatProperty(_RecordFormatProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordformat.html
        Stability:
            stable
        """
        recordFormatType: str
        """``CfnApplicationReferenceDataSourceV2.RecordFormatProperty.RecordFormatType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-recordformat.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-recordformat-recordformattype
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _ReferenceDataSourceProperty(jsii.compat.TypedDict, total=False):
        s3ReferenceDataSource: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationReferenceDataSourceV2.S3ReferenceDataSourceProperty"]
        """``CfnApplicationReferenceDataSourceV2.ReferenceDataSourceProperty.S3ReferenceDataSource``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-s3referencedatasource
        Stability:
            stable
        """
        tableName: str
        """``CfnApplicationReferenceDataSourceV2.ReferenceDataSourceProperty.TableName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-tablename
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceV2.ReferenceDataSourceProperty", jsii_struct_bases=[_ReferenceDataSourceProperty])
    class ReferenceDataSourceProperty(_ReferenceDataSourceProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html
        Stability:
            stable
        """
        referenceSchema: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationReferenceDataSourceV2.ReferenceSchemaProperty"]
        """``CfnApplicationReferenceDataSourceV2.ReferenceDataSourceProperty.ReferenceSchema``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource-referenceschema
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _ReferenceSchemaProperty(jsii.compat.TypedDict, total=False):
        recordEncoding: str
        """``CfnApplicationReferenceDataSourceV2.ReferenceSchemaProperty.RecordEncoding``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordencoding
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceV2.ReferenceSchemaProperty", jsii_struct_bases=[_ReferenceSchemaProperty])
    class ReferenceSchemaProperty(_ReferenceSchemaProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html
        Stability:
            stable
        """
        recordColumns: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnApplicationReferenceDataSourceV2.RecordColumnProperty"]]]
        """``CfnApplicationReferenceDataSourceV2.ReferenceSchemaProperty.RecordColumns``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordcolumns
        Stability:
            stable
        """

        recordFormat: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationReferenceDataSourceV2.RecordFormatProperty"]
        """``CfnApplicationReferenceDataSourceV2.ReferenceSchemaProperty.RecordFormat``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-referenceschema.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referenceschema-recordformat
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceV2.S3ReferenceDataSourceProperty", jsii_struct_bases=[])
    class S3ReferenceDataSourceProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource.html
        Stability:
            stable
        """
        bucketArn: str
        """``CfnApplicationReferenceDataSourceV2.S3ReferenceDataSourceProperty.BucketARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-bucketarn
        Stability:
            stable
        """

        fileKey: str
        """``CfnApplicationReferenceDataSourceV2.S3ReferenceDataSourceProperty.FileKey``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-s3referencedatasource-filekey
        Stability:
            stable
        """


@jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationReferenceDataSourceV2Props", jsii_struct_bases=[])
class CfnApplicationReferenceDataSourceV2Props(jsii.compat.TypedDict):
    """Properties for defining a ``AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html
    Stability:
        stable
    """
    applicationName: str
    """``AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.ApplicationName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-applicationname
    Stability:
        stable
    """

    referenceDataSource: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationReferenceDataSourceV2.ReferenceDataSourceProperty"]
    """``AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource.ReferenceDataSource``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html#cfn-kinesisanalyticsv2-applicationreferencedatasource-referencedatasource
    Stability:
        stable
    """

class CfnApplicationV2(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2"):
    """A CloudFormation ``AWS::KinesisAnalyticsV2::Application``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html
    Stability:
        stable
    cloudformationResource:
        AWS::KinesisAnalyticsV2::Application
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, runtime_environment: str, service_execution_role: str, application_configuration: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ApplicationConfigurationProperty"]]]=None, application_description: typing.Optional[str]=None, application_name: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::KinesisAnalyticsV2::Application``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            runtime_environment: ``AWS::KinesisAnalyticsV2::Application.RuntimeEnvironment``.
            service_execution_role: ``AWS::KinesisAnalyticsV2::Application.ServiceExecutionRole``.
            application_configuration: ``AWS::KinesisAnalyticsV2::Application.ApplicationConfiguration``.
            application_description: ``AWS::KinesisAnalyticsV2::Application.ApplicationDescription``.
            application_name: ``AWS::KinesisAnalyticsV2::Application.ApplicationName``.

        Stability:
            experimental
        """
        props: CfnApplicationV2Props = {"runtimeEnvironment": runtime_environment, "serviceExecutionRole": service_execution_role}

        if application_configuration is not None:
            props["applicationConfiguration"] = application_configuration

        if application_description is not None:
            props["applicationDescription"] = application_description

        if application_name is not None:
            props["applicationName"] = application_name

        jsii.create(CfnApplicationV2, self, [scope, id, props])

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
    @jsii.member(jsii_name="runtimeEnvironment")
    def runtime_environment(self) -> str:
        """``AWS::KinesisAnalyticsV2::Application.RuntimeEnvironment``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-runtimeenvironment
        Stability:
            stable
        """
        return jsii.get(self, "runtimeEnvironment")

    @runtime_environment.setter
    def runtime_environment(self, value: str):
        return jsii.set(self, "runtimeEnvironment", value)

    @property
    @jsii.member(jsii_name="serviceExecutionRole")
    def service_execution_role(self) -> str:
        """``AWS::KinesisAnalyticsV2::Application.ServiceExecutionRole``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-serviceexecutionrole
        Stability:
            stable
        """
        return jsii.get(self, "serviceExecutionRole")

    @service_execution_role.setter
    def service_execution_role(self, value: str):
        return jsii.set(self, "serviceExecutionRole", value)

    @property
    @jsii.member(jsii_name="applicationConfiguration")
    def application_configuration(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ApplicationConfigurationProperty"]]]:
        """``AWS::KinesisAnalyticsV2::Application.ApplicationConfiguration``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationconfiguration
        Stability:
            stable
        """
        return jsii.get(self, "applicationConfiguration")

    @application_configuration.setter
    def application_configuration(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ApplicationConfigurationProperty"]]]):
        return jsii.set(self, "applicationConfiguration", value)

    @property
    @jsii.member(jsii_name="applicationDescription")
    def application_description(self) -> typing.Optional[str]:
        """``AWS::KinesisAnalyticsV2::Application.ApplicationDescription``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationdescription
        Stability:
            stable
        """
        return jsii.get(self, "applicationDescription")

    @application_description.setter
    def application_description(self, value: typing.Optional[str]):
        return jsii.set(self, "applicationDescription", value)

    @property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> typing.Optional[str]:
        """``AWS::KinesisAnalyticsV2::Application.ApplicationName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationname
        Stability:
            stable
        """
        return jsii.get(self, "applicationName")

    @application_name.setter
    def application_name(self, value: typing.Optional[str]):
        return jsii.set(self, "applicationName", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.ApplicationCodeConfigurationProperty", jsii_struct_bases=[])
    class ApplicationCodeConfigurationProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html
        Stability:
            stable
        """
        codeContent: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.CodeContentProperty"]
        """``CfnApplicationV2.ApplicationCodeConfigurationProperty.CodeContent``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html#cfn-kinesisanalyticsv2-application-applicationcodeconfiguration-codecontent
        Stability:
            stable
        """

        codeContentType: str
        """``CfnApplicationV2.ApplicationCodeConfigurationProperty.CodeContentType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationcodeconfiguration.html#cfn-kinesisanalyticsv2-application-applicationcodeconfiguration-codecontenttype
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.ApplicationConfigurationProperty", jsii_struct_bases=[])
    class ApplicationConfigurationProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html
        Stability:
            stable
        """
        applicationCodeConfiguration: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.ApplicationCodeConfigurationProperty"]
        """``CfnApplicationV2.ApplicationConfigurationProperty.ApplicationCodeConfiguration``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationcodeconfiguration
        Stability:
            stable
        """

        applicationSnapshotConfiguration: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.ApplicationSnapshotConfigurationProperty"]
        """``CfnApplicationV2.ApplicationConfigurationProperty.ApplicationSnapshotConfiguration``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-applicationsnapshotconfiguration
        Stability:
            stable
        """

        environmentProperties: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.EnvironmentPropertiesProperty"]
        """``CfnApplicationV2.ApplicationConfigurationProperty.EnvironmentProperties``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-environmentproperties
        Stability:
            stable
        """

        flinkApplicationConfiguration: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.FlinkApplicationConfigurationProperty"]
        """``CfnApplicationV2.ApplicationConfigurationProperty.FlinkApplicationConfiguration``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-flinkapplicationconfiguration
        Stability:
            stable
        """

        sqlApplicationConfiguration: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.SqlApplicationConfigurationProperty"]
        """``CfnApplicationV2.ApplicationConfigurationProperty.SqlApplicationConfiguration``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationconfiguration.html#cfn-kinesisanalyticsv2-application-applicationconfiguration-sqlapplicationconfiguration
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.ApplicationSnapshotConfigurationProperty", jsii_struct_bases=[])
    class ApplicationSnapshotConfigurationProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration.html
        Stability:
            stable
        """
        snapshotsEnabled: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnApplicationV2.ApplicationSnapshotConfigurationProperty.SnapshotsEnabled``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration.html#cfn-kinesisanalyticsv2-application-applicationsnapshotconfiguration-snapshotsenabled
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.CSVMappingParametersProperty", jsii_struct_bases=[])
    class CSVMappingParametersProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html
        Stability:
            stable
        """
        recordColumnDelimiter: str
        """``CfnApplicationV2.CSVMappingParametersProperty.RecordColumnDelimiter``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html#cfn-kinesisanalyticsv2-application-csvmappingparameters-recordcolumndelimiter
        Stability:
            stable
        """

        recordRowDelimiter: str
        """``CfnApplicationV2.CSVMappingParametersProperty.RecordRowDelimiter``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-csvmappingparameters.html#cfn-kinesisanalyticsv2-application-csvmappingparameters-recordrowdelimiter
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _CheckpointConfigurationProperty(jsii.compat.TypedDict, total=False):
        checkpointingEnabled: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnApplicationV2.CheckpointConfigurationProperty.CheckpointingEnabled``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-checkpointingenabled
        Stability:
            stable
        """
        checkpointInterval: jsii.Number
        """``CfnApplicationV2.CheckpointConfigurationProperty.CheckpointInterval``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-checkpointinterval
        Stability:
            stable
        """
        minPauseBetweenCheckpoints: jsii.Number
        """``CfnApplicationV2.CheckpointConfigurationProperty.MinPauseBetweenCheckpoints``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-minpausebetweencheckpoints
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.CheckpointConfigurationProperty", jsii_struct_bases=[_CheckpointConfigurationProperty])
    class CheckpointConfigurationProperty(_CheckpointConfigurationProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html
        Stability:
            stable
        """
        configurationType: str
        """``CfnApplicationV2.CheckpointConfigurationProperty.ConfigurationType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-checkpointconfiguration.html#cfn-kinesisanalyticsv2-application-checkpointconfiguration-configurationtype
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.CodeContentProperty", jsii_struct_bases=[])
    class CodeContentProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html
        Stability:
            stable
        """
        s3ContentLocation: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.S3ContentLocationProperty"]
        """``CfnApplicationV2.CodeContentProperty.S3ContentLocation``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-s3contentlocation
        Stability:
            stable
        """

        textContent: str
        """``CfnApplicationV2.CodeContentProperty.TextContent``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-textcontent
        Stability:
            stable
        """

        zipFileContent: str
        """``CfnApplicationV2.CodeContentProperty.ZipFileContent``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-codecontent.html#cfn-kinesisanalyticsv2-application-codecontent-zipfilecontent
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.EnvironmentPropertiesProperty", jsii_struct_bases=[])
    class EnvironmentPropertiesProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-environmentproperties.html
        Stability:
            stable
        """
        propertyGroups: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.PropertyGroupProperty"]]]
        """``CfnApplicationV2.EnvironmentPropertiesProperty.PropertyGroups``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-environmentproperties.html#cfn-kinesisanalyticsv2-application-environmentproperties-propertygroups
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.FlinkApplicationConfigurationProperty", jsii_struct_bases=[])
    class FlinkApplicationConfigurationProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html
        Stability:
            stable
        """
        checkpointConfiguration: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.CheckpointConfigurationProperty"]
        """``CfnApplicationV2.FlinkApplicationConfigurationProperty.CheckpointConfiguration``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-checkpointconfiguration
        Stability:
            stable
        """

        monitoringConfiguration: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.MonitoringConfigurationProperty"]
        """``CfnApplicationV2.FlinkApplicationConfigurationProperty.MonitoringConfiguration``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-monitoringconfiguration
        Stability:
            stable
        """

        parallelismConfiguration: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.ParallelismConfigurationProperty"]
        """``CfnApplicationV2.FlinkApplicationConfigurationProperty.ParallelismConfiguration``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-flinkapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-flinkapplicationconfiguration-parallelismconfiguration
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.InputLambdaProcessorProperty", jsii_struct_bases=[])
    class InputLambdaProcessorProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor.html
        Stability:
            stable
        """
        resourceArn: str
        """``CfnApplicationV2.InputLambdaProcessorProperty.ResourceARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputlambdaprocessor.html#cfn-kinesisanalyticsv2-application-inputlambdaprocessor-resourcearn
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.InputParallelismProperty", jsii_struct_bases=[])
    class InputParallelismProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputparallelism.html
        Stability:
            stable
        """
        count: jsii.Number
        """``CfnApplicationV2.InputParallelismProperty.Count``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputparallelism.html#cfn-kinesisanalyticsv2-application-inputparallelism-count
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.InputProcessingConfigurationProperty", jsii_struct_bases=[])
    class InputProcessingConfigurationProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration.html
        Stability:
            stable
        """
        inputLambdaProcessor: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.InputLambdaProcessorProperty"]
        """``CfnApplicationV2.InputProcessingConfigurationProperty.InputLambdaProcessor``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputprocessingconfiguration.html#cfn-kinesisanalyticsv2-application-inputprocessingconfiguration-inputlambdaprocessor
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _InputProperty(jsii.compat.TypedDict, total=False):
        inputParallelism: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.InputParallelismProperty"]
        """``CfnApplicationV2.InputProperty.InputParallelism``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputparallelism
        Stability:
            stable
        """
        inputProcessingConfiguration: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.InputProcessingConfigurationProperty"]
        """``CfnApplicationV2.InputProperty.InputProcessingConfiguration``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputprocessingconfiguration
        Stability:
            stable
        """
        kinesisFirehoseInput: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.KinesisFirehoseInputProperty"]
        """``CfnApplicationV2.InputProperty.KinesisFirehoseInput``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-kinesisfirehoseinput
        Stability:
            stable
        """
        kinesisStreamsInput: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.KinesisStreamsInputProperty"]
        """``CfnApplicationV2.InputProperty.KinesisStreamsInput``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-kinesisstreamsinput
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.InputProperty", jsii_struct_bases=[_InputProperty])
    class InputProperty(_InputProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html
        Stability:
            stable
        """
        inputSchema: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.InputSchemaProperty"]
        """``CfnApplicationV2.InputProperty.InputSchema``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-inputschema
        Stability:
            stable
        """

        namePrefix: str
        """``CfnApplicationV2.InputProperty.NamePrefix``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-input.html#cfn-kinesisanalyticsv2-application-input-nameprefix
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _InputSchemaProperty(jsii.compat.TypedDict, total=False):
        recordEncoding: str
        """``CfnApplicationV2.InputSchemaProperty.RecordEncoding``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordencoding
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.InputSchemaProperty", jsii_struct_bases=[_InputSchemaProperty])
    class InputSchemaProperty(_InputSchemaProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html
        Stability:
            stable
        """
        recordColumns: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.RecordColumnProperty"]]]
        """``CfnApplicationV2.InputSchemaProperty.RecordColumns``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordcolumns
        Stability:
            stable
        """

        recordFormat: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.RecordFormatProperty"]
        """``CfnApplicationV2.InputSchemaProperty.RecordFormat``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-inputschema.html#cfn-kinesisanalyticsv2-application-inputschema-recordformat
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.JSONMappingParametersProperty", jsii_struct_bases=[])
    class JSONMappingParametersProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-jsonmappingparameters.html
        Stability:
            stable
        """
        recordRowPath: str
        """``CfnApplicationV2.JSONMappingParametersProperty.RecordRowPath``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-jsonmappingparameters.html#cfn-kinesisanalyticsv2-application-jsonmappingparameters-recordrowpath
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.KinesisFirehoseInputProperty", jsii_struct_bases=[])
    class KinesisFirehoseInputProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput.html
        Stability:
            stable
        """
        resourceArn: str
        """``CfnApplicationV2.KinesisFirehoseInputProperty.ResourceARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisfirehoseinput.html#cfn-kinesisanalyticsv2-application-kinesisfirehoseinput-resourcearn
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.KinesisStreamsInputProperty", jsii_struct_bases=[])
    class KinesisStreamsInputProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisstreamsinput.html
        Stability:
            stable
        """
        resourceArn: str
        """``CfnApplicationV2.KinesisStreamsInputProperty.ResourceARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-kinesisstreamsinput.html#cfn-kinesisanalyticsv2-application-kinesisstreamsinput-resourcearn
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.MappingParametersProperty", jsii_struct_bases=[])
    class MappingParametersProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html
        Stability:
            stable
        """
        csvMappingParameters: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.CSVMappingParametersProperty"]
        """``CfnApplicationV2.MappingParametersProperty.CSVMappingParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html#cfn-kinesisanalyticsv2-application-mappingparameters-csvmappingparameters
        Stability:
            stable
        """

        jsonMappingParameters: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.JSONMappingParametersProperty"]
        """``CfnApplicationV2.MappingParametersProperty.JSONMappingParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-mappingparameters.html#cfn-kinesisanalyticsv2-application-mappingparameters-jsonmappingparameters
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _MonitoringConfigurationProperty(jsii.compat.TypedDict, total=False):
        logLevel: str
        """``CfnApplicationV2.MonitoringConfigurationProperty.LogLevel``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html#cfn-kinesisanalyticsv2-application-monitoringconfiguration-loglevel
        Stability:
            stable
        """
        metricsLevel: str
        """``CfnApplicationV2.MonitoringConfigurationProperty.MetricsLevel``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html#cfn-kinesisanalyticsv2-application-monitoringconfiguration-metricslevel
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.MonitoringConfigurationProperty", jsii_struct_bases=[_MonitoringConfigurationProperty])
    class MonitoringConfigurationProperty(_MonitoringConfigurationProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html
        Stability:
            stable
        """
        configurationType: str
        """``CfnApplicationV2.MonitoringConfigurationProperty.ConfigurationType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-monitoringconfiguration.html#cfn-kinesisanalyticsv2-application-monitoringconfiguration-configurationtype
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _ParallelismConfigurationProperty(jsii.compat.TypedDict, total=False):
        autoScalingEnabled: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnApplicationV2.ParallelismConfigurationProperty.AutoScalingEnabled``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-autoscalingenabled
        Stability:
            stable
        """
        parallelism: jsii.Number
        """``CfnApplicationV2.ParallelismConfigurationProperty.Parallelism``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-parallelism
        Stability:
            stable
        """
        parallelismPerKpu: jsii.Number
        """``CfnApplicationV2.ParallelismConfigurationProperty.ParallelismPerKPU``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-parallelismperkpu
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.ParallelismConfigurationProperty", jsii_struct_bases=[_ParallelismConfigurationProperty])
    class ParallelismConfigurationProperty(_ParallelismConfigurationProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html
        Stability:
            stable
        """
        configurationType: str
        """``CfnApplicationV2.ParallelismConfigurationProperty.ConfigurationType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-parallelismconfiguration.html#cfn-kinesisanalyticsv2-application-parallelismconfiguration-configurationtype
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.PropertyGroupProperty", jsii_struct_bases=[])
    class PropertyGroupProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html
        Stability:
            stable
        """
        propertyGroupId: str
        """``CfnApplicationV2.PropertyGroupProperty.PropertyGroupId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html#cfn-kinesisanalyticsv2-application-propertygroup-propertygroupid
        Stability:
            stable
        """

        propertyMap: typing.Any
        """``CfnApplicationV2.PropertyGroupProperty.PropertyMap``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-propertygroup.html#cfn-kinesisanalyticsv2-application-propertygroup-propertymap
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _RecordColumnProperty(jsii.compat.TypedDict, total=False):
        mapping: str
        """``CfnApplicationV2.RecordColumnProperty.Mapping``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html#cfn-kinesisanalyticsv2-application-recordcolumn-mapping
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.RecordColumnProperty", jsii_struct_bases=[_RecordColumnProperty])
    class RecordColumnProperty(_RecordColumnProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html
        Stability:
            stable
        """
        name: str
        """``CfnApplicationV2.RecordColumnProperty.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html#cfn-kinesisanalyticsv2-application-recordcolumn-name
        Stability:
            stable
        """

        sqlType: str
        """``CfnApplicationV2.RecordColumnProperty.SqlType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordcolumn.html#cfn-kinesisanalyticsv2-application-recordcolumn-sqltype
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _RecordFormatProperty(jsii.compat.TypedDict, total=False):
        mappingParameters: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.MappingParametersProperty"]
        """``CfnApplicationV2.RecordFormatProperty.MappingParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html#cfn-kinesisanalyticsv2-application-recordformat-mappingparameters
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.RecordFormatProperty", jsii_struct_bases=[_RecordFormatProperty])
    class RecordFormatProperty(_RecordFormatProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html
        Stability:
            stable
        """
        recordFormatType: str
        """``CfnApplicationV2.RecordFormatProperty.RecordFormatType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-recordformat.html#cfn-kinesisanalyticsv2-application-recordformat-recordformattype
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.S3ContentLocationProperty", jsii_struct_bases=[])
    class S3ContentLocationProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html
        Stability:
            stable
        """
        bucketArn: str
        """``CfnApplicationV2.S3ContentLocationProperty.BucketARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html#cfn-kinesisanalyticsv2-application-s3contentlocation-bucketarn
        Stability:
            stable
        """

        fileKey: str
        """``CfnApplicationV2.S3ContentLocationProperty.FileKey``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html#cfn-kinesisanalyticsv2-application-s3contentlocation-filekey
        Stability:
            stable
        """

        objectVersion: str
        """``CfnApplicationV2.S3ContentLocationProperty.ObjectVersion``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-s3contentlocation.html#cfn-kinesisanalyticsv2-application-s3contentlocation-objectversion
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2.SqlApplicationConfigurationProperty", jsii_struct_bases=[])
    class SqlApplicationConfigurationProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-sqlapplicationconfiguration.html
        Stability:
            stable
        """
        inputs: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.InputProperty"]]]
        """``CfnApplicationV2.SqlApplicationConfigurationProperty.Inputs``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisanalyticsv2-application-sqlapplicationconfiguration.html#cfn-kinesisanalyticsv2-application-sqlapplicationconfiguration-inputs
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnApplicationV2Props(jsii.compat.TypedDict, total=False):
    applicationConfiguration: typing.Union[aws_cdk.core.IResolvable, "CfnApplicationV2.ApplicationConfigurationProperty"]
    """``AWS::KinesisAnalyticsV2::Application.ApplicationConfiguration``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationconfiguration
    Stability:
        stable
    """
    applicationDescription: str
    """``AWS::KinesisAnalyticsV2::Application.ApplicationDescription``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationdescription
    Stability:
        stable
    """
    applicationName: str
    """``AWS::KinesisAnalyticsV2::Application.ApplicationName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-applicationname
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-kinesisanalytics.CfnApplicationV2Props", jsii_struct_bases=[_CfnApplicationV2Props])
class CfnApplicationV2Props(_CfnApplicationV2Props):
    """Properties for defining a ``AWS::KinesisAnalyticsV2::Application``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html
    Stability:
        stable
    """
    runtimeEnvironment: str
    """``AWS::KinesisAnalyticsV2::Application.RuntimeEnvironment``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-runtimeenvironment
    Stability:
        stable
    """

    serviceExecutionRole: str
    """``AWS::KinesisAnalyticsV2::Application.ServiceExecutionRole``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html#cfn-kinesisanalyticsv2-application-serviceexecutionrole
    Stability:
        stable
    """

__all__ = ["CfnApplication", "CfnApplicationCloudWatchLoggingOptionV2", "CfnApplicationCloudWatchLoggingOptionV2Props", "CfnApplicationOutput", "CfnApplicationOutputProps", "CfnApplicationOutputV2", "CfnApplicationOutputV2Props", "CfnApplicationProps", "CfnApplicationReferenceDataSource", "CfnApplicationReferenceDataSourceProps", "CfnApplicationReferenceDataSourceV2", "CfnApplicationReferenceDataSourceV2Props", "CfnApplicationV2", "CfnApplicationV2Props", "__jsii_assembly__"]

publication.publish()
