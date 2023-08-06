import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_cloudformation
import aws_cdk.aws_codebuild
import aws_cdk.aws_codecommit
import aws_cdk.aws_codedeploy
import aws_cdk.aws_codepipeline
import aws_cdk.aws_ec2
import aws_cdk.aws_ecr
import aws_cdk.aws_ecs
import aws_cdk.aws_events
import aws_cdk.aws_events_targets
import aws_cdk.aws_iam
import aws_cdk.aws_lambda
import aws_cdk.aws_s3
import aws_cdk.aws_sns
import aws_cdk.aws_sns_subscriptions
import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-codepipeline-actions", "0.36.0", __name__, "aws-codepipeline-actions@0.36.0.jsii.tgz")
@jsii.implements(aws_cdk.aws_codepipeline.IAction)
class Action(metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-codepipeline-actions.Action"):
    """Low-level class for generic CodePipeline Actions.

    Stability:
        experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _ActionProxy

    def __init__(self, *, action_name: str, artifact_bounds: aws_cdk.aws_codepipeline.ActionArtifactBounds, category: aws_cdk.aws_codepipeline.ActionCategory, provider: str, inputs: typing.Optional[typing.List[aws_cdk.aws_codepipeline.Artifact]]=None, outputs: typing.Optional[typing.List[aws_cdk.aws_codepipeline.Artifact]]=None, owner: typing.Optional[str]=None, region: typing.Optional[str]=None, resource: typing.Optional[aws_cdk.core.IResource]=None, role: typing.Optional[aws_cdk.aws_iam.IRole]=None, run_order: typing.Optional[jsii.Number]=None, version: typing.Optional[str]=None) -> None:
        """
        Arguments:
            action_properties: -
            action_name: 
            artifact_bounds: 
            category: The category of the action. The category defines which action type the owner (the entity that performs the action) performs.
            provider: The service provider that the action calls.
            inputs: 
            outputs: 
            owner: 
            region: The AWS region the given Action resides in. Note that a cross-region Pipeline requires replication buckets to function correctly. You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property. If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets, that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack. Default: the Action resides in the same region as the Pipeline
            resource: The optional resource that is backing this Action. This is used for automatically handling Actions backed by resources from a different account and/or region.
            role: 
            run_order: The order in which AWS CodePipeline runs this action. For more information, see the AWS CodePipeline User Guide. https://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements
            version: 

        Stability:
            experimental
        """
        action_properties: aws_cdk.aws_codepipeline.ActionProperties = {"actionName": action_name, "artifactBounds": artifact_bounds, "category": category, "provider": provider}

        if inputs is not None:
            action_properties["inputs"] = inputs

        if outputs is not None:
            action_properties["outputs"] = outputs

        if owner is not None:
            action_properties["owner"] = owner

        if region is not None:
            action_properties["region"] = region

        if resource is not None:
            action_properties["resource"] = resource

        if role is not None:
            action_properties["role"] = role

        if run_order is not None:
            action_properties["runOrder"] = run_order

        if version is not None:
            action_properties["version"] = version

        jsii.create(Action, self, [action_properties])

    @jsii.member(jsii_name="bind")
    def bind(self, scope: aws_cdk.core.Construct, stage: aws_cdk.aws_codepipeline.IStage, *, role: aws_cdk.aws_iam.IRole) -> aws_cdk.aws_codepipeline.ActionConfig:
        """
        Arguments:
            scope: -
            stage: -
            options: -
            role: 

        Stability:
            experimental
        """
        options: aws_cdk.aws_codepipeline.ActionBindOptions = {"role": role}

        return jsii.invoke(self, "bind", [scope, stage, options])

    @jsii.member(jsii_name="bound")
    @abc.abstractmethod
    def _bound(self, scope: aws_cdk.core.Construct, stage: aws_cdk.aws_codepipeline.IStage, *, role: aws_cdk.aws_iam.IRole) -> aws_cdk.aws_codepipeline.ActionConfig:
        """The method called when an Action is attached to a Pipeline. This method is guaranteed to be called only once for each Action instance.

        Arguments:
            scope: -
            stage: -
            options: an instance of the {@link ActionBindOptions} class, that contains the necessary information for the Action to configure itself, like a reference to the Role, etc.
            role: 

        Stability:
            experimental
        """
        ...

    @jsii.member(jsii_name="onStateChange")
    def on_state_change(self, name: str, target: typing.Optional[aws_cdk.aws_events.IRuleTarget]=None, *, description: typing.Optional[str]=None, enabled: typing.Optional[bool]=None, event_pattern: typing.Optional[aws_cdk.aws_events.EventPattern]=None, rule_name: typing.Optional[str]=None, schedule: typing.Optional[aws_cdk.aws_events.Schedule]=None, targets: typing.Optional[typing.List[aws_cdk.aws_events.IRuleTarget]]=None) -> aws_cdk.aws_events.Rule:
        """
        Arguments:
            name: -
            target: -
            options: -
            description: A description of the rule's purpose. Default: - No description.
            enabled: Indicates whether the rule is enabled. Default: true
            event_pattern: Describes which events CloudWatch Events routes to the specified target. These routed events are matched events. For more information, see Events and Event Patterns in the Amazon CloudWatch User Guide. Default: - None.
            rule_name: A name for the rule. Default: - AWS CloudFormation generates a unique physical ID and uses that ID for the rule name. For more information, see Name Type.
            schedule: The schedule or rate (frequency) that determines when CloudWatch Events runs the rule. For more information, see Schedule Expression Syntax for Rules in the Amazon CloudWatch User Guide. Default: - None.
            targets: Targets to invoke when this rule matches an event. Input will be the full matched event. If you wish to specify custom target input, use ``addTarget(target[, inputOptions])``. Default: - No targets.

        Stability:
            experimental
        """
        options: aws_cdk.aws_events.RuleProps = {}

        if description is not None:
            options["description"] = description

        if enabled is not None:
            options["enabled"] = enabled

        if event_pattern is not None:
            options["eventPattern"] = event_pattern

        if rule_name is not None:
            options["ruleName"] = rule_name

        if schedule is not None:
            options["schedule"] = schedule

        if targets is not None:
            options["targets"] = targets

        return jsii.invoke(self, "onStateChange", [name, target, options])

    @property
    @jsii.member(jsii_name="actionProperties")
    def action_properties(self) -> aws_cdk.aws_codepipeline.ActionProperties:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "actionProperties")


class _ActionProxy(Action):
    @jsii.member(jsii_name="bound")
    def _bound(self, scope: aws_cdk.core.Construct, stage: aws_cdk.aws_codepipeline.IStage, *, role: aws_cdk.aws_iam.IRole) -> aws_cdk.aws_codepipeline.ActionConfig:
        """The method called when an Action is attached to a Pipeline. This method is guaranteed to be called only once for each Action instance.

        Arguments:
            scope: -
            stage: -
            options: an instance of the {@link ActionBindOptions} class, that contains the necessary information for the Action to configure itself, like a reference to the Role, etc.
            role: 

        Stability:
            experimental
        """
        options: aws_cdk.aws_codepipeline.ActionBindOptions = {"role": role}

        return jsii.invoke(self, "bound", [scope, stage, options])


class AlexaSkillDeployAction(Action, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codepipeline-actions.AlexaSkillDeployAction"):
    """Deploys the skill to Alexa.

    Stability:
        experimental
    """
    def __init__(self, *, client_id: str, client_secret: aws_cdk.core.SecretValue, input: aws_cdk.aws_codepipeline.Artifact, refresh_token: aws_cdk.core.SecretValue, skill_id: str, parameter_overrides_artifact: typing.Optional[aws_cdk.aws_codepipeline.Artifact]=None, action_name: str, run_order: typing.Optional[jsii.Number]=None) -> None:
        """
        Arguments:
            props: -
            client_id: The client id of the developer console token.
            client_secret: The client secret of the developer console token.
            input: The source artifact containing the voice model and skill manifest.
            refresh_token: The refresh token of the developer console token.
            skill_id: The Alexa skill id.
            parameter_overrides_artifact: An optional artifact containing overrides for the skill manifest.
            action_name: The physical, human-readable name of the Action. Not that Action names must be unique within a single Stage.
            run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1

        Stability:
            experimental
        """
        props: AlexaSkillDeployActionProps = {"clientId": client_id, "clientSecret": client_secret, "input": input, "refreshToken": refresh_token, "skillId": skill_id, "actionName": action_name}

        if parameter_overrides_artifact is not None:
            props["parameterOverridesArtifact"] = parameter_overrides_artifact

        if run_order is not None:
            props["runOrder"] = run_order

        jsii.create(AlexaSkillDeployAction, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(self, _scope: aws_cdk.core.Construct, _stage: aws_cdk.aws_codepipeline.IStage, *, role: aws_cdk.aws_iam.IRole) -> aws_cdk.aws_codepipeline.ActionConfig:
        """The method called when an Action is attached to a Pipeline. This method is guaranteed to be called only once for each Action instance.

        Arguments:
            _scope: -
            _stage: -
            _options: -
            role: 

        Stability:
            experimental
        """
        _options: aws_cdk.aws_codepipeline.ActionBindOptions = {"role": role}

        return jsii.invoke(self, "bound", [_scope, _stage, _options])


@jsii.data_type_optionals(jsii_struct_bases=[aws_cdk.aws_codepipeline.CommonActionProps])
class _AlexaSkillDeployActionProps(aws_cdk.aws_codepipeline.CommonActionProps, jsii.compat.TypedDict, total=False):
    parameterOverridesArtifact: aws_cdk.aws_codepipeline.Artifact
    """An optional artifact containing overrides for the skill manifest.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codepipeline-actions.AlexaSkillDeployActionProps", jsii_struct_bases=[_AlexaSkillDeployActionProps])
class AlexaSkillDeployActionProps(_AlexaSkillDeployActionProps):
    """Construction properties of the {@link AlexaSkillDeployAction Alexa deploy Action}.

    Stability:
        experimental
    """
    clientId: str
    """The client id of the developer console token.

    Stability:
        experimental
    """

    clientSecret: aws_cdk.core.SecretValue
    """The client secret of the developer console token.

    Stability:
        experimental
    """

    input: aws_cdk.aws_codepipeline.Artifact
    """The source artifact containing the voice model and skill manifest.

    Stability:
        experimental
    """

    refreshToken: aws_cdk.core.SecretValue
    """The refresh token of the developer console token.

    Stability:
        experimental
    """

    skillId: str
    """The Alexa skill id.

    Stability:
        experimental
    """

class CloudFormationCreateReplaceChangeSetAction(Action, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codepipeline-actions.CloudFormationCreateReplaceChangeSetAction"):
    """CodePipeline action to prepare a change set.

    Creates the change set if it doesn't exist based on the stack name and template that you submit.
    If the change set exists, AWS CloudFormation deletes it, and then creates a new one.

    Stability:
        experimental
    """
    def __init__(self, *, admin_permissions: bool, change_set_name: str, stack_name: str, template_path: aws_cdk.aws_codepipeline.ArtifactPath, capabilities: typing.Optional[typing.List[aws_cdk.aws_cloudformation.CloudFormationCapabilities]]=None, deployment_role: typing.Optional[aws_cdk.aws_iam.IRole]=None, extra_inputs: typing.Optional[typing.List[aws_cdk.aws_codepipeline.Artifact]]=None, output: typing.Optional[aws_cdk.aws_codepipeline.Artifact]=None, output_file_name: typing.Optional[str]=None, parameter_overrides: typing.Optional[typing.Mapping[str,typing.Any]]=None, region: typing.Optional[str]=None, role: typing.Optional[aws_cdk.aws_iam.IRole]=None, template_configuration: typing.Optional[aws_cdk.aws_codepipeline.ArtifactPath]=None, action_name: str, run_order: typing.Optional[jsii.Number]=None) -> None:
        """
        Arguments:
            props: -
            admin_permissions: Whether to grant full permissions to CloudFormation while deploying this template. Setting this to ``true`` affects the defaults for ``role`` and ``capabilities``, if you don't specify any alternatives. The default role that will be created for you will have full (i.e., ``*``) permissions on all resources, and the deployment will have named IAM capabilities (i.e., able to create all IAM resources). This is a shorthand that you can use if you fully trust the templates that are deployed in this pipeline. If you want more fine-grained permissions, use ``addToRolePolicy`` and ``capabilities`` to control what the CloudFormation deployment is allowed to do.
            change_set_name: Name of the change set to create or update.
            stack_name: The name of the stack to apply this action to.
            template_path: Input artifact with the ChangeSet's CloudFormation template.
            capabilities: Acknowledge certain changes made as part of deployment. For stacks that contain certain resources, explicit acknowledgement that AWS CloudFormation might create or update those resources. For example, you must specify ``AnonymousIAM`` or ``NamedIAM`` if your stack template contains AWS Identity and Access Management (IAM) resources. For more information see the link below. Default: None, unless ``adminPermissions`` is true
            deployment_role: IAM role to assume when deploying changes. If not specified, a fresh role is created. The role is created with zero permissions unless ``adminPermissions`` is true, in which case the role will have full permissions. Default: A fresh role with full or no permissions (depending on the value of ``adminPermissions``).
            extra_inputs: The list of additional input Artifacts for this Action. This is especially useful when used in conjunction with the ``parameterOverrides`` property. For example, if you have:. parameterOverrides: { 'Param1': action1.outputArtifact.bucketName, 'Param2': action2.outputArtifact.objectKey, } , if the output Artifacts of ``action1`` and ``action2`` were not used to set either the ``templateConfiguration`` or the ``templatePath`` properties, you need to make sure to include them in the ``extraInputs`` - otherwise, you'll get an "unrecognized Artifact" error during your Pipeline's execution.
            output: The name of the output artifact to generate. Only applied if ``outputFileName`` is set as well. Default: Automatically generated artifact name.
            output_file_name: A name for the filename in the output artifact to store the AWS CloudFormation call's result. The file will contain the result of the call to AWS CloudFormation (for example the call to UpdateStack or CreateChangeSet). AWS CodePipeline adds the file to the output artifact after performing the specified action. Default: No output artifact generated
            parameter_overrides: Additional template parameters. Template parameters specified here take precedence over template parameters found in the artifact specified by the ``templateConfiguration`` property. We recommend that you use the template configuration file to specify most of your parameter values. Use parameter overrides to specify only dynamic parameter values (values that are unknown until you run the pipeline). All parameter names must be present in the stack template. Note: the entire object cannot be more than 1kB. Default: No overrides
            region: The AWS region the given Action resides in. Note that a cross-region Pipeline requires replication buckets to function correctly. You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property. If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets, that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack. Default: the Action resides in the same region as the Pipeline
            role: The service role that is assumed during execution of action. This role is not mandatory, however more advanced configuration may require specifying it.
            template_configuration: Input artifact to use for template parameters values and stack policy. The template configuration file should contain a JSON object that should look like this: ``{ "Parameters": {...}, "Tags": {...}, "StackPolicy": {... }}``. For more information, see `AWS CloudFormation Artifacts <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html>`_. Note that if you include sensitive information, such as passwords, restrict access to this file. Default: No template configuration based on input artifacts
            action_name: The physical, human-readable name of the Action. Not that Action names must be unique within a single Stage.
            run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1

        Stability:
            experimental
        """
        props: CloudFormationCreateReplaceChangeSetActionProps = {"adminPermissions": admin_permissions, "changeSetName": change_set_name, "stackName": stack_name, "templatePath": template_path, "actionName": action_name}

        if capabilities is not None:
            props["capabilities"] = capabilities

        if deployment_role is not None:
            props["deploymentRole"] = deployment_role

        if extra_inputs is not None:
            props["extraInputs"] = extra_inputs

        if output is not None:
            props["output"] = output

        if output_file_name is not None:
            props["outputFileName"] = output_file_name

        if parameter_overrides is not None:
            props["parameterOverrides"] = parameter_overrides

        if region is not None:
            props["region"] = region

        if role is not None:
            props["role"] = role

        if template_configuration is not None:
            props["templateConfiguration"] = template_configuration

        if run_order is not None:
            props["runOrder"] = run_order

        jsii.create(CloudFormationCreateReplaceChangeSetAction, self, [props])

    @jsii.member(jsii_name="addToDeploymentRolePolicy")
    def add_to_deployment_role_policy(self, statement: aws_cdk.aws_iam.PolicyStatement) -> bool:
        """Add statement to the service role assumed by CloudFormation while executing this action.

        Arguments:
            statement: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "addToDeploymentRolePolicy", [statement])

    @jsii.member(jsii_name="bound")
    def _bound(self, scope: aws_cdk.core.Construct, stage: aws_cdk.aws_codepipeline.IStage, *, role: aws_cdk.aws_iam.IRole) -> aws_cdk.aws_codepipeline.ActionConfig:
        """The method called when an Action is attached to a Pipeline. This method is guaranteed to be called only once for each Action instance.

        Arguments:
            scope: -
            stage: -
            options: -
            role: 

        Stability:
            experimental
        """
        options: aws_cdk.aws_codepipeline.ActionBindOptions = {"role": role}

        return jsii.invoke(self, "bound", [scope, stage, options])

    @property
    @jsii.member(jsii_name="deploymentRole")
    def deployment_role(self) -> aws_cdk.aws_iam.IRole:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "deploymentRole")


@jsii.data_type_optionals(jsii_struct_bases=[aws_cdk.aws_codepipeline.CommonActionProps])
class _CloudFormationCreateReplaceChangeSetActionProps(aws_cdk.aws_codepipeline.CommonActionProps, jsii.compat.TypedDict, total=False):
    capabilities: typing.List[aws_cdk.aws_cloudformation.CloudFormationCapabilities]
    """Acknowledge certain changes made as part of deployment.

    For stacks that contain certain resources, explicit acknowledgement that AWS CloudFormation
    might create or update those resources. For example, you must specify ``AnonymousIAM`` or ``NamedIAM``
    if your stack template contains AWS Identity and Access Management (IAM) resources. For more
    information see the link below.

    Default:
        None, unless ``adminPermissions`` is true

    See:
        https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities
    Stability:
        experimental
    """
    deploymentRole: aws_cdk.aws_iam.IRole
    """IAM role to assume when deploying changes.

    If not specified, a fresh role is created. The role is created with zero
    permissions unless ``adminPermissions`` is true, in which case the role will have
    full permissions.

    Default:
        A fresh role with full or no permissions (depending on the value of ``adminPermissions``).

    Stability:
        experimental
    """
    extraInputs: typing.List[aws_cdk.aws_codepipeline.Artifact]
    """The list of additional input Artifacts for this Action. This is especially useful when used in conjunction with the ``parameterOverrides`` property. For example, if you have:.

    parameterOverrides: {
    'Param1': action1.outputArtifact.bucketName,
    'Param2': action2.outputArtifact.objectKey,
    }

    , if the output Artifacts of ``action1`` and ``action2`` were not used to
    set either the ``templateConfiguration`` or the ``templatePath`` properties,
    you need to make sure to include them in the ``extraInputs`` -
    otherwise, you'll get an "unrecognized Artifact" error during your Pipeline's execution.

    Stability:
        experimental
    """
    output: aws_cdk.aws_codepipeline.Artifact
    """The name of the output artifact to generate.

    Only applied if ``outputFileName`` is set as well.

    Default:
        Automatically generated artifact name.

    Stability:
        experimental
    """
    outputFileName: str
    """A name for the filename in the output artifact to store the AWS CloudFormation call's result.

    The file will contain the result of the call to AWS CloudFormation (for example
    the call to UpdateStack or CreateChangeSet).

    AWS CodePipeline adds the file to the output artifact after performing
    the specified action.

    Default:
        No output artifact generated

    Stability:
        experimental
    """
    parameterOverrides: typing.Mapping[str,typing.Any]
    """Additional template parameters.

    Template parameters specified here take precedence over template parameters
    found in the artifact specified by the ``templateConfiguration`` property.

    We recommend that you use the template configuration file to specify
    most of your parameter values. Use parameter overrides to specify only
    dynamic parameter values (values that are unknown until you run the
    pipeline).

    All parameter names must be present in the stack template.

    Note: the entire object cannot be more than 1kB.

    Default:
        No overrides

    Stability:
        experimental
    """
    region: str
    """The AWS region the given Action resides in. Note that a cross-region Pipeline requires replication buckets to function correctly. You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property. If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets, that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack.

    Default:
        the Action resides in the same region as the Pipeline

    Stability:
        experimental
    """
    role: aws_cdk.aws_iam.IRole
    """The service role that is assumed during execution of action. This role is not mandatory, however more advanced configuration may require specifying it.

    See:
        https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions.html
    Stability:
        experimental
    """
    templateConfiguration: aws_cdk.aws_codepipeline.ArtifactPath
    """Input artifact to use for template parameters values and stack policy.

    The template configuration file should contain a JSON object that should look like this:
    ``{ "Parameters": {...}, "Tags": {...}, "StackPolicy": {... }}``. For more information,
    see `AWS CloudFormation Artifacts <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html>`_.

    Note that if you include sensitive information, such as passwords, restrict access to this
    file.

    Default:
        No template configuration based on input artifacts

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codepipeline-actions.CloudFormationCreateReplaceChangeSetActionProps", jsii_struct_bases=[_CloudFormationCreateReplaceChangeSetActionProps])
class CloudFormationCreateReplaceChangeSetActionProps(_CloudFormationCreateReplaceChangeSetActionProps):
    """Properties for the CloudFormationCreateReplaceChangeSetAction.

    Stability:
        experimental
    """
    adminPermissions: bool
    """Whether to grant full permissions to CloudFormation while deploying this template.

    Setting this to ``true`` affects the defaults for ``role`` and ``capabilities``, if you
    don't specify any alternatives.

    The default role that will be created for you will have full (i.e., ``*``)
    permissions on all resources, and the deployment will have named IAM
    capabilities (i.e., able to create all IAM resources).

    This is a shorthand that you can use if you fully trust the templates that
    are deployed in this pipeline. If you want more fine-grained permissions,
    use ``addToRolePolicy`` and ``capabilities`` to control what the CloudFormation
    deployment is allowed to do.

    Stability:
        experimental
    """

    changeSetName: str
    """Name of the change set to create or update.

    Stability:
        experimental
    """

    stackName: str
    """The name of the stack to apply this action to.

    Stability:
        experimental
    """

    templatePath: aws_cdk.aws_codepipeline.ArtifactPath
    """Input artifact with the ChangeSet's CloudFormation template.

    Stability:
        experimental
    """

class CloudFormationCreateUpdateStackAction(Action, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codepipeline-actions.CloudFormationCreateUpdateStackAction"):
    """CodePipeline action to deploy a stack.

    Creates the stack if the specified stack doesn't exist. If the stack exists,
    AWS CloudFormation updates the stack. Use this action to update existing
    stacks.

    AWS CodePipeline won't replace the stack, and will fail deployment if the
    stack is in a failed state. Use ``ReplaceOnFailure`` for an action that
    will delete and recreate the stack to try and recover from failed states.

    Use this action to automatically replace failed stacks without recovering or
    troubleshooting them. You would typically choose this mode for testing.

    Stability:
        experimental
    """
    def __init__(self, *, admin_permissions: bool, stack_name: str, template_path: aws_cdk.aws_codepipeline.ArtifactPath, capabilities: typing.Optional[typing.List[aws_cdk.aws_cloudformation.CloudFormationCapabilities]]=None, deployment_role: typing.Optional[aws_cdk.aws_iam.IRole]=None, extra_inputs: typing.Optional[typing.List[aws_cdk.aws_codepipeline.Artifact]]=None, output: typing.Optional[aws_cdk.aws_codepipeline.Artifact]=None, output_file_name: typing.Optional[str]=None, parameter_overrides: typing.Optional[typing.Mapping[str,typing.Any]]=None, region: typing.Optional[str]=None, replace_on_failure: typing.Optional[bool]=None, role: typing.Optional[aws_cdk.aws_iam.IRole]=None, template_configuration: typing.Optional[aws_cdk.aws_codepipeline.ArtifactPath]=None, action_name: str, run_order: typing.Optional[jsii.Number]=None) -> None:
        """
        Arguments:
            props: -
            admin_permissions: Whether to grant full permissions to CloudFormation while deploying this template. Setting this to ``true`` affects the defaults for ``role`` and ``capabilities``, if you don't specify any alternatives. The default role that will be created for you will have full (i.e., ``*``) permissions on all resources, and the deployment will have named IAM capabilities (i.e., able to create all IAM resources). This is a shorthand that you can use if you fully trust the templates that are deployed in this pipeline. If you want more fine-grained permissions, use ``addToRolePolicy`` and ``capabilities`` to control what the CloudFormation deployment is allowed to do.
            stack_name: The name of the stack to apply this action to.
            template_path: Input artifact with the CloudFormation template to deploy.
            capabilities: Acknowledge certain changes made as part of deployment. For stacks that contain certain resources, explicit acknowledgement that AWS CloudFormation might create or update those resources. For example, you must specify ``AnonymousIAM`` or ``NamedIAM`` if your stack template contains AWS Identity and Access Management (IAM) resources. For more information see the link below. Default: None, unless ``adminPermissions`` is true
            deployment_role: IAM role to assume when deploying changes. If not specified, a fresh role is created. The role is created with zero permissions unless ``adminPermissions`` is true, in which case the role will have full permissions. Default: A fresh role with full or no permissions (depending on the value of ``adminPermissions``).
            extra_inputs: The list of additional input Artifacts for this Action. This is especially useful when used in conjunction with the ``parameterOverrides`` property. For example, if you have:. parameterOverrides: { 'Param1': action1.outputArtifact.bucketName, 'Param2': action2.outputArtifact.objectKey, } , if the output Artifacts of ``action1`` and ``action2`` were not used to set either the ``templateConfiguration`` or the ``templatePath`` properties, you need to make sure to include them in the ``extraInputs`` - otherwise, you'll get an "unrecognized Artifact" error during your Pipeline's execution.
            output: The name of the output artifact to generate. Only applied if ``outputFileName`` is set as well. Default: Automatically generated artifact name.
            output_file_name: A name for the filename in the output artifact to store the AWS CloudFormation call's result. The file will contain the result of the call to AWS CloudFormation (for example the call to UpdateStack or CreateChangeSet). AWS CodePipeline adds the file to the output artifact after performing the specified action. Default: No output artifact generated
            parameter_overrides: Additional template parameters. Template parameters specified here take precedence over template parameters found in the artifact specified by the ``templateConfiguration`` property. We recommend that you use the template configuration file to specify most of your parameter values. Use parameter overrides to specify only dynamic parameter values (values that are unknown until you run the pipeline). All parameter names must be present in the stack template. Note: the entire object cannot be more than 1kB. Default: No overrides
            region: The AWS region the given Action resides in. Note that a cross-region Pipeline requires replication buckets to function correctly. You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property. If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets, that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack. Default: the Action resides in the same region as the Pipeline
            replace_on_failure: Replace the stack if it's in a failed state. If this is set to true and the stack is in a failed state (one of ROLLBACK_COMPLETE, ROLLBACK_FAILED, CREATE_FAILED, DELETE_FAILED, or UPDATE_ROLLBACK_FAILED), AWS CloudFormation deletes the stack and then creates a new stack. If this is not set to true and the stack is in a failed state, the deployment fails. Default: false
            role: The service role that is assumed during execution of action. This role is not mandatory, however more advanced configuration may require specifying it.
            template_configuration: Input artifact to use for template parameters values and stack policy. The template configuration file should contain a JSON object that should look like this: ``{ "Parameters": {...}, "Tags": {...}, "StackPolicy": {... }}``. For more information, see `AWS CloudFormation Artifacts <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html>`_. Note that if you include sensitive information, such as passwords, restrict access to this file. Default: No template configuration based on input artifacts
            action_name: The physical, human-readable name of the Action. Not that Action names must be unique within a single Stage.
            run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1

        Stability:
            experimental
        """
        props: CloudFormationCreateUpdateStackActionProps = {"adminPermissions": admin_permissions, "stackName": stack_name, "templatePath": template_path, "actionName": action_name}

        if capabilities is not None:
            props["capabilities"] = capabilities

        if deployment_role is not None:
            props["deploymentRole"] = deployment_role

        if extra_inputs is not None:
            props["extraInputs"] = extra_inputs

        if output is not None:
            props["output"] = output

        if output_file_name is not None:
            props["outputFileName"] = output_file_name

        if parameter_overrides is not None:
            props["parameterOverrides"] = parameter_overrides

        if region is not None:
            props["region"] = region

        if replace_on_failure is not None:
            props["replaceOnFailure"] = replace_on_failure

        if role is not None:
            props["role"] = role

        if template_configuration is not None:
            props["templateConfiguration"] = template_configuration

        if run_order is not None:
            props["runOrder"] = run_order

        jsii.create(CloudFormationCreateUpdateStackAction, self, [props])

    @jsii.member(jsii_name="addToDeploymentRolePolicy")
    def add_to_deployment_role_policy(self, statement: aws_cdk.aws_iam.PolicyStatement) -> bool:
        """Add statement to the service role assumed by CloudFormation while executing this action.

        Arguments:
            statement: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "addToDeploymentRolePolicy", [statement])

    @jsii.member(jsii_name="bound")
    def _bound(self, scope: aws_cdk.core.Construct, stage: aws_cdk.aws_codepipeline.IStage, *, role: aws_cdk.aws_iam.IRole) -> aws_cdk.aws_codepipeline.ActionConfig:
        """The method called when an Action is attached to a Pipeline. This method is guaranteed to be called only once for each Action instance.

        Arguments:
            scope: -
            stage: -
            options: -
            role: 

        Stability:
            experimental
        """
        options: aws_cdk.aws_codepipeline.ActionBindOptions = {"role": role}

        return jsii.invoke(self, "bound", [scope, stage, options])

    @property
    @jsii.member(jsii_name="deploymentRole")
    def deployment_role(self) -> aws_cdk.aws_iam.IRole:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "deploymentRole")


@jsii.data_type_optionals(jsii_struct_bases=[aws_cdk.aws_codepipeline.CommonActionProps])
class _CloudFormationCreateUpdateStackActionProps(aws_cdk.aws_codepipeline.CommonActionProps, jsii.compat.TypedDict, total=False):
    capabilities: typing.List[aws_cdk.aws_cloudformation.CloudFormationCapabilities]
    """Acknowledge certain changes made as part of deployment.

    For stacks that contain certain resources, explicit acknowledgement that AWS CloudFormation
    might create or update those resources. For example, you must specify ``AnonymousIAM`` or ``NamedIAM``
    if your stack template contains AWS Identity and Access Management (IAM) resources. For more
    information see the link below.

    Default:
        None, unless ``adminPermissions`` is true

    See:
        https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities
    Stability:
        experimental
    """
    deploymentRole: aws_cdk.aws_iam.IRole
    """IAM role to assume when deploying changes.

    If not specified, a fresh role is created. The role is created with zero
    permissions unless ``adminPermissions`` is true, in which case the role will have
    full permissions.

    Default:
        A fresh role with full or no permissions (depending on the value of ``adminPermissions``).

    Stability:
        experimental
    """
    extraInputs: typing.List[aws_cdk.aws_codepipeline.Artifact]
    """The list of additional input Artifacts for this Action. This is especially useful when used in conjunction with the ``parameterOverrides`` property. For example, if you have:.

    parameterOverrides: {
    'Param1': action1.outputArtifact.bucketName,
    'Param2': action2.outputArtifact.objectKey,
    }

    , if the output Artifacts of ``action1`` and ``action2`` were not used to
    set either the ``templateConfiguration`` or the ``templatePath`` properties,
    you need to make sure to include them in the ``extraInputs`` -
    otherwise, you'll get an "unrecognized Artifact" error during your Pipeline's execution.

    Stability:
        experimental
    """
    output: aws_cdk.aws_codepipeline.Artifact
    """The name of the output artifact to generate.

    Only applied if ``outputFileName`` is set as well.

    Default:
        Automatically generated artifact name.

    Stability:
        experimental
    """
    outputFileName: str
    """A name for the filename in the output artifact to store the AWS CloudFormation call's result.

    The file will contain the result of the call to AWS CloudFormation (for example
    the call to UpdateStack or CreateChangeSet).

    AWS CodePipeline adds the file to the output artifact after performing
    the specified action.

    Default:
        No output artifact generated

    Stability:
        experimental
    """
    parameterOverrides: typing.Mapping[str,typing.Any]
    """Additional template parameters.

    Template parameters specified here take precedence over template parameters
    found in the artifact specified by the ``templateConfiguration`` property.

    We recommend that you use the template configuration file to specify
    most of your parameter values. Use parameter overrides to specify only
    dynamic parameter values (values that are unknown until you run the
    pipeline).

    All parameter names must be present in the stack template.

    Note: the entire object cannot be more than 1kB.

    Default:
        No overrides

    Stability:
        experimental
    """
    region: str
    """The AWS region the given Action resides in. Note that a cross-region Pipeline requires replication buckets to function correctly. You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property. If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets, that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack.

    Default:
        the Action resides in the same region as the Pipeline

    Stability:
        experimental
    """
    replaceOnFailure: bool
    """Replace the stack if it's in a failed state.

    If this is set to true and the stack is in a failed state (one of
    ROLLBACK_COMPLETE, ROLLBACK_FAILED, CREATE_FAILED, DELETE_FAILED, or
    UPDATE_ROLLBACK_FAILED), AWS CloudFormation deletes the stack and then
    creates a new stack.

    If this is not set to true and the stack is in a failed state,
    the deployment fails.

    Default:
        false

    Stability:
        experimental
    """
    role: aws_cdk.aws_iam.IRole
    """The service role that is assumed during execution of action. This role is not mandatory, however more advanced configuration may require specifying it.

    See:
        https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions.html
    Stability:
        experimental
    """
    templateConfiguration: aws_cdk.aws_codepipeline.ArtifactPath
    """Input artifact to use for template parameters values and stack policy.

    The template configuration file should contain a JSON object that should look like this:
    ``{ "Parameters": {...}, "Tags": {...}, "StackPolicy": {... }}``. For more information,
    see `AWS CloudFormation Artifacts <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html>`_.

    Note that if you include sensitive information, such as passwords, restrict access to this
    file.

    Default:
        No template configuration based on input artifacts

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codepipeline-actions.CloudFormationCreateUpdateStackActionProps", jsii_struct_bases=[_CloudFormationCreateUpdateStackActionProps])
class CloudFormationCreateUpdateStackActionProps(_CloudFormationCreateUpdateStackActionProps):
    """Properties for the CloudFormationCreateUpdateStackAction.

    Stability:
        experimental
    """
    adminPermissions: bool
    """Whether to grant full permissions to CloudFormation while deploying this template.

    Setting this to ``true`` affects the defaults for ``role`` and ``capabilities``, if you
    don't specify any alternatives.

    The default role that will be created for you will have full (i.e., ``*``)
    permissions on all resources, and the deployment will have named IAM
    capabilities (i.e., able to create all IAM resources).

    This is a shorthand that you can use if you fully trust the templates that
    are deployed in this pipeline. If you want more fine-grained permissions,
    use ``addToRolePolicy`` and ``capabilities`` to control what the CloudFormation
    deployment is allowed to do.

    Stability:
        experimental
    """

    stackName: str
    """The name of the stack to apply this action to.

    Stability:
        experimental
    """

    templatePath: aws_cdk.aws_codepipeline.ArtifactPath
    """Input artifact with the CloudFormation template to deploy.

    Stability:
        experimental
    """

class CloudFormationDeleteStackAction(Action, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codepipeline-actions.CloudFormationDeleteStackAction"):
    """CodePipeline action to delete a stack.

    Deletes a stack. If you specify a stack that doesn't exist, the action completes successfully
    without deleting a stack.

    Stability:
        experimental
    """
    def __init__(self, *, admin_permissions: bool, stack_name: str, capabilities: typing.Optional[typing.List[aws_cdk.aws_cloudformation.CloudFormationCapabilities]]=None, deployment_role: typing.Optional[aws_cdk.aws_iam.IRole]=None, extra_inputs: typing.Optional[typing.List[aws_cdk.aws_codepipeline.Artifact]]=None, output: typing.Optional[aws_cdk.aws_codepipeline.Artifact]=None, output_file_name: typing.Optional[str]=None, parameter_overrides: typing.Optional[typing.Mapping[str,typing.Any]]=None, region: typing.Optional[str]=None, role: typing.Optional[aws_cdk.aws_iam.IRole]=None, template_configuration: typing.Optional[aws_cdk.aws_codepipeline.ArtifactPath]=None, action_name: str, run_order: typing.Optional[jsii.Number]=None) -> None:
        """
        Arguments:
            props: -
            admin_permissions: Whether to grant full permissions to CloudFormation while deploying this template. Setting this to ``true`` affects the defaults for ``role`` and ``capabilities``, if you don't specify any alternatives. The default role that will be created for you will have full (i.e., ``*``) permissions on all resources, and the deployment will have named IAM capabilities (i.e., able to create all IAM resources). This is a shorthand that you can use if you fully trust the templates that are deployed in this pipeline. If you want more fine-grained permissions, use ``addToRolePolicy`` and ``capabilities`` to control what the CloudFormation deployment is allowed to do.
            stack_name: The name of the stack to apply this action to.
            capabilities: Acknowledge certain changes made as part of deployment. For stacks that contain certain resources, explicit acknowledgement that AWS CloudFormation might create or update those resources. For example, you must specify ``AnonymousIAM`` or ``NamedIAM`` if your stack template contains AWS Identity and Access Management (IAM) resources. For more information see the link below. Default: None, unless ``adminPermissions`` is true
            deployment_role: IAM role to assume when deploying changes. If not specified, a fresh role is created. The role is created with zero permissions unless ``adminPermissions`` is true, in which case the role will have full permissions. Default: A fresh role with full or no permissions (depending on the value of ``adminPermissions``).
            extra_inputs: The list of additional input Artifacts for this Action. This is especially useful when used in conjunction with the ``parameterOverrides`` property. For example, if you have:. parameterOverrides: { 'Param1': action1.outputArtifact.bucketName, 'Param2': action2.outputArtifact.objectKey, } , if the output Artifacts of ``action1`` and ``action2`` were not used to set either the ``templateConfiguration`` or the ``templatePath`` properties, you need to make sure to include them in the ``extraInputs`` - otherwise, you'll get an "unrecognized Artifact" error during your Pipeline's execution.
            output: The name of the output artifact to generate. Only applied if ``outputFileName`` is set as well. Default: Automatically generated artifact name.
            output_file_name: A name for the filename in the output artifact to store the AWS CloudFormation call's result. The file will contain the result of the call to AWS CloudFormation (for example the call to UpdateStack or CreateChangeSet). AWS CodePipeline adds the file to the output artifact after performing the specified action. Default: No output artifact generated
            parameter_overrides: Additional template parameters. Template parameters specified here take precedence over template parameters found in the artifact specified by the ``templateConfiguration`` property. We recommend that you use the template configuration file to specify most of your parameter values. Use parameter overrides to specify only dynamic parameter values (values that are unknown until you run the pipeline). All parameter names must be present in the stack template. Note: the entire object cannot be more than 1kB. Default: No overrides
            region: The AWS region the given Action resides in. Note that a cross-region Pipeline requires replication buckets to function correctly. You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property. If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets, that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack. Default: the Action resides in the same region as the Pipeline
            role: The service role that is assumed during execution of action. This role is not mandatory, however more advanced configuration may require specifying it.
            template_configuration: Input artifact to use for template parameters values and stack policy. The template configuration file should contain a JSON object that should look like this: ``{ "Parameters": {...}, "Tags": {...}, "StackPolicy": {... }}``. For more information, see `AWS CloudFormation Artifacts <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html>`_. Note that if you include sensitive information, such as passwords, restrict access to this file. Default: No template configuration based on input artifacts
            action_name: The physical, human-readable name of the Action. Not that Action names must be unique within a single Stage.
            run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1

        Stability:
            experimental
        """
        props: CloudFormationDeleteStackActionProps = {"adminPermissions": admin_permissions, "stackName": stack_name, "actionName": action_name}

        if capabilities is not None:
            props["capabilities"] = capabilities

        if deployment_role is not None:
            props["deploymentRole"] = deployment_role

        if extra_inputs is not None:
            props["extraInputs"] = extra_inputs

        if output is not None:
            props["output"] = output

        if output_file_name is not None:
            props["outputFileName"] = output_file_name

        if parameter_overrides is not None:
            props["parameterOverrides"] = parameter_overrides

        if region is not None:
            props["region"] = region

        if role is not None:
            props["role"] = role

        if template_configuration is not None:
            props["templateConfiguration"] = template_configuration

        if run_order is not None:
            props["runOrder"] = run_order

        jsii.create(CloudFormationDeleteStackAction, self, [props])

    @jsii.member(jsii_name="addToDeploymentRolePolicy")
    def add_to_deployment_role_policy(self, statement: aws_cdk.aws_iam.PolicyStatement) -> bool:
        """Add statement to the service role assumed by CloudFormation while executing this action.

        Arguments:
            statement: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "addToDeploymentRolePolicy", [statement])

    @jsii.member(jsii_name="bound")
    def _bound(self, scope: aws_cdk.core.Construct, stage: aws_cdk.aws_codepipeline.IStage, *, role: aws_cdk.aws_iam.IRole) -> aws_cdk.aws_codepipeline.ActionConfig:
        """The method called when an Action is attached to a Pipeline. This method is guaranteed to be called only once for each Action instance.

        Arguments:
            scope: -
            stage: -
            options: -
            role: 

        Stability:
            experimental
        """
        options: aws_cdk.aws_codepipeline.ActionBindOptions = {"role": role}

        return jsii.invoke(self, "bound", [scope, stage, options])

    @property
    @jsii.member(jsii_name="deploymentRole")
    def deployment_role(self) -> aws_cdk.aws_iam.IRole:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "deploymentRole")


@jsii.data_type_optionals(jsii_struct_bases=[aws_cdk.aws_codepipeline.CommonActionProps])
class _CloudFormationDeleteStackActionProps(aws_cdk.aws_codepipeline.CommonActionProps, jsii.compat.TypedDict, total=False):
    capabilities: typing.List[aws_cdk.aws_cloudformation.CloudFormationCapabilities]
    """Acknowledge certain changes made as part of deployment.

    For stacks that contain certain resources, explicit acknowledgement that AWS CloudFormation
    might create or update those resources. For example, you must specify ``AnonymousIAM`` or ``NamedIAM``
    if your stack template contains AWS Identity and Access Management (IAM) resources. For more
    information see the link below.

    Default:
        None, unless ``adminPermissions`` is true

    See:
        https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#using-iam-capabilities
    Stability:
        experimental
    """
    deploymentRole: aws_cdk.aws_iam.IRole
    """IAM role to assume when deploying changes.

    If not specified, a fresh role is created. The role is created with zero
    permissions unless ``adminPermissions`` is true, in which case the role will have
    full permissions.

    Default:
        A fresh role with full or no permissions (depending on the value of ``adminPermissions``).

    Stability:
        experimental
    """
    extraInputs: typing.List[aws_cdk.aws_codepipeline.Artifact]
    """The list of additional input Artifacts for this Action. This is especially useful when used in conjunction with the ``parameterOverrides`` property. For example, if you have:.

    parameterOverrides: {
    'Param1': action1.outputArtifact.bucketName,
    'Param2': action2.outputArtifact.objectKey,
    }

    , if the output Artifacts of ``action1`` and ``action2`` were not used to
    set either the ``templateConfiguration`` or the ``templatePath`` properties,
    you need to make sure to include them in the ``extraInputs`` -
    otherwise, you'll get an "unrecognized Artifact" error during your Pipeline's execution.

    Stability:
        experimental
    """
    output: aws_cdk.aws_codepipeline.Artifact
    """The name of the output artifact to generate.

    Only applied if ``outputFileName`` is set as well.

    Default:
        Automatically generated artifact name.

    Stability:
        experimental
    """
    outputFileName: str
    """A name for the filename in the output artifact to store the AWS CloudFormation call's result.

    The file will contain the result of the call to AWS CloudFormation (for example
    the call to UpdateStack or CreateChangeSet).

    AWS CodePipeline adds the file to the output artifact after performing
    the specified action.

    Default:
        No output artifact generated

    Stability:
        experimental
    """
    parameterOverrides: typing.Mapping[str,typing.Any]
    """Additional template parameters.

    Template parameters specified here take precedence over template parameters
    found in the artifact specified by the ``templateConfiguration`` property.

    We recommend that you use the template configuration file to specify
    most of your parameter values. Use parameter overrides to specify only
    dynamic parameter values (values that are unknown until you run the
    pipeline).

    All parameter names must be present in the stack template.

    Note: the entire object cannot be more than 1kB.

    Default:
        No overrides

    Stability:
        experimental
    """
    region: str
    """The AWS region the given Action resides in. Note that a cross-region Pipeline requires replication buckets to function correctly. You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property. If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets, that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack.

    Default:
        the Action resides in the same region as the Pipeline

    Stability:
        experimental
    """
    role: aws_cdk.aws_iam.IRole
    """The service role that is assumed during execution of action. This role is not mandatory, however more advanced configuration may require specifying it.

    See:
        https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions.html
    Stability:
        experimental
    """
    templateConfiguration: aws_cdk.aws_codepipeline.ArtifactPath
    """Input artifact to use for template parameters values and stack policy.

    The template configuration file should contain a JSON object that should look like this:
    ``{ "Parameters": {...}, "Tags": {...}, "StackPolicy": {... }}``. For more information,
    see `AWS CloudFormation Artifacts <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-cfn-artifacts.html>`_.

    Note that if you include sensitive information, such as passwords, restrict access to this
    file.

    Default:
        No template configuration based on input artifacts

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codepipeline-actions.CloudFormationDeleteStackActionProps", jsii_struct_bases=[_CloudFormationDeleteStackActionProps])
class CloudFormationDeleteStackActionProps(_CloudFormationDeleteStackActionProps):
    """Properties for the CloudFormationDeleteStackAction.

    Stability:
        experimental
    """
    adminPermissions: bool
    """Whether to grant full permissions to CloudFormation while deploying this template.

    Setting this to ``true`` affects the defaults for ``role`` and ``capabilities``, if you
    don't specify any alternatives.

    The default role that will be created for you will have full (i.e., ``*``)
    permissions on all resources, and the deployment will have named IAM
    capabilities (i.e., able to create all IAM resources).

    This is a shorthand that you can use if you fully trust the templates that
    are deployed in this pipeline. If you want more fine-grained permissions,
    use ``addToRolePolicy`` and ``capabilities`` to control what the CloudFormation
    deployment is allowed to do.

    Stability:
        experimental
    """

    stackName: str
    """The name of the stack to apply this action to.

    Stability:
        experimental
    """

class CloudFormationExecuteChangeSetAction(Action, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codepipeline-actions.CloudFormationExecuteChangeSetAction"):
    """CodePipeline action to execute a prepared change set.

    Stability:
        experimental
    """
    def __init__(self, *, change_set_name: str, stack_name: str, output: typing.Optional[aws_cdk.aws_codepipeline.Artifact]=None, output_file_name: typing.Optional[str]=None, region: typing.Optional[str]=None, role: typing.Optional[aws_cdk.aws_iam.IRole]=None, action_name: str, run_order: typing.Optional[jsii.Number]=None) -> None:
        """
        Arguments:
            props: -
            change_set_name: Name of the change set to execute.
            stack_name: The name of the stack to apply this action to.
            output: The name of the output artifact to generate. Only applied if ``outputFileName`` is set as well. Default: Automatically generated artifact name.
            output_file_name: A name for the filename in the output artifact to store the AWS CloudFormation call's result. The file will contain the result of the call to AWS CloudFormation (for example the call to UpdateStack or CreateChangeSet). AWS CodePipeline adds the file to the output artifact after performing the specified action. Default: No output artifact generated
            region: The AWS region the given Action resides in. Note that a cross-region Pipeline requires replication buckets to function correctly. You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property. If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets, that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack. Default: the Action resides in the same region as the Pipeline
            role: The service role that is assumed during execution of action. This role is not mandatory, however more advanced configuration may require specifying it.
            action_name: The physical, human-readable name of the Action. Not that Action names must be unique within a single Stage.
            run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1

        Stability:
            experimental
        """
        props: CloudFormationExecuteChangeSetActionProps = {"changeSetName": change_set_name, "stackName": stack_name, "actionName": action_name}

        if output is not None:
            props["output"] = output

        if output_file_name is not None:
            props["outputFileName"] = output_file_name

        if region is not None:
            props["region"] = region

        if role is not None:
            props["role"] = role

        if run_order is not None:
            props["runOrder"] = run_order

        jsii.create(CloudFormationExecuteChangeSetAction, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(self, scope: aws_cdk.core.Construct, stage: aws_cdk.aws_codepipeline.IStage, *, role: aws_cdk.aws_iam.IRole) -> aws_cdk.aws_codepipeline.ActionConfig:
        """The method called when an Action is attached to a Pipeline. This method is guaranteed to be called only once for each Action instance.

        Arguments:
            scope: -
            stage: -
            options: -
            role: 

        Stability:
            experimental
        """
        options: aws_cdk.aws_codepipeline.ActionBindOptions = {"role": role}

        return jsii.invoke(self, "bound", [scope, stage, options])


@jsii.data_type_optionals(jsii_struct_bases=[aws_cdk.aws_codepipeline.CommonActionProps])
class _CloudFormationExecuteChangeSetActionProps(aws_cdk.aws_codepipeline.CommonActionProps, jsii.compat.TypedDict, total=False):
    output: aws_cdk.aws_codepipeline.Artifact
    """The name of the output artifact to generate.

    Only applied if ``outputFileName`` is set as well.

    Default:
        Automatically generated artifact name.

    Stability:
        experimental
    """
    outputFileName: str
    """A name for the filename in the output artifact to store the AWS CloudFormation call's result.

    The file will contain the result of the call to AWS CloudFormation (for example
    the call to UpdateStack or CreateChangeSet).

    AWS CodePipeline adds the file to the output artifact after performing
    the specified action.

    Default:
        No output artifact generated

    Stability:
        experimental
    """
    region: str
    """The AWS region the given Action resides in. Note that a cross-region Pipeline requires replication buckets to function correctly. You can provide their names with the {@link PipelineProps#crossRegionReplicationBuckets} property. If you don't, the CodePipeline Construct will create new Stacks in your CDK app containing those buckets, that you will need to ``cdk deploy`` before deploying the main, Pipeline-containing Stack.

    Default:
        the Action resides in the same region as the Pipeline

    Stability:
        experimental
    """
    role: aws_cdk.aws_iam.IRole
    """The service role that is assumed during execution of action. This role is not mandatory, however more advanced configuration may require specifying it.

    See:
        https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-stages-actions.html
    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codepipeline-actions.CloudFormationExecuteChangeSetActionProps", jsii_struct_bases=[_CloudFormationExecuteChangeSetActionProps])
class CloudFormationExecuteChangeSetActionProps(_CloudFormationExecuteChangeSetActionProps):
    """Properties for the CloudFormationExecuteChangeSetAction.

    Stability:
        experimental
    """
    changeSetName: str
    """Name of the change set to execute.

    Stability:
        experimental
    """

    stackName: str
    """The name of the stack to apply this action to.

    Stability:
        experimental
    """

class CodeBuildAction(Action, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codepipeline-actions.CodeBuildAction"):
    """CodePipeline build action that uses AWS CodeBuild.

    Stability:
        experimental
    """
    def __init__(self, *, input: aws_cdk.aws_codepipeline.Artifact, project: aws_cdk.aws_codebuild.IProject, extra_inputs: typing.Optional[typing.List[aws_cdk.aws_codepipeline.Artifact]]=None, outputs: typing.Optional[typing.List[aws_cdk.aws_codepipeline.Artifact]]=None, type: typing.Optional["CodeBuildActionType"]=None, action_name: str, run_order: typing.Optional[jsii.Number]=None) -> None:
        """
        Arguments:
            props: -
            input: The source to use as input for this action.
            project: The action's Project.
            extra_inputs: The list of additional input Artifacts for this action.
            outputs: The list of output Artifacts for this action. **Note**: if you specify more than one output Artifact here, you cannot use the primary 'artifacts' section of the buildspec; you have to use the 'secondary-artifacts' section instead. See https://docs.aws.amazon.com/codebuild/latest/userguide/sample-multi-in-out.html for details. Default: the action will not have any outputs
            type: The type of the action that determines its CodePipeline Category - Build, or Test. Default: CodeBuildActionType.BUILD
            action_name: The physical, human-readable name of the Action. Not that Action names must be unique within a single Stage.
            run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1

        Stability:
            experimental
        """
        props: CodeBuildActionProps = {"input": input, "project": project, "actionName": action_name}

        if extra_inputs is not None:
            props["extraInputs"] = extra_inputs

        if outputs is not None:
            props["outputs"] = outputs

        if type is not None:
            props["type"] = type

        if run_order is not None:
            props["runOrder"] = run_order

        jsii.create(CodeBuildAction, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(self, _scope: aws_cdk.core.Construct, stage: aws_cdk.aws_codepipeline.IStage, *, role: aws_cdk.aws_iam.IRole) -> aws_cdk.aws_codepipeline.ActionConfig:
        """The method called when an Action is attached to a Pipeline. This method is guaranteed to be called only once for each Action instance.

        Arguments:
            _scope: -
            stage: -
            options: -
            role: 

        Stability:
            experimental
        """
        options: aws_cdk.aws_codepipeline.ActionBindOptions = {"role": role}

        return jsii.invoke(self, "bound", [_scope, stage, options])


@jsii.data_type_optionals(jsii_struct_bases=[aws_cdk.aws_codepipeline.CommonActionProps])
class _CodeBuildActionProps(aws_cdk.aws_codepipeline.CommonActionProps, jsii.compat.TypedDict, total=False):
    extraInputs: typing.List[aws_cdk.aws_codepipeline.Artifact]
    """The list of additional input Artifacts for this action.

    Stability:
        experimental
    """
    outputs: typing.List[aws_cdk.aws_codepipeline.Artifact]
    """The list of output Artifacts for this action. **Note**: if you specify more than one output Artifact here, you cannot use the primary 'artifacts' section of the buildspec; you have to use the 'secondary-artifacts' section instead. See https://docs.aws.amazon.com/codebuild/latest/userguide/sample-multi-in-out.html for details.

    Default:
        the action will not have any outputs

    Stability:
        experimental
    """
    type: "CodeBuildActionType"
    """The type of the action that determines its CodePipeline Category - Build, or Test.

    Default:
        CodeBuildActionType.BUILD

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codepipeline-actions.CodeBuildActionProps", jsii_struct_bases=[_CodeBuildActionProps])
class CodeBuildActionProps(_CodeBuildActionProps):
    """Construction properties of the {@link CodeBuildAction CodeBuild build CodePipeline action}.

    Stability:
        experimental
    """
    input: aws_cdk.aws_codepipeline.Artifact
    """The source to use as input for this action.

    Stability:
        experimental
    """

    project: aws_cdk.aws_codebuild.IProject
    """The action's Project.

    Stability:
        experimental
    """

@jsii.enum(jsii_type="@aws-cdk/aws-codepipeline-actions.CodeBuildActionType")
class CodeBuildActionType(enum.Enum):
    """The type of the CodeBuild action that determines its CodePipeline Category - Build, or Test. The default is Build.

    Stability:
        experimental
    """
    BUILD = "BUILD"
    """The action will have the Build Category. This is the default.

    Stability:
        experimental
    """
    TEST = "TEST"
    """The action will have the Test Category.

    Stability:
        experimental
    """

class CodeCommitSourceAction(Action, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codepipeline-actions.CodeCommitSourceAction"):
    """CodePipeline Source that is provided by an AWS CodeCommit repository.

    Stability:
        experimental
    """
    def __init__(self, *, output: aws_cdk.aws_codepipeline.Artifact, repository: aws_cdk.aws_codecommit.IRepository, branch: typing.Optional[str]=None, trigger: typing.Optional["CodeCommitTrigger"]=None, action_name: str, run_order: typing.Optional[jsii.Number]=None) -> None:
        """
        Arguments:
            props: -
            output: 
            repository: The CodeCommit repository.
            branch: Default: 'master'
            trigger: How should CodePipeline detect source changes for this Action. Default: CodeCommitTrigger.EVENTS
            action_name: The physical, human-readable name of the Action. Not that Action names must be unique within a single Stage.
            run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1

        Stability:
            experimental
        """
        props: CodeCommitSourceActionProps = {"output": output, "repository": repository, "actionName": action_name}

        if branch is not None:
            props["branch"] = branch

        if trigger is not None:
            props["trigger"] = trigger

        if run_order is not None:
            props["runOrder"] = run_order

        jsii.create(CodeCommitSourceAction, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(self, _scope: aws_cdk.core.Construct, stage: aws_cdk.aws_codepipeline.IStage, *, role: aws_cdk.aws_iam.IRole) -> aws_cdk.aws_codepipeline.ActionConfig:
        """The method called when an Action is attached to a Pipeline. This method is guaranteed to be called only once for each Action instance.

        Arguments:
            _scope: -
            stage: -
            options: -
            role: 

        Stability:
            experimental
        """
        options: aws_cdk.aws_codepipeline.ActionBindOptions = {"role": role}

        return jsii.invoke(self, "bound", [_scope, stage, options])


@jsii.data_type_optionals(jsii_struct_bases=[aws_cdk.aws_codepipeline.CommonActionProps])
class _CodeCommitSourceActionProps(aws_cdk.aws_codepipeline.CommonActionProps, jsii.compat.TypedDict, total=False):
    branch: str
    """
    Default:
        'master'

    Stability:
        experimental
    """
    trigger: "CodeCommitTrigger"
    """How should CodePipeline detect source changes for this Action.

    Default:
        CodeCommitTrigger.EVENTS

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codepipeline-actions.CodeCommitSourceActionProps", jsii_struct_bases=[_CodeCommitSourceActionProps])
class CodeCommitSourceActionProps(_CodeCommitSourceActionProps):
    """Construction properties of the {@link CodeCommitSourceAction CodeCommit source CodePipeline Action}.

    Stability:
        experimental
    """
    output: aws_cdk.aws_codepipeline.Artifact
    """
    Stability:
        experimental
    """

    repository: aws_cdk.aws_codecommit.IRepository
    """The CodeCommit repository.

    Stability:
        experimental
    """

@jsii.enum(jsii_type="@aws-cdk/aws-codepipeline-actions.CodeCommitTrigger")
class CodeCommitTrigger(enum.Enum):
    """How should the CodeCommit Action detect changes. This is the type of the {@link CodeCommitSourceAction.trigger} property.

    Stability:
        experimental
    """
    NONE = "NONE"
    """The Action will never detect changes - the Pipeline it's part of will only begin a run when explicitly started.

    Stability:
        experimental
    """
    POLL = "POLL"
    """CodePipeline will poll the repository to detect changes.

    Stability:
        experimental
    """
    EVENTS = "EVENTS"
    """CodePipeline will use CloudWatch Events to be notified of changes. This is the default method of detecting changes.

    Stability:
        experimental
    """

class CodeDeployServerDeployAction(Action, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codepipeline-actions.CodeDeployServerDeployAction"):
    """
    Stability:
        experimental
    """
    def __init__(self, *, deployment_group: aws_cdk.aws_codedeploy.IServerDeploymentGroup, input: aws_cdk.aws_codepipeline.Artifact, action_name: str, run_order: typing.Optional[jsii.Number]=None) -> None:
        """
        Arguments:
            props: -
            deployment_group: The CodeDeploy server Deployment Group to deploy to.
            input: The source to use as input for deployment.
            action_name: The physical, human-readable name of the Action. Not that Action names must be unique within a single Stage.
            run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1

        Stability:
            experimental
        """
        props: CodeDeployServerDeployActionProps = {"deploymentGroup": deployment_group, "input": input, "actionName": action_name}

        if run_order is not None:
            props["runOrder"] = run_order

        jsii.create(CodeDeployServerDeployAction, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(self, _scope: aws_cdk.core.Construct, stage: aws_cdk.aws_codepipeline.IStage, *, role: aws_cdk.aws_iam.IRole) -> aws_cdk.aws_codepipeline.ActionConfig:
        """The method called when an Action is attached to a Pipeline. This method is guaranteed to be called only once for each Action instance.

        Arguments:
            _scope: -
            stage: -
            options: -
            role: 

        Stability:
            experimental
        """
        options: aws_cdk.aws_codepipeline.ActionBindOptions = {"role": role}

        return jsii.invoke(self, "bound", [_scope, stage, options])


@jsii.data_type(jsii_type="@aws-cdk/aws-codepipeline-actions.CodeDeployServerDeployActionProps", jsii_struct_bases=[aws_cdk.aws_codepipeline.CommonActionProps])
class CodeDeployServerDeployActionProps(aws_cdk.aws_codepipeline.CommonActionProps, jsii.compat.TypedDict):
    """Construction properties of the {@link CodeDeployServerDeployAction CodeDeploy server deploy CodePipeline Action}.

    Stability:
        experimental
    """
    deploymentGroup: aws_cdk.aws_codedeploy.IServerDeploymentGroup
    """The CodeDeploy server Deployment Group to deploy to.

    Stability:
        experimental
    """

    input: aws_cdk.aws_codepipeline.Artifact
    """The source to use as input for deployment.

    Stability:
        experimental
    """

class EcrSourceAction(Action, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codepipeline-actions.EcrSourceAction"):
    """The ECR Repository source CodePipeline Action.

    Will trigger the pipeline as soon as the target tag in the repository
    changes, but only if there is a CloudTrail Trail in the account that
    captures the ECR event.

    Stability:
        experimental
    """
    def __init__(self, *, output: aws_cdk.aws_codepipeline.Artifact, repository: aws_cdk.aws_ecr.IRepository, image_tag: typing.Optional[str]=None, action_name: str, run_order: typing.Optional[jsii.Number]=None) -> None:
        """
        Arguments:
            props: -
            output: 
            repository: The repository that will be watched for changes.
            image_tag: The image tag that will be checked for changes. Default: 'latest'
            action_name: The physical, human-readable name of the Action. Not that Action names must be unique within a single Stage.
            run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1

        Stability:
            experimental
        """
        props: EcrSourceActionProps = {"output": output, "repository": repository, "actionName": action_name}

        if image_tag is not None:
            props["imageTag"] = image_tag

        if run_order is not None:
            props["runOrder"] = run_order

        jsii.create(EcrSourceAction, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(self, _scope: aws_cdk.core.Construct, stage: aws_cdk.aws_codepipeline.IStage, *, role: aws_cdk.aws_iam.IRole) -> aws_cdk.aws_codepipeline.ActionConfig:
        """The method called when an Action is attached to a Pipeline. This method is guaranteed to be called only once for each Action instance.

        Arguments:
            _scope: -
            stage: -
            options: -
            role: 

        Stability:
            experimental
        """
        options: aws_cdk.aws_codepipeline.ActionBindOptions = {"role": role}

        return jsii.invoke(self, "bound", [_scope, stage, options])


@jsii.data_type_optionals(jsii_struct_bases=[aws_cdk.aws_codepipeline.CommonActionProps])
class _EcrSourceActionProps(aws_cdk.aws_codepipeline.CommonActionProps, jsii.compat.TypedDict, total=False):
    imageTag: str
    """The image tag that will be checked for changes.

    Default:
        'latest'

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codepipeline-actions.EcrSourceActionProps", jsii_struct_bases=[_EcrSourceActionProps])
class EcrSourceActionProps(_EcrSourceActionProps):
    """Construction properties of {@link EcrSourceAction}.

    Stability:
        experimental
    """
    output: aws_cdk.aws_codepipeline.Artifact
    """
    Stability:
        experimental
    """

    repository: aws_cdk.aws_ecr.IRepository
    """The repository that will be watched for changes.

    Stability:
        experimental
    """

class EcsDeployAction(Action, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codepipeline-actions.EcsDeployAction"):
    """CodePipeline Action to deploy an ECS Service.

    Stability:
        experimental
    """
    def __init__(self, *, service: aws_cdk.aws_ecs.BaseService, image_file: typing.Optional[aws_cdk.aws_codepipeline.ArtifactPath]=None, input: typing.Optional[aws_cdk.aws_codepipeline.Artifact]=None, action_name: str, run_order: typing.Optional[jsii.Number]=None) -> None:
        """
        Arguments:
            props: -
            service: The ECS Service to deploy.
            image_file: The name of the JSON image definitions file to use for deployments. The JSON file is a list of objects, each with 2 keys: ``name`` is the name of the container in the Task Definition, and ``imageUri`` is the Docker image URI you want to update your service with. Use this property if you want to use a different name for this file than the default 'imagedefinitions.json'. If you use this property, you don't need to specify the ``input`` property. Default: - one of this property, or ``input``, is required
            input: The input artifact that contains the JSON image definitions file to use for deployments. The JSON file is a list of objects, each with 2 keys: ``name`` is the name of the container in the Task Definition, and ``imageUri`` is the Docker image URI you want to update your service with. If you use this property, it's assumed the file is called 'imagedefinitions.json'. If your build uses a different file, leave this property empty, and use the ``imageFile`` property instead. Default: - one of this property, or ``imageFile``, is required
            action_name: The physical, human-readable name of the Action. Not that Action names must be unique within a single Stage.
            run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1

        Stability:
            experimental
        """
        props: EcsDeployActionProps = {"service": service, "actionName": action_name}

        if image_file is not None:
            props["imageFile"] = image_file

        if input is not None:
            props["input"] = input

        if run_order is not None:
            props["runOrder"] = run_order

        jsii.create(EcsDeployAction, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(self, _scope: aws_cdk.core.Construct, _stage: aws_cdk.aws_codepipeline.IStage, *, role: aws_cdk.aws_iam.IRole) -> aws_cdk.aws_codepipeline.ActionConfig:
        """The method called when an Action is attached to a Pipeline. This method is guaranteed to be called only once for each Action instance.

        Arguments:
            _scope: -
            _stage: -
            options: -
            role: 

        Stability:
            experimental
        """
        options: aws_cdk.aws_codepipeline.ActionBindOptions = {"role": role}

        return jsii.invoke(self, "bound", [_scope, _stage, options])


@jsii.data_type_optionals(jsii_struct_bases=[aws_cdk.aws_codepipeline.CommonActionProps])
class _EcsDeployActionProps(aws_cdk.aws_codepipeline.CommonActionProps, jsii.compat.TypedDict, total=False):
    imageFile: aws_cdk.aws_codepipeline.ArtifactPath
    """The name of the JSON image definitions file to use for deployments. The JSON file is a list of objects, each with 2 keys: ``name`` is the name of the container in the Task Definition, and ``imageUri`` is the Docker image URI you want to update your service with. Use this property if you want to use a different name for this file than the default 'imagedefinitions.json'. If you use this property, you don't need to specify the ``input`` property.

    Default:
        - one of this property, or ``input``, is required

    See:
        https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create.html#pipelines-create-image-definitions
    Stability:
        experimental
    """
    input: aws_cdk.aws_codepipeline.Artifact
    """The input artifact that contains the JSON image definitions file to use for deployments. The JSON file is a list of objects, each with 2 keys: ``name`` is the name of the container in the Task Definition, and ``imageUri`` is the Docker image URI you want to update your service with. If you use this property, it's assumed the file is called 'imagedefinitions.json'. If your build uses a different file, leave this property empty, and use the ``imageFile`` property instead.

    Default:
        - one of this property, or ``imageFile``, is required

    See:
        https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-create.html#pipelines-create-image-definitions
    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codepipeline-actions.EcsDeployActionProps", jsii_struct_bases=[_EcsDeployActionProps])
class EcsDeployActionProps(_EcsDeployActionProps):
    """Construction properties of {@link EcsDeployAction}.

    Stability:
        experimental
    """
    service: aws_cdk.aws_ecs.BaseService
    """The ECS Service to deploy.

    Stability:
        experimental
    """

class GitHubSourceAction(Action, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codepipeline-actions.GitHubSourceAction"):
    """Source that is provided by a GitHub repository.

    Stability:
        experimental
    """
    def __init__(self, *, oauth_token: aws_cdk.core.SecretValue, output: aws_cdk.aws_codepipeline.Artifact, owner: str, repo: str, branch: typing.Optional[str]=None, trigger: typing.Optional["GitHubTrigger"]=None, action_name: str, run_order: typing.Optional[jsii.Number]=None) -> None:
        """
        Arguments:
            props: -
            oauth_token: A GitHub OAuth token to use for authentication. It is recommended to use a Secrets Manager ``SecretString`` to obtain the token: const oauth = new secretsmanager.SecretString(this, 'GitHubOAuthToken', { secretId: 'my-github-token' }); new GitHubSource(this, 'GitHubAction', { oauthToken: oauth.value, ... });
            output: 
            owner: The GitHub account/user that owns the repo.
            repo: The name of the repo, without the username.
            branch: The branch to use. Default: "master"
            trigger: How AWS CodePipeline should be triggered. With the default value "WEBHOOK", a webhook is created in GitHub that triggers the action With "POLL", CodePipeline periodically checks the source for changes With "None", the action is not triggered through changes in the source Default: GitHubTrigger.WEBHOOK
            action_name: The physical, human-readable name of the Action. Not that Action names must be unique within a single Stage.
            run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1

        Stability:
            experimental
        """
        props: GitHubSourceActionProps = {"oauthToken": oauth_token, "output": output, "owner": owner, "repo": repo, "actionName": action_name}

        if branch is not None:
            props["branch"] = branch

        if trigger is not None:
            props["trigger"] = trigger

        if run_order is not None:
            props["runOrder"] = run_order

        jsii.create(GitHubSourceAction, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(self, scope: aws_cdk.core.Construct, stage: aws_cdk.aws_codepipeline.IStage, *, role: aws_cdk.aws_iam.IRole) -> aws_cdk.aws_codepipeline.ActionConfig:
        """The method called when an Action is attached to a Pipeline. This method is guaranteed to be called only once for each Action instance.

        Arguments:
            scope: -
            stage: -
            _options: -
            role: 

        Stability:
            experimental
        """
        _options: aws_cdk.aws_codepipeline.ActionBindOptions = {"role": role}

        return jsii.invoke(self, "bound", [scope, stage, _options])


@jsii.data_type_optionals(jsii_struct_bases=[aws_cdk.aws_codepipeline.CommonActionProps])
class _GitHubSourceActionProps(aws_cdk.aws_codepipeline.CommonActionProps, jsii.compat.TypedDict, total=False):
    branch: str
    """The branch to use.

    Default:
        "master"

    Stability:
        experimental
    """
    trigger: "GitHubTrigger"
    """How AWS CodePipeline should be triggered.

    With the default value "WEBHOOK", a webhook is created in GitHub that triggers the action
    With "POLL", CodePipeline periodically checks the source for changes
    With "None", the action is not triggered through changes in the source

    Default:
        GitHubTrigger.WEBHOOK

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codepipeline-actions.GitHubSourceActionProps", jsii_struct_bases=[_GitHubSourceActionProps])
class GitHubSourceActionProps(_GitHubSourceActionProps):
    """Construction properties of the {@link GitHubSourceAction GitHub source action}.

    Stability:
        experimental
    """
    oauthToken: aws_cdk.core.SecretValue
    """A GitHub OAuth token to use for authentication.

    It is recommended to use a Secrets Manager ``SecretString`` to obtain the token:

    const oauth = new secretsmanager.SecretString(this, 'GitHubOAuthToken', { secretId: 'my-github-token' });
    new GitHubSource(this, 'GitHubAction', { oauthToken: oauth.value, ... });

    Stability:
        experimental
    """

    output: aws_cdk.aws_codepipeline.Artifact
    """
    Stability:
        experimental
    """

    owner: str
    """The GitHub account/user that owns the repo.

    Stability:
        experimental
    """

    repo: str
    """The name of the repo, without the username.

    Stability:
        experimental
    """

@jsii.enum(jsii_type="@aws-cdk/aws-codepipeline-actions.GitHubTrigger")
class GitHubTrigger(enum.Enum):
    """If and how the GitHub source action should be triggered.

    Stability:
        experimental
    """
    NONE = "NONE"
    """
    Stability:
        experimental
    """
    POLL = "POLL"
    """
    Stability:
        experimental
    """
    WEBHOOK = "WEBHOOK"
    """
    Stability:
        experimental
    """

@jsii.interface(jsii_type="@aws-cdk/aws-codepipeline-actions.IJenkinsProvider")
class IJenkinsProvider(aws_cdk.core.IConstruct, jsii.compat.Protocol):
    """A Jenkins provider.

    If you want to create a new Jenkins provider managed alongside your CDK code,
    instantiate the {@link JenkinsProvider} class directly.

    If you want to reference an already registered provider,
    use the {@link JenkinsProvider#fromJenkinsProviderAttributes} method.

    Stability:
        experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _IJenkinsProviderProxy

    @property
    @jsii.member(jsii_name="providerName")
    def provider_name(self) -> str:
        """
        Stability:
            experimental
        """
        ...

    @property
    @jsii.member(jsii_name="serverUrl")
    def server_url(self) -> str:
        """
        Stability:
            experimental
        """
        ...

    @property
    @jsii.member(jsii_name="version")
    def version(self) -> str:
        """
        Stability:
            experimental
        """
        ...


class _IJenkinsProviderProxy(jsii.proxy_for(aws_cdk.core.IConstruct)):
    """A Jenkins provider.

    If you want to create a new Jenkins provider managed alongside your CDK code,
    instantiate the {@link JenkinsProvider} class directly.

    If you want to reference an already registered provider,
    use the {@link JenkinsProvider#fromJenkinsProviderAttributes} method.

    Stability:
        experimental
    """
    __jsii_type__ = "@aws-cdk/aws-codepipeline-actions.IJenkinsProvider"
    @property
    @jsii.member(jsii_name="providerName")
    def provider_name(self) -> str:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "providerName")

    @property
    @jsii.member(jsii_name="serverUrl")
    def server_url(self) -> str:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "serverUrl")

    @property
    @jsii.member(jsii_name="version")
    def version(self) -> str:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "version")


@jsii.implements(IJenkinsProvider)
class BaseJenkinsProvider(aws_cdk.core.Construct, metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-codepipeline-actions.BaseJenkinsProvider"):
    """
    Stability:
        experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _BaseJenkinsProviderProxy

    def __init__(self, scope: aws_cdk.core.Construct, id: str, version: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            version: -

        Stability:
            experimental
        """
        jsii.create(BaseJenkinsProvider, self, [scope, id, version])

    @property
    @jsii.member(jsii_name="providerName")
    @abc.abstractmethod
    def provider_name(self) -> str:
        """
        Stability:
            experimental
        """
        ...

    @property
    @jsii.member(jsii_name="serverUrl")
    @abc.abstractmethod
    def server_url(self) -> str:
        """
        Stability:
            experimental
        """
        ...

    @property
    @jsii.member(jsii_name="version")
    def version(self) -> str:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "version")


class _BaseJenkinsProviderProxy(BaseJenkinsProvider):
    @property
    @jsii.member(jsii_name="providerName")
    def provider_name(self) -> str:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "providerName")

    @property
    @jsii.member(jsii_name="serverUrl")
    def server_url(self) -> str:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "serverUrl")


class JenkinsAction(Action, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codepipeline-actions.JenkinsAction"):
    """Jenkins build CodePipeline Action.

    See:
        https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-four-stage-pipeline.html
    Stability:
        experimental
    """
    def __init__(self, *, jenkins_provider: "IJenkinsProvider", project_name: str, type: "JenkinsActionType", inputs: typing.Optional[typing.List[aws_cdk.aws_codepipeline.Artifact]]=None, outputs: typing.Optional[typing.List[aws_cdk.aws_codepipeline.Artifact]]=None, action_name: str, run_order: typing.Optional[jsii.Number]=None) -> None:
        """
        Arguments:
            props: -
            jenkins_provider: The Jenkins Provider for this Action.
            project_name: The name of the project (sometimes also called job, or task) on your Jenkins installation that will be invoked by this Action.
            type: The type of the Action - Build, or Test.
            inputs: The source to use as input for this build.
            outputs: 
            action_name: The physical, human-readable name of the Action. Not that Action names must be unique within a single Stage.
            run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1

        Stability:
            experimental
        """
        props: JenkinsActionProps = {"jenkinsProvider": jenkins_provider, "projectName": project_name, "type": type, "actionName": action_name}

        if inputs is not None:
            props["inputs"] = inputs

        if outputs is not None:
            props["outputs"] = outputs

        if run_order is not None:
            props["runOrder"] = run_order

        jsii.create(JenkinsAction, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(self, _scope: aws_cdk.core.Construct, _stage: aws_cdk.aws_codepipeline.IStage, *, role: aws_cdk.aws_iam.IRole) -> aws_cdk.aws_codepipeline.ActionConfig:
        """The method called when an Action is attached to a Pipeline. This method is guaranteed to be called only once for each Action instance.

        Arguments:
            _scope: -
            _stage: -
            _options: -
            role: 

        Stability:
            experimental
        """
        _options: aws_cdk.aws_codepipeline.ActionBindOptions = {"role": role}

        return jsii.invoke(self, "bound", [_scope, _stage, _options])


@jsii.data_type_optionals(jsii_struct_bases=[aws_cdk.aws_codepipeline.CommonActionProps])
class _JenkinsActionProps(aws_cdk.aws_codepipeline.CommonActionProps, jsii.compat.TypedDict, total=False):
    inputs: typing.List[aws_cdk.aws_codepipeline.Artifact]
    """The source to use as input for this build.

    Stability:
        experimental
    """
    outputs: typing.List[aws_cdk.aws_codepipeline.Artifact]
    """
    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codepipeline-actions.JenkinsActionProps", jsii_struct_bases=[_JenkinsActionProps])
class JenkinsActionProps(_JenkinsActionProps):
    """Construction properties of {@link JenkinsAction}.

    Stability:
        experimental
    """
    jenkinsProvider: "IJenkinsProvider"
    """The Jenkins Provider for this Action.

    Stability:
        experimental
    """

    projectName: str
    """The name of the project (sometimes also called job, or task) on your Jenkins installation that will be invoked by this Action.

    Stability:
        experimental

    Example::
        'MyJob'
    """

    type: "JenkinsActionType"
    """The type of the Action - Build, or Test.

    Stability:
        experimental
    """

@jsii.enum(jsii_type="@aws-cdk/aws-codepipeline-actions.JenkinsActionType")
class JenkinsActionType(enum.Enum):
    """The type of the Jenkins Action that determines its CodePipeline Category - Build, or Test. Note that a Jenkins provider, even if it has the same name, must be separately registered for each type.

    Stability:
        experimental
    """
    BUILD = "BUILD"
    """The Action will have the Build Category.

    Stability:
        experimental
    """
    TEST = "TEST"
    """The Action will have the Test Category.

    Stability:
        experimental
    """

class JenkinsProvider(BaseJenkinsProvider, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codepipeline-actions.JenkinsProvider"):
    """A class representing Jenkins providers.

    See:
        #import
    Stability:
        experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, provider_name: str, server_url: str, for_build: typing.Optional[bool]=None, for_test: typing.Optional[bool]=None, version: typing.Optional[str]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            provider_name: The name of the Jenkins provider that you set in the AWS CodePipeline plugin configuration of your Jenkins project.
            server_url: The base URL of your Jenkins server.
            for_build: Whether to immediately register a Jenkins Provider for the build category. The Provider will always be registered if you create a {@link JenkinsAction}. Default: false
            for_test: Whether to immediately register a Jenkins Provider for the test category. The Provider will always be registered if you create a {@link JenkinsTestAction}. Default: false
            version: The version of your provider. Default: '1'

        Stability:
            experimental
        """
        props: JenkinsProviderProps = {"providerName": provider_name, "serverUrl": server_url}

        if for_build is not None:
            props["forBuild"] = for_build

        if for_test is not None:
            props["forTest"] = for_test

        if version is not None:
            props["version"] = version

        jsii.create(JenkinsProvider, self, [scope, id, props])

    @jsii.member(jsii_name="fromJenkinsProviderAttributes")
    @classmethod
    def from_jenkins_provider_attributes(cls, scope: aws_cdk.core.Construct, id: str, *, provider_name: str, server_url: str, version: typing.Optional[str]=None) -> "IJenkinsProvider":
        """Import a Jenkins provider registered either outside the CDK, or in a different CDK Stack.

        Arguments:
            scope: the parent Construct for the new provider.
            id: the identifier of the new provider Construct.
            attrs: the properties used to identify the existing provider.
            provider_name: The name of the Jenkins provider that you set in the AWS CodePipeline plugin configuration of your Jenkins project.
            server_url: The base URL of your Jenkins server.
            version: The version of your provider. Default: '1'

        Returns:
            a new Construct representing a reference to an existing Jenkins provider

        Stability:
            experimental
        """
        attrs: JenkinsProviderAttributes = {"providerName": provider_name, "serverUrl": server_url}

        if version is not None:
            attrs["version"] = version

        return jsii.sinvoke(cls, "fromJenkinsProviderAttributes", [scope, id, attrs])

    @property
    @jsii.member(jsii_name="providerName")
    def provider_name(self) -> str:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "providerName")

    @property
    @jsii.member(jsii_name="serverUrl")
    def server_url(self) -> str:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "serverUrl")


@jsii.data_type_optionals(jsii_struct_bases=[])
class _JenkinsProviderAttributes(jsii.compat.TypedDict, total=False):
    version: str
    """The version of your provider.

    Default:
        '1'

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codepipeline-actions.JenkinsProviderAttributes", jsii_struct_bases=[_JenkinsProviderAttributes])
class JenkinsProviderAttributes(_JenkinsProviderAttributes):
    """Properties for importing an existing Jenkins provider.

    Stability:
        experimental
    """
    providerName: str
    """The name of the Jenkins provider that you set in the AWS CodePipeline plugin configuration of your Jenkins project.

    Stability:
        experimental

    Example::
        'MyJenkinsProvider'
    """

    serverUrl: str
    """The base URL of your Jenkins server.

    Stability:
        experimental

    Example::
        'http://myjenkins.com:8080'
    """

@jsii.data_type_optionals(jsii_struct_bases=[])
class _JenkinsProviderProps(jsii.compat.TypedDict, total=False):
    forBuild: bool
    """Whether to immediately register a Jenkins Provider for the build category. The Provider will always be registered if you create a {@link JenkinsAction}.

    Default:
        false

    Stability:
        experimental
    """
    forTest: bool
    """Whether to immediately register a Jenkins Provider for the test category. The Provider will always be registered if you create a {@link JenkinsTestAction}.

    Default:
        false

    Stability:
        experimental
    """
    version: str
    """The version of your provider.

    Default:
        '1'

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codepipeline-actions.JenkinsProviderProps", jsii_struct_bases=[_JenkinsProviderProps])
class JenkinsProviderProps(_JenkinsProviderProps):
    """
    Stability:
        experimental
    """
    providerName: str
    """The name of the Jenkins provider that you set in the AWS CodePipeline plugin configuration of your Jenkins project.

    Stability:
        experimental

    Example::
        'MyJenkinsProvider'
    """

    serverUrl: str
    """The base URL of your Jenkins server.

    Stability:
        experimental

    Example::
        'http://myjenkins.com:8080'
    """

class LambdaInvokeAction(Action, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codepipeline-actions.LambdaInvokeAction"):
    """CodePipeline invoke Action that is provided by an AWS Lambda function.

    See:
        https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-invoke-lambda-function.html
    Stability:
        experimental
    """
    def __init__(self, *, lambda_: aws_cdk.aws_lambda.IFunction, inputs: typing.Optional[typing.List[aws_cdk.aws_codepipeline.Artifact]]=None, outputs: typing.Optional[typing.List[aws_cdk.aws_codepipeline.Artifact]]=None, user_parameters: typing.Optional[typing.Mapping[str,typing.Any]]=None, action_name: str, run_order: typing.Optional[jsii.Number]=None) -> None:
        """
        Arguments:
            props: -
            lambda_: The lambda function to invoke.
            inputs: The optional input Artifacts of the Action. A Lambda Action can have up to 5 inputs. The inputs will appear in the event passed to the Lambda, under the ``'CodePipeline.job'.data.inputArtifacts`` path. Default: the Action will not have any inputs
            outputs: The optional names of the output Artifacts of the Action. A Lambda Action can have up to 5 outputs. The outputs will appear in the event passed to the Lambda, under the ``'CodePipeline.job'.data.outputArtifacts`` path. It is the responsibility of the Lambda to upload ZIP files with the Artifact contents to the provided locations. Default: the Action will not have any outputs
            user_parameters: A set of key-value pairs that will be accessible to the invoked Lambda inside the event that the Pipeline will call it with.
            action_name: The physical, human-readable name of the Action. Not that Action names must be unique within a single Stage.
            run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1

        Stability:
            experimental
        """
        props: LambdaInvokeActionProps = {"lambda": lambda_, "actionName": action_name}

        if inputs is not None:
            props["inputs"] = inputs

        if outputs is not None:
            props["outputs"] = outputs

        if user_parameters is not None:
            props["userParameters"] = user_parameters

        if run_order is not None:
            props["runOrder"] = run_order

        jsii.create(LambdaInvokeAction, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(self, scope: aws_cdk.core.Construct, _stage: aws_cdk.aws_codepipeline.IStage, *, role: aws_cdk.aws_iam.IRole) -> aws_cdk.aws_codepipeline.ActionConfig:
        """The method called when an Action is attached to a Pipeline. This method is guaranteed to be called only once for each Action instance.

        Arguments:
            scope: -
            _stage: -
            options: -
            role: 

        Stability:
            experimental
        """
        options: aws_cdk.aws_codepipeline.ActionBindOptions = {"role": role}

        return jsii.invoke(self, "bound", [scope, _stage, options])


@jsii.data_type_optionals(jsii_struct_bases=[aws_cdk.aws_codepipeline.CommonActionProps])
class _LambdaInvokeActionProps(aws_cdk.aws_codepipeline.CommonActionProps, jsii.compat.TypedDict, total=False):
    inputs: typing.List[aws_cdk.aws_codepipeline.Artifact]
    """The optional input Artifacts of the Action. A Lambda Action can have up to 5 inputs. The inputs will appear in the event passed to the Lambda, under the ``'CodePipeline.job'.data.inputArtifacts`` path.

    Default:
        the Action will not have any inputs

    See:
        https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-invoke-lambda-function.html#actions-invoke-lambda-function-json-event-example
    Stability:
        experimental
    """
    outputs: typing.List[aws_cdk.aws_codepipeline.Artifact]
    """The optional names of the output Artifacts of the Action. A Lambda Action can have up to 5 outputs. The outputs will appear in the event passed to the Lambda, under the ``'CodePipeline.job'.data.outputArtifacts`` path. It is the responsibility of the Lambda to upload ZIP files with the Artifact contents to the provided locations.

    Default:
        the Action will not have any outputs

    Stability:
        experimental
    """
    userParameters: typing.Mapping[str,typing.Any]
    """A set of key-value pairs that will be accessible to the invoked Lambda inside the event that the Pipeline will call it with.

    See:
        https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-invoke-lambda-function.html#actions-invoke-lambda-function-json-event-example
    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codepipeline-actions.LambdaInvokeActionProps", jsii_struct_bases=[_LambdaInvokeActionProps])
class LambdaInvokeActionProps(_LambdaInvokeActionProps):
    """Construction properties of the {@link LambdaInvokeAction Lambda invoke CodePipeline Action}.

    Stability:
        experimental
    """
    lambda_: aws_cdk.aws_lambda.IFunction
    """The lambda function to invoke.

    Stability:
        experimental
    """

class ManualApprovalAction(Action, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codepipeline-actions.ManualApprovalAction"):
    """Manual approval action.

    Stability:
        experimental
    """
    def __init__(self, *, additional_information: typing.Optional[str]=None, notification_topic: typing.Optional[aws_cdk.aws_sns.ITopic]=None, notify_emails: typing.Optional[typing.List[str]]=None, action_name: str, run_order: typing.Optional[jsii.Number]=None) -> None:
        """
        Arguments:
            props: -
            additional_information: Any additional information that you want to include in the notification email message.
            notification_topic: Optional SNS topic to send notifications to when an approval is pending.
            notify_emails: A list of email addresses to subscribe to notifications when this Action is pending approval. If this has been provided, but not ``notificationTopic``, a new Topic will be created.
            action_name: The physical, human-readable name of the Action. Not that Action names must be unique within a single Stage.
            run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1

        Stability:
            experimental
        """
        props: ManualApprovalActionProps = {"actionName": action_name}

        if additional_information is not None:
            props["additionalInformation"] = additional_information

        if notification_topic is not None:
            props["notificationTopic"] = notification_topic

        if notify_emails is not None:
            props["notifyEmails"] = notify_emails

        if run_order is not None:
            props["runOrder"] = run_order

        jsii.create(ManualApprovalAction, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(self, scope: aws_cdk.core.Construct, _stage: aws_cdk.aws_codepipeline.IStage, *, role: aws_cdk.aws_iam.IRole) -> aws_cdk.aws_codepipeline.ActionConfig:
        """The method called when an Action is attached to a Pipeline. This method is guaranteed to be called only once for each Action instance.

        Arguments:
            scope: -
            _stage: -
            options: -
            role: 

        Stability:
            experimental
        """
        options: aws_cdk.aws_codepipeline.ActionBindOptions = {"role": role}

        return jsii.invoke(self, "bound", [scope, _stage, options])

    @property
    @jsii.member(jsii_name="notificationTopic")
    def notification_topic(self) -> typing.Optional[aws_cdk.aws_sns.ITopic]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "notificationTopic")


@jsii.data_type(jsii_type="@aws-cdk/aws-codepipeline-actions.ManualApprovalActionProps", jsii_struct_bases=[aws_cdk.aws_codepipeline.CommonActionProps])
class ManualApprovalActionProps(aws_cdk.aws_codepipeline.CommonActionProps, jsii.compat.TypedDict, total=False):
    """Construction properties of the {@link ManualApprovalAction}.

    Stability:
        experimental
    """
    additionalInformation: str
    """Any additional information that you want to include in the notification email message.

    Stability:
        experimental
    """

    notificationTopic: aws_cdk.aws_sns.ITopic
    """Optional SNS topic to send notifications to when an approval is pending.

    Stability:
        experimental
    """

    notifyEmails: typing.List[str]
    """A list of email addresses to subscribe to notifications when this Action is pending approval. If this has been provided, but not ``notificationTopic``, a new Topic will be created.

    Stability:
        experimental
    """

class S3DeployAction(Action, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codepipeline-actions.S3DeployAction"):
    """Deploys the sourceArtifact to Amazon S3.

    Stability:
        experimental
    """
    def __init__(self, *, bucket: aws_cdk.aws_s3.IBucket, input: aws_cdk.aws_codepipeline.Artifact, extract: typing.Optional[bool]=None, object_key: typing.Optional[str]=None, action_name: str, run_order: typing.Optional[jsii.Number]=None) -> None:
        """
        Arguments:
            props: -
            bucket: The Amazon S3 bucket that is the deploy target.
            input: The input Artifact to deploy to Amazon S3.
            extract: Should the deploy action extract the artifact before deploying to Amazon S3. Default: true
            object_key: The key of the target object. This is required if extract is false.
            action_name: The physical, human-readable name of the Action. Not that Action names must be unique within a single Stage.
            run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1

        Stability:
            experimental
        """
        props: S3DeployActionProps = {"bucket": bucket, "input": input, "actionName": action_name}

        if extract is not None:
            props["extract"] = extract

        if object_key is not None:
            props["objectKey"] = object_key

        if run_order is not None:
            props["runOrder"] = run_order

        jsii.create(S3DeployAction, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(self, _scope: aws_cdk.core.Construct, _stage: aws_cdk.aws_codepipeline.IStage, *, role: aws_cdk.aws_iam.IRole) -> aws_cdk.aws_codepipeline.ActionConfig:
        """The method called when an Action is attached to a Pipeline. This method is guaranteed to be called only once for each Action instance.

        Arguments:
            _scope: -
            _stage: -
            options: -
            role: 

        Stability:
            experimental
        """
        options: aws_cdk.aws_codepipeline.ActionBindOptions = {"role": role}

        return jsii.invoke(self, "bound", [_scope, _stage, options])


@jsii.data_type_optionals(jsii_struct_bases=[aws_cdk.aws_codepipeline.CommonActionProps])
class _S3DeployActionProps(aws_cdk.aws_codepipeline.CommonActionProps, jsii.compat.TypedDict, total=False):
    extract: bool
    """Should the deploy action extract the artifact before deploying to Amazon S3.

    Default:
        true

    Stability:
        experimental
    """
    objectKey: str
    """The key of the target object.

    This is required if extract is false.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codepipeline-actions.S3DeployActionProps", jsii_struct_bases=[_S3DeployActionProps])
class S3DeployActionProps(_S3DeployActionProps):
    """Construction properties of the {@link S3DeployAction S3 deploy Action}.

    Stability:
        experimental
    """
    bucket: aws_cdk.aws_s3.IBucket
    """The Amazon S3 bucket that is the deploy target.

    Stability:
        experimental
    """

    input: aws_cdk.aws_codepipeline.Artifact
    """The input Artifact to deploy to Amazon S3.

    Stability:
        experimental
    """

class S3SourceAction(Action, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-codepipeline-actions.S3SourceAction"):
    """Source that is provided by a specific Amazon S3 object.

    Will trigger the pipeline as soon as the S3 object changes, but only if there is
    a CloudTrail Trail in the account that captures the S3 event.

    Stability:
        experimental
    """
    def __init__(self, *, bucket: aws_cdk.aws_s3.IBucket, bucket_key: str, output: aws_cdk.aws_codepipeline.Artifact, trigger: typing.Optional["S3Trigger"]=None, action_name: str, run_order: typing.Optional[jsii.Number]=None) -> None:
        """
        Arguments:
            props: -
            bucket: The Amazon S3 bucket that stores the source code.
            bucket_key: The key within the S3 bucket that stores the source code.
            output: 
            trigger: How should CodePipeline detect source changes for this Action. Note that if this is S3Trigger.EVENTS, you need to make sure to include the source Bucket in a CloudTrail Trail, as otherwise the CloudWatch Events will not be emitted. Default: S3Trigger.POLL
            action_name: The physical, human-readable name of the Action. Not that Action names must be unique within a single Stage.
            run_order: The runOrder property for this Action. RunOrder determines the relative order in which multiple Actions in the same Stage execute. Default: 1

        Stability:
            experimental
        """
        props: S3SourceActionProps = {"bucket": bucket, "bucketKey": bucket_key, "output": output, "actionName": action_name}

        if trigger is not None:
            props["trigger"] = trigger

        if run_order is not None:
            props["runOrder"] = run_order

        jsii.create(S3SourceAction, self, [props])

    @jsii.member(jsii_name="bound")
    def _bound(self, _scope: aws_cdk.core.Construct, stage: aws_cdk.aws_codepipeline.IStage, *, role: aws_cdk.aws_iam.IRole) -> aws_cdk.aws_codepipeline.ActionConfig:
        """The method called when an Action is attached to a Pipeline. This method is guaranteed to be called only once for each Action instance.

        Arguments:
            _scope: -
            stage: -
            options: -
            role: 

        Stability:
            experimental
        """
        options: aws_cdk.aws_codepipeline.ActionBindOptions = {"role": role}

        return jsii.invoke(self, "bound", [_scope, stage, options])


@jsii.data_type_optionals(jsii_struct_bases=[aws_cdk.aws_codepipeline.CommonActionProps])
class _S3SourceActionProps(aws_cdk.aws_codepipeline.CommonActionProps, jsii.compat.TypedDict, total=False):
    trigger: "S3Trigger"
    """How should CodePipeline detect source changes for this Action. Note that if this is S3Trigger.EVENTS, you need to make sure to include the source Bucket in a CloudTrail Trail, as otherwise the CloudWatch Events will not be emitted.

    Default:
        S3Trigger.POLL

    See:
        https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/log-s3-data-events.html
    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-codepipeline-actions.S3SourceActionProps", jsii_struct_bases=[_S3SourceActionProps])
class S3SourceActionProps(_S3SourceActionProps):
    """Construction properties of the {@link S3SourceAction S3 source Action}.

    Stability:
        experimental
    """
    bucket: aws_cdk.aws_s3.IBucket
    """The Amazon S3 bucket that stores the source code.

    Stability:
        experimental
    """

    bucketKey: str
    """The key within the S3 bucket that stores the source code.

    Stability:
        experimental

    Example::
        'path/to/file.zip'
    """

    output: aws_cdk.aws_codepipeline.Artifact
    """
    Stability:
        experimental
    """

@jsii.enum(jsii_type="@aws-cdk/aws-codepipeline-actions.S3Trigger")
class S3Trigger(enum.Enum):
    """How should the S3 Action detect changes. This is the type of the {@link S3SourceAction.trigger} property.

    Stability:
        experimental
    """
    NONE = "NONE"
    """The Action will never detect changes - the Pipeline it's part of will only begin a run when explicitly started.

    Stability:
        experimental
    """
    POLL = "POLL"
    """CodePipeline will poll S3 to detect changes. This is the default method of detecting changes.

    Stability:
        experimental
    """
    EVENTS = "EVENTS"
    """CodePipeline will use CloudWatch Events to be notified of changes. Note that the Bucket that the Action uses needs to be part of a CloudTrail Trail for the events to be delivered.

    Stability:
        experimental
    """

__all__ = ["Action", "AlexaSkillDeployAction", "AlexaSkillDeployActionProps", "BaseJenkinsProvider", "CloudFormationCreateReplaceChangeSetAction", "CloudFormationCreateReplaceChangeSetActionProps", "CloudFormationCreateUpdateStackAction", "CloudFormationCreateUpdateStackActionProps", "CloudFormationDeleteStackAction", "CloudFormationDeleteStackActionProps", "CloudFormationExecuteChangeSetAction", "CloudFormationExecuteChangeSetActionProps", "CodeBuildAction", "CodeBuildActionProps", "CodeBuildActionType", "CodeCommitSourceAction", "CodeCommitSourceActionProps", "CodeCommitTrigger", "CodeDeployServerDeployAction", "CodeDeployServerDeployActionProps", "EcrSourceAction", "EcrSourceActionProps", "EcsDeployAction", "EcsDeployActionProps", "GitHubSourceAction", "GitHubSourceActionProps", "GitHubTrigger", "IJenkinsProvider", "JenkinsAction", "JenkinsActionProps", "JenkinsActionType", "JenkinsProvider", "JenkinsProviderAttributes", "JenkinsProviderProps", "LambdaInvokeAction", "LambdaInvokeActionProps", "ManualApprovalAction", "ManualApprovalActionProps", "S3DeployAction", "S3DeployActionProps", "S3SourceAction", "S3SourceActionProps", "S3Trigger", "__jsii_assembly__"]

publication.publish()
