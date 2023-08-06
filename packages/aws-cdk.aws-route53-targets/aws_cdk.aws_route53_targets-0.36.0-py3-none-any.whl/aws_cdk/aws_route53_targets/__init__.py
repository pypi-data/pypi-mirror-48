import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_cloudfront
import aws_cdk.aws_elasticloadbalancingv2
import aws_cdk.aws_iam
import aws_cdk.aws_route53
import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-route53-targets", "0.36.0", __name__, "aws-route53-targets@0.36.0.jsii.tgz")
@jsii.implements(aws_cdk.aws_route53.IAliasRecordTarget)
class CloudFrontTarget(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53-targets.CloudFrontTarget"):
    """Use a CloudFront Distribution as an alias record target.

    Stability:
        experimental
    """
    def __init__(self, distribution: aws_cdk.aws_cloudfront.CloudFrontWebDistribution) -> None:
        """
        Arguments:
            distribution: -

        Stability:
            experimental
        """
        jsii.create(CloudFrontTarget, self, [distribution])

    @jsii.member(jsii_name="bind")
    def bind(self, _record: aws_cdk.aws_route53.IRecordSet) -> aws_cdk.aws_route53.AliasRecordTargetConfig:
        """Return hosted zone ID and DNS name, usable for Route53 alias targets.

        Arguments:
            _record: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "bind", [_record])


@jsii.implements(aws_cdk.aws_route53.IAliasRecordTarget)
class LoadBalancerTarget(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53-targets.LoadBalancerTarget"):
    """Use an ELBv2 as an alias record target.

    Stability:
        experimental
    """
    def __init__(self, load_balancer: aws_cdk.aws_elasticloadbalancingv2.ILoadBalancerV2) -> None:
        """
        Arguments:
            load_balancer: -

        Stability:
            experimental
        """
        jsii.create(LoadBalancerTarget, self, [load_balancer])

    @jsii.member(jsii_name="bind")
    def bind(self, _record: aws_cdk.aws_route53.IRecordSet) -> aws_cdk.aws_route53.AliasRecordTargetConfig:
        """Return hosted zone ID and DNS name, usable for Route53 alias targets.

        Arguments:
            _record: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "bind", [_record])


__all__ = ["CloudFrontTarget", "LoadBalancerTarget", "__jsii_assembly__"]

publication.publish()
