from cloudshell.devices.flows.action_flows import RestoreConfigurationFlow
from cloudshell.networking.arista.command_actions.system_actions import SystemActions


class AristaRestoreFlow(RestoreConfigurationFlow):

    def execute_flow(self, path, configuration_type, restore_method, vrf_management_name):
        """ Execute flow which save selected file to the provided destination

        :param path: the path to the configuration file, including the configuration file name
        :param restore_method: the restore method to use when restoring the configuration file.
                               Possible Values are append and override
        :param configuration_type: the configuration type to restore. Possible values are startup and running
        :param vrf_management_name: Virtual Routing and Forwarding Name
        """

        if '-config' not in configuration_type:
            configuration_type += '-config'

        with self._cli_handler.get_cli_service(self._cli_handler.enable_mode) as enable_session:
            restore_action = SystemActions(enable_session, self._logger)
            copy_action_map = restore_action.prepare_action_map(path, configuration_type)

            if 'running' in configuration_type and restore_method == 'override':
                restore_action.override_running(path)
            else:
                restore_action.copy(
                    path, configuration_type, vrf_management_name, action_map=copy_action_map)
