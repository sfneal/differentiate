# Retrieve unique values from two nested lists.
import unittest
from differentiate import diff
from looptools import Timer


class TestDiffDicts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.x = {
            'Activity': 89958,
            'Address': 0,
            'AddressEmailPhoneType': 32,
            'AgeGroup': 0,
            'AllIn_Include': 0,
            'AllIn_Module': 0,
            'Article': 0,
            'Axor_Projects': 0,
            'Axor_Ressources': 0,
            'BasementType': 5,
            'Bill': 0,
            'BillTimeSheet': 0,
            'Builder': 0,
            'COStatus': 0,
            'COType': 0,
            'CObject': 0,
            'CObjectPerson': 0,
            'CObjectPersonRole': 0,
            'CObjectTopic': 0,
            'CodeCompliance': 6,
            'Company': 0,
            'CompanyAddress': 1211,
            'CompanyCountry': 0,
            'CompanyEmailAddress': 0,
            'CompanyPhone': 1863,
            'CompanyProject': 0,
            'CompanyTags': 0,
            'ContactComment': 0,
            'ContactHistory': 0,
            'ContactHistoryEventType': 0,
            'ContentBodyType': 0,
            'Country': 0,
            'DEV_TestUtils': 0,
            'Department': 3,
            'Division': 0,
            'DocumentFile': 0,
            'DocumentObject': 2587,
            'DocumentObjectEventType': 9,
            'DocumentObjectHistory': 2,
            'DocumentObjectStats': 0,
            'DocumentObjectTags': 0,
            'DocumentObjectType': 0,
            'EmailAddress': 2012,
            'FamilyRoomLocation': 0,
            'Field': 0,
            'GarageLocation': 0,
            'GlobalSetting': 27,
            'HOUSE INFO': 0,
            'HOUSE INFO 1': 0,
            'HOUSE INFO 2': 0,
            'HomePlan': 0,
            'HomePlanCodeCompliance': 2498,
            'HomePlanHomeStyle': 2903,
            'HomePlanOption': 4,
            'HomePlanOptionChoice': 2,
            'HomeStyle': 22,
            'Keyword': 5,
            'Login': 0,
            'LoginRole': 32,
            'MainRoofType': 0,
            'Message': 0,
            'MessageDocument': 0,
            'MessageProject': 1320,
            'MessageTask': 19,
            'MessageType': 0,
            'Mime': 1436,
            'Mode_Order': 0,
            'Mode_OrderItem': 0,
            'Mode_OrderType': 0,
            'NewsItem': 0,
            'NonPerson': 0,
            'NonPersonType': 0,
            'Operation': 13,
            'Order': 0,
            'OrderItem': 999,
            'Page': 0,
            'PagePagelet': 0,
            'Person': 0,
            'PersonAddress': 0,
            'PersonCompany': 0,
            'PersonCompanyProjectRole': 5,
            'PersonCountry': 0,
            'PersonDocumentObject': 0,
            'PersonEmailAddress': 1922,
            'PersonPhone': 0,
            'PersonProject': 10760,
            'PersonTags': 0,
            'PersonTimeEvent': 0,
            'PersonWebRole': 0,
            'Phone': 0,
            'PodColumn': 0,
            'Podlet': 0,
            'PodletField': 0,
            'PortalColumn': 3,
            'PortalPod': 24,
            'PortalPodPerson': 0,
            'PortalPodPodlet': 0,
            'PriceCode': 13,
            'PricePlan': 52,
            'Project': 0,
            'ProjectCObject': 2655,
            'ProjectCategory': 0,
            'ProjectComment': 0,
            'ProjectDerivation': 0,
            'ProjectDocumentObject': 2561,
            'ProjectPhase': 9155,
            'ProjectPhaseType': 0,
            'ProjectStatus': 0,
            'ProjectStatusType': 4,
            'ProjectType': 0,
            'ProjectTypeOperation': 0,
            'ProjectTypeRelease': 0,
            'ProjectionLocation': 4,
            'SaleType': 10,
            'StateProvince': 0,
            'Tags': 0,
            'Task': 0,
            'TaskDocumentObject': 0,
            'TaskNotify': 0,
            'TaskSegment': 126301,
            'TaskSegmentCorrection': 0,
            'TeamMember': 20,
            'Ticket': 0,
            'TimeBracket': 0,
            'TimeBracketEvent': 0,
            'TimeEvent': 0,
            'TimeEventActionType': 0,
            'TimeEventHistory': 0,
            'TimeEventTrigger': 0,
            'TimeLineManager': 0,
            'Timeline': 0,
            'TimelineModelProject': 0,
            'TimelineType': 0,
            'Timesheet': 0,
            'TimesheetStatusType': 5,
            'TimesheetTaskSegment': 74253,
            'Topic': 0,
            'Trigger': 0,
            'TriggerType': 2,
            'UIElement': 0,
            'UIElementType': 0,
            'UI_Container': 0,
            'UI_Container2': 0,
            'UI_ContainerRelationship': 0,
            'UI_ContainerType': 0,
            'UI_ContainerTypePage': 0,
            'UI_ContainerTypePagelet': 0,
            'UI_ContainerTypePod': 0,
            'UI_ContainerTypePortal': 0,
            'UI_Field': 0,
            'UI_Form': 0,
            'UI_FormField': 0,
            'UI_Form_UI_FormField': 0,
            'UI_ListField': 6,
            'UI_ListTemplate': 0,
            'UI_Object': 0,
            'UI_Pagelet': 0,
            'UI_SearchForm': 0,
            'UI_SearchParameters': 0,
            'WebRole': 0,
            'WebStatusType': 4,
            'dtproperties': 0,
            'hpaadmin.check_sysuser': 0,
            'iLivError': 0,
            'personRate': 20
        }
        cls.y = {
            'Activity': 89958,
            'Address': 11656,
            'AddressEmailPhoneType': 32,
            'AgeGroup': 0,
            'AllIn_Include': 0,
            'AllIn_Module': 0,
            'Article': 0,
            'Axor_Projects': 0,
            'Axor_Ressources': 0,
            'BasementType': 5,
            'Bill': 0,
            'BillTimeSheet': 0,
            'Builder': 0,
            'COStatus': 0,
            'COType': 0,
            'CObject': 0,
            'CObjectPerson': 0,
            'CObjectPersonRole': 0,
            'CObjectTopic': 0,
            'CodeCompliance': 6,
            'Company': 0,
            'CompanyAddress': 1211,
            'CompanyCountry': 0,
            'CompanyEmailAddress': 0,
            'CompanyPhone': 1863,
            'CompanyProject': 7903,
            'CompanyTags': 0,
            'ContactComment': 0,
            'ContactHistory': 0,
            'ContactHistoryEventType': 0,
            'ContentBodyType': 0,
            'Country': 239,
            'DEV_TestUtils': 0,
            'Department': 3,
            'Division': 0,
            'DocumentFile': 0,
            'DocumentObject': 2587,
            'DocumentObjectEventType': 9,
            'DocumentObjectHistory': 2,
            'DocumentObjectStats': 0,
            'DocumentObjectTags': 0,
            'DocumentObjectType': 0,
            'EmailAddress': 2012,
            'FamilyRoomLocation': 0,
            'Field': 0,
            'GarageLocation': 0,
            'GlobalSetting': 27,
            'HOUSE INFO': 0,
            'HOUSE INFO 1': 0,
            'HOUSE INFO 2': 0,
            'HomePlan': 0,
            'HomePlanCodeCompliance': 2498,
            'HomePlanHomeStyle': 2903,
            'HomePlanOption': 4,
            'HomePlanOptionChoice': 2,
            'HomeStyle': 22,
            'Keyword': 5,
            'Login': 0,
            'LoginRole': 32,
            'MainRoofType': 0,
            'Message': 1322,
            'MessageDocument': 0,
            'MessageProject': 1320,
            'MessageTask': 19,
            'MessageType': 0,
            'Mime': 1436,
            'Mode_Order': 0,
            'Mode_OrderItem': 0,
            'Mode_OrderType': 0,
            'NewsItem': 0,
            'NonPerson': 0,
            'NonPersonType': 0,
            'Operation': 13,
            'Order': 0,
            'OrderItem': 999,
            'Page': 0,
            'PagePagelet': 0,
            'Person': 0,
            'PersonAddress': 2560,
            'PersonCompany': 0,
            'PersonCompanyProjectRole': 5,
            'PersonCountry': 0,
            'PersonDocumentObject': 0,
            'PersonEmailAddress': 1922,
            'PersonPhone': 0,
            'PersonProject': 10760,
            'PersonTags': 0,
            'PersonTimeEvent': 0,
            'PersonWebRole': 0,
            'Phone': 6425,
            'PodColumn': 0,
            'Podlet': 0,
            'PodletField': 0,
            'PortalColumn': 3,
            'PortalPod': 24,
            'PortalPodPerson': 0,
            'PortalPodPodlet': 0,
            'PriceCode': 13,
            'PricePlan': 52,
            'Project': 0,
            'ProjectCObject': 2655,
            'ProjectCategory': 0,
            'ProjectComment': 0,
            'ProjectDerivation': 0,
            'ProjectDocumentObject': 2561,
            'ProjectPhase': 9155,
            'ProjectPhaseType': 0,
            'ProjectStatus': 0,
            'ProjectStatusType': 4,
            'ProjectType': 0,
            'ProjectTypeOperation': 0,
            'ProjectTypeRelease': 0,
            'ProjectionLocation': 4,
            'SaleType': 10,
            'StateProvince': 0,
            'Tags': 0,
            'Task': 12213,
            'TaskDocumentObject': 0,
            'TaskNotify': 0,
            'TaskSegment': 126301,
            'TaskSegmentCorrection': 0,
            'TeamMember': 20,
            'Ticket': 0,
            'TimeBracket': 0,
            'TimeBracketEvent': 0,
            'TimeEvent': 0,
            'TimeEventActionType': 0,
            'TimeEventHistory': 0,
            'TimeEventTrigger': 0,
            'TimeLineManager': 0,
            'Timeline': 0,
            'TimelineModelProject': 0,
            'TimelineType': 0,
            'Timesheet': 0,
            'TimesheetStatusType': 5,
            'TimesheetTaskSegment': 74253,
            'Topic': 0,
            'Trigger': 0,
            'TriggerType': 2,
            'UIElement': 0,
            'UIElementType': 0,
            'UI_Container': 0,
            'UI_Container2': 0,
            'UI_ContainerRelationship': 0,
            'UI_ContainerType': 0,
            'UI_ContainerTypePage': 0,
            'UI_ContainerTypePagelet': 0,
            'UI_ContainerTypePod': 0,
            'UI_ContainerTypePortal': 0,
            'UI_Field': 17,
            'UI_Form': 0,
            'UI_FormField': 0,
            'UI_Form_UI_FormField': 0,
            'UI_ListField': 6,
            'UI_ListTemplate': 0,
            'UI_Object': 0,
            'UI_Pagelet': 0,
            'UI_SearchForm': 1,
            'UI_SearchParameters': 0,
            'WebRole': 0,
            'WebStatusType': 4,
            'dtproperties': 0,
            'hpaadmin.check_sysuser': 0,
            'iLivError': 0,
            'personRate': 20
        }

    @Timer.decorator
    def test_diff_dict(self):
        uniques = diff(self.x, self.y)
        self.assertEqual(len(uniques), 18)

    @Timer.decorator
    def test_diff_dict_x_only(self):
        uniques = diff(self.x, self.y, x_only=True)
        self.assertEqual(len(uniques), 9)

    @Timer.decorator
    def test_diff_dict_y_only(self):
        uniques = diff(self.x, self.y, y_only=True)
        self.assertEqual(len(uniques), 9)


if __name__ == '__main__':
    unittest.main()
