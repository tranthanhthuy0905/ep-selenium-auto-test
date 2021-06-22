import unittest
import time
from tests.base_test import BaseTest
from pages.dashboard_page import DashboardPage
from pages.ec2_instances_page import EC2InstancesPage
from utils.locators import *


class TestInstances(BaseTest):
    def create_vm(self, vm):
        dashboard_page = DashboardPage(self.driver)
        ec2_page = dashboard_page.access_ec2_page()
        self.assertIn("/security_groups", ec2_page.get_url())
        ec2_instances_page = ec2_page.access_ec2_instances_page()
        self.assertIn("/security_groups/instances", ec2_instances_page.get_url())
        ec2_launch_instances_wizard_page = ec2_instances_page.access_launch_instances_wizard_page()
        self.assertIn("/security_groups/launch-instance-wizard", ec2_launch_instances_wizard_page.get_url())
        if vm:
            ec2_launch_instances_wizard_page \
                .choose_instance_details() \
                .create_volume('hahv3-test-volumne-01', '69') \
                .review_and_launch_intance()
        else:
            ec2_launch_instances_wizard_page \
                .choose_instance_details()\
                .review_and_launch_intance()
        return ec2_instances_page

    def test_b_create_vm_with_existed_hostname(self):
        ec2_instances_page = self.create_vm(False)
        ec2_instances_page.check_element_existence(EC2InstancePageLocators.ANNOUNCEMENT)
        ec2_instances_page.check_element_existence(EC2InstancePageLocators.LAUNCH_VM_ERROR_MESSAGE)

    def test_a_create_vm(self):
        ec2_instances_page = self.create_vm(True)
        ec2_instances_page.check_element_existence(EC2InstancePageLocators.ANNOUNCEMENT)
        ec2_instances_page.check_element_existence(EC2InstancePageLocators.LAUNCH_VM_SUCCESS_MESSAGE)

    def test_f_stop_instance(self):
        self.driver.get('https://console.engineering.vng.vn/ec2/instances')
        ec2_instances_page = EC2InstancesPage(self.driver)
        ec2_instances_page.change_instance_states(EC2InstancePageLocators.STOP_INSTANCE_BTN,
                                                  EC2InstancePageLocators.STOP_CONFIRM_BTN,
                                                  EC2InstancePageLocators.STOP_VM_SUCCESS_MESSAGE)

    def test_g_start_instance(self):
        self.driver.get('https://console.engineering.vng.vn/ec2/instances')
        ec2_instances_page = EC2InstancesPage(self.driver)
        ec2_instances_page.change_instance_states(EC2InstancePageLocators.START_INSTANCE_BTN,
                                                  EC2InstancePageLocators.START_CONFIRM_BTN,
                                                  EC2InstancePageLocators.START_VM_SUCCESS_MESSAGE)

    def test_h_reboot_instance(self):
        self.driver.get('https://console.engineering.vng.vn/ec2/instances')
        ec2_instances_page = EC2InstancesPage(self.driver)
        ec2_instances_page.change_instance_states(EC2InstancePageLocators.REBOOT_INSTANCE_BTN,
                                                  EC2InstancePageLocators.REBOOT_CONFIRM_BTN,
                                                  EC2InstancePageLocators.REBOOT_VM_SUCCESS_MESSAGE)

    def test_i_terminate_instance(self):
        self.driver.get('https://console.engineering.vng.vn/ec2/instances')
        ec2_instances_page = EC2InstancesPage(self.driver)
        ec2_instances_page.change_instance_states(EC2InstancePageLocators.TERMINATE_INSTANCE_BTN,
                                                  EC2InstancePageLocators.TERMINATE_CONFIRM_BTN,
                                                  None)

    def test_c_connect_vm(self):
        self.driver.get('https://console.engineering.vng.vn/ec2/instances')
        ec2_instances_page = EC2InstancesPage(self.driver)
        ec2_instances_page\
            .click_button(EC2InstancePageLocators.RADIO_BTN)\
            .click_button(EC2InstancePageLocators.CONNECT_BTN)

    def test_d_copy_instance_detail(self):
        self.driver.get('https://console.engineering.vng.vn/ec2/instances')
        ec2_instances_page = EC2InstancesPage(self.driver)
        ec2_instances_page \
            .click_button(EC2InstancePageLocators.RADIO_BTN)\
            .click_button(EC2InstancePageLocators.INSTANCE_VOLUME_TAB)\
            .click_button(EC2InstancePageLocators.DROP_DOWN_LIST_BTN)\
            .click_button(EC2InstancePageLocators.COPY)

    def test_e_show_instance_types(self):
        dashboard_page = DashboardPage(self.driver)
        ec2_page = dashboard_page.access_ec2_page()
        self.assertIn("/security_groups", ec2_page.get_url())
        instance_types_page = ec2_page.access_ec2_instance_types_page()
        self.assertIn("/security_groups/instances/types", instance_types_page.get_url())
        instance_types_page\
            .click_button(EC2InstanceTypesPageLocators.INTANCE_TYPE_4G_RADIO) \
            .click_button(EC2InstanceTypesPageLocators.INTANCE_TYPE_32G_RADIO) \
            .click_button(EC2InstanceTypesPageLocators.MEMORY_SORTER)\
            .click_button(EC2InstanceTypesPageLocators.COPY) \
            .check_element_existence(EC2InstanceTypesPageLocators.COPY_CLIPBOARD_SUCCESS_MESSAGE)

    def test_k_expunge_volume(self):
        dashboard_page = DashboardPage(self.driver)
        ec2_page = dashboard_page.access_ec2_page()
        self.assertIn("/security_groups", ec2_page.get_url())
        time.sleep(2)
        elastic_block_store_volumnes_page = ec2_page.access_ec2_elastic_block_store_volumnes_page()
        self.assertIn("/security_groups/elastic-block-store/volumes", elastic_block_store_volumnes_page.get_url())
        time.sleep(2)
        elastic_block_store_volumnes_page\
            .click_button(EC2ElasticBlockStoreVolumnePageLocators.CHOOSE_VOLUMNE_RADIO)\
            .click_button(EC2ElasticBlockStoreVolumnePageLocators.VOLUME_ACTIONS_BTN)\
            .click_button(EC2ElasticBlockStoreVolumnePageLocators.EXPUNGE_VOLUME_BTN)\
            .wait_and_click_button(EC2ElasticBlockStoreVolumnePageLocators.EXPUNGE_VOLUME_CONFIRM_BTN)\
            .check_element_existence(EC2ElasticBlockStoreVolumnePageLocators.CREATE_VOLUMNE_SUCCESS_MESSAGE)
