import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_ec2
import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-elasticloadbalancing", "0.37.0", __name__, "aws-elasticloadbalancing@0.37.0.jsii.tgz")
class CfnLoadBalancer(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-elasticloadbalancing.CfnLoadBalancer"):
    """A CloudFormation ``AWS::ElasticLoadBalancing::LoadBalancer``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html
    Stability:
        stable
    cloudformationResource:
        AWS::ElasticLoadBalancing::LoadBalancer
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, listeners: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["ListenersProperty", aws_cdk.core.IResolvable]]], access_logging_policy: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AccessLoggingPolicyProperty"]]]=None, app_cookie_stickiness_policy: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "AppCookieStickinessPolicyProperty"]]]]]=None, availability_zones: typing.Optional[typing.List[str]]=None, connection_draining_policy: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ConnectionDrainingPolicyProperty"]]]=None, connection_settings: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ConnectionSettingsProperty"]]]=None, cross_zone: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, health_check: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["HealthCheckProperty"]]]=None, instances: typing.Optional[typing.List[str]]=None, lb_cookie_stickiness_policy: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "LBCookieStickinessPolicyProperty"]]]]]=None, load_balancer_name: typing.Optional[str]=None, policies: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "PoliciesProperty"]]]]]=None, scheme: typing.Optional[str]=None, security_groups: typing.Optional[typing.List[str]]=None, subnets: typing.Optional[typing.List[str]]=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::ElasticLoadBalancing::LoadBalancer``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            listeners: ``AWS::ElasticLoadBalancing::LoadBalancer.Listeners``.
            access_logging_policy: ``AWS::ElasticLoadBalancing::LoadBalancer.AccessLoggingPolicy``.
            app_cookie_stickiness_policy: ``AWS::ElasticLoadBalancing::LoadBalancer.AppCookieStickinessPolicy``.
            availability_zones: ``AWS::ElasticLoadBalancing::LoadBalancer.AvailabilityZones``.
            connection_draining_policy: ``AWS::ElasticLoadBalancing::LoadBalancer.ConnectionDrainingPolicy``.
            connection_settings: ``AWS::ElasticLoadBalancing::LoadBalancer.ConnectionSettings``.
            cross_zone: ``AWS::ElasticLoadBalancing::LoadBalancer.CrossZone``.
            health_check: ``AWS::ElasticLoadBalancing::LoadBalancer.HealthCheck``.
            instances: ``AWS::ElasticLoadBalancing::LoadBalancer.Instances``.
            lb_cookie_stickiness_policy: ``AWS::ElasticLoadBalancing::LoadBalancer.LBCookieStickinessPolicy``.
            load_balancer_name: ``AWS::ElasticLoadBalancing::LoadBalancer.LoadBalancerName``.
            policies: ``AWS::ElasticLoadBalancing::LoadBalancer.Policies``.
            scheme: ``AWS::ElasticLoadBalancing::LoadBalancer.Scheme``.
            security_groups: ``AWS::ElasticLoadBalancing::LoadBalancer.SecurityGroups``.
            subnets: ``AWS::ElasticLoadBalancing::LoadBalancer.Subnets``.
            tags: ``AWS::ElasticLoadBalancing::LoadBalancer.Tags``.

        Stability:
            stable
        """
        props: CfnLoadBalancerProps = {"listeners": listeners}

        if access_logging_policy is not None:
            props["accessLoggingPolicy"] = access_logging_policy

        if app_cookie_stickiness_policy is not None:
            props["appCookieStickinessPolicy"] = app_cookie_stickiness_policy

        if availability_zones is not None:
            props["availabilityZones"] = availability_zones

        if connection_draining_policy is not None:
            props["connectionDrainingPolicy"] = connection_draining_policy

        if connection_settings is not None:
            props["connectionSettings"] = connection_settings

        if cross_zone is not None:
            props["crossZone"] = cross_zone

        if health_check is not None:
            props["healthCheck"] = health_check

        if instances is not None:
            props["instances"] = instances

        if lb_cookie_stickiness_policy is not None:
            props["lbCookieStickinessPolicy"] = lb_cookie_stickiness_policy

        if load_balancer_name is not None:
            props["loadBalancerName"] = load_balancer_name

        if policies is not None:
            props["policies"] = policies

        if scheme is not None:
            props["scheme"] = scheme

        if security_groups is not None:
            props["securityGroups"] = security_groups

        if subnets is not None:
            props["subnets"] = subnets

        if tags is not None:
            props["tags"] = tags

        jsii.create(CfnLoadBalancer, self, [scope, id, props])

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
    @jsii.member(jsii_name="attrCanonicalHostedZoneName")
    def attr_canonical_hosted_zone_name(self) -> str:
        """
        Stability:
            stable
        cloudformationAttribute:
            CanonicalHostedZoneName
        """
        return jsii.get(self, "attrCanonicalHostedZoneName")

    @property
    @jsii.member(jsii_name="attrCanonicalHostedZoneNameId")
    def attr_canonical_hosted_zone_name_id(self) -> str:
        """
        Stability:
            stable
        cloudformationAttribute:
            CanonicalHostedZoneNameID
        """
        return jsii.get(self, "attrCanonicalHostedZoneNameId")

    @property
    @jsii.member(jsii_name="attrDnsName")
    def attr_dns_name(self) -> str:
        """
        Stability:
            stable
        cloudformationAttribute:
            DNSName
        """
        return jsii.get(self, "attrDnsName")

    @property
    @jsii.member(jsii_name="attrSourceSecurityGroupGroupName")
    def attr_source_security_group_group_name(self) -> str:
        """
        Stability:
            stable
        cloudformationAttribute:
            SourceSecurityGroup.GroupName
        """
        return jsii.get(self, "attrSourceSecurityGroupGroupName")

    @property
    @jsii.member(jsii_name="attrSourceSecurityGroupOwnerAlias")
    def attr_source_security_group_owner_alias(self) -> str:
        """
        Stability:
            stable
        cloudformationAttribute:
            SourceSecurityGroup.OwnerAlias
        """
        return jsii.get(self, "attrSourceSecurityGroupOwnerAlias")

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
        """``AWS::ElasticLoadBalancing::LoadBalancer.Tags``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-elasticloadbalancing-loadbalancer-tags
        Stability:
            stable
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="listeners")
    def listeners(self) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["ListenersProperty", aws_cdk.core.IResolvable]]]:
        """``AWS::ElasticLoadBalancing::LoadBalancer.Listeners``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-listeners
        Stability:
            stable
        """
        return jsii.get(self, "listeners")

    @listeners.setter
    def listeners(self, value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["ListenersProperty", aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "listeners", value)

    @property
    @jsii.member(jsii_name="accessLoggingPolicy")
    def access_logging_policy(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AccessLoggingPolicyProperty"]]]:
        """``AWS::ElasticLoadBalancing::LoadBalancer.AccessLoggingPolicy``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-accessloggingpolicy
        Stability:
            stable
        """
        return jsii.get(self, "accessLoggingPolicy")

    @access_logging_policy.setter
    def access_logging_policy(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["AccessLoggingPolicyProperty"]]]):
        return jsii.set(self, "accessLoggingPolicy", value)

    @property
    @jsii.member(jsii_name="appCookieStickinessPolicy")
    def app_cookie_stickiness_policy(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "AppCookieStickinessPolicyProperty"]]]]]:
        """``AWS::ElasticLoadBalancing::LoadBalancer.AppCookieStickinessPolicy``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-appcookiestickinesspolicy
        Stability:
            stable
        """
        return jsii.get(self, "appCookieStickinessPolicy")

    @app_cookie_stickiness_policy.setter
    def app_cookie_stickiness_policy(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "AppCookieStickinessPolicyProperty"]]]]]):
        return jsii.set(self, "appCookieStickinessPolicy", value)

    @property
    @jsii.member(jsii_name="availabilityZones")
    def availability_zones(self) -> typing.Optional[typing.List[str]]:
        """``AWS::ElasticLoadBalancing::LoadBalancer.AvailabilityZones``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-availabilityzones
        Stability:
            stable
        """
        return jsii.get(self, "availabilityZones")

    @availability_zones.setter
    def availability_zones(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "availabilityZones", value)

    @property
    @jsii.member(jsii_name="connectionDrainingPolicy")
    def connection_draining_policy(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ConnectionDrainingPolicyProperty"]]]:
        """``AWS::ElasticLoadBalancing::LoadBalancer.ConnectionDrainingPolicy``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-connectiondrainingpolicy
        Stability:
            stable
        """
        return jsii.get(self, "connectionDrainingPolicy")

    @connection_draining_policy.setter
    def connection_draining_policy(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ConnectionDrainingPolicyProperty"]]]):
        return jsii.set(self, "connectionDrainingPolicy", value)

    @property
    @jsii.member(jsii_name="connectionSettings")
    def connection_settings(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ConnectionSettingsProperty"]]]:
        """``AWS::ElasticLoadBalancing::LoadBalancer.ConnectionSettings``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-connectionsettings
        Stability:
            stable
        """
        return jsii.get(self, "connectionSettings")

    @connection_settings.setter
    def connection_settings(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["ConnectionSettingsProperty"]]]):
        return jsii.set(self, "connectionSettings", value)

    @property
    @jsii.member(jsii_name="crossZone")
    def cross_zone(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::ElasticLoadBalancing::LoadBalancer.CrossZone``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-crosszone
        Stability:
            stable
        """
        return jsii.get(self, "crossZone")

    @cross_zone.setter
    def cross_zone(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "crossZone", value)

    @property
    @jsii.member(jsii_name="healthCheck")
    def health_check(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["HealthCheckProperty"]]]:
        """``AWS::ElasticLoadBalancing::LoadBalancer.HealthCheck``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-healthcheck
        Stability:
            stable
        """
        return jsii.get(self, "healthCheck")

    @health_check.setter
    def health_check(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional["HealthCheckProperty"]]]):
        return jsii.set(self, "healthCheck", value)

    @property
    @jsii.member(jsii_name="instances")
    def instances(self) -> typing.Optional[typing.List[str]]:
        """``AWS::ElasticLoadBalancing::LoadBalancer.Instances``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-instances
        Stability:
            stable
        """
        return jsii.get(self, "instances")

    @instances.setter
    def instances(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "instances", value)

    @property
    @jsii.member(jsii_name="lbCookieStickinessPolicy")
    def lb_cookie_stickiness_policy(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "LBCookieStickinessPolicyProperty"]]]]]:
        """``AWS::ElasticLoadBalancing::LoadBalancer.LBCookieStickinessPolicy``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-lbcookiestickinesspolicy
        Stability:
            stable
        """
        return jsii.get(self, "lbCookieStickinessPolicy")

    @lb_cookie_stickiness_policy.setter
    def lb_cookie_stickiness_policy(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "LBCookieStickinessPolicyProperty"]]]]]):
        return jsii.set(self, "lbCookieStickinessPolicy", value)

    @property
    @jsii.member(jsii_name="loadBalancerName")
    def load_balancer_name(self) -> typing.Optional[str]:
        """``AWS::ElasticLoadBalancing::LoadBalancer.LoadBalancerName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-elbname
        Stability:
            stable
        """
        return jsii.get(self, "loadBalancerName")

    @load_balancer_name.setter
    def load_balancer_name(self, value: typing.Optional[str]):
        return jsii.set(self, "loadBalancerName", value)

    @property
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "PoliciesProperty"]]]]]:
        """``AWS::ElasticLoadBalancing::LoadBalancer.Policies``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-policies
        Stability:
            stable
        """
        return jsii.get(self, "policies")

    @policies.setter
    def policies(self, value: typing.Optional[typing.Union[typing.Optional[aws_cdk.core.IResolvable], typing.Optional[typing.List[typing.Union[aws_cdk.core.IResolvable, "PoliciesProperty"]]]]]):
        return jsii.set(self, "policies", value)

    @property
    @jsii.member(jsii_name="scheme")
    def scheme(self) -> typing.Optional[str]:
        """``AWS::ElasticLoadBalancing::LoadBalancer.Scheme``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-scheme
        Stability:
            stable
        """
        return jsii.get(self, "scheme")

    @scheme.setter
    def scheme(self, value: typing.Optional[str]):
        return jsii.set(self, "scheme", value)

    @property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.Optional[typing.List[str]]:
        """``AWS::ElasticLoadBalancing::LoadBalancer.SecurityGroups``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-securitygroups
        Stability:
            stable
        """
        return jsii.get(self, "securityGroups")

    @security_groups.setter
    def security_groups(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "securityGroups", value)

    @property
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.Optional[typing.List[str]]:
        """``AWS::ElasticLoadBalancing::LoadBalancer.Subnets``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-subnets
        Stability:
            stable
        """
        return jsii.get(self, "subnets")

    @subnets.setter
    def subnets(self, value: typing.Optional[typing.List[str]]):
        return jsii.set(self, "subnets", value)

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _AccessLoggingPolicyProperty(jsii.compat.TypedDict, total=False):
        emitInterval: jsii.Number
        """``CfnLoadBalancer.AccessLoggingPolicyProperty.EmitInterval``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-accessloggingpolicy.html#cfn-elb-accessloggingpolicy-emitinterval
        Stability:
            stable
        """
        s3BucketPrefix: str
        """``CfnLoadBalancer.AccessLoggingPolicyProperty.S3BucketPrefix``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-accessloggingpolicy.html#cfn-elb-accessloggingpolicy-s3bucketprefix
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-elasticloadbalancing.CfnLoadBalancer.AccessLoggingPolicyProperty", jsii_struct_bases=[_AccessLoggingPolicyProperty])
    class AccessLoggingPolicyProperty(_AccessLoggingPolicyProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-accessloggingpolicy.html
        Stability:
            stable
        """
        enabled: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnLoadBalancer.AccessLoggingPolicyProperty.Enabled``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-accessloggingpolicy.html#cfn-elb-accessloggingpolicy-enabled
        Stability:
            stable
        """

        s3BucketName: str
        """``CfnLoadBalancer.AccessLoggingPolicyProperty.S3BucketName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-accessloggingpolicy.html#cfn-elb-accessloggingpolicy-s3bucketname
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-elasticloadbalancing.CfnLoadBalancer.AppCookieStickinessPolicyProperty", jsii_struct_bases=[])
    class AppCookieStickinessPolicyProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-AppCookieStickinessPolicy.html
        Stability:
            stable
        """
        cookieName: str
        """``CfnLoadBalancer.AppCookieStickinessPolicyProperty.CookieName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-AppCookieStickinessPolicy.html#cfn-elb-appcookiestickinesspolicy-cookiename
        Stability:
            stable
        """

        policyName: str
        """``CfnLoadBalancer.AppCookieStickinessPolicyProperty.PolicyName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-AppCookieStickinessPolicy.html#cfn-elb-appcookiestickinesspolicy-policyname
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _ConnectionDrainingPolicyProperty(jsii.compat.TypedDict, total=False):
        timeout: jsii.Number
        """``CfnLoadBalancer.ConnectionDrainingPolicyProperty.Timeout``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-connectiondrainingpolicy.html#cfn-elb-connectiondrainingpolicy-timeout
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-elasticloadbalancing.CfnLoadBalancer.ConnectionDrainingPolicyProperty", jsii_struct_bases=[_ConnectionDrainingPolicyProperty])
    class ConnectionDrainingPolicyProperty(_ConnectionDrainingPolicyProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-connectiondrainingpolicy.html
        Stability:
            stable
        """
        enabled: typing.Union[bool, aws_cdk.core.IResolvable]
        """``CfnLoadBalancer.ConnectionDrainingPolicyProperty.Enabled``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-connectiondrainingpolicy.html#cfn-elb-connectiondrainingpolicy-enabled
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-elasticloadbalancing.CfnLoadBalancer.ConnectionSettingsProperty", jsii_struct_bases=[])
    class ConnectionSettingsProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-connectionsettings.html
        Stability:
            stable
        """
        idleTimeout: jsii.Number
        """``CfnLoadBalancer.ConnectionSettingsProperty.IdleTimeout``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-connectionsettings.html#cfn-elb-connectionsettings-idletimeout
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-elasticloadbalancing.CfnLoadBalancer.HealthCheckProperty", jsii_struct_bases=[])
    class HealthCheckProperty(jsii.compat.TypedDict):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-health-check.html
        Stability:
            stable
        """
        healthyThreshold: str
        """``CfnLoadBalancer.HealthCheckProperty.HealthyThreshold``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-health-check.html#cfn-elb-healthcheck-healthythreshold
        Stability:
            stable
        """

        interval: str
        """``CfnLoadBalancer.HealthCheckProperty.Interval``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-health-check.html#cfn-elb-healthcheck-interval
        Stability:
            stable
        """

        target: str
        """``CfnLoadBalancer.HealthCheckProperty.Target``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-health-check.html#cfn-elb-healthcheck-target
        Stability:
            stable
        """

        timeout: str
        """``CfnLoadBalancer.HealthCheckProperty.Timeout``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-health-check.html#cfn-elb-healthcheck-timeout
        Stability:
            stable
        """

        unhealthyThreshold: str
        """``CfnLoadBalancer.HealthCheckProperty.UnhealthyThreshold``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-health-check.html#cfn-elb-healthcheck-unhealthythreshold
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-elasticloadbalancing.CfnLoadBalancer.LBCookieStickinessPolicyProperty", jsii_struct_bases=[])
    class LBCookieStickinessPolicyProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-LBCookieStickinessPolicy.html
        Stability:
            stable
        """
        cookieExpirationPeriod: str
        """``CfnLoadBalancer.LBCookieStickinessPolicyProperty.CookieExpirationPeriod``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-LBCookieStickinessPolicy.html#cfn-elb-lbcookiestickinesspolicy-cookieexpirationperiod
        Stability:
            stable
        """

        policyName: str
        """``CfnLoadBalancer.LBCookieStickinessPolicyProperty.PolicyName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-LBCookieStickinessPolicy.html#cfn-elb-lbcookiestickinesspolicy-policyname
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _ListenersProperty(jsii.compat.TypedDict, total=False):
        instanceProtocol: str
        """``CfnLoadBalancer.ListenersProperty.InstanceProtocol``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-listener.html#cfn-ec2-elb-listener-instanceprotocol
        Stability:
            stable
        """
        policyNames: typing.List[str]
        """``CfnLoadBalancer.ListenersProperty.PolicyNames``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-listener.html#cfn-ec2-elb-listener-policynames
        Stability:
            stable
        """
        sslCertificateId: str
        """``CfnLoadBalancer.ListenersProperty.SSLCertificateId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-listener.html#cfn-ec2-elb-listener-sslcertificateid
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-elasticloadbalancing.CfnLoadBalancer.ListenersProperty", jsii_struct_bases=[_ListenersProperty])
    class ListenersProperty(_ListenersProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-listener.html
        Stability:
            stable
        """
        instancePort: str
        """``CfnLoadBalancer.ListenersProperty.InstancePort``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-listener.html#cfn-ec2-elb-listener-instanceport
        Stability:
            stable
        """

        loadBalancerPort: str
        """``CfnLoadBalancer.ListenersProperty.LoadBalancerPort``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-listener.html#cfn-ec2-elb-listener-loadbalancerport
        Stability:
            stable
        """

        protocol: str
        """``CfnLoadBalancer.ListenersProperty.Protocol``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-listener.html#cfn-ec2-elb-listener-protocol
        Stability:
            stable
        """

    @jsii.data_type_optionals(jsii_struct_bases=[])
    class _PoliciesProperty(jsii.compat.TypedDict, total=False):
        instancePorts: typing.List[str]
        """``CfnLoadBalancer.PoliciesProperty.InstancePorts``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-policy.html#cfn-ec2-elb-policy-instanceports
        Stability:
            stable
        """
        loadBalancerPorts: typing.List[str]
        """``CfnLoadBalancer.PoliciesProperty.LoadBalancerPorts``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-policy.html#cfn-ec2-elb-policy-loadbalancerports
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-elasticloadbalancing.CfnLoadBalancer.PoliciesProperty", jsii_struct_bases=[_PoliciesProperty])
    class PoliciesProperty(_PoliciesProperty):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-policy.html
        Stability:
            stable
        """
        attributes: typing.Union[typing.List[typing.Any], aws_cdk.core.IResolvable]
        """``CfnLoadBalancer.PoliciesProperty.Attributes``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-policy.html#cfn-ec2-elb-policy-attributes
        Stability:
            stable
        """

        policyName: str
        """``CfnLoadBalancer.PoliciesProperty.PolicyName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-policy.html#cfn-ec2-elb-policy-policyname
        Stability:
            stable
        """

        policyType: str
        """``CfnLoadBalancer.PoliciesProperty.PolicyType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb-policy.html#cfn-ec2-elb-policy-policytype
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnLoadBalancerProps(jsii.compat.TypedDict, total=False):
    accessLoggingPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnLoadBalancer.AccessLoggingPolicyProperty"]
    """``AWS::ElasticLoadBalancing::LoadBalancer.AccessLoggingPolicy``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-accessloggingpolicy
    Stability:
        stable
    """
    appCookieStickinessPolicy: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLoadBalancer.AppCookieStickinessPolicyProperty"]]]
    """``AWS::ElasticLoadBalancing::LoadBalancer.AppCookieStickinessPolicy``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-appcookiestickinesspolicy
    Stability:
        stable
    """
    availabilityZones: typing.List[str]
    """``AWS::ElasticLoadBalancing::LoadBalancer.AvailabilityZones``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-availabilityzones
    Stability:
        stable
    """
    connectionDrainingPolicy: typing.Union[aws_cdk.core.IResolvable, "CfnLoadBalancer.ConnectionDrainingPolicyProperty"]
    """``AWS::ElasticLoadBalancing::LoadBalancer.ConnectionDrainingPolicy``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-connectiondrainingpolicy
    Stability:
        stable
    """
    connectionSettings: typing.Union[aws_cdk.core.IResolvable, "CfnLoadBalancer.ConnectionSettingsProperty"]
    """``AWS::ElasticLoadBalancing::LoadBalancer.ConnectionSettings``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-connectionsettings
    Stability:
        stable
    """
    crossZone: typing.Union[bool, aws_cdk.core.IResolvable]
    """``AWS::ElasticLoadBalancing::LoadBalancer.CrossZone``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-crosszone
    Stability:
        stable
    """
    healthCheck: typing.Union[aws_cdk.core.IResolvable, "CfnLoadBalancer.HealthCheckProperty"]
    """``AWS::ElasticLoadBalancing::LoadBalancer.HealthCheck``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-healthcheck
    Stability:
        stable
    """
    instances: typing.List[str]
    """``AWS::ElasticLoadBalancing::LoadBalancer.Instances``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-instances
    Stability:
        stable
    """
    lbCookieStickinessPolicy: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLoadBalancer.LBCookieStickinessPolicyProperty"]]]
    """``AWS::ElasticLoadBalancing::LoadBalancer.LBCookieStickinessPolicy``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-lbcookiestickinesspolicy
    Stability:
        stable
    """
    loadBalancerName: str
    """``AWS::ElasticLoadBalancing::LoadBalancer.LoadBalancerName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-elbname
    Stability:
        stable
    """
    policies: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnLoadBalancer.PoliciesProperty"]]]
    """``AWS::ElasticLoadBalancing::LoadBalancer.Policies``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-policies
    Stability:
        stable
    """
    scheme: str
    """``AWS::ElasticLoadBalancing::LoadBalancer.Scheme``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-scheme
    Stability:
        stable
    """
    securityGroups: typing.List[str]
    """``AWS::ElasticLoadBalancing::LoadBalancer.SecurityGroups``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-securitygroups
    Stability:
        stable
    """
    subnets: typing.List[str]
    """``AWS::ElasticLoadBalancing::LoadBalancer.Subnets``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-subnets
    Stability:
        stable
    """
    tags: typing.List[aws_cdk.core.CfnTag]
    """``AWS::ElasticLoadBalancing::LoadBalancer.Tags``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-elasticloadbalancing-loadbalancer-tags
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-elasticloadbalancing.CfnLoadBalancerProps", jsii_struct_bases=[_CfnLoadBalancerProps])
class CfnLoadBalancerProps(_CfnLoadBalancerProps):
    """Properties for defining a ``AWS::ElasticLoadBalancing::LoadBalancer``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html
    Stability:
        stable
    """
    listeners: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union["CfnLoadBalancer.ListenersProperty", aws_cdk.core.IResolvable]]]
    """``AWS::ElasticLoadBalancing::LoadBalancer.Listeners``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#cfn-ec2-elb-listeners
    Stability:
        stable
    """

@jsii.data_type_optionals(jsii_struct_bases=[])
class _HealthCheck(jsii.compat.TypedDict, total=False):
    healthyThreshold: jsii.Number
    """After how many successful checks is an instance considered healthy.

    Default:
        2

    Stability:
        stable
    """
    interval: aws_cdk.core.Duration
    """Number of seconds between health checks.

    Default:
        Duration.seconds(30)

    Stability:
        stable
    """
    path: str
    """What path to use for HTTP or HTTPS health check (must return 200).

    For SSL and TCP health checks, accepting connections is enough to be considered
    healthy.

    Default:
        "/"

    Stability:
        stable
    """
    protocol: "LoadBalancingProtocol"
    """What protocol to use for health checking.

    The protocol is automatically determined from the port if it's not supplied.

    Default:
        Automatic

    Stability:
        stable
    """
    timeout: aws_cdk.core.Duration
    """Health check timeout.

    Default:
        Duration.seconds(5)

    Stability:
        stable
    """
    unhealthyThreshold: jsii.Number
    """After how many unsuccessful checks is an instance considered unhealthy.

    Default:
        5

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-elasticloadbalancing.HealthCheck", jsii_struct_bases=[_HealthCheck])
class HealthCheck(_HealthCheck):
    """Describe the health check to a load balancer.

    Stability:
        stable
    """
    port: jsii.Number
    """What port number to health check on.

    Stability:
        stable
    """

@jsii.interface(jsii_type="@aws-cdk/aws-elasticloadbalancing.ILoadBalancerTarget")
class ILoadBalancerTarget(aws_cdk.aws_ec2.IConnectable, jsii.compat.Protocol):
    """Interface that is going to be implemented by constructs that you can load balance to.

    Stability:
        stable
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _ILoadBalancerTargetProxy

    @jsii.member(jsii_name="attachToClassicLB")
    def attach_to_classic_lb(self, load_balancer: "LoadBalancer") -> None:
        """Attach load-balanced target to a classic ELB.

        Arguments:
            load_balancer: [disable-awslint:ref-via-interface] The load balancer to attach the target to.

        Stability:
            stable
        """
        ...


class _ILoadBalancerTargetProxy(jsii.proxy_for(aws_cdk.aws_ec2.IConnectable)):
    """Interface that is going to be implemented by constructs that you can load balance to.

    Stability:
        stable
    """
    __jsii_type__ = "@aws-cdk/aws-elasticloadbalancing.ILoadBalancerTarget"
    @jsii.member(jsii_name="attachToClassicLB")
    def attach_to_classic_lb(self, load_balancer: "LoadBalancer") -> None:
        """Attach load-balanced target to a classic ELB.

        Arguments:
            load_balancer: [disable-awslint:ref-via-interface] The load balancer to attach the target to.

        Stability:
            stable
        """
        return jsii.invoke(self, "attachToClassicLB", [load_balancer])


@jsii.implements(aws_cdk.aws_ec2.IConnectable)
class ListenerPort(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-elasticloadbalancing.ListenerPort"):
    """Reference to a listener's port just created.

    This implements IConnectable with a default port (the port that an ELB
    listener was just created on) for a given security group so that it can be
    conveniently used just like any Connectable. E.g::

       const listener = elb.addListener(...);

       listener.connections.allowDefaultPortFromAnyIPv4();
       // or
       instance.connections.allowToDefaultPort(listener);

    Stability:
        stable
    """
    def __init__(self, security_group: aws_cdk.aws_ec2.ISecurityGroup, default_port: aws_cdk.aws_ec2.Port) -> None:
        """
        Arguments:
            security_group: -
            default_port: -

        Stability:
            stable
        """
        jsii.create(ListenerPort, self, [security_group, default_port])

    @property
    @jsii.member(jsii_name="connections")
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        """
        Stability:
            stable
        """
        return jsii.get(self, "connections")


@jsii.implements(aws_cdk.aws_ec2.IConnectable)
class LoadBalancer(aws_cdk.core.Resource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-elasticloadbalancing.LoadBalancer"):
    """A load balancer with a single listener.

    Routes to a fleet of of instances in a VPC.

    Stability:
        stable
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, vpc: aws_cdk.aws_ec2.IVpc, cross_zone: typing.Optional[bool]=None, health_check: typing.Optional["HealthCheck"]=None, internet_facing: typing.Optional[bool]=None, listeners: typing.Optional[typing.List["LoadBalancerListener"]]=None, targets: typing.Optional[typing.List["ILoadBalancerTarget"]]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            vpc: VPC network of the fleet instances.
            cross_zone: Whether cross zone load balancing is enabled. This controls whether the load balancer evenly distributes requests across each availability zone Default: true
            health_check: Health check settings for the load balancing targets. Not required but recommended. Default: - None.
            internet_facing: Whether this is an internet-facing Load Balancer. This controls whether the LB has a public IP address assigned. It does not open up the Load Balancer's security groups to public internet access. Default: false
            listeners: What listeners to set up for the load balancer. Can also be added by .addListener() Default: -
            targets: What targets to load balance to. Can also be added by .addTarget() Default: - None.

        Stability:
            stable
        """
        props: LoadBalancerProps = {"vpc": vpc}

        if cross_zone is not None:
            props["crossZone"] = cross_zone

        if health_check is not None:
            props["healthCheck"] = health_check

        if internet_facing is not None:
            props["internetFacing"] = internet_facing

        if listeners is not None:
            props["listeners"] = listeners

        if targets is not None:
            props["targets"] = targets

        jsii.create(LoadBalancer, self, [scope, id, props])

    @jsii.member(jsii_name="addListener")
    def add_listener(self, *, external_port: jsii.Number, allow_connections_from: typing.Optional[typing.List[aws_cdk.aws_ec2.IConnectable]]=None, external_protocol: typing.Optional["LoadBalancingProtocol"]=None, internal_port: typing.Optional[jsii.Number]=None, internal_protocol: typing.Optional["LoadBalancingProtocol"]=None, policy_names: typing.Optional[typing.List[str]]=None, ssl_certificate_id: typing.Optional[str]=None) -> "ListenerPort":
        """Add a backend to the load balancer.

        Arguments:
            listener: -
            external_port: External listening port.
            allow_connections_from: Allow connections to the load balancer from the given set of connection peers. By default, connections will be allowed from anywhere. Set this to an empty list to deny connections, or supply a custom list of peers to allow connections from (IP ranges or security groups). Default: Anywhere
            external_protocol: What public protocol to use for load balancing. Either 'tcp', 'ssl', 'http' or 'https'. May be omitted if the external port is either 80 or 443.
            internal_port: Instance listening port. Same as the externalPort if not specified. Default: externalPort
            internal_protocol: What public protocol to use for load balancing. Either 'tcp', 'ssl', 'http' or 'https'. May be omitted if the internal port is either 80 or 443. The instance protocol is 'tcp' if the front-end protocol is 'tcp' or 'ssl', the instance protocol is 'http' if the front-end protocol is 'https'.
            policy_names: SSL policy names.
            ssl_certificate_id: ID of SSL certificate.

        Returns:
            A ListenerPort object that controls connections to the listener port

        Stability:
            stable
        """
        listener: LoadBalancerListener = {"externalPort": external_port}

        if allow_connections_from is not None:
            listener["allowConnectionsFrom"] = allow_connections_from

        if external_protocol is not None:
            listener["externalProtocol"] = external_protocol

        if internal_port is not None:
            listener["internalPort"] = internal_port

        if internal_protocol is not None:
            listener["internalProtocol"] = internal_protocol

        if policy_names is not None:
            listener["policyNames"] = policy_names

        if ssl_certificate_id is not None:
            listener["sslCertificateId"] = ssl_certificate_id

        return jsii.invoke(self, "addListener", [listener])

    @jsii.member(jsii_name="addTarget")
    def add_target(self, target: "ILoadBalancerTarget") -> None:
        """
        Arguments:
            target: -

        Stability:
            stable
        """
        return jsii.invoke(self, "addTarget", [target])

    @property
    @jsii.member(jsii_name="connections")
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        """Control all connections from and to this load balancer.

        Stability:
            stable
        """
        return jsii.get(self, "connections")

    @property
    @jsii.member(jsii_name="listenerPorts")
    def listener_ports(self) -> typing.List["ListenerPort"]:
        """An object controlling specifically the connections for each listener added to this load balancer.

        Stability:
            stable
        """
        return jsii.get(self, "listenerPorts")

    @property
    @jsii.member(jsii_name="loadBalancerCanonicalHostedZoneName")
    def load_balancer_canonical_hosted_zone_name(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "loadBalancerCanonicalHostedZoneName")

    @property
    @jsii.member(jsii_name="loadBalancerCanonicalHostedZoneNameId")
    def load_balancer_canonical_hosted_zone_name_id(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "loadBalancerCanonicalHostedZoneNameId")

    @property
    @jsii.member(jsii_name="loadBalancerDnsName")
    def load_balancer_dns_name(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "loadBalancerDnsName")

    @property
    @jsii.member(jsii_name="loadBalancerName")
    def load_balancer_name(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "loadBalancerName")

    @property
    @jsii.member(jsii_name="loadBalancerSourceSecurityGroupGroupName")
    def load_balancer_source_security_group_group_name(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "loadBalancerSourceSecurityGroupGroupName")

    @property
    @jsii.member(jsii_name="loadBalancerSourceSecurityGroupOwnerAlias")
    def load_balancer_source_security_group_owner_alias(self) -> str:
        """
        Stability:
            stable
        attribute:
            true
        """
        return jsii.get(self, "loadBalancerSourceSecurityGroupOwnerAlias")


@jsii.data_type_optionals(jsii_struct_bases=[])
class _LoadBalancerListener(jsii.compat.TypedDict, total=False):
    allowConnectionsFrom: typing.List[aws_cdk.aws_ec2.IConnectable]
    """Allow connections to the load balancer from the given set of connection peers.

    By default, connections will be allowed from anywhere. Set this to an empty list
    to deny connections, or supply a custom list of peers to allow connections from
    (IP ranges or security groups).

    Default:
        Anywhere

    Stability:
        stable
    """
    externalProtocol: "LoadBalancingProtocol"
    """What public protocol to use for load balancing.

    Either 'tcp', 'ssl', 'http' or 'https'.

    May be omitted if the external port is either 80 or 443.

    Stability:
        stable
    """
    internalPort: jsii.Number
    """Instance listening port.

    Same as the externalPort if not specified.

    Default:
        externalPort

    Stability:
        stable
    """
    internalProtocol: "LoadBalancingProtocol"
    """What public protocol to use for load balancing.

    Either 'tcp', 'ssl', 'http' or 'https'.

    May be omitted if the internal port is either 80 or 443.

    The instance protocol is 'tcp' if the front-end protocol
    is 'tcp' or 'ssl', the instance protocol is 'http' if the
    front-end protocol is 'https'.

    Stability:
        stable
    """
    policyNames: typing.List[str]
    """SSL policy names.

    Stability:
        stable
    """
    sslCertificateId: str
    """ID of SSL certificate.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-elasticloadbalancing.LoadBalancerListener", jsii_struct_bases=[_LoadBalancerListener])
class LoadBalancerListener(_LoadBalancerListener):
    """Add a backend to the load balancer.

    Stability:
        stable
    """
    externalPort: jsii.Number
    """External listening port.

    Stability:
        stable
    """

@jsii.data_type_optionals(jsii_struct_bases=[])
class _LoadBalancerProps(jsii.compat.TypedDict, total=False):
    crossZone: bool
    """Whether cross zone load balancing is enabled.

    This controls whether the load balancer evenly distributes requests
    across each availability zone

    Default:
        true

    Stability:
        stable
    """
    healthCheck: "HealthCheck"
    """Health check settings for the load balancing targets.

    Not required but recommended.

    Default:
        - None.

    Stability:
        stable
    """
    internetFacing: bool
    """Whether this is an internet-facing Load Balancer.

    This controls whether the LB has a public IP address assigned. It does
    not open up the Load Balancer's security groups to public internet access.

    Default:
        false

    Stability:
        stable
    """
    listeners: typing.List["LoadBalancerListener"]
    """What listeners to set up for the load balancer.

    Can also be added by .addListener()

    Default:
        -

    Stability:
        stable
    """
    targets: typing.List["ILoadBalancerTarget"]
    """What targets to load balance to.

    Can also be added by .addTarget()

    Default:
        - None.

    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-elasticloadbalancing.LoadBalancerProps", jsii_struct_bases=[_LoadBalancerProps])
class LoadBalancerProps(_LoadBalancerProps):
    """Construction properties for a LoadBalancer.

    Stability:
        stable
    """
    vpc: aws_cdk.aws_ec2.IVpc
    """VPC network of the fleet instances.

    Stability:
        stable
    """

@jsii.enum(jsii_type="@aws-cdk/aws-elasticloadbalancing.LoadBalancingProtocol")
class LoadBalancingProtocol(enum.Enum):
    """
    Stability:
        stable
    """
    TCP = "TCP"
    """
    Stability:
        stable
    """
    SSL = "SSL"
    """
    Stability:
        stable
    """
    HTTP = "HTTP"
    """
    Stability:
        stable
    """
    HTTPS = "HTTPS"
    """
    Stability:
        stable
    """

__all__ = ["CfnLoadBalancer", "CfnLoadBalancerProps", "HealthCheck", "ILoadBalancerTarget", "ListenerPort", "LoadBalancer", "LoadBalancerListener", "LoadBalancerProps", "LoadBalancingProtocol", "__jsii_assembly__"]

publication.publish()
