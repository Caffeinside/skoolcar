from .ansible_test_infra_case import AnsibleTestInfraCase


class TestScripts(AnsibleTestInfraCase):

    def test_localadmin_can_run_aivi_scripts(self):
        """aivi service should be running before and after this test"""

        for script_path in ["/opt/aivi/bin/aivi.sh", "/opt/aivi/bin/basler-configurator.sh"]:
            # Given
            script = self.edge_station.file(script_path)
            expected_permissions = 0o755

            # Then
            assert script.exists
            assert script.is_file
            assert script.user == "aivid"
            assert script.mode == expected_permissions
