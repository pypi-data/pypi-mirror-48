import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_autoscaling
import aws_cdk.aws_cloudwatch
import aws_cdk.aws_elasticloadbalancing
import aws_cdk.aws_elasticloadbalancingv2
import aws_cdk.aws_iam
import aws_cdk.aws_lambda
import aws_cdk.aws_s3
import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-codedeploy", "0.36.2", __name__, "aws-codedeploy@0.36.2.jsii.tgz")
@jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.AutoRollbackConfig", jsii_struct_bases=[])
class AutoRollbackConfig(jsii.compat.TypedDict, total=False):
    """The configuration for automatically rolling back deployments in a given Deployment Group.

    Stability:
        stable
    """
    deploymentInAlarm: bool
    """Whether to automatically roll back a deployment during which one of the configured CloudWatch alarms for this Deployment Group went off.

    Default:
        true if you've provided any Alarms with the ``alarms`` property, false otherwise

    Stability:
        stable
    """

    failedDeployment: bool
    """Whether to automatically roll back a deployment that fails.

    Default:
        true

    Stability:
        stable
    """

    stoppedDeployment: bool
    """Whether to automatically roll back a deployment that was manually stopped.

    Default:
        false

    Stability:
        stable
    """

class CfnApplication(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codedeploy.CfnApplication"):
    """A CloudFormation ``AWS::CodeDeploy::Application``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html
    Stability:
        stable
    cloudformationResource:
        AWS::CodeDeploy::Application
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, application_name: typing.Optional[str]=None, compute_platform: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::CodeDeploy::Application``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            application_name: ``AWS::CodeDeploy::Application.ApplicationName``.
            compute_platform: ``AWS::CodeDeploy::Application.ComputePlatform``.

        Stability:
            stable
        """
        props: CfnApplicationProps = {}

        if application_name is not None:
            props["applicationName"] = application_name

        if compute_platform is not None:
            props["computePlatform"] = compute_platform

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
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> typing.Optional[str]:
        """``AWS::CodeDeploy::Application.ApplicationName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html#cfn-codedeploy-application-applicationname
        Stability:
            stable
        """
        return jsii.get(self, "applicationName")

    @application_name.setter
    def application_name(self, value: typing.Optional[str]):
        return jsii.set(self, "applicationName", value)

    @property
    @jsii.member(jsii_name="computePlatform")
    def compute_platform(self) -> typing.Optional[str]:
        """``AWS::CodeDeploy::Application.ComputePlatform``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html#cfn-codedeploy-application-computeplatform
        Stability:
            stable
        """
        return jsii.get(self, "computePlatform")

    @compute_platform.setter
    def compute_platform(self, value: typing.Optional[str]):
        return jsii.set(self, "computePlatform", value)


@jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnApplicationProps", jsii_struct_bases=[])
class CfnApplicationProps(jsii.compat.TypedDict, total=False):
    """Properties for defining a ``AWS::CodeDeploy::Application``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html
    Stability:
        stable
    """
    applicationName: str
    """``AWS::CodeDeploy::Application.ApplicationName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html#cfn-codedeploy-application-applicationname
    Stability:
        stable
    """

    computePlatform: str
    """``AWS::CodeDeploy::Application.ComputePlatform``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html#cfn-codedeploy-application-computeplatform
    Stability:
        stable
    """

class CfnDeploymentConfig(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentConfig"):
    """A CloudFormation ``AWS::CodeDeploy::DeploymentConfig``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html
    Stability:
        stable
    cloudformationResource:
        AWS::CodeDeploy::DeploymentConfig
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, deployment_config_name: typing.Optional[str]=None, minimum_healthy_hosts: typing.Optional[typing.Union[typing.Optional["MinimumHealthyHostsProperty"], typing.Optional[aws_cdk.core.IResolvable]]]=None) -> None:
        """Create a new ``AWS::CodeDeploy::DeploymentConfig``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            deployment_config_name: ``AWS::CodeDeploy::DeploymentConfig.DeploymentConfigName``.
            minimum_healthy_hosts: ``AWS::CodeDeploy::DeploymentConfig.MinimumHealthyHosts``.

        Stability:
            stable
        """
        props: CfnDeploymentConfigProps = {}

        if deployment_config_name is not None:
            props["deploymentConfigName"] = deployment_config_name

        if minimum_healthy_hosts is not None:
            props["minimumHealthyHosts"] = minimum_healthy_hosts

        jsii.create(CfnDeploymentConfig, self, [scope, id, props])

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
    @jsii.member(jsii_name="deploymentConfigName")
    def deployment_config_name(self) -> typing.Optional[str]:
        """``AWS::CodeDeploy::DeploymentConfig.DeploymentConfigName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html#cfn-codedeploy-deploymentconfig-deploymentconfigname
        Stability:
            stable
        """
        return jsii.get(self, "deploymentConfigName")

    @deployment_config_name.setter
    def deployment_config_name(self, value: typing.Optional[str]):
        return jsii.set(self, "deploymentConfigName", value)

    @property
    @jsii.member(jsii_name="minimumHealthyHosts")
    def minimum_healthy_hosts(self) -> typing.Optional[typing.Union[typing.Optional["MinimumHealthyHostsProperty"], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::CodeDeploy::DeploymentConfig.MinimumHealthyHosts``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html#cfn-codedeploy-deploymentconfig-minimumhealthyhosts
        Stability:
            stable
        """
        return jsii.get(self, "minimumHealthyHosts")

    @minimum_healthy_hosts.setter
    def minimum_healthy_hosts(self, value: typing.Optional[typing.Union[typing.Optional["MinimumHealthyHostsProperty"], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "minimumHealthyHosts", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentConfig.MinimumHealthyHostsProperty", jsii_struct_bases=[])
    class MinimumHealthyHostsProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts.html
        Stability:
            stable
        """
        type: str
        """``CfnDeploymentConfig.MinimumHealthyHostsProperty.Type``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts.html#cfn-codedeploy-deploymentconfig-minimumhealthyhosts-type
        Stability:
            stable
        """

        value: jsii.Number
        """``CfnDeploymentConfig.MinimumHealthyHostsProperty.Value``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts.html#cfn-codedeploy-deploymentconfig-minimumhealthyhosts-value
        Stability:
            stable
        """


@jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentConfigProps", jsii_struct_bases=[])
class CfnDeploymentConfigProps(jsii.compat.TypedDict, total=False):
    """Properties for defining a ``AWS::CodeDeploy::DeploymentConfig``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html
    Stability:
        stable
    """
    deploymentConfigName: str
    """``AWS::CodeDeploy::DeploymentConfig.DeploymentConfigName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html#cfn-codedeploy-deploymentconfig-deploymentconfigname
    Stability:
        stable
    """

    minimumHealthyHosts: typing.Union["CfnDeploymentConfig.MinimumHealthyHostsProperty", aws_cdk.core.IResolvable]
    """``AWS::CodeDeploy::DeploymentConfig.MinimumHealthyHosts``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html#cfn-codedeploy-deploymentconfig-minimumhealthyhosts
    Stability:
        stable
    """

class CfnDeploymentGroup(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentGroup"):
    """A CloudFormation ``AWS::CodeDeploy::DeploymentGroup``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html
    Stability:
        stable
    cloudformationResource:
        AWS::CodeDeploy::DeploymentGroup
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, application_name: str, service_role_arn: str, alarm_configuration: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AlarmConfigurationProperty"]]]=None, auto_rollback_configuration: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AutoRollbackConfigurationProperty"]]]=None, auto_scaling_groups: typing.Optional[typing.List[str]]=None, deployment: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["DeploymentProperty"]]]=None, deployment_config_name: typing.Optional[str]=None, deployment_group_name: typing.Optional[str]=None, deployment_style: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["DeploymentStyleProperty"]]]=None, ec2_tag_filters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "EC2TagFilterProperty"]]]]]=None, ec2_tag_set: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["EC2TagSetProperty"]]]=None, load_balancer_info: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["LoadBalancerInfoProperty"]]]=None, on_premises_instance_tag_filters: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TagFilterProperty"]]]]]=None, on_premises_tag_set: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["OnPremisesTagSetProperty"]]]=None, trigger_configurations: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TriggerConfigProperty"]]]]]=None) -> None:
        """Create a new ``AWS::CodeDeploy::DeploymentGroup``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            application_name: ``AWS::CodeDeploy::DeploymentGroup.ApplicationName``.
            service_role_arn: ``AWS::CodeDeploy::DeploymentGroup.ServiceRoleArn``.
            alarm_configuration: ``AWS::CodeDeploy::DeploymentGroup.AlarmConfiguration``.
            auto_rollback_configuration: ``AWS::CodeDeploy::DeploymentGroup.AutoRollbackConfiguration``.
            auto_scaling_groups: ``AWS::CodeDeploy::DeploymentGroup.AutoScalingGroups``.
            deployment: ``AWS::CodeDeploy::DeploymentGroup.Deployment``.
            deployment_config_name: ``AWS::CodeDeploy::DeploymentGroup.DeploymentConfigName``.
            deployment_group_name: ``AWS::CodeDeploy::DeploymentGroup.DeploymentGroupName``.
            deployment_style: ``AWS::CodeDeploy::DeploymentGroup.DeploymentStyle``.
            ec2_tag_filters: ``AWS::CodeDeploy::DeploymentGroup.Ec2TagFilters``.
            ec2_tag_set: ``AWS::CodeDeploy::DeploymentGroup.Ec2TagSet``.
            load_balancer_info: ``AWS::CodeDeploy::DeploymentGroup.LoadBalancerInfo``.
            on_premises_instance_tag_filters: ``AWS::CodeDeploy::DeploymentGroup.OnPremisesInstanceTagFilters``.
            on_premises_tag_set: ``AWS::CodeDeploy::DeploymentGroup.OnPremisesTagSet``.
            trigger_configurations: ``AWS::CodeDeploy::DeploymentGroup.TriggerConfigurations``.

        Stability:
            stable
        """
        props: CfnDeploymentGroupProps = {"applicationName": application_name, "serviceRoleArn": service_role_arn}

        if alarm_configuration is not None:
            props["alarmConfiguration"] = alarm_configuration

        if auto_rollback_configuration is not None:
            props["autoRollbackConfiguration"] = auto_rollback_configuration

        if auto_scaling_groups is not None:
            props["autoScalingGroups"] = auto_scaling_groups

        if deployment is not None:
            props["deployment"] = deployment

        if deployment_config_name is not None:
            props["deploymentConfigName"] = deployment_config_name

        if deployment_group_name is not None:
            props["deploymentGroupName"] = deployment_group_name

        if deployment_style is not None:
            props["deploymentStyle"] = deployment_style

        if ec2_tag_filters is not None:
            props["ec2TagFilters"] = ec2_tag_filters

        if ec2_tag_set is not None:
            props["ec2TagSet"] = ec2_tag_set

        if load_balancer_info is not None:
            props["loadBalancerInfo"] = load_balancer_info

        if on_premises_instance_tag_filters is not None:
            props["onPremisesInstanceTagFilters"] = on_premises_instance_tag_filters

        if on_premises_tag_set is not None:
            props["onPremisesTagSet"] = on_premises_tag_set

        if trigger_configurations is not None:
            props["triggerConfigurations"] = trigger_configurations

        jsii.create(CfnDeploymentGroup, self, [scope, id, props])

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
        """``AWS::CodeDeploy::DeploymentGroup.ApplicationName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-applicationname
        Stability:
            stable
        """
        return jsii.get(self, "applicationName")

    @application_name.setter
    def application_name(self, value: str):
        return jsii.set(self, "applicationName", value)

    @property
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> str:
        """``AWS::CodeDeploy::DeploymentGroup.ServiceRoleArn``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-servicerolearn
        Stability:
            stable
        """
        return jsii.get(self, "serviceRoleArn")

    @service_role_arn.setter
    def service_role_arn(self, value: str):
        return jsii.set(self, "serviceRoleArn", value)

    @property
    @jsii.member(jsii_name="alarmConfiguration")
    def alarm_configuration(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AlarmConfigurationProperty"]]]:
        """``AWS::CodeDeploy::DeploymentGroup.AlarmConfiguration``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-alarmconfiguration
        Stability:
            stable
        """
        return jsii.get(self, "alarmConfiguration")

    @alarm_configuration.setter
    def alarm_configuration(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AlarmConfigurationProperty"]]]):
        return jsii.set(self, "alarmConfiguration", value)

    @property
    @jsii.member(jsii_name="autoRollbackConfiguration")
    def auto_rollback_configuration(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AutoRollbackConfigurationProperty"]]]:
        """``AWS::CodeDeploy::DeploymentGroup.AutoRollbackConfiguration``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-autorollbackconfiguration
        Stability:
            stable
        """
        return jsii.get(self, "autoRollbackConfiguration")

    @auto_rollback_configuration.setter
    def auto_rollback_configuration(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AutoRollbackConfigurationProperty"]]]):
        return jsii.set(self, "autoRollbackConfiguration", value)

    @property
    @jsii.member(jsii_name="autoScalingGroups")
    def auto_scaling_groups(self) -> typing.Optional[typing.List[str]]:
        """``AWS::CodeDeploy::DeploymentGroup.AutoScalingGroups``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-autoscalinggroups
        Stability:
            stable
        """
        return jsii.get(self, "autoScalingGroups")

    @auto_scaling_groups.setter
    def auto_scaling_groups(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "autoScalingGroups", value)

    @property
    @jsii.member(jsii_name="deployment")
    def deployment(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["DeploymentProperty"]]]:
        """``AWS::CodeDeploy::DeploymentGroup.Deployment``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deployment
        Stability:
            stable
        """
        return jsii.get(self, "deployment")

    @deployment.setter
    def deployment(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["DeploymentProperty"]]]):
        return jsii.set(self, "deployment", value)

    @property
    @jsii.member(jsii_name="deploymentConfigName")
    def deployment_config_name(self) -> typing.Optional[str]:
        """``AWS::CodeDeploy::DeploymentGroup.DeploymentConfigName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deploymentconfigname
        Stability:
            stable
        """
        return jsii.get(self, "deploymentConfigName")

    @deployment_config_name.setter
    def deployment_config_name(self, value: typing.Optional[str]):
        return jsii.set(self, "deploymentConfigName", value)

    @property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> typing.Optional[str]:
        """``AWS::CodeDeploy::DeploymentGroup.DeploymentGroupName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deploymentgroupname
        Stability:
            stable
        """
        return jsii.get(self, "deploymentGroupName")

    @deployment_group_name.setter
    def deployment_group_name(self, value: typing.Optional[str]):
        return jsii.set(self, "deploymentGroupName", value)

    @property
    @jsii.member(jsii_name="deploymentStyle")
    def deployment_style(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["DeploymentStyleProperty"]]]:
        """``AWS::CodeDeploy::DeploymentGroup.DeploymentStyle``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deploymentstyle
        Stability:
            stable
        """
        return jsii.get(self, "deploymentStyle")

    @deployment_style.setter
    def deployment_style(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["DeploymentStyleProperty"]]]):
        return jsii.set(self, "deploymentStyle", value)

    @property
    @jsii.member(jsii_name="ec2TagFilters")
    def ec2_tag_filters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "EC2TagFilterProperty"]]]]]:
        """``AWS::CodeDeploy::DeploymentGroup.Ec2TagFilters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-ec2tagfilters
        Stability:
            stable
        """
        return jsii.get(self, "ec2TagFilters")

    @ec2_tag_filters.setter
    def ec2_tag_filters(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "EC2TagFilterProperty"]]]]]):
        return jsii.set(self, "ec2TagFilters", value)

    @property
    @jsii.member(jsii_name="ec2TagSet")
    def ec2_tag_set(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["EC2TagSetProperty"]]]:
        """``AWS::CodeDeploy::DeploymentGroup.Ec2TagSet``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-ec2tagset
        Stability:
            stable
        """
        return jsii.get(self, "ec2TagSet")

    @ec2_tag_set.setter
    def ec2_tag_set(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["EC2TagSetProperty"]]]):
        return jsii.set(self, "ec2TagSet", value)

    @property
    @jsii.member(jsii_name="loadBalancerInfo")
    def load_balancer_info(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["LoadBalancerInfoProperty"]]]:
        """``AWS::CodeDeploy::DeploymentGroup.LoadBalancerInfo``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-loadbalancerinfo
        Stability:
            stable
        """
        return jsii.get(self, "loadBalancerInfo")

    @load_balancer_info.setter
    def load_balancer_info(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["LoadBalancerInfoProperty"]]]):
        return jsii.set(self, "loadBalancerInfo", value)

    @property
    @jsii.member(jsii_name="onPremisesInstanceTagFilters")
    def on_premises_instance_tag_filters(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TagFilterProperty"]]]]]:
        """``AWS::CodeDeploy::DeploymentGroup.OnPremisesInstanceTagFilters``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-onpremisesinstancetagfilters
        Stability:
            stable
        """
        return jsii.get(self, "onPremisesInstanceTagFilters")

    @on_premises_instance_tag_filters.setter
    def on_premises_instance_tag_filters(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TagFilterProperty"]]]]]):
        return jsii.set(self, "onPremisesInstanceTagFilters", value)

    @property
    @jsii.member(jsii_name="onPremisesTagSet")
    def on_premises_tag_set(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["OnPremisesTagSetProperty"]]]:
        """``AWS::CodeDeploy::DeploymentGroup.OnPremisesTagSet``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-onpremisestagset
        Stability:
            stable
        """
        return jsii.get(self, "onPremisesTagSet")

    @on_premises_tag_set.setter
    def on_premises_tag_set(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["OnPremisesTagSetProperty"]]]):
        return jsii.set(self, "onPremisesTagSet", value)

    @property
    @jsii.member(jsii_name="triggerConfigurations")
    def trigger_configurations(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TriggerConfigProperty"]]]]]:
        """``AWS::CodeDeploy::DeploymentGroup.TriggerConfigurations``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-triggerconfigurations
        Stability:
            stable
        """
        return jsii.get(self, "triggerConfigurations")

    @trigger_configurations.setter
    def trigger_configurations(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "TriggerConfigProperty"]]]]]):
        return jsii.set(self, "triggerConfigurations", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentGroup.AlarmConfigurationProperty", jsii_struct_bases=[])
    class AlarmConfigurationProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html
        Stability:
            stable
        """
        alarms: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDeploymentGroup.AlarmProperty"]]]
        """``CfnDeploymentGroup.AlarmConfigurationProperty.Alarms``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html#cfn-codedeploy-deploymentgroup-alarmconfiguration-alarms
        Stability:
            stable
        """

        enabled: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnDeploymentGroup.AlarmConfigurationProperty.Enabled``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html#cfn-codedeploy-deploymentgroup-alarmconfiguration-enabled
        Stability:
            stable
        """

        ignorePollAlarmFailure: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnDeploymentGroup.AlarmConfigurationProperty.IgnorePollAlarmFailure``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html#cfn-codedeploy-deploymentgroup-alarmconfiguration-ignorepollalarmfailure
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentGroup.AlarmProperty", jsii_struct_bases=[])
    class AlarmProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarm.html
        Stability:
            stable
        """
        name: str
        """``CfnDeploymentGroup.AlarmProperty.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarm.html#cfn-codedeploy-deploymentgroup-alarm-name
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentGroup.AutoRollbackConfigurationProperty", jsii_struct_bases=[])
    class AutoRollbackConfigurationProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-autorollbackconfiguration.html
        Stability:
            stable
        """
        enabled: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnDeploymentGroup.AutoRollbackConfigurationProperty.Enabled``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-autorollbackconfiguration.html#cfn-codedeploy-deploymentgroup-autorollbackconfiguration-enabled
        Stability:
            stable
        """

        events: typing.List[str]
        """``CfnDeploymentGroup.AutoRollbackConfigurationProperty.Events``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-autorollbackconfiguration.html#cfn-codedeploy-deploymentgroup-autorollbackconfiguration-events
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _DeploymentProperty(jsii.compat.TypedDict, total=False):
        description: str
        """``CfnDeploymentGroup.DeploymentProperty.Description``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment.html#cfn-properties-codedeploy-deploymentgroup-deployment-description
        Stability:
            stable
        """
        ignoreApplicationStopFailures: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnDeploymentGroup.DeploymentProperty.IgnoreApplicationStopFailures``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment.html#cfn-properties-codedeploy-deploymentgroup-deployment-ignoreapplicationstopfailures
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentGroup.DeploymentProperty", jsii_struct_bases=[_DeploymentProperty])
    class DeploymentProperty(_DeploymentProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment.html
        Stability:
            stable
        """
        revision: typing.Union[aws_cdk.core.IResolvable, "CfnDeploymentGroup.RevisionLocationProperty"]
        """``CfnDeploymentGroup.DeploymentProperty.Revision``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentGroup.DeploymentStyleProperty", jsii_struct_bases=[])
    class DeploymentStyleProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentstyle.html
        Stability:
            stable
        """
        deploymentOption: str
        """``CfnDeploymentGroup.DeploymentStyleProperty.DeploymentOption``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentstyle.html#cfn-codedeploy-deploymentgroup-deploymentstyle-deploymentoption
        Stability:
            stable
        """

        deploymentType: str
        """``CfnDeploymentGroup.DeploymentStyleProperty.DeploymentType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentstyle.html#cfn-codedeploy-deploymentgroup-deploymentstyle-deploymenttype
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentGroup.EC2TagFilterProperty", jsii_struct_bases=[])
    class EC2TagFilterProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html
        Stability:
            stable
        """
        key: str
        """``CfnDeploymentGroup.EC2TagFilterProperty.Key``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html#cfn-codedeploy-deploymentgroup-ec2tagfilter-key
        Stability:
            stable
        """

        type: str
        """``CfnDeploymentGroup.EC2TagFilterProperty.Type``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html#cfn-codedeploy-deploymentgroup-ec2tagfilter-type
        Stability:
            stable
        """

        value: str
        """``CfnDeploymentGroup.EC2TagFilterProperty.Value``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html#cfn-codedeploy-deploymentgroup-ec2tagfilter-value
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentGroup.EC2TagSetListObjectProperty", jsii_struct_bases=[])
    class EC2TagSetListObjectProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagsetlistobject.html
        Stability:
            stable
        """
        ec2TagGroup: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDeploymentGroup.EC2TagFilterProperty"]]]
        """``CfnDeploymentGroup.EC2TagSetListObjectProperty.Ec2TagGroup``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagsetlistobject.html#cfn-codedeploy-deploymentgroup-ec2tagsetlistobject-ec2taggroup
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentGroup.EC2TagSetProperty", jsii_struct_bases=[])
    class EC2TagSetProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagset.html
        Stability:
            stable
        """
        ec2TagSetList: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDeploymentGroup.EC2TagSetListObjectProperty"]]]
        """``CfnDeploymentGroup.EC2TagSetProperty.Ec2TagSetList``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagset.html#cfn-codedeploy-deploymentgroup-ec2tagset-ec2tagsetlist
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentGroup.ELBInfoProperty", jsii_struct_bases=[])
    class ELBInfoProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-elbinfo.html
        Stability:
            stable
        """
        name: str
        """``CfnDeploymentGroup.ELBInfoProperty.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-elbinfo.html#cfn-codedeploy-deploymentgroup-elbinfo-name
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentGroup.GitHubLocationProperty", jsii_struct_bases=[])
    class GitHubLocationProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-githublocation.html
        Stability:
            stable
        """
        commitId: str
        """``CfnDeploymentGroup.GitHubLocationProperty.CommitId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-githublocation.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-githublocation-commitid
        Stability:
            stable
        """

        repository: str
        """``CfnDeploymentGroup.GitHubLocationProperty.Repository``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-githublocation.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-githublocation-repository
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentGroup.LoadBalancerInfoProperty", jsii_struct_bases=[])
    class LoadBalancerInfoProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html
        Stability:
            stable
        """
        elbInfoList: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDeploymentGroup.ELBInfoProperty"]]]
        """``CfnDeploymentGroup.LoadBalancerInfoProperty.ElbInfoList``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html#cfn-codedeploy-deploymentgroup-loadbalancerinfo-elbinfolist
        Stability:
            stable
        """

        targetGroupInfoList: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDeploymentGroup.TargetGroupInfoProperty"]]]
        """``CfnDeploymentGroup.LoadBalancerInfoProperty.TargetGroupInfoList``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html#cfn-codedeploy-deploymentgroup-loadbalancerinfo-targetgroupinfolist
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentGroup.OnPremisesTagSetListObjectProperty", jsii_struct_bases=[])
    class OnPremisesTagSetListObjectProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagsetlistobject.html
        Stability:
            stable
        """
        onPremisesTagGroup: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDeploymentGroup.TagFilterProperty"]]]
        """``CfnDeploymentGroup.OnPremisesTagSetListObjectProperty.OnPremisesTagGroup``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagsetlistobject.html#cfn-codedeploy-deploymentgroup-onpremisestagsetlistobject-onpremisestaggroup
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentGroup.OnPremisesTagSetProperty", jsii_struct_bases=[])
    class OnPremisesTagSetProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagset.html
        Stability:
            stable
        """
        onPremisesTagSetList: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDeploymentGroup.OnPremisesTagSetListObjectProperty"]]]
        """``CfnDeploymentGroup.OnPremisesTagSetProperty.OnPremisesTagSetList``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagset.html#cfn-codedeploy-deploymentgroup-onpremisestagset-onpremisestagsetlist
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentGroup.RevisionLocationProperty", jsii_struct_bases=[])
    class RevisionLocationProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision.html
        Stability:
            stable
        """
        gitHubLocation: typing.Union[aws_cdk.core.IResolvable, "CfnDeploymentGroup.GitHubLocationProperty"]
        """``CfnDeploymentGroup.RevisionLocationProperty.GitHubLocation``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-githublocation
        Stability:
            stable
        """

        revisionType: str
        """``CfnDeploymentGroup.RevisionLocationProperty.RevisionType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-revisiontype
        Stability:
            stable
        """

        s3Location: typing.Union[aws_cdk.core.IResolvable, "CfnDeploymentGroup.S3LocationProperty"]
        """``CfnDeploymentGroup.RevisionLocationProperty.S3Location``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _S3LocationProperty(jsii.compat.TypedDict, total=False):
        bundleType: str
        """``CfnDeploymentGroup.S3LocationProperty.BundleType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location-bundletype
        Stability:
            stable
        """
        eTag: str
        """``CfnDeploymentGroup.S3LocationProperty.ETag``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location-etag
        Stability:
            stable
        """
        version: str
        """``CfnDeploymentGroup.S3LocationProperty.Version``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location-value
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentGroup.S3LocationProperty", jsii_struct_bases=[_S3LocationProperty])
    class S3LocationProperty(_S3LocationProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html
        Stability:
            stable
        """
        bucket: str
        """``CfnDeploymentGroup.S3LocationProperty.Bucket``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location-bucket
        Stability:
            stable
        """

        key: str
        """``CfnDeploymentGroup.S3LocationProperty.Key``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html#cfn-properties-codedeploy-deploymentgroup-deployment-revision-s3location-key
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentGroup.TagFilterProperty", jsii_struct_bases=[])
    class TagFilterProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html
        Stability:
            stable
        """
        key: str
        """``CfnDeploymentGroup.TagFilterProperty.Key``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html#cfn-codedeploy-deploymentgroup-tagfilter-key
        Stability:
            stable
        """

        type: str
        """``CfnDeploymentGroup.TagFilterProperty.Type``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html#cfn-codedeploy-deploymentgroup-tagfilter-type
        Stability:
            stable
        """

        value: str
        """``CfnDeploymentGroup.TagFilterProperty.Value``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html#cfn-codedeploy-deploymentgroup-tagfilter-value
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentGroup.TargetGroupInfoProperty", jsii_struct_bases=[])
    class TargetGroupInfoProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-targetgroupinfo.html
        Stability:
            stable
        """
        name: str
        """``CfnDeploymentGroup.TargetGroupInfoProperty.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-targetgroupinfo.html#cfn-codedeploy-deploymentgroup-targetgroupinfo-name
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentGroup.TriggerConfigProperty", jsii_struct_bases=[])
    class TriggerConfigProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-triggerconfig.html
        Stability:
            stable
        """
        triggerEvents: typing.List[str]
        """``CfnDeploymentGroup.TriggerConfigProperty.TriggerEvents``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-triggerconfig.html#cfn-codedeploy-deploymentgroup-triggerconfig-triggerevents
        Stability:
            stable
        """

        triggerName: str
        """``CfnDeploymentGroup.TriggerConfigProperty.TriggerName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-triggerconfig.html#cfn-codedeploy-deploymentgroup-triggerconfig-triggername
        Stability:
            stable
        """

        triggerTargetArn: str
        """``CfnDeploymentGroup.TriggerConfigProperty.TriggerTargetArn``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-triggerconfig.html#cfn-codedeploy-deploymentgroup-triggerconfig-triggertargetarn
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnDeploymentGroupProps(jsii.compat.TypedDict, total=False):
    alarmConfiguration: typing.Union[aws_cdk.core.IResolvable, "CfnDeploymentGroup.AlarmConfigurationProperty"]
    """``AWS::CodeDeploy::DeploymentGroup.AlarmConfiguration``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-alarmconfiguration
    Stability:
        stable
    """
    autoRollbackConfiguration: typing.Union[aws_cdk.core.IResolvable, "CfnDeploymentGroup.AutoRollbackConfigurationProperty"]
    """``AWS::CodeDeploy::DeploymentGroup.AutoRollbackConfiguration``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-autorollbackconfiguration
    Stability:
        stable
    """
    autoScalingGroups: typing.List[str]
    """``AWS::CodeDeploy::DeploymentGroup.AutoScalingGroups``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-autoscalinggroups
    Stability:
        stable
    """
    deployment: typing.Union[aws_cdk.core.IResolvable, "CfnDeploymentGroup.DeploymentProperty"]
    """``AWS::CodeDeploy::DeploymentGroup.Deployment``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deployment
    Stability:
        stable
    """
    deploymentConfigName: str
    """``AWS::CodeDeploy::DeploymentGroup.DeploymentConfigName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deploymentconfigname
    Stability:
        stable
    """
    deploymentGroupName: str
    """``AWS::CodeDeploy::DeploymentGroup.DeploymentGroupName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deploymentgroupname
    Stability:
        stable
    """
    deploymentStyle: typing.Union[aws_cdk.core.IResolvable, "CfnDeploymentGroup.DeploymentStyleProperty"]
    """``AWS::CodeDeploy::DeploymentGroup.DeploymentStyle``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deploymentstyle
    Stability:
        stable
    """
    ec2TagFilters: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDeploymentGroup.EC2TagFilterProperty"]]]
    """``AWS::CodeDeploy::DeploymentGroup.Ec2TagFilters``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-ec2tagfilters
    Stability:
        stable
    """
    ec2TagSet: typing.Union[aws_cdk.core.IResolvable, "CfnDeploymentGroup.EC2TagSetProperty"]
    """``AWS::CodeDeploy::DeploymentGroup.Ec2TagSet``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-ec2tagset
    Stability:
        stable
    """
    loadBalancerInfo: typing.Union[aws_cdk.core.IResolvable, "CfnDeploymentGroup.LoadBalancerInfoProperty"]
    """``AWS::CodeDeploy::DeploymentGroup.LoadBalancerInfo``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-loadbalancerinfo
    Stability:
        stable
    """
    onPremisesInstanceTagFilters: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDeploymentGroup.TagFilterProperty"]]]
    """``AWS::CodeDeploy::DeploymentGroup.OnPremisesInstanceTagFilters``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-onpremisesinstancetagfilters
    Stability:
        stable
    """
    onPremisesTagSet: typing.Union[aws_cdk.core.IResolvable, "CfnDeploymentGroup.OnPremisesTagSetProperty"]
    """``AWS::CodeDeploy::DeploymentGroup.OnPremisesTagSet``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-onpremisestagset
    Stability:
        stable
    """
    triggerConfigurations: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnDeploymentGroup.TriggerConfigProperty"]]]
    """``AWS::CodeDeploy::DeploymentGroup.TriggerConfigurations``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-triggerconfigurations
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.CfnDeploymentGroupProps", jsii_struct_bases=[_CfnDeploymentGroupProps])
class CfnDeploymentGroupProps(_CfnDeploymentGroupProps):
    """Properties for defining a ``AWS::CodeDeploy::DeploymentGroup``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html
    Stability:
        stable
    """
    applicationName: str
    """``AWS::CodeDeploy::DeploymentGroup.ApplicationName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-applicationname
    Stability:
        stable
    """

    serviceRoleArn: str
    """``AWS::CodeDeploy::DeploymentGroup.ServiceRoleArn``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-servicerolearn
    Stability:
        stable
    """

@jsii.interface(jsii_type="@aws-cdk/aws-codedeploy.ILambdaApplication")
class ILambdaApplication(aws_cdk.core.IResource, jsii.compat.Protocol):
    """Represents a reference to a CodeDeploy Application deploying to AWS Lambda.

    If you're managing the Application alongside the rest of your CDK resources,
    use the {@link LambdaApplication} class.

    If you want to reference an already existing Application,
    or one defined in a different CDK Stack,
    use the {@link LambdaApplication#import} method.

    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _ILambdaApplicationProxy

    @property
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        ...

    @property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        ...


class _ILambdaApplicationProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """Represents a reference to a CodeDeploy Application deploying to AWS Lambda.

    If you're managing the Application alongside the rest of your CDK resources,
    use the {@link LambdaApplication} class.

    If you want to reference an already existing Application,
    or one defined in a different CDK Stack,
    use the {@link LambdaApplication#import} method.

    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-codedeploy.ILambdaApplication"
    @property
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "applicationArn")

    @property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "applicationName")


@jsii.interface(jsii_type="@aws-cdk/aws-codedeploy.ILambdaDeploymentConfig")
class ILambdaDeploymentConfig(jsii.compat.Protocol):
    """The Deployment Configuration of a Lambda Deployment Group. The default, pre-defined Configurations are available as constants on the {@link LambdaDeploymentConfig} class (``LambdaDeploymentConfig.AllAtOnce``, ``LambdaDeploymentConfig.Canary10Percent30Minutes``, etc.).

    Note: CloudFormation does not currently support creating custom lambda configs outside
    of using a custom resource. You can import custom deployment config created outside the
    CDK or via a custom resource with {@link LambdaDeploymentConfig#import}.

    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _ILambdaDeploymentConfigProxy

    @property
    @jsii.member(jsii_name="deploymentConfigArn")
    def deployment_config_arn(self) -> str:
        """
        Stability:
            stable
        """
        ...

    @property
    @jsii.member(jsii_name="deploymentConfigName")
    def deployment_config_name(self) -> str:
        """
        Stability:
            stable
        """
        ...


class _ILambdaDeploymentConfigProxy():
    """The Deployment Configuration of a Lambda Deployment Group. The default, pre-defined Configurations are available as constants on the {@link LambdaDeploymentConfig} class (``LambdaDeploymentConfig.AllAtOnce``, ``LambdaDeploymentConfig.Canary10Percent30Minutes``, etc.).

    Note: CloudFormation does not currently support creating custom lambda configs outside
    of using a custom resource. You can import custom deployment config created outside the
    CDK or via a custom resource with {@link LambdaDeploymentConfig#import}.

    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-codedeploy.ILambdaDeploymentConfig"
    @property
    @jsii.member(jsii_name="deploymentConfigArn")
    def deployment_config_arn(self) -> str:
        """
        Stability:
            stable
        """
        return jsii.get(self, "deploymentConfigArn")

    @property
    @jsii.member(jsii_name="deploymentConfigName")
    def deployment_config_name(self) -> str:
        """
        Stability:
            stable
        """
        return jsii.get(self, "deploymentConfigName")


@jsii.interface(jsii_type="@aws-cdk/aws-codedeploy.ILambdaDeploymentGroup")
class ILambdaDeploymentGroup(aws_cdk.core.IResource, jsii.compat.Protocol):
    """Interface for a Lambda deployment groups.

    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _ILambdaDeploymentGroupProxy

    @property
    @jsii.member(jsii_name="application")
    def application(self) -> "ILambdaApplication":
        """The reference to the CodeDeploy Lambda Application that this Deployment Group belongs to.

        Stability:
            stable
        """
        ...

    @property
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(self) -> "ILambdaDeploymentConfig":
        """The Deployment Configuration this Group uses.

        Stability:
            stable
        """
        ...

    @property
    @jsii.member(jsii_name="deploymentGroupArn")
    def deployment_group_arn(self) -> str:
        """The ARN of this Deployment Group.

        Stability:
            stable
        attribute:
            true
        """
        ...

    @property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> str:
        """The physical name of the CodeDeploy Deployment Group.

        Stability:
            stable
        attribute:
            true
        """
        ...


class _ILambdaDeploymentGroupProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """Interface for a Lambda deployment groups.

    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-codedeploy.ILambdaDeploymentGroup"
    @property
    @jsii.member(jsii_name="application")
    def application(self) -> "ILambdaApplication":
        """The reference to the CodeDeploy Lambda Application that this Deployment Group belongs to.

        Stability:
            stable
        """
        return jsii.get(self, "application")

    @property
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(self) -> "ILambdaDeploymentConfig":
        """The Deployment Configuration this Group uses.

        Stability:
            stable
        """
        return jsii.get(self, "deploymentConfig")

    @property
    @jsii.member(jsii_name="deploymentGroupArn")
    def deployment_group_arn(self) -> str:
        """The ARN of this Deployment Group.

        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "deploymentGroupArn")

    @property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> str:
        """The physical name of the CodeDeploy Deployment Group.

        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "deploymentGroupName")


@jsii.interface(jsii_type="@aws-cdk/aws-codedeploy.IServerApplication")
class IServerApplication(aws_cdk.core.IResource, jsii.compat.Protocol):
    """Represents a reference to a CodeDeploy Application deploying to EC2/on-premise instances.

    If you're managing the Application alongside the rest of your CDK resources,
    use the {@link ServerApplication} class.

    If you want to reference an already existing Application,
    or one defined in a different CDK Stack,
    use the {@link #import} method.

    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IServerApplicationProxy

    @property
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        ...

    @property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        ...


class _IServerApplicationProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """Represents a reference to a CodeDeploy Application deploying to EC2/on-premise instances.

    If you're managing the Application alongside the rest of your CDK resources,
    use the {@link ServerApplication} class.

    If you want to reference an already existing Application,
    or one defined in a different CDK Stack,
    use the {@link #import} method.

    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-codedeploy.IServerApplication"
    @property
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "applicationArn")

    @property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "applicationName")


@jsii.interface(jsii_type="@aws-cdk/aws-codedeploy.IServerDeploymentConfig")
class IServerDeploymentConfig(jsii.compat.Protocol):
    """The Deployment Configuration of an EC2/on-premise Deployment Group. The default, pre-defined Configurations are available as constants on the {@link ServerDeploymentConfig} class (``ServerDeploymentConfig.HalfAtATime``, ``ServerDeploymentConfig.AllAtOnce``, etc.). To create a custom Deployment Configuration, instantiate the {@link ServerDeploymentConfig} Construct.

    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IServerDeploymentConfigProxy

    @property
    @jsii.member(jsii_name="deploymentConfigArn")
    def deployment_config_arn(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        ...

    @property
    @jsii.member(jsii_name="deploymentConfigName")
    def deployment_config_name(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        ...


class _IServerDeploymentConfigProxy():
    """The Deployment Configuration of an EC2/on-premise Deployment Group. The default, pre-defined Configurations are available as constants on the {@link ServerDeploymentConfig} class (``ServerDeploymentConfig.HalfAtATime``, ``ServerDeploymentConfig.AllAtOnce``, etc.). To create a custom Deployment Configuration, instantiate the {@link ServerDeploymentConfig} Construct.

    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-codedeploy.IServerDeploymentConfig"
    @property
    @jsii.member(jsii_name="deploymentConfigArn")
    def deployment_config_arn(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "deploymentConfigArn")

    @property
    @jsii.member(jsii_name="deploymentConfigName")
    def deployment_config_name(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "deploymentConfigName")


@jsii.interface(jsii_type="@aws-cdk/aws-codedeploy.IServerDeploymentGroup")
class IServerDeploymentGroup(aws_cdk.core.IResource, jsii.compat.Protocol):
    """
    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IServerDeploymentGroupProxy

    @property
    @jsii.member(jsii_name="application")
    def application(self) -> "IServerApplication":
        """
        Stability:
            stable
        """
        ...

    @property
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(self) -> "IServerDeploymentConfig":
        """
        Stability:
            stable
        """
        ...

    @property
    @jsii.member(jsii_name="deploymentGroupArn")
    def deployment_group_arn(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        ...

    @property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        ...

    @property
    @jsii.member(jsii_name="autoScalingGroups")
    def auto_scaling_groups(self) -> typing.Optional[typing.List[aws_cdk.aws_autoscaling.AutoScalingGroup]]:
        """
        Stability:
            stable
        """
        ...

    @property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        """
        Stability:
            stable
        """
        ...


class _IServerDeploymentGroupProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """
    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-codedeploy.IServerDeploymentGroup"
    @property
    @jsii.member(jsii_name="application")
    def application(self) -> "IServerApplication":
        """
        Stability:
            stable
        """
        return jsii.get(self, "application")

    @property
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(self) -> "IServerDeploymentConfig":
        """
        Stability:
            stable
        """
        return jsii.get(self, "deploymentConfig")

    @property
    @jsii.member(jsii_name="deploymentGroupArn")
    def deployment_group_arn(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "deploymentGroupArn")

    @property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "deploymentGroupName")

    @property
    @jsii.member(jsii_name="autoScalingGroups")
    def auto_scaling_groups(self) -> typing.Optional[typing.List[aws_cdk.aws_autoscaling.AutoScalingGroup]]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "autoScalingGroups")

    @property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "role")


class InstanceTagSet(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codedeploy.InstanceTagSet"):
    """Represents a set of instance tag groups. An instance will match a set if it matches all of the groups in the set - in other words, sets follow 'and' semantics. You can have a maximum of 3 tag groups inside a set.

    Stability:
        stable
    """
    def __init__(self, *instance_tag_groups: typing.Mapping[str,typing.List[str]]) -> None:
        """
        Arguments:
            instance_tag_groups: -

        Stability:
            stable
        """
        jsii.create(InstanceTagSet, self, [*instance_tag_groups])

    @property
    @jsii.member(jsii_name="instanceTagGroups")
    def instance_tag_groups(self) -> typing.List[typing.Mapping[str,typing.List[str]]]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "instanceTagGroups")


@jsii.implements(ILambdaApplication)
class LambdaApplication(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codedeploy.LambdaApplication"):
    """A CodeDeploy Application that deploys to an AWS Lambda function.

    Stability:
        stable
    resource:
        AWS::CodeDeploy::Application
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, application_name: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            application_name: The physical, human-readable name of the CodeDeploy Application. Default: an auto-generated name will be used

        Stability:
            stable
        """
        props: LambdaApplicationProps = {}

        if application_name is not None:
            props["applicationName"] = application_name

        jsii.create(LambdaApplication, self, [scope, id, props])

    @jsii.member(jsii_name="fromLambdaApplicationName")
    @classmethod
    def from_lambda_application_name(cls, scope: aws_cdk.core.Construct, id: str, lambda_application_name: str) -> "ILambdaApplication":
        """Import an Application defined either outside the CDK, or in a different CDK Stack and exported using the {@link ILambdaApplication#export} method.

        Arguments:
            scope: the parent Construct for this new Construct.
            id: the logical ID of this new Construct.
            lambda_application_name: the name of the application to import.

        Returns:
            a Construct representing a reference to an existing Application

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "fromLambdaApplicationName", [scope, id, lambda_application_name])

    @property
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> str:
        """
        Stability:
            stable
        """
        return jsii.get(self, "applicationArn")

    @property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> str:
        """
        Stability:
            stable
        """
        return jsii.get(self, "applicationName")


@jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.LambdaApplicationProps", jsii_struct_bases=[])
class LambdaApplicationProps(jsii.compat.TypedDict, total=False):
    """Construction properties for {@link LambdaApplication}.

    Stability:
        stable
    """
    applicationName: str
    """The physical, human-readable name of the CodeDeploy Application.

    Default:
        an auto-generated name will be used

    Stability:
        stable
    """

class LambdaDeploymentConfig(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codedeploy.LambdaDeploymentConfig"):
    """A custom Deployment Configuration for a Lambda Deployment Group.

    Note: This class currently stands as namespaced container of the default configurations
    until CloudFormation supports custom Lambda Deployment Configs. Until then it is closed
    (private constructor) and does not extend {@link cdk.Construct}

    Stability:
        stable
    resource:
        AWS::CodeDeploy::DeploymentConfig
    """
    @jsii.member(jsii_name="import")
    @classmethod
    def import_(cls, _scope: aws_cdk.core.Construct, _id: str, *, deployment_config_name: str) -> "ILambdaDeploymentConfig":
        """Import a custom Deployment Configuration for a Lambda Deployment Group defined outside the CDK.

        Arguments:
            _scope: the parent Construct for this new Construct.
            _id: the logical ID of this new Construct.
            props: the properties of the referenced custom Deployment Configuration.
            deployment_config_name: The physical, human-readable name of the custom CodeDeploy Lambda Deployment Configuration that we are referencing.

        Returns:
            a Construct representing a reference to an existing custom Deployment Configuration

        Stability:
            stable
        """
        props: LambdaDeploymentConfigImportProps = {"deploymentConfigName": deployment_config_name}

        return jsii.sinvoke(cls, "import", [_scope, _id, props])

    @classproperty
    @jsii.member(jsii_name="ALL_AT_ONCE")
    def ALL_AT_ONCE(cls) -> "ILambdaDeploymentConfig":
        """
        Stability:
            stable
        """
        return jsii.sget(cls, "ALL_AT_ONCE")

    @classproperty
    @jsii.member(jsii_name="CANARY_10PERCENT_10MINUTES")
    def CANARY_10_PERCENT_10_MINUTES(cls) -> "ILambdaDeploymentConfig":
        """
        Stability:
            stable
        """
        return jsii.sget(cls, "CANARY_10PERCENT_10MINUTES")

    @classproperty
    @jsii.member(jsii_name="CANARY_10PERCENT_15MINUTES")
    def CANARY_10_PERCENT_15_MINUTES(cls) -> "ILambdaDeploymentConfig":
        """
        Stability:
            stable
        """
        return jsii.sget(cls, "CANARY_10PERCENT_15MINUTES")

    @classproperty
    @jsii.member(jsii_name="CANARY_10PERCENT_30MINUTES")
    def CANARY_10_PERCENT_30_MINUTES(cls) -> "ILambdaDeploymentConfig":
        """
        Stability:
            stable
        """
        return jsii.sget(cls, "CANARY_10PERCENT_30MINUTES")

    @classproperty
    @jsii.member(jsii_name="CANARY_10PERCENT_5MINUTES")
    def CANARY_10_PERCENT_5_MINUTES(cls) -> "ILambdaDeploymentConfig":
        """
        Stability:
            stable
        """
        return jsii.sget(cls, "CANARY_10PERCENT_5MINUTES")

    @classproperty
    @jsii.member(jsii_name="LINEAR_10PERCENT_EVERY_10MINUTES")
    def LINEAR_10_PERCENT_EVERY_10_MINUTES(cls) -> "ILambdaDeploymentConfig":
        """
        Stability:
            stable
        """
        return jsii.sget(cls, "LINEAR_10PERCENT_EVERY_10MINUTES")

    @classproperty
    @jsii.member(jsii_name="LINEAR_10PERCENT_EVERY_1MINUTE")
    def LINEAR_10_PERCENT_EVERY_1_MINUTE(cls) -> "ILambdaDeploymentConfig":
        """
        Stability:
            stable
        """
        return jsii.sget(cls, "LINEAR_10PERCENT_EVERY_1MINUTE")

    @classproperty
    @jsii.member(jsii_name="LINEAR_10PERCENT_EVERY_2MINUTES")
    def LINEAR_10_PERCENT_EVERY_2_MINUTES(cls) -> "ILambdaDeploymentConfig":
        """
        Stability:
            stable
        """
        return jsii.sget(cls, "LINEAR_10PERCENT_EVERY_2MINUTES")

    @classproperty
    @jsii.member(jsii_name="LINEAR_10PERCENT_EVERY_3MINUTES")
    def LINEAR_10_PERCENT_EVERY_3_MINUTES(cls) -> "ILambdaDeploymentConfig":
        """
        Stability:
            stable
        """
        return jsii.sget(cls, "LINEAR_10PERCENT_EVERY_3MINUTES")


@jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.LambdaDeploymentConfigImportProps", jsii_struct_bases=[])
class LambdaDeploymentConfigImportProps(jsii.compat.TypedDict):
    """Properties of a reference to a CodeDeploy Lambda Deployment Configuration.

    See:
        LambdaDeploymentConfig#export
    Stability:
        stable
    """
    deploymentConfigName: str
    """The physical, human-readable name of the custom CodeDeploy Lambda Deployment Configuration that we are referencing.

    Stability:
        stable
    """

@jsii.implements(ILambdaDeploymentGroup)
class LambdaDeploymentGroup(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codedeploy.LambdaDeploymentGroup"):
    """
    Stability:
        stable
    resource:
        AWS::CodeDeploy::DeploymentGroup
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, alias: aws_cdk.aws_lambda.Alias, alarms: typing.Optional[typing.List[aws_cdk.aws_cloudwatch.IAlarm]]=None, application: typing.Optional["ILambdaApplication"]=None, auto_rollback: typing.Optional["AutoRollbackConfig"]=None, deployment_config: typing.Optional["ILambdaDeploymentConfig"]=None, deployment_group_name: typing.Optional[str]=None, ignore_poll_alarms_failure: typing.Optional[bool]=None, post_hook: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, pre_hook: typing.Optional[aws_cdk.aws_lambda.IFunction]=None, role: typing.Optional[aws_cdk.aws_iam.IRole]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            alias: Lambda Alias to shift traffic. Updating the version of the alias will trigger a CodeDeploy deployment. [disable-awslint:ref-via-interface] since we need to modify the alias CFN resource update policy
            alarms: The CloudWatch alarms associated with this Deployment Group. CodeDeploy will stop (and optionally roll back) a deployment if during it any of the alarms trigger. Alarms can also be added after the Deployment Group is created using the {@link #addAlarm} method. Default: []
            application: The reference to the CodeDeploy Lambda Application that this Deployment Group belongs to. Default: - One will be created for you.
            auto_rollback: The auto-rollback configuration for this Deployment Group. Default: - default AutoRollbackConfig.
            deployment_config: The Deployment Configuration this Deployment Group uses. Default: LambdaDeploymentConfig.CANARY_10PERCENT_5MINUTES
            deployment_group_name: The physical, human-readable name of the CodeDeploy Deployment Group. Default: - An auto-generated name will be used.
            ignore_poll_alarms_failure: Whether to continue a deployment even if fetching the alarm status from CloudWatch failed. Default: false
            post_hook: The Lambda function to run after traffic routing starts. Default: - None.
            pre_hook: The Lambda function to run before traffic routing starts. Default: - None.
            role: The service Role of this Deployment Group. Default: - A new Role will be created.

        Stability:
            stable
        """
        props: LambdaDeploymentGroupProps = {"alias": alias}

        if alarms is not None:
            props["alarms"] = alarms

        if application is not None:
            props["application"] = application

        if auto_rollback is not None:
            props["autoRollback"] = auto_rollback

        if deployment_config is not None:
            props["deploymentConfig"] = deployment_config

        if deployment_group_name is not None:
            props["deploymentGroupName"] = deployment_group_name

        if ignore_poll_alarms_failure is not None:
            props["ignorePollAlarmsFailure"] = ignore_poll_alarms_failure

        if post_hook is not None:
            props["postHook"] = post_hook

        if pre_hook is not None:
            props["preHook"] = pre_hook

        if role is not None:
            props["role"] = role

        jsii.create(LambdaDeploymentGroup, self, [scope, id, props])

    @jsii.member(jsii_name="fromLambdaDeploymentGroupAttributes")
    @classmethod
    def from_lambda_deployment_group_attributes(cls, scope: aws_cdk.core.Construct, id: str, *, application: "ILambdaApplication", deployment_group_name: str, deployment_config: typing.Optional["ILambdaDeploymentConfig"]=None) -> "ILambdaDeploymentGroup":
        """Import an Lambda Deployment Group defined either outside the CDK, or in a different CDK Stack and exported using the {@link #export} method.

        Arguments:
            scope: the parent Construct for this new Construct.
            id: the logical ID of this new Construct.
            attrs: the properties of the referenced Deployment Group.
            application: The reference to the CodeDeploy Lambda Application that this Deployment Group belongs to.
            deployment_group_name: The physical, human-readable name of the CodeDeploy Lambda Deployment Group that we are referencing.
            deployment_config: The Deployment Configuration this Deployment Group uses. Default: LambdaDeploymentConfig.CANARY_10PERCENT_5MINUTES

        Returns:
            a Construct representing a reference to an existing Deployment Group

        Stability:
            stable
        """
        attrs: LambdaDeploymentGroupAttributes = {"application": application, "deploymentGroupName": deployment_group_name}

        if deployment_config is not None:
            attrs["deploymentConfig"] = deployment_config

        return jsii.sinvoke(cls, "fromLambdaDeploymentGroupAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="addAlarm")
    def add_alarm(self, alarm: aws_cdk.aws_cloudwatch.IAlarm) -> None:
        """Associates an additional alarm with this Deployment Group.

        Arguments:
            alarm: the alarm to associate with this Deployment Group.

        Stability:
            stable
        """
        return jsii.invoke(self, "addAlarm", [alarm])

    @jsii.member(jsii_name="addPostHook")
    def add_post_hook(self, post_hook: aws_cdk.aws_lambda.IFunction) -> None:
        """Associate a function to run after deployment completes.

        Arguments:
            post_hook: function to run after deployment completes.

        Stability:
            stable
        throws:
            an error if a post-hook function is already configured
        """
        return jsii.invoke(self, "addPostHook", [post_hook])

    @jsii.member(jsii_name="addPreHook")
    def add_pre_hook(self, pre_hook: aws_cdk.aws_lambda.IFunction) -> None:
        """Associate a function to run before deployment begins.

        Arguments:
            pre_hook: function to run before deployment beings.

        Stability:
            stable
        throws:
            an error if a pre-hook function is already configured
        """
        return jsii.invoke(self, "addPreHook", [pre_hook])

    @jsii.member(jsii_name="grantPutLifecycleEventHookExecutionStatus")
    def grant_put_lifecycle_event_hook_execution_status(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant a principal permission to codedeploy:PutLifecycleEventHookExecutionStatus on this deployment group resource.

        Arguments:
            grantee: to grant permission to.

        Stability:
            stable
        """
        return jsii.invoke(self, "grantPutLifecycleEventHookExecutionStatus", [grantee])

    @property
    @jsii.member(jsii_name="application")
    def application(self) -> "ILambdaApplication":
        """The reference to the CodeDeploy Lambda Application that this Deployment Group belongs to.

        Stability:
            stable
        """
        return jsii.get(self, "application")

    @property
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(self) -> "ILambdaDeploymentConfig":
        """The Deployment Configuration this Group uses.

        Stability:
            stable
        """
        return jsii.get(self, "deploymentConfig")

    @property
    @jsii.member(jsii_name="deploymentGroupArn")
    def deployment_group_arn(self) -> str:
        """The ARN of this Deployment Group.

        Stability:
            stable
        """
        return jsii.get(self, "deploymentGroupArn")

    @property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> str:
        """The physical name of the CodeDeploy Deployment Group.

        Stability:
            stable
        """
        return jsii.get(self, "deploymentGroupName")

    @property
    @jsii.member(jsii_name="role")
    def role(self) -> aws_cdk.aws_iam.IRole:
        """
        Stability:
            stable
        """
        return jsii.get(self, "role")


@jsii.data_type_optionals(jsii_struct_bases=[])
class _LambdaDeploymentGroupAttributes(jsii.compat.TypedDict, total=False):
    deploymentConfig: "ILambdaDeploymentConfig"
    """The Deployment Configuration this Deployment Group uses.

    Default:
        LambdaDeploymentConfig.CANARY_10PERCENT_5MINUTES

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.LambdaDeploymentGroupAttributes", jsii_struct_bases=[_LambdaDeploymentGroupAttributes])
class LambdaDeploymentGroupAttributes(_LambdaDeploymentGroupAttributes):
    """Properties of a reference to a CodeDeploy Lambda Deployment Group.

    See:
        ILambdaDeploymentGroup#export
    Stability:
        stable
    """
    application: "ILambdaApplication"
    """The reference to the CodeDeploy Lambda Application that this Deployment Group belongs to.

    Stability:
        stable
    """

    deploymentGroupName: str
    """The physical, human-readable name of the CodeDeploy Lambda Deployment Group that we are referencing.

    Stability:
        stable
    """

@jsii.data_type_optionals(jsii_struct_bases=[])
class _LambdaDeploymentGroupProps(jsii.compat.TypedDict, total=False):
    alarms: typing.List[aws_cdk.aws_cloudwatch.IAlarm]
    """The CloudWatch alarms associated with this Deployment Group. CodeDeploy will stop (and optionally roll back) a deployment if during it any of the alarms trigger.

    Alarms can also be added after the Deployment Group is created using the {@link #addAlarm} method.

    Default:
        []

    See:
        https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-create-alarms.html
    Stability:
        stable
    """
    application: "ILambdaApplication"
    """The reference to the CodeDeploy Lambda Application that this Deployment Group belongs to.

    Default:
        - One will be created for you.

    Stability:
        stable
    """
    autoRollback: "AutoRollbackConfig"
    """The auto-rollback configuration for this Deployment Group.

    Default:
        - default AutoRollbackConfig.

    Stability:
        stable
    """
    deploymentConfig: "ILambdaDeploymentConfig"
    """The Deployment Configuration this Deployment Group uses.

    Default:
        LambdaDeploymentConfig.CANARY_10PERCENT_5MINUTES

    Stability:
        stable
    """
    deploymentGroupName: str
    """The physical, human-readable name of the CodeDeploy Deployment Group.

    Default:
        - An auto-generated name will be used.

    Stability:
        stable
    """
    ignorePollAlarmsFailure: bool
    """Whether to continue a deployment even if fetching the alarm status from CloudWatch failed.

    Default:
        false

    Stability:
        stable
    """
    postHook: aws_cdk.aws_lambda.IFunction
    """The Lambda function to run after traffic routing starts.

    Default:
        - None.

    Stability:
        stable
    """
    preHook: aws_cdk.aws_lambda.IFunction
    """The Lambda function to run before traffic routing starts.

    Default:
        - None.

    Stability:
        stable
    """
    role: aws_cdk.aws_iam.IRole
    """The service Role of this Deployment Group.

    Default:
        - A new Role will be created.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.LambdaDeploymentGroupProps", jsii_struct_bases=[_LambdaDeploymentGroupProps])
class LambdaDeploymentGroupProps(_LambdaDeploymentGroupProps):
    """Construction properties for {@link LambdaDeploymentGroup}.

    Stability:
        stable
    """
    alias: aws_cdk.aws_lambda.Alias
    """Lambda Alias to shift traffic. Updating the version of the alias will trigger a CodeDeploy deployment.

    [disable-awslint:ref-via-interface] since we need to modify the alias CFN resource update policy

    Stability:
        stable
    """

class LoadBalancer(metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-codedeploy.LoadBalancer"):
    """An interface of an abstract load balancer, as needed by CodeDeploy. Create instances using the static factory methods: {@link #classic}, {@link #application} and {@link #network}.

    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _LoadBalancerProxy

    def __init__(self) -> None:
        jsii.create(LoadBalancer, self, [])

    @jsii.member(jsii_name="application")
    @classmethod
    def application(cls, alb_target_group: aws_cdk.aws_elasticloadbalancingv2.ApplicationTargetGroup) -> "LoadBalancer":
        """Creates a new CodeDeploy load balancer from an Application Load Balancer Target Group.

        Arguments:
            alb_target_group: an ALB Target Group.

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "application", [alb_target_group])

    @jsii.member(jsii_name="classic")
    @classmethod
    def classic(cls, load_balancer: aws_cdk.aws_elasticloadbalancing.LoadBalancer) -> "LoadBalancer":
        """Creates a new CodeDeploy load balancer from a Classic ELB Load Balancer.

        Arguments:
            load_balancer: a classic ELB Load Balancer.

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "classic", [load_balancer])

    @jsii.member(jsii_name="network")
    @classmethod
    def network(cls, nlb_target_group: aws_cdk.aws_elasticloadbalancingv2.NetworkTargetGroup) -> "LoadBalancer":
        """Creates a new CodeDeploy load balancer from a Network Load Balancer Target Group.

        Arguments:
            nlb_target_group: an NLB Target Group.

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "network", [nlb_target_group])

    @property
    @jsii.member(jsii_name="generation")
    @abc.abstractmethod
    def generation(self) -> "LoadBalancerGeneration":
        """
        Stability:
            stable
        """
        ...

    @property
    @jsii.member(jsii_name="name")
    @abc.abstractmethod
    def name(self) -> str:
        """
        Stability:
            stable
        """
        ...


class _LoadBalancerProxy(LoadBalancer):
    @property
    @jsii.member(jsii_name="generation")
    def generation(self) -> "LoadBalancerGeneration":
        """
        Stability:
            stable
        """
        return jsii.get(self, "generation")

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> str:
        """
        Stability:
            stable
        """
        return jsii.get(self, "name")


@jsii.enum(jsii_type="@aws-cdk/aws-codedeploy.LoadBalancerGeneration")
class LoadBalancerGeneration(enum.Enum):
    """The generations of AWS load balancing solutions.

    Stability:
        stable
    """
    FIRST = "FIRST"
    """The first generation (ELB Classic).

    Stability:
        stable
    """
    SECOND = "SECOND"
    """The second generation (ALB and NLB).

    Stability:
        stable
    """

class MinimumHealthyHosts(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codedeploy.MinimumHealthyHosts"):
    """Minimum number of healthy hosts for a server deployment.

    Stability:
        stable
    """
    @jsii.member(jsii_name="count")
    @classmethod
    def count(cls, value: jsii.Number) -> "MinimumHealthyHosts":
        """The minimum healhty hosts threshold expressed as an absolute number.

        Arguments:
            value: -

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "count", [value])

    @jsii.member(jsii_name="percentage")
    @classmethod
    def percentage(cls, value: jsii.Number) -> "MinimumHealthyHosts":
        """The minmum healhty hosts threshold expressed as a percentage of the fleet.

        Arguments:
            value: -

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "percentage", [value])


@jsii.implements(IServerApplication)
class ServerApplication(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codedeploy.ServerApplication"):
    """A CodeDeploy Application that deploys to EC2/on-premise instances.

    Stability:
        stable
    resource:
        AWS::CodeDeploy::Application
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, application_name: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            application_name: The physical, human-readable name of the CodeDeploy Application. Default: an auto-generated name will be used

        Stability:
            stable
        """
        props: ServerApplicationProps = {}

        if application_name is not None:
            props["applicationName"] = application_name

        jsii.create(ServerApplication, self, [scope, id, props])

    @jsii.member(jsii_name="fromServerApplicationName")
    @classmethod
    def from_server_application_name(cls, scope: aws_cdk.core.Construct, id: str, server_application_name: str) -> "IServerApplication":
        """Import an Application defined either outside the CDK, or in a different CDK Stack and exported using the {@link #export} method.

        Arguments:
            scope: the parent Construct for this new Construct.
            id: the logical ID of this new Construct.
            server_application_name: the name of the application to import.

        Returns:
            a Construct representing a reference to an existing Application

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "fromServerApplicationName", [scope, id, server_application_name])

    @property
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> str:
        """
        Stability:
            stable
        """
        return jsii.get(self, "applicationArn")

    @property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> str:
        """
        Stability:
            stable
        """
        return jsii.get(self, "applicationName")


@jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.ServerApplicationProps", jsii_struct_bases=[])
class ServerApplicationProps(jsii.compat.TypedDict, total=False):
    """Construction properties for {@link ServerApplication}.

    Stability:
        stable
    """
    applicationName: str
    """The physical, human-readable name of the CodeDeploy Application.

    Default:
        an auto-generated name will be used

    Stability:
        stable
    """

@jsii.implements(IServerDeploymentConfig)
class ServerDeploymentConfig(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codedeploy.ServerDeploymentConfig"):
    """A custom Deployment Configuration for an EC2/on-premise Deployment Group.

    Stability:
        stable
    resource:
        AWS::CodeDeploy::DeploymentConfig
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, minimum_healthy_hosts: "MinimumHealthyHosts", deployment_config_name: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            minimum_healthy_hosts: Minimum number of healthy hosts.
            deployment_config_name: The physical, human-readable name of the Deployment Configuration. Default: a name will be auto-generated

        Stability:
            stable
        """
        props: ServerDeploymentConfigProps = {"minimumHealthyHosts": minimum_healthy_hosts}

        if deployment_config_name is not None:
            props["deploymentConfigName"] = deployment_config_name

        jsii.create(ServerDeploymentConfig, self, [scope, id, props])

    @jsii.member(jsii_name="fromServerDeploymentConfigName")
    @classmethod
    def from_server_deployment_config_name(cls, scope: aws_cdk.core.Construct, id: str, server_deployment_config_name: str) -> "IServerDeploymentConfig":
        """Import a custom Deployment Configuration for an EC2/on-premise Deployment Group defined either outside the CDK, or in a different CDK Stack and exported using the {@link #export} method.

        Arguments:
            scope: the parent Construct for this new Construct.
            id: the logical ID of this new Construct.
            server_deployment_config_name: the properties of the referenced custom Deployment Configuration.

        Returns:
            a Construct representing a reference to an existing custom Deployment Configuration

        Stability:
            stable
        """
        return jsii.sinvoke(cls, "fromServerDeploymentConfigName", [scope, id, server_deployment_config_name])

    @classproperty
    @jsii.member(jsii_name="ALL_AT_ONCE")
    def ALL_AT_ONCE(cls) -> "IServerDeploymentConfig":
        """
        Stability:
            stable
        """
        return jsii.sget(cls, "ALL_AT_ONCE")

    @classproperty
    @jsii.member(jsii_name="HALF_AT_A_TIME")
    def HALF_AT_A_TIME(cls) -> "IServerDeploymentConfig":
        """
        Stability:
            stable
        """
        return jsii.sget(cls, "HALF_AT_A_TIME")

    @classproperty
    @jsii.member(jsii_name="ONE_AT_A_TIME")
    def ONE_AT_A_TIME(cls) -> "IServerDeploymentConfig":
        """
        Stability:
            stable
        """
        return jsii.sget(cls, "ONE_AT_A_TIME")

    @property
    @jsii.member(jsii_name="deploymentConfigArn")
    def deployment_config_arn(self) -> str:
        """
        Stability:
            stable
        """
        return jsii.get(self, "deploymentConfigArn")

    @property
    @jsii.member(jsii_name="deploymentConfigName")
    def deployment_config_name(self) -> str:
        """
        Stability:
            stable
        """
        return jsii.get(self, "deploymentConfigName")


@jsii.data_type_optionals(jsii_struct_bases=[])
class _ServerDeploymentConfigProps(jsii.compat.TypedDict, total=False):
    deploymentConfigName: str
    """The physical, human-readable name of the Deployment Configuration.

    Default:
        a name will be auto-generated

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.ServerDeploymentConfigProps", jsii_struct_bases=[_ServerDeploymentConfigProps])
class ServerDeploymentConfigProps(_ServerDeploymentConfigProps):
    """Construction properties of {@link ServerDeploymentConfig}.

    Stability:
        stable
    """
    minimumHealthyHosts: "MinimumHealthyHosts"
    """Minimum number of healthy hosts.

    Stability:
        stable
    """

@jsii.implements(IServerDeploymentGroup)
class ServerDeploymentGroup(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codedeploy.ServerDeploymentGroup"):
    """A CodeDeploy Deployment Group that deploys to EC2/on-premise instances.

    Stability:
        stable
    resource:
        AWS::CodeDeploy::DeploymentGroup
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, alarms: typing.Optional[typing.List[aws_cdk.aws_cloudwatch.IAlarm]]=None, application: typing.Optional["IServerApplication"]=None, auto_rollback: typing.Optional["AutoRollbackConfig"]=None, auto_scaling_groups: typing.Optional[typing.List[aws_cdk.aws_autoscaling.AutoScalingGroup]]=None, deployment_config: typing.Optional["IServerDeploymentConfig"]=None, deployment_group_name: typing.Optional[str]=None, ec2_instance_tags: typing.Optional["InstanceTagSet"]=None, ignore_poll_alarms_failure: typing.Optional[bool]=None, install_agent: typing.Optional[bool]=None, load_balancer: typing.Optional["LoadBalancer"]=None, on_premise_instance_tags: typing.Optional["InstanceTagSet"]=None, role: typing.Optional[aws_cdk.aws_iam.IRole]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            alarms: The CloudWatch alarms associated with this Deployment Group. CodeDeploy will stop (and optionally roll back) a deployment if during it any of the alarms trigger. Alarms can also be added after the Deployment Group is created using the {@link #addAlarm} method. Default: []
            application: The CodeDeploy EC2/on-premise Application this Deployment Group belongs to. Default: - A new Application will be created.
            auto_rollback: The auto-rollback configuration for this Deployment Group. Default: - default AutoRollbackConfig.
            auto_scaling_groups: The auto-scaling groups belonging to this Deployment Group. Auto-scaling groups can also be added after the Deployment Group is created using the {@link #addAutoScalingGroup} method. [disable-awslint:ref-via-interface] is needed because we update userdata for ASGs to install the codedeploy agent. Default: []
            deployment_config: The EC2/on-premise Deployment Configuration to use for this Deployment Group. Default: ServerDeploymentConfig#OneAtATime
            deployment_group_name: The physical, human-readable name of the CodeDeploy Deployment Group. Default: - An auto-generated name will be used.
            ec2_instance_tags: All EC2 instances matching the given set of tags when a deployment occurs will be added to this Deployment Group. Default: - No additional EC2 instances will be added to the Deployment Group.
            ignore_poll_alarms_failure: Whether to continue a deployment even if fetching the alarm status from CloudWatch failed. Default: false
            install_agent: If you've provided any auto-scaling groups with the {@link #autoScalingGroups} property, you can set this property to add User Data that installs the CodeDeploy agent on the instances. Default: true
            load_balancer: The load balancer to place in front of this Deployment Group. Can be created from either a classic Elastic Load Balancer, or an Application Load Balancer / Network Load Balancer Target Group. Default: - Deployment Group will not have a load balancer defined.
            on_premise_instance_tags: All on-premise instances matching the given set of tags when a deployment occurs will be added to this Deployment Group. Default: - No additional on-premise instances will be added to the Deployment Group.
            role: The service Role of this Deployment Group. Default: - A new Role will be created.

        Stability:
            stable
        """
        props: ServerDeploymentGroupProps = {}

        if alarms is not None:
            props["alarms"] = alarms

        if application is not None:
            props["application"] = application

        if auto_rollback is not None:
            props["autoRollback"] = auto_rollback

        if auto_scaling_groups is not None:
            props["autoScalingGroups"] = auto_scaling_groups

        if deployment_config is not None:
            props["deploymentConfig"] = deployment_config

        if deployment_group_name is not None:
            props["deploymentGroupName"] = deployment_group_name

        if ec2_instance_tags is not None:
            props["ec2InstanceTags"] = ec2_instance_tags

        if ignore_poll_alarms_failure is not None:
            props["ignorePollAlarmsFailure"] = ignore_poll_alarms_failure

        if install_agent is not None:
            props["installAgent"] = install_agent

        if load_balancer is not None:
            props["loadBalancer"] = load_balancer

        if on_premise_instance_tags is not None:
            props["onPremiseInstanceTags"] = on_premise_instance_tags

        if role is not None:
            props["role"] = role

        jsii.create(ServerDeploymentGroup, self, [scope, id, props])

    @jsii.member(jsii_name="fromServerDeploymentGroupAttributes")
    @classmethod
    def from_server_deployment_group_attributes(cls, scope: aws_cdk.core.Construct, id: str, *, application: "IServerApplication", deployment_group_name: str, deployment_config: typing.Optional["IServerDeploymentConfig"]=None) -> "IServerDeploymentGroup":
        """Import an EC2/on-premise Deployment Group defined either outside the CDK, or in a different CDK Stack and exported using the {@link #export} method.

        Arguments:
            scope: the parent Construct for this new Construct.
            id: the logical ID of this new Construct.
            attrs: the properties of the referenced Deployment Group.
            application: The reference to the CodeDeploy EC2/on-premise Application that this Deployment Group belongs to.
            deployment_group_name: The physical, human-readable name of the CodeDeploy EC2/on-premise Deployment Group that we are referencing.
            deployment_config: The Deployment Configuration this Deployment Group uses. Default: ServerDeploymentConfig#OneAtATime

        Returns:
            a Construct representing a reference to an existing Deployment Group

        Stability:
            stable
        """
        attrs: ServerDeploymentGroupAttributes = {"application": application, "deploymentGroupName": deployment_group_name}

        if deployment_config is not None:
            attrs["deploymentConfig"] = deployment_config

        return jsii.sinvoke(cls, "fromServerDeploymentGroupAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="addAlarm")
    def add_alarm(self, alarm: aws_cdk.aws_cloudwatch.IAlarm) -> None:
        """Associates an additional alarm with this Deployment Group.

        Arguments:
            alarm: the alarm to associate with this Deployment Group.

        Stability:
            stable
        """
        return jsii.invoke(self, "addAlarm", [alarm])

    @jsii.member(jsii_name="addAutoScalingGroup")
    def add_auto_scaling_group(self, asg: aws_cdk.aws_autoscaling.AutoScalingGroup) -> None:
        """Adds an additional auto-scaling group to this Deployment Group.

        Arguments:
            asg: the auto-scaling group to add to this Deployment Group. [disable-awslint:ref-via-interface] is needed in order to install the code deploy agent by updating the ASGs user data.

        Stability:
            stable
        """
        return jsii.invoke(self, "addAutoScalingGroup", [asg])

    @property
    @jsii.member(jsii_name="application")
    def application(self) -> "IServerApplication":
        """
        Stability:
            stable
        """
        return jsii.get(self, "application")

    @property
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(self) -> "IServerDeploymentConfig":
        """
        Stability:
            stable
        """
        return jsii.get(self, "deploymentConfig")

    @property
    @jsii.member(jsii_name="deploymentGroupArn")
    def deployment_group_arn(self) -> str:
        """
        Stability:
            stable
        """
        return jsii.get(self, "deploymentGroupArn")

    @property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> str:
        """
        Stability:
            stable
        """
        return jsii.get(self, "deploymentGroupName")

    @property
    @jsii.member(jsii_name="autoScalingGroups")
    def auto_scaling_groups(self) -> typing.Optional[typing.List[aws_cdk.aws_autoscaling.AutoScalingGroup]]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "autoScalingGroups")

    @property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        """
        Stability:
            stable
        """
        return jsii.get(self, "role")


@jsii.data_type_optionals(jsii_struct_bases=[])
class _ServerDeploymentGroupAttributes(jsii.compat.TypedDict, total=False):
    deploymentConfig: "IServerDeploymentConfig"
    """The Deployment Configuration this Deployment Group uses.

    Default:
        ServerDeploymentConfig#OneAtATime

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.ServerDeploymentGroupAttributes", jsii_struct_bases=[_ServerDeploymentGroupAttributes])
class ServerDeploymentGroupAttributes(_ServerDeploymentGroupAttributes):
    """Properties of a reference to a CodeDeploy EC2/on-premise Deployment Group.

    See:
        IServerDeploymentGroup#export
    Stability:
        stable
    """
    application: "IServerApplication"
    """The reference to the CodeDeploy EC2/on-premise Application that this Deployment Group belongs to.

    Stability:
        stable
    """

    deploymentGroupName: str
    """The physical, human-readable name of the CodeDeploy EC2/on-premise Deployment Group that we are referencing.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codedeploy.ServerDeploymentGroupProps", jsii_struct_bases=[])
class ServerDeploymentGroupProps(jsii.compat.TypedDict, total=False):
    """Construction properties for {@link ServerDeploymentGroup}.

    Stability:
        stable
    """
    alarms: typing.List[aws_cdk.aws_cloudwatch.IAlarm]
    """The CloudWatch alarms associated with this Deployment Group. CodeDeploy will stop (and optionally roll back) a deployment if during it any of the alarms trigger.

    Alarms can also be added after the Deployment Group is created using the {@link #addAlarm} method.

    Default:
        []

    See:
        https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-create-alarms.html
    Stability:
        stable
    """

    application: "IServerApplication"
    """The CodeDeploy EC2/on-premise Application this Deployment Group belongs to.

    Default:
        - A new Application will be created.

    Stability:
        stable
    """

    autoRollback: "AutoRollbackConfig"
    """The auto-rollback configuration for this Deployment Group.

    Default:
        - default AutoRollbackConfig.

    Stability:
        stable
    """

    autoScalingGroups: typing.List[aws_cdk.aws_autoscaling.AutoScalingGroup]
    """The auto-scaling groups belonging to this Deployment Group.

    Auto-scaling groups can also be added after the Deployment Group is created
    using the {@link #addAutoScalingGroup} method.

    [disable-awslint:ref-via-interface] is needed because we update userdata
    for ASGs to install the codedeploy agent.

    Default:
        []

    Stability:
        stable
    """

    deploymentConfig: "IServerDeploymentConfig"
    """The EC2/on-premise Deployment Configuration to use for this Deployment Group.

    Default:
        ServerDeploymentConfig#OneAtATime

    Stability:
        stable
    """

    deploymentGroupName: str
    """The physical, human-readable name of the CodeDeploy Deployment Group.

    Default:
        - An auto-generated name will be used.

    Stability:
        stable
    """

    ec2InstanceTags: "InstanceTagSet"
    """All EC2 instances matching the given set of tags when a deployment occurs will be added to this Deployment Group.

    Default:
        - No additional EC2 instances will be added to the Deployment Group.

    Stability:
        stable
    """

    ignorePollAlarmsFailure: bool
    """Whether to continue a deployment even if fetching the alarm status from CloudWatch failed.

    Default:
        false

    Stability:
        stable
    """

    installAgent: bool
    """If you've provided any auto-scaling groups with the {@link #autoScalingGroups} property, you can set this property to add User Data that installs the CodeDeploy agent on the instances.

    Default:
        true

    See:
        https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install.html
    Stability:
        stable
    """

    loadBalancer: "LoadBalancer"
    """The load balancer to place in front of this Deployment Group. Can be created from either a classic Elastic Load Balancer, or an Application Load Balancer / Network Load Balancer Target Group.

    Default:
        - Deployment Group will not have a load balancer defined.

    Stability:
        stable
    """

    onPremiseInstanceTags: "InstanceTagSet"
    """All on-premise instances matching the given set of tags when a deployment occurs will be added to this Deployment Group.

    Default:
        - No additional on-premise instances will be added to the Deployment Group.

    Stability:
        stable
    """

    role: aws_cdk.aws_iam.IRole
    """The service Role of this Deployment Group.

    Default:
        - A new Role will be created.

    Stability:
        stable
    """

__all__ = ["AutoRollbackConfig", "CfnApplication", "CfnApplicationProps", "CfnDeploymentConfig", "CfnDeploymentConfigProps", "CfnDeploymentGroup", "CfnDeploymentGroupProps", "ILambdaApplication", "ILambdaDeploymentConfig", "ILambdaDeploymentGroup", "IServerApplication", "IServerDeploymentConfig", "IServerDeploymentGroup", "InstanceTagSet", "LambdaApplication", "LambdaApplicationProps", "LambdaDeploymentConfig", "LambdaDeploymentConfigImportProps", "LambdaDeploymentGroup", "LambdaDeploymentGroupAttributes", "LambdaDeploymentGroupProps", "LoadBalancer", "LoadBalancerGeneration", "MinimumHealthyHosts", "ServerApplication", "ServerApplicationProps", "ServerDeploymentConfig", "ServerDeploymentConfigProps", "ServerDeploymentGroup", "ServerDeploymentGroupAttributes", "ServerDeploymentGroupProps", "__jsii_assembly__"]

publication.publish()
