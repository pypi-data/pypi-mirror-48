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
import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-ecr", "0.36.0", __name__, "aws-ecr@0.36.0.jsii.tgz")
class CfnRepository(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ecr.CfnRepository"):
    """A CloudFormation ``AWS::ECR::Repository``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html
    Stability:
        stable
    cloudformationResource:
        AWS::ECR::Repository
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, lifecycle_policy: typing.Optional[typing.Union[typing.Optional["LifecyclePolicyProperty"], typing.Optional[aws_cdk.core.IResolvable]]]=None, repository_name: typing.Optional[str]=None, repository_policy_text: typing.Any=None, tags: typing.Optional[typing.List[aws_cdk.core.CfnTag]]=None) -> None:
        """Create a new ``AWS::ECR::Repository``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            lifecycle_policy: ``AWS::ECR::Repository.LifecyclePolicy``.
            repository_name: ``AWS::ECR::Repository.RepositoryName``.
            repository_policy_text: ``AWS::ECR::Repository.RepositoryPolicyText``.
            tags: ``AWS::ECR::Repository.Tags``.

        Stability:
            experimental
        """
        props: CfnRepositoryProps = {}

        if lifecycle_policy is not None:
            props["lifecyclePolicy"] = lifecycle_policy

        if repository_name is not None:
            props["repositoryName"] = repository_name

        if repository_policy_text is not None:
            props["repositoryPolicyText"] = repository_policy_text

        if tags is not None:
            props["tags"] = tags

        jsii.create(CfnRepository, self, [scope, id, props])

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
        """``AWS::ECR::Repository.Tags``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-tags
        Stability:
            stable
        """
        return jsii.get(self, "tags")

    @property
    @jsii.member(jsii_name="repositoryPolicyText")
    def repository_policy_text(self) -> typing.Any:
        """``AWS::ECR::Repository.RepositoryPolicyText``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-repositorypolicytext
        Stability:
            stable
        """
        return jsii.get(self, "repositoryPolicyText")

    @repository_policy_text.setter
    def repository_policy_text(self, value: typing.Any):
        return jsii.set(self, "repositoryPolicyText", value)

    @property
    @jsii.member(jsii_name="lifecyclePolicy")
    def lifecycle_policy(self) -> typing.Optional[typing.Union[typing.Optional["LifecyclePolicyProperty"], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::ECR::Repository.LifecyclePolicy``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-lifecyclepolicy
        Stability:
            stable
        """
        return jsii.get(self, "lifecyclePolicy")

    @lifecycle_policy.setter
    def lifecycle_policy(self, value: typing.Optional[typing.Union[typing.Optional["LifecyclePolicyProperty"], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "lifecyclePolicy", value)

    @property
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> typing.Optional[str]:
        """``AWS::ECR::Repository.RepositoryName``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-repositoryname
        Stability:
            stable
        """
        return jsii.get(self, "repositoryName")

    @repository_name.setter
    def repository_name(self, value: typing.Optional[str]):
        return jsii.set(self, "repositoryName", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-ecr.CfnRepository.LifecyclePolicyProperty", jsii_struct_bases=[])
    class LifecyclePolicyProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-lifecyclepolicy.html
        Stability:
            stable
        """
        lifecyclePolicyText: str
        """``CfnRepository.LifecyclePolicyProperty.LifecyclePolicyText``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-lifecyclepolicy.html#cfn-ecr-repository-lifecyclepolicy-lifecyclepolicytext
        Stability:
            stable
        """

        registryId: str
        """``CfnRepository.LifecyclePolicyProperty.RegistryId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecr-repository-lifecyclepolicy.html#cfn-ecr-repository-lifecyclepolicy-registryid
        Stability:
            stable
        """


@jsii.data_type(jsii_type="@aws-cdk/aws-ecr.CfnRepositoryProps", jsii_struct_bases=[])
class CfnRepositoryProps(jsii.compat.TypedDict, total=False):
    """Properties for defining a ``AWS::ECR::Repository``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html
    Stability:
        stable
    """
    lifecyclePolicy: typing.Union["CfnRepository.LifecyclePolicyProperty", aws_cdk.core.IResolvable]
    """``AWS::ECR::Repository.LifecyclePolicy``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-lifecyclepolicy
    Stability:
        stable
    """

    repositoryName: str
    """``AWS::ECR::Repository.RepositoryName``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-repositoryname
    Stability:
        stable
    """

    repositoryPolicyText: typing.Any
    """``AWS::ECR::Repository.RepositoryPolicyText``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-repositorypolicytext
    Stability:
        stable
    """

    tags: typing.List[aws_cdk.core.CfnTag]
    """``AWS::ECR::Repository.Tags``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecr-repository.html#cfn-ecr-repository-tags
    Stability:
        stable
    """

@jsii.interface(jsii_type="@aws-cdk/aws-ecr.IRepository")
class IRepository(aws_cdk.core.IResource, jsii.compat.Protocol):
    """Represents an ECR repository.

    Stability:
        experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IRepositoryProxy

    @property
    @jsii.member(jsii_name="repositoryArn")
    def repository_arn(self) -> str:
        """The ARN of the repository.

        Stability:
            experimental
        attribute:
            true
        """
        ...

    @property
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> str:
        """The name of the repository.

        Stability:
            experimental
        attribute:
            true
        """
        ...

    @property
    @jsii.member(jsii_name="repositoryUri")
    def repository_uri(self) -> str:
        """The URI of this repository (represents the latest image):.

        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY

        Stability:
            experimental
        attribute:
            true
        """
        ...

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(self, statement: aws_cdk.aws_iam.PolicyStatement) -> None:
        """Add a policy statement to the repository's resource policy.

        Arguments:
            statement: -

        Stability:
            experimental
        """
        ...

    @jsii.member(jsii_name="grant")
    def grant(self, grantee: aws_cdk.aws_iam.IGrantable, *actions: str) -> aws_cdk.aws_iam.Grant:
        """Grant the given principal identity permissions to perform the actions on this repository.

        Arguments:
            grantee: -
            actions: -

        Stability:
            experimental
        """
        ...

    @jsii.member(jsii_name="grantPull")
    def grant_pull(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant the given identity permissions to pull images in this repository.

        Arguments:
            grantee: -

        Stability:
            experimental
        """
        ...

    @jsii.member(jsii_name="grantPullPush")
    def grant_pull_push(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant the given identity permissions to pull and push images to this repository.

        Arguments:
            grantee: -

        Stability:
            experimental
        """
        ...

    @jsii.member(jsii_name="onCloudTrailEvent")
    def on_cloud_trail_event(self, id: str, *, description: typing.Optional[str]=None, event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern]=None, rule_name: typing.Optional[str]=None, target: typing.Optional[aws_cdk.aws_events.IRuleTarget]=None) -> aws_cdk.aws_events.Rule:
        """Define a CloudWatch event that triggers when something happens to this repository.

        Requires that there exists at least one CloudTrail Trail in your account
        that captures the event. This method will not create the Trail.

        Arguments:
            id: The id of the rule.
            options: Options for adding the rule.
            description: A description of the rule's purpose. Default: - No description
            event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
            rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
            target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.

        Stability:
            experimental
        """
        ...

    @jsii.member(jsii_name="onCloudTrailImagePushed")
    def on_cloud_trail_image_pushed(self, id: str, *, image_tag: typing.Optional[str]=None, description: typing.Optional[str]=None, event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern]=None, rule_name: typing.Optional[str]=None, target: typing.Optional[aws_cdk.aws_events.IRuleTarget]=None) -> aws_cdk.aws_events.Rule:
        """Defines an AWS CloudWatch event rule that can trigger a target when an image is pushed to this repository.

        Requires that there exists at least one CloudTrail Trail in your account
        that captures the event. This method will not create the Trail.

        Arguments:
            id: The id of the rule.
            options: Options for adding the rule.
            image_tag: Only watch changes to this image tag. Default: - Watch changes to all tags
            description: A description of the rule's purpose. Default: - No description
            event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
            rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
            target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.

        Stability:
            experimental
        """
        ...

    @jsii.member(jsii_name="repositoryUriForTag")
    def repository_uri_for_tag(self, tag: typing.Optional[str]=None) -> str:
        """Returns the URI of the repository for a certain tag. Can be used in ``docker push/pull``.

        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY[:TAG]

        Arguments:
            tag: Image tag to use (tools usually default to "latest" if omitted).

        Stability:
            experimental
        """
        ...


class _IRepositoryProxy(jsii.proxy_for(aws_cdk.core.IResource)):
    """Represents an ECR repository.

    Stability:
        experimental
    """
    __jsii_type__ = "@aws-cdk/aws-ecr.IRepository"
    @property
    @jsii.member(jsii_name="repositoryArn")
    def repository_arn(self) -> str:
        """The ARN of the repository.

        Stability:
            experimental
        attribute:
            true
        """
        return jsii.get(self, "repositoryArn")

    @property
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> str:
        """The name of the repository.

        Stability:
            experimental
        attribute:
            true
        """
        return jsii.get(self, "repositoryName")

    @property
    @jsii.member(jsii_name="repositoryUri")
    def repository_uri(self) -> str:
        """The URI of this repository (represents the latest image):.

        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY

        Stability:
            experimental
        attribute:
            true
        """
        return jsii.get(self, "repositoryUri")

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(self, statement: aws_cdk.aws_iam.PolicyStatement) -> None:
        """Add a policy statement to the repository's resource policy.

        Arguments:
            statement: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "addToResourcePolicy", [statement])

    @jsii.member(jsii_name="grant")
    def grant(self, grantee: aws_cdk.aws_iam.IGrantable, *actions: str) -> aws_cdk.aws_iam.Grant:
        """Grant the given principal identity permissions to perform the actions on this repository.

        Arguments:
            grantee: -
            actions: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "grant", [grantee, *actions])

    @jsii.member(jsii_name="grantPull")
    def grant_pull(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant the given identity permissions to pull images in this repository.

        Arguments:
            grantee: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "grantPull", [grantee])

    @jsii.member(jsii_name="grantPullPush")
    def grant_pull_push(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant the given identity permissions to pull and push images to this repository.

        Arguments:
            grantee: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "grantPullPush", [grantee])

    @jsii.member(jsii_name="onCloudTrailEvent")
    def on_cloud_trail_event(self, id: str, *, description: typing.Optional[str]=None, event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern]=None, rule_name: typing.Optional[str]=None, target: typing.Optional[aws_cdk.aws_events.IRuleTarget]=None) -> aws_cdk.aws_events.Rule:
        """Define a CloudWatch event that triggers when something happens to this repository.

        Requires that there exists at least one CloudTrail Trail in your account
        that captures the event. This method will not create the Trail.

        Arguments:
            id: The id of the rule.
            options: Options for adding the rule.
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

        return jsii.invoke(self, "onCloudTrailEvent", [id, options])

    @jsii.member(jsii_name="onCloudTrailImagePushed")
    def on_cloud_trail_image_pushed(self, id: str, *, image_tag: typing.Optional[str]=None, description: typing.Optional[str]=None, event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern]=None, rule_name: typing.Optional[str]=None, target: typing.Optional[aws_cdk.aws_events.IRuleTarget]=None) -> aws_cdk.aws_events.Rule:
        """Defines an AWS CloudWatch event rule that can trigger a target when an image is pushed to this repository.

        Requires that there exists at least one CloudTrail Trail in your account
        that captures the event. This method will not create the Trail.

        Arguments:
            id: The id of the rule.
            options: Options for adding the rule.
            image_tag: Only watch changes to this image tag. Default: - Watch changes to all tags
            description: A description of the rule's purpose. Default: - No description
            event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
            rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
            target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.

        Stability:
            experimental
        """
        options: OnCloudTrailImagePushedOptions = {}

        if image_tag is not None:
            options["imageTag"] = image_tag

        if description is not None:
            options["description"] = description

        if event_pattern is not None:
            options["eventPattern"] = event_pattern

        if rule_name is not None:
            options["ruleName"] = rule_name

        if target is not None:
            options["target"] = target

        return jsii.invoke(self, "onCloudTrailImagePushed", [id, options])

    @jsii.member(jsii_name="repositoryUriForTag")
    def repository_uri_for_tag(self, tag: typing.Optional[str]=None) -> str:
        """Returns the URI of the repository for a certain tag. Can be used in ``docker push/pull``.

        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY[:TAG]

        Arguments:
            tag: Image tag to use (tools usually default to "latest" if omitted).

        Stability:
            experimental
        """
        return jsii.invoke(self, "repositoryUriForTag", [tag])


@jsii.data_type(jsii_type="@aws-cdk/aws-ecr.LifecycleRule", jsii_struct_bases=[])
class LifecycleRule(jsii.compat.TypedDict, total=False):
    """An ECR life cycle rule.

    Stability:
        experimental
    """
    description: str
    """Describes the purpose of the rule.

    Default:
        No description

    Stability:
        experimental
    """

    maxImageAge: aws_cdk.core.Duration
    """The maximum age of images to retain. The value must represent a number of days.

    Specify exactly one of maxImageCount and maxImageAge.

    Stability:
        experimental
    """

    maxImageCount: jsii.Number
    """The maximum number of images to retain.

    Specify exactly one of maxImageCount and maxImageAgeDays.

    Stability:
        experimental
    """

    rulePriority: jsii.Number
    """Controls the order in which rules are evaluated (low to high).

    All rules must have a unique priority, where lower numbers have
    higher precedence. The first rule that matches is applied to an image.

    There can only be one rule with a tagStatus of Any, and it must have
    the highest rulePriority.

    All rules without a specified priority will have incrementing priorities
    automatically assigned to them, higher than any rules that DO have priorities.

    Default:
        Automatically assigned

    Stability:
        experimental
    """

    tagPrefixList: typing.List[str]
    """Select images that have ALL the given prefixes in their tag.

    Only if tagStatus == TagStatus.Tagged

    Stability:
        experimental
    """

    tagStatus: "TagStatus"
    """Select images based on tags.

    Only one rule is allowed to select untagged images, and it must
    have the highest rulePriority.

    Default:
        TagStatus.Tagged if tagPrefixList is given, TagStatus.Any otherwise

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-ecr.OnCloudTrailImagePushedOptions", jsii_struct_bases=[aws_cdk.aws_events.OnEventOptions])
class OnCloudTrailImagePushedOptions(aws_cdk.aws_events.OnEventOptions, jsii.compat.TypedDict, total=False):
    """Options for the onCloudTrailImagePushed method.

    Stability:
        experimental
    """
    imageTag: str
    """Only watch changes to this image tag.

    Default:
        - Watch changes to all tags

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-ecr.RepositoryAttributes", jsii_struct_bases=[])
class RepositoryAttributes(jsii.compat.TypedDict):
    """
    Stability:
        experimental
    """
    repositoryArn: str
    """
    Stability:
        experimental
    """

    repositoryName: str
    """
    Stability:
        experimental
    """

@jsii.implements(IRepository)
class RepositoryBase(aws_cdk.core.Resource, metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-ecr.RepositoryBase"):
    """Base class for ECR repository.

    Reused between imported repositories and owned repositories.

    Stability:
        experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _RepositoryBaseProxy

    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, physical_name: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time

        Stability:
            experimental
        """
        props: aws_cdk.core.ResourceProps = {}

        if physical_name is not None:
            props["physicalName"] = physical_name

        jsii.create(RepositoryBase, self, [scope, id, props])

    @jsii.member(jsii_name="addToResourcePolicy")
    @abc.abstractmethod
    def add_to_resource_policy(self, statement: aws_cdk.aws_iam.PolicyStatement) -> None:
        """Add a policy statement to the repository's resource policy.

        Arguments:
            statement: -

        Stability:
            experimental
        """
        ...

    @jsii.member(jsii_name="grant")
    def grant(self, grantee: aws_cdk.aws_iam.IGrantable, *actions: str) -> aws_cdk.aws_iam.Grant:
        """Grant the given principal identity permissions to perform the actions on this repository.

        Arguments:
            grantee: -
            actions: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "grant", [grantee, *actions])

    @jsii.member(jsii_name="grantPull")
    def grant_pull(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant the given identity permissions to use the images in this repository.

        Arguments:
            grantee: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "grantPull", [grantee])

    @jsii.member(jsii_name="grantPullPush")
    def grant_pull_push(self, grantee: aws_cdk.aws_iam.IGrantable) -> aws_cdk.aws_iam.Grant:
        """Grant the given identity permissions to pull and push images to this repository.

        Arguments:
            grantee: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "grantPullPush", [grantee])

    @jsii.member(jsii_name="onCloudTrailEvent")
    def on_cloud_trail_event(self, id: str, *, description: typing.Optional[str]=None, event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern]=None, rule_name: typing.Optional[str]=None, target: typing.Optional[aws_cdk.aws_events.IRuleTarget]=None) -> aws_cdk.aws_events.Rule:
        """Define a CloudWatch event that triggers when something happens to this repository.

        Requires that there exists at least one CloudTrail Trail in your account
        that captures the event. This method will not create the Trail.

        Arguments:
            id: The id of the rule.
            options: Options for adding the rule.
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

        return jsii.invoke(self, "onCloudTrailEvent", [id, options])

    @jsii.member(jsii_name="onCloudTrailImagePushed")
    def on_cloud_trail_image_pushed(self, id: str, *, image_tag: typing.Optional[str]=None, description: typing.Optional[str]=None, event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern]=None, rule_name: typing.Optional[str]=None, target: typing.Optional[aws_cdk.aws_events.IRuleTarget]=None) -> aws_cdk.aws_events.Rule:
        """Defines an AWS CloudWatch event rule that can trigger a target when an image is pushed to this repository.

        Requires that there exists at least one CloudTrail Trail in your account
        that captures the event. This method will not create the Trail.

        Arguments:
            id: The id of the rule.
            options: Options for adding the rule.
            image_tag: Only watch changes to this image tag. Default: - Watch changes to all tags
            description: A description of the rule's purpose. Default: - No description
            event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
            rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
            target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.

        Stability:
            experimental
        """
        options: OnCloudTrailImagePushedOptions = {}

        if image_tag is not None:
            options["imageTag"] = image_tag

        if description is not None:
            options["description"] = description

        if event_pattern is not None:
            options["eventPattern"] = event_pattern

        if rule_name is not None:
            options["ruleName"] = rule_name

        if target is not None:
            options["target"] = target

        return jsii.invoke(self, "onCloudTrailImagePushed", [id, options])

    @jsii.member(jsii_name="repositoryUriForTag")
    def repository_uri_for_tag(self, tag: typing.Optional[str]=None) -> str:
        """Returns the URL of the repository. Can be used in ``docker push/pull``.

        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY[:TAG]

        Arguments:
            tag: Optional image tag.

        Stability:
            experimental
        """
        return jsii.invoke(self, "repositoryUriForTag", [tag])

    @property
    @jsii.member(jsii_name="repositoryArn")
    @abc.abstractmethod
    def repository_arn(self) -> str:
        """The ARN of the repository.

        Stability:
            experimental
        """
        ...

    @property
    @jsii.member(jsii_name="repositoryName")
    @abc.abstractmethod
    def repository_name(self) -> str:
        """The name of the repository.

        Stability:
            experimental
        """
        ...

    @property
    @jsii.member(jsii_name="repositoryUri")
    def repository_uri(self) -> str:
        """The URI of this repository (represents the latest image):.

        ACCOUNT.dkr.ecr.REGION.amazonaws.com/REPOSITORY

        Stability:
            experimental
        """
        return jsii.get(self, "repositoryUri")


class _RepositoryBaseProxy(RepositoryBase, jsii.proxy_for(aws_cdk.core.Resource)):
    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(self, statement: aws_cdk.aws_iam.PolicyStatement) -> None:
        """Add a policy statement to the repository's resource policy.

        Arguments:
            statement: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "addToResourcePolicy", [statement])

    @property
    @jsii.member(jsii_name="repositoryArn")
    def repository_arn(self) -> str:
        """The ARN of the repository.

        Stability:
            experimental
        """
        return jsii.get(self, "repositoryArn")

    @property
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> str:
        """The name of the repository.

        Stability:
            experimental
        """
        return jsii.get(self, "repositoryName")


class Repository(RepositoryBase, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ecr.Repository"):
    """Define an ECR repository.

    Stability:
        experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, lifecycle_registry_id: typing.Optional[str]=None, lifecycle_rules: typing.Optional[typing.List["LifecycleRule"]]=None, removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy]=None, repository_name: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            lifecycle_registry_id: The AWS account ID associated with the registry that contains the repository. Default: The default registry is assumed.
            lifecycle_rules: Life cycle rules to apply to this registry. Default: No life cycle rules
            removal_policy: Determine what happens to the repository when the resource/stack is deleted. Default: RemovalPolicy.Retain
            repository_name: Name for this repository. Default: Automatically generated name.

        Stability:
            experimental
        """
        props: RepositoryProps = {}

        if lifecycle_registry_id is not None:
            props["lifecycleRegistryId"] = lifecycle_registry_id

        if lifecycle_rules is not None:
            props["lifecycleRules"] = lifecycle_rules

        if removal_policy is not None:
            props["removalPolicy"] = removal_policy

        if repository_name is not None:
            props["repositoryName"] = repository_name

        jsii.create(Repository, self, [scope, id, props])

    @jsii.member(jsii_name="arnForLocalRepository")
    @classmethod
    def arn_for_local_repository(cls, repository_name: str, scope: aws_cdk.core.IConstruct) -> str:
        """Returns an ECR ARN for a repository that resides in the same account/region as the current stack.

        Arguments:
            repository_name: -
            scope: -

        Stability:
            experimental
        """
        return jsii.sinvoke(cls, "arnForLocalRepository", [repository_name, scope])

    @jsii.member(jsii_name="fromRepositoryArn")
    @classmethod
    def from_repository_arn(cls, scope: aws_cdk.core.Construct, id: str, repository_arn: str) -> "IRepository":
        """
        Arguments:
            scope: -
            id: -
            repository_arn: -

        Stability:
            experimental
        """
        return jsii.sinvoke(cls, "fromRepositoryArn", [scope, id, repository_arn])

    @jsii.member(jsii_name="fromRepositoryAttributes")
    @classmethod
    def from_repository_attributes(cls, scope: aws_cdk.core.Construct, id: str, *, repository_arn: str, repository_name: str) -> "IRepository":
        """Import a repository.

        Arguments:
            scope: -
            id: -
            attrs: -
            repository_arn: 
            repository_name: 

        Stability:
            experimental
        """
        attrs: RepositoryAttributes = {"repositoryArn": repository_arn, "repositoryName": repository_name}

        return jsii.sinvoke(cls, "fromRepositoryAttributes", [scope, id, attrs])

    @jsii.member(jsii_name="fromRepositoryName")
    @classmethod
    def from_repository_name(cls, scope: aws_cdk.core.Construct, id: str, repository_name: str) -> "IRepository":
        """
        Arguments:
            scope: -
            id: -
            repository_name: -

        Stability:
            experimental
        """
        return jsii.sinvoke(cls, "fromRepositoryName", [scope, id, repository_name])

    @jsii.member(jsii_name="addLifecycleRule")
    def add_lifecycle_rule(self, *, description: typing.Optional[str]=None, max_image_age: typing.Optional[aws_cdk.core.Duration]=None, max_image_count: typing.Optional[jsii.Number]=None, rule_priority: typing.Optional[jsii.Number]=None, tag_prefix_list: typing.Optional[typing.List[str]]=None, tag_status: typing.Optional["TagStatus"]=None) -> None:
        """Add a life cycle rule to the repository.

        Life cycle rules automatically expire images from the repository that match
        certain conditions.

        Arguments:
            rule: -
            description: Describes the purpose of the rule. Default: No description
            max_image_age: The maximum age of images to retain. The value must represent a number of days. Specify exactly one of maxImageCount and maxImageAge.
            max_image_count: The maximum number of images to retain. Specify exactly one of maxImageCount and maxImageAgeDays.
            rule_priority: Controls the order in which rules are evaluated (low to high). All rules must have a unique priority, where lower numbers have higher precedence. The first rule that matches is applied to an image. There can only be one rule with a tagStatus of Any, and it must have the highest rulePriority. All rules without a specified priority will have incrementing priorities automatically assigned to them, higher than any rules that DO have priorities. Default: Automatically assigned
            tag_prefix_list: Select images that have ALL the given prefixes in their tag. Only if tagStatus == TagStatus.Tagged
            tag_status: Select images based on tags. Only one rule is allowed to select untagged images, and it must have the highest rulePriority. Default: TagStatus.Tagged if tagPrefixList is given, TagStatus.Any otherwise

        Stability:
            experimental
        """
        rule: LifecycleRule = {}

        if description is not None:
            rule["description"] = description

        if max_image_age is not None:
            rule["maxImageAge"] = max_image_age

        if max_image_count is not None:
            rule["maxImageCount"] = max_image_count

        if rule_priority is not None:
            rule["rulePriority"] = rule_priority

        if tag_prefix_list is not None:
            rule["tagPrefixList"] = tag_prefix_list

        if tag_status is not None:
            rule["tagStatus"] = tag_status

        return jsii.invoke(self, "addLifecycleRule", [rule])

    @jsii.member(jsii_name="addToResourcePolicy")
    def add_to_resource_policy(self, statement: aws_cdk.aws_iam.PolicyStatement) -> None:
        """Add a policy statement to the repository's resource policy.

        Arguments:
            statement: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "addToResourcePolicy", [statement])

    @property
    @jsii.member(jsii_name="repositoryArn")
    def repository_arn(self) -> str:
        """The ARN of the repository.

        Stability:
            experimental
        """
        return jsii.get(self, "repositoryArn")

    @property
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> str:
        """The name of the repository.

        Stability:
            experimental
        """
        return jsii.get(self, "repositoryName")


@jsii.data_type(jsii_type="@aws-cdk/aws-ecr.RepositoryProps", jsii_struct_bases=[])
class RepositoryProps(jsii.compat.TypedDict, total=False):
    """
    Stability:
        experimental
    """
    lifecycleRegistryId: str
    """The AWS account ID associated with the registry that contains the repository.

    Default:
        The default registry is assumed.

    See:
        https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutLifecyclePolicy.html
    Stability:
        experimental
    """

    lifecycleRules: typing.List["LifecycleRule"]
    """Life cycle rules to apply to this registry.

    Default:
        No life cycle rules

    Stability:
        experimental
    """

    removalPolicy: aws_cdk.core.RemovalPolicy
    """Determine what happens to the repository when the resource/stack is deleted.

    Default:
        RemovalPolicy.Retain

    Stability:
        experimental
    """

    repositoryName: str
    """Name for this repository.

    Default:
        Automatically generated name.

    Stability:
        experimental
    """

@jsii.enum(jsii_type="@aws-cdk/aws-ecr.TagStatus")
class TagStatus(enum.Enum):
    """Select images based on tags.

    Stability:
        experimental
    """
    ANY = "ANY"
    """Rule applies to all images.

    Stability:
        experimental
    """
    TAGGED = "TAGGED"
    """Rule applies to tagged images.

    Stability:
        experimental
    """
    UNTAGGED = "UNTAGGED"
    """Rule applies to untagged images.

    Stability:
        experimental
    """

__all__ = ["CfnRepository", "CfnRepositoryProps", "IRepository", "LifecycleRule", "OnCloudTrailImagePushedOptions", "Repository", "RepositoryAttributes", "RepositoryBase", "RepositoryProps", "TagStatus", "__jsii_assembly__"]

publication.publish()
