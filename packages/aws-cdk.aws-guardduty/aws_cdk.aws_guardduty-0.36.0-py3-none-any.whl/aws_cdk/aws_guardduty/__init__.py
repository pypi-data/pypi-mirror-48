import abc
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

from jsii.python import classproperty

import aws_cdk.core
__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-guardduty", "0.36.0", __name__, "aws-guardduty@0.36.0.jsii.tgz")
class CfnDetector(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-guardduty.CfnDetector"):
    """A CloudFormation ``AWS::GuardDuty::Detector``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html
    Stability:
        stable
    cloudformationResource:
        AWS::GuardDuty::Detector
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, enable: typing.Union[bool, aws_cdk.core.IResolvable], finding_publishing_frequency: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::GuardDuty::Detector``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            enable: ``AWS::GuardDuty::Detector.Enable``.
            finding_publishing_frequency: ``AWS::GuardDuty::Detector.FindingPublishingFrequency``.

        Stability:
            experimental
        """
        props: CfnDetectorProps = {"enable": enable}

        if finding_publishing_frequency is not None:
            props["findingPublishingFrequency"] = finding_publishing_frequency

        jsii.create(CfnDetector, self, [scope, id, props])

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
    @jsii.member(jsii_name="enable")
    def enable(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::GuardDuty::Detector.Enable``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-enable
        Stability:
            stable
        """
        return jsii.get(self, "enable")

    @enable.setter
    def enable(self, value: typing.Union[bool, aws_cdk.core.IResolvable]):
        return jsii.set(self, "enable", value)

    @property
    @jsii.member(jsii_name="findingPublishingFrequency")
    def finding_publishing_frequency(self) -> typing.Optional[str]:
        """``AWS::GuardDuty::Detector.FindingPublishingFrequency``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-findingpublishingfrequency
        Stability:
            stable
        """
        return jsii.get(self, "findingPublishingFrequency")

    @finding_publishing_frequency.setter
    def finding_publishing_frequency(self, value: typing.Optional[str]):
        return jsii.set(self, "findingPublishingFrequency", value)


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnDetectorProps(jsii.compat.TypedDict, total=False):
    findingPublishingFrequency: str
    """``AWS::GuardDuty::Detector.FindingPublishingFrequency``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-findingpublishingfrequency
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-guardduty.CfnDetectorProps", jsii_struct_bases=[_CfnDetectorProps])
class CfnDetectorProps(_CfnDetectorProps):
    """Properties for defining a ``AWS::GuardDuty::Detector``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html
    Stability:
        stable
    """
    enable: typing.Union[bool, aws_cdk.core.IResolvable]
    """``AWS::GuardDuty::Detector.Enable``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html#cfn-guardduty-detector-enable
    Stability:
        stable
    """

class CfnFilter(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-guardduty.CfnFilter"):
    """A CloudFormation ``AWS::GuardDuty::Filter``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html
    Stability:
        stable
    cloudformationResource:
        AWS::GuardDuty::Filter
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, action: str, description: str, detector_id: str, finding_criteria: typing.Union[aws_cdk.core.IResolvable, "FindingCriteriaProperty"], rank: jsii.Number, name: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::GuardDuty::Filter``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            action: ``AWS::GuardDuty::Filter.Action``.
            description: ``AWS::GuardDuty::Filter.Description``.
            detector_id: ``AWS::GuardDuty::Filter.DetectorId``.
            finding_criteria: ``AWS::GuardDuty::Filter.FindingCriteria``.
            rank: ``AWS::GuardDuty::Filter.Rank``.
            name: ``AWS::GuardDuty::Filter.Name``.

        Stability:
            experimental
        """
        props: CfnFilterProps = {"action": action, "description": description, "detectorId": detector_id, "findingCriteria": finding_criteria, "rank": rank}

        if name is not None:
            props["name"] = name

        jsii.create(CfnFilter, self, [scope, id, props])

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
    @jsii.member(jsii_name="action")
    def action(self) -> str:
        """``AWS::GuardDuty::Filter.Action``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-action
        Stability:
            stable
        """
        return jsii.get(self, "action")

    @action.setter
    def action(self, value: str):
        return jsii.set(self, "action", value)

    @property
    @jsii.member(jsii_name="description")
    def description(self) -> str:
        """``AWS::GuardDuty::Filter.Description``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-description
        Stability:
            stable
        """
        return jsii.get(self, "description")

    @description.setter
    def description(self, value: str):
        return jsii.set(self, "description", value)

    @property
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> str:
        """``AWS::GuardDuty::Filter.DetectorId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-detectorid
        Stability:
            stable
        """
        return jsii.get(self, "detectorId")

    @detector_id.setter
    def detector_id(self, value: str):
        return jsii.set(self, "detectorId", value)

    @property
    @jsii.member(jsii_name="findingCriteria")
    def finding_criteria(self) -> typing.Union[aws_cdk.core.IResolvable, "FindingCriteriaProperty"]:
        """``AWS::GuardDuty::Filter.FindingCriteria``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-findingcriteria
        Stability:
            stable
        """
        return jsii.get(self, "findingCriteria")

    @finding_criteria.setter
    def finding_criteria(self, value: typing.Union[aws_cdk.core.IResolvable, "FindingCriteriaProperty"]):
        return jsii.set(self, "findingCriteria", value)

    @property
    @jsii.member(jsii_name="rank")
    def rank(self) -> jsii.Number:
        """``AWS::GuardDuty::Filter.Rank``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-rank
        Stability:
            stable
        """
        return jsii.get(self, "rank")

    @rank.setter
    def rank(self, value: jsii.Number):
        return jsii.set(self, "rank", value)

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::GuardDuty::Filter.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-name
        Stability:
            stable
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        return jsii.set(self, "name", value)

    @jsii.data_type(jsii_type="@aws-cdk/aws-guardduty.CfnFilter.ConditionProperty", jsii_struct_bases=[])
    class ConditionProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html
        Stability:
            stable
        """
        eq: typing.List[str]
        """``CfnFilter.ConditionProperty.Eq``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-eq
        Stability:
            stable
        """

        gte: jsii.Number
        """``CfnFilter.ConditionProperty.Gte``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-gte
        Stability:
            stable
        """

        lt: jsii.Number
        """``CfnFilter.ConditionProperty.Lt``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-lt
        Stability:
            stable
        """

        lte: jsii.Number
        """``CfnFilter.ConditionProperty.Lte``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-lte
        Stability:
            stable
        """

        neq: typing.List[str]
        """``CfnFilter.ConditionProperty.Neq``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-condition.html#cfn-guardduty-filter-condition-neq
        Stability:
            stable
        """

    @jsii.data_type(jsii_type="@aws-cdk/aws-guardduty.CfnFilter.FindingCriteriaProperty", jsii_struct_bases=[])
    class FindingCriteriaProperty(jsii.compat.TypedDict, total=False):
        """
        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html
        Stability:
            stable
        """
        criterion: typing.Any
        """``CfnFilter.FindingCriteriaProperty.Criterion``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html#cfn-guardduty-filter-findingcriteria-criterion
        Stability:
            stable
        """

        itemType: typing.Union[aws_cdk.core.IResolvable, "CfnFilter.ConditionProperty"]
        """``CfnFilter.FindingCriteriaProperty.ItemType``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-guardduty-filter-findingcriteria.html#cfn-guardduty-filter-findingcriteria-itemtype
        Stability:
            stable
        """


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnFilterProps(jsii.compat.TypedDict, total=False):
    name: str
    """``AWS::GuardDuty::Filter.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-name
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-guardduty.CfnFilterProps", jsii_struct_bases=[_CfnFilterProps])
class CfnFilterProps(_CfnFilterProps):
    """Properties for defining a ``AWS::GuardDuty::Filter``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html
    Stability:
        stable
    """
    action: str
    """``AWS::GuardDuty::Filter.Action``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-action
    Stability:
        stable
    """

    description: str
    """``AWS::GuardDuty::Filter.Description``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-description
    Stability:
        stable
    """

    detectorId: str
    """``AWS::GuardDuty::Filter.DetectorId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-detectorid
    Stability:
        stable
    """

    findingCriteria: typing.Union[aws_cdk.core.IResolvable, "CfnFilter.FindingCriteriaProperty"]
    """``AWS::GuardDuty::Filter.FindingCriteria``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-findingcriteria
    Stability:
        stable
    """

    rank: jsii.Number
    """``AWS::GuardDuty::Filter.Rank``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html#cfn-guardduty-filter-rank
    Stability:
        stable
    """

class CfnIPSet(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-guardduty.CfnIPSet"):
    """A CloudFormation ``AWS::GuardDuty::IPSet``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html
    Stability:
        stable
    cloudformationResource:
        AWS::GuardDuty::IPSet
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, activate: typing.Union[bool, aws_cdk.core.IResolvable], detector_id: str, format: str, location: str, name: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::GuardDuty::IPSet``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            activate: ``AWS::GuardDuty::IPSet.Activate``.
            detector_id: ``AWS::GuardDuty::IPSet.DetectorId``.
            format: ``AWS::GuardDuty::IPSet.Format``.
            location: ``AWS::GuardDuty::IPSet.Location``.
            name: ``AWS::GuardDuty::IPSet.Name``.

        Stability:
            experimental
        """
        props: CfnIPSetProps = {"activate": activate, "detectorId": detector_id, "format": format, "location": location}

        if name is not None:
            props["name"] = name

        jsii.create(CfnIPSet, self, [scope, id, props])

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
    @jsii.member(jsii_name="activate")
    def activate(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::GuardDuty::IPSet.Activate``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-activate
        Stability:
            stable
        """
        return jsii.get(self, "activate")

    @activate.setter
    def activate(self, value: typing.Union[bool, aws_cdk.core.IResolvable]):
        return jsii.set(self, "activate", value)

    @property
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> str:
        """``AWS::GuardDuty::IPSet.DetectorId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-detectorid
        Stability:
            stable
        """
        return jsii.get(self, "detectorId")

    @detector_id.setter
    def detector_id(self, value: str):
        return jsii.set(self, "detectorId", value)

    @property
    @jsii.member(jsii_name="format")
    def format(self) -> str:
        """``AWS::GuardDuty::IPSet.Format``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-format
        Stability:
            stable
        """
        return jsii.get(self, "format")

    @format.setter
    def format(self, value: str):
        return jsii.set(self, "format", value)

    @property
    @jsii.member(jsii_name="location")
    def location(self) -> str:
        """``AWS::GuardDuty::IPSet.Location``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-location
        Stability:
            stable
        """
        return jsii.get(self, "location")

    @location.setter
    def location(self, value: str):
        return jsii.set(self, "location", value)

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::GuardDuty::IPSet.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-name
        Stability:
            stable
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        return jsii.set(self, "name", value)


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnIPSetProps(jsii.compat.TypedDict, total=False):
    name: str
    """``AWS::GuardDuty::IPSet.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-name
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-guardduty.CfnIPSetProps", jsii_struct_bases=[_CfnIPSetProps])
class CfnIPSetProps(_CfnIPSetProps):
    """Properties for defining a ``AWS::GuardDuty::IPSet``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html
    Stability:
        stable
    """
    activate: typing.Union[bool, aws_cdk.core.IResolvable]
    """``AWS::GuardDuty::IPSet.Activate``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-activate
    Stability:
        stable
    """

    detectorId: str
    """``AWS::GuardDuty::IPSet.DetectorId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-detectorid
    Stability:
        stable
    """

    format: str
    """``AWS::GuardDuty::IPSet.Format``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-format
    Stability:
        stable
    """

    location: str
    """``AWS::GuardDuty::IPSet.Location``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html#cfn-guardduty-ipset-location
    Stability:
        stable
    """

class CfnMaster(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-guardduty.CfnMaster"):
    """A CloudFormation ``AWS::GuardDuty::Master``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html
    Stability:
        stable
    cloudformationResource:
        AWS::GuardDuty::Master
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, detector_id: str, master_id: str, invitation_id: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::GuardDuty::Master``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            detector_id: ``AWS::GuardDuty::Master.DetectorId``.
            master_id: ``AWS::GuardDuty::Master.MasterId``.
            invitation_id: ``AWS::GuardDuty::Master.InvitationId``.

        Stability:
            experimental
        """
        props: CfnMasterProps = {"detectorId": detector_id, "masterId": master_id}

        if invitation_id is not None:
            props["invitationId"] = invitation_id

        jsii.create(CfnMaster, self, [scope, id, props])

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
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> str:
        """``AWS::GuardDuty::Master.DetectorId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-detectorid
        Stability:
            stable
        """
        return jsii.get(self, "detectorId")

    @detector_id.setter
    def detector_id(self, value: str):
        return jsii.set(self, "detectorId", value)

    @property
    @jsii.member(jsii_name="masterId")
    def master_id(self) -> str:
        """``AWS::GuardDuty::Master.MasterId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-masterid
        Stability:
            stable
        """
        return jsii.get(self, "masterId")

    @master_id.setter
    def master_id(self, value: str):
        return jsii.set(self, "masterId", value)

    @property
    @jsii.member(jsii_name="invitationId")
    def invitation_id(self) -> typing.Optional[str]:
        """``AWS::GuardDuty::Master.InvitationId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-invitationid
        Stability:
            stable
        """
        return jsii.get(self, "invitationId")

    @invitation_id.setter
    def invitation_id(self, value: typing.Optional[str]):
        return jsii.set(self, "invitationId", value)


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnMasterProps(jsii.compat.TypedDict, total=False):
    invitationId: str
    """``AWS::GuardDuty::Master.InvitationId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-invitationid
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-guardduty.CfnMasterProps", jsii_struct_bases=[_CfnMasterProps])
class CfnMasterProps(_CfnMasterProps):
    """Properties for defining a ``AWS::GuardDuty::Master``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html
    Stability:
        stable
    """
    detectorId: str
    """``AWS::GuardDuty::Master.DetectorId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-detectorid
    Stability:
        stable
    """

    masterId: str
    """``AWS::GuardDuty::Master.MasterId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html#cfn-guardduty-master-masterid
    Stability:
        stable
    """

class CfnMember(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-guardduty.CfnMember"):
    """A CloudFormation ``AWS::GuardDuty::Member``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html
    Stability:
        stable
    cloudformationResource:
        AWS::GuardDuty::Member
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, detector_id: str, email: str, member_id: str, disable_email_notification: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]=None, message: typing.Optional[str]=None, status: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::GuardDuty::Member``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            detector_id: ``AWS::GuardDuty::Member.DetectorId``.
            email: ``AWS::GuardDuty::Member.Email``.
            member_id: ``AWS::GuardDuty::Member.MemberId``.
            disable_email_notification: ``AWS::GuardDuty::Member.DisableEmailNotification``.
            message: ``AWS::GuardDuty::Member.Message``.
            status: ``AWS::GuardDuty::Member.Status``.

        Stability:
            experimental
        """
        props: CfnMemberProps = {"detectorId": detector_id, "email": email, "memberId": member_id}

        if disable_email_notification is not None:
            props["disableEmailNotification"] = disable_email_notification

        if message is not None:
            props["message"] = message

        if status is not None:
            props["status"] = status

        jsii.create(CfnMember, self, [scope, id, props])

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
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> str:
        """``AWS::GuardDuty::Member.DetectorId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-detectorid
        Stability:
            stable
        """
        return jsii.get(self, "detectorId")

    @detector_id.setter
    def detector_id(self, value: str):
        return jsii.set(self, "detectorId", value)

    @property
    @jsii.member(jsii_name="email")
    def email(self) -> str:
        """``AWS::GuardDuty::Member.Email``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-email
        Stability:
            stable
        """
        return jsii.get(self, "email")

    @email.setter
    def email(self, value: str):
        return jsii.set(self, "email", value)

    @property
    @jsii.member(jsii_name="memberId")
    def member_id(self) -> str:
        """``AWS::GuardDuty::Member.MemberId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-memberid
        Stability:
            stable
        """
        return jsii.get(self, "memberId")

    @member_id.setter
    def member_id(self, value: str):
        return jsii.set(self, "memberId", value)

    @property
    @jsii.member(jsii_name="disableEmailNotification")
    def disable_email_notification(self) -> typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]:
        """``AWS::GuardDuty::Member.DisableEmailNotification``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-disableemailnotification
        Stability:
            stable
        """
        return jsii.get(self, "disableEmailNotification")

    @disable_email_notification.setter
    def disable_email_notification(self, value: typing.Optional[typing.Union[typing.Optional[bool], typing.Optional[aws_cdk.core.IResolvable]]]):
        return jsii.set(self, "disableEmailNotification", value)

    @property
    @jsii.member(jsii_name="message")
    def message(self) -> typing.Optional[str]:
        """``AWS::GuardDuty::Member.Message``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-message
        Stability:
            stable
        """
        return jsii.get(self, "message")

    @message.setter
    def message(self, value: typing.Optional[str]):
        return jsii.set(self, "message", value)

    @property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[str]:
        """``AWS::GuardDuty::Member.Status``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-status
        Stability:
            stable
        """
        return jsii.get(self, "status")

    @status.setter
    def status(self, value: typing.Optional[str]):
        return jsii.set(self, "status", value)


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnMemberProps(jsii.compat.TypedDict, total=False):
    disableEmailNotification: typing.Union[bool, aws_cdk.core.IResolvable]
    """``AWS::GuardDuty::Member.DisableEmailNotification``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-disableemailnotification
    Stability:
        stable
    """
    message: str
    """``AWS::GuardDuty::Member.Message``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-message
    Stability:
        stable
    """
    status: str
    """``AWS::GuardDuty::Member.Status``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-status
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-guardduty.CfnMemberProps", jsii_struct_bases=[_CfnMemberProps])
class CfnMemberProps(_CfnMemberProps):
    """Properties for defining a ``AWS::GuardDuty::Member``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html
    Stability:
        stable
    """
    detectorId: str
    """``AWS::GuardDuty::Member.DetectorId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-detectorid
    Stability:
        stable
    """

    email: str
    """``AWS::GuardDuty::Member.Email``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-email
    Stability:
        stable
    """

    memberId: str
    """``AWS::GuardDuty::Member.MemberId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html#cfn-guardduty-member-memberid
    Stability:
        stable
    """

class CfnThreatIntelSet(aws_cdk.core.CfnResource, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-guardduty.CfnThreatIntelSet"):
    """A CloudFormation ``AWS::GuardDuty::ThreatIntelSet``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html
    Stability:
        stable
    cloudformationResource:
        AWS::GuardDuty::ThreatIntelSet
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, activate: typing.Union[bool, aws_cdk.core.IResolvable], detector_id: str, format: str, location: str, name: typing.Optional[str]=None) -> None:
        """Create a new ``AWS::GuardDuty::ThreatIntelSet``.

        Arguments:
            scope: - scope in which this resource is defined.
            id: - scoped id of the resource.
            props: - resource properties.
            activate: ``AWS::GuardDuty::ThreatIntelSet.Activate``.
            detector_id: ``AWS::GuardDuty::ThreatIntelSet.DetectorId``.
            format: ``AWS::GuardDuty::ThreatIntelSet.Format``.
            location: ``AWS::GuardDuty::ThreatIntelSet.Location``.
            name: ``AWS::GuardDuty::ThreatIntelSet.Name``.

        Stability:
            experimental
        """
        props: CfnThreatIntelSetProps = {"activate": activate, "detectorId": detector_id, "format": format, "location": location}

        if name is not None:
            props["name"] = name

        jsii.create(CfnThreatIntelSet, self, [scope, id, props])

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
    @jsii.member(jsii_name="activate")
    def activate(self) -> typing.Union[bool, aws_cdk.core.IResolvable]:
        """``AWS::GuardDuty::ThreatIntelSet.Activate``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-activate
        Stability:
            stable
        """
        return jsii.get(self, "activate")

    @activate.setter
    def activate(self, value: typing.Union[bool, aws_cdk.core.IResolvable]):
        return jsii.set(self, "activate", value)

    @property
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> str:
        """``AWS::GuardDuty::ThreatIntelSet.DetectorId``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-detectorid
        Stability:
            stable
        """
        return jsii.get(self, "detectorId")

    @detector_id.setter
    def detector_id(self, value: str):
        return jsii.set(self, "detectorId", value)

    @property
    @jsii.member(jsii_name="format")
    def format(self) -> str:
        """``AWS::GuardDuty::ThreatIntelSet.Format``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-format
        Stability:
            stable
        """
        return jsii.get(self, "format")

    @format.setter
    def format(self, value: str):
        return jsii.set(self, "format", value)

    @property
    @jsii.member(jsii_name="location")
    def location(self) -> str:
        """``AWS::GuardDuty::ThreatIntelSet.Location``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-location
        Stability:
            stable
        """
        return jsii.get(self, "location")

    @location.setter
    def location(self, value: str):
        return jsii.set(self, "location", value)

    @property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[str]:
        """``AWS::GuardDuty::ThreatIntelSet.Name``.

        See:
            http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-name
        Stability:
            stable
        """
        return jsii.get(self, "name")

    @name.setter
    def name(self, value: typing.Optional[str]):
        return jsii.set(self, "name", value)


@jsii.data_type_optionals(jsii_struct_bases=[])
class _CfnThreatIntelSetProps(jsii.compat.TypedDict, total=False):
    name: str
    """``AWS::GuardDuty::ThreatIntelSet.Name``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-name
    Stability:
        stable
    """

@jsii.data_type(jsii_type="@aws-cdk/aws-guardduty.CfnThreatIntelSetProps", jsii_struct_bases=[_CfnThreatIntelSetProps])
class CfnThreatIntelSetProps(_CfnThreatIntelSetProps):
    """Properties for defining a ``AWS::GuardDuty::ThreatIntelSet``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html
    Stability:
        stable
    """
    activate: typing.Union[bool, aws_cdk.core.IResolvable]
    """``AWS::GuardDuty::ThreatIntelSet.Activate``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-activate
    Stability:
        stable
    """

    detectorId: str
    """``AWS::GuardDuty::ThreatIntelSet.DetectorId``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-detectorid
    Stability:
        stable
    """

    format: str
    """``AWS::GuardDuty::ThreatIntelSet.Format``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-format
    Stability:
        stable
    """

    location: str
    """``AWS::GuardDuty::ThreatIntelSet.Location``.

    See:
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html#cfn-guardduty-threatintelset-location
    Stability:
        stable
    """

__all__ = ["CfnDetector", "CfnDetectorProps", "CfnFilter", "CfnFilterProps", "CfnIPSet", "CfnIPSetProps", "CfnMaster", "CfnMasterProps", "CfnMember", "CfnMemberProps", "CfnThreatIntelSet", "CfnThreatIntelSetProps", "__jsii_assembly__"]

publication.publish()
