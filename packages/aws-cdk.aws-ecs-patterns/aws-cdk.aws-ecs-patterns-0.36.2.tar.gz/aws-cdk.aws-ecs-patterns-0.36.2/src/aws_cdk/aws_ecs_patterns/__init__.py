import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.aws_applicationautoscaling
import aws_cdk.aws_certificatemanager
import aws_cdk.aws_ec2
import aws_cdk.aws_ecs
import aws_cdk.aws_elasticloadbalancingv2
import aws_cdk.aws_events
import aws_cdk.aws_events_targets
import aws_cdk.aws_iam
import aws_cdk.aws_route53
import aws_cdk.aws_route53_targets
import aws_cdk.aws_sqs
import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-ecs-patterns", "0.36.2", __name__, "aws-ecs-patterns@0.36.2.jsii.tgz")
class LoadBalancedServiceBase(aws_cdk.core.Construct, metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-ecs-patterns.LoadBalancedServiceBase"):
    """Base class for load-balanced Fargate and ECS services.

    Stability:
        experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _LoadBalancedServiceBaseProxy

    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, cluster: aws_cdk.aws_ecs.ICluster, image: aws_cdk.aws_ecs.ContainerImage, certificate: typing.Optional[aws_cdk.aws_certificatemanager.ICertificate]=None, container_port: typing.Optional[jsii.Number]=None, desired_count: typing.Optional[jsii.Number]=None, domain_name: typing.Optional[str]=None, domain_zone: typing.Optional[aws_cdk.aws_route53.IHostedZone]=None, enable_logging: typing.Optional[bool]=None, environment: typing.Optional[typing.Mapping[str,str]]=None, load_balancer_type: typing.Optional["LoadBalancerType"]=None, public_load_balancer: typing.Optional[bool]=None, public_tasks: typing.Optional[bool]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            cluster: The cluster where your service will be deployed.
            image: The image to start.
            certificate: Certificate Manager certificate to associate with the load balancer. Setting this option will set the load balancer port to 443. Default: - No certificate associated with the load balancer.
            container_port: The container port of the application load balancer attached to your Fargate service. Corresponds to container port mapping. Default: 80
            desired_count: Number of desired copies of running tasks. Default: 1
            domain_name: Domain name for the service, e.g. api.example.com. Default: - No domain name.
            domain_zone: Route53 hosted zone for the domain, e.g. "example.com.". Default: - No Route53 hosted domain zone.
            enable_logging: Whether to create an AWS log driver. Default: true
            environment: Environment variables to pass to the container. Default: - No environment variables.
            load_balancer_type: Whether to create an application load balancer or a network load balancer. Default: application
            public_load_balancer: Determines whether the Application Load Balancer will be internet-facing. Default: true
            public_tasks: Determines whether your Fargate Service will be assigned a public IP address. Default: false

        Stability:
            experimental
        """
        props: LoadBalancedServiceBaseProps = {"cluster": cluster, "image": image}

        if certificate is not None:
            props["certificate"] = certificate

        if container_port is not None:
            props["containerPort"] = container_port

        if desired_count is not None:
            props["desiredCount"] = desired_count

        if domain_name is not None:
            props["domainName"] = domain_name

        if domain_zone is not None:
            props["domainZone"] = domain_zone

        if enable_logging is not None:
            props["enableLogging"] = enable_logging

        if environment is not None:
            props["environment"] = environment

        if load_balancer_type is not None:
            props["loadBalancerType"] = load_balancer_type

        if public_load_balancer is not None:
            props["publicLoadBalancer"] = public_load_balancer

        if public_tasks is not None:
            props["publicTasks"] = public_tasks

        jsii.create(LoadBalancedServiceBase, self, [scope, id, props])

    @jsii.member(jsii_name="addServiceAsTarget")
    def _add_service_as_target(self, service: aws_cdk.aws_ecs.BaseService) -> None:
        """
        Arguments:
            service: -

        Stability:
            experimental
        """
        return jsii.invoke(self, "addServiceAsTarget", [service])

    @property
    @jsii.member(jsii_name="listener")
    def listener(self) -> typing.Union[aws_cdk.aws_elasticloadbalancingv2.ApplicationListener, aws_cdk.aws_elasticloadbalancingv2.NetworkListener]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "listener")

    @property
    @jsii.member(jsii_name="loadBalancer")
    def load_balancer(self) -> aws_cdk.aws_elasticloadbalancingv2.BaseLoadBalancer:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "loadBalancer")

    @property
    @jsii.member(jsii_name="loadBalancerType")
    def load_balancer_type(self) -> "LoadBalancerType":
        """
        Stability:
            experimental
        """
        return jsii.get(self, "loadBalancerType")

    @property
    @jsii.member(jsii_name="targetGroup")
    def target_group(self) -> typing.Union[aws_cdk.aws_elasticloadbalancingv2.ApplicationTargetGroup, aws_cdk.aws_elasticloadbalancingv2.NetworkTargetGroup]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "targetGroup")

    @property
    @jsii.member(jsii_name="logDriver")
    def log_driver(self) -> typing.Optional[aws_cdk.aws_ecs.LogDriver]:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "logDriver")


class _LoadBalancedServiceBaseProxy(LoadBalancedServiceBase):
    pass

class LoadBalancedEc2Service(LoadBalancedServiceBase, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ecs-patterns.LoadBalancedEc2Service"):
    """A single task running on an ECS cluster fronted by a load balancer.

    Stability:
        experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, memory_limit_mi_b: typing.Optional[jsii.Number]=None, memory_reservation_mi_b: typing.Optional[jsii.Number]=None, cluster: aws_cdk.aws_ecs.ICluster, image: aws_cdk.aws_ecs.ContainerImage, certificate: typing.Optional[aws_cdk.aws_certificatemanager.ICertificate]=None, container_port: typing.Optional[jsii.Number]=None, desired_count: typing.Optional[jsii.Number]=None, domain_name: typing.Optional[str]=None, domain_zone: typing.Optional[aws_cdk.aws_route53.IHostedZone]=None, enable_logging: typing.Optional[bool]=None, environment: typing.Optional[typing.Mapping[str,str]]=None, load_balancer_type: typing.Optional["LoadBalancerType"]=None, public_load_balancer: typing.Optional[bool]=None, public_tasks: typing.Optional[bool]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            memory_limit_mi_b: The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the allocated memory, the container is terminated. At least one of memoryLimitMiB and memoryReservationMiB is required. Default: - No memory limit.
            memory_reservation_mi_b: The soft limit (in MiB) of memory to reserve for the container. When system memory is under contention, Docker attempts to keep the container memory within the limit. If the container requires more memory, it can consume up to the value specified by the Memory property or all of the available memory on the container instance—whichever comes first. At least one of memoryLimitMiB and memoryReservationMiB is required. Default: - No memory reserved.
            cluster: The cluster where your service will be deployed.
            image: The image to start.
            certificate: Certificate Manager certificate to associate with the load balancer. Setting this option will set the load balancer port to 443. Default: - No certificate associated with the load balancer.
            container_port: The container port of the application load balancer attached to your Fargate service. Corresponds to container port mapping. Default: 80
            desired_count: Number of desired copies of running tasks. Default: 1
            domain_name: Domain name for the service, e.g. api.example.com. Default: - No domain name.
            domain_zone: Route53 hosted zone for the domain, e.g. "example.com.". Default: - No Route53 hosted domain zone.
            enable_logging: Whether to create an AWS log driver. Default: true
            environment: Environment variables to pass to the container. Default: - No environment variables.
            load_balancer_type: Whether to create an application load balancer or a network load balancer. Default: application
            public_load_balancer: Determines whether the Application Load Balancer will be internet-facing. Default: true
            public_tasks: Determines whether your Fargate Service will be assigned a public IP address. Default: false

        Stability:
            experimental
        """
        props: LoadBalancedEc2ServiceProps = {"cluster": cluster, "image": image}

        if memory_limit_mi_b is not None:
            props["memoryLimitMiB"] = memory_limit_mi_b

        if memory_reservation_mi_b is not None:
            props["memoryReservationMiB"] = memory_reservation_mi_b

        if certificate is not None:
            props["certificate"] = certificate

        if container_port is not None:
            props["containerPort"] = container_port

        if desired_count is not None:
            props["desiredCount"] = desired_count

        if domain_name is not None:
            props["domainName"] = domain_name

        if domain_zone is not None:
            props["domainZone"] = domain_zone

        if enable_logging is not None:
            props["enableLogging"] = enable_logging

        if environment is not None:
            props["environment"] = environment

        if load_balancer_type is not None:
            props["loadBalancerType"] = load_balancer_type

        if public_load_balancer is not None:
            props["publicLoadBalancer"] = public_load_balancer

        if public_tasks is not None:
            props["publicTasks"] = public_tasks

        jsii.create(LoadBalancedEc2Service, self, [scope, id, props])

    @property
    @jsii.member(jsii_name="service")
    def service(self) -> aws_cdk.aws_ecs.Ec2Service:
        """The ECS service in this construct.

        Stability:
            experimental
        """
        return jsii.get(self, "service")


class LoadBalancedFargateService(LoadBalancedServiceBase, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ecs-patterns.LoadBalancedFargateService"):
    """A Fargate service running on an ECS cluster fronted by a load balancer.

    Stability:
        experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, container_name: typing.Optional[str]=None, cpu: typing.Optional[jsii.Number]=None, execution_role: typing.Optional[aws_cdk.aws_iam.IRole]=None, memory_limit_mi_b: typing.Optional[jsii.Number]=None, service_name: typing.Optional[str]=None, task_role: typing.Optional[aws_cdk.aws_iam.IRole]=None, cluster: aws_cdk.aws_ecs.ICluster, image: aws_cdk.aws_ecs.ContainerImage, certificate: typing.Optional[aws_cdk.aws_certificatemanager.ICertificate]=None, container_port: typing.Optional[jsii.Number]=None, desired_count: typing.Optional[jsii.Number]=None, domain_name: typing.Optional[str]=None, domain_zone: typing.Optional[aws_cdk.aws_route53.IHostedZone]=None, enable_logging: typing.Optional[bool]=None, environment: typing.Optional[typing.Mapping[str,str]]=None, load_balancer_type: typing.Optional["LoadBalancerType"]=None, public_load_balancer: typing.Optional[bool]=None, public_tasks: typing.Optional[bool]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            container_name: Override value for the container name. Default: - No value
            cpu: The number of cpu units used by the task. Valid values, which determines your range of valid values for the memory parameter: 256 (.25 vCPU) - Available memory values: 0.5GB, 1GB, 2GB 512 (.5 vCPU) - Available memory values: 1GB, 2GB, 3GB, 4GB 1024 (1 vCPU) - Available memory values: 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB 2048 (2 vCPU) - Available memory values: Between 4GB and 16GB in 1GB increments 4096 (4 vCPU) - Available memory values: Between 8GB and 30GB in 1GB increments. This default is set in the underlying FargateTaskDefinition construct. Default: 256
            execution_role: Override for the Fargate Task Definition execution role. Default: - No value
            memory_limit_mi_b: The amount (in MiB) of memory used by the task. This field is required and you must use one of the following values, which determines your range of valid values for the cpu parameter: 0.5GB, 1GB, 2GB - Available cpu values: 256 (.25 vCPU) 1GB, 2GB, 3GB, 4GB - Available cpu values: 512 (.5 vCPU) 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB - Available cpu values: 1024 (1 vCPU) Between 4GB and 16GB in 1GB increments - Available cpu values: 2048 (2 vCPU) Between 8GB and 30GB in 1GB increments - Available cpu values: 4096 (4 vCPU) This default is set in the underlying FargateTaskDefinition construct. Default: 512
            service_name: Override value for the service name. Default: CloudFormation-generated name
            task_role: Override for the Fargate Task Definition task role. Default: - No value
            cluster: The cluster where your service will be deployed.
            image: The image to start.
            certificate: Certificate Manager certificate to associate with the load balancer. Setting this option will set the load balancer port to 443. Default: - No certificate associated with the load balancer.
            container_port: The container port of the application load balancer attached to your Fargate service. Corresponds to container port mapping. Default: 80
            desired_count: Number of desired copies of running tasks. Default: 1
            domain_name: Domain name for the service, e.g. api.example.com. Default: - No domain name.
            domain_zone: Route53 hosted zone for the domain, e.g. "example.com.". Default: - No Route53 hosted domain zone.
            enable_logging: Whether to create an AWS log driver. Default: true
            environment: Environment variables to pass to the container. Default: - No environment variables.
            load_balancer_type: Whether to create an application load balancer or a network load balancer. Default: application
            public_load_balancer: Determines whether the Application Load Balancer will be internet-facing. Default: true
            public_tasks: Determines whether your Fargate Service will be assigned a public IP address. Default: false

        Stability:
            experimental
        """
        props: LoadBalancedFargateServiceProps = {"cluster": cluster, "image": image}

        if container_name is not None:
            props["containerName"] = container_name

        if cpu is not None:
            props["cpu"] = cpu

        if execution_role is not None:
            props["executionRole"] = execution_role

        if memory_limit_mi_b is not None:
            props["memoryLimitMiB"] = memory_limit_mi_b

        if service_name is not None:
            props["serviceName"] = service_name

        if task_role is not None:
            props["taskRole"] = task_role

        if certificate is not None:
            props["certificate"] = certificate

        if container_port is not None:
            props["containerPort"] = container_port

        if desired_count is not None:
            props["desiredCount"] = desired_count

        if domain_name is not None:
            props["domainName"] = domain_name

        if domain_zone is not None:
            props["domainZone"] = domain_zone

        if enable_logging is not None:
            props["enableLogging"] = enable_logging

        if environment is not None:
            props["environment"] = environment

        if load_balancer_type is not None:
            props["loadBalancerType"] = load_balancer_type

        if public_load_balancer is not None:
            props["publicLoadBalancer"] = public_load_balancer

        if public_tasks is not None:
            props["publicTasks"] = public_tasks

        jsii.create(LoadBalancedFargateService, self, [scope, id, props])

    @property
    @jsii.member(jsii_name="service")
    def service(self) -> aws_cdk.aws_ecs.FargateService:
        """The Fargate service in this construct.

        Stability:
            experimental
        """
        return jsii.get(self, "service")


@jsii.data_type_optionals(jsii_struct_bases=[])
class _LoadBalancedServiceBaseProps(jsii.compat.TypedDict, total=False):
    certificate: aws_cdk.aws_certificatemanager.ICertificate
    """Certificate Manager certificate to associate with the load balancer. Setting this option will set the load balancer port to 443.

    Default:
        - No certificate associated with the load balancer.

    Stability:
        experimental
    """
    containerPort: jsii.Number
    """The container port of the application load balancer attached to your Fargate service.

    Corresponds to container port mapping.

    Default:
        80

    Stability:
        experimental
    """
    desiredCount: jsii.Number
    """Number of desired copies of running tasks.

    Default:
        1

    Stability:
        experimental
    """
    domainName: str
    """Domain name for the service, e.g. api.example.com.

    Default:
        - No domain name.

    Stability:
        experimental
    """
    domainZone: aws_cdk.aws_route53.IHostedZone
    """Route53 hosted zone for the domain, e.g. "example.com.".

    Default:
        - No Route53 hosted domain zone.

    Stability:
        experimental
    """
    enableLogging: bool
    """Whether to create an AWS log driver.

    Default:
        true

    Stability:
        experimental
    """
    environment: typing.Mapping[str,str]
    """Environment variables to pass to the container.

    Default:
        - No environment variables.

    Stability:
        experimental
    """
    loadBalancerType: "LoadBalancerType"
    """Whether to create an application load balancer or a network load balancer.

    Default:
        application

    Stability:
        experimental
    """
    publicLoadBalancer: bool
    """Determines whether the Application Load Balancer will be internet-facing.

    Default:
        true

    Stability:
        experimental
    """
    publicTasks: bool
    """Determines whether your Fargate Service will be assigned a public IP address.

    Default:
        false

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-ecs-patterns.LoadBalancedServiceBaseProps", jsii_struct_bases=[_LoadBalancedServiceBaseProps])
class LoadBalancedServiceBaseProps(_LoadBalancedServiceBaseProps):
    """Base properties for load-balanced Fargate and ECS services.

    Stability:
        experimental
    """
    cluster: aws_cdk.aws_ecs.ICluster
    """The cluster where your service will be deployed.

    Stability:
        experimental
    """

    image: aws_cdk.aws_ecs.ContainerImage
    """The image to start.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-ecs-patterns.LoadBalancedEc2ServiceProps", jsii_struct_bases=[LoadBalancedServiceBaseProps])
class LoadBalancedEc2ServiceProps(LoadBalancedServiceBaseProps, jsii.compat.TypedDict, total=False):
    """Properties for a LoadBalancedEc2Service.

    Stability:
        experimental
    """
    memoryLimitMiB: jsii.Number
    """The hard limit (in MiB) of memory to present to the container.

    If your container attempts to exceed the allocated memory, the container
    is terminated.

    At least one of memoryLimitMiB and memoryReservationMiB is required.

    Default:
        - No memory limit.

    Stability:
        experimental
    """

    memoryReservationMiB: jsii.Number
    """The soft limit (in MiB) of memory to reserve for the container.

    When system memory is under contention, Docker attempts to keep the
    container memory within the limit. If the container requires more memory,
    it can consume up to the value specified by the Memory property or all of
    the available memory on the container instance—whichever comes first.

    At least one of memoryLimitMiB and memoryReservationMiB is required.

    Default:
        - No memory reserved.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-ecs-patterns.LoadBalancedFargateServiceProps", jsii_struct_bases=[LoadBalancedServiceBaseProps])
class LoadBalancedFargateServiceProps(LoadBalancedServiceBaseProps, jsii.compat.TypedDict, total=False):
    """Properties for a LoadBalancedFargateService.

    Stability:
        experimental
    """
    containerName: str
    """Override value for the container name.

    Default:
        - No value

    Stability:
        experimental
    """

    cpu: jsii.Number
    """The number of cpu units used by the task. Valid values, which determines your range of valid values for the memory parameter: 256 (.25 vCPU) - Available memory values: 0.5GB, 1GB, 2GB 512 (.5 vCPU) - Available memory values: 1GB, 2GB, 3GB, 4GB 1024 (1 vCPU) - Available memory values: 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB 2048 (2 vCPU) - Available memory values: Between 4GB and 16GB in 1GB increments 4096 (4 vCPU) - Available memory values: Between 8GB and 30GB in 1GB increments.

    This default is set in the underlying FargateTaskDefinition construct.

    Default:
        256

    Stability:
        experimental
    """

    executionRole: aws_cdk.aws_iam.IRole
    """Override for the Fargate Task Definition execution role.

    Default:
        - No value

    Stability:
        experimental
    """

    memoryLimitMiB: jsii.Number
    """The amount (in MiB) of memory used by the task.

    This field is required and you must use one of the following values, which determines your range of valid values
    for the cpu parameter:

    0.5GB, 1GB, 2GB - Available cpu values: 256 (.25 vCPU)

    1GB, 2GB, 3GB, 4GB - Available cpu values: 512 (.5 vCPU)

    2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB - Available cpu values: 1024 (1 vCPU)

    Between 4GB and 16GB in 1GB increments - Available cpu values: 2048 (2 vCPU)

    Between 8GB and 30GB in 1GB increments - Available cpu values: 4096 (4 vCPU)

    This default is set in the underlying FargateTaskDefinition construct.

    Default:
        512

    Stability:
        experimental
    """

    serviceName: str
    """Override value for the service name.

    Default:
        CloudFormation-generated name

    Stability:
        experimental
    """

    taskRole: aws_cdk.aws_iam.IRole
    """Override for the Fargate Task Definition task role.

    Default:
        - No value

    Stability:
        experimental
    """

@jsii.enum(jsii_type="@aws-cdk/aws-ecs-patterns.LoadBalancerType")
class LoadBalancerType(enum.Enum):
    """
    Stability:
        experimental
    """
    APPLICATION = "APPLICATION"
    """
    Stability:
        experimental
    """
    NETWORK = "NETWORK"
    """
    Stability:
        experimental
    """

class QueueProcessingServiceBase(aws_cdk.core.Construct, metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-ecs-patterns.QueueProcessingServiceBase"):
    """Base class for a Fargate and ECS queue processing service.

    Stability:
        experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _QueueProcessingServiceBaseProxy

    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, cluster: aws_cdk.aws_ecs.ICluster, image: aws_cdk.aws_ecs.ContainerImage, command: typing.Optional[typing.List[str]]=None, desired_task_count: typing.Optional[jsii.Number]=None, enable_logging: typing.Optional[bool]=None, environment: typing.Optional[typing.Mapping[str,str]]=None, max_scaling_capacity: typing.Optional[jsii.Number]=None, queue: typing.Optional[aws_cdk.aws_sqs.IQueue]=None, scaling_steps: typing.Optional[typing.List[aws_cdk.aws_applicationautoscaling.ScalingInterval]]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            cluster: Cluster where service will be deployed.
            image: The image to start.
            command: The CMD value to pass to the container. A string with commands delimited by commas. Default: none
            desired_task_count: Number of desired copies of running tasks. Default: 1
            enable_logging: Flag to indicate whether to enable logging. Default: true
            environment: The environment variables to pass to the container. Default: 'QUEUE_NAME: queue.queueName'
            max_scaling_capacity: Maximum capacity to scale to. Default: (desiredTaskCount * 2)
            queue: A queue for which to process items from. If specified and this is a FIFO queue, the queue name must end in the string '.fifo'. Default: 'SQSQueue with CloudFormation-generated name'
            scaling_steps: The intervals for scaling based on the SQS queue's ApproximateNumberOfMessagesVisible metric. Maps a range of metric values to a particular scaling behavior. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html Default: [{ upper: 0, change: -1 },{ lower: 100, change: +1 },{ lower: 500, change: +5 }]

        Stability:
            experimental
        """
        props: QueueProcessingServiceBaseProps = {"cluster": cluster, "image": image}

        if command is not None:
            props["command"] = command

        if desired_task_count is not None:
            props["desiredTaskCount"] = desired_task_count

        if enable_logging is not None:
            props["enableLogging"] = enable_logging

        if environment is not None:
            props["environment"] = environment

        if max_scaling_capacity is not None:
            props["maxScalingCapacity"] = max_scaling_capacity

        if queue is not None:
            props["queue"] = queue

        if scaling_steps is not None:
            props["scalingSteps"] = scaling_steps

        jsii.create(QueueProcessingServiceBase, self, [scope, id, props])

    @jsii.member(jsii_name="configureAutoscalingForService")
    def _configure_autoscaling_for_service(self, service: aws_cdk.aws_ecs.BaseService) -> None:
        """Configure autoscaling based off of CPU utilization as well as the number of messages visible in the SQS queue.

        Arguments:
            service: the ECS/Fargate service for which to apply the autoscaling rules to.

        Stability:
            experimental
        """
        return jsii.invoke(self, "configureAutoscalingForService", [service])

    @property
    @jsii.member(jsii_name="desiredCount")
    def desired_count(self) -> jsii.Number:
        """The minimum number of tasks to run.

        Stability:
            experimental
        """
        return jsii.get(self, "desiredCount")

    @property
    @jsii.member(jsii_name="environment")
    def environment(self) -> typing.Mapping[str,str]:
        """Environment variables that will include the queue name.

        Stability:
            experimental
        """
        return jsii.get(self, "environment")

    @property
    @jsii.member(jsii_name="maxCapacity")
    def max_capacity(self) -> jsii.Number:
        """The maximum number of instances for autoscaling to scale up to.

        Stability:
            experimental
        """
        return jsii.get(self, "maxCapacity")

    @property
    @jsii.member(jsii_name="scalingSteps")
    def scaling_steps(self) -> typing.List[aws_cdk.aws_applicationautoscaling.ScalingInterval]:
        """The scaling interval for autoscaling based off an SQS Queue size.

        Stability:
            experimental
        """
        return jsii.get(self, "scalingSteps")

    @property
    @jsii.member(jsii_name="sqsQueue")
    def sqs_queue(self) -> aws_cdk.aws_sqs.IQueue:
        """The SQS queue that the service will process from.

        Stability:
            experimental
        """
        return jsii.get(self, "sqsQueue")

    @property
    @jsii.member(jsii_name="logDriver")
    def log_driver(self) -> typing.Optional[aws_cdk.aws_ecs.LogDriver]:
        """The AwsLogDriver to use for logging if logging is enabled.

        Stability:
            experimental
        """
        return jsii.get(self, "logDriver")


class _QueueProcessingServiceBaseProxy(QueueProcessingServiceBase):
    pass

class QueueProcessingEc2Service(QueueProcessingServiceBase, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ecs-patterns.QueueProcessingEc2Service"):
    """Class to create a queue processing Ec2 service.

    Stability:
        experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, cpu: typing.Optional[jsii.Number]=None, memory_limit_mi_b: typing.Optional[jsii.Number]=None, memory_reservation_mi_b: typing.Optional[jsii.Number]=None, cluster: aws_cdk.aws_ecs.ICluster, image: aws_cdk.aws_ecs.ContainerImage, command: typing.Optional[typing.List[str]]=None, desired_task_count: typing.Optional[jsii.Number]=None, enable_logging: typing.Optional[bool]=None, environment: typing.Optional[typing.Mapping[str,str]]=None, max_scaling_capacity: typing.Optional[jsii.Number]=None, queue: typing.Optional[aws_cdk.aws_sqs.IQueue]=None, scaling_steps: typing.Optional[typing.List[aws_cdk.aws_applicationautoscaling.ScalingInterval]]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            cpu: The minimum number of CPU units to reserve for the container. Default: - No minimum CPU units reserved.
            memory_limit_mi_b: The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the allocated memory, the container is terminated. At least one of memoryLimitMiB and memoryReservationMiB is required for non-Fargate services. Default: - No memory limit.
            memory_reservation_mi_b: The soft limit (in MiB) of memory to reserve for the container. When system memory is under contention, Docker attempts to keep the container memory within the limit. If the container requires more memory, it can consume up to the value specified by the Memory property or all of the available memory on the container instance—whichever comes first. At least one of memoryLimitMiB and memoryReservationMiB is required for non-Fargate services. Default: - No memory reserved.
            cluster: Cluster where service will be deployed.
            image: The image to start.
            command: The CMD value to pass to the container. A string with commands delimited by commas. Default: none
            desired_task_count: Number of desired copies of running tasks. Default: 1
            enable_logging: Flag to indicate whether to enable logging. Default: true
            environment: The environment variables to pass to the container. Default: 'QUEUE_NAME: queue.queueName'
            max_scaling_capacity: Maximum capacity to scale to. Default: (desiredTaskCount * 2)
            queue: A queue for which to process items from. If specified and this is a FIFO queue, the queue name must end in the string '.fifo'. Default: 'SQSQueue with CloudFormation-generated name'
            scaling_steps: The intervals for scaling based on the SQS queue's ApproximateNumberOfMessagesVisible metric. Maps a range of metric values to a particular scaling behavior. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html Default: [{ upper: 0, change: -1 },{ lower: 100, change: +1 },{ lower: 500, change: +5 }]

        Stability:
            experimental
        """
        props: QueueProcessingEc2ServiceProps = {"cluster": cluster, "image": image}

        if cpu is not None:
            props["cpu"] = cpu

        if memory_limit_mi_b is not None:
            props["memoryLimitMiB"] = memory_limit_mi_b

        if memory_reservation_mi_b is not None:
            props["memoryReservationMiB"] = memory_reservation_mi_b

        if command is not None:
            props["command"] = command

        if desired_task_count is not None:
            props["desiredTaskCount"] = desired_task_count

        if enable_logging is not None:
            props["enableLogging"] = enable_logging

        if environment is not None:
            props["environment"] = environment

        if max_scaling_capacity is not None:
            props["maxScalingCapacity"] = max_scaling_capacity

        if queue is not None:
            props["queue"] = queue

        if scaling_steps is not None:
            props["scalingSteps"] = scaling_steps

        jsii.create(QueueProcessingEc2Service, self, [scope, id, props])

    @property
    @jsii.member(jsii_name="service")
    def service(self) -> aws_cdk.aws_ecs.Ec2Service:
        """The ECS service in this construct.

        Stability:
            experimental
        """
        return jsii.get(self, "service")


class QueueProcessingFargateService(QueueProcessingServiceBase, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ecs-patterns.QueueProcessingFargateService"):
    """Class to create a queue processing Fargate service.

    Stability:
        experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, cpu: typing.Optional[jsii.Number]=None, memory_limit_mi_b: typing.Optional[jsii.Number]=None, cluster: aws_cdk.aws_ecs.ICluster, image: aws_cdk.aws_ecs.ContainerImage, command: typing.Optional[typing.List[str]]=None, desired_task_count: typing.Optional[jsii.Number]=None, enable_logging: typing.Optional[bool]=None, environment: typing.Optional[typing.Mapping[str,str]]=None, max_scaling_capacity: typing.Optional[jsii.Number]=None, queue: typing.Optional[aws_cdk.aws_sqs.IQueue]=None, scaling_steps: typing.Optional[typing.List[aws_cdk.aws_applicationautoscaling.ScalingInterval]]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            cpu: The number of cpu units used by the task. Valid values, which determines your range of valid values for the memory parameter: 256 (.25 vCPU) - Available memory values: 0.5GB, 1GB, 2GB 512 (.5 vCPU) - Available memory values: 1GB, 2GB, 3GB, 4GB 1024 (1 vCPU) - Available memory values: 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB 2048 (2 vCPU) - Available memory values: Between 4GB and 16GB in 1GB increments 4096 (4 vCPU) - Available memory values: Between 8GB and 30GB in 1GB increments. This default is set in the underlying FargateTaskDefinition construct. Default: 256
            memory_limit_mi_b: The amount (in MiB) of memory used by the task. This field is required and you must use one of the following values, which determines your range of valid values for the cpu parameter: 0.5GB, 1GB, 2GB - Available cpu values: 256 (.25 vCPU) 1GB, 2GB, 3GB, 4GB - Available cpu values: 512 (.5 vCPU) 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB - Available cpu values: 1024 (1 vCPU) Between 4GB and 16GB in 1GB increments - Available cpu values: 2048 (2 vCPU) Between 8GB and 30GB in 1GB increments - Available cpu values: 4096 (4 vCPU) This default is set in the underlying FargateTaskDefinition construct. Default: 512
            cluster: Cluster where service will be deployed.
            image: The image to start.
            command: The CMD value to pass to the container. A string with commands delimited by commas. Default: none
            desired_task_count: Number of desired copies of running tasks. Default: 1
            enable_logging: Flag to indicate whether to enable logging. Default: true
            environment: The environment variables to pass to the container. Default: 'QUEUE_NAME: queue.queueName'
            max_scaling_capacity: Maximum capacity to scale to. Default: (desiredTaskCount * 2)
            queue: A queue for which to process items from. If specified and this is a FIFO queue, the queue name must end in the string '.fifo'. Default: 'SQSQueue with CloudFormation-generated name'
            scaling_steps: The intervals for scaling based on the SQS queue's ApproximateNumberOfMessagesVisible metric. Maps a range of metric values to a particular scaling behavior. https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html Default: [{ upper: 0, change: -1 },{ lower: 100, change: +1 },{ lower: 500, change: +5 }]

        Stability:
            experimental
        """
        props: QueueProcessingFargateServiceProps = {"cluster": cluster, "image": image}

        if cpu is not None:
            props["cpu"] = cpu

        if memory_limit_mi_b is not None:
            props["memoryLimitMiB"] = memory_limit_mi_b

        if command is not None:
            props["command"] = command

        if desired_task_count is not None:
            props["desiredTaskCount"] = desired_task_count

        if enable_logging is not None:
            props["enableLogging"] = enable_logging

        if environment is not None:
            props["environment"] = environment

        if max_scaling_capacity is not None:
            props["maxScalingCapacity"] = max_scaling_capacity

        if queue is not None:
            props["queue"] = queue

        if scaling_steps is not None:
            props["scalingSteps"] = scaling_steps

        jsii.create(QueueProcessingFargateService, self, [scope, id, props])

    @property
    @jsii.member(jsii_name="service")
    def service(self) -> aws_cdk.aws_ecs.FargateService:
        """The Fargate service in this construct.

        Stability:
            experimental
        """
        return jsii.get(self, "service")


@jsii.data_type_optionals(jsii_struct_bases=[])
class _QueueProcessingServiceBaseProps(jsii.compat.TypedDict, total=False):
    command: typing.List[str]
    """The CMD value to pass to the container.

    A string with commands delimited by commas.

    Default:
        none

    Stability:
        experimental
    """
    desiredTaskCount: jsii.Number
    """Number of desired copies of running tasks.

    Default:
        1

    Stability:
        experimental
    """
    enableLogging: bool
    """Flag to indicate whether to enable logging.

    Default:
        true

    Stability:
        experimental
    """
    environment: typing.Mapping[str,str]
    """The environment variables to pass to the container.

    Default:
        'QUEUE_NAME: queue.queueName'

    Stability:
        experimental
    """
    maxScalingCapacity: jsii.Number
    """Maximum capacity to scale to.

    Default:
        (desiredTaskCount * 2)

    Stability:
        experimental
    """
    queue: aws_cdk.aws_sqs.IQueue
    """A queue for which to process items from.

    If specified and this is a FIFO queue, the queue name must end in the string '.fifo'.

    Default:
        'SQSQueue with CloudFormation-generated name'

    See:
        https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html
    Stability:
        experimental
    """
    scalingSteps: typing.List[aws_cdk.aws_applicationautoscaling.ScalingInterval]
    """The intervals for scaling based on the SQS queue's ApproximateNumberOfMessagesVisible metric.

    Maps a range of metric values to a particular scaling behavior.
    https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html

    Default:
        [{ upper: 0, change: -1 },{ lower: 100, change: +1 },{ lower: 500, change: +5 }]

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-ecs-patterns.QueueProcessingServiceBaseProps", jsii_struct_bases=[_QueueProcessingServiceBaseProps])
class QueueProcessingServiceBaseProps(_QueueProcessingServiceBaseProps):
    """Properties to define a queue processing service.

    Stability:
        experimental
    """
    cluster: aws_cdk.aws_ecs.ICluster
    """Cluster where service will be deployed.

    Stability:
        experimental
    """

    image: aws_cdk.aws_ecs.ContainerImage
    """The image to start.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-ecs-patterns.QueueProcessingEc2ServiceProps", jsii_struct_bases=[QueueProcessingServiceBaseProps])
class QueueProcessingEc2ServiceProps(QueueProcessingServiceBaseProps, jsii.compat.TypedDict, total=False):
    """Properties to define a queue processing Ec2 service.

    Stability:
        experimental
    """
    cpu: jsii.Number
    """The minimum number of CPU units to reserve for the container.

    Default:
        - No minimum CPU units reserved.

    Stability:
        experimental
    """

    memoryLimitMiB: jsii.Number
    """The hard limit (in MiB) of memory to present to the container.

    If your container attempts to exceed the allocated memory, the container
    is terminated.

    At least one of memoryLimitMiB and memoryReservationMiB is required for non-Fargate services.

    Default:
        - No memory limit.

    Stability:
        experimental
    """

    memoryReservationMiB: jsii.Number
    """The soft limit (in MiB) of memory to reserve for the container.

    When system memory is under contention, Docker attempts to keep the
    container memory within the limit. If the container requires more memory,
    it can consume up to the value specified by the Memory property or all of
    the available memory on the container instance—whichever comes first.

    At least one of memoryLimitMiB and memoryReservationMiB is required for non-Fargate services.

    Default:
        - No memory reserved.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-ecs-patterns.QueueProcessingFargateServiceProps", jsii_struct_bases=[QueueProcessingServiceBaseProps])
class QueueProcessingFargateServiceProps(QueueProcessingServiceBaseProps, jsii.compat.TypedDict, total=False):
    """Properties to define a queue processing Fargate service.

    Stability:
        experimental
    """
    cpu: jsii.Number
    """The number of cpu units used by the task. Valid values, which determines your range of valid values for the memory parameter: 256 (.25 vCPU) - Available memory values: 0.5GB, 1GB, 2GB 512 (.5 vCPU) - Available memory values: 1GB, 2GB, 3GB, 4GB 1024 (1 vCPU) - Available memory values: 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB 2048 (2 vCPU) - Available memory values: Between 4GB and 16GB in 1GB increments 4096 (4 vCPU) - Available memory values: Between 8GB and 30GB in 1GB increments.

    This default is set in the underlying FargateTaskDefinition construct.

    Default:
        256

    Stability:
        experimental
    """

    memoryLimitMiB: jsii.Number
    """The amount (in MiB) of memory used by the task.

    This field is required and you must use one of the following values, which determines your range of valid values
    for the cpu parameter:

    0.5GB, 1GB, 2GB - Available cpu values: 256 (.25 vCPU)

    1GB, 2GB, 3GB, 4GB - Available cpu values: 512 (.5 vCPU)

    2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB - Available cpu values: 1024 (1 vCPU)

    Between 4GB and 16GB in 1GB increments - Available cpu values: 2048 (2 vCPU)

    Between 8GB and 30GB in 1GB increments - Available cpu values: 4096 (4 vCPU)

    This default is set in the underlying FargateTaskDefinition construct.

    Default:
        512

    Stability:
        experimental
    """

class ScheduledTaskBase(aws_cdk.core.Construct, metaclass=jsii.JSIIAbstractClass, jsii_type="@aws-cdk/aws-ecs-patterns.ScheduledTaskBase"):
    """A scheduled task base that will be initiated off of cloudwatch events.

    Stability:
        experimental
    """
    @staticmethod
    def __jsii_proxy_class__():
        return _ScheduledTaskBaseProxy

    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, cluster: aws_cdk.aws_ecs.ICluster, image: aws_cdk.aws_ecs.ContainerImage, schedule: aws_cdk.aws_events.Schedule, command: typing.Optional[typing.List[str]]=None, desired_task_count: typing.Optional[jsii.Number]=None, environment: typing.Optional[typing.Mapping[str,str]]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            cluster: The cluster where your service will be deployed.
            image: The image to start.
            schedule: The schedule or rate (frequency) that determines when CloudWatch Events runs the rule. For more information, see Schedule Expression Syntax for Rules in the Amazon CloudWatch User Guide.
            command: The CMD value to pass to the container. A string with commands delimited by commas. Default: none
            desired_task_count: Number of desired copies of running tasks. Default: 1
            environment: The environment variables to pass to the container. Default: none

        Stability:
            experimental
        """
        props: ScheduledTaskBaseProps = {"cluster": cluster, "image": image, "schedule": schedule}

        if command is not None:
            props["command"] = command

        if desired_task_count is not None:
            props["desiredTaskCount"] = desired_task_count

        if environment is not None:
            props["environment"] = environment

        jsii.create(ScheduledTaskBase, self, [scope, id, props])

    @jsii.member(jsii_name="addTaskDefinitionToEventTarget")
    def _add_task_definition_to_event_target(self, task_definition: aws_cdk.aws_ecs.TaskDefinition) -> aws_cdk.aws_events_targets.EcsTask:
        """Create an ecs task using the task definition provided and add it to the scheduled event rule.

        Arguments:
            task_definition: the TaskDefinition to add to the event rule.

        Stability:
            experimental
        """
        return jsii.invoke(self, "addTaskDefinitionToEventTarget", [task_definition])

    @jsii.member(jsii_name="createAWSLogDriver")
    def _create_aws_log_driver(self, prefix: str) -> aws_cdk.aws_ecs.AwsLogDriver:
        """Create an AWS Log Driver with the provided streamPrefix.

        Arguments:
            prefix: the Cloudwatch logging prefix.

        Stability:
            experimental
        """
        return jsii.invoke(self, "createAWSLogDriver", [prefix])

    @property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> aws_cdk.aws_ecs.ICluster:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "cluster")

    @property
    @jsii.member(jsii_name="desiredTaskCount")
    def desired_task_count(self) -> jsii.Number:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "desiredTaskCount")

    @property
    @jsii.member(jsii_name="eventRule")
    def event_rule(self) -> aws_cdk.aws_events.Rule:
        """
        Stability:
            experimental
        """
        return jsii.get(self, "eventRule")


class _ScheduledTaskBaseProxy(ScheduledTaskBase):
    pass

class ScheduledEc2Task(ScheduledTaskBase, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ecs-patterns.ScheduledEc2Task"):
    """A scheduled Ec2 task that will be initiated off of cloudwatch events.

    Stability:
        experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, cpu: typing.Optional[jsii.Number]=None, memory_limit_mi_b: typing.Optional[jsii.Number]=None, memory_reservation_mi_b: typing.Optional[jsii.Number]=None, cluster: aws_cdk.aws_ecs.ICluster, image: aws_cdk.aws_ecs.ContainerImage, schedule: aws_cdk.aws_events.Schedule, command: typing.Optional[typing.List[str]]=None, desired_task_count: typing.Optional[jsii.Number]=None, environment: typing.Optional[typing.Mapping[str,str]]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            cpu: The minimum number of CPU units to reserve for the container. Default: none
            memory_limit_mi_b: The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the allocated memory, the container is terminated. At least one of memoryLimitMiB and memoryReservationMiB is required for non-Fargate services. Default: - No memory limit.
            memory_reservation_mi_b: The soft limit (in MiB) of memory to reserve for the container. When system memory is under contention, Docker attempts to keep the container memory within the limit. If the container requires more memory, it can consume up to the value specified by the Memory property or all of the available memory on the container instance—whichever comes first. At least one of memoryLimitMiB and memoryReservationMiB is required for non-Fargate services. Default: - No memory reserved.
            cluster: The cluster where your service will be deployed.
            image: The image to start.
            schedule: The schedule or rate (frequency) that determines when CloudWatch Events runs the rule. For more information, see Schedule Expression Syntax for Rules in the Amazon CloudWatch User Guide.
            command: The CMD value to pass to the container. A string with commands delimited by commas. Default: none
            desired_task_count: Number of desired copies of running tasks. Default: 1
            environment: The environment variables to pass to the container. Default: none

        Stability:
            experimental
        """
        props: ScheduledEc2TaskProps = {"cluster": cluster, "image": image, "schedule": schedule}

        if cpu is not None:
            props["cpu"] = cpu

        if memory_limit_mi_b is not None:
            props["memoryLimitMiB"] = memory_limit_mi_b

        if memory_reservation_mi_b is not None:
            props["memoryReservationMiB"] = memory_reservation_mi_b

        if command is not None:
            props["command"] = command

        if desired_task_count is not None:
            props["desiredTaskCount"] = desired_task_count

        if environment is not None:
            props["environment"] = environment

        jsii.create(ScheduledEc2Task, self, [scope, id, props])


class ScheduledFargateTask(ScheduledTaskBase, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-ecs-patterns.ScheduledFargateTask"):
    """A scheduled Fargate task that will be initiated off of cloudwatch events.

    Stability:
        experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, cpu: typing.Optional[jsii.Number]=None, memory_limit_mi_b: typing.Optional[jsii.Number]=None, cluster: aws_cdk.aws_ecs.ICluster, image: aws_cdk.aws_ecs.ContainerImage, schedule: aws_cdk.aws_events.Schedule, command: typing.Optional[typing.List[str]]=None, desired_task_count: typing.Optional[jsii.Number]=None, environment: typing.Optional[typing.Mapping[str,str]]=None) -> None:
        """
        Arguments:
            scope: -
            id: -
            props: -
            cpu: The number of cpu units used by the task. Valid values, which determines your range of valid values for the memory parameter: 256 (.25 vCPU) - Available memory values: 0.5GB, 1GB, 2GB 512 (.5 vCPU) - Available memory values: 1GB, 2GB, 3GB, 4GB 1024 (1 vCPU) - Available memory values: 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB 2048 (2 vCPU) - Available memory values: Between 4GB and 16GB in 1GB increments 4096 (4 vCPU) - Available memory values: Between 8GB and 30GB in 1GB increments. This default is set in the underlying FargateTaskDefinition construct. Default: 256
            memory_limit_mi_b: The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the allocated memory, the container is terminated. At least one of memoryLimitMiB and memoryReservationMiB is required for non-Fargate services. Default: 512
            cluster: The cluster where your service will be deployed.
            image: The image to start.
            schedule: The schedule or rate (frequency) that determines when CloudWatch Events runs the rule. For more information, see Schedule Expression Syntax for Rules in the Amazon CloudWatch User Guide.
            command: The CMD value to pass to the container. A string with commands delimited by commas. Default: none
            desired_task_count: Number of desired copies of running tasks. Default: 1
            environment: The environment variables to pass to the container. Default: none

        Stability:
            experimental
        """
        props: ScheduledFargateTaskProps = {"cluster": cluster, "image": image, "schedule": schedule}

        if cpu is not None:
            props["cpu"] = cpu

        if memory_limit_mi_b is not None:
            props["memoryLimitMiB"] = memory_limit_mi_b

        if command is not None:
            props["command"] = command

        if desired_task_count is not None:
            props["desiredTaskCount"] = desired_task_count

        if environment is not None:
            props["environment"] = environment

        jsii.create(ScheduledFargateTask, self, [scope, id, props])


@jsii.data_type_optionals(jsii_struct_bases=[])
class _ScheduledTaskBaseProps(jsii.compat.TypedDict, total=False):
    command: typing.List[str]
    """The CMD value to pass to the container.

    A string with commands delimited by commas.

    Default:
        none

    Stability:
        experimental
    """
    desiredTaskCount: jsii.Number
    """Number of desired copies of running tasks.

    Default:
        1

    Stability:
        experimental
    """
    environment: typing.Mapping[str,str]
    """The environment variables to pass to the container.

    Default:
        none

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-ecs-patterns.ScheduledTaskBaseProps", jsii_struct_bases=[_ScheduledTaskBaseProps])
class ScheduledTaskBaseProps(_ScheduledTaskBaseProps):
    """
    Stability:
        experimental
    """
    cluster: aws_cdk.aws_ecs.ICluster
    """The cluster where your service will be deployed.

    Stability:
        experimental
    """

    image: aws_cdk.aws_ecs.ContainerImage
    """The image to start.

    Stability:
        experimental
    """

    schedule: aws_cdk.aws_events.Schedule
    """The schedule or rate (frequency) that determines when CloudWatch Events runs the rule.

    For more information, see Schedule Expression Syntax for
    Rules in the Amazon CloudWatch User Guide.

    See:
        http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html
    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-ecs-patterns.ScheduledEc2TaskProps", jsii_struct_bases=[ScheduledTaskBaseProps])
class ScheduledEc2TaskProps(ScheduledTaskBaseProps, jsii.compat.TypedDict, total=False):
    """
    Stability:
        experimental
    """
    cpu: jsii.Number
    """The minimum number of CPU units to reserve for the container.

    Default:
        none

    Stability:
        experimental
    """

    memoryLimitMiB: jsii.Number
    """The hard limit (in MiB) of memory to present to the container.

    If your container attempts to exceed the allocated memory, the container
    is terminated.

    At least one of memoryLimitMiB and memoryReservationMiB is required for non-Fargate services.

    Default:
        - No memory limit.

    Stability:
        experimental
    """

    memoryReservationMiB: jsii.Number
    """The soft limit (in MiB) of memory to reserve for the container.

    When system memory is under contention, Docker attempts to keep the
    container memory within the limit. If the container requires more memory,
    it can consume up to the value specified by the Memory property or all of
    the available memory on the container instance—whichever comes first.

    At least one of memoryLimitMiB and memoryReservationMiB is required for non-Fargate services.

    Default:
        - No memory reserved.

    Stability:
        experimental
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-ecs-patterns.ScheduledFargateTaskProps", jsii_struct_bases=[ScheduledTaskBaseProps])
class ScheduledFargateTaskProps(ScheduledTaskBaseProps, jsii.compat.TypedDict, total=False):
    """
    Stability:
        experimental
    """
    cpu: jsii.Number
    """The number of cpu units used by the task. Valid values, which determines your range of valid values for the memory parameter: 256 (.25 vCPU) - Available memory values: 0.5GB, 1GB, 2GB 512 (.5 vCPU) - Available memory values: 1GB, 2GB, 3GB, 4GB 1024 (1 vCPU) - Available memory values: 2GB, 3GB, 4GB, 5GB, 6GB, 7GB, 8GB 2048 (2 vCPU) - Available memory values: Between 4GB and 16GB in 1GB increments 4096 (4 vCPU) - Available memory values: Between 8GB and 30GB in 1GB increments.

    This default is set in the underlying FargateTaskDefinition construct.

    Default:
        256

    Stability:
        experimental
    """

    memoryLimitMiB: jsii.Number
    """The hard limit (in MiB) of memory to present to the container.

    If your container attempts to exceed the allocated memory, the container
    is terminated.

    At least one of memoryLimitMiB and memoryReservationMiB is required for non-Fargate services.

    Default:
        512

    Stability:
        experimental
    """

__all__ = ["LoadBalancedEc2Service", "LoadBalancedEc2ServiceProps", "LoadBalancedFargateService", "LoadBalancedFargateServiceProps", "LoadBalancedServiceBase", "LoadBalancedServiceBaseProps", "LoadBalancerType", "QueueProcessingEc2Service", "QueueProcessingEc2ServiceProps", "QueueProcessingFargateService", "QueueProcessingFargateServiceProps", "QueueProcessingServiceBase", "QueueProcessingServiceBaseProps", "ScheduledEc2Task", "ScheduledEc2TaskProps", "ScheduledFargateTask", "ScheduledFargateTaskProps", "ScheduledTaskBase", "ScheduledTaskBaseProps", "__jsii_assembly__"]

publication.publish()
