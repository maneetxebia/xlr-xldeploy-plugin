#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from xldeploy.XLDeployClientUtil import XLDeployClientUtil

xld_client = XLDeployClientUtil.create_xldeploy_client(xldeployServer, username, password)

try:
	throwOnFail
except:
	throwOnFail = False
	
try:
    response = xld_client.check_ci_exist(applicationId)
except:
	response = False

if throwOnFail and not response:
	raise Exception(applicationId + " does not exist")

packageId = xld_client.get_latest_package_version(applicationId)

if stripApplications:
    packageId = packageId.partition('/')[2]

if throwOnFail and packageId == "":
	raise Exception(applicationId + " exists but has no versions")
