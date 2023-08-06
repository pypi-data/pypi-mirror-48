import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_events
import aws_cdk.aws_iam
import aws_cdk.aws_lambda
import aws_cdk.aws_sns
import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-config", "0.37.0", __name__, "aws-config@0.37.0.jsii.tgz")
class CfnAggregationAuthorization(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-config.CfnAggregationAuthorization"):
    """A CloudFormation ``AWS::Config::AggregationAuthorization``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html
    Stability:
        stable
    cloudformationResource:
        AWS::Config::AggregationAuthorization
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, authorized_account_id: str, authorized_aws_region: str) -> None:
        """Create a new ``AWS::Config::AggregationAuthorization``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            authorized_account_id: ``AWS::Config::AggregationAuthorization.AuthorizedAccountId``.
            authorized_aws_region: ``AWS::Config::AggregationAuthorization.AuthorizedAwsRegion``.

        Stability:
            stable
        """
        props: CfnAggregationAuthorizationProps = {"authorizedAccountId": authorized_account_id, "authorizedAwsRegion": authorized_aws_region}

        jsii.create(CfnAggregationAuthorization, self, [scope, id, props])

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
    @jsii.member(jsii_name="authorizedAccountId")
    def authorized_account_id(self) -> str:
        """``AWS::Config::AggregationAuthorization.AuthorizedAccountId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html#cfn-config-aggregationauthorization-authorizedaccountid
        Stability:
            stable
        """
        return jsii.get(self, "authorizedAccountId")

    @authorized_account_id.setter
    def authorized_account_id(self, value: str):
        return jsii.set(self, "authorizedAccountId", value)

    @property
    @jsii.member(jsii_name="authorizedAwsRegion")
    def authorized_aws_region(self) -> str:
        """``AWS::Config::AggregationAuthorization.AuthorizedAwsRegion``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html#cfn-config-aggregationauthorization-authorizedawsregion
        Stability:
            stable
        """
        return jsii.get(self, "authorizedAwsRegion")

    @authorized_aws_region.setter
    def authorized_aws_region(self, value: str):
        return jsii.set(self, "authorizedAwsRegion", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-config.CfnAggregationAuthorizationProps", jsii_struct_bases=[])
class CfnAggregationAuthorizationProps(jsii.compat.TypedDict):
    """Properties for defining a ``AWS::Config::AggregationAuthorization``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html
    Stability:
        stable
    """
    authorizedAccountId: str
    """``AWS::Config::AggregationAuthorization.AuthorizedAccountId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html#cfn-config-aggregationauthorization-authorizedaccountid
    Stability:
        stable
    """

    authorizedAwsRegion: str
    """``AWS::Config::AggregationAuthorization.AuthorizedAwsRegion``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html#cfn-config-aggregationauthorization-authorizedawsregion
    Stability:
        stable
    """

class CfnConfigRule(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-config.CfnConfigRule"):
    """A CloudFormation ``AWS::Config::ConfigRule``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html
    Stability:
        stable
    cloudformationResource:
        AWS::Config::ConfigRule
    """
    def __init__(self, scope_: aws_cdk.core.Construct, id: str, *, source: typing.Union["SourceProperty", aws_cdk.core.IResolvable], config_rule_name: typing.Optional[str]=None, description: typing.Optional[str]=None, input_parameters: typing.Any=None, maximum_execution_frequency: typing.Optional[str]=None, scope: typing.Optional[typing.Union[typing.Optional["ScopeProperty"], typing.Optional[aws_cdk.core.IResolvable]]]=None) -> None:
        """Create a new ``AWS::Config::ConfigRule``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            source: ``AWS::Config::ConfigRule.Source``.
            config_rule_name: ``AWS::Config::ConfigRule.ConfigRuleName``.
            description: ``AWS::Config::ConfigRule.Description``.
            input_parameters: ``AWS::Config::ConfigRule.InputParameters``.
            maximum_execution_frequency: ``AWS::Config::ConfigRule.MaximumExecutionFrequency``.
            scope: ``AWS::Config::ConfigRule.Scope``.

        Stability:
            stable
        """
        props: CfnConfigRuleProps = {"source": source}

        if config_rule_name is not None:
            props["configRuleName"] = config_rule_name

        if description is not None:
            props["description"] = description

        if input_parameters is not None:
            props["inputParameters"] = input_parameters

        if maximum_execution_frequency is not None:
            props["maximumExecutionFrequency"] = maximum_execution_frequency

        if scope is not None:
            props["scope"] = scope

        jsii.create(CfnConfigRule, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrComplianceType")
    def attr_compliance_type(self) -> str:
        """
        Stability:
            stable
        cloudformationAttribute:
            Compliance.Type
        """
        return jsii.get(self, "attrComplianceType")

    @property
    @jsii.member(jsii_name="attrConfigRuleId")
    def attr_config_rule_id(self) -> str:
        """
        Stability:
            stable
        cloudformationAttribute:
            ConfigRuleId
        """
        return jsii.get(self, "attrConfigRuleId")

    @property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[str,typing.Any]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "cfnProperties")

    @property
    @jsii.member(jsii_name="inputParameters")
    def input_parameters(self) -> typing.Any:
        """``AWS::Config::ConfigRule.InputParameters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-inputparameters
        Stability:
            stable
        """
        return jsii.get(self, "inputParameters")

    @input_parameters.setter
    def input_parameters(self, value: typing.Any):
        return jsii.set(self, "inputParameters", value)

    @property
    @jsii.member(jsii_name="source")
    def source(self) -> typing.Union["SourceProperty", aws_cdk.core.IResolvable]:
        """``AWS::Config::ConfigRule.Source``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-source
        Stability:
            stable
        """
        return jsii.get(self, "source")

    @source.setter
    def source(self, value: typing.Union["SourceProperty", aws_cdk.core.IResolvable]):
        return jsii.set(self, "source", value)

    @property
    @jsii.member(jsii_name="configRuleName")
    def config_rule_name(self) -> typing.Optional[str]:
        """``AWS::Config::ConfigRule.ConfigRuleName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-configrulename
        Stability:
            stable
        """
        return jsii.get(self, "configRuleName")

    @config_rule_name.setter
    def config_rule_name(self, value: typing.Optional[str]):
        return jsii.set(self, "configRuleName", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[str]:
        """``AWS::Config::ConfigRule.Description``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-description
        Stability:
            stable
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: typing.Optional[str]):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> typing.Optional[str]:
        """``AWS::Config::ConfigRule.MaximumExecutionFrequency``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-maximumexecutionfrequency
        Stability:
            stable
        """
        return jsii.get(self, "maximumExecutionFrequency")

    @maximum_execution_frequency.setter
    def maximum_execution_frequency(self, value: typing.Optional[str]):
        return jsii.set(self, "maximumExecutionFrequency", value)

    @property
    @jsii.member(jsii_name="scope")
    def scope(self) -> typing.Optional[typing.Union[typing.Optional["ScopeProperty"], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::Config::ConfigRule.Scope``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-scope
        Stability:
            stable
        """
        return jsii.get(self, "scope")

    @scope.setter
    def scope(self, value: typing.Optional[typing.Union[typing.Optional["ScopeProperty"], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "scope", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-config.CfnConfigRule.ScopeProperty", jsii_struct_bases=[])
    class ScopeProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html
        Stability:
            stable
        """
        complianceResourceId: str
        """``CfnConfigRule.ScopeProperty.ComplianceResourceId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-complianceresourceid
        Stability:
            stable
        """

        complianceResourceTypes: typing.List[str]
        """``CfnConfigRule.ScopeProperty.ComplianceResourceTypes``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-complianceresourcetypes
        Stability:
            stable
        """

        tagKey: str
        """``CfnConfigRule.ScopeProperty.TagKey``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-tagkey
        Stability:
            stable
        """

        tagValue: str
        """``CfnConfigRule.ScopeProperty.TagValue``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-tagvalue
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _SourceDetailProperty(jsii.compat.TypedDict, total=False):
        maximumExecutionFrequency: str
        """``CfnConfigRule.SourceDetailProperty.MaximumExecutionFrequency``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source-sourcedetails.html#cfn-config-configrule-sourcedetail-maximumexecutionfrequency
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-config.CfnConfigRule.SourceDetailProperty", jsii_struct_bases=[_SourceDetailProperty])
    class SourceDetailProperty(_SourceDetailProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source-sourcedetails.html
        Stability:
            stable
        """
        eventSource: str
        """``CfnConfigRule.SourceDetailProperty.EventSource``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source-sourcedetails.html#cfn-config-configrule-source-sourcedetail-eventsource
        Stability:
            stable
        """

        messageType: str
        """``CfnConfigRule.SourceDetailProperty.MessageType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source-sourcedetails.html#cfn-config-configrule-source-sourcedetail-messagetype
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _SourceProperty(jsii.compat.TypedDict, total=False):
        sourceDetails: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnConfigRule.SourceDetailProperty"]]]
        """``CfnConfigRule.SourceProperty.SourceDetails``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-sourcedetails
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-config.CfnConfigRule.SourceProperty", jsii_struct_bases=[_SourceProperty])
    class SourceProperty(_SourceProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html
        Stability:
            stable
        """
        owner: str
        """``CfnConfigRule.SourceProperty.Owner``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-owner
        Stability:
            stable
        """

        sourceIdentifier: str
        """``CfnConfigRule.SourceProperty.SourceIdentifier``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-sourceidentifier
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnConfigRuleProps(jsii.compat.TypedDict, total=False):
    configRuleName: str
    """``AWS::Config::ConfigRule.ConfigRuleName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-configrulename
    Stability:
        stable
    """
    description: str
    """``AWS::Config::ConfigRule.Description``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-description
    Stability:
        stable
    """
    inputParameters: typing.Any
    """``AWS::Config::ConfigRule.InputParameters``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-inputparameters
    Stability:
        stable
    """
    maximumExecutionFrequency: str
    """``AWS::Config::ConfigRule.MaximumExecutionFrequency``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-maximumexecutionfrequency
    Stability:
        stable
    """
    scope: typing.Union["CfnConfigRule.ScopeProperty", aws_cdk.core.IResolvable]
    """``AWS::Config::ConfigRule.Scope``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-scope
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-config.CfnConfigRuleProps", jsii_struct_bases=[_CfnConfigRuleProps])
class CfnConfigRuleProps(_CfnConfigRuleProps):
    """Properties for defining a ``AWS::Config::ConfigRule``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html
    Stability:
        stable
    """
    source: typing.Union["CfnConfigRule.SourceProperty", aws_cdk.core.IResolvable]
    """``AWS::Config::ConfigRule.Source``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-source
    Stability:
        stable
    """

class CfnConfigurationAggregator(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-config.CfnConfigurationAggregator"):
    """A CloudFormation ``AWS::Config::ConfigurationAggregator``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html
    Stability:
        stable
    cloudformationResource:
        AWS::Config::ConfigurationAggregator
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, configuration_aggregator_name: str, account_aggregation_sources: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "AccountAggregationSourceProperty"]]]]]=None, organization_aggregation_source: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["OrganizationAggregationSourceProperty"]]]=None) -> None:
        """Create a new ``AWS::Config::ConfigurationAggregator``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            configuration_aggregator_name: ``AWS::Config::ConfigurationAggregator.ConfigurationAggregatorName``.
            account_aggregation_sources: ``AWS::Config::ConfigurationAggregator.AccountAggregationSources``.
            organization_aggregation_source: ``AWS::Config::ConfigurationAggregator.OrganizationAggregationSource``.

        Stability:
            stable
        """
        props: CfnConfigurationAggregatorProps = {"configurationAggregatorName": configuration_aggregator_name}

        if account_aggregation_sources is not None:
            props["accountAggregationSources"] = account_aggregation_sources

        if organization_aggregation_source is not None:
            props["organizationAggregationSource"] = organization_aggregation_source

        jsii.create(CfnConfigurationAggregator, self, [scope, id, props])

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
    @jsii.member(jsii_name="configurationAggregatorName")
    def configuration_aggregator_name(self) -> str:
        """``AWS::Config::ConfigurationAggregator.ConfigurationAggregatorName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-configurationaggregatorname
        Stability:
            stable
        """
        return jsii.get(self, "configurationAggregatorName")

    @configuration_aggregator_name.setter
    def configuration_aggregator_name(self, value: str):
        return jsii.set(self, "configurationAggregatorName", value)

    @property
    @jsii.member(jsii_name="accountAggregationSources")
    def account_aggregation_sources(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "AccountAggregationSourceProperty"]]]]]:
        """``AWS::Config::ConfigurationAggregator.AccountAggregationSources``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-accountaggregationsources
        Stability:
            stable
        """
        return jsii.get(self, "accountAggregationSources")

    @account_aggregation_sources.setter
    def account_aggregation_sources(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "AccountAggregationSourceProperty"]]]]]):
        return jsii.set(self, "accountAggregationSources", value)

    @property
    @jsii.member(jsii_name="organizationAggregationSource")
    def organization_aggregation_source(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["OrganizationAggregationSourceProperty"]]]:
        """``AWS::Config::ConfigurationAggregator.OrganizationAggregationSource``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-organizationaggregationsource
        Stability:
            stable
        """
        return jsii.get(self, "organizationAggregationSource")

    @organization_aggregation_source.setter
    def organization_aggregation_source(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["OrganizationAggregationSourceProperty"]]]):
        return jsii.set(self, "organizationAggregationSource", value)

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _AccountAggregationSourceProperty(jsii.compat.TypedDict, total=False):
        allAwsRegions: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnConfigurationAggregator.AccountAggregationSourceProperty.AllAwsRegions``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html#cfn-config-configurationaggregator-accountaggregationsource-allawsregions
        Stability:
            stable
        """
        awsRegions: typing.List[str]
        """``CfnConfigurationAggregator.AccountAggregationSourceProperty.AwsRegions``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html#cfn-config-configurationaggregator-accountaggregationsource-awsregions
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-config.CfnConfigurationAggregator.AccountAggregationSourceProperty", jsii_struct_bases=[_AccountAggregationSourceProperty])
    class AccountAggregationSourceProperty(_AccountAggregationSourceProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html
        Stability:
            stable
        """
        accountIds: typing.List[str]
        """``CfnConfigurationAggregator.AccountAggregationSourceProperty.AccountIds``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html#cfn-config-configurationaggregator-accountaggregationsource-accountids
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _OrganizationAggregationSourceProperty(jsii.compat.TypedDict, total=False):
        allAwsRegions: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnConfigurationAggregator.OrganizationAggregationSourceProperty.AllAwsRegions``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html#cfn-config-configurationaggregator-organizationaggregationsource-allawsregions
        Stability:
            stable
        """
        awsRegions: typing.List[str]
        """``CfnConfigurationAggregator.OrganizationAggregationSourceProperty.AwsRegions``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html#cfn-config-configurationaggregator-organizationaggregationsource-awsregions
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-config.CfnConfigurationAggregator.OrganizationAggregationSourceProperty", jsii_struct_bases=[_OrganizationAggregationSourceProperty])
    class OrganizationAggregationSourceProperty(_OrganizationAggregationSourceProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html
        Stability:
            stable
        """
        roleArn: str
        """``CfnConfigurationAggregator.OrganizationAggregationSourceProperty.RoleArn``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html#cfn-config-configurationaggregator-organizationaggregationsource-rolearn
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnConfigurationAggregatorProps(jsii.compat.TypedDict, total=False):
    accountAggregationSources: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationAggregator.AccountAggregationSourceProperty"]]]
    """``AWS::Config::ConfigurationAggregator.AccountAggregationSources``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-accountaggregationsources
    Stability:
        stable
    """
    organizationAggregationSource: typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationAggregator.OrganizationAggregationSourceProperty"]
    """``AWS::Config::ConfigurationAggregator.OrganizationAggregationSource``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-organizationaggregationsource
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-config.CfnConfigurationAggregatorProps", jsii_struct_bases=[_CfnConfigurationAggregatorProps])
class CfnConfigurationAggregatorProps(_CfnConfigurationAggregatorProps):
    """Properties for defining a ``AWS::Config::ConfigurationAggregator``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html
    Stability:
        stable
    """
    configurationAggregatorName: str
    """``AWS::Config::ConfigurationAggregator.ConfigurationAggregatorName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-configurationaggregatorname
    Stability:
        stable
    """

class CfnConfigurationRecorder(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-config.CfnConfigurationRecorder"):
    """A CloudFormation ``AWS::Config::ConfigurationRecorder``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html
    Stability:
        stable
    cloudformationResource:
        AWS::Config::ConfigurationRecorder
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, role_arn: str, name: typing.Optional[str]=None, recording_group: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["RecordingGroupProperty"]]]=None) -> None:
        """Create a new ``AWS::Config::ConfigurationRecorder``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            role_arn: ``AWS::Config::ConfigurationRecorder.RoleARN``.
            name: ``AWS::Config::ConfigurationRecorder.Name``.
            recording_group: ``AWS::Config::ConfigurationRecorder.RecordingGroup``.

        Stability:
            stable
        """
        props: CfnConfigurationRecorderProps = {"roleArn": role_arn}

        if name is not None:
            props["name"] = name

        if recording_group is not None:
            props["recordingGroup"] = recording_group

        jsii.create(CfnConfigurationRecorder, self, [scope, id, props])

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
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> str:
        """``AWS::Config::ConfigurationRecorder.RoleARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-rolearn
        Stability:
            stable
        """
        return jsii.get(self, "roleArn")

    @role_arn.setter
    def role_arn(self, value: str):
        return jsii.set(self, "roleArn", value)

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::Config::ConfigurationRecorder.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-name
        Stability:
            stable
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="recordingGroup")
    def recording_group(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["RecordingGroupProperty"]]]:
        """``AWS::Config::ConfigurationRecorder.RecordingGroup``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-recordinggroup
        Stability:
            stable
        """
        return jsii.get(self, "recordingGroup")

    @recording_group.setter
    def recording_group(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["RecordingGroupProperty"]]]):
        return jsii.set(self, "recordingGroup", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-config.CfnConfigurationRecorder.RecordingGroupProperty", jsii_struct_bases=[])
    class RecordingGroupProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html
        Stability:
            stable
        """
        allSupported: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnConfigurationRecorder.RecordingGroupProperty.AllSupported``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-allsupported
        Stability:
            stable
        """

        includeGlobalResourceTypes: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnConfigurationRecorder.RecordingGroupProperty.IncludeGlobalResourceTypes``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-includeglobalresourcetypes
        Stability:
            stable
        """

        resourceTypes: typing.List[str]
        """``CfnConfigurationRecorder.RecordingGroupProperty.ResourceTypes``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-resourcetypes
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnConfigurationRecorderProps(jsii.compat.TypedDict, total=False):
    name: str
    """``AWS::Config::ConfigurationRecorder.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-name
    Stability:
        stable
    """
    recordingGroup: typing.Union[aws_cdk.core.IResolvable, "CfnConfigurationRecorder.RecordingGroupProperty"]
    """``AWS::Config::ConfigurationRecorder.RecordingGroup``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-recordinggroup
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-config.CfnConfigurationRecorderProps", jsii_struct_bases=[_CfnConfigurationRecorderProps])
class CfnConfigurationRecorderProps(_CfnConfigurationRecorderProps):
    """Properties for defining a ``AWS::Config::ConfigurationRecorder``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html
    Stability:
        stable
    """
    roleArn: str
    """``AWS::Config::ConfigurationRecorder.RoleARN``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-rolearn
    Stability:
        stable
    """

class CfnDeliveryChannel(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-config.CfnDeliveryChannel"):
    """A CloudFormation ``AWS::Config::DeliveryChannel``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html
    Stability:
        stable
    cloudformationResource:
        AWS::Config::DeliveryChannel
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, s3_bucket_name: str, config_snapshot_delivery_properties: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ConfigSnapshotDeliveryPropertiesProperty"]]]=None, name: typing.Optional[str]=None, s3_key_prefix: typing.Optional[str]=None, sns_topic_arn: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::Config::DeliveryChannel``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            s3_bucket_name: ``AWS::Config::DeliveryChannel.S3BucketName``.
            config_snapshot_delivery_properties: ``AWS::Config::DeliveryChannel.ConfigSnapshotDeliveryProperties``.
            name: ``AWS::Config::DeliveryChannel.Name``.
            s3_key_prefix: ``AWS::Config::DeliveryChannel.S3KeyPrefix``.
            sns_topic_arn: ``AWS::Config::DeliveryChannel.SnsTopicARN``.

        Stability:
            stable
        """
        props: CfnDeliveryChannelProps = {"s3BucketName": s3_bucket_name}

        if config_snapshot_delivery_properties is not None:
            props["configSnapshotDeliveryProperties"] = config_snapshot_delivery_properties

        if name is not None:
            props["name"] = name

        if s3_key_prefix is not None:
            props["s3KeyPrefix"] = s3_key_prefix

        if sns_topic_arn is not None:
            props["snsTopicArn"] = sns_topic_arn

        jsii.create(CfnDeliveryChannel, self, [scope, id, props])

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
    @jsii.member(jsii_name="s3BucketName")
    def s3_bucket_name(self) -> str:
        """``AWS::Config::DeliveryChannel.S3BucketName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-s3bucketname
        Stability:
            stable
        """
        return jsii.get(self, "s3BucketName")

    @s3_bucket_name.setter
    def s3_bucket_name(self, value: str):
        return jsii.set(self, "s3BucketName", value)

    @property
    @jsii.member(jsii_name="configSnapshotDeliveryProperties")
    def config_snapshot_delivery_properties(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ConfigSnapshotDeliveryPropertiesProperty"]]]:
        """``AWS::Config::DeliveryChannel.ConfigSnapshotDeliveryProperties``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-configsnapshotdeliveryproperties
        Stability:
            stable
        """
        return jsii.get(self, "configSnapshotDeliveryProperties")

    @config_snapshot_delivery_properties.setter
    def config_snapshot_delivery_properties(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ConfigSnapshotDeliveryPropertiesProperty"]]]):
        return jsii.set(self, "configSnapshotDeliveryProperties", value)

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::Config::DeliveryChannel.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-name
        Stability:
            stable
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        return jsii.set(self, "name", value)

    @property
    @jsii.member(jsii_name="s3KeyPrefix")
    def s3_key_prefix(self) -> typing.Optional[str]:
        """``AWS::Config::DeliveryChannel.S3KeyPrefix``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-s3keyprefix
        Stability:
            stable
        """
        return jsii.get(self, "s3KeyPrefix")

    @s3_key_prefix.setter
    def s3_key_prefix(self, value: typing.Optional[str]):
        return jsii.set(self, "s3KeyPrefix", value)

    @property
    @jsii.member(jsii_name="snsTopicArn")
    def sns_topic_arn(self) -> typing.Optional[str]:
        """``AWS::Config::DeliveryChannel.SnsTopicARN``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-snstopicarn
        Stability:
            stable
        """
        return jsii.get(self, "snsTopicArn")

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: typing.Optional[str]):
        return jsii.set(self, "snsTopicArn", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-config.CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty", jsii_struct_bases=[])
    class ConfigSnapshotDeliveryPropertiesProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-deliverychannel-configsnapshotdeliveryproperties.html
        Stability:
            stable
        """
        deliveryFrequency: str
        """``CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty.DeliveryFrequency``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-deliverychannel-configsnapshotdeliveryproperties.html#cfn-config-deliverychannel-configsnapshotdeliveryproperties-deliveryfrequency
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnDeliveryChannelProps(jsii.compat.TypedDict, total=False):
    configSnapshotDeliveryProperties: typing.Union[aws_cdk.core.IResolvable, "CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty"]
    """``AWS::Config::DeliveryChannel.ConfigSnapshotDeliveryProperties``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-configsnapshotdeliveryproperties
    Stability:
        stable
    """
    name: str
    """``AWS::Config::DeliveryChannel.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-name
    Stability:
        stable
    """
    s3KeyPrefix: str
    """``AWS::Config::DeliveryChannel.S3KeyPrefix``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-s3keyprefix
    Stability:
        stable
    """
    snsTopicArn: str
    """``AWS::Config::DeliveryChannel.SnsTopicARN``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-snstopicarn
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-config.CfnDeliveryChannelProps", jsii_struct_bases=[_CfnDeliveryChannelProps])
class CfnDeliveryChannelProps(_CfnDeliveryChannelProps):
    """Properties for defining a ``AWS::Config::DeliveryChannel``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html
    Stability:
        stable
    """
    s3BucketName: str
    """``AWS::Config::DeliveryChannel.S3BucketName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-s3bucketname
    Stability:
        stable
    """

@jsii.interface(jsii_type="@aws-cdk/aws-config.IRule")
class IRule(aws_cdk.core.IResource, jsii.compat.Protocol):
    """A config rule.

    Stability:
        experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IRuleProxy

    @property
    @jsii.member(jsii_name="configRuleName")
    def config_rule_name(self) -> str:
        """The name of the rule.

        Stability:
            experimental
        attribute:
            true
        """
        ...

    @jsii.member(jsii_name="onComplianceChange")
    def on_compliance_change(self, id: str, *, description: typing.Optional[str]=None, event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern]=None, rule_name: typing.Optional[str]=None, target: typing.Optional[aws_cdk.aws_events.IRuleTarget]=None) -> aws_cdk.aws_events.Rule:
        """Defines a CloudWatch event rule which triggers for rule compliance events.

        Arguments:
            id: -
            options: -
            description: A description of the rule's purpose. Default: - No description
            event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
            rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
            target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.

        Stability:
            experimental
        """
        ...

    @jsii.member(jsii_name="onEvent")
    def on_event(self, id: str, *, description: typing.Optional[str]=None, event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern]=None, rule_name: typing.Optional[str]=None, target: typing.Optional[aws_cdk.aws_events.IRuleTarget]=None) -> aws_cdk.aws_events.Rule:
        """Defines a CloudWatch event rule which triggers for rule events.

        Use
        ``rule.addEventPattern(pattern)`` to specify a filter.

        Arguments:
            id: -
            options: -
            description: A description of the rule's purpose. Default: - No description
            event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
            rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
            target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.

        Stability:
            experimental
        """
        ...

    @jsii.member(jsii_name="onReEvaluationStatus")
    def on_re_evaluation_status(self, id: str, *, description: typing.Optional[str]=None, event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern]=None, rule_name: typing.Optional[str]=None, target: typing.Optional[aws_cdk.aws_events.IRuleTarget]=None) -> aws_cdk.aws_events.Rule:
        """Defines a CloudWatch event rule which triggers for rule re-evaluation status events.

        Arguments:
            id: -
            options: -
            description: A description of the rule's purpose. Default: - No description
            event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
            rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
            target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.

        Stability:
            experimental
        """
        ...


class _IRuleProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """A config rule.

    Stability:
        experimental
    """
    __jsii_type__ = "@aws-cdk/aws-config.IRule"
    @property
    @jsii.member(jsii_name="configRuleName")
    def config_rule_name(self) -> str:
        """The name of the rule.

        Stability:
            experimental
        attribute:
            true
        """
        return jsii.get(self, "configRuleName")

    @jsii.member(jsii_name="onComplianceChange")
    def on_compliance_change(self, id: str, *, description: typing.Optional[str]=None, event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern]=None, rule_name: typing.Optional[str]=None, target: typing.Optional[aws_cdk.aws_events.IRuleTarget]=None) -> aws_cdk.aws_events.Rule:
        """Defines a CloudWatch event rule which triggers for rule compliance events.

        Arguments:
            id: -
            options: -
            description: A description of the rule's purpose. Default: - No description
            event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
            rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
            target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.

        Stability:
            experimental
        """
        options: aws_cdk.aws_events.OnEventOptions = {}

        if description is not None:
            options["description"] = description

        if event_pattern is not None:
            options["eventPattern"] = event_pattern

        if rule_name is not None:
            options["ruleName"] = rule_name

        if target is not None:
            options["target"] = target

        return jsii.invoke(self, "onComplianceChange", [id, options])

    @jsii.member(jsii_name="onEvent")
    def on_event(self, id: str, *, description: typing.Optional[str]=None, event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern]=None, rule_name: typing.Optional[str]=None, target: typing.Optional[aws_cdk.aws_events.IRuleTarget]=None) -> aws_cdk.aws_events.Rule:
        """Defines a CloudWatch event rule which triggers for rule events.

        Use
        ``rule.addEventPattern(pattern)`` to specify a filter.

        Arguments:
            id: -
            options: -
            description: A description of the rule's purpose. Default: - No description
            event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
            rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
            target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.

        Stability:
            experimental
        """
        options: aws_cdk.aws_events.OnEventOptions = {}

        if description is not None:
            options["description"] = description

        if event_pattern is not None:
            options["eventPattern"] = event_pattern

        if rule_name is not None:
            options["ruleName"] = rule_name

        if target is not None:
            options["target"] = target

        return jsii.invoke(self, "onEvent", [id, options])

    @jsii.member(jsii_name="onReEvaluationStatus")
    def on_re_evaluation_status(self, id: str, *, description: typing.Optional[str]=None, event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern]=None, rule_name: typing.Optional[str]=None, target: typing.Optional[aws_cdk.aws_events.IRuleTarget]=None) -> aws_cdk.aws_events.Rule:
        """Defines a CloudWatch event rule which triggers for rule re-evaluation status events.

        Arguments:
            id: -
            options: -
            description: A description of the rule's purpose. Default: - No description
            event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
            rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
            target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.

        Stability:
            experimental
        """
        options: aws_cdk.aws_events.OnEventOptions = {}

        if description is not None:
            options["description"] = description

        if event_pattern is not None:
            options["eventPattern"] = event_pattern

        if rule_name is not None:
            options["ruleName"] = rule_name

        if target is not None:
            options["target"] = target

        return jsii.invoke(self, "onReEvaluationStatus", [id, options])


@jsii.implements(IRule)
class CustomRule(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-config.CustomRule"):
    """A new custom rule.

    Stability:
        experimental
    resource:
        AWS::Config::ConfigRule
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, lambda_function: aws_cdk.aws_lambda.IFunction, configuration_changes: typing.Optional[bool]=None, periodic: typing.Optional[bool]=None, config_rule_name: typing.Optional[str]=None, description: typing.Optional[str]=None, input_parameters: typing.Optional[typing.Mapping[str,typing.Any]]=None, maximum_execution_frequency: typing.Optional["MaximumExecutionFrequency"]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            lambda_function: The Lambda function to run.
            configuration_changes: Whether to run the rule on configuration changes. Default: false
            periodic: Whether to run the rule on a fixed frequency. Default: false
            config_rule_name: A name for the AWS Config rule. Default: a CloudFormation generated name
            description: A description about this AWS Config rule. Default: no description
            input_parameters: Input parameter values that are passed to the AWS Config rule. Default: no input parameters
            maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: 24 hours

        Stability:
            experimental
        """
        props: CustomRuleProps = {"lambdaFunction": lambda_function}

        if configuration_changes is not None:
            props["configurationChanges"] = configuration_changes

        if periodic is not None:
            props["periodic"] = periodic

        if config_rule_name is not None:
            props["configRuleName"] = config_rule_name

        if description is not None:
            props["description"] = description

        if input_parameters is not None:
            props["inputParameters"] = input_parameters

        if maximum_execution_frequency is not None:
            props["maximumExecutionFrequency"] = maximum_execution_frequency

        jsii.create(CustomRule, self, [scope, id, props])

    @jsii.member(jsii_name="fromConfigRuleName")
    @classmethod
    def from_config_rule_name(cls, scope: aws_cdk.core.Construct, id: str, config_rule_name: str) -> "IRule":
        """Imports an existing rule.

        Arguments:
            scope: -
            id: -
            config_rule_name: the name of the rule.

        Stability:
            experimental
        """
        return jsii.sinvoke(cls, "fromConfigRuleName", [scope, id, config_rule_name])

    @jsii.member(jsii_name="onComplianceChange")
    def on_compliance_change(self, id: str, *, description: typing.Optional[str]=None, event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern]=None, rule_name: typing.Optional[str]=None, target: typing.Optional[aws_cdk.aws_events.IRuleTarget]=None) -> aws_cdk.aws_events.Rule:
        """Defines a CloudWatch event rule which triggers for rule compliance events.

        Arguments:
            id: -
            options: -
            description: A description of the rule's purpose. Default: - No description
            event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
            rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
            target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.

        Stability:
            experimental
        """
        options: aws_cdk.aws_events.OnEventOptions = {}

        if description is not None:
            options["description"] = description

        if event_pattern is not None:
            options["eventPattern"] = event_pattern

        if rule_name is not None:
            options["ruleName"] = rule_name

        if target is not None:
            options["target"] = target

        return jsii.invoke(self, "onComplianceChange", [id, options])

    @jsii.member(jsii_name="onEvent")
    def on_event(self, id: str, *, description: typing.Optional[str]=None, event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern]=None, rule_name: typing.Optional[str]=None, target: typing.Optional[aws_cdk.aws_events.IRuleTarget]=None) -> aws_cdk.aws_events.Rule:
        """Defines a CloudWatch event rule which triggers for rule events.

        Use
        ``rule.addEventPattern(pattern)`` to specify a filter.

        Arguments:
            id: -
            options: -
            description: A description of the rule's purpose. Default: - No description
            event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
            rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
            target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.

        Stability:
            experimental
        """
        options: aws_cdk.aws_events.OnEventOptions = {}

        if description is not None:
            options["description"] = description

        if event_pattern is not None:
            options["eventPattern"] = event_pattern

        if rule_name is not None:
            options["ruleName"] = rule_name

        if target is not None:
            options["target"] = target

        return jsii.invoke(self, "onEvent", [id, options])

    @jsii.member(jsii_name="onReEvaluationStatus")
    def on_re_evaluation_status(self, id: str, *, description: typing.Optional[str]=None, event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern]=None, rule_name: typing.Optional[str]=None, target: typing.Optional[aws_cdk.aws_events.IRuleTarget]=None) -> aws_cdk.aws_events.Rule:
        """Defines a CloudWatch event rule which triggers for rule re-evaluation status events.

        Arguments:
            id: -
            options: -
            description: A description of the rule's purpose. Default: - No description
            event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
            rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
            target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.

        Stability:
            experimental
        """
        options: aws_cdk.aws_events.OnEventOptions = {}

        if description is not None:
            options["description"] = description

        if event_pattern is not None:
            options["eventPattern"] = event_pattern

        if rule_name is not None:
            options["ruleName"] = rule_name

        if target is not None:
            options["target"] = target

        return jsii.invoke(self, "onReEvaluationStatus", [id, options])

    @jsii.member(jsii_name="scopeToResource")
    def scope_to_resource(self, type: str, identifier: typing.Optional[str]=None) -> None:
        """Restrict scope of changes to a specific resource.

        Arguments:
            type: the resource type.
            identifier: the resource identifier.

        See:
            https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources
        Stability:
            experimental
        """
        return jsii.invoke(self, "scopeToResource", [type, identifier])

    @jsii.member(jsii_name="scopeToResources")
    def scope_to_resources(self, *types: str) -> None:
        """Restrict scope of changes to specific resource types.

        Arguments:
            types: resource types.

        See:
            https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources
        Stability:
            experimental
        """
        return jsii.invoke(self, "scopeToResources", [*types])

    @jsii.member(jsii_name="scopeToTag")
    def scope_to_tag(self, key: str, value: typing.Optional[str]=None) -> None:
        """Restrict scope of changes to a specific tag.

        Arguments:
            key: the tag key.
            value: the tag value.

        Stability:
            experimental
        """
        return jsii.invoke(self, "scopeToTag", [key, value])

    @property
    @jsii.member(jsii_name="configRuleArn")
    def config_rule_arn(self) -> str:
        """The arn of the rule.

        Stability:
            experimental
        attribute:
            true
        """
        return jsii.get(self, "configRuleArn")

    @property
    @jsii.member(jsii_name="configRuleComplianceType")
    def config_rule_compliance_type(self) -> str:
        """The compliance status of the rule.

        Stability:
            experimental
        attribute:
            true
        """
        return jsii.get(self, "configRuleComplianceType")

    @property
    @jsii.member(jsii_name="configRuleId")
    def config_rule_id(self) -> str:
        """The id of the rule.

        Stability:
            experimental
        attribute:
            true
        """
        return jsii.get(self, "configRuleId")

    @property
    @jsii.member(jsii_name="configRuleName")
    def config_rule_name(self) -> str:
        """The name of the rule.

        Stability:
            experimental
        attribute:
            true
        """
        return jsii.get(self, "configRuleName")

    @property
    @jsii.member(jsii_name="isCustomWithChanges")
    def _is_custom_with_changes(self) -> typing.Optional[bool]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "isCustomWithChanges")

    @_is_custom_with_changes.setter
    def _is_custom_with_changes(self, value: typing.Optional[bool]):
        return jsii.set(self, "isCustomWithChanges", value)

    @property
    @jsii.member(jsii_name="isManaged")
    def _is_managed(self) -> typing.Optional[bool]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "isManaged")

    @_is_managed.setter
    def _is_managed(self, value: typing.Optional[bool]):
        return jsii.set(self, "isManaged", value)

    @property
    @jsii.member(jsii_name="scope")
    def _scope(self) -> typing.Optional["CfnConfigRule.ScopeProperty"]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "scope")

    @_scope.setter
    def _scope(self, value: typing.Optional["CfnConfigRule.ScopeProperty"]):
        return jsii.set(self, "scope", value)


@jsii.implements(IRule)
class ManagedRule(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-config.ManagedRule"):
    """A new managed rule.

    Stability:
        experimental
    resource:
        AWS::Config::ConfigRule
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, identifier: str, config_rule_name: typing.Optional[str]=None, description: typing.Optional[str]=None, input_parameters: typing.Optional[typing.Mapping[str,typing.Any]]=None, maximum_execution_frequency: typing.Optional["MaximumExecutionFrequency"]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            identifier: The identifier of the AWS managed rule.
            config_rule_name: A name for the AWS Config rule. Default: a CloudFormation generated name
            description: A description about this AWS Config rule. Default: no description
            input_parameters: Input parameter values that are passed to the AWS Config rule. Default: no input parameters
            maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: 24 hours

        Stability:
            experimental
        """
        props: ManagedRuleProps = {"identifier": identifier}

        if config_rule_name is not None:
            props["configRuleName"] = config_rule_name

        if description is not None:
            props["description"] = description

        if input_parameters is not None:
            props["inputParameters"] = input_parameters

        if maximum_execution_frequency is not None:
            props["maximumExecutionFrequency"] = maximum_execution_frequency

        jsii.create(ManagedRule, self, [scope, id, props])

    @jsii.member(jsii_name="fromConfigRuleName")
    @classmethod
    def from_config_rule_name(cls, scope: aws_cdk.core.Construct, id: str, config_rule_name: str) -> "IRule":
        """Imports an existing rule.

        Arguments:
            scope: -
            id: -
            config_rule_name: the name of the rule.

        Stability:
            experimental
        """
        return jsii.sinvoke(cls, "fromConfigRuleName", [scope, id, config_rule_name])

    @jsii.member(jsii_name="onComplianceChange")
    def on_compliance_change(self, id: str, *, description: typing.Optional[str]=None, event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern]=None, rule_name: typing.Optional[str]=None, target: typing.Optional[aws_cdk.aws_events.IRuleTarget]=None) -> aws_cdk.aws_events.Rule:
        """Defines a CloudWatch event rule which triggers for rule compliance events.

        Arguments:
            id: -
            options: -
            description: A description of the rule's purpose. Default: - No description
            event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
            rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
            target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.

        Stability:
            experimental
        """
        options: aws_cdk.aws_events.OnEventOptions = {}

        if description is not None:
            options["description"] = description

        if event_pattern is not None:
            options["eventPattern"] = event_pattern

        if rule_name is not None:
            options["ruleName"] = rule_name

        if target is not None:
            options["target"] = target

        return jsii.invoke(self, "onComplianceChange", [id, options])

    @jsii.member(jsii_name="onEvent")
    def on_event(self, id: str, *, description: typing.Optional[str]=None, event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern]=None, rule_name: typing.Optional[str]=None, target: typing.Optional[aws_cdk.aws_events.IRuleTarget]=None) -> aws_cdk.aws_events.Rule:
        """Defines a CloudWatch event rule which triggers for rule events.

        Use
        ``rule.addEventPattern(pattern)`` to specify a filter.

        Arguments:
            id: -
            options: -
            description: A description of the rule's purpose. Default: - No description
            event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
            rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
            target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.

        Stability:
            experimental
        """
        options: aws_cdk.aws_events.OnEventOptions = {}

        if description is not None:
            options["description"] = description

        if event_pattern is not None:
            options["eventPattern"] = event_pattern

        if rule_name is not None:
            options["ruleName"] = rule_name

        if target is not None:
            options["target"] = target

        return jsii.invoke(self, "onEvent", [id, options])

    @jsii.member(jsii_name="onReEvaluationStatus")
    def on_re_evaluation_status(self, id: str, *, description: typing.Optional[str]=None, event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern]=None, rule_name: typing.Optional[str]=None, target: typing.Optional[aws_cdk.aws_events.IRuleTarget]=None) -> aws_cdk.aws_events.Rule:
        """Defines a CloudWatch event rule which triggers for rule re-evaluation status events.

        Arguments:
            id: -
            options: -
            description: A description of the rule's purpose. Default: - No description
            event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
            rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
            target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.

        Stability:
            experimental
        """
        options: aws_cdk.aws_events.OnEventOptions = {}

        if description is not None:
            options["description"] = description

        if event_pattern is not None:
            options["eventPattern"] = event_pattern

        if rule_name is not None:
            options["ruleName"] = rule_name

        if target is not None:
            options["target"] = target

        return jsii.invoke(self, "onReEvaluationStatus", [id, options])

    @jsii.member(jsii_name="scopeToResource")
    def scope_to_resource(self, type: str, identifier: typing.Optional[str]=None) -> None:
        """Restrict scope of changes to a specific resource.

        Arguments:
            type: the resource type.
            identifier: the resource identifier.

        See:
            https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources
        Stability:
            experimental
        """
        return jsii.invoke(self, "scopeToResource", [type, identifier])

    @jsii.member(jsii_name="scopeToResources")
    def scope_to_resources(self, *types: str) -> None:
        """Restrict scope of changes to specific resource types.

        Arguments:
            types: resource types.

        See:
            https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources
        Stability:
            experimental
        """
        return jsii.invoke(self, "scopeToResources", [*types])

    @jsii.member(jsii_name="scopeToTag")
    def scope_to_tag(self, key: str, value: typing.Optional[str]=None) -> None:
        """Restrict scope of changes to a specific tag.

        Arguments:
            key: the tag key.
            value: the tag value.

        Stability:
            experimental
        """
        return jsii.invoke(self, "scopeToTag", [key, value])

    @property
    @jsii.member(jsii_name="configRuleArn")
    def config_rule_arn(self) -> str:
        """The arn of the rule.

        Stability:
            experimental
        attribute:
            true
        """
        return jsii.get(self, "configRuleArn")

    @property
    @jsii.member(jsii_name="configRuleComplianceType")
    def config_rule_compliance_type(self) -> str:
        """The compliance status of the rule.

        Stability:
            experimental
        attribute:
            true
        """
        return jsii.get(self, "configRuleComplianceType")

    @property
    @jsii.member(jsii_name="configRuleId")
    def config_rule_id(self) -> str:
        """The id of the rule.

        Stability:
            experimental
        attribute:
            true
        """
        return jsii.get(self, "configRuleId")

    @property
    @jsii.member(jsii_name="configRuleName")
    def config_rule_name(self) -> str:
        """The name of the rule.

        Stability:
            experimental
        attribute:
            true
        """
        return jsii.get(self, "configRuleName")

    @property
    @jsii.member(jsii_name="isCustomWithChanges")
    def _is_custom_with_changes(self) -> typing.Optional[bool]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "isCustomWithChanges")

    @_is_custom_with_changes.setter
    def _is_custom_with_changes(self, value: typing.Optional[bool]):
        return jsii.set(self, "isCustomWithChanges", value)

    @property
    @jsii.member(jsii_name="isManaged")
    def _is_managed(self) -> typing.Optional[bool]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "isManaged")

    @_is_managed.setter
    def _is_managed(self, value: typing.Optional[bool]):
        return jsii.set(self, "isManaged", value)

    @property
    @jsii.member(jsii_name="scope")
    def _scope(self) -> typing.Optional["CfnConfigRule.ScopeProperty"]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "scope")

    @_scope.setter
    def _scope(self, value: typing.Optional["CfnConfigRule.ScopeProperty"]):
        return jsii.set(self, "scope", value)


class AccessKeysRotated(ManagedRule, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-config.AccessKeysRotated"):
    """Checks whether the active access keys are rotated within the number of days specified in ``maxAge``.

    See:
        https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html
    Stability:
        experimental
    resource:
        AWS::Config::ConfigRule
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, max_age: typing.Optional[aws_cdk.core.Duration]=None, config_rule_name: typing.Optional[str]=None, description: typing.Optional[str]=None, input_parameters: typing.Optional[typing.Mapping[str,typing.Any]]=None, maximum_execution_frequency: typing.Optional["MaximumExecutionFrequency"]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            max_age: The maximum number of days within which the access keys must be rotated. Default: Duration.days(90)
            config_rule_name: A name for the AWS Config rule. Default: a CloudFormation generated name
            description: A description about this AWS Config rule. Default: no description
            input_parameters: Input parameter values that are passed to the AWS Config rule. Default: no input parameters
            maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: 24 hours

        Stability:
            experimental
        """
        props: AccessKeysRotatedProps = {}

        if max_age is not None:
            props["maxAge"] = max_age

        if config_rule_name is not None:
            props["configRuleName"] = config_rule_name

        if description is not None:
            props["description"] = description

        if input_parameters is not None:
            props["inputParameters"] = input_parameters

        if maximum_execution_frequency is not None:
            props["maximumExecutionFrequency"] = maximum_execution_frequency

        jsii.create(AccessKeysRotated, self, [scope, id, props])


class CloudFormationStackDriftDetectionCheck(ManagedRule, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-config.CloudFormationStackDriftDetectionCheck"):
    """Checks whether your CloudFormation stacks' actual configuration differs, or has drifted, from its expected configuration.

    See:
        https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-stack-drift-detection-check.html
    Stability:
        experimental
    resource:
        AWS::Config::ConfigRule
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, own_stack_only: typing.Optional[bool]=None, role: typing.Optional[aws_cdk.aws_iam.IRole]=None, config_rule_name: typing.Optional[str]=None, description: typing.Optional[str]=None, input_parameters: typing.Optional[typing.Mapping[str,typing.Any]]=None, maximum_execution_frequency: typing.Optional["MaximumExecutionFrequency"]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            own_stack_only: Whether to check only the stack where this rule is deployed. Default: false
            role: The IAM role to use for this rule. It must have permissions to detect drift for AWS CloudFormation stacks. Ensure to attach ``config.amazonaws.com`` trusted permissions and ``ReadOnlyAccess`` policy permissions. For specific policy permissions, refer to https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html. Default: a role will be created
            config_rule_name: A name for the AWS Config rule. Default: a CloudFormation generated name
            description: A description about this AWS Config rule. Default: no description
            input_parameters: Input parameter values that are passed to the AWS Config rule. Default: no input parameters
            maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: 24 hours

        Stability:
            experimental
        """
        props: CloudFormationStackDriftDetectionCheckProps = {}

        if own_stack_only is not None:
            props["ownStackOnly"] = own_stack_only

        if role is not None:
            props["role"] = role

        if config_rule_name is not None:
            props["configRuleName"] = config_rule_name

        if description is not None:
            props["description"] = description

        if input_parameters is not None:
            props["inputParameters"] = input_parameters

        if maximum_execution_frequency is not None:
            props["maximumExecutionFrequency"] = maximum_execution_frequency

        jsii.create(CloudFormationStackDriftDetectionCheck, self, [scope, id, props])


class CloudFormationStackNotificationCheck(ManagedRule, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-config.CloudFormationStackNotificationCheck"):
    """Checks whether your CloudFormation stacks are sending event notifications to a SNS topic.

    Optionally checks whether specified SNS topics are used.

    See:
        https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-stack-notification-check.html
    Stability:
        experimental
    resource:
        AWS::Config::ConfigRule
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, topics: typing.Optional[typing.List[aws_cdk.aws_sns.ITopic]]=None, config_rule_name: typing.Optional[str]=None, description: typing.Optional[str]=None, input_parameters: typing.Optional[typing.Mapping[str,typing.Any]]=None, maximum_execution_frequency: typing.Optional["MaximumExecutionFrequency"]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            topics: A list of allowed topics. At most 5 topics. Default: - No topics.
            config_rule_name: A name for the AWS Config rule. Default: a CloudFormation generated name
            description: A description about this AWS Config rule. Default: no description
            input_parameters: Input parameter values that are passed to the AWS Config rule. Default: no input parameters
            maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: 24 hours

        Stability:
            experimental
        """
        props: CloudFormationStackNotificationCheckProps = {}

        if topics is not None:
            props["topics"] = topics

        if config_rule_name is not None:
            props["configRuleName"] = config_rule_name

        if description is not None:
            props["description"] = description

        if input_parameters is not None:
            props["inputParameters"] = input_parameters

        if maximum_execution_frequency is not None:
            props["maximumExecutionFrequency"] = maximum_execution_frequency

        jsii.create(CloudFormationStackNotificationCheck, self, [scope, id, props])


@jsii.enum(jsii_type="@aws-cdk/aws-config.MaximumExecutionFrequency")
class MaximumExecutionFrequency(enum.Enum):
    """The maximum frequency at which the AWS Config rule runs evaluations.

    Stability:
        experimental
    """
    ONE_HOUR = "ONE_HOUR"
    """
    Stability:
        experimental
    """
    THREE_HOURS = "THREE_HOURS"
    """
    Stability:
        experimental
    """
    SIX_HOURS = "SIX_HOURS"
    """
    Stability:
        experimental
    """
    TWELVE_HOURS = "TWELVE_HOURS"
    """
    Stability:
        experimental
    """
    TWENTY_FOUR_HOURS = "TWENTY_FOUR_HOURS"
    """
    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-config.RuleProps", jsii_struct_bases=[])
class RuleProps(jsii.compat.TypedDict, total=False):
    """Construction properties for a new rule.

    Stability:
        experimental
    """
    configRuleName: str
    """A name for the AWS Config rule.

    Default:
        a CloudFormation generated name

    Stability:
        experimental
    """

    description: str
    """A description about this AWS Config rule.

    Default:
        no description

    Stability:
        experimental
    """

    inputParameters: typing.Mapping[str,typing.Any]
    """Input parameter values that are passed to the AWS Config rule.

    Default:
        no input parameters

    Stability:
        experimental
    """

    maximumExecutionFrequency: "MaximumExecutionFrequency"
    """The maximum frequency at which the AWS Config rule runs evaluations.

    Default:
        24 hours

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-config.AccessKeysRotatedProps", jsii_struct_bases=[RuleProps])
class AccessKeysRotatedProps(RuleProps, jsii.compat.TypedDict, total=False):
    """Construction properties for a AccessKeysRotated.

    Stability:
        experimental
    """
    maxAge: aws_cdk.core.Duration
    """The maximum number of days within which the access keys must be rotated.

    Default:
        Duration.days(90)

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-config.CloudFormationStackDriftDetectionCheckProps", jsii_struct_bases=[RuleProps])
class CloudFormationStackDriftDetectionCheckProps(RuleProps, jsii.compat.TypedDict, total=False):
    """Construction properties for a CloudFormationStackDriftDetectionCheck.

    Stability:
        experimental
    """
    ownStackOnly: bool
    """Whether to check only the stack where this rule is deployed.

    Default:
        false

    Stability:
        experimental
    """

    role: aws_cdk.aws_iam.IRole
    """The IAM role to use for this rule.

    It must have permissions to detect drift
    for AWS CloudFormation stacks. Ensure to attach ``config.amazonaws.com`` trusted
    permissions and ``ReadOnlyAccess`` policy permissions. For specific policy permissions,
    refer to https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html.

    Default:
        a role will be created

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-config.CloudFormationStackNotificationCheckProps", jsii_struct_bases=[RuleProps])
class CloudFormationStackNotificationCheckProps(RuleProps, jsii.compat.TypedDict, total=False):
    """Construction properties for a CloudFormationStackNotificationCheck.

    Stability:
        experimental
    """
    topics: typing.List[aws_cdk.aws_sns.ITopic]
    """A list of allowed topics.

    At most 5 topics.

    Default:
        - No topics.

    Stability:
        experimental
    """

@jsii.data_type_optionals(jsii_struct_bases=[RuleProps])
class _CustomRuleProps(RuleProps, jsii.compat.TypedDict, total=False):
    configurationChanges: bool
    """Whether to run the rule on configuration changes.

    Default:
        false

    Stability:
        experimental
    """
    periodic: bool
    """Whether to run the rule on a fixed frequency.

    Default:
        false

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-config.CustomRuleProps", jsii_struct_bases=[_CustomRuleProps])
class CustomRuleProps(_CustomRuleProps):
    """Consruction properties for a CustomRule.

    Stability:
        experimental
    """
    lambdaFunction: aws_cdk.aws_lambda.IFunction
    """The Lambda function to run.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-config.ManagedRuleProps", jsii_struct_bases=[RuleProps])
class ManagedRuleProps(RuleProps, jsii.compat.TypedDict):
    """Construction properties for a ManagedRule.

    Stability:
        experimental
    """
    identifier: str
    """The identifier of the AWS managed rule.

    See:
        https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html
    Stability:
        experimental
    """

__all__ = ["AccessKeysRotated", "AccessKeysRotatedProps", "CfnAggregationAuthorization", "CfnAggregationAuthorizationProps", "CfnConfigRule", "CfnConfigRuleProps", "CfnConfigurationAggregator", "CfnConfigurationAggregatorProps", "CfnConfigurationRecorder", "CfnConfigurationRecorderProps", "CfnDeliveryChannel", "CfnDeliveryChannelProps", "CloudFormationStackDriftDetectionCheck", "CloudFormationStackDriftDetectionCheckProps", "CloudFormationStackNotificationCheck", "CloudFormationStackNotificationCheckProps", "CustomRule", "CustomRuleProps", "IRule", "ManagedRule", "ManagedRuleProps", "MaximumExecutionFrequency", "RuleProps", "__jsii_assembly__"]

publication.publish()
