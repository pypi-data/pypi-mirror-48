import logging

import requests

logger = logging.getLogger(__name__)


class VMwareClient(object):
    """
    Lightweight VMware vCenter Automation API client.
    See also: https://code.vmware.com/apis/191/vsphere-automation
    """

    def __init__(self, host, verify_ssl=True):
        """
        Initialize client with connection options.

        :param host: VMware vCenter server IP address / FQDN
        :type host: string
        :param verify_ssl: verify SSL certificates for HTTPS requests
        :type verify_ssl: bool
        """
        self._host = host
        self._base_url = 'https://{0}/rest'.format(self._host)
        self._session = requests.Session()
        self._session.verify = verify_ssl

    def _get(self, endpoint):
        url = '%s/%s' % (self._base_url, endpoint)
        response = self._session.get(url)
        response.raise_for_status()
        if response.content:
            return response.json()

    def _post(self, endpoint, **kwargs):
        url = '%s/%s' % (self._base_url, endpoint)
        response = self._session.post(url, **kwargs)
        response.raise_for_status()
        if response.content:
            return response.json()

    def _patch(self, endpoint, **kwargs):
        url = '%s/%s' % (self._base_url, endpoint)
        response = self._session.patch(url, **kwargs)
        response.raise_for_status()
        if response.content:
            return response.json()

    def _delete(self, endpoint):
        url = '%s/%s' % (self._base_url, endpoint)
        response = self._session.delete(url)
        response.raise_for_status()
        if response.content:
            return response.json()

    def login(self, username, password):
        """
        Login to vCenter server using username and password.

        :param username: user to connect
        :type username: string
        :param password: password of the user
        :type password: string
        :raises Unauthorized: raised if credentials are invalid.
        """
        self._post('com/vmware/cis/session', auth=(username, password))
        logger.info('Successfully logged in as {0}'.format(username))

    def list_clusters(self):
        return self._get('vcenter/cluster')['value']

    def list_datacenters(self):
        return self._get('vcenter/datacenter')['value']

    def list_datastores(self):
        return self._get('vcenter/datastore')['value']

    def list_folders(self):
        return self._get('vcenter/folder')['value']

    def list_vms(self):
        """
        Get all the VMs from vCenter inventory.
        """
        return self._get('vcenter/vm')['value']

    def get_vm(self, vm_id):
        """
        Returns information about a virtual machine.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        """
        return self._get('vcenter/vm/{}'.format(vm_id))['value']

    def create_vm(self, spec):
        """
        Creates a virtual machine.

        :param spec: new virtual machine specification
        :type spec: dict
        :return: Virtual machine identifier
        :rtype: string
        """
        return self._post('vcenter/vm', json=spec)['value']

    def delete_vm(self, vm_id):
        """
        Deletes a virtual machine.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        """
        return self._delete('vcenter/vm/{}'.format(vm_id))

    def start_vm(self, vm_id):
        """
        Power on given virtual machine.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        """
        return self._post('vcenter/vm/{}/power/start'.format(vm_id))

    def stop_vm(self, vm_id):
        """
        Power off given virtual machine.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        """
        return self._post('vcenter/vm/{}/power/stop'.format(vm_id))

    def reset_vm(self, vm_id):
        """
        Resets a powered-on virtual machine.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        """
        return self._post('vcenter/vm/{}/power/reset'.format(vm_id))

    def suspend_vm(self, vm_id):
        """
        Suspends a powered-on virtual machine.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        """
        return self._post('vcenter/vm/{}/power/suspend'.format(vm_id))

    def update_cpu(self, vm_id, spec):
        """
        Updates the CPU-related settings of a virtual machine.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        :param spec: CPU specification
        :type spec: dict
        """
        return self._patch('vcenter/vm/{}/hardware/cpu'.format(vm_id), json=spec)

    def update_memory(self, vm_id, spec):
        """
        Updates the memory-related settings of a virtual machine.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        :param spec: CPU specification
        :type spec: dict
        """
        return self._patch('vcenter/vm/{}/hardware/memory'.format(vm_id), json=spec)

    def create_disk(self, vm_id, spec):
        """
        Adds a virtual disk to the virtual machine

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        :param spec: new virtual disk specification
        :type spec: dict
        """
        return self._post('vcenter/vm/{}/hardware/disk'.format(vm_id), json=spec)

    def delete_disk(self, vm_id, disk_id):
        """
        Removes a virtual disk from the virtual machine.
        This operation does not destroy the VMDK file that backs the virtual disk.
        It only detaches the VMDK file from the virtual machine.
        Once detached, the VMDK file will not be destroyed when the virtual machine
        to which it was associated is deleted.

        :param vm_id: Virtual machine identifier.
        :type vm_id: string
        :param disk_id: Virtual disk identifier.
        :type disk_id: string
        """
        return self._delete('vcenter/vm/{}/hardware/disk/{}'.format(vm_id, disk_id))

    def connect_cdrom(self, vm_id, cdrom_id):
        """
        Connects a virtual CD-ROM device of a powered-on virtual machine to its backing.

        :param vm_id: Virtual machine identifier
        :type vm_id: string
        :param cdrom_id: Virtual CD-ROM device identifier.
        :type cdrom_id: string
        """
        return self._post('vcenter/vm/{}/hardware/cdrom/{}/connect'.format(vm_id, cdrom_id))

    def disconnect_cdrom(self, vm_id, cdrom_id):
        """
        Disconnects a virtual CD-ROM device of a powered-on virtual machine from its backing.

        :param vm_id: Virtual machine identifier.
        :type vm_id: string
        :param cdrom_id: Virtual CD-ROM device identifier.
        :type cdrom_id: string
        """
        return self._post('vcenter/vm/{}/hardware/cdrom/{}/disconnect'.format(vm_id, cdrom_id))

    def connect_nic(self, vm_id, nic_id):
        """
        Connects a virtual Ethernet adapter of a powered-on virtual machine to its backing.

        :param vm_id: Virtual machine identifier.
        :type vm_id: string
        :param nic_id: Virtual Ethernet adapter identifier.
        :type nic_id: string
        """
        return self._post('vcenter/vm/{}/hardware/ethernet/{}/connect'.format(vm_id, nic_id))

    def disconnect_nic(self, vm_id, nic_id):
        """
        Disconnects a virtual Ethernet adapter of a powered-on virtual machine from its backing.

        :param vm_id: Virtual machine identifier.
        :type vm_id: string
        :param nic_id: Virtual Ethernet adapter identifier.
        :type nic_id: string
        """
        return self._post('vcenter/vm/{}/hardware/ethernet/{}/disconnect'.format(vm_id, nic_id))
